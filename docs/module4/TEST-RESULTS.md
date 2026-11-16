# Module 4 — browser and optimization test results

**Method:** Chromium via Playwright; actual project HTML/CSS loaded in memory with the stylesheet embedded and exact WebP bytes served as browser Blob URLs. Direct local and HTTP navigation is blocked by the managed browser environment. This preserves browser layout, image decoding and srcset selection, but is not a published HTTP network benchmark. The test forced lazy images to load for inspection; production markup retains lazy loading. All 6 pages were checked at 320, 402, 720, 744, and 1440 CSS pixels (30 runs), with zero document-level horizontal overflow and all images decoded. See browser-results.json for every page and image. 

| Page | Viewport | Selected image and rendered size (px) | Horizontal overflow (px) |
| --- | --- | --- | --- |
| index.html | 402 | hero-480.webp (368×229), breakfast-avocado-toast-480.webp (368×207), lunch-chicken-rice-480.webp (368×207), snack-yogurt-granola-480.webp (368×207) | 0 |
| recipe.html | 402 | one-pan-veggie-pasta-480.webp (368×229) | 0 |
| index.html | 744 | hero-480.webp (323×201), breakfast-avocado-toast-480.webp (326×183), lunch-chicken-rice-480.webp (326×183), snack-yogurt-granola-480.webp (326×183) | 0 |
| recipe.html | 744 | one-pan-veggie-pasta-768.webp (686×428) | 0 |
| index.html | 1440 | hero-768.webp (480×299), breakfast-avocado-toast-480.webp (366×206), lunch-chicken-rice-480.webp (366×206), snack-yogurt-granola-480.webp (366×206) | 0 |
| recipe.html | 1440 | one-pan-veggie-pasta-768.webp (480×299) | 0 |

## Zoom, accessibility, font fallback and preferences

- Actual browser zoom: a headed Chromium window was operated using the browser keyboard zoom controls. At 100%, the viewport was 1440 CSS px and DPR 1; at 200%, it was 720 CSS px and DPR 2. All six pages showed decoded images and no horizontal overflow (scrollWidth was 8px less than innerWidth because of the scrollbar). See zoom-results.json and the two zoom screenshots. This is actual browser zoom, not merely a narrow-viewport proxy.
- Alt text: browser accessibility tree confirms the decorative hero is omitted, the three card images have names and each link has a descriptive dish title; recipe images have descriptive alt attributes. See accessibility-font-results.json. No audio/video/SVG/embed captions, transcripts, or labels are required because none are present. Ornamental text glyphs are hidden from assistive technology.
- Keyboard: 12 consecutive Tab stops on the 402px homepage had solid focus outlines, including skip link, navigation, CTA, all three recipe cards and the pasta link. Reduced-motion emulation changed scroll behavior to auto. The existing contrast preference and print rules remain in CSS.
- Font: computed stacks are Georgia/Times New Roman/serif and Trebuchet MS/Arial/sans-serif; Chromium's actual platform fonts were Tinos and Arimo in this environment. Forced missing preferred families fell back to serif/sans-serif with zero overflow. No web font requests were observed. Actual font availability varies by device.

## Slow-delivery simulation and layout stability

At 402px, the homepage was loaded without image sources, then the real image bytes were assigned after a 1.2-second delay. Before/after captures show reserved media space. The hero and all three image wrappers and card bodies retained identical offsetTop and offsetHeight values (see browser-results.json); the sum of observed layout-shift entries was 0. This isolates layout stability during late image arrival. It is **not** a measured Slow 3G transfer, and no live-network load-time or Lighthouse score is claimed. The screenshot pair is delayed-before.png and delayed-after.png.

For a real network check before release: serve the project through a local development server or published preview, open Chrome DevTools Network, disable cache, choose Slow 3G/Slow 4G, reload at 402 and 1440px, scroll to the cards, and inspect the selected image URLs, transferred sizes and any unexpected layout shift in Performance. Record results from the actual network session; this remains unverified here. All measured WebP file sizes are below 300,000 bytes. Browser screenshots are from actual rendered project markup, not illustrative images.

## Scope

No Firefox/Safari or deployed-site check was performed. The recipe content is still a preview and not verified for cooking. The original Module 3 testing records are retained under docs/module3 as historical evidence.
