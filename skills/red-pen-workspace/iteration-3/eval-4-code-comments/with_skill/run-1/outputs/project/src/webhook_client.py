import random
import time

import httpx

MAX_ATTEMPTS = 3
BACKOFF_BASE_S = 0.2

# Partners register one HTTPS endpoint each. Delivery is at-least-once; the
# partner dedupes on event_id.
class WebhookClient:
    def __init__(self, timeout: float = 5.0):
        self._http = httpx.Client(timeout=timeout)

    # Timeouts and connection errors are not retried; they raise on the first
    # attempt.
    def send(self, url: str, payload: dict) -> bool:
        for attempt in range(MAX_ATTEMPTS):
            if attempt:
                # Jitter: a partner outage fails many events at once, and
                # unjittered retries would all land on it together.
                time.sleep(BACKOFF_BASE_S * 2 ** (attempt - 1) * random.uniform(0.5, 1.5))
            resp = self._http.post(url, json=payload)
            # 429 fails fast with the rest of 4xx; Retry-After is not honored.
            if resp.status_code < 500:
                return resp.status_code < 300
        return False

    def close(self) -> None:
        self._http.close()
