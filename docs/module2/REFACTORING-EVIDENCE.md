# Refactoring Evidence — Architecture Examples

Student Bites is a first production architecture rather than a refactor of a previously published stylesheet. The examples below illustrate how duplicated or fragile CSS was avoided during the build; they are not presented as historical commits.

## Example 1: Shared surface tokens
Before (a fragile approach):
```css
.hero { background: #f6f0e7; }
.callout { background: #f6f0e7; }
```
After (the current strategy):
```css
:root { --color-cream: #f6f0e7; }
.hero, .callout { background: var(--color-cream); }
```
In the completed stylesheet, each component has its own rule but draws from the same token.

## Example 2: Shared cards instead of per-category CSS
Before (a fragile approach):
```css
.breakfast-card { padding: 1rem; border-radius: .65rem; }
.lunch-card { padding: 1rem; border-radius: .65rem; }
.snack-card { padding: 1rem; border-radius: .65rem; }
```
After:
```css
.recipe-card { --card-padding: 1.05rem; border-radius: var(--radius-md); }
.recipe-card__body { padding: var(--card-padding); }
```
All three featured cards share the same markup structure and classes.

## Example 3: Specificity control
Before (a fragile approach):
```css
header .primary-nav ul li a:hover { background: #e9eee3; }
```
After:
```css
@layer states { .site-nav a:hover { background: var(--color-sage-light); } }
```
Interaction states do not rely on long descendant chains.

## Example 4: Layout reuse
The desktop card grid uses one `.recipe-grid` class with breakpoint changes instead of three separate stylesheets. This also keeps the 402px, 744px, and 1440px layout goals in one place.
