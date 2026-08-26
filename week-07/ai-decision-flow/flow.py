from dataclasses import dataclass, field
from typing import Dict, Literal


State = Literal["received", "classified", "urgent_queue", "human_review", "completed"]


@dataclass
class Decision:
    message_id: str
    state: State
    label: str | None = None
    confidence: float | None = None
    reason: str | None = None
    history: list[State] = field(default_factory=list)


class DecisionFlow:
    def __init__(self) -> None:
        self.decisions: Dict[str, Decision] = {}

    def process(self, message_id: str, label: str, confidence: float, reason: str) -> Decision:
        if not message_id or not label or not reason:
            raise ValueError("message_id, label, and reason are required")
        if not 0 <= confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        if message_id in self.decisions:
            return self.decisions[message_id]

        decision = Decision(message_id=message_id, state="received")
        decision.history.append("received")
        decision.label = label
        decision.confidence = confidence
        decision.reason = reason
        decision.state = "classified"
        decision.history.append("classified")

        if confidence < 0.7:
            decision.state = "human_review"
        elif label == "urgent":
            decision.state = "urgent_queue"
        else:
            decision.state = "completed"
        decision.history.append(decision.state)
        self.decisions[message_id] = decision
        return decision
