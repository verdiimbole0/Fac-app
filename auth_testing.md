# Billy's Store — Auth Testing Playbook

## Test admin credentials
- **Email**: `admin@billystore.com`
- **Password**: `Billy2026!Admin`
- **JWT endpoint**: `POST /api/auth/login`
- **Session endpoint**: `POST /api/auth/google-session` (from `session_id` fragment after Emergent auth)
- **Whoami**: `GET /api/auth/me` (works with either Bearer JWT or session_token cookie)
- **Logout**: `POST /api/auth/logout`

The Google Auth flow is **restricted** to the configured `ADMIN_EMAIL` (`admin@billystore.com`). Any other Google email will get a 403.

## Quickstart curl
```bash
API=$(grep REACT_APP_BACKEND_URL /app/frontend/.env | cut -d= -f2)
TOKEN=$(curl -s -X POST "$API/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@billystore.com","password":"Billy2026!Admin"}' \
  | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")

# Protected calls
curl -s "$API/api/auth/me" -H "Authorization: Bearer $TOKEN"
curl -s "$API/api/admin/orders" -H "Authorization: Bearer $TOKEN"
curl -s "$API/api/admin/promos" -H "Authorization: Bearer $TOKEN"
```

## Frontend flow
- `/admin/login` → email+password form OR "Continue with Google" button.
- Google button redirects to `https://auth.emergentagent.com/?redirect=<origin>/admin/auth-callback`.
- After Emergent auth, browser lands at `/admin/auth-callback#session_id=...`.
- `AuthCallback` page reads `useLocation().hash`, exchanges the session_id for a session_token cookie via `POST /api/auth/google-session`, then navigates to `/admin`.

## Test in browser
```javascript
// Set JWT in localStorage and navigate
await page.context.add_cookies([{
  "name": "session_token",
  "value": "YOUR_SESSION_TOKEN",
  "domain": "billy-shop.preview.emergentagent.com",
  "path": "/",
  "httpOnly": true,
  "secure": true,
  "sameSite": "None"
}]);
await page.goto("https://billy-shop.preview.emergentagent.com/admin");
```

## Success indicators
- ✅ `/api/auth/me` returns `{user_id, email, name, auth_type: 'jwt'|'google'}`
- ✅ `/admin` renders sidebar with 4 nav items (Dashboard, Products, Orders, Promo codes)
- ✅ `POST /api/admin/products` with valid body creates a product
- ✅ `POST /api/admin/promos` creates a promo and appears in list

## Failure indicators
- ❌ 401 on `/auth/me` after JWT login: check `JWT_SECRET` env var
- ❌ 403 on `/auth/google-session`: only `ADMIN_EMAIL` is allowed
- ❌ 401 on admin routes with token: verify header is `Authorization: Bearer <token>`

## Clean test data
```bash
mongosh --eval "
use('test_database');
db.admin_users.deleteMany({email: /test\./});
db.admin_sessions.deleteMany({session_token: /test_/});
"
```
