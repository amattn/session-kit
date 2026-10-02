Session cookies, with the session state in Redis.

Why, given what's in this repo:

- **You already have Redis shared across the three replicas.** That's the one thing that normally makes server-side sessions annoying (you'd otherwise need sticky sessions, which you've already rejected once), and it's solved. A session is a `session_id -> {admin_user_id, expires_at}` entry in Redis; any replica can look it up.
- **Admin panel means high privilege and few users.** The thing you want most is instant revocation: when someone leaves or a laptop is lost, you delete the session key and they're out on the next request. A JWT stays valid until it expires unless you build a denylist, and once you've built a denylist you've reinvented server-side sessions with extra steps.
- **It's a browser app.** `HttpOnly; Secure; SameSite=Lax` cookies keep the credential out of reach of JavaScript. JWTs in a browser end up in `localStorage` (readable by any XSS) or in a cookie anyway, at which point you've just chosen a more complicated cookie.
- **No refresh-token dance.** Idle timeout and absolute timeout are two numbers on the Redis entry. No access/refresh pair, no clock skew, no key rotation.

JWTs are the right fit for the *partner API* side of ledgerd (stateless bearer token, machine-to-machine, no cookies — which is exactly why sticky sessions were rejected for partners). They're the wrong fit for a human sitting in a browser with elevated privileges.

Concrete default, since you said pick one:

- Cookie: `HttpOnly; Secure; SameSite=Lax; Path=/admin`
- Session store: Redis key `admin_session:<random 32 bytes>`, value is the user id + created-at, TTL 12h absolute, refreshed on activity up to that cap. Keep this in a separate Redis keyspace or DB from the balance cache so an admin logout can never touch the 30s balance TTL invariant.
- CSRF: `SameSite=Lax` plus a per-session CSRF token checked on every non-GET request. Lax alone doesn't cover top-level POST navigations from other sites.
- Serve the admin panel from the same origin as the API (`/admin/...`) so the cookie and CSRF story stays simple. If it has to be a separate origin, use a subdomain and set `Domain=`; don't go cross-site, or you'll be back to tokens-in-headers.

One thing I'd want to confirm before writing it into NOTES.md: is the admin panel a browser UI served by ledgerd itself, or a separate service that calls ledgerd server-to-server? The above assumes the former. If it's the latter, the answer flips to a bearer token (API key or JWT) for that service, same as partners.

Want me to add this as a Key Design Decision in NOTES.md once you confirm?
