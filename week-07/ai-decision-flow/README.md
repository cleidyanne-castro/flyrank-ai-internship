# AI Decision Flow

This repository contains a small executable reference flow for data and security triage. It makes each state transition explicit and keeps low-confidence results out of the automatic decision path.

## Flow

1. Receive a message with an id.
2. Validate the input at the boundary.
3. Classify the message and keep the confidence score.
4. Route high-risk cases to an urgent queue.
5. Send low-confidence cases to human review.
6. Store the decision, reason, and timestamp.

The important rule is that a low confidence result cannot silently become an automated decision. Every transition keeps the message id so a retry does not create a second decision.

## Run

```bash
python3 -m unittest -v
```

The tests cover the normal route, low-confidence human review, high-risk routing, duplicate event handling, and invalid input.

## Evidence

`flow.py` implements the state transitions without external credentials. `test_flow.py` verifies the output state and the idempotency rule. The state model is ready to be rendered in React Flow and invoked by Inngest, but those framework integrations are not included in this dependency-free reference implementation.

## Limitations

The reference flow stores state in memory and does not call a live model, queue, database, or notification provider. Production execution would need durable state, authenticated events, observability, and a real worker runtime.
