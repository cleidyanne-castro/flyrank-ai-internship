# Week 6: Explain It Like You Built It

## Piece I chose

I chose the navigation and deployment path because it is the part that turns separate files into a site a person can actually use.

## Explanation in plain words

The navigation is just a group of links placed at the top of each page. Each link points to a destination. A link such as `#work` does not open another website. It moves the reader to the section whose HTML element has `id="work"`. The language links point to the other page, so the English page can open `pt.html` and the Portuguese page can return to the English page.

The project links use the full GitHub URL because each card should open the repository that contains the real work. This keeps the portfolio honest: the card is not pretending to be the project. It is a short explanation that leads to the source.

GitHub Pages publishes the files from the repository. When a commit reaches the main branch, the workflow checks out the repository, packages the site files, and deploys them. The browser then requests the page from the GitHub Pages URL. There is no separate application server for this version. The HTML, CSS, and embedded hero image are enough for the browser to render the page.

The reason this works without a build step on GitHub Pages is that the public copy is static HTML. The Next.js source is useful for development, but the deployed folder already contains the files the browser needs. This also makes the deployment easy to inspect and easy to replace.

## Two checks I can do myself

1. If I change the target of a navigation link, the browser will go to a different destination. A wrong section ID will leave the reader on the same page, so the ID and the link must match exactly.
2. If the workflow points to the wrong folder, GitHub Pages can deploy successfully but show the wrong content. The workflow currently uploads the repository root, where the public HTML files live.

## What I learned

The navigation is not decoration. It is a small map of the site. Deployment is not magic either. It is a sequence: commit, workflow, uploaded files, and browser request. Understanding that sequence makes it possible to diagnose a broken link or an outdated page without guessing.
