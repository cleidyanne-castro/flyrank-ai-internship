# PDF report generator

## Goal

Generate a recruiter-ready PDF summary from structured project data.

## Input

The generator accepts a JSON object with project name, role, summary, technologies, links, and outcomes.

## Output

It produces a readable PDF with a title, short summary, project sections, links, and a generated timestamp. Missing optional fields are omitted instead of rendered as empty headings.

## Verification

The output must open as a valid PDF, preserve links, and keep headings together with their text. The source data remains separate from layout code.
