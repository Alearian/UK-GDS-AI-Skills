#  Skip link 
Use the skip link component to help keyboard-only users skip to the main content on a page.
[ Open this example in a new tab: skip link ](./components/skip-link/default.md)
  * [HTML](./components/skip-link/#skip-link-example-html.md)
  * [Nunjucks](./components/skip-link/#skip-link-example-nunjucks.md)

HTML
Copy code
```
<p class="govuk-body">To view the skip link component tab to this example, or click inside this example and press tab.</p>
<a href="#" class="govuk-skip-link" data-module="govuk-skip-link">Skip to main content</a>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the skip link component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the skip link component. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  The value of the skip link’s `href` attribute. Defaults to `"#content"` if you do not provide a value.   |  
| classes  | string  |  Classes to add to the skip link.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the skip link.   |  
Copy code
```
<p class="govuk-body">To view the skip link component tab to this example, or click inside this example and press tab.</p>

{% from "govuk/components/skip-link/macro.njk" import govukSkipLink %}

{{ govukSkipLink({
  text: "Skip to main content",
  href: "#"
}) }}
```

If you use the page template, you’ll also get the skip link without having to add it, as it’s included by default. However, if you want to customise the default skip link, read the [page template guidance about customising components](./styles/page-template/#changing-template-content.md).
## When to use this component
All GOV.UK pages must include a skip link. Usually, you should place the skip link immediately after the opening `<body>` tag. However, if you’re using a [Cookie banner component](./components/cookie-banner.md), place the skip link immediately after the cookie banner.
Some automated accessibility testing tools may warn that the skip link element is not inside a landmark. This warning does not apply to skip links, so you can ignore it. Do not wrap the skip link in a `<nav>` region, or move it inside the header.
## How it works
Some people use the tab key on their keyboard to navigate through the links and form elements on a web page.
Including the skip link component gives users the option to bypass the top-level navigation links and jump to the main content on a page.
The skip link component is visually hidden until a keyboard press activates it.
There are 2 ways to use the skip link component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: skip link second ](./components/skip-link/default.md)
  * [HTML](./components/skip-link/#skip-link-second-example-html.md)
  * [Nunjucks](./components/skip-link/#skip-link-second-example-nunjucks.md)

HTML
Copy code
```
<p class="govuk-body">To view the skip link component tab to this example, or click inside this example and press tab.</p>
<a href="#" class="govuk-skip-link" data-module="govuk-skip-link">Skip to main content</a>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the skip link component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the skip link component. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  The value of the skip link’s `href` attribute. Defaults to `"#content"` if you do not provide a value.   |  
| classes  | string  |  Classes to add to the skip link.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the skip link.   |  
Copy code
```
<p class="govuk-body">To view the skip link component tab to this example, or click inside this example and press tab.</p>

{% from "govuk/components/skip-link/macro.njk" import govukSkipLink %}

{{ govukSkipLink({
  text: "Skip to main content",
  href: "#"
}) }}
```

## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Skip link’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/66) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/skip-link/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/skip-link/#top.md)
