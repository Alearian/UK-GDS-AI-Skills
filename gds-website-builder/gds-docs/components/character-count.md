#  Character count 
Help users know how much text they can enter when there is a limit on the number of characters.
[ Open this example in a new tab: character count ](./components/character-count/default.md)
  * [HTML](./components/character-count/#character-count-example-html.md)
  * [Nunjucks](./components/character-count/#character-count-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-character-count" data-module="govuk-character-count" data-maxlength="200">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="with-hint">
      Can you provide more detail?
    </label>
  </h1>
  <div id="with-hint-hint" class="govuk-hint">
    Do not include personal or financial information like your National Insurance number or credit card details
  </div>
  <textarea class="govuk-textarea govuk-js-character-count" id="with-hint" name="withHint" rows="5" aria-describedby="with-hint-info with-hint-hint"></textarea>
  <div id="with-hint-info" class="govuk-hint govuk-character-count__message">
    You can enter up to 200 characters
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| maxlength  | string  |  **Required.** If `maxwords` is set, this is not required. The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| maxwords  | string  |  **Required.** If `maxlength` is set, this is not required. The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| threshold  | string  |  The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.   |  
| label  | object  |  **Required.** The label used by the character count component. [ See macro options for label](./components/character-count/#options-character-count-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the character count component. [ See macro options for hint](./components/character-count/#options-character-count-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the character count component. [ See macro options for formGroup](./components/character-count/#options-character-count-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the character count.   |  
| countMessage  | object  |  Additional options for the count message used by the character count component. [ See macro options for countMessage](./components/character-count/#options-character-count-example--count-message.md).   |  
| textareaDescriptionText  | string  |  Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page when JavaScript is unavailable. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` parameter.   |  
| charactersUnderLimitText  | object  |  Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| charactersAtLimitText  | string  |  Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.   |  
| charactersOverLimitText  | object  |  Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum.[Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsUnderLimitText  | object  |  Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsAtLimitText  | string  |  Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.   |  
| wordsOverLimitText  | object  |  Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the character count component. [ See macro options for formGroup beforeInput](./components/character-count/#options-character-count-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the character count component. [ See macro options for formGroup afterInput](./components/character-count/#options-character-count-example--form-group-after-input.md).   |  
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
Options for `countMessage` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the count message.   |  
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
{% from "govuk/components/character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  name: "withHint",
  id: "with-hint",
  maxlength: 200,
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "Do not include personal or financial information like your National Insurance number or credit card details"
  }
}) }}
```

## When to use this component
Always test your service without a character count first.
Only use the character count component when there is a good reason for limiting the number of characters users can enter. For example, if there is:
  * evidence that users are likely to enter more information than they need to
  * a legal or technical reason that means an entry must be no more than a certain number of characters

## When not to use this component
If your users keep hitting the character limit imposed by the backend of your service then try to increase the limit rather than use a character count.
## How it works
It tells users how many characters they have remaining as they type into a [Textarea component](./components/textarea.md) with a character limit.
Users will get updates at a pace that works best for the way they interact with the textarea. This means:
  * sighted users will see a count message that updates as they type
  * screen reader users will hear the count announcement when they stop typing.

This component does not restrict the user from entering information. The user can enter more than the character limit, but are told they’ve entered too many characters. This lets them type or copy and paste their full answer, then edit it down.
The count message appears below the textarea so that:
  * it’s clearly separate from any hint text or error message above the textarea
  * if it’s below the visible screen area, users will still see it again when they scroll down to send their response

This component uses JavaScript. If JavaScript is not available, users will see a static message in place of the count message, telling them how many characters they can enter.
There are 2 ways to use the character count component. You can use HTML or, if you’re using Nunjucks or the GOV.UK Prototype Kit, you can use the Nunjucks macro.
[ Open this example in a new tab: character count second ](./components/character-count/default.md)
  * [HTML](./components/character-count/#character-count-second-example-html.md)
  * [Nunjucks](./components/character-count/#character-count-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-character-count" data-module="govuk-character-count" data-maxlength="200">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="with-hint">
      Can you provide more detail?
    </label>
  </h1>
  <div id="with-hint-hint" class="govuk-hint">
    Do not include personal or financial information like your National Insurance number or credit card details
  </div>
  <textarea class="govuk-textarea govuk-js-character-count" id="with-hint" name="withHint" rows="5" aria-describedby="with-hint-info with-hint-hint"></textarea>
  <div id="with-hint-info" class="govuk-hint govuk-character-count__message">
    You can enter up to 200 characters
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| maxlength  | string  |  **Required.** If `maxwords` is set, this is not required. The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| maxwords  | string  |  **Required.** If `maxlength` is set, this is not required. The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| threshold  | string  |  The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.   |  
| label  | object  |  **Required.** The label used by the character count component. [ See macro options for label](./components/character-count/#options-character-count-second-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the character count component. [ See macro options for hint](./components/character-count/#options-character-count-second-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the character count component. [ See macro options for formGroup](./components/character-count/#options-character-count-second-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the character count.   |  
| countMessage  | object  |  Additional options for the count message used by the character count component. [ See macro options for countMessage](./components/character-count/#options-character-count-second-example--count-message.md).   |  
| textareaDescriptionText  | string  |  Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page when JavaScript is unavailable. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` parameter.   |  
| charactersUnderLimitText  | object  |  Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| charactersAtLimitText  | string  |  Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.   |  
| charactersOverLimitText  | object  |  Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum.[Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsUnderLimitText  | object  |  Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsAtLimitText  | string  |  Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.   |  
| wordsOverLimitText  | object  |  Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the character count component. [ See macro options for formGroup beforeInput](./components/character-count/#options-character-count-second-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the character count component. [ See macro options for formGroup afterInput](./components/character-count/#options-character-count-second-example--form-group-after-input.md).   |  
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
Options for `countMessage` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the count message.   |  
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
{% from "govuk/components/character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  name: "withHint",
  id: "with-hint",
  maxlength: 200,
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  hint: {
    text: "Do not include personal or financial information like your National Insurance number or credit card details"
  }
}) }}
```

### If you’re asking more than one question on the page
If you’re asking more than one question on the page, do not set the contents of the `<label>` as the page heading. Read more about [asking multiple questions on Question pages](./patterns/question-pages/#asking-multiple-questions-on-a-page.md).
[ Open this example in a new tab: character count without a heading – character count ](./components/character-count/without-heading.md)
  * [HTML](./components/character-count/#character-count-without-a-heading-character-count-example-html.md)
  * [Nunjucks](./components/character-count/#character-count-without-a-heading-character-count-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-character-count" data-module="govuk-character-count" data-maxlength="200">
  <label class="govuk-label" for="label-as-page-heading">
    Describe the nature of your event
  </label>
  <textarea class="govuk-textarea govuk-js-character-count" id="label-as-page-heading" name="labelAsPageHeading" rows="5" aria-describedby="label-as-page-heading-info"></textarea>
  <div id="label-as-page-heading-info" class="govuk-hint govuk-character-count__message">
    You can enter up to 200 characters
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| maxlength  | string  |  **Required.** If `maxwords` is set, this is not required. The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| maxwords  | string  |  **Required.** If `maxlength` is set, this is not required. The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| threshold  | string  |  The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.   |  
| label  | object  |  **Required.** The label used by the character count component. [ See macro options for label](./components/character-count/#options-character-count-without-a-heading-character-count-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the character count component. [ See macro options for hint](./components/character-count/#options-character-count-without-a-heading-character-count-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the character count component. [ See macro options for formGroup](./components/character-count/#options-character-count-without-a-heading-character-count-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the character count.   |  
| countMessage  | object  |  Additional options for the count message used by the character count component. [ See macro options for countMessage](./components/character-count/#options-character-count-without-a-heading-character-count-example--count-message.md).   |  
| textareaDescriptionText  | string  |  Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page when JavaScript is unavailable. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` parameter.   |  
| charactersUnderLimitText  | object  |  Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| charactersAtLimitText  | string  |  Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.   |  
| charactersOverLimitText  | object  |  Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum.[Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsUnderLimitText  | object  |  Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsAtLimitText  | string  |  Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.   |  
| wordsOverLimitText  | object  |  Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the character count component. [ See macro options for formGroup beforeInput](./components/character-count/#options-character-count-without-a-heading-character-count-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the character count component. [ See macro options for formGroup afterInput](./components/character-count/#options-character-count-without-a-heading-character-count-example--form-group-after-input.md).   |  
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
Options for `countMessage` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the count message.   |  
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
{% from "govuk/components/character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  id: "label-as-page-heading",
  name: "labelAsPageHeading",
  maxlength: 200,
  label: {
    text: "Describe the nature of your event"
  }
}) }}
```

### Consider if a word count is more helpful
In some cases it may be more helpful to show a word count. For example, if your question requires a longer answer.
Do this by setting `data-maxwords` in the component markup. For example, `data-maxwords="150"` will set a word limit of 150.
[ Open this example in a new tab: word count – character count ](./components/character-count/word-count.md)
  * [HTML](./components/character-count/#word-count-character-count-example-html.md)
  * [Nunjucks](./components/character-count/#word-count-character-count-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-character-count" data-module="govuk-character-count" data-maxwords="150">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="word-count">
      Enter a job description
    </label>
  </h1>
  <textarea class="govuk-textarea govuk-js-character-count" id="word-count" name="wordCount" rows="5" aria-describedby="word-count-info"></textarea>
  <div id="word-count-info" class="govuk-hint govuk-character-count__message">
    You can enter up to 150 words
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| maxlength  | string  |  **Required.** If `maxwords` is set, this is not required. The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| maxwords  | string  |  **Required.** If `maxlength` is set, this is not required. The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| threshold  | string  |  The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.   |  
| label  | object  |  **Required.** The label used by the character count component. [ See macro options for label](./components/character-count/#options-word-count-character-count-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the character count component. [ See macro options for hint](./components/character-count/#options-word-count-character-count-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the character count component. [ See macro options for formGroup](./components/character-count/#options-word-count-character-count-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the character count.   |  
| countMessage  | object  |  Additional options for the count message used by the character count component. [ See macro options for countMessage](./components/character-count/#options-word-count-character-count-example--count-message.md).   |  
| textareaDescriptionText  | string  |  Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page when JavaScript is unavailable. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` parameter.   |  
| charactersUnderLimitText  | object  |  Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| charactersAtLimitText  | string  |  Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.   |  
| charactersOverLimitText  | object  |  Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum.[Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsUnderLimitText  | object  |  Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsAtLimitText  | string  |  Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.   |  
| wordsOverLimitText  | object  |  Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the character count component. [ See macro options for formGroup beforeInput](./components/character-count/#options-word-count-character-count-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the character count component. [ See macro options for formGroup afterInput](./components/character-count/#options-word-count-character-count-example--form-group-after-input.md).   |  
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
Options for `countMessage` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the count message.   |  
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
{% from "govuk/components/character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  name: "wordCount",
  id: "word-count",
  maxwords: 150,
  label: {
    text: "Enter a job description",
    classes: "govuk-label--l",
    isPageHeading: true
  }
}) }}
```

### Avoid narrow limits
When using a character count, try to set the limit higher than most users will need. Find out what this is by doing user research and data analysis.
#### If the limit is far higher than users are likely to reach
You can choose to display a character count message when the length of text within the textarea passes a certain ‘threshold’ of characters. This is useful when a character limit is needed due to the technical limitations of the service, but users are unlikely to reach that limit.
To do this, set the threshold in the component markup as a percentage. For example, `data-threshold="75"` will show the count message only when the user has entered a length of text that’s 75% of the limit or more.
Screen reader users will hear the character limit when they first interact with a textarea using the threshold option. Sighted users will not see anything until the count message is shown – though you might choose to include the character limit in the hint text.
[ Open this example in a new tab: threshold – character count ](./components/character-count/threshold.md)
  * [HTML](./components/character-count/#threshold-character-count-example-html.md)
  * [Nunjucks](./components/character-count/#threshold-character-count-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-character-count" data-module="govuk-character-count" data-maxlength="1000" data-threshold="85">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="threshold">
      Can you provide more detail?
    </label>
  </h1>
  <textarea class="govuk-textarea govuk-js-character-count" id="threshold" name="threshold" rows="5" aria-describedby="threshold-info">This example of a textarea has a character limit of 1000 characters. The character count is hidden, but will appear when more than 850 characters are entered in this textarea. Type some more text into this textarea to see the character count appear. This paragraph will now repeat 2 more times.

This example of a textarea has a character limit of 1000 characters. The character count is hidden, but will appear when more than 850 characters are entered in this textarea. Type some more text into this textarea to see the character count appear. This paragraph will now repeat 1 more time.

This example of a textarea has a character limit of 1000 characters. The character count is hidden, but will appear when more than 850 characters are entered in this textarea. Type some more text into this textarea to see the character count appear.</textarea>
  <div id="threshold-info" class="govuk-hint govuk-character-count__message">
    You can enter up to 1000 characters
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| maxlength  | string  |  **Required.** If `maxwords` is set, this is not required. The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| maxwords  | string  |  **Required.** If `maxlength` is set, this is not required. The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| threshold  | string  |  The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.   |  
| label  | object  |  **Required.** The label used by the character count component. [ See macro options for label](./components/character-count/#options-threshold-character-count-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the character count component. [ See macro options for hint](./components/character-count/#options-threshold-character-count-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the character count component. [ See macro options for formGroup](./components/character-count/#options-threshold-character-count-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the character count.   |  
| countMessage  | object  |  Additional options for the count message used by the character count component. [ See macro options for countMessage](./components/character-count/#options-threshold-character-count-example--count-message.md).   |  
| textareaDescriptionText  | string  |  Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page when JavaScript is unavailable. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` parameter.   |  
| charactersUnderLimitText  | object  |  Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| charactersAtLimitText  | string  |  Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.   |  
| charactersOverLimitText  | object  |  Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum.[Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsUnderLimitText  | object  |  Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsAtLimitText  | string  |  Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.   |  
| wordsOverLimitText  | object  |  Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the character count component. [ See macro options for formGroup beforeInput](./components/character-count/#options-threshold-character-count-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the character count component. [ See macro options for formGroup afterInput](./components/character-count/#options-threshold-character-count-example--form-group-after-input.md).   |  
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
Options for `countMessage` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the count message.   |  
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
{% from "govuk/components/character-count/macro.njk" import govukCharacterCount %}

{% set textareaValue -%}
This example of a textarea has a character limit of 1000 characters. The character count is hidden, but will appear when more than 850 characters are entered in this textarea. Type some more text into this textarea to see the character count appear. This paragraph will now repeat 2 more times.

This example of a textarea has a character limit of 1000 characters. The character count is hidden, but will appear when more than 850 characters are entered in this textarea. Type some more text into this textarea to see the character count appear. This paragraph will now repeat 1 more time.

This example of a textarea has a character limit of 1000 characters. The character count is hidden, but will appear when more than 850 characters are entered in this textarea. Type some more text into this textarea to see the character count appear.
{%- endset %}

{{ govukCharacterCount({
  name: "threshold",
  id: "threshold",
  maxlength: 1000,
  threshold: 85,
  value: textareaValue,
  label: {
    text: "Can you provide more detail?",
    classes: "govuk-label--l",
    isPageHeading: true
  }
}) }}
```

### Error messages
Error messages should be styled like this:
[ Open this example in a new tab: error – character count ](./components/character-count/error.md)
  * [HTML](./components/character-count/#error-character-count-example-html.md)
  * [Nunjucks](./components/character-count/#error-character-count-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error govuk-character-count" data-module="govuk-character-count" data-maxlength="350">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label govuk-label--l" for="exceeding-characters">
      Enter a job description
    </label>
  </h1>
  <p id="exceeding-characters-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Job description must be 350 characters or less
  </p>
  <textarea class="govuk-textarea govuk-textarea--error govuk-js-character-count" id="exceeding-characters" name="exceeding" rows="5" aria-describedby="exceeding-characters-info exceeding-characters-error">A content designer works on the end-to-end journey of a service to help users complete their goal and government deliver a policy intent. Their work may involve the creation of, or change to, a transaction, product or single piece of content that stretches across digital and offline channels. They make sure appropriate content is shown to a user in the right place and in the best format.</textarea>
  <div id="exceeding-characters-info" class="govuk-hint govuk-character-count__message">
    You can enter up to 350 characters
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
| id  | string  |  The ID of the textarea. Defaults to the value of `name`.   |  
| name  | string  |  **Required.** The name of the textarea, which is submitted with the form data.   |  
| rows  | string  |  Optional number of textarea rows (default is 5 rows).   |  
| value  | string  |  Optional initial value of the textarea.   |  
| maxlength  | string  |  **Required.** If `maxwords` is set, this is not required. The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| maxwords  | string  |  **Required.** If `maxlength` is set, this is not required. The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.   |  
| threshold  | string  |  The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.   |  
| label  | object  |  **Required.** The label used by the character count component. [ See macro options for label](./components/character-count/#options-error-character-count-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the character count component. [ See macro options for hint](./components/character-count/#options-error-character-count-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the character count component. [ See macro options for formGroup](./components/character-count/#options-error-character-count-example--form-group.md).   |  
| classes  | string  |  Classes to add to the textarea.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the textarea.   |  
| spellcheck  | boolean  |  Optional field to enable or disable the `spellcheck` attribute on the character count.   |  
| countMessage  | object  |  Additional options for the count message used by the character count component. [ See macro options for countMessage](./components/character-count/#options-error-character-count-example--count-message.md).   |  
| textareaDescriptionText  | string  |  Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page when JavaScript is unavailable. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` parameter.   |  
| charactersUnderLimitText  | object  |  Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| charactersAtLimitText  | string  |  Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.   |  
| charactersOverLimitText  | object  |  Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum.[Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsUnderLimitText  | object  |  Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
| wordsAtLimitText  | string  |  Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.   |  
| wordsOverLimitText  | object  |  Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of characters above the maximum. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the textarea used by the character count component. [ See macro options for formGroup beforeInput](./components/character-count/#options-error-character-count-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the textarea used by the character count component. [ See macro options for formGroup afterInput](./components/character-count/#options-error-character-count-example--form-group-after-input.md).   |  
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
Options for `countMessage` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the count message.   |  
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
{% from "govuk/components/character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  id: "exceeding-characters",
  name: "exceeding",
  maxlength: 350,
  value: "A content designer works on the end-to-end journey of a service to help users complete their goal and government deliver a policy intent. Their work may involve the creation of, or change to, a transaction, product or single piece of content that stretches across digital and offline channels. They make sure appropriate content is shown to a user in the right place and in the best format.",
  label: {
    text: "Enter a job description",
    classes: "govuk-label--l",
    isPageHeading: true
  },
  errorMessage: {
    text: "Job description must be 350 characters or less"
  }
}) }}
```

If a user tries to send their response with too many characters, you must show an error message above the field as well as the count message below it.
The error message tells users what went wrong and how to fix it. The count message provides live feedback and updates as a user types.
The input shows a red border only when the user tries to enter more than the character limit. If the number of characters is within the limit, the input does not show this border even when there’s been an error. We felt it might cause the user difficulty if the border disappeared once they started typing.
Make sure errors follow GOV.UK guidance on [writing error messages](./components/error-message/#be-clear-and-concise.md) and have specific error messages for specific error states.
#### If the input is empty
Say ‘Enter [whatever it is]’.  
  
For example, ‘Enter a summary’.
#### If the input is too long
Say ‘[whatever it is] must be [number] characters or less’.  
  
For example, ‘Summary must be 400 characters or less’.
## Research on this component
In 2017, the Government Digital Service (GDS) [developed and tested this component](https://github.com/alphagov/govuk-design-system/wiki/Character-count-testing-and-user-research) in a prototype of the ‘Apply for a temporary event notice’ service. During this research, the component was tested with 17 users, including those with low digital skills and users with disabilities.
In 2022, the GOV.UK Design System team [updated the component to make it more accessible](https://github.com/alphagov/govuk-design-system-backlog/issues/67#issuecomment-1131719459), stopping the character count being announced twice by some screenreaders.
### Known issues and gaps
In Internet Explorer 11, JAWS will ignore any set threshold and announce the character count, even if the user entered less than the threshold.
In Chrome version 99, JAWS will not announce the hint or character count of a pre-populated textarea. This is a [known issue for the developer of JAWS](https://github.com/FreedomScientific/VFO-standards-support/issues/201).
Also, this component [counts some characters as multiple characters](https://github.com/alphagov/govuk-frontend/issues/1104). For example, emojis and some non-Latin characters.
### Services using this component
The component is used in a number of services, including the following.
**Department for Education**  
  
Publish teacher training courses
**Government Digital Service**  
  
Content publisher application
### Next steps
More user research is needed to find out:
  * how to decide between a character limit and a word limit
  * if highlighting characters over the limit in red would be helpful for users
  * how the component might work with lower as well as upper limits
  * if enabling a character count on text inputs would be useful

If you’ve used this component, get in touch to share your user research findings.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Character count’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/67) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/character-count/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/character-count/#top.md)
