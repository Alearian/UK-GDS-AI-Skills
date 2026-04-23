#  File upload 
This guidance is for government teams that build online services. [To find information and services for the public, go to GOV.UK](https://www.gov.uk/).
Help users select and upload a file.
[ Open this example in a new tab: file upload ](./components/file-upload/default.md)
  * [HTML](./components/file-upload/#file-upload-example-html.md)
  * [Nunjucks](./components/file-upload/#file-upload-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="file-upload-1">
    Upload a file
  </label>
  <input class="govuk-file-upload" id="file-upload-1" name="fileUpload1" type="file">
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
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| disabled  | boolean  |  If `true`, file input will be disabled.   |  
| multiple  | boolean  |  If `true`, a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the file upload component. [ See macro options for label](./components/file-upload/#options-file-upload-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the file upload component. [ See macro options for hint](./components/file-upload/#options-file-upload-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the file upload component. [ See macro options for formGroup](./components/file-upload/#options-file-upload-example--form-group.md).   |  
| javascript  | boolean  |  Can be used to enable JavaScript enhancements for the component.   |  
| chooseFilesButtonText  | string  |  The text of the button that opens the file picker. Default is `"Choose file"`. If `javascript` is not provided, this option will be ignored.   |  
| dropInstructionText  | string  |  The text informing users they can drop files. Default is `"or drop file"`. If `javascript` is not provided, this option will be ignored.   |  
| multipleFilesChosenText  | object  |  The text displayed when multiple files have been chosen by the user. The component will replace the `%{count}` placeholder with the number of files selected. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules). If `javascript` is not provided, this option will be ignored.   |  
| noFileChosenText  | string  |  The text displayed when no file has been chosen by the user. Default is `"No file chosen"`. If `javascript` is not provided, this option will be ignored.   |  
| enteredDropZoneText  | string  |  The text announced by assistive technology when user drags files and enters the drop zone. Default is `"Entered drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| leftDropZoneText  | string  |  The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is `"Left drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| classes  | string  |  Classes to add to the file upload component.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the file upload component.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the file upload component. [ See macro options for formGroup beforeInput](./components/file-upload/#options-file-upload-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the file upload component. [ See macro options for formGroup afterInput](./components/file-upload/#options-file-upload-example--form-group-after-input.md).   |  
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
{% from "govuk/components/file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  id: "file-upload-1",
  name: "fileUpload1",
  label: {
    text: "Upload a file"
  }
}) }}
```

## When to use this component
You should only ask users to upload something if it’s critical to the delivery of your service.
We improved the component in March 2025, so you’ll need to enable the [improved File upload component](./components/file-upload/#using-the-improved-file-upload-component.md) as a new feature.
Read a blog post about [design tips for helping users upload things](https://designnotes.blog.gov.uk/2017/02/14/some-design-tips-for-uploading-things/).
## How it works
To upload a file, the user can either:
  * use the ‘Choose file’ button
  * drag and drop a file into the file upload input area

### Let users reuse uploaded files
Make sure users can easily reuse a previously uploaded file within a single journey, unless doing so would be a major security or privacy concern.
For example, a user might need to upload a photo of their driving licence to prove their identity, and again to prove their address.
You can make it easier for the user to reuse a file by showing it as an option for the user to select so they do not need to upload it again. Consider users on public devices before choosing to make the file available to preview or download.
There are 2 ways to use the file upload component. You can use HTML or, if you’re using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: file upload second ](./components/file-upload/default.md)
  * [HTML](./components/file-upload/#file-upload-second-example-html.md)
  * [Nunjucks](./components/file-upload/#file-upload-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="file-upload-1">
    Upload a file
  </label>
  <input class="govuk-file-upload" id="file-upload-1" name="fileUpload1" type="file">
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
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| disabled  | boolean  |  If `true`, file input will be disabled.   |  
| multiple  | boolean  |  If `true`, a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the file upload component. [ See macro options for label](./components/file-upload/#options-file-upload-second-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the file upload component. [ See macro options for hint](./components/file-upload/#options-file-upload-second-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the file upload component. [ See macro options for formGroup](./components/file-upload/#options-file-upload-second-example--form-group.md).   |  
| javascript  | boolean  |  Can be used to enable JavaScript enhancements for the component.   |  
| chooseFilesButtonText  | string  |  The text of the button that opens the file picker. Default is `"Choose file"`. If `javascript` is not provided, this option will be ignored.   |  
| dropInstructionText  | string  |  The text informing users they can drop files. Default is `"or drop file"`. If `javascript` is not provided, this option will be ignored.   |  
| multipleFilesChosenText  | object  |  The text displayed when multiple files have been chosen by the user. The component will replace the `%{count}` placeholder with the number of files selected. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules). If `javascript` is not provided, this option will be ignored.   |  
| noFileChosenText  | string  |  The text displayed when no file has been chosen by the user. Default is `"No file chosen"`. If `javascript` is not provided, this option will be ignored.   |  
| enteredDropZoneText  | string  |  The text announced by assistive technology when user drags files and enters the drop zone. Default is `"Entered drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| leftDropZoneText  | string  |  The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is `"Left drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| classes  | string  |  Classes to add to the file upload component.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the file upload component.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the file upload component. [ See macro options for formGroup beforeInput](./components/file-upload/#options-file-upload-second-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the file upload component. [ See macro options for formGroup afterInput](./components/file-upload/#options-file-upload-second-example--form-group-after-input.md).   |  
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
{% from "govuk/components/file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  id: "file-upload-1",
  name: "fileUpload1",
  label: {
    text: "Upload a file"
  }
}) }}
```

### Error messages
Error messages should be styled like this:
[ Open this example in a new tab: error – file upload ](./components/file-upload/error.md)
  * [HTML](./components/file-upload/#error-file-upload-example-html.md)
  * [Nunjucks](./components/file-upload/#error-file-upload-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <label class="govuk-label" for="file-upload-1">
    Upload a file
  </label>
  <p id="file-upload-1-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> The CSV must be smaller than 2MB
  </p>
  <input class="govuk-file-upload govuk-file-upload--error" id="file-upload-1" name="fileUpload1" type="file" aria-describedby="file-upload-1-error">
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
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| disabled  | boolean  |  If `true`, file input will be disabled.   |  
| multiple  | boolean  |  If `true`, a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the file upload component. [ See macro options for label](./components/file-upload/#options-error-file-upload-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the file upload component. [ See macro options for hint](./components/file-upload/#options-error-file-upload-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the file upload component. [ See macro options for formGroup](./components/file-upload/#options-error-file-upload-example--form-group.md).   |  
| javascript  | boolean  |  Can be used to enable JavaScript enhancements for the component.   |  
| chooseFilesButtonText  | string  |  The text of the button that opens the file picker. Default is `"Choose file"`. If `javascript` is not provided, this option will be ignored.   |  
| dropInstructionText  | string  |  The text informing users they can drop files. Default is `"or drop file"`. If `javascript` is not provided, this option will be ignored.   |  
| multipleFilesChosenText  | object  |  The text displayed when multiple files have been chosen by the user. The component will replace the `%{count}` placeholder with the number of files selected. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules). If `javascript` is not provided, this option will be ignored.   |  
| noFileChosenText  | string  |  The text displayed when no file has been chosen by the user. Default is `"No file chosen"`. If `javascript` is not provided, this option will be ignored.   |  
| enteredDropZoneText  | string  |  The text announced by assistive technology when user drags files and enters the drop zone. Default is `"Entered drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| leftDropZoneText  | string  |  The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is `"Left drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| classes  | string  |  Classes to add to the file upload component.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the file upload component.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the file upload component. [ See macro options for formGroup beforeInput](./components/file-upload/#options-error-file-upload-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the file upload component. [ See macro options for formGroup afterInput](./components/file-upload/#options-error-file-upload-example--form-group-after-input.md).   |  
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
{% from "govuk/components/file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  id: "file-upload-1",
  name: "fileUpload1",
  label: {
    text: "Upload a file"
  },
  errorMessage: {
    text: "The CSV must be smaller than 2MB"
  }
}) }}
```

Make sure errors follow the guidance in the [Error message component](./components/error-message.md) and have specific error messages for specific error states.
#### If no file has been selected
Say ‘Select a [whatever they need to select]’.  
  
For example, ‘Select a report’.
#### If the file is the wrong file type
Say ‘The selected file must be a [list of file types]’.  
  
For example, ‘The selected file must be a CSV or ODS’ or ‘The selected file must be a JPG, BMP, PNG, TIF or PDF’.
#### If the file is too big
Say ‘The selected file must be smaller than [largest file size]’.  
  
For example, ‘The selected file must be smaller than 2MB’.
#### If the file is empty
Say ‘The selected file is empty’.
#### If the file contains a virus
Say ‘The selected file contains a virus’.
#### If the file is password protected
Say ‘The selected file is password protected’.
#### If there was a problem and the file was not uploaded
Say ‘The selected file could not be uploaded – try again’.
#### If there is a limit on how many files the user can select
Say ‘You can only select up to [highest number] files at the same time’.  
  
For example, ‘You can only select up to 10 files at the same time’.
#### If the file is not in a template that must be used or the template has been changed
Say ‘The selected file must use the template’.
## Using the improved File upload component
In March 2025, we introduced changes to the File upload component that service teams can opt in to as part of GOV.UK Frontend 5.9.0.
The improved component is intended to:
  * fix accessibility issues
  * improve the user experience
  * allow text in the component to be translated

We recommend service teams start using the latest component to improve the experience for users. However, it’s a visual change from the previous component and might affect existing designs and layouts.
To let teams migrate at their own pace, the improvements are only enabled if you use the `javascript` macro option or extra markup in your HTML.
This example shows you how to enable the improved File upload component:
[ Open this example in a new tab: enhanced - file upload ](./components/file-upload/enhanced.md)
  * [HTML](./components/file-upload/#enhanced-file-upload-example-html.md)
  * [Nunjucks](./components/file-upload/#enhanced-file-upload-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="file-upload-1">
    Upload a file
  </label>
  <div
    class="govuk-drop-zone"
    data-module="govuk-file-upload">
    <input class="govuk-file-upload" id="file-upload-1" name="fileUpload1" type="file">
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
| name  | string  |  **Required.** The name of the input, which is submitted with the form data.   |  
| id  | string  |  The ID of the input. Defaults to the value of `name`.   |  
| disabled  | boolean  |  If `true`, file input will be disabled.   |  
| multiple  | boolean  |  If `true`, a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the file upload component. [ See macro options for label](./components/file-upload/#options-enhanced-file-upload-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to the file upload component. [ See macro options for hint](./components/file-upload/#options-enhanced-file-upload-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the file upload component. [ See macro options for formGroup](./components/file-upload/#options-enhanced-file-upload-example--form-group.md).   |  
| javascript  | boolean  |  Can be used to enable JavaScript enhancements for the component.   |  
| chooseFilesButtonText  | string  |  The text of the button that opens the file picker. Default is `"Choose file"`. If `javascript` is not provided, this option will be ignored.   |  
| dropInstructionText  | string  |  The text informing users they can drop files. Default is `"or drop file"`. If `javascript` is not provided, this option will be ignored.   |  
| multipleFilesChosenText  | object  |  The text displayed when multiple files have been chosen by the user. The component will replace the `%{count}` placeholder with the number of files selected. [Our pluralisation rules apply to this macro option](https://frontend.design-system.service.gov.uk/localise-govuk-frontend/#understanding-pluralisation-rules). If `javascript` is not provided, this option will be ignored.   |  
| noFileChosenText  | string  |  The text displayed when no file has been chosen by the user. Default is `"No file chosen"`. If `javascript` is not provided, this option will be ignored.   |  
| enteredDropZoneText  | string  |  The text announced by assistive technology when user drags files and enters the drop zone. Default is `"Entered drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| leftDropZoneText  | string  |  The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is `"Left drop zone"`. If `javascript` is not provided, this option will be ignored.   |  
| classes  | string  |  Classes to add to the file upload component.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the file upload component.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the file upload component. [ See macro options for formGroup beforeInput](./components/file-upload/#options-enhanced-file-upload-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the file upload component. [ See macro options for formGroup afterInput](./components/file-upload/#options-enhanced-file-upload-example--form-group-after-input.md).   |  
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
{% from "govuk/components/file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  id: "file-upload-1",
  name: "fileUpload1",
  label: {
    text: "Upload a file"
  },
  javascript: true
}) }}
```

### Changes in the improved component
To make it easier for users to drag and drop files, we’ve made the drop zone:
  * bigger
  * visible at all times
  * more visually responsive to user interactions

We’ve also changed the ‘Choose file’ button to be more consistent with the secondary button in the [Button component](./components/button.md).
Service teams can change the text on the button and in the ‘No file chosen’ message. We decided to make this text changeable for translation purposes and to let teams be specific about the file to upload. However, teams should aim to keep the text as short as possible for accessibility purposes. For example, screen reader users might find it difficult to use the component if the text is too long.
All the text in the component can now be translated to match the language of the page content when JavaScript is running.
#### Improvements for assistive technology users
Users of Dragon, a speech recognition tool, [cannot activate their browser’s native file inputs](https://github.com/alphagov/govuk-frontend/issues/3686) by using commands for interacting with [web page controls](https://www.nuance.com/products/help/dragon/dragon-for-pc/enx/professionalgroup/main/Content/Web/working_with_chrome.htm?Highlight=click%20button). They have to rely on [mouse commands](https://www.nuance.com/products/help/dragon/dragon-for-pc/enx/professionalgroup/main/Content/CommandandControl/using_your_mouse.htm) or [keyboard commands](https://www.nuance.com/products/help/dragon/dragon-for-pc/enx/professionalgroup/main/Content/CommandandControl/using_your_keyboard.htm), which take multiple steps to activate the component.
With the improved File upload component, users can say commands for interacting with web page controls to choose files.
However, due to [browser security features](https://developer.mozilla.org/en-US/docs/Web/Security/User_activation), this may not work right away or on subsequent interactions on the same page. If users cannot interact with the component, they’ll first need to perform another action, such as a mouse click.
## Research on this component
### Colour and ‘interaction state’ updates from the GOV.UK brand refresh
In February 2026, we updated the improved File upload component.
As part of colour changes to the GOV.UK brand, we improved the various ‘states’ that show as the user interacts with the component. For example, we’ve made it easier for users to see when they’ve added a file.
We’ve also updated the colours to make user interaction more consistent and less distracting than before.
### Known issues and gaps
The earlier version of the File upload component does not show a visual target area when dragging and dropping a file. The component inherits and uses the browser’s default behaviour. More detail on the findings can be found in the [GitHub issue: ‘Upload file component has no visual target area when dragging and dropping a file’](https://github.com/alphagov/govuk-frontend/issues/3685).
We revisited this issue in March 2025 and have published an improved File upload component to improve accessibility. Although we’re confident the new component is an improvement on the browser’s default behaviour, teams can continue to use the existing component until the next major release, when the new version will be enabled by default.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘File upload’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/49) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/file-upload/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/file-upload/#top.md)
