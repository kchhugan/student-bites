# Module 4 — media and typography optimization

## Changes from Module 3

I kept the layered stylesheet, sage/cream colors, intrinsic grids, logical wrappers, recipe-stat container query and preference rules. I replaced the five placeholder regions with responsive images and added three recipe previews using the existing detail template. Each featured card now opens its own dish preview instead of the pasta page. The original pasta preview remains accessible from the homepage. Quantities, times and prices remain clearly unverified; this is not a completed recipe collection.

## Image decisions

- Original PNGs were resized to 480, 768 and 1200 pixels wide, preserving source ratio, using Lanczos resampling and WebP quality 82. Exact bytes/dimensions are in the inventory and JSON. The largest output is 168,788 bytes, below the 300 KB target from the planning package. The five originals total 13,001,988 bytes; the 15 optimized variants are stored locally, and browsers request only the selected candidate per image.
- Each img has a width-descriptor srcset, a sizes attribute, a 768px default src, explicit intrinsic width/height, and async decoding. The hero and detail image use high fetch priority; featured cards use lazy loading. Sizes correspond to the actual layout: single-column cards below ~632px, two columns until ~936px, three above; hero stacks at 42rem, detail stacks at 60rem. The largest detail region is the stacked tablet width, so its sizes expression differs from the hero's. Sizes are estimates of content width, not exact CSS pixel promises.
- Art direction: one composition is enough because the main dishes are centered and remain identifiable in the mobile and desktop crops. The hero/detail region uses 16:10 and cards use 16:9 with object-fit: cover. The browser captures show the actual crops at 402, 744 and 1440px. No text is embedded in the images. A separate picture source or alternate crop is not needed for these compositions. WebP is supported by the current Chrome/Firefox/Safari target; text and descriptive alt remain available if an image cannot load. No legacy JPEG delivery is included.
- The original assets were not placed in the serving folder, preventing accidental downloads of multi-megabyte PNGs. The source archive is retained separately. No asset is loaded from a third-party host.

## Typography and stability

The base type remains 1rem (16px at default browser settings) with line-height 1.65. Heading sizes use clamp(2.35rem, 4.3vw, 4.15rem) for H1 and clamp(2rem, 3.4vw, 3rem) for H2; H3 is 1.3rem. Headings use line-height 1.14, 500 weight and Georgia; body uses Trebuchet MS 400/700. Paragraph measure is capped at 64ch. Reusable spacing tokens maintain rhythm; headings can wrap anywhere when needed, and card metadata uses the shared small-text token. The font stacks load locally, so no web-font request or font-display swap is necessary. Differences in installed font metrics can still change line wraps; the forced fallback test checks that content still fits.

Image wrappers reserve their aspect ratio before the image is loaded, so the text below them does not jump. The delayed-image test checks element positions before and after arrival and records layout-shift entries. Print continues to hide photographs and retain recipe text. Reduced motion is preserved; decorative symbols are hidden from assistive technology.

## Verification and remaining work

See TEST-RESULTS.md for actual Chromium results, including browser UI zoom and delayed-image simulation. The original Module 2/3 notes and screenshots are historical records, not current asset evidence. No live preview or repository URL has been created in this environment; add the actual repository link to the submission if publishing the project. Firefox/Safari, real network throttling, and final recipe accuracy remain unverified.

## AI disclosure

I used ChatGPT to generate the five food illustrations, help extend the Module 3 HTML/CSS for responsive images and typography, and prepare the asset inventory and test documentation. The generated images, resize choices, layout changes and alternatives were reviewed against the Student Bites plan; measured file sizes and browser observations are recorded separately. The original design was preserved, image placeholders were replaced, and the card destinations were corrected. The images are identified as generated rather than as photographs of tested recipes.
