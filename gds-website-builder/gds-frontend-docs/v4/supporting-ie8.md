#  [](./v4/supporting-ie8/#support-internet-explorer-8.md)Support Internet Explorer 8
Follow these extra steps if your service needs to support Internet Explorer 8 (IE8):
  1. Include an HTML5 shiv.
  2. Generate an IE8-specific stylesheet.
  3. Transform the IE8 stylesheet using oldie.
  4. Include the IE8 stylesheet in your project.

Once you have completed these steps, you will be able to [write CSS that targets IE8 in your own application styles](./v4/supporting-ie8/#writing-styles-that-target-ie8.md).
If you [installed using precompiled files](./v4/install-using-precompiled-files.md), you can include the IE8-specific stylesheet in your project, allowing you to skip steps 2 and 3.
##  [](./v4/supporting-ie8/#1-include-an-html5-shiv.md)1. Include an HTML5 shiv
You will need to to include an [HTML5 shiv](https://github.com/aFarkas/html5shiv) which allows the ‘semantic’ HTML elements introduced in HTML5 to be used in older browsers which do not natively support them.
These elements include `article`, `aside`, `figcaption`, `figure`, `footer`, `header`, `main`, `mark`, `nav`, `section`, and `time`.
To improve performance for users of modern browsers, you can wrap the shiv include with conditional comments that target only the browsers that need it:

```
<!--[if lt IE 9]>
  <script src="/path/tohtml5shiv.js"></script>
<![endif]-->

```

Note that some libraries such as Modernizr may already include html5shiv.
##  [](./v4/supporting-ie8/#2-generate-an-ie8-specific-stylesheet.md)2. Generate an IE8-specific stylesheet
Setting the `$govuk-is-ie8` variable to `true` when generating the stylesheet will create a version that targets IE8. For example, it will:
  * flatten media queries to create a ‘desktop only’ version
  * include any conditional styles that target IE8
  * exclude any conditional styles that target browsers other than IE8

You must set the variable before importing GOV.UK Frontend.
In most scenarios you should be able to create a separate stylesheet for IE8, set the `$govuk-is-ie8` variable to true and then import your main application stylesheet without having to redefine anything else.

```
// application.scss

@import "govuk-frontend/frontend/all";

.example {
  // example application style
}

// application-ie8.scss

$govuk-is-ie8: true;

@import "application";

```

##  [](./v4/supporting-ie8/#3-transform-the-generated-stylesheet-using-39-oldie-39.md)3. Transform the generated stylesheet using ‘oldie’
You should use the [oldie plugin](https://github.com/jonathantneal/oldie) for [postcss](https://github.com/postcss/postcss) to further transform the stylesheet:
  * replacing opacity properties with compatible filter properties
  * swapping `::` selectors with compatible `:` selectors for pseudo-elements
  * swapping rgba colours with compatible hex colours and filter properties

The oldie plugin is also able to flatten media queries, but this will already have been done as part of the stylesheet compilation in step 1.
Doing this as a separate step allows us to keep the source of GOV.UK Frontend simple, without having to wrap syntax that would need to be transformed in mixins or functions.
##  [](./v4/supporting-ie8/#4-include-the-ie8-stylesheet-in-your-project.md)4. Include the IE8 stylesheet in your project
Now that you have an IE8 compatible stylesheet you should include it using [conditional comments](https://www.quirksmode.org/css/condcom.html):

```
<!--[if !IE 8]><!-->
  <link rel="stylesheet" href="assets/application.css">
<!--<![endif]-->
<!--[if IE 8]>
  <link rel="stylesheet" href="assets/application-ie8.css">
<![endif]-->

```

##  [](./v4/supporting-ie8/#writing-styles-that-target-ie8.md)Writing styles that target IE8
Wrapping rules with the `govuk-if-ie8` mixin will ensure that they are only outputted when generating the IE8-specific stylesheet.

```
.foo {
  min-width: 100px;

  // Specify width for IE8 only
  @include govuk-if-ie8 {
    width: 100px;
  }
}

```

The `govuk-not-ie8` mixin can be used to wrap rules that you want to exclude when generating the IE8-specific stylesheet.

```
.foo {
  font-weight: bold;

  // Enhance foo only for modern browsers (not IE8)
  @include govuk-not-ie8 {
    font-family: "Comic Sans MS", "Curlz MT" cursive, sans-serif;
    color: #FF69B4;
  }
}

```

  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/supporting-ie8/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Support+Internet+Explorer+8+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Fsupporting-ie8%2F%29&labels=bug&title=Re%3A+%27Support+Internet+Explorer+8+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
