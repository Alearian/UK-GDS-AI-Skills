#  [](./v4/testing-your-html/#test-if-your-html-matches-gov-uk-frontend.md)Test if your HTML matches GOV.UK Frontend
You can use our test fixtures to check you’re outputting the same HTML that GOV.UK Frontend uses, when you:
  * create your own component macros (also called ‘partials’ or ‘templates’)
  * [update GOV.UK Frontend](./v4/staying-up-to-date.md)

##  [](./v4/testing-your-html/#using-the-html-test-files.md)Using the HTML test files
If you [installed GOV.UK Frontend with Node.js package manager (npm)](./v4/installing-with-npm.md), you can find the `fixtures.json` file for each component in the `node_modules/govuk-frontend/govuk/components/COMPONENT-NAME/` folder, where `COMPONENT-NAME` is the name of the component.
For example, you can find the `fixtures.json` file for the button component in the `node_modules/govuk-frontend/govuk/components/button/` folder:

```
{
  "component": "button",
  "fixtures": [
    {
      "name": "default",
      "options": {
        "text": "Save and continue"
      },
      "html": "<button class=\"govuk-button\" data-module=\"govuk-button\">\n  Save and continue\n</button>",
      "hidden": false
    },
    {
      "name": "secondary button",
      "options": {
        "text": "Find address",
        "classes": "govuk-button--secondary"
      },
      "html": "<button class=\"govuk-button govuk-button--secondary\" data-module=\"govuk-button\">\nFind address\n</button>",
      "hidden": false
    },
    ...
  ]
}

```

Each object in the `fixtures` list is a different example of the component, where:
  * `name` is the name of the example
  * `options` are the options that generate this example’s `html`
  * `html` is the HTML that GOV.UK Frontend outputs with these options
  * `hidden` is `true` if the fixture does not look or behave differently to the other fixtures provided

Do not include `hidden` fixtures when you use fixtures for manual or visual regression testing.
For each example, pass `options` into your own macro and check the generated HTML matches `html`.
If your HTML does not match exactly, you’ll need to write your tests so they ignore known differences. For example your framework may add extra whitespace or attributes to your HTML.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/testing-your-html/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Test+if+your+HTML+matches+GOV.UK+Frontend+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Ftesting-your-html%2F%29&labels=bug&title=Re%3A+%27Test+if+your+HTML+matches+GOV.UK+Frontend+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
