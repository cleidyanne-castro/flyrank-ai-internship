# Build an AI Decision Flow

## Design

The workflow is: receive a message, classify it, route urgent cases, request human review when confidence is low, and finish with a logged decision.

## States

1. Received
2. Classified
3. Urgent route
4. Human review
5. Completed

## Reliability notes

Every transition carries the message id and decision reason. Low confidence never skips human review. A failed step can be retried without creating a second decision.

## Evidence

This design extends the Week 6 judgement endpoint and is documented as a state graph before implementation. The next implementation step is wiring the graph to React Flow and an Inngest function.
