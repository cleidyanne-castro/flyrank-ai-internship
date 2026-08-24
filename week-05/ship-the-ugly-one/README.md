# Week 5: Ship the Ugly One

This is the first public version of my portfolio. The goal was to make the real work reachable before polishing every detail.

## Live deliverables

Portfolio in English:

https://cleidyanne-castro.github.io/cleidyanne-castro/

Portfolio for Brazilian recruiters:

https://cleidyanne-castro.github.io/cleidyanne-castro/pt.html

The English page includes the main navigation, selected data and AI projects, an about section, a résumé link, LinkedIn, GitHub, and contact links. The Portuguese page follows the same path for Brazilian readers.

## What is live

The portfolio currently presents four selected repositories:

- AWS Digital Bank Triage Assistant
- E-commerce RAG Chatbot
- BCB Databricks Case
- LH Nautical Lighthouse

The GitHub profile shows the full set of 16 public repositories. The portfolio uses the four projects that best communicate a coherent direction in data engineering, analytics engineering, cloud, and applied AI.

## Build notes

The public version is a static GitHub Pages site. The source portfolio is built with Next.js and TypeScript, and the GitHub Pages copy keeps the same content in simple HTML and CSS.

The current visual system uses a dark navy background, cobalt and violet accents, large editorial headings, and a data and AI hero visual with a slow motion effect. The English and Portuguese pages are intentionally separate so each audience can read the content in their own language.

## First real reaction

Reviewer: the portfolio owner, a data and AI professional who used the site during the build.

Reaction:

The reviewer liked the typography, layout, and technology-focused visual direction. They asked for better readability in smaller text, a stronger dark blue and violet palette, a Portuguese page for Brazilian recruiters, and a clearer project count. They also corrected the repository count from eight to sixteen and selected four projects that best represent the intended portfolio direction.

Those changes were applied before this submission. This was an informal real-user review, not a formal recruiter review.

## Still ugly

- The public site is static, so it does not have a contact form yet.
- The English and Portuguese pages are maintained separately and can drift if one is changed without the other.
- The project cards are concise summaries, not full case studies with metrics and architecture diagrams.
- There is no custom domain or analytics setup yet.
- The hero image is embedded in the page to keep the GitHub Pages deployment self-contained.
- A full accessibility and performance pass on several physical devices is still pending.

## What I can explain

I can explain the page structure, the project data model, the card rendering, the responsive CSS, the GitHub Pages workflow, and the reason for separating the English and Portuguese pages. I also understand the deployment path from a commit on the main branch to the live GitHub Pages URL.

## Repository

https://github.com/cleidyanne-castro/cleidyanne-castro
