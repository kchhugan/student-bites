# CSS Architecture Notes — Student Bites

## Scope and visual direction
The homepage and recipe-detail page use the layout patterns from the Module 1 desktop wireframes: a horizontal navigation bar, two-column hero, three featured cards, a two-part recipe introduction, side-by-side ingredients and steps, and a distinct budget tip. The palette is a provisional cream, sage, and warm green treatment rather than a literal grayscale wireframe. No completed recipe or final photo is claimed.

## Cascade strategy
`@layer reset, base, layout, components, utilities, states, overrides;` establishes the order for normal author declarations. `reset` removes inconsistent defaults; `base` contains shared tokens, typography, and fundamental rules; `layout` manages compositions and responsive grids; `components` defines patterns; `utilities` provides limited helpers; `states` handles interactive feedback; `overrides` is reserved for rare exceptions. Print rules are collected in a separate `@media print` block with appropriate layer placement.

## Tokens and component scopes
Purpose-based custom properties cover backgrounds, surfaces, ink, borders, links, focus, type scale, spacing, widths, shape, and shadows. For example, `--color-forest`, `--space-5`, and `--focus-ring` are used across repeated patterns. `--button-background`, `--button-foreground`, and `--button-border` are component-local values, while `--card-padding` and `--callout-accent` control component adjustments. The color names are provisional design choices, not requirements from Module 1.

## Components and utilities
Reusable components include the header/navigation, hero, call-to-action button, recipe card, photo placeholder, recipe statistics, detail panel, budget tip callout, expandable tip disclosure, and footer. Utilities include `u-skip-link`, `u-flow`, `u-measure`, `u-text-center`, and `u-mt-4`. Classes use readable, hyphenated names; element variants use `--` and component parts use `__`. CSS avoids deep selectors and ID-based styling.

## Accessibility and states
The navigation marks the current page using `aria-current="page"`; links and buttons have visible `:focus-visible` outlines; cards have a `:focus-within` state; buttons have `:hover` and `:active` states; native `<details>` components receive `[open]` styling. The skip link becomes visible on focus. The compact-width navigation stays fully accessible without pretending an unimplemented menu icon works.

## Print and performance
The recipe detail page has a simplified print layout with readable ingredient and instruction sections, reduced decoration, and hidden site navigation and image placeholders. The site uses no external fonts or image downloads. Replacing placeholders with original or licensed images later requires alt text and the planned image-size checks.

## Browser testing
See `TEST-RESULTS.md` for checks conducted on a representative browser environment and screenshots. Testing in Firefox, Safari, and on physical devices remains to be done. The package does not claim a deployed preview.

## AI disclosure
**AI Disclosure**

I used ChatGPT to help improve the website layout based on my Figma wireframes, and review the assignment requirements. It also helped me refine my design decisions and organize my documentation.
