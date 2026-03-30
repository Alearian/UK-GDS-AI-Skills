#  Textarea 
[ Open this example in a new tab: textarea ](./components/textarea/default.md)
  * [HTML](./components/textarea/#textarea-example-html.md)
  * [Nunjucks](./components/textarea/#textarea-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="more-detail">
      Can you provide more detail?
    </label>
  </h1>
  <div id="more-detail-hint" class="govuk-hint">
    Do not include personal or financial information, like your National Insurance number or credit card details
  </div>
  <textarea class="govuk-textarea" id="more-detail" name="moreDetail" rows="5" aria-describedby="more-detail-hint"></textarea>
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the textarea.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| disabled  | boolean  |  If `true`, textarea will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the textarea component. [ See macro options for label](./components/textarea/#options-textarea-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the textarea component. [ See macro options for hint](./components/textarea/#options-textarea-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the textarea component. [ See macro options for formGroup](./components/textarea/#options-textarea-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the textarea component. [ See macro options for formGroup beforeInput](./components/textarea/#options-textarea-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the textarea component. [ See macro options for formGroup afterInput](./components/textarea/#options-textarea-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
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
{% from "govuk/components/textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  name: "moreDetail",
  id: "more-detail",
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "Do not include personal or financial information, like your National Insurance number or credit card details"
  }
}) }}
```

## When to use this component
Use the textarea component when you need to let users enter an amount of text that’s longer than a single line.
## When not to use this component
Users can find open-ended questions difficult to answer. It might be better to break up one complex question into a series of simple ones, for example where users can select from options using a [Radios component](./components/radios.md).
### If you need to ask an open question
Do not use the textarea component if you need to let users enter shorter answers no longer than a single line, such as a phone number or name. In this case, you should use the [Text input component](./components/text-input.md).
## How it works
You must label textareas. Placeholder text is not a suitable substitute for a label, as it disappears when users click inside the textarea.
Labels must be aligned above the textarea they refer to. They should be short, direct and written in sentence case. Do not use colons at the end of labels.
There are 2 ways to use the textarea component. You can use HTML or, if you’re using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: textarea second ](./components/textarea/default.md)
  * [HTML](./components/textarea/#textarea-second-example-html.md)
  * [Nunjucks](./components/textarea/#textarea-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="more-detail">
      Can you provide more detail?
    </label>
  </h1>
  <div id="more-detail-hint" class="govuk-hint">
    Do not include personal or financial information, like your National Insurance number or credit card details
  </div>
  <textarea class="govuk-textarea" id="more-detail" name="moreDetail" rows="5" aria-describedby="more-detail-hint"></textarea>
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the textarea.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| disabled  | boolean  |  If `true`, textarea will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the textarea component. [ See macro options for label](./components/textarea/#options-textarea-second-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the textarea component. [ See macro options for hint](./components/textarea/#options-textarea-second-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the textarea component. [ See macro options for formGroup](./components/textarea/#options-textarea-second-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the textarea component. [ See macro options for formGroup beforeInput](./components/textarea/#options-textarea-second-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the textarea component. [ See macro options for formGroup afterInput](./components/textarea/#options-textarea-second-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
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
{% from "govuk/components/textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  name: "moreDetail",
  id: "more-detail",
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "Do not include personal or financial information, like your National Insurance number or credit card details"
  }
}) }}
```

### Use appropriately-sized textareas
Make the height of a textarea proportional to the amount of text you expect users to enter. You can set the height of a textarea by specifying the `rows` attribute.
[ Open this example in a new tab: textarea appropriately-sized with rows – textarea ](./components/textarea/specifying-rows.md)
  * [HTML](./components/textarea/#textarea-appropriately-sized-with-rows-textarea-example-html.md)
  * [Nunjucks](./components/textarea/#textarea-appropriately-sized-with-rows-textarea-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="more-detail">
      Can you provide more detail?
    </label>
  </h1>
  <div id="more-detail-hint" class="govuk-hint">
    Do not include personal or financial information, like your National Insurance number or credit card details
  </div>
  <textarea class="govuk-textarea" id="more-detail" name="moreDetail" rows="8" aria-describedby="more-detail-hint"></textarea>
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the textarea.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| disabled  | boolean  |  If `true`, textarea will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the textarea component. [ See macro options for label](./components/textarea/#options-textarea-appropriately-sized-with-rows-textarea-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the textarea component. [ See macro options for hint](./components/textarea/#options-textarea-appropriately-sized-with-rows-textarea-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the textarea component. [ See macro options for formGroup](./components/textarea/#options-textarea-appropriately-sized-with-rows-textarea-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the textarea component. [ See macro options for formGroup beforeInput](./components/textarea/#options-textarea-appropriately-sized-with-rows-textarea-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the textarea component. [ See macro options for formGroup afterInput](./components/textarea/#options-textarea-appropriately-sized-with-rows-textarea-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
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
{% from "govuk/components/textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  name: "moreDetail",
  id: "more-detail",
  rows: "8",
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "Do not include personal or financial information, like your National Insurance number or credit card details"
  }
}) }}
```

### Do not disable copy and paste
Users will often need to copy and paste information into a textarea, so do not stop them from doing this.
### If you’re asking more than one question on the page
If you’re asking more than one question on the page, do not set the contents of the `<label>` as the page heading. Read more about [asking multiple questions on Question pages](./patterns/question-pages/#asking-multiple-questions-on-a-page.md).
[ Open this example in a new tab: textarea without a heading – textarea ](./components/textarea/without-heading.md)
  * [HTML](./components/textarea/#textarea-without-a-heading-textarea-example-html.md)
  * [Nunjucks](./components/textarea/#textarea-without-a-heading-textarea-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="more-detail">
    Can you provide more detail?
  </label>
  <textarea class="govuk-textarea" id="more-detail" name="moreDetail" rows="5"></textarea>
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the textarea.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| disabled  | boolean  |  If `true`, textarea will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the textarea component. [ See macro options for label](./components/textarea/#options-textarea-without-a-heading-textarea-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the textarea component. [ See macro options for hint](./components/textarea/#options-textarea-without-a-heading-textarea-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the textarea component. [ See macro options for formGroup](./components/textarea/#options-textarea-without-a-heading-textarea-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the textarea component. [ See macro options for formGroup beforeInput](./components/textarea/#options-textarea-without-a-heading-textarea-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the textarea component. [ See macro options for formGroup afterInput](./components/textarea/#options-textarea-without-a-heading-textarea-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
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
{% from "govuk/components/textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  name: "moreDetail",
  id: "more-detail",
  label: {
    text: "Can you provide more detail?"
  }
}) }}
```

### Limiting the number of characters
If there’s a good reason to limit the number of characters users can enter, you can use the [Character count component](./components/character-count.md).
### Error messages
Error messages should be styled like this:
[ Open this example in a new tab: textarea with error – textarea ](./components/textarea/error.md)
  * [HTML](./components/textarea/#textarea-with-error-textarea-example-html.md)
  * [Nunjucks](./components/textarea/#textarea-with-error-textarea-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="more-detail">
      Can you provide more detail?
    </label>
  </h1>
  <div id="more-detail-hint" class="govuk-hint">
    Do not include personal or financial information, like your National Insurance number or credit card details
  </div>
  <p id="more-detail-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Enter more detail
  </p>
  <textarea class="govuk-textarea govuk-textarea--error" id="more-detail" name="moreDetail" rows="5" aria-describedby="more-detail-hint more-detail-error"></textarea>
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the textarea.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| disabled  | boolean  |  If `true`, textarea will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the textarea component. [ See macro options for label](./components/textarea/#options-textarea-with-error-textarea-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the textarea component. [ See macro options for hint](./components/textarea/#options-textarea-with-error-textarea-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the textarea component. [ See macro options for formGroup](./components/textarea/#options-textarea-with-error-textarea-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the textarea component. [ See macro options for formGroup beforeInput](./components/textarea/#options-textarea-with-error-textarea-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the textarea component. [ See macro options for formGroup afterInput](./components/textarea/#options-textarea-with-error-textarea-example--form-group-after-input.md).   |  
Options for formGroup `beforeInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the textarea. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInput` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the textarea. If `html` is provided, the `text` option will be ignored.   |  
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
{% from "govuk/components/textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  name: "moreDetail",
  id: "more-detail",
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "Do not include personal or financial information, like your National Insurance number or credit card details"
  },
  errorMessage: {
    text: "Enter more detail"
  }
}) }}
```

Make sure errors follow the guidance in the [Error message component](./components/error-message.md) and have specific error messages for specific error states.
#### If the input is empty
Say ‘Enter [whatever it is]’.  
  
For example, ‘Enter summary’.
#### If the input is too long
Say ‘[whatever it is] must be [number] characters or less’.  
  
For example, ‘Summary must be 400 characters or less’.
#### If the input is too short
Say ‘[whatever it is] must be [number] characters or more’.  
  
For example, ‘Summary must be 10 characters or more’.
#### If the input is too long or too short
Say ‘[whatever it is] must be between [number] and [number] characters’.  
  
For example, ‘Summary must be between 10 and 400 characters’.
#### If the input uses characters that are not allowed and you know what the characters are
Say ‘[whatever it is] must not include [characters]’.  
  
For example, ‘Summary must not include è and £’.
#### If the input uses characters that are not allowed and you do not know what the characters are
Say ‘[whatever it is] must only include [list of allowed characters]’.  
  
For example, ‘Summary must only include letters a to z, hyphens, spaces and apostrophes.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Textarea’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/65) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/textarea/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/textarea/#top.md)
