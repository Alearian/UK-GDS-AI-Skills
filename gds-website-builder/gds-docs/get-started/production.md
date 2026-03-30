#  Production 
This guide explains how to set up your project so you can start using the styles and coded examples in the GOV.UK Design System in production.
! ** Warning If your service still uses GOV.UK Template, GOV.UK Frontend Toolkit or GOV.UK Elements, you should [install the latest v4 release of GOV.UK Frontend](https://frontend.design-system.service.gov.uk/v4/installing-with-npm/) and follow the guidance on [migrating from our old frameworks](https://frontend.design-system.service.gov.uk/v4/migrating-from-legacy-products/). **
## Include GOV.UK Frontend in your project
To start using GOV.UK styles, components and patterns contained here, you’ll need to include GOV.UK Frontend in your project.
There are 2 ways to include GOV.UK Frontend in your project. You can either install it using node package manager (npm) or include the compiled files in your application.
### Option 1: install using npm
We recommend [installing GOV.UK Frontend using npm](https://frontend.design-system.service.gov.uk/installing-with-npm/).
Using this option, you will be able to:
  * [selectively include the CSS for individual components](https://frontend.design-system.service.gov.uk/import-css/)
  * [selectively include the JavaScript for individual components](https://frontend.design-system.service.gov.uk/import-javascript/)
  * build your own styles or components based on the palette or typography and spacing mixins
  * customise the build (for example, overriding colours or enabling global styles)
  * use [our Nunjucks template and macros](https://frontend.design-system.service.gov.uk/use-nunjucks/) if your environment supports them

### Option 2: include compiled files
If your project does not use npm, or if you want to try out GOV.UK Frontend in your project without installing it through npm, you can [download and include compiled stylesheets, JavaScript and the asset files](https://frontend.design-system.service.gov.uk/install-using-precompiled-files/).
Using this option, you will be able to include all the CSS and JavaScript of GOV.UK Frontend in your project.
You will not be able to:
  * [selectively include the CSS for individual components](https://frontend.design-system.service.gov.uk/import-css/)
  * [selectively include the JavaScript for individual components](https://frontend.design-system.service.gov.uk/import-javascript/)
  * build your own styles or components based on the palette or typography and spacing mixins
  * customise the build, for example, overriding colours or enabling global styles
  * use the component Nunjucks templates

## Start using the GOV.UK page template
You can set up a basic page that is consistent with GOV.UK branding by [using the GOV.UK page template](./styles/page-template.md).
## Styling page elements
The Design System provides CSS classes for styling content, instead of global styles.
The class names follow the Block Element Modifier (BEM) naming convention. This can look a bit daunting at first, but it makes robust code that’s easy to maintain.
Explore the [Styles section](./styles.md) of the Design System to see what classes are available.
## Using components
The components in the Design System are designed to be accessible and responsive.
You can use them in your live application as either:
  * HTML
  * [our Nunjucks macros](https://frontend.design-system.service.gov.uk/use-nunjucks/), if you’ve installed GOV.UK Frontend using npm and your application uses Node.js

You can get the code from the HTML or Nunjucks tabs below any examples:
[ Open this example in a new tab: button ](./components/button/default.md)
  * [HTML](./get-started/production/#button-example-html.md)
  * [Nunjucks](./get-started/production/#button-example-nunjucks.md)

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

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./get-started/production/#top.md)
