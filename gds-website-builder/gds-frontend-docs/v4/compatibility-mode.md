#  [](./v4/compatibility-mode/#use-with-our-old-frameworks-or-colours.md)Use with our old frameworks or colours
You can configure GOV.UK Frontend to look like our old frameworks, GOV.UK Elements, GOV.UK Template and GOV.UK Frontend Toolkit.
If you do this, your service will not meet the [Web Content Accessibility Guidelines (WCAG 2.1 level AA)](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps) because your users will not be able to change the font size.
You cannot use the following features if you installed GOV.UK Frontend using precompiled files. [Install with node package manager](./v4/installing-with-npm.md) instead.
##  [](./v4/compatibility-mode/#39-compatibility-mode-39.md)‘Compatibility mode’
Use ‘compatibility mode’ if you want to use GOV.UK Frontend components and an old framework together in a service.
GOV.UK Frontend will:
  * use the old colour palette
  * use the old GOV.UK font from GOV.UK Template
  * override some of the CSS in the legacy frameworks
  * no longer use `rem` for font sizes

##  [](./v4/compatibility-mode/#turn-on-39-compatibility-mode-39.md)Turn on ‘compatibility mode’
Add one or more of the following lines to your project’s Sass file, above `@import "govuk-frontend/govuk/all"`:
  * `$govuk-compatibility-govukelements: true;` if you’re using GOV.UK Elements
  * `$govuk-compatibility-govuktemplate: true;` if you’re using GOV.UK Template
  * `$govuk-compatibility-govukfrontendtoolkit: true;` if you’re using GOV.UK Frontend toolkit

##  [](./v4/compatibility-mode/#turn-off-39-compatibility-mode-39.md)Turn off ‘compatibility mode’
Remove the following lines from your project’s Sass file:
  * `$govuk-compatibility-govukelements: true;`
  * `$govuk-compatibility-govuktemplate: true;`
  * `$govuk-compatibility-govukfrontendtoolkit: true;`

##  [](./v4/compatibility-mode/#use-the-old-colour-palette.md)Use the old colour palette
If you’re not using any of our old frameworks, you can still configure GOV.UK Frontend to use the old colour palette.
Add the following variable to your project’s Sass file, above `@import "govuk-frontend/govuk/all"`:

```
$govuk-use-legacy-palette: true;

```

  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/compatibility-mode/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Use+with+our+old+frameworks+or+colours+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Fcompatibility-mode%2F%29&labels=bug&title=Re%3A+%27Use+with+our+old+frameworks+or+colours+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
