import unittest

from job import run_job


class BackgroundJobTests(unittest.TestCase):
    def test_successful_job_stores_summary(self):
        store = {}
        result = run_job("demo", lambda slug: {"name": "Demo", "description": "Example"}, store)
        self.assertEqual(result.status, "completed")
        self.assertEqual(result.attempts, 1)
        self.assertEqual(store["demo"].summary, "Demo: Example")

    def test_transient_failure_is_retried(self):
        calls = []

        def fetcher(slug):
            calls.append(slug)
            if len(calls) == 1:
                raise OSError("temporary failure")
            return {"name": "Recovered"}

        result = run_job("retry", fetcher, {})
        self.assertEqual(result.status, "completed")
        self.assertEqual(result.attempts, 2)

    def test_permanent_failure_is_bounded(self):
        result = run_job("fail", lambda slug: (_ for _ in ()).throw(OSError("offline")), {}, max_attempts=3)
        self.assertEqual(result.status, "failed")
        self.assertEqual(result.attempts, 3)

    def test_duplicate_slug_does_not_run_again(self):
        calls = []
        store = {}

        def fetcher(slug):
            calls.append(slug)
            return {"name": "Once"}

        first = run_job("same", fetcher, store)
        second = run_job("same", fetcher, store)
        self.assertIs(first, second)
        self.assertEqual(calls, ["same"])


if __name__ == "__main__":
    unittest.main()
