"""Auth + admin + promo + payments module for Billy's Store."""
import os
import uuid
import hashlib
import hmac
from datetime import datetime, timezone, timedelta
from typing import Optional, List

import bcrypt
import jwt
import httpx
from fastapi import APIRouter, HTTPException, Request, Response, Header, Depends
from pydantic import BaseModel, Field, EmailStr, ConfigDict

JWT_SECRET = os.environ.get("JWT_SECRET", "dev-secret")
JWT_ALGO = "HS256"
JWT_EXPIRE_HOURS = 24 * 7  # 7 days
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "admin@billystore.com")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Billy2026!Admin")

FLW_SECRET_KEY = os.environ.get("FLW_SECRET_KEY", "")
FLW_SECRET_HASH = os.environ.get("FLW_SECRET_HASH", "")
FLW_CURRENCY = os.environ.get("FLW_CURRENCY", "XOF")
PUBLIC_BACKEND_URL = os.environ.get("PUBLIC_BACKEND_URL", "")
PUBLIC_FRONTEND_URL = os.environ.get("PUBLIC_FRONTEND_URL", "")

EMERGENT_AUTH_URL = "https://demobackend.emergentagent.com/auth/v1/env/oauth/session-data"


# ---------- Auth Utils ----------
def hash_password(pw: str) -> str:
    return bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(pw: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(pw.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False


def make_jwt(sub: str, email: str) -> str:
    payload = {
        "sub": sub,
        "email": email,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRE_HOURS),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)


def decode_jwt(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
    except Exception:
        return None


class AdminUser(BaseModel):
    model_config = ConfigDict(extra="ignore")

    user_id: str
    email: str
    name: str
    picture: Optional[str] = None
    auth_type: str  # "jwt" | "google"


async def get_current_admin(
    request: Request,
    authorization: Optional[str] = Header(None),
) -> AdminUser:
    """Extract admin from JWT header OR Emergent session cookie."""
    from server import db  # circular-safe

    # 1. JWT Bearer
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.replace("Bearer ", "").strip()

    if token:
        payload = decode_jwt(token)
        if payload:
            user_doc = await db.admin_users.find_one(
                {"user_id": payload["sub"]}, {"_id": 0}
            )
            if user_doc:
                return AdminUser(**user_doc, auth_type="jwt")

    # 2. Emergent session cookie
    session_token = request.cookies.get("session_token")
    if not session_token and authorization and not authorization.startswith("Bearer "):
        session_token = authorization

    if session_token:
        sess = await db.admin_sessions.find_one({"session_token": session_token}, {"_id": 0})
        if sess:
            expires_at = sess["expires_at"]
            if isinstance(expires_at, str):
                expires_at = datetime.fromisoformat(expires_at)
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=timezone.utc)
            if expires_at > datetime.now(timezone.utc):
                user_doc = await db.admin_users.find_one(
                    {"user_id": sess["user_id"]}, {"_id": 0}
                )
                if user_doc:
                    return AdminUser(**user_doc, auth_type="google")

    raise HTTPException(status_code=401, detail="Not authenticated")


# ---------- Router ----------
router = APIRouter()


# ============== AUTH ==============
class LoginPayload(BaseModel):
    email: EmailStr
    password: str


@router.post("/auth/login")
async def login_jwt(payload: LoginPayload):
    from server import db

    user = await db.admin_users.find_one({"email": payload.email.lower()}, {"_id": 0})
    if not user or not verify_password(payload.password, user.get("password_hash", "")):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = make_jwt(user["user_id"], user["email"])
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "user_id": user["user_id"],
            "email": user["email"],
            "name": user["name"],
            "picture": user.get("picture"),
        },
    }


class GoogleSessionPayload(BaseModel):
    session_id: str


@router.post("/auth/google-session")
async def google_session(payload: GoogleSessionPayload, response: Response):
    """Exchange Emergent session_id for our own session_token cookie."""
    from server import db

    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(
            EMERGENT_AUTH_URL,
            headers={"X-Session-ID": payload.session_id},
        )
    if r.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid Emergent session")
    data = r.json()
    email = data["email"].lower()

    # Only allow the configured admin email (or any email if you want to open it up).
    # For a single-admin app, restrict to ADMIN_EMAIL.
    if email != ADMIN_EMAIL.lower():
        raise HTTPException(
            status_code=403,
            detail=f"Access restricted to {ADMIN_EMAIL}",
        )

    user_doc = await db.admin_users.find_one({"email": email}, {"_id": 0})
    if not user_doc:
        user_id = f"user_{uuid.uuid4().hex[:12]}"
        user_doc = {
            "user_id": user_id,
            "email": email,
            "name": data.get("name", email),
            "picture": data.get("picture"),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        await db.admin_users.insert_one(user_doc.copy())
    else:
        await db.admin_users.update_one(
            {"user_id": user_doc["user_id"]},
            {"$set": {"picture": data.get("picture"), "name": data.get("name", user_doc.get("name"))}},
        )

    session_token = data["session_token"]
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    await db.admin_sessions.insert_one(
        {
            "session_token": session_token,
            "user_id": user_doc["user_id"],
            "expires_at": expires_at.isoformat(),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
    )

    response.set_cookie(
        key="session_token",
        value=session_token,
        max_age=7 * 24 * 60 * 60,
        httponly=True,
        secure=True,
        samesite="none",
        path="/",
    )
    return {
        "user": {
            "user_id": user_doc["user_id"],
            "email": user_doc["email"],
            "name": user_doc["name"],
            "picture": user_doc.get("picture"),
        }
    }


@router.get("/auth/me")
async def auth_me(admin: AdminUser = Depends(get_current_admin)):
    return {
        "user_id": admin.user_id,
        "email": admin.email,
        "name": admin.name,
        "picture": admin.picture,
        "auth_type": admin.auth_type,
    }


@router.post("/auth/logout")
async def logout(request: Request, response: Response):
    from server import db

    session_token = request.cookies.get("session_token")
    if session_token:
        await db.admin_sessions.delete_one({"session_token": session_token})
    response.delete_cookie("session_token", path="/")
    return {"ok": True}


# ============== ADMIN PRODUCTS ==============
class ProductUpsert(BaseModel):
    id: Optional[str] = None
    name_fr: str
    name_en: str
    slug: str
    category: str
    subcategory: str
    price: float
    compare_at: Optional[float] = None
    currency: str = "USD"
    images: List[str]
    description_fr: str = ""
    description_en: str = ""
    composition_fr: str = ""
    composition_en: str = ""
    variants: dict = Field(default_factory=lambda: {"sizes": [], "colors": [], "materials": []})
    rating: float = 4.6
    reviews_count: int = 0
    reviews: List[dict] = Field(default_factory=list)
    stock: int = 25
    badges: List[str] = Field(default_factory=list)


@router.post("/admin/products")
async def admin_create_product(payload: ProductUpsert, admin: AdminUser = Depends(get_current_admin)):
    from server import db

    doc = payload.model_dump()
    doc["id"] = doc.get("id") or str(uuid.uuid4())
    doc["created_at"] = datetime.now(timezone.utc).isoformat()
    existing = await db.products.find_one({"slug": doc["slug"]})
    if existing:
        raise HTTPException(status_code=400, detail="Slug already exists")
    await db.products.insert_one(doc)
    doc.pop("_id", None)
    return doc


@router.put("/admin/products/{slug}")
async def admin_update_product(slug: str, payload: ProductUpsert, admin: AdminUser = Depends(get_current_admin)):
    from server import db

    doc = payload.model_dump(exclude={"id"})
    result = await db.products.update_one({"slug": slug}, {"$set": doc})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    updated = await db.products.find_one({"slug": doc["slug"]}, {"_id": 0})
    return updated


@router.delete("/admin/products/{slug}")
async def admin_delete_product(slug: str, admin: AdminUser = Depends(get_current_admin)):
    from server import db

    r = await db.products.delete_one({"slug": slug})
    if r.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"ok": True}


# ============== ADMIN ORDERS ==============
@router.get("/admin/orders")
async def admin_list_orders(admin: AdminUser = Depends(get_current_admin), limit: int = 200):
    from server import db

    docs = await db.orders.find({}, {"_id": 0}).sort("created_at", -1).limit(limit).to_list(limit)
    return docs


@router.patch("/admin/orders/{order_id}/status")
async def admin_update_order_status(order_id: str, body: dict, admin: AdminUser = Depends(get_current_admin)):
    from server import db

    new_status = body.get("status")
    if new_status not in ("pending", "paid", "shipped", "delivered", "cancelled", "failed"):
        raise HTTPException(status_code=400, detail="Invalid status")
    r = await db.orders.update_one({"id": order_id}, {"$set": {"status": new_status}})
    if r.matched_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"ok": True}


# ============== PROMO CODES ==============
class PromoUpsert(BaseModel):
    code: str
    kind: str  # "percent" | "fixed"
    value: float
    min_subtotal: float = 0
    category: Optional[str] = None  # jewelry | women | men | kids | None(=all)
    expires_at: Optional[str] = None  # ISO date
    max_uses: Optional[int] = None
    active: bool = True


@router.get("/admin/promos")
async def admin_list_promos(admin: AdminUser = Depends(get_current_admin)):
    from server import db

    docs = await db.promos.find({}, {"_id": 0}).sort("created_at", -1).to_list(200)
    return docs


@router.post("/admin/promos")
async def admin_create_promo(payload: PromoUpsert, admin: AdminUser = Depends(get_current_admin)):
    from server import db

    doc = payload.model_dump()
    doc["code"] = doc["code"].upper().strip()
    if await db.promos.find_one({"code": doc["code"]}):
        raise HTTPException(status_code=400, detail="Code already exists")
    doc["id"] = str(uuid.uuid4())
    doc["uses"] = 0
    doc["created_at"] = datetime.now(timezone.utc).isoformat()
    await db.promos.insert_one(doc)
    doc.pop("_id", None)
    return doc


@router.delete("/admin/promos/{code}")
async def admin_delete_promo(code: str, admin: AdminUser = Depends(get_current_admin)):
    from server import db

    r = await db.promos.delete_one({"code": code.upper()})
    if r.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Promo not found")
    return {"ok": True}


class ApplyPromoPayload(BaseModel):
    code: str
    subtotal: float
    category_totals: dict = Field(default_factory=dict)  # {"women": 120.0, "jewelry": 80.0}


@router.post("/promos/apply")
async def apply_promo(payload: ApplyPromoPayload):
    """Public endpoint - validates promo and returns discount."""
    from server import db

    code = payload.code.upper().strip()
    promo = await db.promos.find_one({"code": code}, {"_id": 0})
    if not promo:
        raise HTTPException(status_code=404, detail="Promo not found")
    if not promo.get("active", True):
        raise HTTPException(status_code=400, detail="Promo inactive")
    if promo.get("expires_at"):
        exp = datetime.fromisoformat(promo["expires_at"].replace("Z", "+00:00")) if isinstance(promo["expires_at"], str) else promo["expires_at"]
        if exp.tzinfo is None:
            exp = exp.replace(tzinfo=timezone.utc)
        if exp < datetime.now(timezone.utc):
            raise HTTPException(status_code=400, detail="Promo expired")
    if promo.get("max_uses") is not None and promo.get("uses", 0) >= promo["max_uses"]:
        raise HTTPException(status_code=400, detail="Promo usage limit reached")

    # Category-scoped promo — check base amount
    if promo.get("category"):
        base = payload.category_totals.get(promo["category"], 0)
    else:
        base = payload.subtotal

    if base < promo.get("min_subtotal", 0):
        raise HTTPException(
            status_code=400,
            detail=f"Minimum subtotal is {promo['min_subtotal']}",
        )

    if promo["kind"] == "percent":
        discount = round(base * promo["value"] / 100, 2)
    else:
        discount = min(promo["value"], base)

    return {
        "code": promo["code"],
        "discount": discount,
        "kind": promo["kind"],
        "value": promo["value"],
        "category": promo.get("category"),
    }


# ============== FLUTTERWAVE PAYMENTS ==============
async def _flw_verify(transaction_id: str) -> dict:
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(
            f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify",
            headers={"Authorization": f"Bearer {FLW_SECRET_KEY}"},
        )
    r.raise_for_status()
    return r.json()


async def initialize_flutterwave_payment(order: dict) -> str:
    """Return payment_link URL. Order must have tx_ref, total, contact.email, contact.first_name."""
    if not FLW_SECRET_KEY:
        raise HTTPException(
            status_code=503,
            detail="Flutterwave not configured — set FLW_SECRET_KEY in backend/.env",
        )
    payload = {
        "tx_ref": order["tx_ref"],
        "amount": float(order["total"]),
        "currency": FLW_CURRENCY,
        "redirect_url": f"{PUBLIC_FRONTEND_URL}/payment/result",
        "customer": {
            "email": order["contact"]["email"],
            "name": f"{order['contact']['first_name']} {order['contact']['last_name']}",
            "phonenumber": order["contact"].get("phone", ""),
        },
        "customizations": {
            "title": "Billy's Store",
            "description": f"Order {order.get('order_number', order['tx_ref'])}",
        },
        "meta": {"order_id": order["id"]},
    }
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.post(
            "https://api.flutterwave.com/v3/payments",
            json=payload,
            headers={
                "Authorization": f"Bearer {FLW_SECRET_KEY}",
                "Content-Type": "application/json",
            },
        )
    if r.status_code >= 400:
        raise HTTPException(status_code=502, detail=f"Flutterwave error: {r.text[:200]}")
    data = r.json()
    link = data.get("data", {}).get("link")
    if not link:
        raise HTTPException(status_code=502, detail="Flutterwave returned no payment link")
    return link


async def finalize_flw_payment(tx_ref: str, transaction_id: str) -> str:
    from server import db

    order = await db.orders.find_one({"tx_ref": tx_ref}, {"_id": 0})
    if not order:
        return "unknown"
    if order.get("status") == "paid":
        return "paid"

    verified = await _flw_verify(transaction_id)
    data = verified.get("data", {})
    successful = data.get("status") in ("successful", "succeeded")
    amount_ok = float(data.get("amount", 0)) == float(order["total"])
    currency_ok = data.get("currency") == FLW_CURRENCY
    ref_ok = data.get("tx_ref") == tx_ref

    new_status = "paid" if (successful and amount_ok and currency_ok and ref_ok) else "failed"
    await db.orders.update_one(
        {"tx_ref": tx_ref, "status": {"$ne": "paid"}},
        {
            "$set": {
                "status": new_status,
                "flutterwave_transaction_id": str(transaction_id),
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }
        },
    )

    # Increment promo uses if applicable
    if new_status == "paid" and order.get("promo_code"):
        await db.promos.update_one(
            {"code": order["promo_code"]}, {"$inc": {"uses": 1}}
        )
    return new_status


@router.get("/payments/verify/{tx_ref}")
async def verify_payment(tx_ref: str, transaction_id: str):
    """Called by frontend after Flutterwave redirect."""
    status = await finalize_flw_payment(tx_ref, transaction_id)
    from server import db
    order = await db.orders.find_one({"tx_ref": tx_ref}, {"_id": 0})
    return {"status": status, "order": order}


@router.post("/payments/flutterwave/webhook")
async def flutterwave_webhook(request: Request):
    raw = await request.body()
    signature = request.headers.get("flutterwave-signature")
    legacy_hash = request.headers.get("verif-hash")

    if not FLW_SECRET_HASH:
        raise HTTPException(status_code=503, detail="Webhook not configured")

    expected = hmac.new(FLW_SECRET_HASH.encode(), raw, hashlib.sha256).hexdigest()
    current_valid = bool(signature) and hmac.compare_digest(signature, expected)
    legacy_valid = bool(legacy_hash) and hmac.compare_digest(legacy_hash, FLW_SECRET_HASH)
    if not (current_valid or legacy_valid):
        raise HTTPException(status_code=401, detail="Invalid signature")

    payload = await request.json()
    data = payload.get("data", {})
    tx_ref = data.get("tx_ref") or data.get("reference")
    transaction_id = data.get("id") or data.get("transaction_id")
    if tx_ref and transaction_id:
        await finalize_flw_payment(tx_ref, str(transaction_id))
    return {"received": True}
