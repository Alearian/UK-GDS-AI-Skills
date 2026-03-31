#  [](./v5/import-css/#import-css.md)Import CSS
To import the CSS from GOV.UK Frontend, you can either:
  * add GOV.UK Frontend’s CSS file to your HTML
  * import the CSS into your own Sass file

##  [](./v5/import-css/#add-the-css-file-to-your-html.md)Add the CSS file to your HTML
If you decide to add the CSS to your HTML, you can do one of the following:
  * set up your routing so requests for the CSS file are served from `node_modules/govuk-frontend/dist/govuk/govuk-frontend.min.css`
  * copy the `node_modules/govuk-frontend/dist/govuk/govuk-frontend.min.css` file into your application

Then link the CSS file inside the `<head>` tag of your HTML page or page template.

```
<head>
  <!-- // ... -->
  <link rel="stylesheet" href="<YOUR-STYLESHEETS-FOLDER>/govuk-frontend.min.css">
  <!-- // ... -->
</head>

```

##  [](./v5/import-css/#import-using-sass.md)Import using Sass
To import all the Sass rules from GOV.UK Frontend, add the following to your Sass file:

```
@import "node_modules/govuk-frontend/dist/govuk/index";

```

You do not need `/index` at the end of your import if you’re using Dart Sass, LibSass 3.6.0 or higher, or Ruby Sass 3.6.0 or higher.
##  [](./v5/import-css/#import-specific-parts-using-sass.md)Import specific parts using Sass
If you want to improve how quickly your service’s pages load in browsers, you can import only the Sass rules you need.
  1. Import `node_modules/govuk-frontend/dist/govuk/base` in your Sass file.
  2. Import only the Sass you need based on the components and other classes your service is using.

The biggest optimisations come from excluding any components or overrides you’re not using.
You must import the layers in the order listed in the example below.

```
// 'Base' includes everything from settings, tools and helpers. Nothing
// in the base outputs any CSS.

@import "node_modules/govuk-frontend/dist/govuk/base";

// Basic content styles for typography, links etc. Approximately 10% of
// the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/core/index";

// Objects include things like the page template, grid and form groups.
// Approximately 5% of the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/objects/index";

// The components themselves - try to only include the components you
// are using in your project. Approximately 70% of the CSS output if
// you include everything.

@import "node_modules/govuk-frontend/dist/govuk/components/accordion/index";
@import "node_modules/govuk-frontend/dist/govuk/components/back-link/index";
@import "node_modules/govuk-frontend/dist/govuk/components/breadcrumbs/index";
@import "node_modules/govuk-frontend/dist/govuk/components/button/index";
@import "node_modules/govuk-frontend/dist/govuk/components/character-count/index";
@import "node_modules/govuk-frontend/dist/govuk/components/checkboxes/index";
@import "node_modules/govuk-frontend/dist/govuk/components/cookie-banner/index";
@import "node_modules/govuk-frontend/dist/govuk/components/date-input/index";
@import "node_modules/govuk-frontend/dist/govuk/components/details/index";
@import "node_modules/govuk-frontend/dist/govuk/components/error-message/index";
@import "node_modules/govuk-frontend/dist/govuk/components/error-summary/index";
@import "node_modules/govuk-frontend/dist/govuk/components/exit-this-page/index";
@import "node_modules/govuk-frontend/dist/govuk/components/fieldset/index";
@import "node_modules/govuk-frontend/dist/govuk/components/file-upload/index";
@import "node_modules/govuk-frontend/dist/govuk/components/footer/index";
@import "node_modules/govuk-frontend/dist/govuk/components/header/index";
@import "node_modules/govuk-frontend/dist/govuk/components/hint/index";
@import "node_modules/govuk-frontend/dist/govuk/components/input/index";
@import "node_modules/govuk-frontend/dist/govuk/components/inset-text/index";
@import "node_modules/govuk-frontend/dist/govuk/components/label/index";
@import "node_modules/govuk-frontend/dist/govuk/components/notification-banner/index";
@import "node_modules/govuk-frontend/dist/govuk/components/pagination/index";
@import "node_modules/govuk-frontend/dist/govuk/components/panel/index";
@import "node_modules/govuk-frontend/dist/govuk/components/password-input/index";
@import "node_modules/govuk-frontend/dist/govuk/components/phase-banner/index";
@import "node_modules/govuk-frontend/dist/govuk/components/radios/index";
@import "node_modules/govuk-frontend/dist/govuk/components/select/index";
@import "node_modules/govuk-frontend/dist/govuk/components/service-navigation/index";
@import "node_modules/govuk-frontend/dist/govuk/components/skip-link/index";
@import "node_modules/govuk-frontend/dist/govuk/components/summary-list/index";
@import "node_modules/govuk-frontend/dist/govuk/components/table/index";
@import "node_modules/govuk-frontend/dist/govuk/components/tabs/index";
@import "node_modules/govuk-frontend/dist/govuk/components/tag/index";
@import "node_modules/govuk-frontend/dist/govuk/components/task-list/index";
@import "node_modules/govuk-frontend/dist/govuk/components/textarea/index";
@import "node_modules/govuk-frontend/dist/govuk/components/warning-text/index";

/*
// Alternatively, you can import all components:
@import "node_modules/govuk-frontend/dist/govuk/components/index";
*/

// Utilities, for example govuk-clearfix or govuk-visually-hidden.
// Approximately 1% of the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/utilities/index";

// Overrides, used to adjust things like the amount of spacing on an
// element. Override classes always include `-!-` in the class name.
// Approximately 15% of the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/overrides/index";

/*
// Alternatively, you can import the specific groups of overrides
// you need for your project:

// Display overrides - for example govuk-!-display-inline
@import "node_modules/govuk-frontend/dist/govuk/overrides/display";

// Spacing overrides - for example govuk-!-margin-4, govuk-!-static-padding-4
@import "node_modules/govuk-frontend/dist/govuk/overrides/spacing";

// Text align overrides - for example govuk-!-text-align-left
@import "node_modules/govuk-frontend/dist/govuk/overrides/text-align";

// Typography overrides - for example govuk-!-font-size-19, govuk-!-font-weight-bold
@import "node_modules/govuk-frontend/dist/govuk/overrides/typography";

// Width overrides - for example govuk-!-width-two-thirds
@import "node_modules/govuk-frontend/dist/govuk/overrides/width";
*/

```

You can remove lines that import parts of the CSS you do not need.
[Read more about the different parts of GOV.UK Frontend’s CSS](https://github.com/alphagov/govuk-frontend/tree/main/packages/govuk-frontend/src).
You do not need `/index` at the end of your imports if you’re using Dart Sass, LibSass 3.6.0 or higher, or Ruby Sass 3.6.0 or higher.
##  [](./v5/import-css/#import-an-individual-component-s-css-using-a-single-sass-import.md)Import an individual component’s CSS using a single Sass import
You can also import a component and all its dependencies without importing `node_modules/govuk-frontend/dist/govuk/base` first.
To import the button component for example, add the following to your Sass file:

```
@import "node_modules/govuk-frontend/dist/govuk/components/button/button";

```

##  [](./v5/import-css/#simplify-sass-import-paths.md)Simplify Sass import paths
If you want to make Sass import paths shorter, add `node_modules/govuk-frontend/dist` to either your:
  * [Sass load paths](https://sass-lang.com/documentation/at-rules/import#finding-the-file)
  * [assets paths](http://guides.rubyonrails.org/asset_pipeline.html#search-paths) if you use Ruby in your project

You can then import without using `node_modules/govuk-frontend/dist/` in your import path. For example:

```
@import "govuk/components/button/button";

```

##  [](./v5/import-css/#override-with-your-own-css.md)Override with your own CSS
If you want to override GOV.UK Frontend’s styles with your own styles, `@import` GOV.UK Frontend’s styles before your own Sass rules.
##  [](./v5/import-css/#silence-deprecation-warnings-from-dependencies-in-dart-sass.md)Silence deprecation warnings from dependencies in Dart Sass
If you’re using Dart Sass 1.33.0 or greater, you may see deprecation warnings when compiling your Sass. For example:

```
DEPRECATION WARNING: Using / for division is deprecated and will be removed in Dart Sass 2.0.0.

```

We’re currently unable to fix these deprecation warnings without breaking support for LibSass. However, you can silence the warnings caused by GOV.UK Frontend and other dependencies. Make sure you’re using Dart Sass 1.49.10 or greater, and then if you’re:
  * calling the Sass compiler from the command line, [pass the `--quiet-deps` flag](https://sass-lang.com/documentation/cli/dart-sass#quiet-deps)
  * using the JavaScript API, [include `quietDeps: true`](https://sass-lang.com/documentation/js-api#quietdeps) in the `options` object

You’ll still see deprecation warnings if you’re using `/` for division in your own Sass code.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v5/import-css/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Import+CSS%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv5%2Fimport-css%2F%29&labels=bug&title=Re%3A+%27Import+CSS%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
