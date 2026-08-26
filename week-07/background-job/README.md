# First Background Job

The job receives a project slug, fetches repository metadata, validates the response, and stores a short summary.

It is safe to retry because the project slug is the idempotency key. Temporary network failures use a bounded retry count. The log records success or failure without exposing credentials.

The useful connection to my portfolio is the same one I use in data engineering: keep slow enrichment work off the request path and make the result observable.

## Run

```bash
python3 -m unittest -v
python3 run_demo.py
```

The tests use an injected fetcher, so they do not require a network connection. They cover a successful fetch, a transient failure followed by success, a permanent failure, duplicate job submission, and invalid retry configuration. The demo prints the completed, retried, and failed result states.

## Evidence

`job.py` exposes a small worker function with a bounded retry count, explicit status, validation, and a slug-based idempotency key. `test_job.py` verifies each result. `run_demo.py` provides a deterministic success, retry, and failure run.

## Limitations

The example uses an in-memory store and an injected fetcher. It does not include a live queue, durable database, scheduled trigger, authentication, or production repository integration.
