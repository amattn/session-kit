import httpx
import pytest

from src.webhook_client import WebhookClient


def make_client(responses):
    """Client whose transport returns `responses` in order; records calls and sleeps."""
    calls = []
    sleeps = []
    it = iter(responses)

    def handler(request):
        calls.append(request)
        r = next(it)
        if isinstance(r, Exception):
            raise r
        return httpx.Response(r)

    client = WebhookClient(sleep=sleeps.append)
    client._http = httpx.Client(transport=httpx.MockTransport(handler))
    return client, calls, sleeps


def test_2xx_succeeds_first_try():
    client, calls, sleeps = make_client([200])
    assert client.send("https://partner.example/hook", {"event_id": "e1"}) is True
    assert len(calls) == 1
    assert sleeps == []


def test_5xx_then_success_retries():
    client, calls, sleeps = make_client([503, 502, 200])
    assert client.send("https://partner.example/hook", {"event_id": "e1"}) is True
    assert len(calls) == 3
    assert len(sleeps) == 2
    assert 0 <= sleeps[0] <= 0.2
    assert 0 <= sleeps[1] <= 0.4


def test_5xx_gives_up_after_three_attempts():
    client, calls, sleeps = make_client([500, 500, 500, 200])
    assert client.send("https://partner.example/hook", {"event_id": "e1"}) is False
    assert len(calls) == 3
    assert len(sleeps) == 2


def test_4xx_fails_fast():
    client, calls, sleeps = make_client([400, 200])
    assert client.send("https://partner.example/hook", {"event_id": "e1"}) is False
    assert len(calls) == 1
    assert sleeps == []


def test_transport_error_is_retried():
    client, calls, sleeps = make_client([httpx.ConnectError("boom"), 200])
    assert client.send("https://partner.example/hook", {"event_id": "e1"}) is True
    assert len(calls) == 2
    assert len(sleeps) == 1


def test_transport_error_gives_up_after_three_attempts():
    errs = [httpx.ReadTimeout("slow")] * 3
    client, calls, sleeps = make_client(errs)
    assert client.send("https://partner.example/hook", {"event_id": "e1"}) is False
    assert len(calls) == 3
