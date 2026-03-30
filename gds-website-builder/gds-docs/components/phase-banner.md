#  Phase banner 
Use the phase banner component to show users your service is still being worked on.
[ Open this example in a new tab: phase banner ](./components/phase-banner/default.md)
  * [HTML](./components/phase-banner/#phase-banner-example-html.md)
  * [Nunjucks](./components/phase-banner/#phase-banner-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-phase-banner govuk-width-container">
  <p class="govuk-phase-banner__content">
    <strong class="govuk-tag govuk-phase-banner__content__tag">
      Alpha
    </strong>
    <span class="govuk-phase-banner__text">
      This is a new service. Help us improve it and <a class="govuk-link" href="#">give your feedback by email</a>.
    </span>
  </p>
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the phase banner. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the phase banner. If `html` is provided, the `text` option will be ignored.   |  
| tag  | object  |  **Required.** The tag used by the phase banner component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| classes  | string  |  Classes to add to the phase banner container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the phase banner container.   |  
Copy code
```
{% from "govuk/components/phase-banner/macro.njk" import govukPhaseBanner %}

{{ govukPhaseBanner({
  tag: {
    text: "Alpha"
  },
  html: 'This is a new service. Help us improve it and <a class="govuk-link" href="#">give your feedback by email</a>.'
}) }}
```

## When to use this component
Services hosted on a service.gov.uk domain must use the phase banner until they pass a live assessment.
## How it works
There are 2 ways to use the phase banner component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
Use an alpha banner when your service is in alpha, and a beta banner if your service is in private or public beta.
Show the Phase banner inside the `<header>` element, directly after either:
  * the [Service navigation component](./components/service-navigation.md)
  * the [GOV.UK header component](./components/header.md) and its blue colour bar (if your service does not use the Service navigation component)

If you use Nunjucks, use the `headerEnd` block to place the Phase banner on your page.
See [‘Add extra content at the start or end of the `<header>` element’ in ‘Page template: Blocks and options’](./styles/page-template/#add-extra-content-at-the-start-or-end-of-the-header-element.md).
Phase banners are shown across all pages of a service, so users should understand it as a service-level message.
You can choose to place the Phase banner in a more appropriate place for your service, however you’ll need to customise the component and provide your own CSS code to make it show correctly.
### Add a feedback link
Use a ‘feedback’ link to collect on-page feedback about your service. This can open an email or take the user to a dedicated page or form.
[ Open this example in a new tab: phase banner second ](./components/phase-banner/default.md)
  * [HTML](./components/phase-banner/#phase-banner-second-example-html.md)
  * [Nunjucks](./components/phase-banner/#phase-banner-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-phase-banner govuk-width-container">
  <p class="govuk-phase-banner__content">
    <strong class="govuk-tag govuk-phase-banner__content__tag">
      Alpha
    </strong>
    <span class="govuk-phase-banner__text">
      This is a new service. Help us improve it and <a class="govuk-link" href="#">give your feedback by email</a>.
    </span>
  </p>
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the phase banner. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the phase banner. If `html` is provided, the `text` option will be ignored.   |  
| tag  | object  |  **Required.** The tag used by the phase banner component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| classes  | string  |  Classes to add to the phase banner container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the phase banner container.   |  
Copy code
```
{% from "govuk/components/phase-banner/macro.njk" import govukPhaseBanner %}

{{ govukPhaseBanner({
  tag: {
    text: "Alpha"
  },
  html: 'This is a new service. Help us improve it and <a class="govuk-link" href="#">give your feedback by email</a>.'
}) }}
```

[ Open this example in a new tab: phase banner with beta text – phase banner ](./components/phase-banner/beta.md)
  * [HTML](./components/phase-banner/#phase-banner-with-beta-text-phase-banner-example-html.md)
  * [Nunjucks](./components/phase-banner/#phase-banner-with-beta-text-phase-banner-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-phase-banner govuk-width-container">
  <p class="govuk-phase-banner__content">
    <strong class="govuk-tag govuk-phase-banner__content__tag">
      Beta
    </strong>
    <span class="govuk-phase-banner__text">
      This is a new service. Help us improve it and <a class="govuk-link" href="#">give your feedback (opens in new tab)</a>.
    </span>
  </p>
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the phase banner. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the phase banner. If `html` is provided, the `text` option will be ignored.   |  
| tag  | object  |  **Required.** The tag used by the phase banner component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| classes  | string  |  Classes to add to the phase banner container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the phase banner container.   |  
Copy code
```
{% from "govuk/components/phase-banner/macro.njk" import govukPhaseBanner %}

{{ govukPhaseBanner({
  tag: {
    text: "Beta"
  },
  html: 'This is a new service. Help us improve it and <a class="govuk-link" href="#">give your feedback (opens in new tab)</a>.'
}) }}
```

Whatever option you use, make sure that users do not lose their place in the service and can return to the page they were on.
[Find out what feedback you need to collect at each phase](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction#user-satisfaction-through-each-service-phase) in the GOV.UK Service Manual.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Phase banner’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/57) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/phase-banner/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/phase-banner/#top.md)
