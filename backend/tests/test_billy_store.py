"""Billy's Store — iteration 2 backend regression tests.
Covers: JWT auth, admin products/orders/promos, promo apply, Flutterwave 503 guard.
"""
import os
import uuid
import pytest
import requests
from datetime import datetime, timezone, timedelta

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://billy-shop.preview.emergentagent.com").rstrip("/")
API = f"{BASE_URL}/api"

ADMIN_EMAIL = "admin@billystore.com"
ADMIN_PASSWORD = "Billy2026!Admin"


# ---------- Fixtures ----------
@pytest.fixture(scope="session")
def api_client():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s


@pytest.fixture(scope="session")
def admin_token(api_client):
    r = api_client.post(f"{API}/auth/login", json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD})
    assert r.status_code == 200, f"login failed: {r.status_code} {r.text}"
    return r.json()["access_token"]


@pytest.fixture(scope="session")
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}", "Content-Type": "application/json"}


# ---------- Health / root ----------
def test_root(api_client):
    r = api_client.get(f"{API}/")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


# ---------- Auth ----------
class TestAuth:
    def test_login_success(self, api_client):
        r = api_client.post(f"{API}/auth/login", json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD})
        assert r.status_code == 200
        data = r.json()
        assert "access_token" in data and isinstance(data["access_token"], str) and len(data["access_token"]) > 20
        assert data["token_type"] == "bearer"
        assert data["user"]["email"] == ADMIN_EMAIL

    def test_login_wrong_password(self, api_client):
        r = api_client.post(f"{API}/auth/login", json={"email": ADMIN_EMAIL, "password": "WrongPass!"})
        assert r.status_code == 401

    def test_auth_me_with_jwt(self, api_client, admin_token):
        r = api_client.get(f"{API}/auth/me", headers={"Authorization": f"Bearer {admin_token}"})
        assert r.status_code == 200
        data = r.json()
        assert data["email"] == ADMIN_EMAIL
        assert data["auth_type"] == "jwt"

    def test_auth_me_without_token(self, api_client):
        r = requests.get(f"{API}/auth/me")  # fresh session, no auth
        assert r.status_code == 401


# ---------- Admin Orders protection ----------
class TestAdminOrders:
    def test_orders_requires_auth(self):
        r = requests.get(f"{API}/admin/orders")
        assert r.status_code == 401

    def test_orders_list_with_jwt(self, api_client, auth_headers):
        r = api_client.get(f"{API}/admin/orders", headers=auth_headers)
        assert r.status_code == 200
        assert isinstance(r.json(), list)


# ---------- Admin Products CRUD ----------
class TestAdminProducts:
    slug = f"test-product-{uuid.uuid4().hex[:8]}"

    def test_create_product(self, api_client, auth_headers):
        payload = {
            "name_fr": "TEST Produit",
            "name_en": "TEST Product",
            "slug": self.slug,
            "category": "women",
            "subcategory": "test",
            "price": 99.99,
            "images": ["https://example.com/img.jpg"],
            "description_fr": "desc",
            "description_en": "desc",
            "composition_fr": "c",
            "composition_en": "c",
            "stock": 10,
        }
        r = api_client.post(f"{API}/admin/products", json=payload, headers=auth_headers)
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["slug"] == self.slug
        assert "_id" not in data

        # GET verify persistence
        g = api_client.get(f"{API}/products/{self.slug}")
        assert g.status_code == 200
        assert g.json()["price"] == 99.99

    def test_update_product(self, api_client, auth_headers):
        payload = {
            "name_fr": "TEST Produit Updated",
            "name_en": "TEST Product Updated",
            "slug": self.slug,
            "category": "women",
            "subcategory": "test",
            "price": 149.99,
            "images": ["https://example.com/img.jpg"],
            "stock": 5,
        }
        r = api_client.put(f"{API}/admin/products/{self.slug}", json=payload, headers=auth_headers)
        assert r.status_code == 200, r.text
        # verify persistence
        g = api_client.get(f"{API}/products/{self.slug}")
        assert g.status_code == 200
        assert g.json()["price"] == 149.99
        assert g.json()["name_en"] == "TEST Product Updated"

    def test_delete_product(self, api_client, auth_headers):
        r = api_client.delete(f"{API}/admin/products/{self.slug}", headers=auth_headers)
        assert r.status_code == 200
        # verify gone
        g = api_client.get(f"{API}/products/{self.slug}")
        assert g.status_code == 404

    def test_create_product_no_auth(self, api_client):
        r = requests.post(f"{API}/admin/products", json={"name_fr": "x", "name_en": "x", "slug": "x", "category": "women", "subcategory": "x", "price": 1, "images": []})
        assert r.status_code == 401


# ---------- Promos ----------
class TestPromos:
    percent_code = f"TESTPCT{uuid.uuid4().hex[:5].upper()}"
    fixed_code = f"TESTFIX{uuid.uuid4().hex[:5].upper()}"
    expired_code = f"TESTEXP{uuid.uuid4().hex[:5].upper()}"

    def test_create_percent_promo_uppercased(self, api_client, auth_headers):
        r = api_client.post(
            f"{API}/admin/promos",
            json={"code": self.percent_code.lower(), "kind": "percent", "value": 20, "min_subtotal": 100},
            headers=auth_headers,
        )
        assert r.status_code == 200, r.text
        assert r.json()["code"] == self.percent_code  # uppercased

    def test_create_fixed_promo(self, api_client, auth_headers):
        r = api_client.post(
            f"{API}/admin/promos",
            json={"code": self.fixed_code, "kind": "fixed", "value": 10, "min_subtotal": 20},
            headers=auth_headers,
        )
        assert r.status_code == 200

    def test_create_expired_promo(self, api_client, auth_headers):
        expired = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        r = api_client.post(
            f"{API}/admin/promos",
            json={"code": self.expired_code, "kind": "percent", "value": 10, "min_subtotal": 0, "expires_at": expired},
            headers=auth_headers,
        )
        assert r.status_code == 200

    def test_list_promos(self, api_client, auth_headers):
        r = api_client.get(f"{API}/admin/promos", headers=auth_headers)
        assert r.status_code == 200
        codes = [p["code"] for p in r.json()]
        assert self.percent_code in codes

    def test_apply_percent_promo(self, api_client):
        r = api_client.post(f"{API}/promos/apply", json={"code": self.percent_code, "subtotal": 200})
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["discount"] == 40.0
        assert data["kind"] == "percent"

    def test_apply_fixed_promo(self, api_client):
        r = api_client.post(f"{API}/promos/apply", json={"code": self.fixed_code, "subtotal": 50})
        assert r.status_code == 200
        assert r.json()["discount"] == 10.0

    def test_apply_below_min_subtotal(self, api_client):
        r = api_client.post(f"{API}/promos/apply", json={"code": self.percent_code, "subtotal": 50})
        assert r.status_code == 400

    def test_apply_expired_promo(self, api_client):
        r = api_client.post(f"{API}/promos/apply", json={"code": self.expired_code, "subtotal": 100})
        assert r.status_code == 400
        assert "expired" in r.json().get("detail", "").lower()

    def test_apply_unknown_promo(self, api_client):
        r = api_client.post(f"{API}/promos/apply", json={"code": "NOPE_XYZ_UNKNOWN", "subtotal": 100})
        assert r.status_code == 404

    def test_delete_promos_cleanup(self, api_client, auth_headers):
        for c in (self.percent_code, self.fixed_code, self.expired_code):
            r = api_client.delete(f"{API}/admin/promos/{c}", headers=auth_headers)
            assert r.status_code == 200


# ---------- Orders (payment methods) ----------
def _make_order_payload(payment_method: str, phone: str = "+22501020304"):
    return {
        "contact": {
            "email": "test@example.com",
            "phone": "+22501020304",
            "first_name": "Test",
            "last_name": "User",
        },
        "shipping": {
            "address": "1 rue test",
            "city": "Abidjan",
            "postal_code": "00225",
            "country": "CI",
        },
        "payment_method": payment_method,
        "payment_phone": phone,
        "items": [{"product_id": "p1", "name": "Item", "price": 20, "quantity": 1}],
        "subtotal": 20,
        "shipping_cost": 5,
        "total": 25,
    }


class TestOrders:
    def test_flutterwave_returns_503_when_not_configured(self, api_client):
        r = api_client.post(f"{API}/orders", json=_make_order_payload("flutterwave"))
        assert r.status_code == 503, r.text

    def test_orange_money_order_works(self, api_client):
        r = api_client.post(f"{API}/orders", json=_make_order_payload("orange_money"))
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["order_number"].startswith("BS-")
        assert data["status"] == "pending"
        assert data["payment_method"] == "orange_money"
        # persistence
        g = api_client.get(f"{API}/orders/{data['id']}")
        assert g.status_code == 200

    def test_patch_order_status(self, api_client, auth_headers):
        # create order
        c = api_client.post(f"{API}/orders", json=_make_order_payload("wave"))
        assert c.status_code == 200
        order_id = c.json()["id"]
        # patch
        p = api_client.patch(f"{API}/admin/orders/{order_id}/status", json={"status": "paid"}, headers=auth_headers)
        assert p.status_code == 200
        # verify via admin list
        lst = api_client.get(f"{API}/admin/orders", headers=auth_headers)
        found = next((o for o in lst.json() if o["id"] == order_id), None)
        assert found is not None
        assert found["status"] == "paid"

    def test_patch_order_invalid_status(self, api_client, auth_headers):
        c = api_client.post(f"{API}/orders", json=_make_order_payload("mtn_momo"))
        order_id = c.json()["id"]
        p = api_client.patch(f"{API}/admin/orders/{order_id}/status", json={"status": "banana"}, headers=auth_headers)
        assert p.status_code == 400
