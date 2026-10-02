import random
import time

import httpx

# Retry policy. Fixed on purpose (see NOTES.md: "pick a default and we'll
# revisit") rather than exposed as constructor knobs.
MAX_ATTEMPTS = 3
BASE_BACKOFF_S = 0.2
MAX_BACKOFF_S = 2.0


# Partners register one HTTPS endpoint each. Delivery is at-least-once; the
# partner dedupes on event_id. That dedupe is what makes retrying safe: a
# request that timed out may have already been received, and resending it is
# harmless.
class WebhookClient:
    def __init__(self, timeout: float = 5.0):
        self._http = httpx.Client(timeout=timeout)

    def send(self, url: str, payload: dict) -> bool:
        """Deliver payload to url. Returns True on a 2xx response.

        Retries up to MAX_ATTEMPTS times on 5xx and on transport errors
        (connect/read timeouts, connection reset), with exponential backoff
        and full jitter. Any 4xx fails immediately: the partner rejected the
        request and resending the same bytes will not change that.
        """
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                resp = self._http.post(url, json=payload)
            except httpx.TransportError:
                if attempt == MAX_ATTEMPTS:
                    return False
                self._sleep_before_retry(attempt)
                continue

            if resp.status_code < 300:
                return True
            if resp.status_code < 500 or attempt == MAX_ATTEMPTS:
                return False
            self._sleep_before_retry(attempt)

        return False

    @staticmethod
    def _sleep_before_retry(attempt: int) -> None:
        # Full jitter (0..cap) rather than a fixed delay so that the three
        # replicas retrying the same flapping partner don't line up their
        # requests and land on it in lockstep.
        cap = min(MAX_BACKOFF_S, BASE_BACKOFF_S * (2 ** (attempt - 1)))
        time.sleep(random.uniform(0, cap))

    def close(self) -> None:
        self._http.close()
