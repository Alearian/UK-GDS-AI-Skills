#  Warning text 
[ Open this example in a new tab: warning text ](./components/warning-text/default.md)
  * [HTML](./components/warning-text/#warning-text-example-html.md)
  * [Nunjucks](./components/warning-text/#warning-text-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-visually-hidden">Warning</span>
    You can be fined up to £5,000 if you do not register.
  </strong>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the warning text component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the warning text component. If `html` is provided, the `text` option will be ignored.   |  
| iconFallbackText  | string  |  The fallback text for the icon. Defaults to `"Warning"`.   |  
| classes  | string  |  Classes to add to the warning text.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the warning text.   |  
Copy code
```
{% from "govuk/components/warning-text/macro.njk" import govukWarningText %}

{{ govukWarningText({
  text: "You can be fined up to £5,000 if you do not register.",
  iconFallbackText: "Warning"
}) }}
```

## When to use this component
Use the warning text component when you need to warn users about something important, such as legal consequences of an action, or lack of action, that they might take.
## How it works
There are 2 ways to use the warning text component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: warning text second ](./components/warning-text/default.md)
  * [HTML](./components/warning-text/#warning-text-second-example-html.md)
  * [Nunjucks](./components/warning-text/#warning-text-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-visually-hidden">Warning</span>
    You can be fined up to £5,000 if you do not register.
  </strong>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the warning text component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the warning text component. If `html` is provided, the `text` option will be ignored.   |  
| iconFallbackText  | string  |  The fallback text for the icon. Defaults to `"Warning"`.   |  
| classes  | string  |  Classes to add to the warning text.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the warning text.   |  
Copy code
```
{% from "govuk/components/warning-text/macro.njk" import govukWarningText %}

{{ govukWarningText({
  text: "You can be fined up to £5,000 if you do not register.",
  iconFallbackText: "Warning"
}) }}
```

You might need to rewrite the hidden text (‘Warning’ in the example) to make it appropriate for your context.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Warning text’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/71) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/warning-text/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/warning-text/#top.md)
