# Week 9: Break It, Then Launch It

## Hardening target

https://cleidyanne-castro.github.io/cleidyanne-castro/

## Where it breaks

### Fixed now

- The portfolio had no social sharing metadata. Page title, description, and Open Graph tags are now present on the English and Portuguese pages.
- The project list was too broad. It now contains four focused projects.
- The repository count was inaccurate. It now shows sixteen public repositories.
- The site needed a Portuguese route. The live `pt.html` page is reachable from the English page.

### Known limitations

- The site is hosted on the GitHub Pages subdomain, not a custom domain.
- Analytics has not been installed.
- A FlyRank graduate badge has not been added because there is no verification URL available in this repository.
- A physical phone test and formal hardening review still need to happen.
- The live site has no server-backed contact form. The Week 8 project filter is client-side.

## Checks performed

- Verified that the English page links to all four selected public repositories.
- Verified that the Portuguese page links to the same four repositories.
- Verified that the English and Portuguese pages have titles and descriptions.
- Verified that the English and Portuguese pages contain Open Graph title and description tags.
- Ran the local production build successfully.
- Checked that the responsive CSS includes a narrow-screen layout.
- Checked that the new project filter has All, AI, Data, and Analytics states.

## Fix-now decision

The metadata and clarity issues were fixed in the public files. The domain, analytics, badge, and physical-device review are launch requirements that cannot be honestly claimed without the corresponding account, verification URL, or device evidence. They remain visible here as known limitations.
