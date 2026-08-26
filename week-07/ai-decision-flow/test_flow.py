import unittest

from flow import DecisionFlow


class DecisionFlowTests(unittest.TestCase):
    def setUp(self):
        self.flow = DecisionFlow()

    def test_normal_result_completes(self):
        result = self.flow.process("m-1", "normal", 0.92, "Routine request")
        self.assertEqual(result.state, "completed")
        self.assertEqual(result.history, ["received", "classified", "completed"])

    def test_urgent_result_is_queued(self):
        result = self.flow.process("m-2", "urgent", 0.91, "Possible account takeover")
        self.assertEqual(result.state, "urgent_queue")

    def test_low_confidence_requires_human_review(self):
        result = self.flow.process("m-3", "normal", 0.42, "Ambiguous message")
        self.assertEqual(result.state, "human_review")

    def test_duplicate_message_id_is_idempotent(self):
        first = self.flow.process("m-4", "urgent", 0.88, "Incident")
        second = self.flow.process("m-4", "normal", 0.99, "Changed input")
        self.assertIs(first, second)
        self.assertEqual(second.label, "urgent")

    def test_invalid_confidence_is_rejected(self):
        with self.assertRaises(ValueError):
            self.flow.process("m-5", "normal", 1.2, "Invalid")


if __name__ == "__main__":
    unittest.main()
