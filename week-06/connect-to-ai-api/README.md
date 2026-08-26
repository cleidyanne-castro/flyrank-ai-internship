# Connect to an AI API

A small FastAPI endpoint that turns a message into a structured judgement.

## Endpoint

POST /judge

Input:

    {"message": "Card blocked after a suspected fraud alert"}

Output:

    {"label": "urgent", "confidence": 0.72, "reason": "..."}

The response is validated by Pydantic. The gateway uses an eight second timeout and three attempts. A kill switch and deterministic fallback keep the endpoint useful when the provider is unavailable. The default provider URL is OpenAI compatible, so it can be replaced with another compatible gateway.

## Run

    python -m venv .venv
    .venv/bin/pip install -r requirements.txt
    .venv/bin/uvicorn app:app --reload

Run tests with:

    .venv/bin/pytest -q

## Test evidence

The test file covers eight judgement inputs, schema validation, empty input rejection, and fallback behaviour. The fallback covers outage, downtime, fraud, blocked access, and breach terms. No API key is committed.

Run the test suite from this directory. A passing run should report 12 passed.

## Configuration

Set AI_API_KEY, AI_URL, AI_MODEL, or AI_KILL_SWITCH in the environment. Without a key, or when the kill switch is true, the service uses the deterministic fallback. The model gateway is not called in that mode.

## Limitations

The fallback is a safety path, not a substitute for model quality evaluation. The service does not persist requests, authenticate callers, or expose production monitoring. The provider contract assumes an OpenAI compatible JSON response.
