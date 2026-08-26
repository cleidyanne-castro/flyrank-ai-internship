# First Background Job evidence

## Execution

Run:

```bash
python3 -m unittest -v
python3 run_demo.py
```

Expected demo states:

| Scenario | Initial state | Worker result | Attempts |
| --- | --- | --- | --- |
| Success | Not present in the store | `completed` with a summary | 1 |
| Transient failure | Not present in the store | `completed` after retry | 2 |
| Permanent failure | Not present in the store | `failed` with the last error | 3 |
| Duplicate submission | Existing result for the slug | Existing result returned | 0 additional |

The test suite validates these states without network access. The slug is the idempotency key and the in-memory dictionary represents the result store.

## Boundaries

This is a worker function reference implementation. It does not claim a live queue, durable storage, scheduled trigger, authentication, or production repository integration.
