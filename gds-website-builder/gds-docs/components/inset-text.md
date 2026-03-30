#  Inset text 
[ Open this example in a new tab: inset text ](./components/inset-text/default.md)
  * [HTML](./components/inset-text/#inset-text-example-html.md)
  * [Nunjucks](./components/inset-text/#inset-text-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-inset-text">
  It can take up to 8 weeks to register a lasting power of attorney if there are no mistakes in the application.
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the inset text component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the inset text component. If `html` is provided, the `text` option will be ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire inset text component in a `call` block.   |  
| id  | string  |  ID attribute to add to the inset text container.   |  
| classes  | string  |  Classes to add to the inset text container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the inset text container.   |  
Copy code
```
{% from "govuk/components/inset-text/macro.njk" import govukInsetText %}

{{ govukInsetText({
  text: "It can take up to 8 weeks to register a lasting power of attorney if there are no mistakes in the application."
}) }}
```

## When to use this component
Use the inset text component to differentiate a block of text from the content that surrounds it, for example:
  * quotes
  * examples
  * additional information about the page

## When not to use this component
Some users do not notice inset text if it’s used on complex pages or near to other visually prominent elements. For this reason, avoid using inset text as a way of highlighting very important information that users need to see.
If you need to draw attention to very important content, like legal information, use the [Warning text component](./components/warning-text.md) instead.
## How it works
Use inset text very sparingly - it’s less effective if it’s overused.
There are 2 ways to use the inset text component. You can use HTML or, if you’re using Nunjucks or the GOV.UK Prototype Kit, you can use the Nunjucks macro.
[ Open this example in a new tab: inset text second ](./components/inset-text/default.md)
  * [HTML](./components/inset-text/#inset-text-second-example-html.md)
  * [Nunjucks](./components/inset-text/#inset-text-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-inset-text">
  It can take up to 8 weeks to register a lasting power of attorney if there are no mistakes in the application.
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the inset text component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the inset text component. If `html` is provided, the `text` option will be ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire inset text component in a `call` block.   |  
| id  | string  |  ID attribute to add to the inset text container.   |  
| classes  | string  |  Classes to add to the inset text container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the inset text container.   |  
Copy code
```
{% from "govuk/components/inset-text/macro.njk" import govukInsetText %}

{{ govukInsetText({
  text: "It can take up to 8 weeks to register a lasting power of attorney if there are no mistakes in the application."
}) }}
```

## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Inset text’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/136) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/inset-text/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/inset-text/#top.md)
