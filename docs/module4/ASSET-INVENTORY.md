# Student Bites — asset inventory and provenance

## Images

The five source PNGs were generated with ChatGPT for Student Bites on November 14, 2026. They are food illustrations, not evidence of cooked or tested recipes. No stock-photo source, photographer, or external license is claimed. The source archive is `Student_Bites_Module4_Original_Images.zip` (kept separately); the optimized website files are in `assets/`. Original hashes, dimensions and exact byte counts are in `asset-metrics.json`.

**Permission basis for every row:** OpenAI Terms of Use, effective January 1, 2026, ownership of content: between the user and OpenAI, the user owns output to the extent permitted by applicable law. This is not a Creative Commons license or a guarantee of copyright or third-party clearance. Source: https://openai.com/policies/terms-of-use/ (checked November 14, 2026).

| Source filename | Placement | Original format, dimensions, bytes | Current variants and bytes | Purpose and alternative |
| --- | --- | --- | --- | --- |
| hero.png | Homepage hero | PNG 1672×941; 2,253,303 B | WebP: 480×270 (24,142 B); 768×432 (47,524 B); 1200×675 (90,676 B) | Decorative; alt="" (intro provides context) |
| breakfast-avocado-toast.png | Breakfast card and preview | PNG 1536×1024; 2,644,638 B | WebP: 480×320 (31,842 B); 768×512 (69,854 B); 1200×800 (140,910 B) | Informative: Avocado toast with a fried egg and fruit |
| lunch-chicken-rice.png | Lunch card and preview | PNG 1536×1024; 2,748,988 B | WebP: 480×320 (36,008 B); 768×512 (80,946 B); 1200×800 (161,900 B) | Informative: Rice bowl with grilled chicken and roasted vegetables |
| snack-yogurt-granola.png | Snacks card and preview | PNG 1536×1024; 2,599,838 B | WebP: 480×320 (28,040 B); 768×512 (62,936 B); 1200×800 (127,398 B) | Informative: Yogurt with granola, banana, strawberries and blueberries |
| one-pan-veggie-pasta.png | Pasta detail preview | PNG 1536×1024; 2,755,221 B | WebP: 480×320 (34,454 B); 768×512 (79,860 B); 1200×800 (168,788 B) | Informative: Penne with tomatoes, bell peppers, zucchini and herbs |

Every width variant has the same composition as its original. The original ratio is retained in the resized file; the CSS display crop is centered. The card versions are reused in their own recipe previews, not duplicated. The hero has an empty alt attribute because it is decorative; the card and detail photos have descriptive alt attributes. Card links also include readable dish titles. Final recipe content still needs verification against the illustrations.

## Other media

| Asset/type | Source / permission | Accessibility and delivery |
| --- | --- | --- |
| Decorative star and arrow glyphs | Unicode text in existing HTML, rendered by local fonts; no image files | aria-hidden on ornamental glyphs; adjacent text supplies meaning |
| SVG | None used | No SVG label required |
| Audio / video | None used or planned for this build | Captions/transcripts/player controls not applicable |
| External embeds | None | No third-party requests, embed titles or privacy controls needed |
| CSS motion | Existing smooth scroll and button active transform | Reduced-motion query disables these; no autoplay or timed animation |
| Expandable tips | Native HTML details/summary, existing project content | Built-in keyboard interaction; no external embed or script |

## Typography

| Family | Role / source | License and loading | Weights/styles |
| --- | --- | --- | --- |
| Georgia | Preferred heading, Microsoft system typeface | Proprietary installed font; CSS reference only | Normal; CSS 500 (nearest available weight if unavailable) |
| Times New Roman | Heading fallback, system typeface | Proprietary installed font; CSS reference only | Normal; nearest available heading weight |
| Trebuchet MS | Preferred body, Microsoft system typeface | Proprietary installed font; CSS reference only | Normal 400, bold 700 |
| Arial | Body fallback, system typeface | Proprietary installed font; CSS reference only | Normal 400, bold 700 |
| serif / sans-serif | Generic platform fallback | Browser/OS supplied; no bundled font | Browser-selected |

Heading stack: Georgia, Times New Roman, serif. Body stack: Trebuchet MS, Arial, sans-serif. No downloaded font, font-face, remote font import or font redistribution. Microsoft's font FAQ permits referencing Windows fonts by name in CSS, but does not grant self-hosting or conversion rights. Sources: https://learn.microsoft.com/en-us/typography/fonts/font-faq ; https://learn.microsoft.com/en-us/typography/font-list/georgia ; https://learn.microsoft.com/en-us/typography/font-list/trebuchet-ms .

The browser test environment rendered Tinos and Arimo as local substitutions, rather than assuming the preferred fonts were installed. The generic fallback test is recorded in `accessibility-font-results.json`.
