Session cookies, stored in Redis. Redis is already in the deploy and shared by the three replicas, so a server-side session store costs nothing new; an admin panel is a browser UI, and an HttpOnly, SameSite cookie is the simplest XSS/CSRF story there; and admin access needs instant revocation (offboarded staff, stolen laptop), which a stateless JWT can't give you without a denylist, which is a session store anyway.

JWT wins only if the panel is a separate SPA on another origin, or if machine clients need the admin API. The "partners don't send cookies" note in NOTES.md is about the rate limiter, not this.

Nothing in the repo mentions an admin panel yet. Is it a browser UI served by ledgerd itself?
