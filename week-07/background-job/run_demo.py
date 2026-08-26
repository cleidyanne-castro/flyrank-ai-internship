from job import run_job


def run_success_case():
    return run_job("success", lambda slug: {"name": "Demo", "description": "Completed"}, {})


def run_retry_case():
    calls = {"count": 0}

    def fetcher(slug):
        calls["count"] += 1
        if calls["count"] == 1:
            raise OSError("temporary failure")
        return {"name": "Demo", "description": "Recovered"}

    return run_job("retry", fetcher, {})


def run_failure_case():
    return run_job("failure", lambda slug: (_ for _ in ()).throw(OSError("offline")), {}, max_attempts=3)


if __name__ == "__main__":
    for result in (run_success_case(), run_retry_case(), run_failure_case()):
        print(result)
