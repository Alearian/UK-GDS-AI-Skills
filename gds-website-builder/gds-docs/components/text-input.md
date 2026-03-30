#  Text input 
[ Open this example in a new tab: text input ](./components/text-input/default.md)
  * [HTML](./components/text-input/#text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="event-name">
      What is the name of the event?
    </label>
  </h1>
  <input class="govuk-input" id="event-name" name="eventName" type="text">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "What is the name of the event?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  id: "event-name",
  name: "eventName"
}) }}
```

## When to use this component
Use the text input component when you need to let users enter text that’s no longer than a single line, such as their name or phone number.
## When not to use this component
Do not use the text input component if you need to let users enter longer answers that might span multiple lines. In this case, you should use the [Textarea component](./components/textarea.md).
## How it works
All text inputs must have labels, and in most cases the label should be visible.
You should align labels above the text input they refer to. They should be short, direct and written in sentence case. Do not use colons at the end of labels.
### Avoid placeholder text
Do not use placeholder text in place of a label, or for hints or examples, as:
  * it vanishes when the user starts typing, which can cause problems for users with memory conditions or when reviewing answers
  * not all screen readers read it out
  * its browser default styles often do not meet [WCAG 2.2 success criterion 1.4.3 Contrast (minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum)

### If you’re asking one question on the page
If you’re asking just [one question per page in your service](./patterns/question-pages/#start-by-asking-one-question-per-page.md) as recommended, you can set the contents of the `<label>` as the page heading. This is good practice as it means that users of screen readers will only hear the contents once.
Read more about [why and how to set legends as headings](./get-started/labels-legends-headings.md).
There are 2 ways to use the text input component. You can use HTML or, if you’re using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: text input second ](./components/text-input/default.md)
  * [HTML](./components/text-input/#text-input-second-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="event-name">
      What is the name of the event?
    </label>
  </h1>
  <input class="govuk-input" id="event-name" name="eventName" type="text">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-second-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-second-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-second-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-second-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-second-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-second-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-second-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-second-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "What is the name of the event?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  id: "event-name",
  name: "eventName"
}) }}
```

### If you’re asking more than one question on the page
If you’re asking more than one question on the page, do not set the contents of the `<label>` as the page heading. Read more about [asking multiple questions on Question pages](./patterns/question-pages/#asking-multiple-questions-on-a-page.md).
[ Open this example in a new tab: text input without a heading – text input ](./components/text-input/without-heading.md)
  * [HTML](./components/text-input/#text-input-without-a-heading-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-without-a-heading-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="event-name">
    What is the name of the event?
  </label>
  <input class="govuk-input" id="event-name" name="eventName" type="text">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-without-a-heading-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-without-a-heading-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-without-a-heading-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-without-a-heading-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-without-a-heading-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-without-a-heading-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-without-a-heading-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-without-a-heading-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "What is the name of the event?"
  },
  id: "event-name",
  name: "eventName"
}) }}
```

### Use appropriately-sized text inputs
Help users understand what they should enter by making text inputs the right size for the content they’re intended for.
By default, the width of text inputs is fluid and will fit the full width of the container they are placed into.
If you want to make the input smaller, you can either use a fixed width input, or use the width override classes to create a smaller, fluid width input.
#### Fixed width inputs
Use fixed width inputs for content that has a specific, known length. Postcode inputs should be postcode-sized, phone number inputs should be phone number-sized.
The widths are designed for specific character lengths and to be consistent across a range of browsers. They include extra padding to fit icons that some browsers might insert into the input (for example to show or generate a password).
On fixed width inputs, the width will remain fixed on all screens unless it is wider than the viewport, in which case it will shrink to fit.
[ Open this example in a new tab: fixed width inputs – text input ](./components/text-input/input-fixed-width.md)
  * [HTML](./components/text-input/#fixed-width-inputs-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#fixed-width-inputs-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="width-20">
    20 character width
  </label>
  <input class="govuk-input govuk-input--width-20" id="width-20" name="width20" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="width-10">
    10 character width
  </label>
  <input class="govuk-input govuk-input--width-10" id="width-10" name="width10" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="width-5">
    5 character width
  </label>
  <input class="govuk-input govuk-input--width-5" id="width-5" name="width5" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="width-4">
    4 character width
  </label>
  <input class="govuk-input govuk-input--width-4" id="width-4" name="width4" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="width-3">
    3 character width
  </label>
  <input class="govuk-input govuk-input--width-3" id="width-3" name="width3" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="width-2">
    2 character width
  </label>
  <input class="govuk-input govuk-input--width-2" id="width-2" name="width2" type="text">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-fixed-width-inputs-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-fixed-width-inputs-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-fixed-width-inputs-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-fixed-width-inputs-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-fixed-width-inputs-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-fixed-width-inputs-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-fixed-width-inputs-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-fixed-width-inputs-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "20 character width"
  },
  classes: "govuk-input--width-20",
  id: "width-20",
  name: "width20"
}) }}

{{ govukInput({
  label: {
    text: "10 character width"
  },
  classes: "govuk-input--width-10",
  id: "width-10",
  name: "width10"
}) }}

{{ govukInput({
  label: {
    text: "5 character width"
  },
  classes: "govuk-input--width-5",
  id: "width-5",
  name: "width5"
}) }}

{{ govukInput({
  label: {
    text: "4 character width"
  },
  classes: "govuk-input--width-4",
  id: "width-4",
  name: "width4"
}) }}

{{ govukInput({
  label: {
    text: "3 character width"
  },
  classes: "govuk-input--width-3",
  id: "width-3",
  name: "width3"
}) }}

{{ govukInput({
  label: {
    text: "2 character width"
  },
  classes: "govuk-input--width-2",
  id: "width-2",
  name: "width2"
}) }}
```

#### Fluid width inputs
Use the width override classes to reduce the width of an input in relation to its parent container, for example, to two-thirds.
Fluid width inputs will resize with the viewport.
[ Open this example in a new tab: fluid width inputs – text input ](./components/text-input/input-fluid-width.md)
  * [HTML](./components/text-input/#fluid-width-inputs-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#fluid-width-inputs-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="full">
    Full width
  </label>
  <input class="govuk-input govuk-!-width-full" id="full" name="full" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="three-quarters">
    Three-quarters width
  </label>
  <input class="govuk-input govuk-!-width-three-quarters" id="three-quarters" name="threeQuarters" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="two-thirds">
    Two-thirds width
  </label>
  <input class="govuk-input govuk-!-width-two-thirds" id="two-thirds" name="twoThirds" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="one-half">
    One-half width
  </label>
  <input class="govuk-input govuk-!-width-one-half" id="one-half" name="oneHalf" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="one-third">
    One-third width
  </label>
  <input class="govuk-input govuk-!-width-one-third" id="one-third" name="oneThird" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="one-quarter">
    One-quarter width
  </label>
  <input class="govuk-input govuk-!-width-one-quarter" id="one-quarter" name="oneQuarter" type="text">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-fluid-width-inputs-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-fluid-width-inputs-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-fluid-width-inputs-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-fluid-width-inputs-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-fluid-width-inputs-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-fluid-width-inputs-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-fluid-width-inputs-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-fluid-width-inputs-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "Full width"
  },
  classes: "govuk-!-width-full",
  id: "full",
  name: "full"
}) }}

{{ govukInput({
  label: {
    text: "Three-quarters width"
  },
  classes: "govuk-!-width-three-quarters",
  id: "three-quarters",
  name: "threeQuarters"
}) }}

{{ govukInput({
  label: {
    text: "Two-thirds width"
  },
  classes: "govuk-!-width-two-thirds",
  id: "two-thirds",
  name: "twoThirds"
}) }}

{{ govukInput({
  label: {
    text: "One-half width"
  },
  classes: "govuk-!-width-one-half",
  id: "one-half",
  name: "oneHalf"
}) }}

{{ govukInput({
  label: {
    text: "One-third width"
  },
  classes: "govuk-!-width-one-third",
  id: "one-third",
  name: "oneThird"
}) }}

{{ govukInput({
  label: {
    text: "One-quarter width"
  },
  classes: "govuk-!-width-one-quarter",
  id: "one-quarter",
  name: "oneQuarter"
}) }}
```

### Hint text
Use hint text for help that’s relevant to the majority of users, like how their information will be used, or where to find it.
Keep hint text to a single short sentence, without any full stops.
Do not use links in hint text. While screen readers will read out the link text when describing the field, they usually do not tell users the text is a link.
[ Open this example in a new tab: hint text – text input ](./components/text-input/input-hint-text.md)
  * [HTML](./components/text-input/#hint-text-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#hint-text-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="event-name">
      What is the name of the event?
    </label>
  </h1>
  <div id="event-name-hint" class="govuk-hint">
    The name you’ll use on promotional material
  </div>
  <input class="govuk-input" id="event-name" name="eventName" type="text" aria-describedby="event-name-hint">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-hint-text-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-hint-text-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-hint-text-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-hint-text-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-hint-text-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-hint-text-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-hint-text-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-hint-text-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "What is the name of the event?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "The name you’ll use on promotional material"
  },
  id: "event-name",
  name: "eventName"
}) }}
```

#### When not to use hint text
Do not use hint text to explain anything that’s longer than a short, simple sentence. Screen readers read out the entire text when users interact with the form element. This could frustrate users if the text is long.
If you’re asking a question that needs a detailed explanation, see [asking complex questions without using hint text](./patterns/question-pages/#asking-complex-questions-without-using-hint-text.md).
#### Avoid links
Do not include links within hint text. While screen readers will read out the link text when describing the field, they will not tell users that the text is a link.
### Numbers
#### Asking for whole numbers
If you’re asking the user to enter a whole number, set the `inputmode` attribute to `numeric` to use the numeric keypad on devices with on-screen keyboards.
See how to do this by opening the HTML and Nunjucks tabs in this example:
[ Open this example in a new tab: number input – text input ](./components/text-input/number-input.md)
  * [HTML](./components/text-input/#number-input-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#number-input-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="account-number">
      What is your account number?
    </label>
  </h1>
  <div id="account-number-hint" class="govuk-hint">
    Must be between 6 and 8 digits long
  </div>
  <input class="govuk-input govuk-input--width-10" id="account-number" name="accountNumber" type="text" spellcheck="false" aria-describedby="account-number-hint" inputmode="numeric">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-number-input-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-number-input-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-number-input-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-number-input-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-number-input-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-number-input-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-number-input-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-number-input-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "What is your account number?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  classes: "govuk-input--width-10",
  hint: {
    text: "Must be between 6 and 8 digits long"
  },
  id: "account-number",
  name: "accountNumber",
  inputmode: "numeric",
  spellcheck: false
}) }}
```

There is specific guidance on:
  * [how to ask for dates](./patterns/dates.md)
  * [how to ask for phone numbers](./patterns/phone-numbers.md)

#### Asking for decimal numbers
If you’re asking the user to enter a number that might include decimal places, use `input type="text"`.
Do not set the `inputmode` attribute to `decimal` as it causes some devices to bring up a keypad without a key for the decimal separator.
[ Open this example in a new tab: example of an input asking for numbers with decimal places – text input ](./components/text-input/decimal-input.md)
  * [HTML](./components/text-input/#example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="weight">
    Weight, in kilograms
  </label>
  <div class="govuk-input__wrapper">
    <input class="govuk-input govuk-input--width-5" id="weight" name="weight" type="text" spellcheck="false">
    <div class="govuk-input__suffix" aria-hidden="true">kg</div>
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-example-of-an-input-asking-for-numbers-with-decimal-places-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "Weight, in kilograms"
  },
  classes: "govuk-input--width-5",
  id: "weight",
  name: "weight",
  suffix: {
    text: "kg"
  },
  spellcheck: false
}) }}
```

#### Avoid using inputs with a type of number
Do not use `<input type="number">` unless your user research shows that there’s a need for it. With `<input type="number">` there’s a risk of users accidentally incrementing a number when they’re trying to do something else - for example, scroll up or down the page. And if the user tries to enter something that’s not a number, there’s no explicit feedback about what they’re doing wrong.
### Codes and sequences
Help the user visually check the code they’ve typed is correct by styling the input’s text to visually separate each character. This is important if you’re asking the user to enter a code or sequence they’re unlikely to have memorised, such as an application reference ID, account number or security code.
You do not need to do this for memorable information, such as phone numbers and postcodes.
[ Open this example in a new tab: example of a text input asking for a code or sequence – text input ](./components/text-input/code-sequence.md)
  * [HTML](./components/text-input/#example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="authentication-code">
    Company authentication code
  </label>
  <div id="authentication-code-hint" class="govuk-hint">
    This is on the company incorporation letter sent to the registered office address
  </div>
  <input class="govuk-input govuk-input--width-5 govuk-input--extra-letter-spacing" id="authentication-code" name="authenticationCode" type="text" spellcheck="false" value="NC1701" aria-describedby="authentication-code-hint">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-example-of-a-text-input-asking-for-a-code-or-sequence-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "Company authentication code"
  },
  hint: {
    text: "This is on the company incorporation letter sent to the registered office address"
  },
  classes: "govuk-input--width-5 govuk-input--extra-letter-spacing",
  id: "authentication-code",
  name: "authenticationCode",
  spellcheck: false,
  value: "NC1701"
}) }}
```

There is specific guidance on:
  * [how to ask for bank account details](./patterns/bank-details.md)
  * [how to ask for National Insurance numbers](./patterns/national-insurance-numbers.md)
  * [how to confirm a phone number](./patterns/confirm-a-phone-number.md)

### Prefixes and suffixes
Use prefixes and suffixes to help users enter things like currencies and measurements.
[ Open this example in a new tab: text input with prefix and suffix – text input ](./components/text-input/input-prefix-suffix.md)
  * [HTML](./components/text-input/#text-input-with-prefix-and-suffix-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-prefix-and-suffix-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="cost-per-item">
      What is the cost per item, in pounds?
    </label>
  </h1>
  <div class="govuk-input__wrapper">
    <div class="govuk-input__prefix" aria-hidden="true">£</div>
    <input class="govuk-input govuk-input--width-5" id="cost-per-item" name="costPerItem" type="text" spellcheck="false">
    <div class="govuk-input__suffix" aria-hidden="true">per item</div>
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-prefix-and-suffix-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  id: "cost-per-item",
  name: "costPerItem",
  label: {
    text: "What is the cost per item, in pounds?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  prefix: {
    text: "£"
  },
  suffix: {
    text: "per item"
  },
  classes: "govuk-input--width-5",
  spellcheck: false
}) }}
```

Prefixes and suffixes are useful when there’s a commonly understood symbol or abbreviation for the type of information you’re asking for. Do not rely on prefixes or suffixes alone, because screen readers will not read them out.
If you need a specific type of information, say so in the input label or hint text as well. For example, put ‘Cost, in pounds’ in the input label and use the ‘£’ symbol in the prefix.
Position prefixes and suffixes so that they’re outside of their input. This is to avoid interfering with some browsers that might insert an icon into the input (for example to show or generate a password).
Some users may miss that the input already has a suffix or prefix, and enter a prefix or suffix into the input. Allow for this in your validation and do not show an error.
#### Text inputs with a prefix
[ Open this example in a new tab: text input with prefix – text input ](./components/text-input/input-prefix.md)
  * [HTML](./components/text-input/#text-input-with-prefix-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-prefix-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="cost">
      What is the cost in pounds?
    </label>
  </h1>
  <div class="govuk-input__wrapper">
    <div class="govuk-input__prefix" aria-hidden="true">£</div>
    <input class="govuk-input govuk-input--width-5" id="cost" name="cost" type="text" spellcheck="false">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-prefix-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-prefix-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-prefix-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-prefix-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-prefix-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-prefix-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-prefix-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-prefix-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  id: "cost",
  name: "cost",
  label: {
    text: "What is the cost in pounds?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  prefix: {
    text: "£"
  },
  classes: "govuk-input--width-5",
  spellcheck: false
}) }}
```

#### Text inputs with a suffix
[ Open this example in a new tab: text input with suffix – text input ](./components/text-input/input-suffix.md)
  * [HTML](./components/text-input/#text-input-with-suffix-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-suffix-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="weight">
      What is the weight in kilograms?
    </label>
  </h1>
  <div class="govuk-input__wrapper">
    <input class="govuk-input govuk-input--width-5" id="weight" name="weight" type="text" spellcheck="false">
    <div class="govuk-input__suffix" aria-hidden="true">kg</div>
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-suffix-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-suffix-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-suffix-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-suffix-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-suffix-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-suffix-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-suffix-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-suffix-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  id: "weight",
  name: "weight",
  label: {
    text: "What is the weight in kilograms?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  suffix: {
    text: "kg"
  },
  classes: "govuk-input--width-5",
  spellcheck: false
}) }}
```

### Use the autocomplete attribute
Use the `autocomplete` attribute on text inputs to help users complete forms more quickly. This lets you specify an input’s purpose so browsers can autofill the information on a user’s behalf if they’ve entered it previously.
For example, to enable autofill on a postcode field, set the `autocomplete` attribute to `postal-code`. See how to do this in the HTML and Nunjucks tabs in the following example.
  * [HTML](./components/text-input/#text-input-with-autocomplete-attribute-text-input-example-open-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-autocomplete-attribute-text-input-example-open-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="postcode">
    Postcode
  </label>
  <input class="govuk-input govuk-input--width-10" id="postcode" name="postcode" type="text" autocomplete="postal-code">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-autocomplete-attribute-text-input-example-open--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "Postcode"
  },
  classes: "govuk-input--width-10",
  id: "postcode",
  name: "postcode",
  autocomplete: "postal-code"
}) }}
```

If you are working in production and there is a relevant [input purpose](https://www.w3.org/TR/WCAG22/#input-purposes), you’ll need to use the `autocomplete` attribute to meet [WCAG 2.2 success criterion 1.3.5 Identify input purpose, level AA](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html).
You will not normally need to use the `autocomplete` attribute in prototypes, as users will not generally be using their own devices.
### Do not disable copy and paste
Users often need to copy and paste information into a text input, so do not stop them from doing this.
### Avoid restricting the length of a user’s input
Using the `maxlength` attribute means there is no feedback to users that their text input is truncated. This is especially true where the text has been copied and pasted from elsewhere. This can cause users to accidentally provide incorrect or incomplete information.
A restrictive maximum length can stop users from formatting information in their usual way. For example, putting spaces in a postcode or commas in a large number.
Some assistive technologies do not tell users if an input has a `maxlength` set or if the user has passed the limit. Voice control software may insert additional spaces into the input.
If you must enforce a maximum length for technical reasons, inform the user of the limit in the hint, but allow them to provide more information. Only return an error if the value is longer than allowed after normalisation. For longer values, consider using the [Character count component](./components/character-count.md) instead.
### How and when to spellcheck a user’s input
Sometimes, browsers will spellcheck the information a user puts into a text input. If a user enters something which is recognised as a spelling error, sighted users will see a red line under the word.
If you are asking users for information which is not appropriate to spellcheck, like a reference number, name, email address or National Insurance number, disable the spellcheck.
To do this set the `spellcheck` attribute to `false` as shown in this example.
  * [HTML](./components/text-input/#text-input-with-spellcheck-disabled-text-input-example-open-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-spellcheck-disabled-text-input-example-open-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="name">
    Reference number
  </label>
  <input class="govuk-input" id="name" name="name" type="text" spellcheck="false">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-spellcheck-disabled-text-input-example-open--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "Reference number"
  },
  id: "name",
  name: "name",
  spellcheck: false
}) }}
```

Browsers do not consistently spellcheck user’s input by default. If you are asking a question where spellcheck would be useful, set the `spellcheck` attribute to `true`.
### Error messages
Error messages should be styled like this:
[ Open this example in a new tab: text input with errors – text input ](./components/text-input/error.md)
  * [HTML](./components/text-input/#text-input-with-errors-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-errors-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="event-name">
      What is the name of the event?
    </label>
  </h1>
  <div id="event-name-hint" class="govuk-hint">
    The name you’ll use on promotional material
  </div>
  <p id="event-name-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Enter an event name
  </p>
  <input class="govuk-input govuk-input--error" id="event-name" name="eventName" type="text" aria-describedby="event-name-hint event-name-error">
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-errors-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-errors-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-errors-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-errors-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-errors-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-errors-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-errors-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-errors-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  label: {
    text: "What is the name of the event?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  id: "event-name",
  name: "eventName",
  hint: {
    text: "The name you’ll use on promotional material"
  },
  errorMessage: {
    text: "Enter an event name"
  }
}) }}
```

#### If the input has a prefix or a suffix
[ Open this example in a new tab: text input with prefix and suffix with error – text input ](./components/text-input/input-prefix-suffix-error.md)
  * [HTML](./components/text-input/#text-input-with-prefix-and-suffix-with-error-text-input-example-html.md)
  * [Nunjucks](./components/text-input/#text-input-with-prefix-and-suffix-with-error-text-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="cost-per-item-error">
      What is the cost per item, in pounds?
    </label>
  </h1>
  <p id="cost-per-item-error-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Enter a cost per item, in pounds
  </p>
  <div class="govuk-input__wrapper">
    <div class="govuk-input__prefix" aria-hidden="true">£</div>
    <input class="govuk-input govuk-input--width-5 govuk-input--error" id="cost-per-item-error" name="costPerItemError" type="text" spellcheck="false" aria-describedby="cost-per-item-error-error">
    <div class="govuk-input__suffix" aria-hidden="true">per item</div>
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
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| type  | string  |  Type of input control to render, for example, a password input control. Defaults to `"text"`.   |  
| inputmode  | string  |  Optional value for [the inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode).   |  
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| prefix  | object  |  Can be used to add a prefix to the text input component. [ See macro options for prefix](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--prefix.md).   |  
| suffix  | object  |  Can be used to add a suffix to the text input component. [ See macro options for suffix](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--suffix.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the input.   |  
| autocapitalize  | string  |  Optional field to enable or disable autocapitalisation of user input. [See the Autocapitalization section in the HTML spec](https://html.spec.whatwg.org/multipage/interaction.html#autocapitalization) for a full list of values that can be used.   |  
| inputWrapper  | object  |  If any of `prefix`, `suffix`, `formGroup.beforeInput` or `formGroup.afterInput` have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. [ See macro options for inputWrapper](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--input-wrapper.md).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
Options for `prefix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Required. If `html` is set, this is not required. Text to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** Required. If `text` is set, this is not required. HTML to use within the prefix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the prefix.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the prefix element.   |  
Options for `suffix` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the suffix. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the suffix element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the suffix element.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/text-input/#options-text-input-with-prefix-and-suffix-with-error-text-input-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the input. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the input. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the input. If `html` is provided, the `text` option will be ignored.   |  
Options for `inputWrapper` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the wrapping element.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the wrapping element.   |  
Options for `label` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the label. If `html` is provided, the `text` option will be ignored.   |  
| for  | string  |  The value of the `for` attribute, the ID of the input the label is associated with.   |  
| isPageHeading  | boolean  |  Whether the label also acts as the heading for the page.   |  
| classes  | string  |  Classes to add to the label tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the label tag.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/input/macro.njk" import govukInput %}

{{ govukInput({
  id: "cost-per-item-error",
  name: "costPerItemError",
  label: {
    text: "What is the cost per item, in pounds?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  prefix: {
    text: "£"
  },
  suffix: {
    text: "per item"
  },
  errorMessage: {
    text: "Enter a cost per item, in pounds"
  },
  classes: "govuk-input--width-5",
  spellcheck: false
}) }}
```

Make sure errors follow the guidance in the [Error message component](./components/error-message.md) and have specific error messages for specific error states.
#### If the input is empty
Say ‘Enter [whatever it is]’.  
  
For example, ‘Enter your first name’.
#### If the input is too long
Say ‘[whatever it is] must be [number] characters or less’.  
  
For example, ‘Address line 1 must be 35 characters or less’.
#### If the input is too short
Say ‘[whatever it is] must be [number] characters or more’.  
  
For example, ‘Full name must be 2 characters or more’.
#### If the input has both a minimum and maximum length
Say ‘[whatever it is] must be between [number] and [number] characters’.  
  
For example, ‘Last name must be between 2 and 35 characters’.
#### If the input uses characters that are not allowed and you know what the characters are
Say ‘[whatever it is] must not include [characters]’.  
  
For example, ‘Town or city must not include è and £’.
Support all the characters the user might need to enter, including numbers and symbols.
#### If the input uses characters that are not allowed and you do not know what the characters are
Say ‘[whatever it is] must only include [list of allowed characters]’.  
  
For example, ‘Full name must only include letters a to z, and special characters such as hyphens, spaces and apostrophes’.
Support all the characters the user might need to enter, including numbers and symbols.
#### If the input is not a number
Say ‘[whatever it is] must be a number [optional example]’.  
  
For example, ‘Hours worked a week must be a number, like 30’.
If the input requires a decimal, use a decimal in the example. If the input allows both whole numbers and decimals, use both in the example.
#### If the input is not a whole number
Say ‘[whatever it is] must be a whole number [optional example]’.  
  
For example, ‘Hours worked a week must be a whole number, like 30’.
#### If the number is too low
Say ‘[whatever it is] must be [lowest] or more’.  
  
For example, ‘Hours worked a week must be 16 or more’.
#### If the number is too high
Say ‘[whatever it is] must be [highest] or fewer’.  
  
For example, ‘Hours worked a week must be 99 or fewer’.
#### If the input must be between 2 numbers
Say ‘[whatever it is] must be between [lowest] and [highest]’.  
  
For example, ‘Hours worked a week must be between 16 and 99’.
#### If the input is an amount of money that needs decimals
Say ‘[whatever it is] must include pence, like 123.45 or 156.00’.  
  
For example, ‘How much you earn a week must include pence, like 123.45 or 156.00’.
#### If the input is an amount of money that must not have decimals
Say ‘[whatever it is] must not include pence, like 123 or 156’.  
  
For example, ‘How much you earn a week must not include pence, like 123 or 156’.
## Research on this component
Read a blog post about [the problems we discovered with input type=”number”](https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/).
The prefix and suffix design has tested well in a number of services, but [some users have been observed clicking on prefixes](https://github.com/alphagov/govuk-design-system-backlog/issues/134#issuecomment-655615251), on the assumption that this would do something.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Text input’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/51) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/text-input/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/text-input/#top.md)
