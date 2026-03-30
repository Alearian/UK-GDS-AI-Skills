#  Fieldset 
Use the fieldset component to group related form inputs.
## When to use this component
Use the fieldset component when you need to show a relationship between multiple form inputs. For example, you may need to group a set of text inputs into a single fieldset when [asking for an address in your service](./patterns/addresses.md).
[ Open this example in a new tab: address group – fieldset ](./components/fieldset/address-group.md)
  * [HTML](./components/fieldset/#address-group-fieldset-example-html.md)
  * [Nunjucks](./components/fieldset/#address-group-fieldset-example-nunjucks.md)

HTML
Copy code
```
<fieldset class="govuk-fieldset">
  <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
    <h1 class="govuk-fieldset__heading">
      What is your address?
    </h1>
  </legend>
  <div class="govuk-form-group">
    <label class="govuk-label" for="address-line-1">
      Address line 1
    </label>
    <input class="govuk-input" id="address-line-1" name="addressLine1" type="text" autocomplete="address-line1">
  </div>
  <div class="govuk-form-group">
    <label class="govuk-label" for="address-line-2">
      Address line 2 (optional)
    </label>
    <input class="govuk-input" id="address-line-2" name="addressLine2" type="text" autocomplete="address-line2">
  </div>
  <div class="govuk-form-group">
    <label class="govuk-label" for="address-town">
      Town or city
    </label>
    <input class="govuk-input govuk-!-width-two-thirds" id="address-town" name="addressTown" type="text" autocomplete="address-level2">
  </div>
  <div class="govuk-form-group">
    <label class="govuk-label" for="address-postcode">
      Postcode
    </label>
    <input class="govuk-input govuk-input--width-10" id="address-postcode" name="addressPostcode" type="text" autocomplete="postal-code">
  </div>
</fieldset>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| legend  | object  |  The legend for the fieldset component. [ See macro options for legend](./components/fieldset/#options-address-group-fieldset-example--legend.md).   |  
| classes  | string  |  Classes to add to the fieldset container.   |  
| role  | string  |  Optional ARIA role attribute.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the fieldset container.   |  
| html  | string  |  HTML to use/render within the fieldset element.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire fieldset component in a `call` block.   |  
Options for `legend` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the legend. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the legend. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the legend.   |  
| isPageHeading  | boolean  |  Whether the legend also acts as the heading for the page.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}
{% from "govuk/components/fieldset/macro.njk" import govukFieldset %}

{% call govukFieldset({
  legend: {
    text: "What is your address?",
    classes: "govuk-fieldset__legend--l",
    isPageHeading: true
  }
}) %}

  {{ govukInput({
    label: {
      text: "Address line 1"
    },
    id: "address-line-1",
    name: "addressLine1",
    autocomplete: "address-line1"
  }) }}

  {{ govukInput({
    label: {
      text: "Address line 2 (optional)"
    },
    id: "address-line-2",
    name: "addressLine2",
    autocomplete: "address-line2"
  }) }}

  {{ govukInput({
    label: {
      text: "Town or city"
    },
    classes: "govuk-!-width-two-thirds",
    id: "address-town",
    name: "addressTown",
    autocomplete: "address-level2"
  }) }}

  {{ govukInput({
    label: {
      text: "Postcode"
    },
    classes: "govuk-input--width-10",
    id: "address-postcode",
    name: "addressPostcode",
    autocomplete: "postal-code"
  }) }}

{% endcall %}
```

If you’re using the examples or macros for a [Radios component](./components/radios.md), [Checkboxes component](./components/checkboxes.md) or [Date input component](./components/date-input.md), the fieldset will already be included.
## How it works
The first element inside a fieldset must be a `legend` which describes the group of inputs. This could be a question, such as ‘What is your current address?’ or a statement like ‘Personal details’.
If you’re asking just [one question per page in your service](./patterns/question-pages/#start-by-asking-one-question-per-page.md) as recommended, you can set the contents of the `<legend>` as the page heading, as shown in the example below. This is good practice as it means that users of screen readers will only hear the contents once.
Read more about [why and how to set legends as headings](./get-started/labels-legends-headings.md).
[ Open this example in a new tab: fieldset ](./components/fieldset/default.md)
  * [HTML](./components/fieldset/#fieldset-example-html.md)
  * [Nunjucks](./components/fieldset/#fieldset-example-nunjucks.md)

HTML
Copy code
```
<fieldset class="govuk-fieldset">
  <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
    <h1 class="govuk-fieldset__heading">
      Legend as page heading
    </h1>
  </legend>
</fieldset>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| legend  | object  |  The legend for the fieldset component. [ See macro options for legend](./components/fieldset/#options-fieldset-example--legend.md).   |  
| classes  | string  |  Classes to add to the fieldset container.   |  
| role  | string  |  Optional ARIA role attribute.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the fieldset container.   |  
| html  | string  |  HTML to use/render within the fieldset element.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire fieldset component in a `call` block.   |  
Options for `legend` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the legend. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the legend. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the legend.   |  
| isPageHeading  | boolean  |  Whether the legend also acts as the heading for the page.   |  
Copy code
```
{% from "govuk/components/fieldset/macro.njk" import govukFieldset %}

{{ govukFieldset({
  legend: {
    text: "Legend as page heading",
    classes: "govuk-fieldset__legend--l",
    isPageHeading: true
  }
}) }}
```

On [Question pages in your service](./patterns/question-pages.md) containing a group of inputs, including the question as the legend helps users of screen readers to understand that the inputs are all related to that question.
Include general help text in the legend if it would help the user fill in the form, and you [cannot write it as hint text](./components/text-input/#hint-text.md). However, try to keep it as short as possible.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Fieldset’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/48) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/fieldset/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/fieldset/#top.md)
