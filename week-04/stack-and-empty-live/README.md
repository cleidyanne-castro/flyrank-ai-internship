# Week 4: Pick the Stack

## Constraints

- Free hosting
- A beginner-readable build
- Real repository links
- A strong visual hierarchy for data and AI work
- English and Portuguese content
- No backend required for the first public version
- A deployment path I can explain and maintain

## Three roads considered

### No-code builder

A tool such as Carrd or Framer would publish quickly and reduce implementation work. The trade-off is less control over the layout and less evidence that I can maintain the site itself.

### Plain HTML and CSS on a free host

This is the smallest technical option. It is easy to inspect and works well for a static portfolio. The trade-off is that repeated content and language variants need more manual maintenance.

### Next.js and TypeScript with a static GitHub Pages copy

This gives a structured source project, reusable components, and a clear path for future features. The trade-off is more setup than a plain page and a build step that I need to understand.

## Decision

I chose Next.js and TypeScript for the source project, with a static HTML copy deployed on GitHub Pages.

The source structure is useful while the portfolio grows. The public copy is simple enough for the browser and easy to inspect in the repository. This is the smallest setup that still gives me room to maintain repeated project cards, an English route, and a Portuguese route.

The two options I did not choose were no-code and plain HTML only. No-code would publish faster but would hide too much of the implementation I want to learn. Plain HTML only would work now, but would make the source harder to extend as the portfolio gains case studies.

Can I maintain this? Yes. The project is small, the content is explicit, the build is reproducible, and the deployed files remain understandable without the framework.

## Empty but live milestone

The selected repository and GitHub Pages workflow established the near-blank public milestone before the full portfolio was filled in.

Current live URL:

https://cleidyanne-castro.github.io/cleidyanne-castro/

The empty milestone has since been superseded by the finished public portfolio. No screenshot is claimed here because the early blank state was not preserved as a separate public artifact.
