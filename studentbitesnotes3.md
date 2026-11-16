# Student Bites — Responsive Layout Systems Build (Module 3)

This ZIP extends the Student Bites Module 2 CSS architecture with intrinsic CSS Grid layouts, container-based recipe information, logical properties, and documented fallback behavior. The green/cream design and sample HTML pages are preserved.

## Open Locally

Extract the ZIP, then open `index.html` in a browser. The stylesheet is `css/styles.css`. Visit `recipe.html` and `tips.html` too. The sample recipe content and image boxes are placeholders; they are not finalized recipes or licensed photography.

## Files

- `index.html`: homepage, navigation, hero, and featured recipe cards
- `recipe.html`: recipe detail template and container-query recipe stats
- `tips.html`: budget tip disclosure grid
- `css/styles.css`: one CSS system, extending Module 2's layers and variables
- `docs/LAYOUT-NOTES.md`: architecture explanation, breakpoint rationale, subgrid decision, feature fallback, and AI disclosure
- `docs/module3/TEST-RESULTS.md`: test record and limitations
- `docs/module3/*.png`: selected browser screenshots
- `docs/module3/results.json`: computed browser observations
- `docs/module2/`: original Module 2 evidence and its previous stylesheet

## Testing and Manual Review

The responsive layouts were tested at narrow, medium, and wide viewport widths. Additional checks covered container-query behavior, keyboard focus, reduced motion, increased contrast, and print styling.

I also manually checked the website using the browser's actual **200% zoom** setting and confirmed that the layout remained usable.

Before submission, the remaining recommended checks are to Tab through the full navigation, open the expandable tips, inspect the recipe print preview, and review the website in Firefox or Safari if available.

No repository URL or published preview is claimed in this package.