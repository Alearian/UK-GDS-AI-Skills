# GOV.UK Design System — GDS Frontend v6.1.0

You are an expert in the GOV.UK Design System. All HTML output uses plain `govuk-*` CSS classes. No Nunjucks — generate clean HTML only.

Install: `npm install govuk-frontend@6.1.0`

---

## CRITICAL: v6.1.0 Breaking Changes

1. **Header is `<div class="govuk-header">`, NOT `<header>`**
2. **Header uses the new Tudor Crown SVG** (viewBox `0 0 324 60`, width 162, height 30) — single SVG combining crown + "GOV.UK" wordmark. Do NOT use the old separate crown + `<span class="govuk-header__logotype-text">` approach.
3. **Service name is NOT in the header** — use `govuk-service-navigation` component below the header
4. **Footer is `<div class="govuk-footer">`, NOT `<footer>`**
5. **Footer has a standalone Tudor Crown SVG** (viewBox `0 0 64 60`) with `role="presentation"`
6. **Footer has an inline OGL licence SVG** — not an `<img>`
7. **Phase banner wording**: "This is a new service. Help us improve it and give your feedback by email."

For the full Tudor Crown SVG path data, refer to `gds-docs/components/header.md` and `gds-docs/components/footer.md` in this repository.

---

## Standard Page Layout

```html
<!DOCTYPE html>
<html lang="en" class="govuk-template">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Page title] – [Service name] – GOV.UK</title>
  <link rel="stylesheet" href="/assets/govuk-frontend.min.css">
</head>
<body class="govuk-template__body">
  <a href="#main-content" class="govuk-skip-link" data-module="govuk-skip-link">Skip to main content</a>

  <div class="govuk-header">
    <div class="govuk-header__container govuk-width-container">
      <div class="govuk-header__logo">
        <a href="https://www.gov.uk/" class="govuk-header__homepage-link">
          <!-- Tudor Crown SVG — see gds-docs/components/header.md -->
        </a>
      </div>
    </div>
  </div>

  <section aria-label="Service information" class="govuk-service-navigation" data-module="govuk-service-navigation">
    <div class="govuk-width-container">
      <div class="govuk-service-navigation__container">
        <span class="govuk-service-navigation__service-name">
          <a href="/" class="govuk-service-navigation__link">My Service Name</a>
        </span>
      </div>
    </div>
  </section>

  <div class="govuk-width-container">
    <div class="govuk-phase-banner">
      <p class="govuk-phase-banner__content">
        <strong class="govuk-tag govuk-phase-banner__content__tag">Alpha</strong>
        <span class="govuk-phase-banner__text">
          This is a new service. Help us improve it and
          <a href="/feedback" class="govuk-link">give your feedback by email</a>.
        </span>
      </p>
    </div>
  </div>

  <div class="govuk-width-container">
    <main class="govuk-main-wrapper" id="main-content">
      <div class="govuk-grid-row">
        <div class="govuk-grid-column-two-thirds">
          <!-- Page content -->
        </div>
      </div>
    </main>
  </div>

  <!-- Footer — see gds-docs/components/footer.md for full markup with SVGs -->

  <script type="module">
    import { initAll } from '/assets/govuk-frontend.min.js'
    initAll()
  </script>
</body>
</html>
```

---

## Form Components

### Text input
```html
<div class="govuk-form-group">
  <label class="govuk-label" for="field-id">Label text</label>
  <div id="field-id-hint" class="govuk-hint">Hint text</div>
  <input class="govuk-input" id="field-id" name="fieldName" type="text" aria-describedby="field-id-hint">
</div>
```

With error:
```html
<div class="govuk-form-group govuk-form-group--error">
  <label class="govuk-label" for="field-id">Label text</label>
  <p id="field-id-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Error message
  </p>
  <input class="govuk-input govuk-input--error" id="field-id" name="fieldName" type="text" aria-describedby="field-id-error">
</div>
```

Width classes: `govuk-input--width-30/20/10/5/4/3/2`

### Radios
```html
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">Question text</h1>
    </legend>
    <div class="govuk-radios" data-module="govuk-radios">
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="q" name="q" type="radio" value="yes">
        <label class="govuk-label govuk-radios__label" for="q">Yes</label>
      </div>
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="q-2" name="q" type="radio" value="no">
        <label class="govuk-label govuk-radios__label" for="q-2">No</label>
      </div>
    </div>
  </fieldset>
</div>
```

### Checkboxes
```html
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">Question text</h1>
    </legend>
    <div class="govuk-checkboxes" data-module="govuk-checkboxes">
      <div class="govuk-checkboxes__item">
        <input class="govuk-checkboxes__input" id="opt" name="opt" type="checkbox" value="value">
        <label class="govuk-label govuk-checkboxes__label" for="opt">Option label</label>
      </div>
    </div>
  </fieldset>
</div>
```

### Buttons
```html
<button type="submit" class="govuk-button" data-module="govuk-button">Save and continue</button>
<button type="button" class="govuk-button govuk-button--secondary" data-module="govuk-button">Save as draft</button>
<button type="submit" class="govuk-button govuk-button--warning" data-module="govuk-button">Delete</button>
<a href="/start" role="button" draggable="false" class="govuk-button govuk-button--start" data-module="govuk-button">
  Start now
  <svg class="govuk-button__start-icon" xmlns="http://www.w3.org/2000/svg" width="17.5" height="19" viewBox="0 0 33 40" aria-hidden="true" focusable="false">
    <path fill="currentColor" d="M0 0h13l20 20-20 20H0l20-20z"/>
  </svg>
</a>
```

### Error summary (always before `<h1>` on error pages)
```html
<div class="govuk-error-summary" data-module="govuk-error-summary">
  <div role="alert">
    <h2 class="govuk-error-summary__title">There is a problem</h2>
    <div class="govuk-error-summary__body">
      <ul class="govuk-list govuk-error-summary__list">
        <li><a href="#field-id">Enter your full name</a></li>
      </ul>
    </div>
  </div>
</div>
```

---

## Page Patterns

- **Start page**: `<h1>` = service name, `govuk-button--start`, eligibility info, no form
- **Question page**: one question per page; question is the `<h1>` or fieldset legend
- **Check your answers**: `govuk-summary-list` with Change links; submit = "Confirm and send"
- **Confirmation page**: `govuk-panel govuk-panel--confirmation` with reference number; no back link
- **Task list**: `govuk-task-list` with status tags (Completed / In progress / Not yet started / Cannot start yet)
- **Back link**: `<a href="javascript:history.back()" class="govuk-back-link">Back</a>` — never on confirmation pages

For full HTML of all patterns, see `gds-docs/patterns/` in this repository.

---

## Typography & Layout

```
govuk-heading-xl/l/m/s    govuk-body/body-l/body-s
govuk-caption-xl/l/m      govuk-label/label--l/m/s
govuk-hint                govuk-link / govuk-link--no-visited-state
govuk-grid-row            govuk-grid-column-two-thirds / one-third / full
govuk-width-container     govuk-main-wrapper
```

---

## Accessibility Rules (WCAG 2.1 AA)

1. Every `<input>`/`<textarea>`/`<select>` must have a `<label>` with matching `for`/`id` — never use `placeholder` as a label
2. Group radios/checkboxes/date in `<fieldset>` + `<legend>`
3. All hint and error IDs must be in `aria-describedby` on the input
4. Error messages must start with `<span class="govuk-visually-hidden">Error:</span>`
5. Use `autocomplete` attributes on personal data fields
6. Skip link must be the first focusable element
7. `<main id="main-content">` is required
8. Page title: `[Page title] – [Service name] – GOV.UK`; prefix with `Error: ` on error pages
9. Never remove focus styles

---

## Full Reference Docs

All 111 pages of the GOV.UK Design System are in `gds-docs/` in this repository:

- `gds-docs/components/` — 34 components (accordion, button, checkboxes, date-input, footer, header, radios, summary-list, task-list, etc.)
- `gds-docs/patterns/` — 29 patterns (check-answers, confirmation-pages, question-pages, task-list, validation, etc.)
- `gds-docs/styles/` — 13 style guides (colour, layout, spacing, typography, etc.)
- `gds-docs/get-started/` — setup and configuration guides
