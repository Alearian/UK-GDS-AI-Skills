---
name: gds-website-builder
description: >
  GOV.UK Design System (GDS) expert skill for GDS Frontend v6.3.0. Use this skill whenever the user
  asks to build, review, or design any page or component for a UK government service or GDS-compliant
  prototype application.

  ALWAYS use this skill for:
  - Writing HTML that uses govuk-frontend CSS classes
  - Implementing GDS page patterns (start page, question page, check-answers, confirmation, task list)
  - Choosing the right GDS component for a form field, message, or navigation need
  - Structuring a GOV.UK page layout (skip-link, header, service-navigation, phase-banner, main content, footer)
  - Making pages WCAG 2.1 AA accessible using GDS conventions
  - Handling form validation and error display the GDS way
  - Building GDS prototype apps using TypeScript + HTML or Nunjucks macros
  - Writing Nunjucks templates using govukButton, govukInput, govukRadios etc. macros
  - Setting up the GOV.UK Prototype Kit or an Express/Nunjucks app with govuk-frontend
  - Reviewing or fixing pages for GDS compliance

  Also trigger for: govuk, gov.uk design system, GDS component, govuk-frontend, government service,
  prototype kit pattern, one-thing-per-page, check your answers, confirmation page, phase banner,
  nunjucks macro, prototype kit, govukButton, govukInput, njk template
---

# GDS Website Builder Skill

GOV.UK Frontend v6.3.0 provides the CSS, JS, and component patterns for UK government services.
Output can use either **plain HTML** with `govuk-*` CSS classes, or **Nunjucks macros** (the
GOV.UK-approved server-side templating approach used by the Prototype Kit and production Node apps).

## Output format â€” ask the user first

**Before generating any component or page code**, if the user has not already indicated their stack,
ask:

> "Would you like the output as **plain HTML** (for React, TypeScript, or static sites) or as
> **Nunjucks macros** (for the GOV.UK Prototype Kit or an Express/Node app)?"

Only skip the question when the context makes it obvious:
- User mentions React, Next.js, TypeScript, or a static site â†’ plain HTML, no question needed
- User mentions Prototype Kit, `.njk`, Express, or Nunjucks â†’ Nunjucks macros, no question needed
- User explicitly says "HTML" or "Nunjucks" â†’ honour that, no question needed

If the user chooses Nunjucks, read `gds-docs/nunjucks-macros.md` before generating output.

**Choose based on context:**
- **Plain HTML** â†’ React, TypeScript, static sites, any non-Node stack
- **Nunjucks macros** â†’ GOV.UK Prototype Kit, Express/Node apps, server-rendered `.njk` templates

Install: `npm install govuk-frontend@6.3.0`

In your HTML `<head>`:
```html
<link rel="stylesheet" href="/govuk-frontend/dist/govuk/govuk-frontend.min.css">
```

Before `</body>`:
```html
<script type="module" src="/govuk-frontend/dist/govuk/govuk-frontend.min.js"></script>
<script type="module">
  import { initAll } from '/govuk-frontend/dist/govuk/govuk-frontend.min.js'
  initAll()
</script>
```

---

## Reference docs â€” selective loading

Three local reference sources are available. **Always read `DOCS_INDEX.md` first**, then
load only the specific file(s) needed. Never load all docs at once.

| Source | Location | What it contains |
|---|---|---|
| `DOCS_INDEX.md` | `~/.claude/skills/gds-website-builder/DOCS_INDEX.md` | Full index â€” read this first to find the right file |
| Design System docs | `~/.claude/skills/gds-website-builder/gds-docs/` | Components, patterns, styles, accessibility |
| Frontend how-to docs | `~/.claude/skills/gds-website-builder/gds-frontend-docs/` | NPM setup, CSS/JS importing, configuration |
| Source repo | `~/.claude/skills/gds-website-builder/gds_git/govuk-design-system/` | Nunjucks macros, SASS source |

### Quick lookup rules

- **Building a specific component** â†’ read `gds-docs/components/{component-name}.md`
- **Implementing a pattern** â†’ read `gds-docs/patterns/{pattern-name}.md`
- **CSS/JS setup, NPM install, or configuration** â†’ read from `gds-frontend-docs/`
- **Need Nunjucks macro or SASS variable** â†’ Grep `gds_git/govuk-design-system/`
- **Unsure what file to read** â†’ read `DOCS_INDEX.md` first, then the specific file

### Example: building a button component

```
1. Read DOCS_INDEX.md  â†’  confirms gds-docs/components/button.md exists
2. Read gds-docs/components/button.md  â†’  get the correct HTML
3. Done â€” no other files needed
```

Run the `gds-docs-update` skill to populate or refresh any of these sources.

---

## CRITICAL: v6.3.0 Breaking Changes from v5.x

The June 2025 GOV.UK brand refresh introduced several **breaking changes**. Always follow these rules:

1. **Header is a `<div>`, NOT a `<header>`** â€” use `<div class="govuk-header">`
2. **Header uses the new Tudor Crown SVG logotype** â€” a single combined SVG (viewBox `0 0 324 60`, width 162, height 30) containing both the crown graphic and "GOV.UK" wordmark. Uses `role="img"`, `aria-label="GOV.UK"`, and a `<title>` element. Do NOT use the old separate crown SVG + `<span class="govuk-header__logotype-text">` approach.
3. **Service name is NO LONGER in the header** â€” use the separate **Service navigation** component (`govuk-service-navigation`) below the header instead. The header `<div>` should contain ONLY the logo.
4. **Footer is a `<div>`, NOT a `<footer>`** â€” use `<div class="govuk-footer">`
5. **Footer has a standalone Tudor Crown SVG** â€” a crown-only SVG (viewBox `0 0 64 60`, width 32, height 30) with `role="presentation"` appears inside the footer container before the meta section.
6. **Footer has an inline OGL licence logo SVG** â€” replaces old image reference.
7. **Phase banner wording changed** â€” now uses "This is a new service. Help us improve it and give your feedback by email."

---

## Standard Page Layout

Every GDS page follows this structure:

```html
<!DOCTYPE html>
<html lang="en" class="govuk-template">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Page title] â€“ [Service name] â€“ GOV.UK</title>
  <link rel="stylesheet" href="/assets/govuk-frontend.min.css">
</head>
<body class="govuk-template__body">

  <!-- Skip link: MUST be first interactive element -->
  <a href="#main-content" class="govuk-skip-link" data-module="govuk-skip-link">Skip to main content</a>

  <!-- GOV.UK header (v6.3.0 â€” <div>, Tudor Crown logotype, NO service name) -->
  <div class="govuk-header">
    <div class="govuk-header__container govuk-width-container">
      <div class="govuk-header__logo">
        <a href="https://www.gov.uk/" class="govuk-header__homepage-link">
          <!-- Full Tudor Crown logotype SVG â€” see gds-docs/components/header.md -->
        </a>
      </div>
    </div>
  </div>

  <!-- Service navigation (service name lives HERE, not in the header) -->
  <section aria-label="Service information" class="govuk-service-navigation"
    data-module="govuk-service-navigation">
    <div class="govuk-width-container">
      <div class="govuk-service-navigation__container">
        <span class="govuk-service-navigation__service-name">
          <a href="/" class="govuk-service-navigation__link">My Service Name</a>
        </span>
      </div>
    </div>
  </section>

  <!-- Phase banner (Alpha/Beta) -->
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

  <!-- Main content -->
  <div class="govuk-width-container">
    <main class="govuk-main-wrapper" id="main-content">
      <div class="govuk-grid-row">
        <div class="govuk-grid-column-two-thirds">
          <!-- Page content here -->
        </div>
      </div>
    </main>
  </div>

  <!-- Footer (v6.3.0 â€” <div>, Tudor Crown SVG, OGL licence logo SVG) -->
  <!-- Full footer markup â€” see gds-docs/components/footer.md -->

  <script type="module">
    import { initAll } from '/assets/govuk-frontend.min.js'
    initAll()
  </script>
</body>
</html>
```

**Grid columns:** `govuk-grid-column-two-thirds` for content, `govuk-grid-column-one-third` for sidebar. Always wrap in `govuk-grid-row`.

---

## Core Form Components

### Text input

```html
<div class="govuk-form-group">
  <label class="govuk-label" for="full-name">Full name</label>
  <div id="full-name-hint" class="govuk-hint">As it appears on your passport</div>
  <input class="govuk-input" id="full-name" name="fullName"
         type="text" aria-describedby="full-name-hint" autocomplete="name">
</div>
```

With error:
```html
<div class="govuk-form-group govuk-form-group--error">
  <label class="govuk-label" for="ni-number">National Insurance number</label>
  <div id="ni-number-hint" class="govuk-hint">It's on your P60, for example QQ 12 34 56 C</div>
  <p id="ni-number-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Enter a National Insurance number in the correct format
  </p>
  <input class="govuk-input govuk-input--error" id="ni-number" name="niNumber"
         type="text" aria-describedby="ni-number-hint ni-number-error">
</div>
```

**Input width classes:** `govuk-input--width-30` (full), `govuk-input--width-20`, `govuk-input--width-10`, `govuk-input--width-5`, `govuk-input--width-4`, `govuk-input--width-3`, `govuk-input--width-2`

### Radios

```html
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">Have you changed your name?</h1>
    </legend>
    <div class="govuk-radios" data-module="govuk-radios">
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="changed-name" name="changedName" type="radio" value="yes">
        <label class="govuk-label govuk-radios__label" for="changed-name">Yes</label>
      </div>
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="changed-name-2" name="changedName" type="radio" value="no">
        <label class="govuk-label govuk-radios__label" for="changed-name-2">No</label>
      </div>
    </div>
  </fieldset>
</div>
```

Add `govuk-radios--inline` to the `govuk-radios` div for side-by-side layout (Yes/No questions).

### Checkboxes

```html
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">Which types of waste do you transport?</h1>
    </legend>
    <div id="waste-hint" class="govuk-hint">Select all that apply</div>
    <div class="govuk-checkboxes" data-module="govuk-checkboxes">
      <div class="govuk-checkboxes__item">
        <input class="govuk-checkboxes__input" id="waste" name="waste" type="checkbox" value="carcasses">
        <label class="govuk-label govuk-checkboxes__label" for="waste">Carcasses</label>
      </div>
      <div class="govuk-checkboxes__item">
        <input class="govuk-checkboxes__input" id="waste-2" name="waste" type="checkbox" value="mines">
        <label class="govuk-label govuk-checkboxes__label" for="waste-2">Mines</label>
      </div>
    </div>
  </fieldset>
</div>
```

### Textarea, Select, Date input, File upload, Password input

See the collated GDS docs for full HTML of these form components:
- `gds-docs/components/textarea.md`
- `gds-docs/components/select.md`
- `gds-docs/components/date-input.md`
- `gds-docs/components/file-upload.md`
- `gds-docs/components/password-input.md`

---

## Buttons

```html
<!-- Primary (submit) -->
<button type="submit" class="govuk-button" data-module="govuk-button">Save and continue</button>

<!-- Secondary -->
<button type="button" class="govuk-button govuk-button--secondary" data-module="govuk-button">Save as draft</button>

<!-- Warning (destructive) -->
<button type="submit" class="govuk-button govuk-button--warning" data-module="govuk-button">Delete account</button>

<!-- Start button (with arrow) -->
<a href="/start" role="button" draggable="false" class="govuk-button govuk-button--start" data-module="govuk-button">
  Start now
  <svg class="govuk-button__start-icon" xmlns="http://www.w3.org/2000/svg" width="17.5" height="19" viewBox="0 0 33 40" aria-hidden="true" focusable="false">
    <path fill="currentColor" d="M0 0h13l20 20-20 20H0l20-20z"/>
  </svg>
</a>
```

---

## Error Handling

**Always show error summary at top of page, before the `<h1>`:**

```html
<div class="govuk-error-summary" data-module="govuk-error-summary">
  <div role="alert">
    <h2 class="govuk-error-summary__title">There is a problem</h2>
    <div class="govuk-error-summary__body">
      <ul class="govuk-list govuk-error-summary__list">
        <li><a href="#full-name">Enter your full name</a></li>
        <li><a href="#dob-day">Enter a date of birth</a></li>
      </ul>
    </div>
  </div>
</div>
```

Rules:
- The `href` in each error link must match the `id` of the erroring input
- Add `govuk-form-group--error` to the wrapping `govuk-form-group`
- Add `govuk-input--error` (or `govuk-radios--error` etc.) to the input/container
- Add the `govuk-error-message` paragraph immediately before the input
- The `<span class="govuk-visually-hidden">Error:</span>` prefix is mandatory for screen readers

---

## GDS Page Patterns

For full HTML and research-backed guidance, read the relevant file from `gds-docs/patterns/`. Summary:

### One Thing Per Page
Each question page asks exactly one thing. The question is the `<h1>`. Use `govuk-fieldset__heading` inside a `<legend>` when the question wraps a fieldset (radios, checkboxes, date).

### Start Page
- `<h1>` is the service name
- `govuk-button--start` link
- Eligibility info and what they'll need
- No form on this page

### Check Your Answers
- `govuk-summary-list` with Change links
- `<h1>` is "Check your answers"
- Submit button: "Confirm and send" or "Accept and send"

### Confirmation Page
- `govuk-panel govuk-panel--confirmation` with reference number
- What happens next section
- No back link on this page

### Task List
- `govuk-task-list` with status tags
- Sections group related tasks
- Tags: "Completed" (no colour), "In progress" (`govuk-tag--blue`), "Not yet started" (`govuk-tag--grey`), "Cannot start yet" (grey, no link)

---

## Navigation & Feedback Components

### Back link
```html
<a href="javascript:history.back()" class="govuk-back-link">Back</a>
```
Place inside `govuk-width-container`, before `govuk-main-wrapper`. Never show on confirmation pages.

### Notification banner
```html
<!-- Info (blue) -->
<div class="govuk-notification-banner" role="region"
     aria-labelledby="govuk-notification-banner-title" data-module="govuk-notification-banner">
  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title" id="govuk-notification-banner-title">Important</h2>
  </div>
  <div class="govuk-notification-banner__content">
    <p class="govuk-notification-banner__heading">Your details have been updated.</p>
  </div>
</div>

<!-- Success (green) â€” add role="alert" and type="success" -->
<div class="govuk-notification-banner govuk-notification-banner--success" role="alert"
     aria-labelledby="govuk-notification-banner-title" data-module="govuk-notification-banner">
  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title" id="govuk-notification-banner-title">Success</h2>
  </div>
  <div class="govuk-notification-banner__content">
    <h3 class="govuk-notification-banner__heading">Application submitted</h3>
  </div>
</div>
```

---

## Typography Classes

```
govuk-heading-xl    h1 equivalent â€” 48px bold
govuk-heading-l     h2 equivalent â€” 36px bold
govuk-heading-m     h3 equivalent â€” 24px bold
govuk-heading-s     h4 equivalent â€” 19px bold
govuk-body          Standard body text â€” 19px
govuk-body-l        Large body â€” 24px
govuk-body-s        Small body â€” 16px
govuk-caption-xl/l/m  Caption above heading (e.g. section name)
govuk-label         Form label
govuk-label--l/m/s  Label sizing
govuk-hint          Hint text â€” grey
govuk-link          Hyperlink style
govuk-link--no-visited-state  Link that doesn't change colour when visited
```

---

## Accessibility Rules (WCAG 2.1 AA)

1. Every `<input>`, `<textarea>`, `<select>` must have a `<label>` with a matching `for`/`id` pair â€” never use `placeholder` as a label substitute
2. Group related inputs (radios, checkboxes, date) in a `<fieldset>` with `<legend>`
3. All hint and error IDs must be in `aria-describedby` on the input
4. Error messages must include `<span class="govuk-visually-hidden">Error:</span>` prefix
5. Use `autocomplete` attributes on personal data fields
6. The skip link `<a href="#main-content">` must be the first focusable element
7. `<main id="main-content">` is required â€” the skip link target
8. Colour must never be the only means of conveying information
9. Focus styles must not be removed â€” never `outline: none` without a replacement
10. `aria-label` / `aria-describedby` on any icon-only buttons
11. Images must have descriptive `alt` text; decorative images use `alt=""`
12. Page `<title>` format: `[Page title] â€“ [Service name] â€“ GOV.UK`
13. On error pages: `<title>` must be prefixed with `Error: `

---

## Nunjucks Macros

When the user's project uses the **GOV.UK Prototype Kit**, **Express/Nunjucks**, or requests `.njk`
templates, use Nunjucks macros instead of plain HTML. Read the macro reference first:

```
~/.claude/skills/gds-website-builder/gds-docs/nunjucks-macros.md
```

It covers: Prototype Kit setup, Express/Node setup, the `govuk/template.njk` base template, import
paths for all 34 components, and full options tables for every major component.

**Key rule:** In the Prototype Kit, omit the `{% from â€¦ %}` import line â€” macros are auto-available.
In a custom Express app, add the import at the top of each template.

---

## GDS Docs â€” Authoritative Reference

All GDS documentation is collated from the live GOV.UK Design System website and stored in the `gds-docs/` folder alongside this skill. **When you need full HTML markup, Nunjucks macros, options, or guidance for any component or pattern, read the relevant file below.**

Base path: `~/.claude/skills/gds-website-builder/gds-docs/`
> **Windows:** `%USERPROFILE%\.claude\skills\gds-website-builder\gds-docs\`

### Components (34 files)
Read `components/<name>.md` for any component â€” full HTML examples, options table, accessibility notes:

| Component | File |
|-----------|------|
| Accordion | `components/accordion.md` |
| Back link | `components/back-link.md` |
| Breadcrumbs | `components/breadcrumbs.md` |
| Button | `components/button.md` |
| Character count | `components/character-count.md` |
| Checkboxes | `components/checkboxes.md` |
| Cookie banner | `components/cookie-banner.md` |
| Date input | `components/date-input.md` |
| Details | `components/details.md` |
| Error message | `components/error-message.md` |
| Error summary | `components/error-summary.md` |
| Exit this page | `components/exit-this-page.md` |
| Fieldset | `components/fieldset.md` |
| File upload | `components/file-upload.md` |
| Footer | `components/footer.md` |
| Header | `components/header.md` |
| Inset text | `components/inset-text.md` |
| Notification banner | `components/notification-banner.md` |
| Pagination | `components/pagination.md` |
| Panel | `components/panel.md` |
| Password input | `components/password-input.md` |
| Phase banner | `components/phase-banner.md` |
| Radios | `components/radios.md` |
| Select | `components/select.md` |
| Service navigation | `components/service-navigation.md` |
| Skip link | `components/skip-link.md` |
| Summary list | `components/summary-list.md` |
| Table | `components/table.md` |
| Tabs | `components/tabs.md` |
| Tag | `components/tag.md` |
| Task list | `components/task-list.md` |
| Text input | `components/text-input.md` |
| Textarea | `components/textarea.md` |
| Warning text | `components/warning-text.md` |

### Patterns (29 files)
Read `patterns/<name>.md` for guidance, research, and HTML examples:

`addresses`, `bank-details`, `check-a-service-is-suitable`, `check-answers`, `complete-multiple-tasks`, `confirm-a-phone-number`, `confirm-an-email-address`, `confirmation-pages`, `contact-a-department-or-service-team`, `cookies-page`, `create-a-username`, `create-accounts`, `dates`, `email-addresses`, `equality-information`, `exit-a-page-quickly`, `names`, `national-insurance-numbers`, `navigate-a-service`, `page-not-found-pages`, `passwords`, `payment-card-details`, `phone-numbers`, `problem-with-the-service-pages`, `question-pages`, `service-unavailable-pages`, `start-using-a-service`, `step-by-step-navigation`, `validation`

### Styles (13 files)
Read `styles/<name>.md` for layout, spacing, typography, colour, and images guidance:

`colour`, `font-override-classes`, `headings`, `images`, `layout`, `links`, `lists`, `page-template`, `paragraphs`, `section-break`, `spacing`, `type-scale`, `typeface`

### Get Started (6 files)
Read `get-started/<name>.md`:

`extending-and-modifying-components`, `focus-states`, `labels-legends-headings`, `new-type-scale`, `production`, `prototyping`

### Accessibility
Read `accessibility/accessibility-strategy.md` for the GOV.UK accessibility strategy.

### Department-specific guidance
When the user explicitly names a UK government department (MoJ, DfT, MoD, FCDO, HO, HMRC, DWP, HMPPS, etc.), read `departments.md`. It covers:
- The correct footer `meta` text-link pattern for departmental attribution (no logos â€” the header never changes)
- Department reference table (gov.uk URLs, frontend library)
- MoJ Frontend extension setup for MoJ/HMPPS/HMCTS services
- What not to do (no departmental logos, no replacing Crown copyright)

---

**Usage:** When a user asks about a specific component, pattern, or style â€” read the relevant file from the base path above before generating HTML. The collated docs contain the canonical HTML, all variant examples, and up-to-date guidance from the live design system.

