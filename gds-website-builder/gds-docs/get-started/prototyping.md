#  Prototyping 
This guide explains how to create prototypes using the GOV.UK Design System and GOV.UK Prototype Kit.
## Before you start
To make prototypes you will need to install version 7 or later of the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk/docs/create-new-prototype) which has been built to work with the Design System.
Version 7 of the Prototype Kit works in the same way as previous versions except that it uses a new frontend framework called GOV.UK Frontend.
This means that any code that you copy across from old prototypes will not display correctly. Instead, you should use the code provided in the Design System.
## Styling page elements
The Design System provides lots of new CSS classes for styling page elements, so you should not need to write as much of your own Sass or CSS.
Explore the [Styles section](./styles.md) of the Design System to see what classes are available and how to apply them.
## Using components
Components are reusable parts of the user interface, like buttons, text inputs and checkboxes. The components in the Design System are designed to be accessible and responsive.
There are 2 ways to use components in the Design System. You can either use HTML or a Nunjucks macro.
You can copy the code from the HTML or Nunjucks tabs below any examples:
[ Open this example in a new tab: button ](./components/button/default.md)
  * [HTML](./get-started/prototyping/#button-example-html.md)
  * [Nunjucks](./get-started/prototyping/#button-example-nunjucks.md)

HTML
Copy code
```
<button type="submit" class="govuk-button" data-module="govuk-button">
  Save and continue
</button>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for the button. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for the button. If `html` is provided, the `text` option will be ignored.   |  
| type  | string  |  Type of the button, determining its behaviour in forms – `"button"`, `"submit"` or `"reset"`. Defaults to `"submit"`. This has no effect if `href` is set.   |  
| name  | string  |  Name of the button, sent when a form is submitted. This has no effect if `href` is set.   |  
| value  | string  |  Value of the button, sent when a form is submitted. This has no effect if `href` is set.   |  
| disabled  | boolean  |  Whether the button should be disabled. `disabled` and `aria-disabled` attributes will be set automatically. This has no effect if `href` is set.   |  
| href  | string  |  The URL that the button should link to.   |  
| classes  | string  |  Classes to add to the button.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the button.   |  
| preventDoubleClick  | boolean  |  Prevent accidental double clicks on submit buttons from submitting forms multiple times. This has no effect if `href` is set.   |  
| isStartButton  | boolean  |  Use for the main call to action on your service’s start page.   |  
| id  | string  |  The ID of the button.   |  
Copy code
```
{% from "govuk/components/button/macro.njk" import govukButton %}

{{ govukButton({
  text: "Save and continue"
}) }}
```

## Using Nunjucks macros
A Nunjucks macro is a simple template that generates more complex HTML. However, macros are more sensitive to mistakes than HTML, so it’s worth saving and previewing.
When using Nunjucks macros in the Prototype Kit leave out the first line that starts with `{% from ...`.
## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./get-started/prototyping/#top.md)
