# Week 8: Wire One Real Thing

## Feature

The portfolio now has one dynamic feature: project filtering.

A recruiter can switch between All, AI, Data, and Analytics. The cards update immediately in the browser without reloading the page.

Live page:

https://cleidyanne-castro.github.io/cleidyanne-castro/

## Why this feature

The portfolio is meant to help a reader understand the work quickly. A filter is useful for a recruiter who wants to see a specific type of project without opening every card.

I kept the scope to one feature. There is no second half-built feature and no unnecessary backend.

## How the data flows

Each project card has a category stored in a data attribute on the HTML element. Each filter button has a matching category value.

When a button is selected, the browser reads that value, checks every card, and adds or removes a hidden class. The browser then redraws the visible cards. No personal data is collected and no server is required.

The feature works entirely in the page, so it remains compatible with GitHub Pages.

## Plain-words backend explanation

This feature does not need a backend. A backend is useful when a page needs to remember or process something after the browser sends it, such as storing a message or sending an email. The project filter only changes what is visible on the current page, so the browser can handle it by itself.

## Test cases

- All shows the four selected projects.
- AI shows the AWS Digital Bank Triage Assistant.
- Data shows the E-commerce RAG Chatbot and LH Nautical Lighthouse.
- Analytics shows the BCB Databricks Case.
- Selecting a new filter updates the pressed state for screen readers.
- The page stays on the same URL and does not reload.

## Limitation

The feature is live and client-side, but it is not a contact form. A future version can add a tested form when a free submission service and its verification path are available.
