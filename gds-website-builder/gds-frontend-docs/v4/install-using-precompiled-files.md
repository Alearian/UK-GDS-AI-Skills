#  [](./v4/install-using-precompiled-files/#install-using-precompiled-files.md)Install using precompiled files
You can install GOV.UK Frontend by copying our CSS, JavaScript and asset files into your project. If you install this way, you can try GOV.UK Frontend in your application without having to make many changes.
! ** Warning In your live application, you should [install with Node.js package manager (npm)](./installing-with-npm.md) instead. **
##  [](./v4/install-using-precompiled-files/#what-you-cannot-do-after-installing.md)What you cannot do after installing
You’ll not be able to:
  * change [Sass settings](./v4/sass-api-reference.md), for example override colours or set your own font
  * use the Nunjucks code from the [Design System website](https://design-system.service.gov.uk/) to add components
  * import an individual component’s CSS or JavaScript
  * use GOV.UK Frontend’s colours or mixins in your custom code

##  [](./v4/install-using-precompiled-files/#copy-the-files.md)Copy the files
  1. Download the `release-<VERSION-NUMBER>.zip` file at the bottom of the [latest GOV.UK Frontend release note](https://github.com/alphagov/govuk-frontend/releases/latest).
  2. Unzip the zip file.
  3. Copy the `assets` folder to the root of your project’s public folder, so that for example `<YOUR-SITE-URL>/assets/govuk-logotype-crown.png` shows the `govuk-logotype-crown.png` image in your users’ browsers.
  4. Copy the 2 `.css` files to a stylesheets folder in the root of your project’s public folder, so that for example `<YOUR-SITE-URL>/stylesheets/govuk-frontend-<VERSION-NUMBER>.min.css` shows the CSS file in your users’ browsers.
  5. Copy the `.js` file to a JavaScript folder in the root of your project’s public folder, so that for example `<YOUR-SITE-URL>/javascript/govuk-frontend-<VERSION-NUMBER>.min.js` shows the JavaScript file in your users’ browsers.

##  [](./v4/install-using-precompiled-files/#check-an-example-page.md)Check an example page
  1. Create a page in your project using the following HTML (in your live application, you should use the [Design System page template](https://design-system.service.gov.uk/styles/page-template/) instead):

```
<!DOCTYPE html>
<html lang="en" class="govuk-template ">
  <head>
    <title>Example - GOV.UK</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <!--[if !IE 8]><!-->
      <link rel="stylesheet" href="/stylesheets/govuk-frontend-<VERSION-NUMBER>.min.css">
    <!--<![endif]-->
    <!--[if IE 8]>
      <link rel="stylesheet" href="/stylesheets/govuk-frontend-ie8-<VERSION-NUMBER>.min.css">
    <![endif]-->
  </head>
  <body class="govuk-template__body ">
    <script>
      document.body.className = ((document.body.className) ? document.body.className + ' js-enabled' : 'js-enabled');
    </script>
    <!-- component HTML -->
    <script src="/javascript/govuk-frontend-<VERSION-NUMBER>.min.js"></script>
    <script>
      window.GOVUKFrontend.initAll()
    </script>
  </body>
</html>

```

  2. Replace `<VERSION-NUMBER>` so the 3 filenames match the files you [copied from GOV.UK Frontend’s GitHub repo](./v4/install-using-precompiled-files/#copy-the-files.md).
  3. Go to the [example accordion component](https://design-system.service.gov.uk/components/accordion/#accordion-example) on the Design System website and copy the HTML from the first example.
  4. Replace `<!-- component HTML -->` with the accordion HTML you copied.
  5. Run your application - you can check it works the same way as the [Design System accordion example](https://design-system.service.gov.uk/components/accordion/default/index.html) by selecting the buttons and checking the accordion ‘shows’ and ‘hides’ sections.

You can now get the full code for page layouts and other components from the [Design System website](https://design-system.service.gov.uk/).
If the accordion does not work, you can [find out more about how to import GOV.UK Frontend’s CSS and JavaScript](./v4/importing-css-assets-and-javascript/#import-css-assets-and-javascript.md).
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/install-using-precompiled-files/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Install+using+precompiled+files+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Finstall-using-precompiled-files%2F%29&labels=bug&title=Re%3A+%27Install+using+precompiled+files+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
