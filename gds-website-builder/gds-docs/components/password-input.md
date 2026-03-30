#  Password input 
Help users to create and enter passwords.
[ Open this example in a new tab: password input ](./components/password-input/default.md)
  * [HTML](./components/password-input/#password-input-example-html.md)
  * [Nunjucks](./components/password-input/#password-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-password-input" data-module="govuk-password-input">
  <label class="govuk-label" for="password-input">
    Password
  </label>
  <div class="govuk-input__wrapper govuk-password-input__wrapper">
    <input class="govuk-input govuk-password-input__input govuk-js-password-input-input" id="password-input" name="password" type="password" spellcheck="false" autocomplete="current-password" autocapitalize="none">
    <button type="button" class="govuk-button govuk-button--secondary govuk-password-input__toggle govuk-js-password-input-toggle" data-module="govuk-button" aria-controls="password-input" aria-label="Show password" hidden>
      Show
    </button>
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
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/password-input/#options-password-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/password-input/#options-password-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/password-input/#options-password-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html). See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) for full list of attributes that can be used. Default is `"current-password"`.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
| showPasswordText  | string  |  Button text when the password is hidden. Defaults to `"Show"`.   |  
| hidePasswordText  | string  |  Button text when the password is visible. Defaults to `"Hide"`.   |  
| showPasswordAriaLabelText  | string  |  Button text exposed to assistive technologies, like screen readers, when the password is hidden. Defaults to `"Show password"`.   |  
| hidePasswordAriaLabelText  | string  |  Button text exposed to assistive technologies, like screen readers, when the password is visible. Defaults to `"Hide password"`.   |  
| passwordShownAnnouncementText  | string  |  Announcement made to screen reader users when their password has become visible in plain text. Defaults to `"Your password is visible"`.   |  
| passwordHiddenAnnouncementText  | string  |  Announcement made to screen reader users when their password has been obscured and is not visible. Defaults to `"Your password is hidden"`.   |  
| button  | object  |  Optional object allowing customisation of the toggle button. [ See macro options for button](./components/password-input/#options-password-input-example--button.md).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/password-input/#options-password-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/password-input/#options-password-input-example--form-group-after-input.md).   |  
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
Options for `button` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the button.   |  
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
{% from "govuk/components/password-input/macro.njk" import govukPasswordInput %}

{{ govukPasswordInput({
  label: {
    text: "Password"
  },
  id: "password-input",
  name: "password"
}) }}
```

## When to use this component
Use this component whenever you need users to create or enter a password.
Before using this component, you should also read the guidance on the [Ask users for passwords pattern](./patterns/passwords.md) and [Creating user accounts pattern](./patterns/create-accounts.md).
## When not to use this component
Do not use this component to ask for any information other than a password.
Use a [Text input component](./components/text-input.md) to ask for other security information, such as:
  * multi-factor authentication codes
  * answers to security questions
  * other personally identifiable information

Also see the [Confirm a phone number pattern](./patterns/confirm-a-phone-number.md).
## How it works
This component allows users to enter a password, with an option to show what they’ve entered as plain text.
This allows users to visually check their password before they submit it, which helps them reduce errors and choose passwords that are more unique and secure.
### Error messages
[ Open this example in a new tab: password input with errors – password input ](./components/password-input/error.md)
  * [HTML](./components/password-input/#password-input-with-errors-password-input-example-html.md)
  * [Nunjucks](./components/password-input/#password-input-with-errors-password-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error govuk-password-input" data-module="govuk-password-input">
  <label class="govuk-label" for="password-input-with-error-message">
    Password
  </label>
  <p id="password-input-with-error-message-error" class="govuk-error-message">
    <span class="govuk-visually-hidden">Error:</span> Enter a password
  </p>
  <div class="govuk-input__wrapper govuk-password-input__wrapper">
    <input class="govuk-input govuk-password-input__input govuk-js-password-input-input govuk-input--error" id="password-input-with-error-message" name="password-input-with-error-message" type="password" spellcheck="false" aria-describedby="password-input-with-error-message-error" autocomplete="current-password" autocapitalize="none">
    <button type="button" class="govuk-button govuk-button--secondary govuk-password-input__toggle govuk-js-password-input-toggle" data-module="govuk-button" aria-controls="password-input-with-error-message" aria-label="Show password" hidden>
      Show
    </button>
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
| value  | string  |  Optional initial value of the input.   |  
| disabled  | boolean  |  If `true`, input will be disabled.   |  
| describedBy  | string  |  One or more element IDs to add to the `aria-describedby` attribute, used to provide additional descriptive information for screenreader users.   |  
| label  | object  |  **Required.** The label used by the text input component. [ See macro options for label](./components/password-input/#options-password-input-with-errors-password-input-example--label.md).   |  
| hint  | object  |  Can be used to add a hint to a text input component. [ See macro options for hint](./components/password-input/#options-password-input-with-errors-password-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the text input component. [ See macro options for formGroup](./components/password-input/#options-password-input-with-errors-password-input-example--form-group.md).   |  
| classes  | string  |  Classes to add to the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html). See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) for full list of attributes that can be used. Default is `"current-password"`.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the input.   |  
| showPasswordText  | string  |  Button text when the password is hidden. Defaults to `"Show"`.   |  
| hidePasswordText  | string  |  Button text when the password is visible. Defaults to `"Hide"`.   |  
| showPasswordAriaLabelText  | string  |  Button text exposed to assistive technologies, like screen readers, when the password is hidden. Defaults to `"Show password"`.   |  
| hidePasswordAriaLabelText  | string  |  Button text exposed to assistive technologies, like screen readers, when the password is visible. Defaults to `"Hide password"`.   |  
| passwordShownAnnouncementText  | string  |  Announcement made to screen reader users when their password has become visible in plain text. Defaults to `"Your password is visible"`.   |  
| passwordHiddenAnnouncementText  | string  |  Announcement made to screen reader users when their password has been obscured and is not visible. Defaults to `"Your password is hidden"`.   |  
| button  | object  |  Optional object allowing customisation of the toggle button. [ See macro options for button](./components/password-input/#options-password-input-with-errors-password-input-example--button.md).   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInput  | object  |  Content to add before the input used by the text input component. [ See macro options for formGroup beforeInput](./components/password-input/#options-password-input-with-errors-password-input-example--form-group-before-input.md).   |  
| afterInput  | object  |  Content to add after the input used by the text input component. [ See macro options for formGroup afterInput](./components/password-input/#options-password-input-with-errors-password-input-example--form-group-after-input.md).   |  
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
Options for `button` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the button.   |  
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
{% from "govuk/components/password-input/macro.njk" import govukPasswordInput %}

{{ govukPasswordInput({
  label: {
    text: "Password"
  },
  id: "password-input-with-error-message",
  name: "password-input-with-error-message",
  errorMessage: {
    text: "Enter a password"
  }
}) }}
```

If the user enters their account details incorrectly, do not reveal whether they got the username or password wrong. Clear any information entered into the password input.
Revealing the source of the error can help fraudsters break into people’s accounts.
See how to handle incorrect login attempts and help users who forget their password in the [Ask users for passwords pattern](./patterns/passwords.md).
### Showing and hiding passwords
Hide passwords by default until the user chooses to show it using the ‘show’ button. Users might not be in a private space when entering or creating a password, so you should hide passwords by default.
If you do choose to include two or more password inputs on a page, the ‘show’ and ‘hide’ toggles and labels for each password input must be different.
For example, you can label:
  * the first input as ‘Password’ with a toggle of ‘show password’
  * the second input as ‘Re-enter password’ with a toggle of ‘show re-entered password’

### Avoid adding a ‘confirm password’ field
It’s not necessary to add a second password field, also known as a ‘confirm password’ field, particularly as this component allows users to show and hide passwords.
See [Research on this component](./components/password-input/#research-on-this-component.md) and why we decided having a second field is not helpful for users.
### Define the input’s type as ‘password’
When the form is submitted, the password input should automatically change its `type` to `password`, if it has not already done so.
This is to prevent browsers from remembering it as a previously-provided value and potentially displaying it as an autofill option on non-password inputs.
### Use the autocomplete attribute
Use the `autocomplete` attribute on password inputs to help users complete forms faster.
`Autocomplete` indicates to browsers and password managers what kind of password is needed so it can be entered for the user.
Set the `autocomplete` attribute to `new-password` if the user is creating a password. Otherwise, use `current-password`.
Many browsers will autofill password inputs, even when the `autocomplete` attribute is missing or set to `off`.
### Allow copy and paste
Always allow users to copy and paste in password fields. People may have very good reasons why they want to do this, for example if they’re using a password manager.
#### Copying text from password fields
Users can copy any text from a password field when it’s set on ‘show’ – this is a feature of browser behaviour and cannot be overridden.
This can be useful for users, such as to save a password that the browser has suggested into a separate password manager.
### Avoid restricting the user’s input
See the [Ask users for passwords pattern](./patterns/passwords.md) to see how to help users choose strong passwords.
Support all the characters users may need to enter a password, including numbers and symbols.
If you must place password restrictions on users, such as for technical or security reasons, be clear and consistent.
Any restrictions must be identical wherever the user creates or enters a password. If you change the restrictions over time, you must continue to support existing user passwords or ask them to set a new one.
#### Do not use maxlength to restrict password length
Users will not get any feedback when they’ve reached the `maxlength` and their text input has been truncated. This happens when a user has pasted text from elsewhere or it’s been autofilled by a password manager.
If you must restrict the length of a password, show an error message instead using the [Validation pattern](./patterns/validation.md).
### Do not spellcheck or autocapitalise the user’s input
Some browsers might automatically change what the user is typing when the input’s text is visible, such as correcting spelling or automatically turning on upper case letters at the start of sentences.
You can tell browsers not to correct spellings by setting the `spellcheck` attribute to `false`.
Doing this can [avoid making your service vulnerable to ‘spell-jacking’](https://www.itpro.com/security/vulnerability/370010/what-is-spell-jacking), where security researchers have found some spell checking tools gathering personal identifiable information, even user’s passwords, from password input fields to send to third party services.
You can tell browsers not to autocapitalise values by setting the `autocapitalize` attribute to `off`.
### Known issues
Some apps and tools will add their own native functionality to show and hide passwords.
These tools include:
  * browsers (particularly when suggesting new passwords)
  * password managers
  * screen readers

We’ve tried to minimise duplicate functionality by hiding other types of ‘show password’ buttons where possible.
There’s also other instances where a password could be ‘shown’ or ‘hidden’ without the use of a button – causing a mismatch with the button label (in other words, the user would see a button to ‘show’ a password that’s already visible).
[We found this mismatch happens in some browsers](https://github.com/alphagov/govuk-design-system/issues/3552#issuecomment-1976660248) when:
  * a keyboard shortcut is pressed
  * a suggested password is created

## Research on this component
We [decided that having a second field is not helpful for users](https://github.com/alphagov/govuk-design-system-backlog/issues/240#issuecomment-2020125340), particularly on password inputs with show and hide buttons.
However, we’d like to better support our rationale with real life examples from service teams and get your feedback.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Password input’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/240) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/password-input/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/password-input/#top.md)
