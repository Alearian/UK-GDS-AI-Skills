#  [](./import-css/#import-css.md)Import CSS
To import the CSS from GOV.UK Frontend, you can either:
  * add GOV.UK Frontend’s CSS file to your HTML
  * import the CSS into your own Sass file

##  [](./import-css/#add-the-css-file-to-your-html.md)Add the CSS file to your HTML
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

##  [](./import-css/#import-using-sass.md)Import using Sass
To import all the Sass rules from GOV.UK Frontend, add the following to your Sass file:

```
@import "node_modules/govuk-frontend/dist/govuk";

```

##  [](./import-css/#import-specific-parts-using-sass.md)Import specific parts using Sass
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

@import "node_modules/govuk-frontend/dist/govuk/core";

// Objects include things like the page template, grid and form groups.
// Approximately 5% of the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/objects";

// The components themselves - try to only include the components you
// are using in your project. Approximately 70% of the CSS output if
// you include everything.

@import "node_modules/govuk-frontend/dist/govuk/components/accordion";
@import "node_modules/govuk-frontend/dist/govuk/components/back-link";
@import "node_modules/govuk-frontend/dist/govuk/components/breadcrumbs";
@import "node_modules/govuk-frontend/dist/govuk/components/button";
@import "node_modules/govuk-frontend/dist/govuk/components/character-count";
@import "node_modules/govuk-frontend/dist/govuk/components/checkboxes";
@import "node_modules/govuk-frontend/dist/govuk/components/cookie-banner";
@import "node_modules/govuk-frontend/dist/govuk/components/date-input";
@import "node_modules/govuk-frontend/dist/govuk/components/details";
@import "node_modules/govuk-frontend/dist/govuk/components/error-message";
@import "node_modules/govuk-frontend/dist/govuk/components/error-summary";
@import "node_modules/govuk-frontend/dist/govuk/components/exit-this-page";
@import "node_modules/govuk-frontend/dist/govuk/components/fieldset";
@import "node_modules/govuk-frontend/dist/govuk/components/file-upload";
@import "node_modules/govuk-frontend/dist/govuk/components/footer";
@import "node_modules/govuk-frontend/dist/govuk/components/header";
@import "node_modules/govuk-frontend/dist/govuk/components/hint";
@import "node_modules/govuk-frontend/dist/govuk/components/input";
@import "node_modules/govuk-frontend/dist/govuk/components/inset-text";
@import "node_modules/govuk-frontend/dist/govuk/components/label";
@import "node_modules/govuk-frontend/dist/govuk/components/notification-banner";
@import "node_modules/govuk-frontend/dist/govuk/components/pagination";
@import "node_modules/govuk-frontend/dist/govuk/components/panel";
@import "node_modules/govuk-frontend/dist/govuk/components/password-input";
@import "node_modules/govuk-frontend/dist/govuk/components/phase-banner";
@import "node_modules/govuk-frontend/dist/govuk/components/radios";
@import "node_modules/govuk-frontend/dist/govuk/components/select";
@import "node_modules/govuk-frontend/dist/govuk/components/service-navigation";
@import "node_modules/govuk-frontend/dist/govuk/components/skip-link";
@import "node_modules/govuk-frontend/dist/govuk/components/summary-list";
@import "node_modules/govuk-frontend/dist/govuk/components/table";
@import "node_modules/govuk-frontend/dist/govuk/components/tabs";
@import "node_modules/govuk-frontend/dist/govuk/components/tag";
@import "node_modules/govuk-frontend/dist/govuk/components/task-list";
@import "node_modules/govuk-frontend/dist/govuk/components/textarea";
@import "node_modules/govuk-frontend/dist/govuk/components/warning-text";

/*
// Alternatively, you can import all components:
@import "node_modules/govuk-frontend/dist/govuk/components";
*/

// Utilities, for example govuk-clearfix or govuk-visually-hidden.
// Approximately 1% of the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/utilities";

// Overrides, used to adjust things like the amount of spacing on an
// element. Override classes always include `-!-` in the class name.
// Approximately 15% of the CSS output if you include everything.

@import "node_modules/govuk-frontend/dist/govuk/overrides";

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
##  [](./import-css/#import-an-individual-component-s-css-using-a-single-sass-import.md)Import an individual component’s CSS using a single Sass import
You can also import a component and all its dependencies without importing `node_modules/govuk-frontend/dist/govuk/base` first.
For example, to import the button component, add the following to your Sass file:

```
@import "node_modules/govuk-frontend/dist/govuk/components/button";

```

We’re deprecating using `_<COMPONENT_NAME>.scss` files (like `node_modules/govuk-frontend/dist/govuk/components/button/button`) and will remove them in the next major release of GOV.UK Frontend.
##  [](./import-css/#simplify-sass-import-paths.md)Simplify Sass import paths
If you want to make Sass import paths shorter, add `node_modules/govuk-frontend/dist` to either your:
  * [Sass load paths](https://sass-lang.com/documentation/at-rules/import#finding-the-file)
  * [assets paths](http://guides.rubyonrails.org/asset_pipeline.html#search-paths) if you use Ruby in your project

You can then import without using `node_modules/govuk-frontend/dist/` in your import path. For example:

```
@import "govuk/components/button/button";

```

##  [](./import-css/#override-with-your-own-css.md)Override with your own CSS
If you want to override GOV.UK Frontend’s styles with your own styles, `@import` GOV.UK Frontend’s styles before your own Sass rules.
##  [](./import-css/#silence-deprecation-warnings-from-dependencies-in-dart-sass.md)Silence deprecation warnings from dependencies in Dart Sass
If you’re using Dart Sass 1.33.0 or greater, you may see deprecation warnings when compiling your Sass. For example:

```
DEPRECATION WARNING: Using / for division is deprecated and will be removed in Dart Sass 2.0.0.

```

You can silence the warnings caused by GOV.UK Frontend and other dependencies. If you’re:
  * calling the Sass compiler from the command line, [pass the `--quiet-deps` flag](https://sass-lang.com/documentation/cli/dart-sass#quiet-deps)
  * using the JavaScript API, [include `quietDeps: true`](https://sass-lang.com/documentation/js-api#quietdeps) in the `options` object

You’ll still see deprecation warnings if you’re using `/` for division in your own Sass code.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/import-css/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Import+CSS%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fimport-css%2F%29&labels=bug&title=Re%3A+%27Import+CSS%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
