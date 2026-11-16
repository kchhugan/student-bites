# Module 3 — Responsive Layout Notes

**Project:** Student Bites (extension of the submitted Module 2 CSS architecture)

## What changed and why

The seven-layer architecture and the sage/cream design were retained. This work extends the existing `css/styles.css` rather than replacing the site or introducing a second stylesheet. The original Module 2 stylesheet is kept in `docs/module2/styles-before-module3.css` for comparison.

- **Wrapper and spacing:** `.container` uses a maximum inline size and automatic inline margins. Sections use block-axis padding, and the hero gets fluid space with `clamp()`. This makes widths less dependent on a particular writing direction and avoids fixed-height content boxes.
- **Intrinsic Grid 1:** `.recipe-grid` uses `repeat(auto-fit, minmax(min(100%, 17rem), 1fr))`. Cards need enough room for a title and the time/cost label; columns emerge when the parent is wide enough, rather than being forced by device categories.
- **Intrinsic Grid 2:** `.recipe-body` uses `repeat(auto-fit, minmax(min(100%, 22rem), 1fr))` for readable ingredient and instruction panels. When both panels cannot fit at their useful minimum width, they stack. `.tips-grid` uses another `auto-fit` pattern with a 16rem minimum.
- **Container query:** `.recipe-intro__copy` becomes a named `recipe-summary` query container. The reusable `.recipe-stats` component starts with three columns, changes to two if its container is narrower than 29rem, and to one below 21rem. This matters when the recipe summary is beside an image, stacked below it, or reused in a narrower section.
- **Breakpoint reasoning:** The header rearranges below 60rem because its long navigation labels start to compete with the brand. The hero stacks below 42rem because its text and placeholder image cannot both remain readable in two columns. These are content-fit decisions; card and tips grids do not need explicit viewport breakpoints to choose their column counts.
- **Logical properties:** Main wrapper uses `inline-size` and `margin-inline`. Ingredient list indentation uses `padding-inline-start`; budget tip accent uses `border-inline-start`; the skip link uses logical inset offsets. Existing component classes, tokens, focus styles, and print rules remain.

## Subgrid decision

Subgrid was considered for the three homepage cards. These are short, independent content groups with only title and metadata, so they do not need to share individual internal rows across cards yet. A normal auto-fit grid is simpler and avoids unnecessary coupling between cards. Revisit subgrid after real recipe titles and metadata are available if cross-card row alignment becomes necessary.

## Progressive enhancement / fallback

The three-column recipe statistics style is the readable base layout. `@supports (container-type: inline-size)` establishes the query container in supporting browsers; the `@container` rules progressively adjust the number of columns. When container queries are unsupported, the existing three-column version remains, with wrapping text, and the page-level Grid/layout still works. `minmax()` + `auto-fit` are broadly supported Grid features. Basic content is readable even without CSS.

## Preference settings

`prefers-reduced-motion: reduce` turns off smooth scroll and pressed-button motion. `prefers-contrast: more` darkens border/secondary-text values and strengthens the focus ring. Focus styling remains visible by keyboard through `:focus-visible`.

## Content status and next steps

The photo areas are intentionally placeholders, consistent with the Module 1 plan. The categories still lead to a single sample recipe template rather than finished recipes. That is a known prototype limitation and should be corrected before the final site launch. Verify final titles, prices, ingredient quantities, cooking directions, image rights, and image sizes before publishing. These are not Module 3 layout features.

## Verification

See `docs/module3/TEST-RESULTS.md` for browser results, the 720px reflow proxy and separately reported manual 200% browser zoom check, keyboard focus, contrast/reduced-motion, print checks, screenshot evidence and remaining limitations.

## AI disclosure

I used ChatGPT to help extend and organize the responsive CSS, review the layout decisions against my Figma work and Module 2 files, and prepare these notes. I reviewed the proposed Grid patterns, container query, and fallback approach; the CSS was adjusted to preserve the existing Student Bites page structure. Automated browser checks were performed on the HTML/CSS content, with limitations documented in the testing notes.
