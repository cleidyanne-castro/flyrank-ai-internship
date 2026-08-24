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

    pip install -r requirements.txt
    uvicorn app:app --reload

Run tests with:

    pytest -q

## Evidence

The test file covers eight judgement inputs, schema validation, empty input rejection, and fallback behaviour. No API key is committed. Set AI_API_KEY, AI_URL, AI_MODEL, or AI_KILL_SWITCH in the environment.
