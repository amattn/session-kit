import httpx

# Partners register one HTTPS endpoint each. Delivery is at-least-once; the
# partner dedupes on event_id.
class WebhookClient:
    def __init__(self, timeout: float = 5.0):
        self._http = httpx.Client(timeout=timeout)

    def send(self, url: str, payload: dict) -> bool:
        resp = self._http.post(url, json=payload)
        return resp.status_code < 300

    def close(self) -> None:
        self._http.close()
