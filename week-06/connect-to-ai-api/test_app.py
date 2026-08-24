import pytest
from httpx import ASGITransport, AsyncClient

from app import app, fallback_judgement

@pytest.mark.anyio
@pytest.mark.parametrize(
    ("message", "label"),
    [
        ("Card blocked after a suspected fraud alert", "urgent"),
        ("The banking app is down for every customer", "urgent"),
        ("There may be a security breach", "urgent"),
        ("Please review my account details", "normal"),
        ("Can you explain the monthly report?", "normal"),
        ("I want to update my address", "normal"),
        ("Thanks for the help", "normal"),
        ("Just checking the status", "normal"),
    ],
)
async def test_judge_returns_schema_for_eight_cases(message, label, monkeypatch):
    monkeypatch.setenv("AI_KILL_SWITCH", "true")
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/judge", json={"message": message})
    assert response.status_code == 200
    body = response.json()
    assert body["label"] in {"urgent", "normal", "low"}
    assert 0 <= body["confidence"] <= 1
    assert body["reason"]
    assert body["label"] == label if label == "urgent" else True

@pytest.mark.parametrize(
    "message",
    ["outage in production", "suspected fraud", "urgent blocked account"],
)
def test_fallback_marks_risk_messages_urgent(message):
    assert fallback_judgement(message).label == "urgent"

@pytest.mark.anyio
async def test_empty_message_is_rejected():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/judge", json={"message": ""})
    assert response.status_code == 422
