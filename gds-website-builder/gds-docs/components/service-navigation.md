#  Service navigation 
Service navigation helps users understand that they’re using your service and lets them navigate around your service.
[ Open this example in a new tab: service navigation ](./components/service-navigation/default.md)
  * [HTML](./components/service-navigation/#service-navigation-example-html.md)
  * [Nunjucks](./components/service-navigation/#service-navigation-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-service-navigation"
  data-module="govuk-service-navigation">
  <div class="govuk-width-container">
    <div class="govuk-service-navigation__container">
      <nav aria-label="Menu" class="govuk-service-navigation__wrapper">
        <button type="button" class="govuk-service-navigation__toggle govuk-js-service-navigation-toggle" aria-controls="navigation" hidden aria-hidden="true">
          Menu
        </button>
        <ul class="govuk-service-navigation__list" id="navigation">
          <li class="govuk-service-navigation__item">
            <a class="govuk-service-navigation__link" href="#">
              Navigation item 1
            </a>
          </li>
          <li class="govuk-service-navigation__item govuk-service-navigation__item--active">
            <a class="govuk-service-navigation__link" href="#" aria-current="true">
              <strong class="govuk-service-navigation__active-fallback">Navigation item 2</strong>
            </a>
          </li>
          <li class="govuk-service-navigation__item">
            <a class="govuk-service-navigation__link" href="#">
              Navigation item 3
            </a>
          </li>
        </ul>
      </nav>
    </div>
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
| classes  | string  |  Classes to add to the service navigation container.   |  
| attributes  | object  |  HTML attributes (for example, data attributes) to add to the service navigation container.   |  
| ariaLabel  | string  |  The text for the `aria-label` which labels the service navigation container when a service name is included. Defaults to `"Service information"`.   |  
| menuButtonText  | string  |  The text of the mobile navigation menu toggle.   |  
| menuButtonLabel  | string  |  The screen reader label for the mobile navigation menu toggle. Defaults to the same value as `menuButtonText` if not specified.   |  
| navigationLabel  | string  |  The screen reader label for the mobile navigation menu. Defaults to the same value as `menuButtonText` if not specified.   |  
| navigationId  | string  |  The ID used to associate the mobile navigation toggle with the navigation menu. Defaults to `navigation`.   |  
| navigationClasses  | string  |  Classes to add to the navigation menu container.   |  
| collapseNavigationOnMobile  | boolean  |  Whether the navigation should be collapsed inside a menu on mobile. Defaults to true if there is more than one navigation item.   |  
| serviceName  | string  |  The name of your service.   |  
| serviceUrl  | string  |  The homepage of your service.   |  
| navigation  | array  |  **Required.** Used to add navigation to the service header. [ See macro options for navigation](./components/service-navigation/#options-service-navigation-example--navigation.md).   |  
| slots  | object  |  Specified points for injecting custom HTML into the service header. [ See macro options for slots](./components/service-navigation/#options-service-navigation-example--slots.md).   |  
Options for `navigation` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| current  | boolean  |  If `true`, indicates that the user is currently on this page. This takes precedence over `active`.   |  
| active  | boolean  |  If `true`, indicates that the user is within this group of pages in the navigation hierarchy.   |  
| html  | string  |  **Required.** HTML for the navigation item. If `html` is provided, the `text` option will be ignored.   |  
| text  | string  |  **Required.** Text for the navigation item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  URL of the navigation item anchor.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the navigation item anchor.   |  
Options for `slots` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| start  | string  |  HTML injected at the start of the service header container.   |  
| end  | string  |  HTML injected at the end of the service header container.   |  
| navigationStart  | string  |  HTML injected before the first list item in the navigation list. Requires `navigation` to be set.   |  
| navigationEnd  | string  |  HTML injected after the last list item in the navigation list. Requires `navigation` to be set.   |  
Copy code
```
{% from "govuk/components/service-navigation/macro.njk" import govukServiceNavigation %}

{{ govukServiceNavigation({
  navigation: [
    {
      href: "#",
      text: "Navigation item 1"
    },
    {
      href: "#",
      text: "Navigation item 2",
      active: true
    },
    {
      href: "#",
      text: "Navigation item 3"
    }
  ]
}) }}
```

If you use the page template, you’ll also get the Service navigation without having to add it, as it’s included by default. However, if you want to customise the default Service navigation, read the [page template guidance about customising components](./styles/page-template/#changing-template-content.md).
## When to use this component
Use the Service navigation to help users understand that they’re using your service.
To decide when to use navigation links in your service, see the [Help users to navigate a service pattern](./patterns/navigate-a-service.md).
## How it works
Together, the [GOV.UK header component](./components/header.md) and Service navigation component ensure users get a consistent experience on GOV.UK.
This also assures users that they’re in the right place to use your service and to understand that GOV.UK functions as one website.
For guidance on how to plan your header and navigation, see the [Help users navigate a service pattern](./patterns/navigate-a-service.md).
### Showing your service name only
Use the Service navigation component to show your service name.
[ Open this example in a new tab: service navigation with service name – service navigation ](./components/service-navigation/with-service-name.md)
  * [HTML](./components/service-navigation/#service-navigation-with-service-name-service-navigation-example-html.md)
  * [Nunjucks](./components/service-navigation/#service-navigation-with-service-name-service-navigation-example-nunjucks.md)

HTML
Copy code
```
<section aria-label="Service information" class="govuk-service-navigation"
  data-module="govuk-service-navigation">
  <div class="govuk-width-container">
    <div class="govuk-service-navigation__container">
      <span class="govuk-service-navigation__service-name">
        <a href="#" class="govuk-service-navigation__link">
          Service name
        </a>
      </span>
    </div>
  </div>
</section>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the service navigation container.   |  
| attributes  | object  |  HTML attributes (for example, data attributes) to add to the service navigation container.   |  
| ariaLabel  | string  |  The text for the `aria-label` which labels the service navigation container when a service name is included. Defaults to `"Service information"`.   |  
| menuButtonText  | string  |  The text of the mobile navigation menu toggle.   |  
| menuButtonLabel  | string  |  The screen reader label for the mobile navigation menu toggle. Defaults to the same value as `menuButtonText` if not specified.   |  
| navigationLabel  | string  |  The screen reader label for the mobile navigation menu. Defaults to the same value as `menuButtonText` if not specified.   |  
| navigationId  | string  |  The ID used to associate the mobile navigation toggle with the navigation menu. Defaults to `navigation`.   |  
| navigationClasses  | string  |  Classes to add to the navigation menu container.   |  
| collapseNavigationOnMobile  | boolean  |  Whether the navigation should be collapsed inside a menu on mobile. Defaults to true if there is more than one navigation item.   |  
| serviceName  | string  |  The name of your service.   |  
| serviceUrl  | string  |  The homepage of your service.   |  
| navigation  | array  |  **Required.** Used to add navigation to the service header. [ See macro options for navigation](./components/service-navigation/#options-service-navigation-with-service-name-service-navigation-example--navigation.md).   |  
| slots  | object  |  Specified points for injecting custom HTML into the service header. [ See macro options for slots](./components/service-navigation/#options-service-navigation-with-service-name-service-navigation-example--slots.md).   |  
Options for `navigation` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| current  | boolean  |  If `true`, indicates that the user is currently on this page. This takes precedence over `active`.   |  
| active  | boolean  |  If `true`, indicates that the user is within this group of pages in the navigation hierarchy.   |  
| html  | string  |  **Required.** HTML for the navigation item. If `html` is provided, the `text` option will be ignored.   |  
| text  | string  |  **Required.** Text for the navigation item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  URL of the navigation item anchor.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the navigation item anchor.   |  
Options for `slots` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| start  | string  |  HTML injected at the start of the service header container.   |  
| end  | string  |  HTML injected at the end of the service header container.   |  
| navigationStart  | string  |  HTML injected before the first list item in the navigation list. Requires `navigation` to be set.   |  
| navigationEnd  | string  |  HTML injected after the last list item in the navigation list. Requires `navigation` to be set.   |  
Copy code
```
{% from "govuk/components/service-navigation/macro.njk" import govukServiceNavigation %}

{{ govukServiceNavigation({
  serviceName: "Service name",
  serviceUrl: "#"
}) }}
```

### Showing service name and navigation links
Show navigation links to let users navigate to different parts of your service and find useful links and tools.
[ Open this example in a new tab: service navigation with service name and navigation – service navigation ](./components/service-navigation/with-service-name-and-navigation.md)
  * [HTML](./components/service-navigation/#service-navigation-with-service-name-and-navigation-service-navigation-example-html.md)
  * [Nunjucks](./components/service-navigation/#service-navigation-with-service-name-and-navigation-service-navigation-example-nunjucks.md)

HTML
Copy code
```
<section aria-label="Service information" class="govuk-service-navigation"
  data-module="govuk-service-navigation">
  <div class="govuk-width-container">
    <div class="govuk-service-navigation__container">
      <span class="govuk-service-navigation__service-name">
        <a href="#" class="govuk-service-navigation__link">
          Service name
        </a>
      </span>
      <nav aria-label="Menu" class="govuk-service-navigation__wrapper">
        <button type="button" class="govuk-service-navigation__toggle govuk-js-service-navigation-toggle" aria-controls="navigation" hidden aria-hidden="true">
          Menu
        </button>
        <ul class="govuk-service-navigation__list" id="navigation">
          <li class="govuk-service-navigation__item">
            <a class="govuk-service-navigation__link" href="#">
              Navigation item 1
            </a>
          </li>
          <li class="govuk-service-navigation__item govuk-service-navigation__item--active">
            <a class="govuk-service-navigation__link" href="#" aria-current="true">
              <strong class="govuk-service-navigation__active-fallback">Navigation item 2</strong>
            </a>
          </li>
          <li class="govuk-service-navigation__item">
            <a class="govuk-service-navigation__link" href="#">
              Navigation item 3
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</section>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the service navigation container.   |  
| attributes  | object  |  HTML attributes (for example, data attributes) to add to the service navigation container.   |  
| ariaLabel  | string  |  The text for the `aria-label` which labels the service navigation container when a service name is included. Defaults to `"Service information"`.   |  
| menuButtonText  | string  |  The text of the mobile navigation menu toggle.   |  
| menuButtonLabel  | string  |  The screen reader label for the mobile navigation menu toggle. Defaults to the same value as `menuButtonText` if not specified.   |  
| navigationLabel  | string  |  The screen reader label for the mobile navigation menu. Defaults to the same value as `menuButtonText` if not specified.   |  
| navigationId  | string  |  The ID used to associate the mobile navigation toggle with the navigation menu. Defaults to `navigation`.   |  
| navigationClasses  | string  |  Classes to add to the navigation menu container.   |  
| collapseNavigationOnMobile  | boolean  |  Whether the navigation should be collapsed inside a menu on mobile. Defaults to true if there is more than one navigation item.   |  
| serviceName  | string  |  The name of your service.   |  
| serviceUrl  | string  |  The homepage of your service.   |  
| navigation  | array  |  **Required.** Used to add navigation to the service header. [ See macro options for navigation](./components/service-navigation/#options-service-navigation-with-service-name-and-navigation-service-navigation-example--navigation.md).   |  
| slots  | object  |  Specified points for injecting custom HTML into the service header. [ See macro options for slots](./components/service-navigation/#options-service-navigation-with-service-name-and-navigation-service-navigation-example--slots.md).   |  
Options for `navigation` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| current  | boolean  |  If `true`, indicates that the user is currently on this page. This takes precedence over `active`.   |  
| active  | boolean  |  If `true`, indicates that the user is within this group of pages in the navigation hierarchy.   |  
| html  | string  |  **Required.** HTML for the navigation item. If `html` is provided, the `text` option will be ignored.   |  
| text  | string  |  **Required.** Text for the navigation item. If `html` is provided, the `text` option will be ignored.   |  
| href  | string  |  URL of the navigation item anchor.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the navigation item anchor.   |  
Options for `slots` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| start  | string  |  HTML injected at the start of the service header container.   |  
| end  | string  |  HTML injected at the end of the service header container.   |  
| navigationStart  | string  |  HTML injected before the first list item in the navigation list. Requires `navigation` to be set.   |  
| navigationEnd  | string  |  HTML injected after the last list item in the navigation list. Requires `navigation` to be set.   |  
Copy code
```
{% from "govuk/components/service-navigation/macro.njk" import govukServiceNavigation %}

{{ govukServiceNavigation({
  serviceName: "Service name",
  serviceUrl: "#",
  navigation: [
    {
      href: "#",
      text: "Navigation item 1"
    },
    {
      href: "#",
      text: "Navigation item 2",
      active: true
    },
    {
      href: "#",
      text: "Navigation item 3"
    }
  ]
}) }}
```

See when and how to show navigation links in the [Help users navigate a service pattern](./patterns/navigate-a-service.md).
## Use ‘slots’ to add custom elements
The Service navigation includes the option to use ‘slots’ to insert custom HTML code at specific points inside the component. This helps you extend the component to add custom elements, such as language selectors.
You must provide your own styles and JavaScript code for the content within a slot, particularly if you’re not using an existing component. You’ll need to decide on the most appropriate layout and positioning.
The [Help users to navigate a service pattern](./patterns/navigate-a-service.md) includes some guidance on ‘Adding other header and navigation elements’.
### Ensure the ‘aria-label’ is accurate for users of assistive technology
When a service name is shown, we let users know that there’s information about the service with a ‘region landmark’ using the `<section>` element.
Depending on what you add in the slots, you might need to rename the `aria-label` to accurately describe what’s in the section.
### Test with each update of GOV.UK Frontend
There’s a risk that slot contents may look or work differently in a future release of GOV.UK Frontend.
You’ll need to ensure that slot content still works as intended after each update.
## Brand refresh of the Service navigation component
In June 2025, we updated this component to support a wider refresh of the GOV.UK brand.
You should now use the refreshed GOV.UK branding. If your service has updated to GOV.UK Frontend v6.0.0 or later, you no longer need to use the `govukRebrand` feature flag and should remove it.
## Research on this component
See the [research section in the Help users navigate a service pattern](./patterns/navigate-a-service/#research-on-this-pattern.md) for a summary of our research on the GOV.UK header and Service navigation, and how you can share your feedback with us.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Service navigation’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/76) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/service-navigation/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/service-navigation/#top.md)
