#  [](./changes-to-govuk-frontend-v6/#changes-in-gov-uk-frontend-v6-0-0.md)Changes in GOV.UK Frontend v6.0.0
GOV.UK Frontend v6.0.0 includes changes to:
  * improve our Sass architecture
  * use an updated type scale to improve accessibility for small screens
  * update colours to use the GOV.UK web palette in the GOV.UK brand guidelines
  * improve the page template layout

We’ve also removed a number of deprecated APIs, Sass variables and component options.
##  [](./changes-to-govuk-frontend-v6/#migrating-from-v5-to-v6-0-0.md)Migrating from v5 to v6.0.0
Follow the guidance about [staying up to date with GOV.UK Frontend](./staying-up-to-date.md).
When making the decision to migrate, consider your service’s requirements and your ability to update Sass tooling and templates. In particular, you must update to [Dart Sass v1.79.0 or later](https://sass-lang.com/dart-sass/) before upgrading to v6.0.0.
##  [](./changes-to-govuk-frontend-v6/#benefits-of-updating-to-v6-0-0.md)Benefits of updating to v6.0.0
By updating to v6.0.0 you’ll:
  * stay aligned with the GOV.UK look and feel: we’ve updated GOV.UK Frontend to use the GOV.UK web palette from the GOV.UK brand guidelines
  * benefit from a more consistent colour system in certain components
  * get the latest accessibility improvements, based on ongoing testing and feedback from services across government
  * benefit from a smaller CSS payload
  * be able to customise the page template further than before

##  [](./changes-to-govuk-frontend-v6/#updating-to-v6-0-0.md)Updating to v6.0.0
Read the [GOV.UK Frontend v6.0.0 release notes](https://github.com/alphagov/govuk-frontend/releases/v6.0.0) to see the full list of breaking and recommended changes.
You might need to update some items to update to v6.0.0, including:
  * updating your Sass compiler to [Dart Sass v1.79.0 or later](https://sass-lang.com/dart-sass/)
  * using the latest GOV.UK web palette 
  * using the new colour functions and replacing colours to follow the new naming convention

You’ll need to check some items still work as expected, including:
  * making sure any custom use of functional colours still follows best accessibility practice for contrast and legibility
  * updating any custom header or footer content, as we’ve changed how you can use and customise these components
  * testing the new type scale in your service to see if you need to make any adjustments

You’ll also need to remove references to any APIs, Sass variables and component options that we’ve removed.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/changes-to-govuk-frontend-v6/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Changes+in+GOV.UK+Frontend+v6.0.0%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fchanges-to-govuk-frontend-v6%2F%29&labels=bug&title=Re%3A+%27Changes+in+GOV.UK+Frontend+v6.0.0%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
