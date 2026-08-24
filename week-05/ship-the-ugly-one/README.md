# Week 5: Personal Website Live

## Live URL

https://cleidyanne-castro.github.io/cleidyanne-castro/

Portuguese recruiter page:

https://cleidyanne-castro.github.io/cleidyanne-castro/pt.html

The site is live over HTTPS on the GitHub Pages free domain. GitHub Pages is an accepted hosting path for this assignment.

## What the site contains

The page explains my focus in data engineering, analytics engineering, cloud, and applied AI. It links to:

- LinkedIn: https://www.linkedin.com/in/cleidyanne-castro-pereira-612506160/
- GitHub: https://github.com/cleidyanne-castro
- CV: https://cleidyanne-castro.github.io/cleidyanne-castro/CVDataCleidyanneCastro.pdf
- Email contact: mailto:annecbs93@gmail.com

It also includes a Portuguese version for Brazilian recruiters and four selected project links.

## DNS walkthrough

DNS is the directory that connects a human-readable website address to the server that can answer requests.

When someone types an address, the browser first asks a DNS resolver. The resolver checks whether it already knows the answer. If it does not, it asks the relevant nameserver for the domain. The nameserver returns a DNS record, such as an A record with an IP address or a CNAME record that points one hostname to another. The browser then connects to the destination returned by DNS and asks for the page.

A CNAME is useful when a subdomain should follow another hostname. For example, `www.example.com` can point to a host's assigned address with a CNAME. The browser still starts with the visitor's address, but DNS tells it where that address is served.

This portfolio currently uses the free GitHub Pages address, so I do not need to configure a custom domain or write DNS records for the first launch. If I later buy a domain, I would add the records requested by the host, verify that the record points to the correct GitHub Pages or hosting address, wait for DNS propagation, and then confirm HTTPS on the final address.

## Hosting decision

I chose GitHub Pages because the portfolio is static, the repository is already public, and the deployment workflow is easy to inspect. A commit to main triggers the workflow, the site files are uploaded, and GitHub serves them over HTTPS.

The source project uses Next.js and TypeScript. The public copy is plain HTML and CSS so the deployed files remain understandable and maintainable.

## First real reaction

The first reviewer was the portfolio owner, a data and AI professional who used the site during the build. They liked the typography, layout, and technology direction. Their practical feedback was to increase small text, use dark blue and violet, add a Portuguese page, correct the repository count from eight to sixteen, and narrow the work section to four projects. Those changes are now live.

## Still rough

- There is no custom domain yet.
- The contact action is email rather than a scheduling system.
- The English and Portuguese files are maintained separately.
- The project cards are short summaries, not full case studies.
- A physical phone and private-window check should still be performed before final launch.

## Repository

https://github.com/cleidyanne-castro/cleidyanne-castro
