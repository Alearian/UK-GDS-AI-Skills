# GOV.UK Design System â€” Nunjucks Macro Reference

GOV.UK Frontend v6.3.0 ships Nunjucks macros for every component. Use these when building with
the GOV.UK Prototype Kit, Express/Nunjucks apps, or any server-side Node project where `.njk`
templates are rendered server-side.

> **Production XSS warning:** If you pass `html` (or any option ending in `html`) into a macro in
> production, you **must sanitise** the value first to prevent cross-site scripting attacks.

---

## Setup

### GOV.UK Prototype Kit (recommended for prototyping)

Install **v7 or later** of the Prototype Kit â€” it includes govuk-frontend and configures Nunjucks
automatically. Do **not** add the `{% from â€¦ %}` import line; the Kit resolves macros globally.

```bash
npx govuk-prototype-kit create my-prototype
```

### Express / custom Node app

```bash
npm install govuk-frontend@6.3.0 nunjucks
```

Configure Nunjucks to resolve macros from the package:

```js
const nunjucks = require('nunjucks')
const path = require('path')

nunjucks.configure([
  path.join(__dirname, 'views'),
  path.join(__dirname, 'node_modules/govuk-frontend/dist')
], { autoescape: true, express: app })
```

In every template that uses a macro, add the import at the top:

```nunjucks
{% from "govuk/components/button/macro.njk" import govukButton %}
```

---

## Page Template (govukPageLayout)

The `govuk/template.njk` base template provides the full GOV.UK page shell. Extend it and fill
the named blocks:

```nunjucks
{% extends "govuk/template.njk" %}

{% set pageTitle = "My page â€“ My Service â€“ GOV.UK" %}

{% block head %}
  <link rel="stylesheet" href="/assets/govuk-frontend.min.css">
{% endblock %}

{% block header %}
  {% from "govuk/components/header/macro.njk" import govukHeader %}
  {{ govukHeader({ homepageUrl: "https://www.gov.uk/" }) }}
{% endblock %}

{% block content %}
  <h1 class="govuk-heading-l">Hello</h1>
{% endblock %}

{% block bodyEnd %}
  <script type="module">
    import { initAll } from '/assets/govuk-frontend.min.js'
    initAll()
  </script>
{% endblock %}
```

### Template variables

| Variable | Description |
|---|---|
| `pageTitle` | `<title>` text. Prefix with `Error: ` on error pages. |
| `htmlLang` | Language for `<html lang="">` (default `en`) |
| `htmlClasses` | Extra classes on `<html>` |
| `bodyClasses` | Extra classes on `<body>` |
| `bodyAttributes` | Object of extra attributes on `<body>` |
| `assetPath` | Override default asset path |
| `themeColor` | Browser theme colour meta tag |
| `containerClasses` | Classes for the width container |
| `mainClasses` | Classes for `<main>` |
| `mainLang` | Language for `<main>` content |

### Template blocks

| Block | Purpose |
|---|---|
| `head` | Additional `<head>` content (CSS, meta tags) |
| `bodyStart` | Content immediately after `<body>` |
| `header` | Override the entire header |
| `govukServiceNavigation` | Insert service navigation below header |
| `containerStart` | Before `<main>` inside the width container |
| `content` | **Your page content** goes here |
| `containerEnd` | After `</main>` |
| `footer` | Override the entire footer |
| `bodyEnd` | Before `</body>` (JS scripts) |

---

## Import path convention

All macros live at:
```
govuk/components/<component-name>/macro.njk
```

The Nunjucks function name is always `govuk` + PascalCase component name:

| Component | Import | Function |
|---|---|---|
| Button | `govuk/components/button/macro.njk` | `govukButton` |
| Text input | `govuk/components/input/macro.njk` | `govukInput` |
| Radios | `govuk/components/radios/macro.njk` | `govukRadios` |
| Checkboxes | `govuk/components/checkboxes/macro.njk` | `govukCheckboxes` |
| Textarea | `govuk/components/textarea/macro.njk` | `govukTextarea` |
| Select | `govuk/components/select/macro.njk` | `govukSelect` |
| Date input | `govuk/components/date-input/macro.njk` | `govukDateInput` |
| Error summary | `govuk/components/error-summary/macro.njk` | `govukErrorSummary` |
| Summary list | `govuk/components/summary-list/macro.njk` | `govukSummaryList` |
| Task list | `govuk/components/task-list/macro.njk` | `govukTaskList` |
| Header | `govuk/components/header/macro.njk` | `govukHeader` |
| Footer | `govuk/components/footer/macro.njk` | `govukFooter` |
| Phase banner | `govuk/components/phase-banner/macro.njk` | `govukPhaseBanner` |
| Back link | `govuk/components/back-link/macro.njk` | `govukBackLink` |
| Breadcrumbs | `govuk/components/breadcrumbs/macro.njk` | `govukBreadcrumbs` |
| Notification banner | `govuk/components/notification-banner/macro.njk` | `govukNotificationBanner` |
| Pagination | `govuk/components/pagination/macro.njk` | `govukPagination` |
| Panel | `govuk/components/panel/macro.njk` | `govukPanel` |
| Tag | `govuk/components/tag/macro.njk` | `govukTag` |
| Tabs | `govuk/components/tabs/macro.njk` | `govukTabs` |
| Accordion | `govuk/components/accordion/macro.njk` | `govukAccordion` |
| Character count | `govuk/components/character-count/macro.njk` | `govukCharacterCount` |
| Cookie banner | `govuk/components/cookie-banner/macro.njk` | `govukCookieBanner` |
| Details | `govuk/components/details/macro.njk` | `govukDetails` |
| Exit this page | `govuk/components/exit-this-page/macro.njk` | `govukExitThisPage` |
| Fieldset | `govuk/components/fieldset/macro.njk` | `govukFieldset` |
| File upload | `govuk/components/file-upload/macro.njk` | `govukFileUpload` |
| Inset text | `govuk/components/inset-text/macro.njk` | `govukInsetText` |
| Password input | `govuk/components/password-input/macro.njk` | `govukPasswordInput` |
| Service navigation | `govuk/components/service-navigation/macro.njk` | `govukServiceNavigation` |
| Skip link | `govuk/components/skip-link/macro.njk` | `govukSkipLink` |
| Table | `govuk/components/table/macro.njk` | `govukTable` |
| Warning text | `govuk/components/warning-text/macro.njk` | `govukWarningText` |

---

## Component macros â€” complete reference

### govukHeader

```nunjucks
{% from "govuk/components/header/macro.njk" import govukHeader %}

{{ govukHeader({
  homepageUrl: "https://www.gov.uk/"
}) }}
```

| Option | Type | Description |
|---|---|---|
| `homepageUrl` | string | URL for the GOV.UK logo link (default: `https://www.gov.uk/`) |
| `productName` | string | Product name displayed after "GOV.UK" |
| `containerClasses` | string | Classes for the inner container |
| `classes` | string | Classes on the header element |
| `attributes` | object | HTML attributes on the header element |

---

### govukButton

```nunjucks
{% from "govuk/components/button/macro.njk" import govukButton %}

{{ govukButton({ text: "Save and continue" }) }}

{{ govukButton({ text: "Save as draft", classes: "govuk-button--secondary" }) }}

{{ govukButton({ text: "Delete account", classes: "govuk-button--warning" }) }}

{{ govukButton({ text: "Start now", href: "/start", isStartButton: true }) }}
```

| Option | Type | Description |
|---|---|---|
| `text` | string | Button label (required unless `html` set) |
| `html` | string | HTML label (overrides `text`) |
| `type` | string | `submit` (default), `button`, or `reset` |
| `name` | string | Form submission name |
| `value` | string | Form submission value |
| `href` | string | Renders as `<a>` link instead of `<button>` |
| `isStartButton` | boolean | Adds the start-page arrow icon |
| `preventDoubleClick` | boolean | Blocks double-submission |
| `disabled` | boolean | Adds `disabled` + `aria-disabled` |
| `id` | string | ID attribute |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

---

### govukInput (text input)

```nunjucks
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  id: "full-name",
  name: "fullName",
  label: {
    text: "Full name",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: { text: "As it appears on your passport" },
  autocomplete: "name"
}) }}
```

With error:

```nunjucks
{{ govukInput({
  id: "ni-number",
  name: "niNumber",
  label: { text: "National Insurance number" },
  hint: { text: "It's on your P60, for example QQ 12 34 56 C" },
  errorMessage: { text: "Enter a National Insurance number in the correct format" },
  classes: "govuk-input--width-10"
}) }}
```

| Option | Type | Description |
|---|---|---|
| `id` | string | Input ID (defaults to `name`) |
| `name` | string | **Required.** Form field name |
| `type` | string | Input type (default `text`) |
| `value` | string | Pre-filled value |
| `label` | object | **Required.** Label config |
| `hint` | object | Hint config |
| `errorMessage` | object | Error message config |
| `classes` | string | Width/extra classes e.g. `govuk-input--width-10` |
| `autocomplete` | string | Autocomplete attribute (WCAG 1.3.5) |
| `prefix` | object | Prefix text/html (e.g. `Â£`) |
| `suffix` | object | Suffix text/html (e.g. `kg`) |
| `spellcheck` | boolean | Enable/disable spellcheck |
| `disabled` | boolean | Disable the input |
| `formGroup` | object | Form group options |
| `attributes` | object | HTML attributes |

**Width classes:** `govuk-input--width-30`, `govuk-input--width-20`, `govuk-input--width-10`,
`govuk-input--width-5`, `govuk-input--width-4`, `govuk-input--width-3`, `govuk-input--width-2`

---

### govukTextarea

```nunjucks
{% from "govuk/components/textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  id: "more-detail",
  name: "moreDetail",
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: { text: "Do not include personal or financial information." },
  rows: "5"
}) }}
```

| Option | Type | Description |
|---|---|---|
| `id` | string | Textarea ID |
| `name` | string | **Required.** Form field name |
| `label` | object | **Required.** Label config |
| `hint` | object | Hint config |
| `errorMessage` | object | Error message config |
| `rows` | string | Number of visible rows (default `5`) |
| `value` | string | Pre-filled content |
| `spellcheck` | boolean | Enable/disable spellcheck |
| `disabled` | boolean | Disable the textarea |
| `autocomplete` | string | Autocomplete attribute |
| `formGroup` | object | Form group options |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

---

### govukSelect

```nunjucks
{% from "govuk/components/select/macro.njk" import govukSelect %}

{{ govukSelect({
  id: "sort",
  name: "sort",
  label: { text: "Sort by" },
  items: [
    { value: "published", text: "Recently published" },
    { value: "updated", text: "Recently updated", selected: true },
    { value: "views", text: "Most views" }
  ]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `id` | string | Select ID (defaults to `name`) |
| `name` | string | **Required.** Form field name |
| `label` | object | **Required.** Label config |
| `items` | array | **Required.** Option items |
| `value` | string | Pre-selected value |
| `hint` | object | Hint config |
| `errorMessage` | object | Error message config |
| `disabled` | boolean | Disable the select |
| `formGroup` | object | Form group options |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

**Item options:** `value`, `text`, `html`, `selected` (boolean), `disabled` (boolean), `attributes`

---

### govukRadios

```nunjucks
{% from "govuk/components/radios/macro.njk" import govukRadios %}

{{ govukRadios({
  name: "whereDoYouLive",
  fieldset: {
    legend: {
      text: "Where do you live?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: { text: "Select one option." },
  items: [
    { value: "england", text: "England" },
    { value: "scotland", text: "Scotland" },
    { value: "wales", text: "Wales" },
    { divider: "or" },
    { value: "abroad", text: "I am a British citizen living abroad" }
  ]
}) }}
```

Conditional reveal:

```nunjucks
{{ govukRadios({
  name: "contact",
  fieldset: {
    legend: { text: "How would you like to be contacted?", isPageHeading: true, classes: "govuk-fieldset__legend--l" }
  },
  items: [
    {
      value: "email",
      text: "Email",
      conditional: { html: emailInputHtml }
    },
    { value: "phone", text: "Phone" }
  ]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `name` | string | **Required.** Input name |
| `items` | array | **Required.** Radio items |
| `fieldset` | object | Fieldset/legend wrapper |
| `hint` | object | Hint config |
| `errorMessage` | object | Error message config |
| `idPrefix` | string | Prefix for IDs (defaults to `name`) |
| `value` | string | Pre-checked value |
| `classes` | string | e.g. `govuk-radios--inline`, `govuk-radios--small` |
| `formGroup` | object | Form group options |
| `attributes` | object | HTML attributes |

**Item options:** `value`*, `text`*, `html`, `id`, `checked`, `disabled`, `hint`, `label`,
`conditional` (object with `html`), `divider`, `attributes`

---

### govukCheckboxes

```nunjucks
{% from "govuk/components/checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  name: "waste",
  fieldset: {
    legend: {
      text: "Which types of waste do you transport?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: { text: "Select all that apply." },
  items: [
    { value: "carcasses", text: "Waste from animal carcasses" },
    { value: "mines", text: "Waste from mines or quarries" },
    {
      value: "none",
      text: "None of these",
      behaviour: "exclusive"
    }
  ]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `name` | string | **Required.** Shared input name |
| `items` | array | **Required.** Checkbox items |
| `fieldset` | object | Fieldset/legend wrapper |
| `hint` | object | Hint config |
| `errorMessage` | object | Error message config |
| `idPrefix` | string | Prefix for IDs |
| `values` | array | Pre-checked values |
| `classes` | string | e.g. `govuk-checkboxes--small` |
| `formGroup` | object | Form group options |
| `attributes` | object | HTML attributes |

**Item options:** `value`*, `text`*, `html`, `id`, `name`, `checked`, `disabled`, `hint`, `label`,
`conditional` (object with `html`), `behaviour` (`"exclusive"`), `divider`, `attributes`

---

### govukDateInput

```nunjucks
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "passport-issued",
  namePrefix: "passport-issued",
  fieldset: {
    legend: {
      text: "When was your passport issued?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: { text: "For example, 27 3 2007" }
}) }}
```

Date of birth (with autocomplete):

```nunjucks
{{ govukDateInput({
  id: "dob",
  namePrefix: "dob",
  fieldset: {
    legend: { text: "What is your date of birth?", isPageHeading: true, classes: "govuk-fieldset__legend--l" }
  },
  hint: { text: "For example, 31 3 1980" },
  items: [
    { name: "day",   classes: "govuk-input--width-2", autocomplete: "bday-day" },
    { name: "month", classes: "govuk-input--width-2", autocomplete: "bday-month" },
    { name: "year",  classes: "govuk-input--width-4", autocomplete: "bday-year" }
  ]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `id` | string | **Required.** Component ID; also prefixes each input |
| `namePrefix` | string | Prefix for item `name` attributes (e.g. `dob` â†’ `dob-day`) |
| `items` | array | Day/month/year input configs (auto-generated if omitted) |
| `fieldset` | object | Fieldset/legend wrapper |
| `hint` | object | Hint config |
| `errorMessage` | object | Error message config |
| `formGroup` | object | Form group options |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

**Item options:** `name`*, `id`, `value`, `label`, `autocomplete`, `pattern`, `classes`, `attributes`

---

### govukErrorSummary

Place at the top of the page, before the `<h1>`, whenever there are validation errors.

```nunjucks
{% from "govuk/components/error-summary/macro.njk" import govukErrorSummary %}

{{ govukErrorSummary({
  titleText: "There is a problem",
  errorList: [
    { text: "Enter your full name", href: "#full-name" },
    { text: "Enter a date of birth", href: "#dob-day" }
  ]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `titleText` | string | Heading text (required unless `titleHtml` set) |
| `titleHtml` | string | Heading HTML |
| `descriptionText` | string | Optional description text |
| `descriptionHtml` | string | Optional description HTML |
| `errorList` | array | Error link items |
| `disableAutoFocus` | boolean | Prevent focus moving to summary on load |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

**errorList item options:** `href`, `text`/`html`*, `attributes`

---

### govukSummaryList

```nunjucks
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  rows: [
    {
      key: { text: "Name" },
      value: { text: "Sarah Philips" },
      actions: {
        items: [
          { href: "/name", text: "Change", visuallyHiddenText: "name" }
        ]
      }
    },
    {
      key: { text: "Date of birth" },
      value: { text: "5 January 1978" },
      actions: {
        items: [
          { href: "/dob", text: "Change", visuallyHiddenText: "date of birth" }
        ]
      }
    }
  ]
}) }}
```

Wrapped in a summary card:

```nunjucks
{{ govukSummaryList({
  card: {
    title: { text: "Applicant 1" },
    actions: { items: [{ href: "/remove/1", text: "Remove applicant", visuallyHiddenText: "Applicant 1" }] }
  },
  rows: [...]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `rows` | array | **Required.** Row objects |
| `card` | object | Wraps list in a summary card |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

**Row options:** `key`* (object), `value`* (object), `actions` (object), `classes`

**Key/value options:** `text`/`html`*, `classes`

**Actions options:** `items` (array), `classes`

**Action item options:** `href`*, `text`/`html`*, `visuallyHiddenText`, `classes`, `attributes`

---

### govukTaskList

```nunjucks
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}

{{ govukTaskList({
  idPrefix: "company-details",
  items: [
    {
      title: { text: "Company details" },
      href: "/company-details",
      status: { text: "Completed" }
    },
    {
      title: { text: "Business address" },
      href: "/address",
      status: { tag: { text: "In progress", classes: "govuk-tag--blue" } }
    },
    {
      title: { text: "Contact details" },
      hint: { text: "Add a phone number and email address" },
      status: { tag: { text: "Not yet started", classes: "govuk-tag--grey" } }
    },
    {
      title: { text: "Business directors" },
      status: { text: "Cannot start yet", classes: "govuk-task-list__status--cannot-start-yet" }
    }
  ]
}) }}
```

| Option | Type | Description |
|---|---|---|
| `items` | array | **Required.** Task items |
| `idPrefix` | string | Prefix for IDs |
| `classes` | string | Extra classes on `<ul>` |
| `attributes` | object | HTML attributes |

**Item options:** `title`* (object), `href`, `status`* (object), `hint` (object), `classes`

**Status tag colours:** none = completed (teal), `govuk-tag--blue` = in progress,
`govuk-tag--grey` = not started / cannot start

---

### govukNotificationBanner

```nunjucks
{% from "govuk/components/notification-banner/macro.njk" import govukNotificationBanner %}

{# Info banner (using caller block) #}
{% call govukNotificationBanner() %}
  <p class="govuk-notification-banner__heading">
    You have 7 days left to send your application.
    <a class="govuk-notification-banner__link" href="#">View application</a>.
  </p>
{% endcall %}

{# Success banner #}
{% call govukNotificationBanner({ type: "success" }) %}
  <h3 class="govuk-notification-banner__heading">Application submitted</h3>
{% endcall %}
```

Or pass content directly:

```nunjucks
{{ govukNotificationBanner({
  text: "New email received.",
  titleText: "Important"
}) }}
```

| Option | Type | Description |
|---|---|---|
| `text` | string | Banner body text |
| `html` | string | Banner body HTML |
| `titleText` | string | Title (default: "Important" or "Success") |
| `titleHtml` | string | Title HTML |
| `titleHeadingLevel` | string | Heading level 1â€“6 (default `2`) |
| `type` | string | `"success"` for green success banner |
| `role` | string | ARIA role (default `region`; `alert` for success) |
| `disableAutoFocus` | boolean | Prevent auto-focus on load |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

---

### govukPhaseBanner

```nunjucks
{% from "govuk/components/phase-banner/macro.njk" import govukPhaseBanner %}

{{ govukPhaseBanner({
  tag: { text: "Alpha" },
  html: 'This is a new service. Help us improve it and <a class="govuk-link" href="/feedback">give your feedback by email</a>.'
}) }}
```

| Option | Type | Description |
|---|---|---|
| `tag` | object | Tag component config (use `text` for phase name) |
| `text` | string | Banner text |
| `html` | string | Banner HTML (allows links) |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

---

### govukBackLink

```nunjucks
{% from "govuk/components/back-link/macro.njk" import govukBackLink %}

{{ govukBackLink({ text: "Back", href: "javascript:history.back()" }) }}
```

| Option | Type | Description |
|---|---|---|
| `text` | string | Link text (default `"Back"`) |
| `html` | string | Link HTML |
| `href` | string | Link URL |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

---

### govukPanel (confirmation page)

```nunjucks
{% from "govuk/components/panel/macro.njk" import govukPanel %}

{{ govukPanel({
  titleText: "Application complete",
  html: "Your reference number<br><strong>HDJ2123F</strong>"
}) }}
```

| Option | Type | Description |
|---|---|---|
| `titleText` | string | Panel heading (required unless `titleHtml`) |
| `titleHtml` | string | Panel heading HTML |
| `text` | string | Panel body text |
| `html` | string | Panel body HTML |
| `headingLevel` | integer | Heading level 1â€“6 (default `1`) |
| `classes` | string | Extra classes |
| `attributes` | object | HTML attributes |

---

## Nunjucks tips

### Reuse macros in loops

```nunjucks
{% for item in items %}
  {{ govukSummaryList({ rows: item.rows }) }}
{% endfor %}
```

### Set variables for conditional HTML

```nunjucks
{% set emailInputHtml %}
  {{ govukInput({ id: "email", name: "email", label: { text: "Email address" } }) }}
{% endset %}

{{ govukRadios({
  name: "contact",
  items: [
    { value: "email", text: "Email", conditional: { html: emailInputHtml } }
  ]
}) }}
```

### Macro sensitivity

Macros raise unhelpful errors when required options are missing or types are wrong. Always preview
after changes. Common mistakes:
- Passing a string where an object is expected (`label: "Name"` â†’ should be `label: { text: "Name" }`)
- Missing `name` on inputs
- Using `title:` instead of `titleText:` on error summary

