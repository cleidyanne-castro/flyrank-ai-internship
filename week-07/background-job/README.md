# Your first background job

## Job design

A background job receives a project slug, fetches repository metadata, validates the response, and stores a compact summary.

## Safety

The job is idempotent by project slug, retries transient network failures with a bounded limit, records the final status, and exposes no credentials in logs.

## Completion criteria

A successful run stores the summary. A failed run stores the error and can be retried without duplicating the record.
