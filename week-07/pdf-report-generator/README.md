# PDF Report Generator

The report is meant to turn structured project data into something a recruiter can read quickly.

## Input

The generator expects a project name, role, short summary, technologies, links, and outcomes.

## Output

The PDF has a title, summary, project sections, links, and a generated timestamp. Empty optional fields are left out instead of becoming blank headings.

## Checks

A generated file should open as a valid PDF, keep each heading with its text, and preserve links. The data object stays separate from the layout code so the same template can be reused for another project.

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python generator.py --input sample_project.json --output output/pdf/sample-report.pdf
```

Run the tests with:

```bash
.venv/bin/python -m unittest -v
```

The generator validates the input contract, creates a PDF with a title, summary, technologies, outcomes, links, and UTC generation time, and writes the result to the requested path.

Observed result for the included sample: the test suite passes two tests and the generator creates a one-page A4 PDF. The PDF was rendered with `pdftoppm` for a visual layout check.

## Evidence

The generator source, sample input, tests, and generated PDF are included in the repository.

## Limitations

The template does not calculate business metrics. It reports only the outcomes supplied in the input JSON. A production version would add stronger schema validation, template versioning, and visual regression checks for larger reports.
