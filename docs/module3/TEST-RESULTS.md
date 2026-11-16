# Module 3 Layout Test Results

**Method:** Chromium headless with Playwright. The three uploaded HTML files were loaded with their CSS embedded in memory because direct `file://` navigation is blocked in this environment. Results represent those HTML/CSS contents, not a published website or Firefox/Safari.

| Page | CSS viewport | Observed layout | Horizontal overflow |
| --- | --- | --- | --- |
| Home | 320px | One recipe-card column | None |
| Home | 402px | One recipe-card column | None |
| Home | 744px | Two recipe-card columns | None |
| Home | 1440px | Three recipe-card columns | None |
| Recipe | 320px | One-column details, one stat column | None |
| Recipe | 402px | One-column details, two stat columns | None |
| Recipe | 744px | One-column details, three stat columns | None |
| Recipe | 1440px | Two ingredient/instruction columns | None |
| Tips | 320px / 402px | One tip column | None |
| Tips | 744px | Two tip columns | None |
| Tips | 1440px | Three tip columns | None |

**200% zoom / reflow proxy:** With a nominal 1440px browser, 200% zoom leaves roughly 720 CSS pixels of usable width. I tested all three pages in a **720px CSS viewport**; none had document-level horizontal overflow. This was the automated viewport-equivalent reflow check, not a direct test of browser zoom. Separately, I manually tested the site using the browser's actual **200% zoom** setting and confirmed that the layout remained usable.

**Keyboard focus:** At 402px, keyboard Tab focused the visible skip link. The computed outline was solid. The other interactive elements use the same shared `:focus-visible` outline rule, but were not individually tab-tested.

**Container query:** The recipe summary component was forced to 250px, 390px, and 560px widths while the viewport stayed fixed at 1200px. The computed recipe-stat layout changed from one to two to three columns. This demonstrates container-based behavior independent of viewport width.

**User preferences:** Emulated `prefers-reduced-motion: reduce` yielded `scroll-behavior: auto`; emulated `prefers-contrast: more` changed the border token to `#5d645b`.

**Print:** In print media, the recipe page header was hidden, recipe-body became block layout, and the body background became white.

**Limitations:** Automated checks did not operate the browser zoom UI; the actual 200% zoom check was completed manually. Firefox, Safari, physical devices, and deployed URL checks remain unverified. The recipe texts and image placeholders are still unfinished content by design.

Screenshots and machine-readable observations are in this directory (`results.json`).
