#  Panel 
The panel component is a visible container used on confirmation or results pages to highlight important content.
[ Open this example in a new tab: panel ](./components/panel/default.md)
  * [HTML](./components/panel/#panel-example-html.md)
  * [Nunjucks](./components/panel/#panel-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-panel govuk-panel--confirmation">
  <h1 class="govuk-panel__title">
    Application complete
  </h1>
  <div class="govuk-panel__body">
    Your reference number<br><strong>HDJ2123F</strong>
  </div>
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
| titleText  | string  |  **Required.** If `titleHtml` is set, this is not required. Text to use within the panel. If `titleHtml` is provided, the `titleText` option will be ignored.   |  
| titleHtml  | string  |  **Required.** If `titleText` is set, this is not required. HTML to use within the panel. If `titleHtml` is provided, the `titleText` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `1`.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the panel content. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the panel content. If `html` is provided, the `text` option will be ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire panel component in a `call` block.   |  
| classes  | string  |  Classes to add to the panel container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the panel container.   |  
Copy code
```
{% from "govuk/components/panel/macro.njk" import govukPanel %}

{{ govukPanel({
  titleText: "Application complete",
  html: "Your reference number<br><strong>HDJ2123F</strong>"
}) }}
```

## When to use this component
Use the panel component to display important information when a transaction has been completed.
In most cases, the panel component is used on [Confirmation pages in your service](./patterns/confirmation-pages.md), to tell the user they have successfully completed the transaction.
## When not to use this component
Never use the panel component to highlight important information within body content.
## How it works
There are 2 ways to use the panel component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: panel second ](./components/panel/default.md)
  * [HTML](./components/panel/#panel-second-example-html.md)
  * [Nunjucks](./components/panel/#panel-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-panel govuk-panel--confirmation">
  <h1 class="govuk-panel__title">
    Application complete
  </h1>
  <div class="govuk-panel__body">
    Your reference number<br><strong>HDJ2123F</strong>
  </div>
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
| titleText  | string  |  **Required.** If `titleHtml` is set, this is not required. Text to use within the panel. If `titleHtml` is provided, the `titleText` option will be ignored.   |  
| titleHtml  | string  |  **Required.** If `titleText` is set, this is not required. HTML to use within the panel. If `titleHtml` is provided, the `titleText` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `1`.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the panel content. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the panel content. If `html` is provided, the `text` option will be ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire panel component in a `call` block.   |  
| classes  | string  |  Classes to add to the panel container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the panel container.   |  
Copy code
```
{% from "govuk/components/panel/macro.njk" import govukPanel %}

{{ govukPanel({
  titleText: "Application complete",
  html: "Your reference number<br><strong>HDJ2123F</strong>"
}) }}
```

### How to write panel text
Keep your panel text brief, as it’s only meant for a high-level explanation of what has happened. For example, ‘Application complete’.
Aim to use short words and phrases to make sure highlighted information is easy to read at different screen sizes. For example, shorter amounts of information is less likely to wrap around the panel, which can happen when using the zoom function on mobiles.
If you need to give detailed information, or more context, use the description text under the heading text.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Panel’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/55) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/panel/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/panel/#top.md)
