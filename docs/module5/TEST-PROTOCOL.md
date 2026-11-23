# Module 5 repeatable test protocol and evidence index

**Baseline:** Student Bites Module 4 final ZIP. **Build:** Module 5 revision. **Date:** 2026-11-22. **Browser:** Headless Chromium through Python Playwright. **Execution environment limitation:** HTTP and file URL navigation blocked; in-memory HTML/CSS/media used for Chromium testing. Tests therefore do not cover hosting, network response headers, or real network throttling.

## Steps to repeat

1. Open each of `index.html`, `recipe.html`, `tips.html`, `breakfast.html`, `lunch.html`, `snack.html` in a normal local Chrome browser.
2. Inspect each page's browser title and document outline: one H1, logical H2/H3 levels, header/nav/main/footer landmarks, descriptive links, `aria-current` where appropriate, alt text, labels and native element choices. Run `python tools/check_accessibility.py` for a reproducible automated *basic* structural check.
3. Without a mouse, press Tab from the top: first focus should be the skip link. Press Enter; focus should move to main. Continue with Tab and Shift+Tab: confirm visible focus and logical order. On Tips, test all three `details/summary` panels with Enter and Space. Ensure focus can exit.
4. In responsive DevTools set CSS width to 320, 402, 744 and 1440px, then confirm no horizontal scrolling, clipped text or hidden controls, with panels open and closed.
5. Set **actual Chrome zoom to 200%** from the browser menu, then check the pages again; this must be carried out on a regular browser because the evidence environment only permitted a 720px viewport proxy. Also test text spacing: line height 1.5, letter spacing .12em, word spacing .16em, paragraph spacing 2em.
6. Use a contrast checker to verify meaningful text, link, button, focus and current-page states: normal text ≥4.5:1, large text ≥3:1, relevant non-text UI indicators ≥3:1 where applicable.
7. In accessibility tree or with a screen reader, sample landmarks/headings/link names on Home and disclosure controls on Tips. Check image-alt decisions on recipe details. A speech output test remains to be conducted separately.
8. Run **axe DevTools/Lighthouse** from your local/hosted browser when available and export results. Record tool version, URL, timestamp, passes, violations and manual limitations. The included automated scanner is *not* a substitute.
9. Record issues as issue ID, page, steps, expected, observed, evidence, impact, priority, patch, retest and residual risk. See `REMEDIATION-LOG.md` for this build's seven fixes.

## Evidence actually gathered

- `automated-structural-audit.json`: Python/BeautifulSoup audit across six files; no rule failures after fixes.
- `browser-checks.json`: 24 responsive viewport runs (6 × four widths), plus six proxy-zoom and six text-spacing runs. All measured document widths were within viewport width. Image decoding measured on four core viewport sizes.
- `test-run-console.txt`: console summary of those runs.
- `accessibility-tree-sample.json`: Chromium accessibility-tree sample for Tips page and its three disclosure nodes.
- `index-402.png`, `index-744.png`, `index-1440.png` and corresponding `recipe`/`tips` screenshots: visual evidence of layout at representative widths.
- `index-zoom-equivalent-720.png`, `recipe-zoom-equivalent-720.png`: **not actual zoom**; 720px reflow proxy.
- `index-narrow-320.png`, `recipe-narrow-320.png`: 320px with text-spacing overrides.
- `REMEDIATION-LOG.md`: baseline vs fixed evidence and retests.
- `CONFORMANCE-SUMMARY.md`: bounded findings, non-applicable components and unfinished checks.

## Limits of interpretation

This package does **not** include a third-party axe/Lighthouse report, physical keyboard user session, real screen-reader speech, actual browser zoom at 200%, network throttling or full WCAG 2.2 AA audit. Don't describe simulated/automated keypresses as human manual tests, and don't describe a responsive-width proxy as actual browser zoom. Those checks are explicitly described in the remaining-checks section rather than silently claimed as completed.
