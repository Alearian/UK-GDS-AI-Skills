#  Notification banner 
Use a notification banner to tell the user about something they need to know about, but that’s not directly related to the page content.
[ Open this example in a new tab: notification banner ](./components/notification-banner/default.md)
  * [HTML](./components/notification-banner/#notification-banner-example-html.md)
  * [Nunjucks](./components/notification-banner/#notification-banner-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-notification-banner" role="region" aria-labelledby="govuk-notification-banner-title" data-module="govuk-notification-banner">
  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title" id="govuk-notification-banner-title">
      Important
    </h2>
  </div>
  <div class="govuk-notification-banner__content">
    <p class="govuk-notification-banner__heading">
      You have 7 days left to send your application.
      <a class="govuk-notification-banner__link" href="#">View application</a>.
    </p>
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
| text  | string  |  **Required.** The text that displays in the notification banner. You can use any string with this option. If you set `html`, this option is not required and is ignored.   |  
| html  | string  |  **Required.** The HTML to use within the notification banner. You can use any string with this option. If you set `html`, `text` is not required and is ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire notification banner component in a `call` block.   |  
| titleText  | string  |  The title text that displays in the notification banner. You can use any string with this option. Use this option to set text that does not contain HTML. The available default values are ‘Important’, ‘Success’, and null:
  * if you do not set `type`, `titleText` defaults to `"Important"`
  * if you set `type` to `success`, `titleText` defaults to `"Success"`
  * if you set `titleHtml`, this option is ignored

 |  
| titleHtml  | string  |  The title HTML to use within the notification banner. You can use any string with this option. Use this option to set text that contains HTML. If you set `titleHtml`, the `titleText` option is ignored.   |  
| titleHeadingLevel  | string  |  Sets heading level for the title only. You can only use values between `1` and `6` with this option. The default is `2`.   |  
| type  | string  |  The type of notification to render. You can use only `"success"` or `null` values with this option. If you set `type` to `"success"`, the notification banner sets `role` to `"alert"`. JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set `type`, the notification banner sets `role` to `"region"`.   |  
| role  | string  |  Overrides the value of the `role` attribute for the notification banner. Defaults to `"region"`. If you set `type` to `"success"`, `role` defaults to `"alert"`.   |  
| titleId  | string  |  The `id` for the banner title, and the `aria-labelledby` attribute in the banner. Defaults to `"govuk-notification-banner-title"`.   |  
| disableAutoFocus  | boolean  |  If you set `type` to `"success"`, or `role` to `"alert"`, JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set `disableAutoFocus` to `true`.   |  
| classes  | string  |  The classes that you want to add to the notification banner.   |  
| attributes  | object  |  The HTML attributes that you want to add to the notification banner, for example, data attributes.   |  
Copy code
```
{% from "govuk/components/notification-banner/macro.njk" import govukNotificationBanner %}

{% set html %}
  <p class="govuk-notification-banner__heading">
    You have 7 days left to send your application.
    <a class="govuk-notification-banner__link" href="#">View application</a>.
  </p>
{% endset %}

{{ govukNotificationBanner({
  html: html
}) }}
```

## When to use this component
A notification banner lets you tell the user about something that’s not directly relevant to the thing they’re trying to do on that page of the service. For example:
  * telling the user about a problem that’s affecting the service as a whole (for example, delays in processing applications because of an emergency)
  * telling the user about something that affects them in particular (for example, an approaching deadline they need to meet)
  * telling the user about the outcome of something they’ve just done on a previous page (for example, confirming that an email has been sent)

## When not to use this component
Use notification banners sparingly. There’s [evidence that people often miss them](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/), and using them too often is likely to make this problem worse.
If the information is directly relevant to the thing the user is doing on that page, put the information in the main page content instead. Use an [Inset text component](./components/inset-text.md) or [Warning text component](./components/warning-text.md) if it needs to stand out.
Do not:
  * use a notification banner to tell the user about validation errors - use an [Error message component](./components/error-message.md) and [Error summary component](./components/error-summary.md) instead
  * show a notification banner and an [Error summary component](./components/error-summary.md) on the same page - just show the error summary

## How it works
Position a notification banner immediately before the page `h1`. The notification banner should be the same width as the page’s other content, such as components, headings and body text. For example, if the other content takes up two-thirds of the screen on desktop devices, then the notification banner should also take up two-thirds. [Read about how to lay out pages](./styles/layout.md).
Use `role="region"` and `aria-labelledby="govuk-notification-banner-title"` (with `id="govuk-notification-banner-title"` on `<govuk-notification-banner__title>`) so that screen reader users can navigate to the notification banner.
Avoid showing more than one notification banner on the same page. Instead, combine the messages in a single notification banner. If the messages are too different to combine, only show the highest priority notification banner.
### Notification banner headings
You can use `<h3>` headings in the `govuk-notification-banner__content` to help structure your content.
Avoid using headings for single-line notifications that do not need them.
## Telling the user about a problem that affects the whole service
Use a ‘neutral’ blue notification banner if the user needs to know about a problem with the service as a whole.
For example:
  * in a service that lets the user register or apply for something, they might need to know that it’s taking longer than usual to process applications because of an emergency
  * in an account-type service, the user might need to know that the service will be down for scheduled maintenance

[ Open this example in a new tab: whole service – notification banner ](./components/notification-banner/whole-service.md)
  * [HTML](./components/notification-banner/#whole-service-notification-banner-example-html.md)
  * [Nunjucks](./components/notification-banner/#whole-service-notification-banner-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-notification-banner" role="region" aria-labelledby="govuk-notification-banner-title" data-module="govuk-notification-banner">
  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title" id="govuk-notification-banner-title">
      Important
    </h2>
  </div>
  <div class="govuk-notification-banner__content">
    <p class="govuk-notification-banner__heading">
      There may be a delay in processing your application because of the coronavirus outbreak.
    </p>
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
| text  | string  |  **Required.** The text that displays in the notification banner. You can use any string with this option. If you set `html`, this option is not required and is ignored.   |  
| html  | string  |  **Required.** The HTML to use within the notification banner. You can use any string with this option. If you set `html`, `text` is not required and is ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire notification banner component in a `call` block.   |  
| titleText  | string  |  The title text that displays in the notification banner. You can use any string with this option. Use this option to set text that does not contain HTML. The available default values are ‘Important’, ‘Success’, and null:
  * if you do not set `type`, `titleText` defaults to `"Important"`
  * if you set `type` to `success`, `titleText` defaults to `"Success"`
  * if you set `titleHtml`, this option is ignored

 |  
| titleHtml  | string  |  The title HTML to use within the notification banner. You can use any string with this option. Use this option to set text that contains HTML. If you set `titleHtml`, the `titleText` option is ignored.   |  
| titleHeadingLevel  | string  |  Sets heading level for the title only. You can only use values between `1` and `6` with this option. The default is `2`.   |  
| type  | string  |  The type of notification to render. You can use only `"success"` or `null` values with this option. If you set `type` to `"success"`, the notification banner sets `role` to `"alert"`. JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set `type`, the notification banner sets `role` to `"region"`.   |  
| role  | string  |  Overrides the value of the `role` attribute for the notification banner. Defaults to `"region"`. If you set `type` to `"success"`, `role` defaults to `"alert"`.   |  
| titleId  | string  |  The `id` for the banner title, and the `aria-labelledby` attribute in the banner. Defaults to `"govuk-notification-banner-title"`.   |  
| disableAutoFocus  | boolean  |  If you set `type` to `"success"`, or `role` to `"alert"`, JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set `disableAutoFocus` to `true`.   |  
| classes  | string  |  The classes that you want to add to the notification banner.   |  
| attributes  | object  |  The HTML attributes that you want to add to the notification banner, for example, data attributes.   |  
Copy code
```
{% from "govuk/components/notification-banner/macro.njk" import govukNotificationBanner %}

{{ govukNotificationBanner({
  text: "There may be a delay in processing your application because of the coronavirus outbreak."
}) }}
```

If your service is on GOV.UK and it’s affected by an emergency, ask your department’s content team to [request a change to the service start page](https://www.gov.uk/guidance/contact-the-government-digital-service/request-a-thing#change-govuk-content).  
If your service is getting more demand than usual, check that you’ve set up [There is a problem with the service pages](./patterns/problem-with-the-service-pages.md) and [Service unavailable pages](./patterns/service-unavailable-pages.md), and the wording is up to date.
## Telling the user about something that’s happening elsewhere
Use a ‘neutral’ notification banner if the user needs to know about something that’s happening elsewhere in the service. For example:
  * in a case working system, the user might need to know that there are new cases waiting for their attention
  * in an account-type service, you might need to tell the user that there’s a deadline approaching or that a payment is overdue

[ Open this example in a new tab: notification banner second ](./components/notification-banner/default.md)
  * [HTML](./components/notification-banner/#notification-banner-second-example-html.md)
  * [Nunjucks](./components/notification-banner/#notification-banner-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-notification-banner" role="region" aria-labelledby="govuk-notification-banner-title" data-module="govuk-notification-banner">
  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title" id="govuk-notification-banner-title">
      Important
    </h2>
  </div>
  <div class="govuk-notification-banner__content">
    <p class="govuk-notification-banner__heading">
      You have 7 days left to send your application.
      <a class="govuk-notification-banner__link" href="#">View application</a>.
    </p>
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
| text  | string  |  **Required.** The text that displays in the notification banner. You can use any string with this option. If you set `html`, this option is not required and is ignored.   |  
| html  | string  |  **Required.** The HTML to use within the notification banner. You can use any string with this option. If you set `html`, `text` is not required and is ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire notification banner component in a `call` block.   |  
| titleText  | string  |  The title text that displays in the notification banner. You can use any string with this option. Use this option to set text that does not contain HTML. The available default values are ‘Important’, ‘Success’, and null:
  * if you do not set `type`, `titleText` defaults to `"Important"`
  * if you set `type` to `success`, `titleText` defaults to `"Success"`
  * if you set `titleHtml`, this option is ignored

 |  
| titleHtml  | string  |  The title HTML to use within the notification banner. You can use any string with this option. Use this option to set text that contains HTML. If you set `titleHtml`, the `titleText` option is ignored.   |  
| titleHeadingLevel  | string  |  Sets heading level for the title only. You can only use values between `1` and `6` with this option. The default is `2`.   |  
| type  | string  |  The type of notification to render. You can use only `"success"` or `null` values with this option. If you set `type` to `"success"`, the notification banner sets `role` to `"alert"`. JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set `type`, the notification banner sets `role` to `"region"`.   |  
| role  | string  |  Overrides the value of the `role` attribute for the notification banner. Defaults to `"region"`. If you set `type` to `"success"`, `role` defaults to `"alert"`.   |  
| titleId  | string  |  The `id` for the banner title, and the `aria-labelledby` attribute in the banner. Defaults to `"govuk-notification-banner-title"`.   |  
| disableAutoFocus  | boolean  |  If you set `type` to `"success"`, or `role` to `"alert"`, JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set `disableAutoFocus` to `true`.   |  
| classes  | string  |  The classes that you want to add to the notification banner.   |  
| attributes  | object  |  The HTML attributes that you want to add to the notification banner, for example, data attributes.   |  
Copy code
```
{% from "govuk/components/notification-banner/macro.njk" import govukNotificationBanner %}

{% set html %}
  <p class="govuk-notification-banner__heading">
    You have 7 days left to send your application.
    <a class="govuk-notification-banner__link" href="#">View application</a>.
  </p>
{% endset %}

{{ govukNotificationBanner({
  html: html
}) }}
```

## Reacting to something the user has done
You can also use a notification banner to tell the user about the outcome of something they’ve just done - but they have not finished the current journey, so it does not make sense to use a [Confirmation page at this point in your service](./patterns/confirmation-pages.md).
Using a notification banner is unlikely to be the right approach in a linear service - for example, a service that lets the user register or apply for a thing. For a linear service, it will usually make sense to stick to the [‘one thing per page’ approach](https://www.gov.uk/service-manual/design/form-structure), and avoid using a notification banner.
Use a [Confirmation page in a linear service](./patterns/confirmation-pages.md) to tell users that they’ve finished using the service instead of a notification banner.
Use the green version of the notification banner to confirm that something they’re expecting to happen has happened.
[ Open this example in a new tab: success banner – notification banner ](./components/notification-banner/success.md)
  * [HTML](./components/notification-banner/#success-banner-notification-banner-example-html.md)
  * [Nunjucks](./components/notification-banner/#success-banner-notification-banner-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-notification-banner govuk-notification-banner--success" role="alert" aria-labelledby="govuk-notification-banner-title" data-module="govuk-notification-banner">
  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title" id="govuk-notification-banner-title">
      Success
    </h2>
  </div>
  <div class="govuk-notification-banner__content">
    <h3 class="govuk-notification-banner__heading">
      Training outcome recorded and trainee withdrawn
    </h3>
    <p class="govuk-body">Contact <a class="govuk-notification-banner__link" href="#">example@department.gov.uk</a> if you think there’s a problem.</p>
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
| text  | string  |  **Required.** The text that displays in the notification banner. You can use any string with this option. If you set `html`, this option is not required and is ignored.   |  
| html  | string  |  **Required.** The HTML to use within the notification banner. You can use any string with this option. If you set `html`, `text` is not required and is ignored.   |  
| caller  | nunjucks-block  |  Not strictly a parameter but [Nunjucks code convention](https://mozilla.github.io/nunjucks/templating.html#call). Using a `call` block enables you to call a macro with all the text inside the tag. This is helpful if you want to pass a lot of content into a macro. To use it, you will need to wrap the entire notification banner component in a `call` block.   |  
| titleText  | string  |  The title text that displays in the notification banner. You can use any string with this option. Use this option to set text that does not contain HTML. The available default values are ‘Important’, ‘Success’, and null:
  * if you do not set `type`, `titleText` defaults to `"Important"`
  * if you set `type` to `success`, `titleText` defaults to `"Success"`
  * if you set `titleHtml`, this option is ignored

 |  
| titleHtml  | string  |  The title HTML to use within the notification banner. You can use any string with this option. Use this option to set text that contains HTML. If you set `titleHtml`, the `titleText` option is ignored.   |  
| titleHeadingLevel  | string  |  Sets heading level for the title only. You can only use values between `1` and `6` with this option. The default is `2`.   |  
| type  | string  |  The type of notification to render. You can use only `"success"` or `null` values with this option. If you set `type` to `"success"`, the notification banner sets `role` to `"alert"`. JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set `type`, the notification banner sets `role` to `"region"`.   |  
| role  | string  |  Overrides the value of the `role` attribute for the notification banner. Defaults to `"region"`. If you set `type` to `"success"`, `role` defaults to `"alert"`.   |  
| titleId  | string  |  The `id` for the banner title, and the `aria-labelledby` attribute in the banner. Defaults to `"govuk-notification-banner-title"`.   |  
| disableAutoFocus  | boolean  |  If you set `type` to `"success"`, or `role` to `"alert"`, JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set `disableAutoFocus` to `true`.   |  
| classes  | string  |  The classes that you want to add to the notification banner.   |  
| attributes  | object  |  The HTML attributes that you want to add to the notification banner, for example, data attributes.   |  
Copy code
```
{% from "govuk/components/notification-banner/macro.njk" import govukNotificationBanner %}

{% set html %}
  <h3 class="govuk-notification-banner__heading">
    Training outcome recorded and trainee withdrawn
  </h3>
  <p class="govuk-body">Contact <a class="govuk-notification-banner__link" href="#">example@department.gov.uk</a> if you think there’s a problem.</p>
{% endset %}

{{ govukNotificationBanner({
  html: html,
  type: "success"
}) }}
```

Since you’re using the notification banner to tell the user about the outcome of something they’ve just done, add `role="alert"` so focus shifts to the notification banner on page load.
Remove a green notification banner when the user moves to a new page.
To make the green version of the notification banner accessible:
  * use headings like ‘Success’ - so that you’re not relying on colour alone to convey meaning – to [meet WCAG 2.2 success criterion 1.4.1 Use of colour](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
  * use the same heading for green notification banners within the same service - so that you’re identifying components that work in the same way consistently – this is to [meet WCAG 2.2 success criterion 3.2.4 Consistent identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification)

## Research on this component
We need more research to understand:
  * how common it is for users to miss important information in notification banners (including users of assistive technology, who might skip straight to the `h1`)
  * whether it’s sometimes helpful to allow users to dismiss notifications, and how to do this

## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Notification banner’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/2) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/notification-banner/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/notification-banner/#top.md)
