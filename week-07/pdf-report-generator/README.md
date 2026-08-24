# PDF Report Generator

The report is meant to turn structured project data into something a recruiter can read quickly.

## Input

The generator expects a project name, role, short summary, technologies, links, and outcomes.

## Output

The PDF has a title, summary, project sections, links, and a generated timestamp. Empty optional fields are left out instead of becoming blank headings.

## Checks

A generated file should open as a valid PDF, keep each heading with its text, and preserve links. The data object stays separate from the layout code so the same template can be reused for another project.
