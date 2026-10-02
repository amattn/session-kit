Session cookies, stored in Redis.

One caveat first: there's no admin panel anywhere in the repo or in NOTES.md — no routes, no auth code, no decision record. So I'm assuming it's a browser-based UI for your own staff (not a programmatic client like the partners). If it's actually a separate SPA calling the API from another origin, say so and the answer shifts a bit.

Why cookies win here:

- **You already have Redis shared across the three replicas.** That's the one thing that makes server-side sessions awkward, and you've already solved it for the rate limiter. A session store is the same shape of problem: small keyed state, shared by all replicas.
- **Admin sessions need to be revocable.** When someone leaves or a laptop is lost, you want "log them out now," not "wait for the token to expire." Stateless JWTs can't do that without a denylist, and once you add a denylist you've rebuilt server-side sessions with extra steps.
- **Browsers handle cookies safely by default.** `HttpOnly; Secure; SameSite=Lax` keeps the credential out of reach of JS. A JWT in localStorage is readable by any XSS, and a JWT in a cookie is just a session cookie with a bigger payload.
- **Partners don't send cookies, and that's fine.** The 2026-09-10 rate-limiter note rejected sticky sessions because partners are cookie-less. That's about partners; the admin panel is a different client with a different trust model, so it doesn't conflict.

Where JWTs would make sense: the admin panel talks to a separate service that can't reach your Redis, or you need to hand short-lived tokens to a third party. Neither applies as far as I can tell.

Concrete default, per your "pick a default and we'll revisit": random 32-byte session id in an `HttpOnly; Secure; SameSite=Lax` cookie, session record in Redis with an idle timeout (something like 12 hours) and an absolute cap (something like 7 days), rotated on login, deleted on logout. No config knobs.

If you want, I'll add this as a Key Design Decision in NOTES.md so it's on record next to the rate-limiter choices.
