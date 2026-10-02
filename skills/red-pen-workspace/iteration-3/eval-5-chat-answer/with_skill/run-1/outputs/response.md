Session cookies, with the session stored in Redis.

- Revocation is immediate: delete the Redis key and the admin is logged out. A JWT stays valid until it expires unless you add a denylist, which is a session store again.
- The usual argument for JWT, no shared state across replicas, doesn't apply: Redis is already shared by all three.
- An admin panel is browser-only, so an `HttpOnly; Secure; SameSite=Strict` cookie keeps the credential out of reach of page JavaScript. You will need CSRF protection on state-changing routes.

This doesn't touch partner auth; they keep API keys.

I'd switch to JWT only if admin sign-in comes from an external identity provider that already issues them. There's no admin panel in NOTES.md or the code yet, so I'm assuming a new, browser-based internal tool served from ledgerd; is that right?
