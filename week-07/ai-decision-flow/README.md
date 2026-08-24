# AI Decision Flow

This is the workflow I would use for a data and security triage service.

## Flow

1. Receive a message with an id.
2. Validate the input at the boundary.
3. Classify the message and keep the confidence score.
4. Route high-risk cases to an urgent queue.
5. Send low-confidence cases to human review.
6. Store the decision, reason, and timestamp.

The important rule is that a low confidence result cannot silently become an automated decision. Every transition keeps the message id so a retry does not create a second decision.

## Scope

This submission documents the state design and the failure rules. The next implementation would connect the states to React Flow for visibility and Inngest for retries and background execution.
