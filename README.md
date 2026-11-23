# Student Bites — Module 5 Accessibility Conformance and Inclusive Quality Build

This version builds on the **Module 4** media/typography package; the sage/cream palette, responsive WebP assets, CSS layers, responsive layout and recipe-preview content are retained. Module 5 adds accessibility improvements (more usable navigation targets, page-level breadcrumb orientation, distinct pasta browser title, less repetitive card link names, explicit skip destination focus support and enhanced disclosure focus), plus evidence and a seven-item remediation log.

## Open the project

Open `index.html` from this folder in a browser. Navigation links lead to the four recipe previews and Tips; all assets are local. This capstone still contains unverified recipe instructions/costs and is **not** a complete public recipe resource.

## Submission evidence

- `docs/module5/CONFORMANCE-SUMMARY.md`: scope, observed behavior, contrasts, media decisions and limitations.
- `docs/module5/REMEDIATION-LOG.md`: seven findings with evidence, impact, priority, fix and retest.
- `docs/module5/TEST-PROTOCOL.md`: repeatable steps, evidence index and explicitly pending checks.
- `docs/module5/automated-structural-audit.json`: project-specific static automated audit (not axe/Lighthouse).
- `docs/module5/browser-checks.json`: in-memory Chromium responsive/reflow/keyboard observations.
- `docs/module5/accessibility-tree-sample.json`: sampled Chromium accessibility tree for Tips.
- `docs/module5/*.png`: browser screenshots; proxy zoom images clearly labeled.
- `tools/check_accessibility.py`: repeatable static accessibility checker. Requires `beautifulsoup4`.
- `docs/module4/`, `docs/module3/` and `docs/module2/`: earlier module evidence retained.

## Repository and submission

Repository: https://github.com/kchhugan/student-bites

This ZIP is the **Module 5 revision**. The repository was created during Module 4; to make it represent this Module 5 build, upload the revised files and folders from this ZIP and commit the changes. No claim is made that the repository already contains the Module 5 revision or that a published preview exists.

## Honest testing boundary

Chromium testing was performed with in-memory HTML/CSS/images because local/HTTP navigation was blocked in the test environment. The current evidence includes a custom structural checker (not an axe or Lighthouse scan), programmatic browser-assisted keyboard/reflow tests, contrast calculations and accessibility-tree inspection. True browser zoom, manual whole-site keyboard navigation, axe/Lighthouse, real screen-reader speech and cross-browser checks remain for release testing. See conformance summary for details.
