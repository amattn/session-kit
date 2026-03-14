# How FastAPI Handles Async Requests

FastAPI is built on top of **Starlette** (an ASGI framework) and uses **Uvicorn** (or another ASGI server) to handle async requests. Here is how it works:

## The ASGI Foundation

FastAPI uses the ASGI (Asynchronous Server Gateway Interface) standard rather than the older WSGI standard. ASGI is designed from the ground up for async Python, allowing the server to handle many concurrent connections without dedicating a thread to each one.

## `async def` vs `def` Endpoints

FastAPI supports both sync and async route handlers:

- **`async def` routes** run directly on the main async event loop (typically `asyncio`). When the handler hits an `await` (e.g., an async database query or HTTP call), it yields control back to the event loop, which can then serve other requests. This is non-blocking concurrency — one thread, many concurrent tasks.

- **`def` (sync) routes** are automatically run in an external **threadpool** (`anyio.to_thread.run_sync`). This prevents a blocking sync function from stalling the event loop. FastAPI detects whether your function is a coroutine or a regular function and dispatches accordingly.

## Event Loop and Concurrency Model

Under the hood:

1. **Uvicorn** starts an `asyncio` event loop.
2. Each incoming HTTP request is dispatched as a coroutine to the event loop.
3. For `async def` handlers, the coroutine runs directly on the loop.
4. For `def` handlers, the coroutine wraps the sync call in a threadpool executor.
5. While one handler is `await`-ing I/O, the event loop processes other requests.

This means a single worker process can handle thousands of concurrent connections as long as the handlers are doing I/O-bound work with `await`.

## Practical Implications

- **I/O-bound work** (database queries, HTTP calls, file reads): use `async def` with an async client library (e.g., `httpx`, `asyncpg`, `aiofiles`) to get maximum concurrency.
- **CPU-bound work** (image processing, heavy computation): async does not help here since the event loop is single-threaded. Offload to a process pool or a task queue like Celery.
- **Sync libraries** (e.g., `requests`, synchronous SQLAlchemy): use `def` (not `async def`) so FastAPI puts the call in a threadpool. If you use a sync blocking call inside `async def`, it blocks the entire event loop.

## Dependencies and Middleware

FastAPI's dependency injection system (`Depends(...)`) also supports both sync and async dependencies using the same dispatch logic. ASGI middleware likewise runs within the async context, so the entire request pipeline is async-aware.

## Summary

FastAPI's async handling comes from the ASGI stack: Uvicorn runs an asyncio event loop, Starlette dispatches requests as coroutines, and FastAPI adds the routing and DI layer on top. `async def` handlers run on the loop directly; `def` handlers get offloaded to a threadpool automatically. The result is high concurrency for I/O-bound workloads with a clean, straightforward API.
