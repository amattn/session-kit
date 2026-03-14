# How FastAPI Handles Async Requests

FastAPI is built on top of **Starlette** (an ASGI framework) and uses **Uvicorn** (an ASGI server) to handle async requests. Here's how the pieces fit together:

## The ASGI Foundation

Unlike WSGI (which handles one request per thread synchronously), ASGI (Asynchronous Server Gateway Interface) is designed around Python's `asyncio` event loop. Every incoming request is handled as a coroutine, which means the server can juggle thousands of concurrent connections on a single thread without blocking.

## `async def` vs `def` Endpoints

FastAPI supports both styles:

- **`async def` endpoints** run directly on the main asyncio event loop. When your handler `await`s an I/O operation (database query, HTTP call, file read), control returns to the event loop, which can serve other requests in the meantime. This is true non-blocking concurrency.

- **Plain `def` endpoints** are automatically run in an external **threadpool** (`anyio.to_thread.run_sync`). FastAPI does this so that synchronous code doesn't block the event loop. The tradeoff: you get thread-based concurrency instead of coroutine-based concurrency, with slightly higher overhead per request.

## The Event Loop in Practice

1. **Uvicorn** starts the asyncio event loop and listens for connections.
2. An HTTP request arrives. Uvicorn parses it and hands it to **Starlette's** routing layer.
3. Starlette matches the route and calls your **FastAPI endpoint**.
4. If the endpoint is `async def`, it runs on the event loop. Each `await` yields control so other requests can proceed.
5. If the endpoint is plain `def`, Starlette dispatches it to a thread in the default threadpool.
6. The response flows back through Starlette to Uvicorn to the client.

## Key Implications

- **Use `async def`** when your I/O libraries support async (e.g., `httpx`, `asyncpg`, `aiofiles`). This gives you maximum concurrency with minimal resource usage.
- **Use plain `def`** when you're calling synchronous libraries (e.g., `requests`, most ORMs without async support). FastAPI's threadpool dispatch prevents these from blocking the event loop.
- **Don't mix blocking calls into `async def` endpoints** without wrapping them in `run_in_executor` or similar. A blocking call inside an `async def` handler stalls the entire event loop, affecting all concurrent requests.

## Scaling Beyond One Process

The event loop is single-threaded, so CPU-bound work still blocks it. For production, you typically run multiple Uvicorn **workers** (via `--workers` or a process manager like Gunicorn with `uvicorn.workers.UvicornWorker`), giving you one event loop per process.

---

```
A. Dive deeper into a specific area (middleware, dependency injection, WebSockets, etc.)
B. See a code example demonstrating async vs sync behavior
C. Recommendations — tell me what you'd suggest
D. Ok — approve as-is
```
