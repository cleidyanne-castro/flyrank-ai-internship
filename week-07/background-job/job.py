from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class JobResult:
    slug: str
    status: str
    summary: str = ""
    attempts: int = 0
    error: str = ""


def run_job(
    slug: str,
    fetcher: Callable[[str], dict],
    store: Dict[str, JobResult],
    max_attempts: int = 3,
) -> JobResult:
    if not slug:
        raise ValueError("slug is required")
    if slug in store:
        return store[slug]

    last_error = ""
    for attempt in range(1, max_attempts + 1):
        try:
            payload = fetcher(slug)
            name = payload.get("name")
            description = payload.get("description", "")
            if not isinstance(name, str) or not name:
                raise ValueError("metadata name is required")
            result = JobResult(slug, "completed", f"{name}: {description}".strip(), attempt)
            store[slug] = result
            return result
        except (OSError, ValueError, KeyError) as exc:
            last_error = str(exc)

    result = JobResult(slug, "failed", attempts=max_attempts, error=last_error)
    store[slug] = result
    return result
