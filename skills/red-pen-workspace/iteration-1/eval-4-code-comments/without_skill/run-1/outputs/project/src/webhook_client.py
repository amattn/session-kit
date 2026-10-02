import random
import time

import httpx

# Partners register one HTTPS endpoint each. Delivery is at-least-once; the
# partner dedupes on event_id.
class WebhookClient:
    MAX_ATTEMPTS = 3
    BASE_DELAY = 0.2  # seconds; delays are 0.2s, 0.4s (plus jitter)

    def __init__(self, timeout: float = 5.0, sleep=time.sleep):
        self._http = httpx.Client(timeout=timeout)
        self._sleep = sleep

    def send(self, url: str, payload: dict) -> bool:
        for attempt in range(1, self.MAX_ATTEMPTS + 1):
            try:
                resp = self._http.post(url, json=payload)
            except httpx.TransportError:
                # Timeout / connection failure. Safe to retry: at-least-once
                # delivery, partner dedupes on event_id.
                if attempt == self.MAX_ATTEMPTS:
                    return False
            else:
                if resp.status_code < 300:
                    return True
                if resp.status_code < 500 or attempt == self.MAX_ATTEMPTS:
                    # 4xx: our request is bad; retrying won't change the answer.
                    return False
            self._sleep(self._backoff(attempt))
        return False

    def _backoff(self, attempt: int) -> float:
        # Full jitter so three replicas retrying the same partner don't sync up.
        return random.uniform(0, self.BASE_DELAY * 2 ** (attempt - 1))

    def close(self) -> None:
        self._http.close()
