Session cookies, with the session stored server-side in Redis.

- **Revocation.** On a system that serves balances, you need to be able to end an admin's access immediately (offboarding, lost laptop, suspected compromise). With server-side sessions that is deleting a Redis key. A JWT stays valid until it expires unless you add a denylist, and a denylist is a session store by another name.
- **You already have the shared store.** The usual argument for JWT is avoiding shared state across replicas. ledgerd has three replicas and already keeps shared state in Redis for the rate limiter, so that argument doesn't apply.
- **Browser storage.** An admin panel is a browser app. An `HttpOnly; Secure; SameSite=Strict` cookie is out of reach of page JavaScript; a JWT usually ends up in `localStorage`, where any XSS can read it.

What cookies cost you: CSRF protection on state-changing routes (`SameSite=Strict` plus a CSRF token), and the panel has to be served from the same site as the API.

Two assumptions, since nothing in the repo or NOTES.md describes the admin panel yet:

1. It is a browser UI used by a small number of internal staff. If it were a separate service calling ledgerd machine-to-machine, I'd say short-lived tokens instead.
2. You are doing login yourselves. If admins sign in through a company SSO (Okta, Google Workspace), the IdP will hand you a JWT at login; verify it once, then issue your own session cookie rather than using the IdP token as the session.

This is separate from partner auth: partners keep using API keys, and nothing here changes that.

I haven't recorded this in NOTES.md. Say the word if you want it added as a decision.
