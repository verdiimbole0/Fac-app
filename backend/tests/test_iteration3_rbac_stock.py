"""Iteration 3 tests: RBAC (admin users), stock decrement/rollback, email silent-skip."""
import os
import uuid
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://billy-shop.preview.emergentagent.com").rstrip("/")
API = f"{BASE_URL}/api"

ADMIN_EMAIL = "admin@billystore.com"
ADMIN_PASSWORD = "Billy2026!Admin"


# ---------- Helpers ----------
def _login(email, password):
    r = requests.post(f"{API}/auth/login", json={"email": email, "password": password})
    return r


def _auth(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


@pytest.fixture(scope="module")
def super_token():
    r = _login(ADMIN_EMAIL, ADMIN_PASSWORD)
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


@pytest.fixture(scope="module")
def super_headers(super_token):
    return _auth(super_token)


@pytest.fixture(scope="module")
def stocked_product():
    r = requests.get(f"{API}/products?limit=100")
    for p in r.json():
        if p.get("stock", 0) >= 10:
            return p
    pytest.skip("No product with stock >= 10 available")


# ---------- /auth/me role+permissions ----------
class TestAuthMeRolePerms:
    def test_super_admin_role_and_perms(self, super_headers):
        r = requests.get(f"{API}/auth/me", headers=super_headers)
        assert r.status_code == 200
        d = r.json()
        assert d["role"] == "super_admin"
        assert set(d["permissions"]) == {"orders", "products", "promos", "users"}


# ---------- Admin Users CRUD & RBAC ----------
class TestAdminUsers:
    created_users = []

    def _create(self, super_headers, role, prefix="TEST"):
        email = f"{prefix.lower()}_{uuid.uuid4().hex[:8]}@example.com"
        password = "TestPass1234!"
        r = requests.post(
            f"{API}/admin/users",
            json={"email": email, "password": password, "name": f"{prefix} {role}", "role": role},
            headers=super_headers,
        )
        assert r.status_code == 200, r.text
        u = r.json()
        assert "password_hash" not in u
        assert u["email"] == email
        assert u["role"] == role
        self.created_users.append(u["user_id"])
        return {"email": email, "password": password, "user_id": u["user_id"], "role": role}

    def test_create_products_editor(self, super_headers):
        user = self._create(super_headers, "products_editor")
        # login as new user
        lr = _login(user["email"], user["password"])
        assert lr.status_code == 200
        token = lr.json()["access_token"]
        h = _auth(token)

        # /auth/me
        me = requests.get(f"{API}/auth/me", headers=h).json()
        assert me["role"] == "products_editor"
        assert me["permissions"] == ["products"]

        # Products access: PUT/DELETE guarded by require_perm; POST currently only requires auth
        # Verify PUT non-existent slug returns 404 (auth passed)
        put = requests.put(f"{API}/admin/products/__nope__", json={
            "name_fr":"x","name_en":"x","slug":"__nope__","category":"women","subcategory":"x",
            "price":1.0,"images":["https://ex.com"],
        }, headers=h)
        assert put.status_code in (404, 400), put.text  # not 403

        # Denied: orders, users, promos
        assert requests.get(f"{API}/admin/orders", headers=h).status_code == 403
        assert requests.get(f"{API}/admin/users", headers=h).status_code == 403
        assert requests.get(f"{API}/admin/promos", headers=h).status_code == 403

    def test_create_orders_manager(self, super_headers):
        user = self._create(super_headers, "orders_manager")
        lr = _login(user["email"], user["password"])
        token = lr.json()["access_token"]
        h = _auth(token)

        # orders_manager can list orders + patch status
        assert requests.get(f"{API}/admin/orders", headers=h).status_code == 200
        # invalid status returns 400 not 403
        r = requests.patch(f"{API}/admin/orders/nonexistent/status", json={"status": "paid"}, headers=h)
        assert r.status_code in (404, 400)  # not 403

        # Denied: users, promos, products-mutation
        assert requests.get(f"{API}/admin/users", headers=h).status_code == 403
        assert requests.get(f"{API}/admin/promos", headers=h).status_code == 403
        put = requests.put(f"{API}/admin/products/__nope__", json={
            "name_fr":"x","name_en":"x","slug":"__nope__","category":"women","subcategory":"x",
            "price":1.0,"images":["https://ex.com"],
        }, headers=h)
        assert put.status_code == 403, put.text

    def test_invalid_role_400(self, super_headers):
        r = requests.post(f"{API}/admin/users",
            json={"email": f"t_{uuid.uuid4().hex[:6]}@x.y", "password": "TestPass1234!", "name": "n", "role": "hacker"},
            headers=super_headers)
        assert r.status_code == 400

    def test_list_admin_users_no_password_hash(self, super_headers):
        r = requests.get(f"{API}/admin/users", headers=super_headers)
        assert r.status_code == 200
        for u in r.json():
            assert "password_hash" not in u

    def test_patch_role(self, super_headers):
        user = self._create(super_headers, "products_editor")
        r = requests.patch(f"{API}/admin/users/{user['user_id']}/role",
                           json={"role": "orders_manager"}, headers=super_headers)
        assert r.status_code == 200
        # invalid
        r = requests.patch(f"{API}/admin/users/{user['user_id']}/role",
                           json={"role": "banana"}, headers=super_headers)
        assert r.status_code == 400

    def test_cannot_delete_self(self, super_headers):
        me = requests.get(f"{API}/auth/me", headers=super_headers).json()
        r = requests.delete(f"{API}/admin/users/{me['user_id']}", headers=super_headers)
        assert r.status_code == 400

    def test_delete_user(self, super_headers):
        user = self._create(super_headers, "orders_manager")
        r = requests.delete(f"{API}/admin/users/{user['user_id']}", headers=super_headers)
        assert r.status_code == 200

    def test_cleanup_created_users(self, super_headers):
        for uid in self.created_users:
            requests.delete(f"{API}/admin/users/{uid}", headers=super_headers)


# ---------- Stock decrement / rollback ----------
def _order_body(items, subtotal, payment_method="orange_money"):
    return {
        "contact": {"email": "test@example.com", "phone": "+22501020304", "first_name": "T", "last_name": "U"},
        "shipping": {"address": "1", "city": "Abidjan", "postal_code": "00225", "country": "CI"},
        "payment_method": payment_method,
        "payment_phone": "+22501020304",
        "items": items,
        "subtotal": subtotal,
        "shipping_cost": 5,
        "total": subtotal + 5,
    }


class TestStock:
    def test_stock_decrement_success(self, stocked_product):
        p = stocked_product
        before = requests.get(f"{API}/products/{p['slug']}").json()["stock"]
        qty = 2
        r = requests.post(f"{API}/orders", json=_order_body(
            [{"product_id": p["id"], "name": p["name_en"], "price": p["price"], "quantity": qty}],
            p["price"] * qty
        ))
        assert r.status_code == 200, r.text
        after = requests.get(f"{API}/products/{p['slug']}").json()["stock"]
        assert after == before - qty, f"Expected {before - qty}, got {after}"

    def test_insufficient_stock_409(self, stocked_product):
        p = stocked_product
        before = requests.get(f"{API}/products/{p['slug']}").json()["stock"]
        overshoot = before + 100
        r = requests.post(f"{API}/orders", json=_order_body(
            [{"product_id": p["id"], "name": p["name_en"], "price": p["price"], "quantity": overshoot}],
            p["price"] * overshoot
        ))
        assert r.status_code == 409, r.text
        assert "Insufficient stock" in r.json().get("detail", "")
        # stock unchanged
        after = requests.get(f"{API}/products/{p['slug']}").json()["stock"]
        assert after == before

    def test_multi_item_rollback(self):
        # Get 2 products; item1 valid, item2 insufficient
        prods = requests.get(f"{API}/products?limit=100").json()
        good = next((x for x in prods if x.get("stock", 0) >= 3), None)
        bad = next((x for x in prods if x["id"] != good["id"] and x.get("stock", 0) >= 1), None)
        if not (good and bad):
            pytest.skip("Need two products with stock")
        good_before = requests.get(f"{API}/products/{good['slug']}").json()["stock"]
        bad_before = requests.get(f"{API}/products/{bad['slug']}").json()["stock"]
        overshoot = bad_before + 50
        items = [
            {"product_id": good["id"], "name": good["name_en"], "price": good["price"], "quantity": 1},
            {"product_id": bad["id"], "name": bad["name_en"], "price": bad["price"], "quantity": overshoot},
        ]
        subtotal = good["price"] + bad["price"] * overshoot
        r = requests.post(f"{API}/orders", json=_order_body(items, subtotal))
        assert r.status_code == 409, r.text
        # Both stocks unchanged (rollback)
        assert requests.get(f"{API}/products/{good['slug']}").json()["stock"] == good_before
        assert requests.get(f"{API}/products/{bad['slug']}").json()["stock"] == bad_before


# ---------- Email silent-skip (RESEND_API_KEY empty) ----------
class TestEmailSilentSkip:
    def test_order_succeeds_without_resend_key(self, stocked_product):
        p = stocked_product
        r = requests.post(f"{API}/orders", json=_order_body(
            [{"product_id": p["id"], "name": p["name_en"], "price": p["price"], "quantity": 1}],
            p["price"]
        ))
        assert r.status_code == 200, r.text
        assert r.json()["order_number"].startswith("BS-")


# ---------- Backfilled role on existing admin ----------
class TestExistingAdminRoleBackfill:
    def test_jwt_admin_is_super(self):
        r = _login(ADMIN_EMAIL, ADMIN_PASSWORD)
        assert r.status_code == 200
        me = requests.get(f"{API}/auth/me", headers=_auth(r.json()["access_token"])).json()
        assert me["role"] == "super_admin"


# ---------- Promo uses increments for non-Flutterwave ----------
class TestPromoUsesIncrement:
    def test_promo_uses_bumped(self, super_headers):
        code = f"TESTPUSE{uuid.uuid4().hex[:5].upper()}"
        r = requests.post(f"{API}/admin/promos",
                          json={"code": code, "kind": "percent", "value": 10, "min_subtotal": 0},
                          headers=super_headers)
        assert r.status_code == 200
        # pick a product different from what TestStock uses (last stocked product)
        prods = [x for x in requests.get(f"{API}/products?limit=100").json() if x.get("stock", 0) >= 5]
        p = prods[-1] if prods else None
        assert p, "no stocked product"
        body = _order_body(
            [{"product_id": p["id"], "name": p["name_en"], "price": p["price"], "quantity": 1}],
            p["price"]
        )
        body["promo_code"] = code
        body["discount"] = p["price"] * 0.1
        body["total"] = p["price"] - body["discount"] + 5
        r2 = requests.post(f"{API}/orders", json=body)
        assert r2.status_code == 200, r2.text
        # list and check uses
        promos = requests.get(f"{API}/admin/promos", headers=super_headers).json()
        found = next(x for x in promos if x["code"] == code)
        assert found["uses"] >= 1
        # cleanup
        requests.delete(f"{API}/admin/promos/{code}", headers=super_headers)
