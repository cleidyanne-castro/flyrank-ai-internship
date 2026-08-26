import os
from typing import Literal

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Message Judgement API")
AI_URL = os.getenv("AI_URL", "https://api.openai.com/v1/chat/completions")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")
AI_KEY = os.getenv("AI_API_KEY", "")

class JudgeRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

class JudgeResponse(BaseModel):
    label: Literal["urgent", "normal", "low"]
    confidence: float = Field(ge=0, le=1)
    reason: str = Field(min_length=1)

def fallback_judgement(message: str) -> JudgeResponse:
    text = message.lower()
    urgent = any(word in text for word in ("outage", "down", "unavailable", "fraud", "blocked", "urgent", "breach"))
    return JudgeResponse(
        label="urgent" if urgent else "normal",
        confidence=0.72 if urgent else 0.55,
        reason="Deterministic fallback used because the model gateway is unavailable.",
    )

async def ask_model(message: str) -> JudgeResponse:
    kill_switch = os.getenv("AI_KILL_SWITCH", "false").lower() == "true"
    if kill_switch or not AI_KEY:
        return fallback_judgement(message)

    payload = {
        "model": AI_MODEL,
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": "Classify the message as urgent, normal, or low. Return JSON with label, confidence, reason."},
            {"role": "user", "content": message},
        ],
    }
    headers = {"Authorization": f"Bearer {AI_KEY}"}
    last_error = None
    for attempt in range(3):
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                response = await client.post(AI_URL, json=payload, headers=headers)
                response.raise_for_status()
                data = response.json()["choices"][0]["message"]["content"]
                result = JudgeResponse.model_validate_json(data)
                return result
        except (httpx.HTTPError, KeyError, ValueError) as exc:
            last_error = exc
            if attempt == 2:
                break
    raise HTTPException(status_code=502, detail=f"AI gateway failed after retries: {last_error}")

@app.post("/judge", response_model=JudgeResponse)
async def judge(request: JudgeRequest) -> JudgeResponse:
    return await ask_model(request.message)
