#  [](./v5/javascript-api-reference/#javascript-api-reference.md)JavaScript API Reference
Some of our components can be passed JavaScript configuration objects. You can do it both:
  * [when configuring instances of specific components](./v5/configure-components/#configure-instances-of-specific-components-using-the-createall-function.md)
  * [when configuring all components using the `initAll` function](./v5/configure-components/#configure-all-components-using-the-initall-function.md)

This page lists the options available for the following components:
  * [Accordion](./v5/javascript-api-reference/#accordion.md)
  * [Button](./v5/javascript-api-reference/#button.md)
  * [CharacterCount](./v5/javascript-api-reference/#charactercount.md)
  * [ErrorSummary](./v5/javascript-api-reference/#errorsummary.md)
  * [ExitThisPage](./v5/javascript-api-reference/#exitthispage.md)
  * [FileUpload](./v5/javascript-api-reference/#fileupload.md)
  * [NotificationBanner](./v5/javascript-api-reference/#notificationbanner.md)
  * [PasswordInput](./v5/javascript-api-reference/#passwordinput.md)

##  [](./v5/javascript-api-reference/#accordion.md)Accordion
###  [](./v5/javascript-api-reference/#i18n.md)i18n
Type: object
Messages the component uses for the labels of its buttons. This includes the visible text shown on screen, and text to help assistive technology users for the buttons toggling each section.
Default: see properties
####  [](./v5/javascript-api-reference/#properties.md)Properties
#####  [](./v5/javascript-api-reference/#hideallsections.md)hideAllSections
Type: string
The text content for the ‘Hide all sections’ button, used when at least one section is expanded.
Default:

```
'Hide all sections'

```

#####  [](./v5/javascript-api-reference/#hidesection.md)hideSection
Type: string
The text content for the ‘Hide’ button, used when a section is expanded.
Default:

```
'Hide'

```

#####  [](./v5/javascript-api-reference/#hidesectionarialabel.md)hideSectionAriaLabel
Type: string
The text content appended to the ‘Hide’ button’s accessible name when a section is expanded.
Default:

```
'Hide this section'

```

#####  [](./v5/javascript-api-reference/#showallsections.md)showAllSections
Type: string
The text content for the ‘Show all sections’ button, used when all sections are collapsed.
Default:

```
'Show all sections'

```

#####  [](./v5/javascript-api-reference/#showsection.md)showSection
Type: string
The text content for the ‘Show’ button, used when a section is collapsed.
Default:

```
'Show'

```

#####  [](./v5/javascript-api-reference/#showsectionarialabel.md)showSectionAriaLabel
Type: string
The text content appended to the ‘Show’ button’s accessible name when a section is expanded.
Default:

```
'Show this section'

```

###  [](./v5/javascript-api-reference/#rememberexpanded.md)rememberExpanded
Type: boolean
Whether the expanded and collapsed state of each section is remembered and restored when navigating
##  [](./v5/javascript-api-reference/#button.md)Button
###  [](./v5/javascript-api-reference/#preventdoubleclick.md)preventDoubleClick
Type: boolean
Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Default:

```
false

```

##  [](./v5/javascript-api-reference/#charactercount.md)CharacterCount
###  [](./v5/javascript-api-reference/#maxlength.md)maxlength
Type: number
The maximum number of characters. If `maxwords` is provided, the `maxlength` option will be ignored.
###  [](./v5/javascript-api-reference/#maxwords.md)maxwords
Type: number
The maximum number of words. If `maxwords` is provided, the `maxlength` option will be ignored.
###  [](./v5/javascript-api-reference/#threshold.md)threshold
Type: number
The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.
Default:

```
0

```

###  [](./v5/javascript-api-reference/#charactercount-i18n.md)i18n
Type: object
Messages shown to users as they type. It provides feedback on how many words or characters they have remaining or if they are over the limit. This also includes a message used as an accessible description for the textarea.
Default: see properties
####  [](./v5/javascript-api-reference/#charactercount-i18n-properties.md)Properties
#####  [](./v5/javascript-api-reference/#charactersunderlimit.md)charactersUnderLimit
Type: object
Message displayed when the number of characters is under the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. This is a [pluralised list of messages](./v5/localise-govuk-frontend/#understanding-pluralisation-rules.md).
Default:

```
{
  one: 'You have %{count} character remaining',
  other: 'You have %{count} characters remaining'
}

```

#####  [](./v5/javascript-api-reference/#charactersatlimit.md)charactersAtLimit
Type: string
Message displayed when the number of characters reaches the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies.
Default:

```
'You have 0 characters remaining'

```

#####  [](./v5/javascript-api-reference/#charactersoverlimit.md)charactersOverLimit
Type: object
Message displayed when the number of characters is over the configured maximum, `maxlength`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining characters. This is a [pluralised list of messages](./v5/localise-govuk-frontend/#understanding-pluralisation-rules.md).
Default:

```
{
  one: 'You have %{count} character too many',
  other: 'You have %{count} characters too many'
}

```

#####  [](./v5/javascript-api-reference/#wordsunderlimit.md)wordsUnderLimit
Type: object
Message displayed when the number of words is under the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. This is a [pluralised list of messages](./v5/localise-govuk-frontend/#understanding-pluralisation-rules.md).
Default:

```
{
  one: 'You have %{count} word remaining',
  other: 'You have %{count} words remaining'
}

```

#####  [](./v5/javascript-api-reference/#wordsatlimit.md)wordsAtLimit
Type: string
Message displayed when the number of words reaches the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies.
Default:

```
'You have 0 words remaining'

```

#####  [](./v5/javascript-api-reference/#wordsoverlimit.md)wordsOverLimit
Type: object
Message displayed when the number of words is over the configured maximum, `maxwords`. This message is displayed visually and through assistive technologies. The component will replace the `%{count}` placeholder with the number of remaining words. This is a [pluralised list of messages](./v5/localise-govuk-frontend/#understanding-pluralisation-rules.md).
Default:

```
{
  one: 'You have %{count} word too many',
  other: 'You have %{count} words too many'
}

```

#####  [](./v5/javascript-api-reference/#textareadescription.md)textareaDescription
Type: object
Message made available to assistive technologies, if none is already present in the HTML, to describe that the component accepts only a limited amount of content. The component will replace the `%{count}` placeholder with the value of the `maxlength` or `maxwords` option.
Default:

```
{
  other: ''
}

```

##  [](./v5/javascript-api-reference/#errorsummary.md)ErrorSummary
###  [](./v5/javascript-api-reference/#disableautofocus.md)disableAutoFocus
If set to `true` the error summary will not be focussed when the page loads.
Type: boolean
Default

```
false

```

##  [](./v5/javascript-api-reference/#exitthispage.md)ExitThisPage
###  [](./v5/javascript-api-reference/#exitthispage-i18n.md)i18n
Type: object
Messages the component uses for screen reader announcements relating to the keyboard shortcut functionality, informing assistive technology users of the current state of the shortcut.
All of these strings should be short and in plain text.
Default: see properties
####  [](./v5/javascript-api-reference/#exitthispage-i18n-properties.md)Properties
#####  [](./v5/javascript-api-reference/#activated.md)activated
Type: string
Text to announce when the Exit This Page keyboard shortcut has been activated and the user is being directed away from the current page.
Default:

```
'Loading.'

```

#####  [](./v5/javascript-api-reference/#pressonemoretime.md)pressOneMoreTime
Type: string
Text to announce when the user has pressed the activation key (Shift) twice, and must press it one more time to activate the functionality.
Default:

```
'Shift, press 1 more time to exit.'

```

#####  [](./v5/javascript-api-reference/#presstwomoretimes.md)pressTwoMoreTimes
Type: string
Text to announce when the user has pressed the activation key (Shift) once, and must press it two more times to activate the functionality.
Default:

```
'Shift, press 2 more times to exit.'

```

#####  [](./v5/javascript-api-reference/#timedout.md)timedOut
Type: string
Text to announce if the user hasn’t completed the keyboard shortcut within the allowed time, so that the user is aware that they must begin the sequence again.
Default:

```
'Exit this page expired.'

```

##  [](./v5/javascript-api-reference/#fileupload.md)FileUpload
###  [](./v5/javascript-api-reference/#fileupload-i18n.md)i18n
Type: object
Messages the component uses for screen reader announcements relating to choosing and dropping files.
All of these strings should be short and in plain text.
####  [](./v5/javascript-api-reference/#fileupload-i18n-properties.md)Properties
#####  [](./v5/javascript-api-reference/#choosefilesbutton.md)chooseFilesButton
Type: string
The text of the button that opens the file picker.
Default:

```
  'Choose file'

```

#####  [](./v5/javascript-api-reference/#dropinstruction.md)dropInstruction
Type: string
The text informing users they can drop files.
Default:

```
  'or drop file'

```

#####  [](./v5/javascript-api-reference/#nofilechosen.md)noFileChosen
Type: string
The text to display when no file has been chosen by the user.
Default:

```
  'No file chosen'

```

#####  [](./v5/javascript-api-reference/#multiplefileschosen.md)multipleFilesChosen
Type: object
The text displayed when multiple files have been chosen by the user.
Default:

```
  {
    // the 'one' string isn't used as the component displays the filename
    // instead, however it's here for coverage's sake
    one: '%{count} file chosen',
    other: '%{count} files chosen'
  },

```

#####  [](./v5/javascript-api-reference/#entereddropzone.md)enteredDropZone
Type: string
The text announced by assistive technology when the user drags files and enters the drop zone
Default:

```
  'Entered drop zone'

```

#####  [](./v5/javascript-api-reference/#leftdropzone.md)leftDropZone
Type: string
The text announced by assistive technology when user drags files and leaves the drop zone without dropping
Default:

```
  'Left drop zone'

```

##  [](./v5/javascript-api-reference/#notificationbanner.md)NotificationBanner
###  [](./v5/javascript-api-reference/#notificationbanner-disableautofocus.md)disableAutoFocus
Type: boolean
If set to `true` the notification banner will not be focussed when the page loads. This only applies if the component has a `role` of `alert` – in other cases the component will not be focused on page load, regardless of this option.
Default:

```
false

```

##  [](./v5/javascript-api-reference/#passwordinput.md)PasswordInput
###  [](./v5/javascript-api-reference/#passwordinput-i18n.md)i18n
####  [](./v5/javascript-api-reference/#passwordinput-i18n-properties.md)Properties
#####  [](./v5/javascript-api-reference/#hidepassword.md)hidePassword
Type: string
Visible text of the button when the password is currently visible.
Default:

```
  'Hide'

```

#####  [](./v5/javascript-api-reference/#hidepasswordarialabel.md)hidePasswordAriaLabel
Type: string
aria-label of the button when the password is currently visible.
Default:

```
  'Hide password'

```

#####  [](./v5/javascript-api-reference/#passwordhiddenannouncement.md)passwordHiddenAnnouncement
Type: string
Screen reader announcement to make when the password has just been hidden.
Default:

```
  'Your password is hidden'

```

#####  [](./v5/javascript-api-reference/#passwordshownannouncement.md)passwordShownAnnouncement
Type: string
Screen reader announcement to make when the password has just become visible.
Default:

```
  'Your password is visible'

```

#####  [](./v5/javascript-api-reference/#showpassword.md)showPassword
Type: string
Visible text of the button when the password is currently hidden.
Default:

```
  'Show'

```

#####  [](./v5/javascript-api-reference/#showpasswordarialabel.md)showPasswordAriaLabel
Type: string
aria-label of the button when the password is currently hidden.
Default:

```
  'Show password'

```

  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v5/javascript-api-reference/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27JavaScript+API+Reference%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv5%2Fjavascript-api-reference%2F%29&labels=bug&title=Re%3A+%27JavaScript+API+Reference%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
