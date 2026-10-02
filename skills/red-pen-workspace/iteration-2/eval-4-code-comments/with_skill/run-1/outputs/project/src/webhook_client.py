import time

import httpx

MAX_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 0.2

# Partners register one HTTPS endpoint each. Delivery is at-least-once; the
# partner dedupes on event_id.
class WebhookClient:
    def __init__(self, timeout: float = 5.0):
        self._http = httpx.Client(timeout=timeout)

    def send(self, url: str, payload: dict) -> bool:
        for attempt in range(MAX_ATTEMPTS):
            resp = self._http.post(url, json=payload)
            # 5xx is the partner's outage; 4xx means they rejected this payload,
            # and an identical resend gets the same answer.
            if resp.status_code < 500:
                return resp.status_code < 300
            if attempt < MAX_ATTEMPTS - 1:
                time.sleep(BACKOFF_BASE_SECONDS * 2**attempt)
        return False

    def close(self) -> None:
        self._http.close()
