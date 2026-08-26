import tempfile
import unittest
from pathlib import Path

from generator import generate_report, validate_project


SAMPLE = {
    "project_name": "Test project",
    "role": "Engineer",
    "summary": "A short project summary.",
    "technologies": ["Python"],
    "links": [{"label": "Repository", "url": "https://example.com/repository"}],
    "outcomes": ["A documented result"],
}


class GeneratorTests(unittest.TestCase):
    def test_required_fields_are_checked(self):
        with self.assertRaises(ValueError):
            validate_project({"project_name": "Incomplete"})

    def test_pdf_is_created(self):
        with tempfile.TemporaryDirectory() as directory:
            output = generate_report(SAMPLE, Path(directory) / "report.pdf")
            self.assertTrue(output.exists())
            self.assertGreater(output.stat().st_size, 1000)
            self.assertEqual(output.read_bytes()[:4], b"%PDF")


if __name__ == "__main__":
    unittest.main()
