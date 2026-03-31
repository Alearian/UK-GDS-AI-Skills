#  [](./import-font-and-images-assets/#import-font-and-images-assets.md)Import font and images assets
To use the font and image assets from GOV.UK Frontend, you can either:
  * serve the assets from the GOV.UK Frontend assets folder - recommended
  * copy the font and image files into your application

##  [](./import-font-and-images-assets/#serve-the-assets-from-the-gov-uk-frontend-assets-folder-recommended.md)Serve the assets from the GOV.UK Frontend assets folder - recommended
Set up your routing so requests for files in `<YOUR-SITE-URL>/assets` are served from `/node_modules/govuk-frontend/dist/govuk/assets`.
For example if you’re using [express.js](https://expressjs.com/), add the following to your `app.js` file:

```
const path = require('path');
app.use('/assets', express.static(path.join(__dirname, '/node_modules/govuk-frontend/dist/govuk/assets')))

```

##  [](./import-font-and-images-assets/#copy-the-font-and-image-files-into-your-application.md)Copy the font and image files into your application
If you decide to copy the assets instead, copy the:
  * `/node_modules/govuk-frontend/dist/govuk/assets/images` folder to `<YOUR-APP>/assets/images`
  * `/node_modules/govuk-frontend/dist/govuk/assets/fonts` folder to `<YOUR-APP>/assets/fonts`
  * `/node_modules/govuk-frontend/dist/govuk/assets/manifest.json` file to `<YOUR-APP>/assets`

You should use an automated task or your build pipeline to copy the files, so your project folder stays up to date when we update GOV.UK Frontend.
###  [](./import-font-and-images-assets/#if-you-have-your-own-folder-structure.md)If you have your own folder structure
If you use a different folder structure than `<YOUR-APP>/assets/images` and `<YOUR-APP>/assets/fonts`, you can set Sass variables so that Sass builds the CSS to point to your folders.
Set one of the following before the `@import` line in your Sass file:
  * `$govuk-assets-path`
  * `$govuk-images-path` and `$govuk-fonts-path`

Set the `$govuk-assets-path` variable if your `font` and `image` folders have the same parent folder. For example:

```
$govuk-assets-path: "/<YOUR-ASSETS-FOLDER>/";

```

Set the `$govuk-images-path` and `$govuk-fonts-path` variables if your `font` and `image` folders have different parent folders. For example:

```
$govuk-images-path: "/<YOUR-IMAGES-FOLDER>/";
$govuk-fonts-path: "/<YOUR-FONTS-FOLDER>/";

```

You can also use your own function to generate paths, for example if you’re using `asset-pipeline` in [sass-rails](https://github.com/rails/sass-rails). Set the `$govuk-image-url-function` and `$govuk-font-url-function` variables to the name of your function.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/import-font-and-images-assets/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Import+font+and+images+assets%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fimport-font-and-images-assets%2F%29&labels=bug&title=Re%3A+%27Import+font+and+images+assets%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
