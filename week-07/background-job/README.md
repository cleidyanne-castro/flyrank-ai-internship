# First Background Job

The job receives a project slug, fetches repository metadata, validates the response, and stores a short summary.

It is safe to retry because the project slug is the idempotency key. Temporary network failures use a bounded retry count. The log records success or failure without exposing credentials.

The useful connection to my portfolio is the same one I use in data engineering: keep slow enrichment work off the request path and make the result observable.
