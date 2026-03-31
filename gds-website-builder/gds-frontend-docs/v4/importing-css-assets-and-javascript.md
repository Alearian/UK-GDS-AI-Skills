#  [](./v4/importing-css-assets-and-javascript/#import-css-assets-and-javascript.md)Import CSS, assets and JavaScript
##  [](./v4/importing-css-assets-and-javascript/#css.md)CSS
###  [](./v4/importing-css-assets-and-javascript/#import-all-the-css.md)Import all the CSS
To import all the Sass rules from GOV.UK Frontend, add the following to your Sass file:

```
@import "node_modules/govuk-frontend/govuk/all";

```

###  [](./v4/importing-css-assets-and-javascript/#import-specific-parts-of-the-css.md)Import specific parts of the CSS
If you want to improve how quickly your service’s pages load in browsers, you can import only the Sass rules you need.
  1. Import `node_modules/govuk-frontend/govuk/base` in your Sass file.
  2. Import the parts of the CSS you need.

For example, add the following to your Sass file to import the CSS you need for a basic GOV.UK page.

```
@import "node_modules/govuk-frontend/govuk/base";

@import "node_modules/govuk-frontend/govuk/core/all";
@import "node_modules/govuk-frontend/govuk/objects/all";
@import "node_modules/govuk-frontend/govuk/components/footer/index";
@import "node_modules/govuk-frontend/govuk/components/header/index";
@import "node_modules/govuk-frontend/govuk/components/skip-link/index";
@import "node_modules/govuk-frontend/govuk/utilities/all";
@import "node_modules/govuk-frontend/govuk/overrides/all";

```

You can remove lines that import parts of the CSS you do not need.
[Read more about the different parts of GOV.UK Frontend’s CSS](https://github.com/alphagov/govuk-frontend/tree/master/src/govuk).
You do not need `/index` at the end of your component imports if you’re using Dart Sass, LibSass 3.6.0 or higher, or Ruby Sass 3.6.0 or higher.
###  [](./v4/importing-css-assets-and-javascript/#import-an-individual-component-s-css-using-a-single-import.md)Import an individual component’s CSS using a single import
You can also import a component and all its dependencies without importing `node_modules/govuk-frontend/govuk/base` first.
To import the button component for example, add the following to your Sass file:

```
@import "node_modules/govuk-frontend/govuk/components/button/button";

```

###  [](./v4/importing-css-assets-and-javascript/#simplify-sass-import-paths.md)Simplify Sass import paths
If you want to make Sass import paths shorter, add `node_modules/govuk-frontend` to either your:
  * [Sass load paths](https://sass-lang.com/documentation/at-rules/import#finding-the-file)
  * [assets paths](http://guides.rubyonrails.org/asset_pipeline.html#search-paths) if you use Ruby in your project

You can then import without using `node_modules/govuk-frontend/` in your import path. For example:

```
@import "govuk/components/button/button";

```

###  [](./v4/importing-css-assets-and-javascript/#override-with-your-own-css.md)Override with your own CSS
If you want to override GOV.UK Frontend’s styles with your own styles, `@import` GOV.UK Frontend’s styles before your own Sass rules.
###  [](./v4/importing-css-assets-and-javascript/#using-gov-uk-frontend-with-our-old-frameworks.md)Using GOV.UK Frontend with our old frameworks
If your project uses GOV.UK Frontend toolkit, GOV.UK Template or GOV.UK Elements, you can [configure GOV.UK Frontend to work with them](./v4/compatibility-mode.md).
###  [](./v4/importing-css-assets-and-javascript/#silence-deprecation-warnings-from-dependencies-in-dart-sass.md)Silence deprecation warnings from dependencies in Dart Sass
If you’re using Dart Sass 1.33.0 or greater, you may see deprecation warnings when compiling your Sass. For example:

```
DEPRECATION WARNING: Using / for division is deprecated and will be removed in Dart Sass 2.0.0.

```

We’re currently unable to fix these deprecation warnings without breaking support for LibSass. However, you can silence the warnings caused by GOV.UK Frontend and other dependencies. Make sure you’re using Dart Sass 1.49.10 or greater, and then if you’re:
  * calling the Sass compiler from the command line, [pass the `--quiet-deps` flag](https://sass-lang.com/documentation/cli/dart-sass#quiet-deps)
  * using the JavaScript API, [include `quietDeps: true`](https://sass-lang.com/documentation/js-api#quietdeps) in the `options` object

You’ll still see deprecation warnings if you’re using `/` for division in your own Sass code.
##  [](./v4/importing-css-assets-and-javascript/#font-and-image-assets.md)Font and image assets
To use the font and image assets from GOV.UK Frontend, you can either:
  * serve the assets from the GOV.UK Frontend assets folder - recommended
  * copy the font and image files into your application

###  [](./v4/importing-css-assets-and-javascript/#serve-the-assets-from-the-gov-uk-frontend-assets-folder-recommended.md)Serve the assets from the GOV.UK Frontend assets folder - recommended
Set up your routing so that requests for files in `<YOUR-SITE-URL>/assets` are served from `/node_modules/govuk-frontend/govuk/assets`.
For example if you’re using [express.js](https://expressjs.com/), add the following to your `app.js` file:

```
var path = require('path');
app.use('/assets', express.static(path.join(__dirname, '/node_modules/govuk-frontend/govuk/assets')))

```

###  [](./v4/importing-css-assets-and-javascript/#copy-the-font-and-image-files-into-your-application.md)Copy the font and image files into your application
If you decide to copy the assets instead, copy the:
  * `/node_modules/govuk-frontend/govuk/assets/images` folder to `<YOUR-APP>/assets/images`
  * `/node_modules/govuk-frontend/govuk/assets/fonts` folder to `<YOUR-APP>/assets/fonts`

You should use an automated task or your build pipeline to copy the files, so your project folder stays up to date when we update GOV.UK Frontend.
####  [](./v4/importing-css-assets-and-javascript/#if-you-have-your-own-folder-structure.md)If you have your own folder structure
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
##  [](./v4/importing-css-assets-and-javascript/#javascript.md)JavaScript
To import the JavaScript from GOV.UK Frontend, you can either:
  * add GOV.UK Frontend’s JavaScript file to your HTML
  * import the JavaScript using a bundler like [Webpack](https://webpack.js.org/)

###  [](./v4/importing-css-assets-and-javascript/#add-the-javascript-file-to-your-html.md)Add the JavaScript file to your HTML
If you decide to add the JavaScript to your HTML, first either:
  * set up your routing so that requests for the JavaScript file are served from `node_modules/govuk-frontend/govuk/all.js`
  * copy the `node_modules/govuk-frontend/govuk/all.js` file into your application

Then import the JavaScript file before the closing `</body>` tag of your HTML page or page template, and run the `initAll` function to initialise all the components.

```
<body>
...
  <script src="<YOUR-APP>/<YOUR-JS-FILE>.js"></script>
  <script>
    window.GOVUKFrontend.initAll()
  </script>
</body>

```

####  [](./v4/importing-css-assets-and-javascript/#select-and-initialise-an-individual-component.md)Select and initialise an individual component
You can select and initialise a specific component by using its `data-module` attribute. For example, use `govuk-radios` to initialise the first radio component on a page:

```
  <script>
    var Radios = window.GOVUKFrontend.Radios
    var $radio = document.querySelector('[data-module="govuk-radios"]')
    if ($radio) {
      new Radios($radio).init()
    }
  </script>

```

###  [](./v4/importing-css-assets-and-javascript/#import-javascript-using-a-bundler.md)Import JavaScript using a bundler
If you decide to import using a bundler, we recommend you use `import` to only import the JavaScript for components you’re using in your service. For example:

```
import { SkipLink, Radios } from 'govuk-frontend'

var $skipLink = document.querySelector('[data-module="govuk-skip-link"]')
if ($skipLink) {
  new SkipLink($skipLink).init()
}

var $radios = document.querySelectorAll('[data-module="govuk-radios"]')
if ($radios) {
  for (var i = 0; i < $radios.length; i++) {
    new Radios($radios[i]).init()
  }
}

```

If you need to import all of GOV.UK Frontend’s components, then run the `initAll` function to initialise them:

```
import { initAll } from 'govuk-frontend'
initAll()

```

If you’re using a bundler that uses CommonJS like [Browserify](http://browserify.org/), you should use `require`:

```
const GOVUKFrontend = require('govuk-frontend')
GOVUKFrontend.initAll()

```

###  [](./v4/importing-css-assets-and-javascript/#select-and-initialise-part-of-a-page.md)Select and initialise part of a page
If you update a page with new markup, for example a modal dialogue box, you can run `initAll` with a `{ scope }` option to initialise the components on part of a page.
For example:

```
  <script>
    var $modal = document.querySelector('.modal')
    window.GOVUKFrontend.initAll({
      scope: $modal
    })
  </script>

```

###  [](./v4/importing-css-assets-and-javascript/#if-your-javascript-is-not-working-properly.md)If your JavaScript is not working properly
If your site has a Content Security Policy (CSP), the CSP may block the inline JavaScript in the page template. You may see a warning like the following in your browser’s developer tools:

```
Refused to execute inline script because it violates the following Content Security Policy directive: "default-src 'self'".

```

To unblock inline JavaScript, do one of the following:
  * include a hash (recommended)
  * use a nonce

Make sure you [understand the security implications of using either option](https://www.w3.org/TR/CSP/#security-considerations), as wrong implementation could affect your service’s security. If you’re not sure what to do, talk to a security expert.
####  [](./v4/importing-css-assets-and-javascript/#use-a-hash-to-unblock-inline-javascript.md)Use a hash to unblock inline JavaScript
You can unblock inline JavaScript by including the following hash in your CSP:

```
sha256-+6WnXIl4mbFTCARd8N3COQmT3bJJmo32N8q8ZSQAIcU=

```

You do not need to make any changes to the HTML.
[Learn more about Content Security Policy on the MDN Web Docs website](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP).
####  [](./v4/importing-css-assets-and-javascript/#use-a-nonce-attribute-to-unblock-inline-javascript.md)Use a `nonce` attribute to unblock inline JavaScript
If you’re unable to use the hash in your CSP, you can also use a `nonce` on inline JavaScript.
However, you should provide a nonce that hostile actors cannot guess. Otherwise, they could easily find a way around your CSP.
You should use a value which is:
  * unique for each HTTP response
  * generated using a cryptographically-secure random generator
  * at least 32 characters for hex, or 24 characters for base64

Make sure your script tags do not have any untrusted or unescaped variables.
If you’re using the Nunjucks page template, you can add the `nonce` attribute by setting the `cspNonce` variable.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/importing-css-assets-and-javascript/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Import+CSS%2C+assets+and+JavaScript+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Fimporting-css-assets-and-javascript%2F%29&labels=bug&title=Re%3A+%27Import+CSS%2C+assets+and+JavaScript+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
