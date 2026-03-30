#  Details 
Make a page easier to scan by letting users reveal more detailed information only if they need it.
[ Open this example in a new tab: details ](./components/details/default.md)
  * [HTML](./components/details/#details-example-html.md)
  * [Nunjucks](./components/details/#details-example-nunjucks.md)

HTML
Copy code
```
<details class="govuk-details">
  <summary class="govuk-details__summary">
    <span class="govuk-details__summary-text">
      Help with nationality
    </span>
  </summary>
  <div class="govuk-details__text">
    We need to know your nationality so we can work out which elections you’re entitled to vote in. If you cannot provide your nationality, you’ll have to send copies of identity documents through the post.
  </div>
</details>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| summaryText  | string  |  **Required.** If `summmaryHtml` is set, this is not required. Text to use within the summary element (the visible part of the details element). If `summaryHtml` is provided, the `summaryText` option will be ignored.   |  
| summaryHtml  | string  |  **Required.** If `summmaryText` is set, this is not required. HTML to use within the summary element (the visible part of the details element). If `summaryHtml` is provided, the `summaryText` option will be ignored.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the disclosed part of the details element. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the disclosed part of the details element. If `html` is provided, the `text` option will be ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire details component in a `call` block.   |  
| id  | string  |  ID to add to the details element.   |  
| open  | boolean  |  If `true`, details element will be expanded.   |  
| classes  | string  |  Classes to add to the `<details>` element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the `<details>` element.   |  
Copy code
```
{% from "govuk/components/details/macro.njk" import govukDetails %}

{{ govukDetails({
  summaryText: "Help with nationality",
  text: "We need to know your nationality so we can work out which elections you’re entitled to vote in. If you cannot provide your nationality, you’ll have to send copies of identity documents through the post."
}) }}
```

## When to use this component
Use the details component to make a page easier to scan when it contains information that only some users will need.
## When not to use this component
Do not use the details component to hide information that the majority of your users will need.
## Decide between using details, accordions and tabs
The Details component, [Accordion component](./components/accordion.md), and [Tabs component](./components/tabs.md) all hide sections of content which a user can choose to reveal.
Use the details component instead of tabs or an accordion if you only have 1 section of content.
The details component is less visually prominent than tabs and accordions, so tends to work better for content which is not as important to users.
## How it works
The details component is a short link that shows more detailed help text when a user clicks on it.
There are 2 ways to use the details component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: details second ](./components/details/default.md)
  * [HTML](./components/details/#details-second-example-html.md)
  * [Nunjucks](./components/details/#details-second-example-nunjucks.md)

HTML
Copy code
```
<details class="govuk-details">
  <summary class="govuk-details__summary">
    <span class="govuk-details__summary-text">
      Help with nationality
    </span>
  </summary>
  <div class="govuk-details__text">
    We need to know your nationality so we can work out which elections you’re entitled to vote in. If you cannot provide your nationality, you’ll have to send copies of identity documents through the post.
  </div>
</details>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| summaryText  | string  |  **Required.** If `summmaryHtml` is set, this is not required. Text to use within the summary element (the visible part of the details element). If `summaryHtml` is provided, the `summaryText` option will be ignored.   |  
| summaryHtml  | string  |  **Required.** If `summmaryText` is set, this is not required. HTML to use within the summary element (the visible part of the details element). If `summaryHtml` is provided, the `summaryText` option will be ignored.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the disclosed part of the details element. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the disclosed part of the details element. If `html` is provided, the `text` option will be ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire details component in a `call` block.   |  
| id  | string  |  ID to add to the details element.   |  
| open  | boolean  |  If `true`, details element will be expanded.   |  
| classes  | string  |  Classes to add to the `<details>` element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the `<details>` element.   |  
Copy code
```
{% from "govuk/components/details/macro.njk" import govukDetails %}

{{ govukDetails({
  summaryText: "Help with nationality",
  text: "We need to know your nationality so we can work out which elections you’re entitled to vote in. If you cannot provide your nationality, you’ll have to send copies of identity documents through the post."
}) }}
```

### Write clear link text
Make the link text short and descriptive so users can quickly work out if they need to click on it.
## Research on this component
There is [evidence that some users avoid clicking the link to show more details](https://github.com/alphagov/govuk-design-system-backlog/issues/44#issuecomment-629122091), as they think it will take them away from the page.
There are [concerns that some users of voice assist software will not be able to interact with the component](https://github.com/alphagov/govuk-design-system-backlog/issues/44#issuecomment-628082040). Some software might require the user to specifically refer to the link to show more details as a button in order to interact with it.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Details’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/44) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/details/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/details/#top.md)
