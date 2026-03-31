#  [](./v4/migrating-from-legacy-products/#migrate-from-our-old-frameworks.md)Migrate from our old frameworks
This page explains how to migrate to GOV.UK Frontend if you’re using any of the following old frameworks:
  * GOV.UK Elements
  * GOV.UK Template
  * GOV.UK Frontend Toolkit

We’re no longer updating these old frameworks, and they do not meet the modern accessibility standards.
! ** Warning GOV.UK Frontend versions 5 and later are not compatible with these old frameworks. Remain on version 4 until you have finished migrating to GOV.UK Frontend and uninstalled the old frameworks. **
After you include GOV.UK Frontend in your project, your service should look and behave the same as before. This means you can migrate one component at a time in your live service.
Your service might be slightly slower until you’ve finished migrating, because your users’ browsers will download CSS and JavaScript from both GOV.UK Frontend and the old frameworks.
You can read about [how the GOV.UK Pay team migrated their service](https://technology.blog.gov.uk/2018/12/21/the-benefits-of-migrating-gov-uk-pays-codebase-to-the-gov-uk-design-system/).
##  [](./v4/migrating-from-legacy-products/#audit-your-service-39-s-components.md)Audit your service’s components
To help you migrate, you should work with a designer to make a list of the components in your service, and compare it to [the components in GOV.UK Frontend](https://design-system.service.gov.uk/components/).
You can use your list to see where you can replace similar elements in your service with one GOV.UK Frontend component. For example, if you have a range of similar buttons, you might be able to replace them all with the [button component](https://design-system.service.gov.uk/components/button/).
##  [](./v4/migrating-from-legacy-products/#choose-a-template-engine.md)Choose a template engine
We recommend using [a template engine like Nunjucks](https://mozilla.github.io/nunjucks/) to abstract each component into a reusable macro (also called a ‘partial’ or ‘template’). You can do this before or during your migration.
Macros will help make your project easier to:
  * migrate, because your project will be organised the same way we organise the GOV.UK Design System
  * update when new versions of GOV.UK Frontend are released

If you’re using Node.js, you can [use our Nunjucks macros](./v4/use-nunjucks.md).
Each [component page](https://design-system.service.gov.uk/components/) on the GOV.UK Design System website has example Nunjucks macros and a table of macro options.
##  [](./v4/migrating-from-legacy-products/#add-gov-uk-frontend-to-your-project.md)Add GOV.UK Frontend to your project
  1. [Install the latest v4 release of GOV.UK Frontend using npm](./v4/installing-with-npm.md). Do not install using precompiled files, or you will not be able to turn on ‘compatibility mode’.
  2. [Turn on GOV.UK Frontend’s ‘compatibility mode’](./v4/compatibility-mode/#turn-on-39-compatibility-mode-39.md) so your service continues using the old colours and font until you finish migrating.
  3. Test your application to make sure it looks the same and behaves correctly.

##  [](./v4/migrating-from-legacy-products/#migrate-your-pages-and-components.md)Migrate your pages and components
After you install GOV.UK Frontend, you can either migrate:
  * one page at a time - if your service is small, for example a single service with 10 pages
  * one component at a time - if your service is big or complicated

###  [](./v4/migrating-from-legacy-products/#migrate-one-page-at-a-time.md)Migrate one page at a time
We recommend creating a separate page layout based on our [page template](https://design-system.service.gov.uk/styles/page-template/), so that you can make changes without affecting the pages you have not migrated yet.
You must:
  * include GOV.UK Frontend JavaScript and CSS files below our old frameworks’ JavaScript and CSS files
  * use GOV.UK Frontend markup for all the [typography](https://design-system.service.gov.uk/styles/typography/) and [layout](https://design-system.service.gov.uk/styles/layout/) in your service
  * include and initialise GOV.UK Frontend’s JavaScript for all the components that use it

You should also follow our [guidance if you extend or modify GOV.UK Frontend components](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/).
###  [](./v4/migrating-from-legacy-products/#migrate-one-component-at-a-time.md)Migrate one component at a time
We recommend migrating in the following order:
  * [components](https://design-system.service.gov.uk/components/)
  * [typography](https://design-system.service.gov.uk/styles/typography/)
  * [header](https://design-system.service.gov.uk/components/header/)
  * [footer](https://design-system.service.gov.uk/components/footer/)
  * [page template](https://design-system.service.gov.uk/styles/page-template/)

We do not recommend the reverse order, because if you migrate the page template too early it might:
  * break CSS or JavaScript that relies on your old page template
  * apply layout features that are better applied at the end
  * make it harder to identify and cleanly remove old CSS and JavaScript

You must:
  * include GOV.UK Frontend JavaScript and CSS files below our old frameworks’ JavaScript and CSS files
  * use GOV.UK Frontend markup for all the [typography](https://design-system.service.gov.uk/styles/typography/) and [layout](https://design-system.service.gov.uk/styles/layout/) in your service
  * include and initialise GOV.UK Frontend’s JavaScript for all the components that use it

You should also follow our [guidance if you extend or modify GOV.UK Frontend components](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/).
To keep your design looking the same as it is now, you might need to add styles that [temporarily override GOV.UK Frontend styles](https://design-system.service.gov.uk/styles/spacing/#spacing-override-classes). For example, most GOV.UK Frontend components only have a bottom margin, so you might need to add temporary margins to the top, left or right.
##  [](./v4/migrating-from-legacy-products/#update-your-custom-code.md)Update your custom code
If you’ve created custom code that uses code from either GOV.UK Elements or GOV.UK Frontend Toolkit, you’ll need to:
  * [use GOV.UK Frontend variables, functions and mixins](./v4/migration-reference.md) instead
  * update your components’ focus states so they’re consistent with the [Design System’s focus styles](https://design-system.service.gov.uk/get-started/focus-states/).

##  [](./v4/migrating-from-legacy-products/#remove-our-old-frameworks.md)Remove our old frameworks
Once you’ve completely migrated your service to GOV.UK Frontend, you can remove our old frameworks.
###  [](./v4/migrating-from-legacy-products/#1-uninstall.md)1. Uninstall
Uninstall GOV.UK Frontend Toolkit, GOV.UK Element and GOV.UK Template.
###  [](./v4/migrating-from-legacy-products/#2-turn-off-compatibility-mode.md)2. Turn off compatibility mode
[Turn off ‘compatibility mode’](./v4/compatibility-mode/#turn-off-39-compatibility-mode-39.md) so your service stops using the old colours and font.
Replace the following old colour variables if you’re using Sass.  
| Old colour  | Suggested replacement  |  
| --- | --- |  
|  `bright-red`  | `red`  |  
|  `grey-1`  | `dark-grey`  |  
|  `grey-2`  | `mid-grey`  |  
|  `grey-3`  | `light-grey`  |  
|  `grey-4`  | `light-grey`  |  
You should also remove any temporary overrides you added earlier.
###  [](./v4/migrating-from-legacy-products/#3-test-your-updated-service.md)3. Test your updated service
You should check your application looks the same and works correctly, and that it’s using:
  * `rem` for font sizes
  * the [GOV.UK colour palette](https://design-system.service.gov.uk/styles/colour/)
  * the [GOV.UK font](https://design-system.service.gov.uk/styles/typography/#font)

You should also use the developer tools in your browser to check that your project:
  * is no longer using files from our old frameworks
  * is downloading only one version of the font
  * does not contain any unused stylesheets or JavaScript

###  [](./v4/migrating-from-legacy-products/#4-update-to-the-latest-version.md)4. Update to the latest version
Now that you have uninstalled the old frameworks and turned off compatibility mode, you can [update to the latest major version of GOV.UK Frontend](./staying-up-to-date.md).
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/migrating-from-legacy-products/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Migrate+from+our+old+frameworks+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Fmigrating-from-legacy-products%2F%29&labels=bug&title=Re%3A+%27Migrate+from+our+old+frameworks+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
