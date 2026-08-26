# PDF Report Generator

The report is meant to turn structured project data into something a recruiter can read quickly.

## Input

The generator expects a project name, role, short summary, technologies, links, and outcomes.

## Output

The PDF has a title, summary, project sections, links, and a generated timestamp. Empty optional fields are left out instead of becoming blank headings.

## Checks

A generated file should open as a valid PDF, keep each heading with its text, and preserve links. The data object stays separate from the layout code so the same template can be reused for another project.

## Reproduction checklist

1. Provide one project data object with all required fields.
2. Generate one PDF from the template.
3. Open the file in a PDF viewer.
4. Check the title, summary, section headings, links, and generated timestamp.
5. Repeat with optional fields omitted and confirm that no empty headings appear.

## Evidence

The README defines the input contract and the layout checks. A generated PDF and the generator source are required for a complete implementation review.

## Limitations

This directory currently documents the contract and verification criteria. It does not include a committed generator script or generated PDF artifact, so the output cannot be independently reproduced from this directory alone.
