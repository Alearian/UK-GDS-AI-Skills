#  Breadcrumbs 
The breadcrumbs component helps users to understand where they are within a website’s structure and move between levels.
[ Open this example in a new tab: breadcrumbs ](./components/breadcrumbs/default.md)
  * [HTML](./components/breadcrumbs/#breadcrumbs-example-html.md)
  * [Nunjucks](./components/breadcrumbs/#breadcrumbs-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-breadcrumbs" aria-label="Breadcrumb">
  <ol class="govuk-breadcrumbs__list">
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Home</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Passports, travel and living abroad</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Travel abroad</a>
    </li>
  </ol>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items within breadcrumbs. [ See macro options for items](./components/breadcrumbs/#options-breadcrumbs-example--items.md).   |  
| classes  | string  |  Classes to add to the breadcrumbs container.   |  
| collapseOnMobile  | boolean  |  When true, the breadcrumbs will collapse to the first and last item only on tablet breakpoint and below.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the breadcrumbs container.   |  
| labelText  | string  |  Plain text label identifying the landmark to screen readers. Defaults to “Breadcrumb”.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  Link for the breadcrumbs item. If not specified, breadcrumbs item is a normal list item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the individual crumb.   |  
Copy code
```
{% from "govuk/components/breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  items: [
    {
      text: "Home",
      href: "#"
    },
    {
      text: "Passports, travel and living abroad",
      href: "#"
    },
    {
      text: "Travel abroad",
      href: "#"
    }
  ]
}) }}
```

## When to use this component
Use the breadcrumbs component when you need to help users understand and move between the multiple levels of a website.
## When not to use this component
Do not use the breadcrumbs component on websites with a flat structure, or to show progress through a linear journey or transaction.
If you’re using other navigational elements on the page, such as a sidebar, consider whether your users need the additional support of breadcrumbs.
## How it works
Always place breadcrumbs at the top of a page, before the `<main>` element. Placing them here means that the ‘Skip to main content’ link allows the user to skip all navigation links, including breadcrumbs.
The breadcrumbs should start with your ‘home’ page and end with the parent section of the current page.
There are 2 ways to use the breadcrumbs component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: breadcrumbs second ](./components/breadcrumbs/default.md)
  * [HTML](./components/breadcrumbs/#breadcrumbs-second-example-html.md)
  * [Nunjucks](./components/breadcrumbs/#breadcrumbs-second-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-breadcrumbs" aria-label="Breadcrumb">
  <ol class="govuk-breadcrumbs__list">
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Home</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Passports, travel and living abroad</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Travel abroad</a>
    </li>
  </ol>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items within breadcrumbs. [ See macro options for items](./components/breadcrumbs/#options-breadcrumbs-second-example--items.md).   |  
| classes  | string  |  Classes to add to the breadcrumbs container.   |  
| collapseOnMobile  | boolean  |  When true, the breadcrumbs will collapse to the first and last item only on tablet breakpoint and below.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the breadcrumbs container.   |  
| labelText  | string  |  Plain text label identifying the landmark to screen readers. Defaults to “Breadcrumb”.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  Link for the breadcrumbs item. If not specified, breadcrumbs item is a normal list item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the individual crumb.   |  
Copy code
```
{% from "govuk/components/breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  items: [
    {
      text: "Home",
      href: "#"
    },
    {
      text: "Passports, travel and living abroad",
      href: "#"
    },
    {
      text: "Travel abroad",
      href: "#"
    }
  ]
}) }}
```

### Collapsing breadcrumbs on mobile devices
If you have long breadcrumbs you can configure the component to only show the first and last items on mobile devices.
To do this, add a `govuk-breadcrumbs--collapse-on-mobile` class to the outer `<div>` element of the component HTML. Or if you’re using Nunjucks, add `collapseOnMobile: true` to the Nunjucks macro as shown in this example.
[ Open this example in a new tab: breadcrumbs that collapse on mobile – breadcrumbs ](./components/breadcrumbs/collapse-mobile.md)
  * [HTML](./components/breadcrumbs/#breadcrumbs-that-collapse-on-mobile-breadcrumbs-example-html.md)
  * [Nunjucks](./components/breadcrumbs/#breadcrumbs-that-collapse-on-mobile-breadcrumbs-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-breadcrumbs govuk-breadcrumbs--collapse-on-mobile" aria-label="Breadcrumb">
  <ol class="govuk-breadcrumbs__list">
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Home</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Environment</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Rural and countryside</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Rural development and land management</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Economic growth in rural areas</a>
    </li>
  </ol>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items within breadcrumbs. [ See macro options for items](./components/breadcrumbs/#options-breadcrumbs-that-collapse-on-mobile-breadcrumbs-example--items.md).   |  
| classes  | string  |  Classes to add to the breadcrumbs container.   |  
| collapseOnMobile  | boolean  |  When true, the breadcrumbs will collapse to the first and last item only on tablet breakpoint and below.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the breadcrumbs container.   |  
| labelText  | string  |  Plain text label identifying the landmark to screen readers. Defaults to “Breadcrumb”.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  Link for the breadcrumbs item. If not specified, breadcrumbs item is a normal list item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the individual crumb.   |  
Copy code
```
{% from "govuk/components/breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  collapseOnMobile: true,
  items: [
    {
      text: "Home",
      href: "#"
    },
    {
      text: "Environment",
      href: "#"
    },
    {
      text: "Rural and countryside",
      href: "#"
    },
    {
      text: "Rural development and land management",
      href: "#"
    },
    {
      text: "Economic growth in rural areas",
      href: "#"
    }
  ]
}) }}
```

### Breadcrumbs on dark backgrounds
Use the `govuk-breadcrumbs--inverse` modifier class to show white links and arrows on dark backgrounds – for example, in headers, custom components, and patterns with darker backgrounds.
Make sure all users can see the breadcrumbs – the background colour must have a contrast ratio of at least 4.5:1 with white to [meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
[ Open this example in a new tab: inverse breadcrumbs – breadcrumbs ](./components/breadcrumbs/inverse.md)
  * [HTML](./components/breadcrumbs/#inverse-breadcrumbs-breadcrumbs-example-html.md)
  * [Nunjucks](./components/breadcrumbs/#inverse-breadcrumbs-breadcrumbs-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-breadcrumbs govuk-breadcrumbs--inverse" aria-label="Breadcrumb">
  <ol class="govuk-breadcrumbs__list">
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Home</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Passports, travel and living abroad</a>
    </li>
    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="#">Travel abroad</a>
    </li>
  </ol>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items within breadcrumbs. [ See macro options for items](./components/breadcrumbs/#options-inverse-breadcrumbs-breadcrumbs-example--items.md).   |  
| classes  | string  |  Classes to add to the breadcrumbs container.   |  
| collapseOnMobile  | boolean  |  When true, the breadcrumbs will collapse to the first and last item only on tablet breakpoint and below.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the breadcrumbs container.   |  
| labelText  | string  |  Plain text label identifying the landmark to screen readers. Defaults to “Breadcrumb”.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the breadcrumbs item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  Link for the breadcrumbs item. If not specified, breadcrumbs item is a normal list item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the individual crumb.   |  
Copy code
```
{% from "govuk/components/breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  classes: "govuk-breadcrumbs--inverse",
  items: [
    {
      text: "Home",
      href: "#"
    },
    {
      text: "Passports, travel and living abroad",
      href: "#"
    },
    {
      text: "Travel abroad",
      href: "#"
    }
  ]
}) }}
```

## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Breadcrumbs’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/33) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/breadcrumbs/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/breadcrumbs/#top.md)
