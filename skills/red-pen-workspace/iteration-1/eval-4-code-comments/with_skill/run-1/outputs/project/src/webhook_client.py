import random
import time

import httpx

_MAX_ATTEMPTS = 3
_BACKOFF_BASE_SECONDS = 0.2

# Partners register one HTTPS endpoint each. Delivery is at-least-once; the
# partner dedupes on event_id.
class WebhookClient:
    def __init__(self, timeout: float = 5.0):
        self._http = httpx.Client(timeout=timeout)

    def send(self, url: str, payload: dict) -> bool:
        # Transport errors (timeout, refused connection) are not retried; they raise.
        for attempt in range(_MAX_ATTEMPTS):
            resp = self._http.post(url, json=payload)
            if resp.status_code < 500:
                # 4xx is our payload or their config; a retry can't change it.
                return resp.status_code < 300
            if attempt < _MAX_ATTEMPTS - 1:
                # Jitter keeps the three replicas from retrying a partner in lockstep.
                time.sleep(_BACKOFF_BASE_SECONDS * 2**attempt + random.uniform(0, _BACKOFF_BASE_SECONDS))
        return False

    def close(self) -> None:
        self._http.close()
