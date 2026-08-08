from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone

from seed_data import SEED_PRODUCTS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

mongo_url = os.environ["MONGO_URL"]
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ["DB_NAME"]]

app = FastAPI(title="Billy's Store API")
api_router = APIRouter(prefix="/api")

# Import admin router AFTER db is defined
from admin import router as admin_router, hash_password, ADMIN_EMAIL, ADMIN_PASSWORD, initialize_flutterwave_payment, FLW_SECRET_KEY, decrement_stock, send_order_confirmation_email

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# ---------- Models ----------
class Variant(BaseModel):
    sizes: List[str] = []
    colors: List[dict] = []  # {name, hex}
    materials: List[str] = []


class Review(BaseModel):
    author: str
    rating: int
    date: str
    title: str
    body: str
    photo: Optional[str] = None


class Product(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    name_fr: str
    name_en: str
    slug: str
    category: str  # jewelry | men | women | kids
    subcategory: str
    price: float
    compare_at: Optional[float] = None
    currency: str = "USD"
    images: List[str]
    description_fr: str
    description_en: str
    composition_fr: str
    composition_en: str
    variants: Variant = Field(default_factory=Variant)
    rating: float = 4.6
    reviews_count: int = 0
    reviews: List[Review] = []
    stock: int = 25
    badges: List[str] = []  # new | bestseller | soldout
    created_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class OrderItem(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int
    size: Optional[str] = None
    color: Optional[str] = None
    image: Optional[str] = None


class Contact(BaseModel):
    email: EmailStr
    phone: str
    first_name: str
    last_name: str


class ShippingAddress(BaseModel):
    address: str
    city: str
    postal_code: str
    country: str


class OrderCreate(BaseModel):
    contact: Contact
    shipping: ShippingAddress
    payment_method: str  # orange_money | mtn_momo | wave | moov | flutterwave
    payment_phone: Optional[str] = ""
    items: List[OrderItem]
    subtotal: float
    shipping_cost: float
    total: float
    promo_code: Optional[str] = None
    discount: float = 0


class Order(OrderCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    status: str = "pending"
    order_number: str = Field(
        default_factory=lambda: "BS-" + uuid.uuid4().hex[:8].upper()
    )
    tx_ref: str = Field(default_factory=lambda: f"billy-{uuid.uuid4().hex[:16]}")
    payment_link: Optional[str] = None
    flutterwave_transaction_id: Optional[str] = None
    created_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


# ---------- Utils ----------
def clean_doc(doc: dict) -> dict:
    doc.pop("_id", None)
    return doc


# ---------- Routes ----------
@api_router.get("/")
async def root():
    return {"message": "Billy's Store API", "status": "ok"}


@api_router.get("/categories")
async def get_categories():
    return [
        {
            "slug": "jewelry",
            "name_fr": "Bijoux & Accessoires",
            "name_en": "Jewelry & Accessories",
            "hero": "https://images.unsplash.com/photo-1625516152414-8f33eef3d660?crop=entropy&cs=srgb&fm=jpg&q=85",
        },
        {
            "slug": "women",
            "name_fr": "Mode Femme",
            "name_en": "Women",
            "hero": "https://images.unsplash.com/photo-1613915617430-8ab0fd7c6baf?crop=entropy&cs=srgb&fm=jpg&q=85",
        },
        {
            "slug": "men",
            "name_fr": "Mode Homme",
            "name_en": "Men",
            "hero": "https://images.unsplash.com/photo-1619603364937-8d7af41ef206?crop=entropy&cs=srgb&fm=jpg&q=85",
        },
        {
            "slug": "kids",
            "name_fr": "Mode Enfant",
            "name_en": "Kids",
            "hero": "https://images.unsplash.com/photo-1724365309223-89899d9e9845?crop=entropy&cs=srgb&fm=jpg&q=85",
        },
    ]


@api_router.get("/products", response_model=List[Product])
async def list_products(
    category: Optional[str] = None,
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    size: Optional[str] = None,
    color: Optional[str] = None,
    availability: Optional[str] = None,  # in_stock | out_of_stock
    sort: Optional[str] = "newest",  # newest | price_asc | price_desc | bestseller
    limit: int = 100,
):
    q: dict = {}
    if category and category != "all":
        q["category"] = category
    if min_price is not None:
        q.setdefault("price", {})["$gte"] = min_price
    if max_price is not None:
        q.setdefault("price", {})["$lte"] = max_price
    if size:
        q["variants.sizes"] = size
    if color:
        q["variants.colors.name"] = color
    if availability == "in_stock":
        q["stock"] = {"$gt": 0}
    if availability == "out_of_stock":
        q["stock"] = 0
    if search:
        rx = {"$regex": search, "$options": "i"}
        q["$or"] = [
            {"name_fr": rx},
            {"name_en": rx},
            {"subcategory": rx},
            {"description_en": rx},
            {"description_fr": rx},
        ]

    sort_map = {
        "newest": [("created_at", -1)],
        "price_asc": [("price", 1)],
        "price_desc": [("price", -1)],
        "bestseller": [("reviews_count", -1), ("rating", -1)],
    }
    cursor = db.products.find(q, {"_id": 0}).sort(sort_map.get(sort, sort_map["newest"])).limit(limit)
    docs = await cursor.to_list(limit)
    return [Product(**d) for d in docs]


@api_router.get("/products/suggest")
async def suggest(q: str = Query(..., min_length=1)):
    rx = {"$regex": q, "$options": "i"}
    docs = await db.products.find(
        {"$or": [{"name_fr": rx}, {"name_en": rx}, {"subcategory": rx}]},
        {"_id": 0, "id": 1, "name_fr": 1, "name_en": 1, "slug": 1, "images": 1, "price": 1, "category": 1},
    ).limit(6).to_list(6)
    return docs


@api_router.get("/products/{slug}", response_model=Product)
async def get_product(slug: str):
    doc = await db.products.find_one({"slug": slug}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**doc)


@api_router.get("/products/{slug}/related", response_model=List[Product])
async def related_products(slug: str, limit: int = 4):
    current = await db.products.find_one({"slug": slug}, {"_id": 0})
    if not current:
        raise HTTPException(status_code=404, detail="Product not found")
    docs = await db.products.find(
        {"category": current["category"], "slug": {"$ne": slug}}, {"_id": 0}
    ).limit(limit).to_list(limit)
    return [Product(**d) for d in docs]


@api_router.post("/orders", response_model=Order)
async def create_order(payload: OrderCreate):
    order = Order(**payload.model_dump())
    doc = order.model_dump()

    # 1. Decrement stock atomically (rolls back on failure)
    items_dicts = [i.model_dump() for i in payload.items]
    fail_name = await decrement_stock(items_dicts)
    if fail_name:
        raise HTTPException(status_code=409, detail=f"Insufficient stock for: {fail_name}")

    try:
        # 2. If payment method is 'flutterwave', initialize hosted checkout
        if payload.payment_method == "flutterwave":
            if not FLW_SECRET_KEY:
                raise HTTPException(
                    status_code=503,
                    detail="Flutterwave not configured. Set FLW_SECRET_KEY in backend/.env",
                )
            link = await initialize_flutterwave_payment(doc)
            doc["payment_link"] = link
            order.payment_link = link
        else:
            # Non-Flutterwave (Mobile Money manual) orders are considered "committed" — bump promo usage
            if payload.promo_code:
                await db.promos.update_one(
                    {"code": payload.promo_code}, {"$inc": {"uses": 1}}
                )

        await db.orders.insert_one(doc)
    except HTTPException:
        # Restore stock if Flutterwave init failed
        from admin import restore_stock
        await restore_stock(items_dicts)
        raise

    # 3. Send email for non-Flutterwave orders (fire and forget)
    if payload.payment_method != "flutterwave":
        try:
            await send_order_confirmation_email(doc, lang="fr")
        except Exception as e:
            logger.warning(f"Email send failed: {e}")

    return order


@api_router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str):
    doc = await db.orders.find_one({"id": order_id}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Order not found")
    return Order(**doc)


# ---------- Startup: seed products + admin ----------
@app.on_event("startup")
async def seed_startup():
    count = await db.products.count_documents({})
    if count == 0:
        await db.products.insert_many([p.copy() for p in SEED_PRODUCTS])
        logger.info(f"Seeded {len(SEED_PRODUCTS)} products")
    else:
        logger.info(f"Products already seeded ({count} exist)")

    # Seed default admin
    existing_admin = await db.admin_users.find_one({"email": ADMIN_EMAIL.lower()})
    if not existing_admin:
        from admin import ROLE_SUPER
        admin_doc = {
            "user_id": f"user_{uuid.uuid4().hex[:12]}",
            "email": ADMIN_EMAIL.lower(),
            "password_hash": hash_password(ADMIN_PASSWORD),
            "name": "Billy Admin",
            "picture": None,
            "role": ROLE_SUPER,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        await db.admin_users.insert_one(admin_doc)
        logger.info(f"Seeded default admin: {ADMIN_EMAIL}")
    else:
        # Ensure existing admin has a role assigned (idempotent migration)
        if not existing_admin.get("role"):
            from admin import ROLE_SUPER
            await db.admin_users.update_one(
                {"email": ADMIN_EMAIL.lower()}, {"$set": {"role": ROLE_SUPER}}
            )
    # Indexes
    await db.orders.create_index("tx_ref", unique=True, sparse=True)
    await db.promos.create_index("code", unique=True)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


app.include_router(api_router)
app.include_router(admin_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)
