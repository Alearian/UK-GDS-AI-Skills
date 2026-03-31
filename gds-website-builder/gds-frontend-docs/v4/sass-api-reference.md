#  [](./v4/sass-api-reference/#sass-api-reference.md)Sass API reference
##  [](./v4/sass-api-reference/#settings.md)Settings
###  [](./v4/sass-api-reference/#assets.md)Assets
####  [](./v4/sass-api-reference/#govuk-assets-path.md)$govuk-assets-path
Path to the assets directory, with trailing slash.
This is the directory where the images and fonts subdirectories live. You will need to make this directory available via your application – see the README for details.
#####  [](./v4/sass-api-reference/#default-value.md)Default value

```
$govuk-assets-path: "/assets/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L14-L14)
####  [](./v4/sass-api-reference/#govuk-images-path.md)$govuk-images-path
Path to the images folder, with trailing slash.
#####  [](./v4/sass-api-reference/#govuk-images-path-default-value.md)Default value

```
$govuk-images-path: "#{$govuk-assets-path}images/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L21-L21)
####  [](./v4/sass-api-reference/#govuk-fonts-path.md)$govuk-fonts-path
Path to the fonts folder, with trailing slash.
#####  [](./v4/sass-api-reference/#govuk-fonts-path-default-value.md)Default value

```
$govuk-fonts-path: "#{$govuk-assets-path}fonts/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L28-L28)
####  [](./v4/sass-api-reference/#govuk-image-url-function.md)$govuk-image-url-function
Custom image URL function
If the built-in image URL helper does not meet your needs, you can specify the name of a custom handler – either built in or by writing your own function.
If you are writing your own handler, ensure that it returns a string wrapped with `url()`
#####  [](./v4/sass-api-reference/#govuk-image-url-function-default-value.md)Default value

```
$govuk-image-url-function: false;

```

#####  [](./v4/sass-api-reference/#example-rails-asset-handling.md)Example: Rails asset handling

```
$govuk-image-url-function: 'image-url';

```

#####  [](./v4/sass-api-reference/#example-custom-asset-handling.md)Example: Custom asset handling

```
@function my-url-handler($filename) {
  // Some custom URL handling
  @return url('example.jpg');
}

$govuk-image-url-function: 'my-url-handler';

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L55-L55)
####  [](./v4/sass-api-reference/#govuk-font-url-function.md)$govuk-font-url-function
Custom font URL function
If the built-in font URL helper does not meet your needs, you can specify the name of a custom handler – either built in or by writing your own function.
If you are writing your own handler, ensure that it returns a string wrapped with `url()`
#####  [](./v4/sass-api-reference/#govuk-font-url-function-default-value.md)Default value

```
$govuk-font-url-function: false;

```

#####  [](./v4/sass-api-reference/#govuk-font-url-function-example-rails-asset-handling.md)Example: Rails asset handling

```
$govuk-font-url-function: 'font-url';

```

#####  [](./v4/sass-api-reference/#govuk-font-url-function-example-custom-asset-handling.md)Example: Custom asset handling

```
@function my-url-handler($filename) {
  // Some custom URL handling
  @return url('example.woff');
}

$govuk-font-url-function: 'my-url-handler';

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L82-L82)
###  [](./v4/sass-api-reference/#colours.md)Colours
####  [](./v4/sass-api-reference/#govuk-brand-colour.md)$govuk-brand-colour
Brand colour
#####  [](./v4/sass-api-reference/#govuk-brand-colour-default-value.md)Default value

```
$govuk-brand-colour: govuk-colour("blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L16-L16)
####  [](./v4/sass-api-reference/#govuk-text-colour.md)$govuk-text-colour
Text colour
#####  [](./v4/sass-api-reference/#govuk-text-colour-default-value.md)Default value

```
$govuk-text-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L23-L23)
####  [](./v4/sass-api-reference/#govuk-canvas-background-colour.md)$govuk-canvas-background-colour
Canvas background colour
Used by the footer component and template to give the illusion of a long footer.
#####  [](./v4/sass-api-reference/#govuk-canvas-background-colour-default-value.md)Default value

```
$govuk-canvas-background-colour: govuk-colour("light-grey", $legacy: "grey-3");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L33-L33)
####  [](./v4/sass-api-reference/#govuk-body-background-colour.md)$govuk-body-background-colour
Body background colour
#####  [](./v4/sass-api-reference/#govuk-body-background-colour-default-value.md)Default value

```
$govuk-body-background-colour: govuk-colour("white");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L40-L40)
####  [](./v4/sass-api-reference/#govuk-print-text-colour.md)$govuk-print-text-colour
Text colour for print media
Use ‘true black’ to avoid printers using colour ink to print body text
#####  [](./v4/sass-api-reference/#govuk-print-text-colour-default-value.md)Default value

```
$govuk-print-text-colour: #000000;

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L49-L49)
####  [](./v4/sass-api-reference/#govuk-secondary-text-colour.md)$govuk-secondary-text-colour
Secondary text colour
Used in for example ‘muted’ text and help text.
#####  [](./v4/sass-api-reference/#govuk-secondary-text-colour-default-value.md)Default value

```
$govuk-secondary-text-colour: govuk-colour("dark-grey", $legacy: "grey-1");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L58-L58)
####  [](./v4/sass-api-reference/#govuk-focus-colour.md)$govuk-focus-colour
Focus colour
Used for outline (and background, where appropriate) when interactive elements (links, form controls) have keyboard focus.
#####  [](./v4/sass-api-reference/#govuk-focus-colour-default-value.md)Default value

```
$govuk-focus-colour: govuk-colour("yellow");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L68-L68)
####  [](./v4/sass-api-reference/#govuk-focus-text-colour.md)$govuk-focus-text-colour
Focused text colour
Ensure that the contrast between the text and background colour passes WCAG Level AA contrast requirements.
#####  [](./v4/sass-api-reference/#govuk-focus-text-colour-default-value.md)Default value

```
$govuk-focus-text-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L78-L78)
####  [](./v4/sass-api-reference/#govuk-error-colour.md)$govuk-error-colour
Error colour
Used to highlight error messages and form controls in an error state
#####  [](./v4/sass-api-reference/#govuk-error-colour-default-value.md)Default value

```
$govuk-error-colour: govuk-colour("red");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L87-L87)
####  [](./v4/sass-api-reference/#govuk-success-colour.md)$govuk-success-colour
Success colour
Used to highlight success messages and banners
#####  [](./v4/sass-api-reference/#govuk-success-colour-default-value.md)Default value

```
$govuk-success-colour: govuk-colour("green");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L96-L96)
####  [](./v4/sass-api-reference/#govuk-border-colour.md)$govuk-border-colour
Border colour
Used in for example borders, separators, rules and keylines.
#####  [](./v4/sass-api-reference/#govuk-border-colour-default-value.md)Default value

```
$govuk-border-colour: govuk-colour("mid-grey", $legacy: "grey-2");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L105-L105)
####  [](./v4/sass-api-reference/#govuk-input-border-colour.md)$govuk-input-border-colour
Input border colour
Used for form inputs and controls
#####  [](./v4/sass-api-reference/#govuk-input-border-colour-default-value.md)Default value

```
$govuk-input-border-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L114-L114)
####  [](./v4/sass-api-reference/#govuk-hover-colour.md)$govuk-hover-colour
Input hover colour
Used for hover states on form controls
#####  [](./v4/sass-api-reference/#govuk-hover-colour-default-value.md)Default value

```
$govuk-hover-colour: govuk-colour("mid-grey", $legacy: "grey-3");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L123-L123)
####  [](./v4/sass-api-reference/#govuk-link-colour.md)$govuk-link-colour
Link colour
#####  [](./v4/sass-api-reference/#govuk-link-colour-default-value.md)Default value

```
$govuk-link-colour: govuk-colour("blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L134-L134)
####  [](./v4/sass-api-reference/#govuk-link-visited-colour.md)$govuk-link-visited-colour
Visited link colour
#####  [](./v4/sass-api-reference/#govuk-link-visited-colour-default-value.md)Default value

```
$govuk-link-visited-colour: govuk-colour("purple", $legacy: #4c2c92);

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L141-L141)
####  [](./v4/sass-api-reference/#govuk-link-hover-colour.md)$govuk-link-hover-colour
Link hover colour
#####  [](./v4/sass-api-reference/#govuk-link-hover-colour-default-value.md)Default value

```
$govuk-link-hover-colour: govuk-colour("dark-blue", $legacy: "light-blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L148-L148)
####  [](./v4/sass-api-reference/#govuk-link-active-colour.md)$govuk-link-active-colour
Active link colour
#####  [](./v4/sass-api-reference/#govuk-link-active-colour-default-value.md)Default value

```
$govuk-link-active-colour: govuk-colour("black", $legacy: "light-blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L155-L155)
####  [](./v4/sass-api-reference/#govuk-colours-organisations.md)$govuk-colours-organisations
Organisation colours
#####  [](./v4/sass-api-reference/#govuk-colours-organisations-default-value.md)Default value

```
$govuk-colours-organisations: (
  "attorney-generals-office": (
    colour: #9f1888,
    colour-websafe: #a03a88
  ),
  "cabinet-office": (
    colour: #005abb,
    colour-websafe: #347da4
  ),
  "civil-service": (
    colour: #af292e
  ),
  "department-for-business-innovation-skills": (
    colour: #003479,
    colour-websafe: #347da4
  ),
  "department-for-communities-and-local-government": (
    colour: #009999,
    colour-websafe: #37836e
  ),
  "department-for-culture-media-sport": (
    colour: #d40072,
    colour-websafe: #a03155
  ),
  "department-for-education": (
    colour: #003a69,
    colour-websafe: #347ca9
  ),
  "department-for-environment-food-rural-affairs": (
    colour: #00a33b,
    colour-websafe: #008938
  ),
  "department-for-international-development": (
    colour: #002878,
    colour-websafe: #405e9a
  ),
  "department-for-international-trade": (
    colour: #cf102d,
    colour-websafe: #005ea5
  ),
  "department-for-business-and-trade": (
    colour: #cf102d,
    colour-websafe: #005ea5
  ),
  "department-for-levelling-up-housing-and-communities": (
    colour: #012169,
  ),
  "department-for-transport": (
    colour: #006c56,
    colour-websafe: #398373
  ),
  "department-for-work-pensions": (
    colour: #00beb7,
    colour-websafe: #37807b
  ),
  "department-of-energy-climate-change": (
    colour: #009ddb,
    colour-websafe: #2b7cac
  ),
  "department-of-health": (
    colour: #00ad93,
    colour-websafe: #39836e
  ),
  "foreign-commonwealth-development-office": (
    colour: #012169
  ),
  "foreign-commonwealth-office": (
    colour: #003e74,
    colour-websafe: #406e97
  ),
  "government-equalities-office": (
    colour:  #9325b2
  ),
  "hm-government": (
    colour: #0076c0,
    colour-websafe: #347da4
  ),
  "hm-revenue-customs": (
    colour: #009390,
    colour-websafe: #008670
  ),
  "hm-treasury": (
    colour: #af292e,
    colour-websafe: #832322
  ),
  "home-office": (
    colour: #9325b2,
    colour-websafe: #9440b2
  ),
  "ministry-of-defence": (
    colour: #4d2942,
    colour-websafe: #5a5c92
  ),
  "ministry-of-justice": (
    colour: #231f20,
    colour-websafe: #5a5c92
  ),
  "northern-ireland-office": (
    colour: #002663,
    colour-websafe: #3e598c
  ),
  "office-of-the-advocate-general-for-scotland": (
    colour: #002663,
    colour-websafe: #005ea5
  ),
  "office-of-the-leader-of-the-house-of-commons": (
    colour: #317023,
    colour-websafe: #005f8f
  ),
  "office-of-the-leader-of-the-house-of-lords": (
    colour: #9c132e,
    colour-websafe: #c2395d
  ),
  "scotland-office": (
    colour: #002663,
    colour-websafe: #405c8a
  ),
  "uk-export-finance": (
    colour: #005747,
    colour-websafe: #005ea5
  ),
  "uk-trade-investment": (
    colour: #c80651,
    colour-websafe: #005ea5
  ),
  "wales-office": (
    colour: #a33038,
    colour-websafe: #7a242a
  )
);

```

[ View source code for _colours-organisations.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-organisations.scss#L17-L146)
####  [](./v4/sass-api-reference/#govuk-use-legacy-palette.md)$govuk-use-legacy-palette
Use ‘legacy’ colour palette
Whether or not to use the colour palette from GOV.UK Elements / Frontend Toolkit, for teams that are migrating to GOV.UK Frontend and may be using components from both places in a single application.
#####  [](./v4/sass-api-reference/#usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-use-legacy-palette-default-value.md)Default value

```
$govuk-use-legacy-palette: if(
  (
    $govuk-compatibility-govukfrontendtoolkit or
    $govuk-compatibility-govuktemplate or
    $govuk-compatibility-govukelements
  ),
  true,
  false
);

```

[ View source code for _colours-palette.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-palette.scss#L21-L29)
####  [](./v4/sass-api-reference/#govuk-colours.md)$govuk-colours
Colour palette
#####  [](./v4/sass-api-reference/#govuk-colours-default-value.md)Default value

```
$govuk-colours: if(
  $govuk-use-legacy-palette,
  $_govuk-colour-palette-legacy,
  $_govuk-colour-palette-modern
);

```

[ View source code for _colours-palette.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-palette.scss#L116-L120)
###  [](./v4/sass-api-reference/#compatibility.md)Compatibility
####  [](./v4/sass-api-reference/#govuk-compatibility-govukfrontendtoolkit.md)$govuk-compatibility-govukfrontendtoolkit
Compatibility Mode: alphagov/govuk_frontend_toolkit
Set this to true if you are also including alphagov/govuk_frontend_toolkit in your application.
#####  [](./v4/sass-api-reference/#govuk-compatibility-govukfrontendtoolkit-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-compatibility-govukfrontendtoolkit-default-value.md)Default value

```
$govuk-compatibility-govukfrontendtoolkit: false;

```

[ View source code for _compatibility.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_compatibility.scss#L29-L29)
####  [](./v4/sass-api-reference/#govuk-compatibility-govuktemplate.md)$govuk-compatibility-govuktemplate
Compatibility Mode: alphagov/govuk_template
Enabling this will:
  * prevent GOV.UK Frontend from including the New Transport typeface, as it’ll use the version of New Transport included with GOV.UK Template.
  * alter some of the CSS outputted by GOV.UK Frontend to ‘counter’ specific CSS rules in GOV.UK Template.

Set this to true if you are also including alphagov/govuk_template in your application.
#####  [](./v4/sass-api-reference/#govuk-compatibility-govuktemplate-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-compatibility-govuktemplate-default-value.md)Default value

```
$govuk-compatibility-govuktemplate: false;

```

[ View source code for _compatibility.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_compatibility.scss#L55-L55)
####  [](./v4/sass-api-reference/#govuk-compatibility-govukelements.md)$govuk-compatibility-govukelements
Compatibility Mode: alphagov/govuk_elements
Enabling this will:
  * alter some of the CSS outputted by GOV.UK Frontend to ‘counter’ specific CSS rules in GOV.UK Elements.

Set this to true if you are also including alphagov/govuk_elements in your application.
#####  [](./v4/sass-api-reference/#govuk-compatibility-govukelements-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-compatibility-govukelements-default-value.md)Default value

```
$govuk-compatibility-govukelements: false;

```

[ View source code for _compatibility.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_compatibility.scss#L78-L78)
###  [](./v4/sass-api-reference/#global-styles.md)Global styles
####  [](./v4/sass-api-reference/#govuk-global-styles.md)$govuk-global-styles
Include ‘global’ styles
Whether to style paragraphs (`<p>`) and links (`<a>`) without explicitly having to apply the `govuk-body` and `govuk-link` classes.
#####  [](./v4/sass-api-reference/#govuk-global-styles-default-value.md)Default value

```
$govuk-global-styles: false;

```

[ View source code for _global-styles.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_global-styles.scss#L13-L13)
###  [](./v4/sass-api-reference/#internet-explorer-8.md)Internet explorer 8
####  [](./v4/sass-api-reference/#govuk-is-ie8.md)$govuk-is-ie8
Whether the stylesheet being built is targeting Internet Explorer 8.
#####  [](./v4/sass-api-reference/#govuk-is-ie8-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0
**
#####  [](./v4/sass-api-reference/#govuk-is-ie8-default-value.md)Default value

```
$govuk-is-ie8: false;

```

[ View source code for _ie8.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_ie8.scss#L11-L11)
####  [](./v4/sass-api-reference/#govuk-ie8-breakpoint.md)$govuk-ie8-breakpoint
The name of the breakpoint to use as the target when rasterizing media queries
#####  [](./v4/sass-api-reference/#govuk-ie8-breakpoint-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0
**
#####  [](./v4/sass-api-reference/#govuk-ie8-breakpoint-default-value.md)Default value

```
$govuk-ie8-breakpoint: desktop;

```

[ View source code for _ie8.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_ie8.scss#L27-L27)
###  [](./v4/sass-api-reference/#links.md)Links
####  [](./v4/sass-api-reference/#govuk-new-link-styles.md)$govuk-new-link-styles
Enable new link styles
If enabled, the link styles will change. Underlines will:
  * be consistently thinner and a bit further away from the link text
  * have a clearer hover state, where the underline gets thicker to make the link stand out to users

You should only enable the new link styles if both:
  * you’ve made sure your whole service will use the new style consistently
  * you do not have links in a multi-column CSS layout - there’s [a Chromium bug that affects links](https://github.com/alphagov/govuk-frontend/issues/2204)

#####  [](./v4/sass-api-reference/#govuk-new-link-styles-default-value.md)Default value

```
$govuk-new-link-styles: false;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L22-L22)
####  [](./v4/sass-api-reference/#govuk-link-underline-thickness.md)$govuk-link-underline-thickness
Thickness of link underlines
The default will be either:
  * 1px
  * 0.0625rem, if it’s thicker than 1px because the user has changed the text size in their browser

Set this variable to `false` to avoid setting a thickness.
#####  [](./v4/sass-api-reference/#govuk-link-underline-thickness-default-value.md)Default value

```
$govuk-link-underline-thickness: unquote("max(1px, .0625rem)");

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L37-L37)
####  [](./v4/sass-api-reference/#govuk-link-underline-offset.md)$govuk-link-underline-offset
Offset of link underlines from text baseline
The default is 3px expressed as ems, as calculated against the default body font size (on desktop) of 19px. 3 ÷ 19 = 0.1578
Set this variable to `false` to avoid setting an offset.
#####  [](./v4/sass-api-reference/#govuk-link-underline-offset-default-value.md)Default value

```
$govuk-link-underline-offset: .1578em;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L50-L50)
####  [](./v4/sass-api-reference/#govuk-link-hover-underline-thickness.md)$govuk-link-hover-underline-thickness
Thickness of link underlines in hover state
The default for each link will be the thickest of the following:
  * 3px
  * 0.1875rem, if it’s thicker than 3px because the user has changed the text size in their browser
  * 0.12em (relative to the link’s text size)

Set this variable to `false` to avoid setting a thickness.
#####  [](./v4/sass-api-reference/#govuk-link-hover-underline-thickness-default-value.md)Default value

```
$govuk-link-hover-underline-thickness: unquote("max(3px, .1875rem, .12em)");

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L66-L66)
###  [](./v4/sass-api-reference/#measurements.md)Measurements
####  [](./v4/sass-api-reference/#govuk-page-width.md)$govuk-page-width
Width of main container
#####  [](./v4/sass-api-reference/#govuk-page-width-default-value.md)Default value

```
$govuk-page-width: 960px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L14-L14)
####  [](./v4/sass-api-reference/#govuk-grid-widths.md)$govuk-grid-widths
Map of grid column widths
#####  [](./v4/sass-api-reference/#govuk-grid-widths-default-value.md)Default value

```
$govuk-grid-widths: (
  one-quarter: (100% / 4),
  one-third: (100% / 3),
  one-half: (100% / 2),
  two-thirds: (200% / 3),
  three-quarters: (300% / 4),
  full: 100%
);

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L21-L28)
####  [](./v4/sass-api-reference/#govuk-gutter.md)$govuk-gutter
Width of gutter between grid columns
#####  [](./v4/sass-api-reference/#govuk-gutter-default-value.md)Default value

```
$govuk-gutter: 30px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L35-L35)
####  [](./v4/sass-api-reference/#govuk-gutter-half.md)$govuk-gutter-half
Width of half the gutter between grid columns
#####  [](./v4/sass-api-reference/#govuk-gutter-half-default-value.md)Default value

```
$govuk-gutter-half: $govuk-gutter / 2;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L42-L42)
####  [](./v4/sass-api-reference/#govuk-border-width.md)$govuk-border-width
Standard border width
#####  [](./v4/sass-api-reference/#govuk-border-width-default-value.md)Default value

```
$govuk-border-width: 5px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L53-L53)
####  [](./v4/sass-api-reference/#govuk-border-width-wide.md)$govuk-border-width-wide
Wide border width
#####  [](./v4/sass-api-reference/#govuk-border-width-wide-default-value.md)Default value

```
$govuk-border-width-wide: 10px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L60-L60)
####  [](./v4/sass-api-reference/#govuk-border-width-narrow.md)$govuk-border-width-narrow
Narrow border width
#####  [](./v4/sass-api-reference/#govuk-border-width-narrow-default-value.md)Default value

```
$govuk-border-width-narrow: 4px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L67-L67)
####  [](./v4/sass-api-reference/#govuk-border-width-form-element.md)$govuk-border-width-form-element
Form control border width
#####  [](./v4/sass-api-reference/#govuk-border-width-form-element-default-value.md)Default value

```
$govuk-border-width-form-element: 2px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L74-L74)
####  [](./v4/sass-api-reference/#govuk-border-width-form-group-error.md)$govuk-border-width-form-group-error
Form group border width when in error state
#####  [](./v4/sass-api-reference/#govuk-border-width-form-group-error-default-value.md)Default value

```
$govuk-border-width-form-group-error: $govuk-border-width;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L81-L81)
####  [](./v4/sass-api-reference/#govuk-focus-width.md)$govuk-focus-width
Border width of focus outline
#####  [](./v4/sass-api-reference/#govuk-focus-width-default-value.md)Default value

```
$govuk-focus-width: 3px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L88-L88)
####  [](./v4/sass-api-reference/#govuk-hover-width.md)$govuk-hover-width
Hover width for form controls with a hover state
#####  [](./v4/sass-api-reference/#govuk-hover-width-default-value.md)Default value

```
$govuk-hover-width: 10px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L95-L95)
###  [](./v4/sass-api-reference/#media-queries.md)Media queries
####  [](./v4/sass-api-reference/#govuk-breakpoints.md)$govuk-breakpoints
Breakpoint definitions
#####  [](./v4/sass-api-reference/#govuk-breakpoints-default-value.md)Default value

```
$govuk-breakpoints: (
  mobile:  320px,
  tablet:  641px,
  desktop: 769px
);

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_media-queries.scss#L10-L14)
####  [](./v4/sass-api-reference/#govuk-show-breakpoints.md)$govuk-show-breakpoints
Show active breakpoint in top-right corner.
Only use this during local development.
#####  [](./v4/sass-api-reference/#govuk-show-breakpoints-default-value.md)Default value

```
$govuk-show-breakpoints: false;

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_media-queries.scss#L23-L23)
###  [](./v4/sass-api-reference/#typography.md)Typography
####  [](./v4/sass-api-reference/#govuk-font-family-gds-transport.md)$govuk-font-family-gds-transport
List of font families to use if using GDS Transport (the default font ‘stack’ for GOV.UK)
#####  [](./v4/sass-api-reference/#govuk-font-family-gds-transport-default-value.md)Default value

```
$govuk-font-family-gds-transport: "GDS Transport", arial, sans-serif;

```

[ View source code for _typography-font-families.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font-families.scss#L11-L11)
####  [](./v4/sass-api-reference/#govuk-font-family-nta.md)$govuk-font-family-nta
List of font families to use if using NTA (old font ‘stack’ for GOV.UK)
#####  [](./v4/sass-api-reference/#govuk-font-family-nta-usage.md)Usage
! ** Warning
Deprecated: To be removed once support for compatibility mode is dropped
**
#####  [](./v4/sass-api-reference/#govuk-font-family-nta-default-value.md)Default value

```
$govuk-font-family-nta: "nta", arial, sans-serif;

```

[ View source code for _typography-font-families.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font-families.scss#L20-L20)
####  [](./v4/sass-api-reference/#govuk-font-family-nta-tabular.md)$govuk-font-family-nta-tabular
List of font families to use if using the ‘tabular numbers’ subset of NTA (the default font ‘stack’ for GOV.UK)
Because ntatabularnumbers only includes the digits 0-10, all other glyphs will ‘fall-through’ the stack to NTA.
#####  [](./v4/sass-api-reference/#govuk-font-family-nta-tabular-usage.md)Usage
! ** Warning
Deprecated: To be removed once support for compatibility mode is dropped
**
#####  [](./v4/sass-api-reference/#govuk-font-family-nta-tabular-default-value.md)Default value

```
$govuk-font-family-nta-tabular: "ntatabularnumbers", $govuk-font-family-nta;

```

[ View source code for _typography-font-families.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font-families.scss#L32-L32)
####  [](./v4/sass-api-reference/#govuk-use-legacy-font.md)$govuk-use-legacy-font
Use ‘legacy’ fonts
Whether or not to use v1 nta font from GOV.UK Elements / Frontend Toolkit, for teams that are migrating to GOV.UK Frontend and may be using components from both places in a single application.
#####  [](./v4/sass-api-reference/#govuk-use-legacy-font-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-use-legacy-font-default-value.md)Default value

```
$govuk-use-legacy-font: if(
  (
    $govuk-compatibility-govukfrontendtoolkit or
    $govuk-compatibility-govuktemplate or
    $govuk-compatibility-govukelements
  ),
  true,
  false
);

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L19-L27)
####  [](./v4/sass-api-reference/#govuk-font-family.md)$govuk-font-family
Font families to use for all typography on screen media
#####  [](./v4/sass-api-reference/#govuk-font-family-default-value.md)Default value

```
$govuk-font-family: if(
  $govuk-use-legacy-font,
  $govuk-font-family-nta,
  $govuk-font-family-gds-transport
);

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L49-L53)
####  [](./v4/sass-api-reference/#govuk-font-family-tabular.md)$govuk-font-family-tabular
Font families to use when displaying tabular numbers
#####  [](./v4/sass-api-reference/#govuk-font-family-tabular-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-font-family-tabular-default-value.md)Default value

```
$govuk-font-family-tabular: if(
  $govuk-use-legacy-font,
  $govuk-font-family-nta-tabular,
  false
);

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L62-L66)
####  [](./v4/sass-api-reference/#govuk-font-family-print.md)$govuk-font-family-print
Font families to use for print media
We recommend that you use system fonts when printing. This will avoid issues with some printer drivers and operating systems.
#####  [](./v4/sass-api-reference/#govuk-font-family-print-default-value.md)Default value

```
$govuk-font-family-print: sans-serif;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L84-L84)
####  [](./v4/sass-api-reference/#govuk-include-default-font-face.md)$govuk-include-default-font-face
Include the default @font-face declarations
If you have set $govuk-font-family to something other than `$govuk-font-family-gds-transport` this option is disabled by default.
#####  [](./v4/sass-api-reference/#govuk-include-default-font-face-default-value.md)Default value

```
$govuk-include-default-font-face: (
  $govuk-font-family == $govuk-font-family-gds-transport
);

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L94-L96)
####  [](./v4/sass-api-reference/#govuk-font-weight-regular.md)$govuk-font-weight-regular
Font weight for regular typography
#####  [](./v4/sass-api-reference/#govuk-font-weight-regular-default-value.md)Default value

```
$govuk-font-weight-regular: 400;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L106-L106)
####  [](./v4/sass-api-reference/#govuk-font-weight-bold.md)$govuk-font-weight-bold
Font weight for bold typography
#####  [](./v4/sass-api-reference/#govuk-font-weight-bold-default-value.md)Default value

```
$govuk-font-weight-bold: 700;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L112-L112)
####  [](./v4/sass-api-reference/#govuk-typography-use-rem.md)$govuk-typography-use-rem
Whether or not to define font sizes in rem, improving accessibility by allowing users to adjust the base font-size. This is enabled by default, unless any of the compatibility mode settings are enabled.
You should make sure that $govuk-root-font-size is set correctly for your project.
#####  [](./v4/sass-api-reference/#govuk-typography-use-rem-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**
#####  [](./v4/sass-api-reference/#govuk-typography-use-rem-default-value.md)Default value

```
$govuk-typography-use-rem: if(
  (
    $govuk-compatibility-govukfrontendtoolkit or
    $govuk-compatibility-govuktemplate or
    $govuk-compatibility-govukelements
  ),
  false,
  true
);

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L19-L27)
####  [](./v4/sass-api-reference/#govuk-root-font-size.md)$govuk-root-font-size
Root font size
This is used to calculate rem sizes for the typography, and should match the _effective_ font-size of your root (or html) element.
Ideally you should not be setting the font-size on the html or root element in order to allow it to scale with user-preference, in which case this should be set to 16px.
If you are integrating Frontend into an existing project that also uses alphagov/govuk_template and you wish to enable `$govuk-typography-use-rem` then you should set this to 10px to match the 62.5% (10px) base font size that govuk_template sets on the element.
#####  [](./v4/sass-api-reference/#govuk-root-font-size-default-value.md)Default value

```
$govuk-root-font-size: 16px;

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L56-L56)
####  [](./v4/sass-api-reference/#govuk-typography-scale.md)$govuk-typography-scale
Responsive typography font map
This is used to generate responsive typography that adapts according to the breakpoints.
Font size and font weight can be defined for each breakpoint. You can define different behaviour on tablet and desktop. The ‘null’ breakpoint is for mobile.
Line-heights will automatically be converted from pixel measurements into relative values. For example, with a font-size of 16px and a line-height of 24px, the line-height will be converted to 1.5 before output.
You can also specify a separate font size and line height for print media.
#####  [](./v4/sass-api-reference/#govuk-typography-scale-default-value.md)Default value

```
$govuk-typography-scale: (
  80: (
    null: (
      font-size: 53px,
      line-height: 55px
    ),
    tablet: (
      font-size: 80px,
      line-height: 80px
    ),
    print: (
      font-size: 53pt,
      line-height: 1.1
    )
  ),
  48: (
    null: (
      font-size: 32px,
      line-height: 35px
    ),
    tablet: (
      font-size: 48px,
      line-height: 50px
    ),
    print: (
      font-size: 32pt,
      line-height: 1.15
    )
  ),
  36: (
    null: (
      font-size: 24px,
      line-height: 25px
    ),
    tablet: (
      font-size: 36px,
      line-height: 40px
    ),
    print: (
      font-size: 24pt,
      line-height: 1.05
    )
  ),
  27: (
    null: (
      font-size: 18px,
      line-height: 20px
    ),
    tablet: (
      font-size: 27px,
      line-height: 30px
    ),
    print: (
      font-size: 18pt,
      line-height: 1.15
    )
  ),
  24: (
    null: (
      font-size: 18px,
      line-height: 20px
    ),
    tablet: (
      font-size: 24px,
      line-height: 30px
    ),
    print: (
      font-size: 18pt,
      line-height: 1.15
    )
  ),
  19: (
    null: (
      font-size: 16px,
      line-height: 20px
    ),
    tablet: (
      font-size: 19px,
      line-height: 25px
    ),
    print: (
      font-size: 14pt,
      line-height: 1.15
    )
  ),
  16: (
    null: (
      font-size: 14px,
      line-height: 16px
    ),
    tablet: (
      font-size: 16px,
      line-height: 20px
    ),
    print: (
      font-size: 14pt,
      line-height: 1.2
    )
  ),
  14: (
    null: (
      font-size: 12px,
      line-height: 15px
    ),
    tablet: (
      font-size: 14px,
      line-height: 20px
    ),
    print: (
      font-size: 12pt,
      line-height: 1.2
    )
  )
);

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L82-L195)
###  [](./v4/sass-api-reference/#warnings.md)Warnings
####  [](./v4/sass-api-reference/#govuk-suppressed-warnings.md)$govuk-suppressed-warnings
Suppressed warnings map
This map is used to determine which deprecation warnings to **not** show to users when compiling sass. This is in place for codebases that do not have the necessary capacity to upgrade and remove the deprecation, particularly if the deprecation is significant. For example, removal of compatibility with legacy libraries such as govuk_elements.
You can add to this map and define which warnings to suppress by appending to it using the warning key, found in the warning message. For example:
#####  [](./v4/sass-api-reference/#govuk-suppressed-warnings-default-value.md)Default value

```
$govuk-suppressed-warnings: ();

```

#####  [](./v4/sass-api-reference/#example.md)Example: :

```
// warning message:
//  $foobar is no longer supported. To silence this warning, update
//  $govuk-suppressed-warnings with key: "foobar"
$govuk-suppressed-warnings: (
  foobar
);

```

[ View source code for _warnings.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_warnings.scss#L27-L27)
##  [](./v4/sass-api-reference/#tools.md)Tools
###  [](./v4/sass-api-reference/#general-tools.md)General tools
####  [](./v4/sass-api-reference/#govuk-exports.md)govuk-exports
Export module
Ensure that the modules of CSS that we define throughout Frontend are only included in the generated CSS once, no matter how many times they are imported across the individual components.
#####  [](./v4/sass-api-reference/#parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$name`  | Name of module - must be unique within the codebase  | `String`  | —  |  
#####  [](./v4/sass-api-reference/#govuk-exports-usage.md)Usage

```
@include govuk-exports($name) {
  //..
}

```

[ View source code for _exports.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_exports.scss#L23-L33)
###  [](./v4/sass-api-reference/#tools-assets.md)Assets
####  [](./v4/sass-api-reference/#govuk-font-url.md)govuk-font-url
Font URL
If a custom font-url handler is defined ($govuk-font-url-function) then it will be called, otherwise a url will be returned with the filename appended to the font path.
#####  [](./v4/sass-api-reference/#govuk-font-url-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$filename`  | Font filename  | `String`  | —  |  
[ View source code for _font-url.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_font-url.scss#L15-L25)
####  [](./v4/sass-api-reference/#govuk-image-url.md)govuk-image-url
Image URL
If a custom image-url handler is defined ($govuk-image-url-function) then it will be called, otherwise a url will be returned with the filename appended to the image path.
#####  [](./v4/sass-api-reference/#govuk-image-url-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$Filename`  | for the image to load  | `String`  | —  |  
[ View source code for _image-url.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_image-url.scss#L15-L25)
###  [](./v4/sass-api-reference/#compatibility-mode.md)Compatibility mode
####  [](./v4/sass-api-reference/#govuk-compatibility.md)govuk-compatibility
Conditional Compatibility Mixin
Selectively output a block (available to the mixin as @content) if a given $product is also identified as being used in the project.
This can then be used to include styles that are only needed to override styles provided by those other products (e.g. where govuk_template has a very specific link selector that otherwise affects buttons).
#####  [](./v4/sass-api-reference/#govuk-compatibility-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$product`  | Name of product that we are ‘defending’ against.  | `String`  | —  |  
#####  [](./v4/sass-api-reference/#govuk-compatibility-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0 with the rest of the compatibility mode suite of tools and settings
**

```
@include govuk-compatibility($product) {
  //..
}

```

#####  [](./v4/sass-api-reference/#govuk-compatibility-example.md)Example

```
// Override .my-class if GOV.UK Template is also being used
@include govuk-compatibility(govuk_template) {
  .my-class {
    color: inherit;
  }
}

```

[ View source code for _compatibility.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_compatibility.scss#L44-L50)
###  [](./v4/sass-api-reference/#tools-internet-explorer-8.md)Internet explorer 8
####  [](./v4/sass-api-reference/#govuk-if-ie8.md)govuk-if-ie8
Conditionally include rules only for IE8
#####  [](./v4/sass-api-reference/#govuk-if-ie8-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0
**

```
@include govuk-if-ie8 {
  //..
}

```

#####  [](./v4/sass-api-reference/#example-usage.md)Example: Usage

```
.foo {
  min-width: 100px;
  // Specify width for IE8 only
  @include govuk-if-ie8 {
    width: 100px;
  }
}

```

[ View source code for _ie8.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_ie8.scss#L36-L45)
####  [](./v4/sass-api-reference/#govuk-not-ie8.md)govuk-not-ie8
Conditionally exclude rules for IE8
#####  [](./v4/sass-api-reference/#govuk-not-ie8-usage.md)Usage
! ** Warning
Deprecated: Will be removed in v5.0
**

```
@include govuk-not-ie8 {
  //..
}

```

#####  [](./v4/sass-api-reference/#govuk-not-ie8-example-usage.md)Example: Usage

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

[ View source code for _ie8.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_ie8.scss#L78-L87)
###  [](./v4/sass-api-reference/#unit-conversion.md)Unit conversion
####  [](./v4/sass-api-reference/#govuk-em.md)govuk-em
Convert pixels to em
#####  [](./v4/sass-api-reference/#govuk-em-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | Length in pixels  | `Number`  | —  |  
|  `$context-font-size`  | Font size of element  | `Number`  | —  |  
[ View source code for _px-to-em.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_px-to-em.scss#L12-L20)
####  [](./v4/sass-api-reference/#govuk-px-to-rem.md)govuk-px-to-rem
Convert pixels to rem
The $govuk-root-font-size (defined in settings/_typography-responsive.scss) must be configured to match the font-size of your root (html) element
#####  [](./v4/sass-api-reference/#govuk-px-to-rem-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | Length in pixels  | `Number`  | —  |  
[ View source code for _px-to-rem.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_px-to-rem.scss#L14-L20)
##  [](./v4/sass-api-reference/#helpers.md)Helpers
###  [](./v4/sass-api-reference/#general-helpers.md)General helpers
####  [](./v4/sass-api-reference/#govuk-device-pixel-ratio.md)govuk-device-pixel-ratio
Media query for retina images (device-pixel-ratio)
#####  [](./v4/sass-api-reference/#govuk-device-pixel-ratio-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$ratio`  | Device pixel ratio  | `Number`  | `2`  |  
#####  [](./v4/sass-api-reference/#govuk-device-pixel-ratio-usage.md)Usage

```
@include govuk-device-pixel-ratio($ratio: 2) {
  //..
}

```

#####  [](./v4/sass-api-reference/#example-providing-a-2x-image-for-screens-that-support-it.md)Example: Providing a @2x image for screens that support it

```
background-image: govuk-image-url("my-image.png");

@include govuk-device-pixel-ratio {
  background-image: govuk-image-url("my-image-2x.png");
}

```

#####  [](./v4/sass-api-reference/#example-using-a-custom-ratio.md)Example: Using a custom ratio

```
background-image: govuk-image-url("my-image.png");

@include govuk-device-pixel-ratio {
  background-image: govuk-image-url("my-image-2x.png");
}

@include govuk-device-pixel-ratio(3) {
  background-image: govuk-image-url("my-image-3x.png");
}

```

[ View source code for _device-pixels.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_device-pixels.scss#L30-L37)
###  [](./v4/sass-api-reference/#accessibility.md)Accessibility
####  [](./v4/sass-api-reference/#govuk-focused-text.md)govuk-focused-text
Focused text
Provides an outline to clearly indicate when the target element is focused. Used for interactive text-based elements.
#####  [](./v4/sass-api-reference/#govuk-focused-text-usage.md)Usage

```
@include govuk-focused-text;

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L12-L33)
####  [](./v4/sass-api-reference/#govuk-visually-hidden.md)govuk-visually-hidden
Hide an element visually, but have it available for screen readers
#####  [](./v4/sass-api-reference/#govuk-visually-hidden-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `true`  |  
#####  [](./v4/sass-api-reference/#govuk-visually-hidden-usage.md)Usage

```
@include govuk-visually-hidden($important: true);

```

[ View source code for _visually-hidden.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_visually-hidden.scss#L16-L49)
####  [](./v4/sass-api-reference/#govuk-visually-hidden-focusable.md)govuk-visually-hidden-focusable
Hide an element visually, but have it available for screen readers whilst allowing the element to be focused when navigated to via the keyboard (e.g. for the skip link)
This is slightly less opinionated about borders and padding to make it easier to style the focussed element.
#####  [](./v4/sass-api-reference/#govuk-visually-hidden-focusable-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `true`  |  
#####  [](./v4/sass-api-reference/#govuk-visually-hidden-focusable-usage.md)Usage

```
@include govuk-visually-hidden-focusable($important: true);

```

[ View source code for _visually-hidden.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_visually-hidden.scss#L62-L96)
###  [](./v4/sass-api-reference/#colour.md)Colour
####  [](./v4/sass-api-reference/#govuk-colour.md)govuk-colour
Get colour
#####  [](./v4/sass-api-reference/#govuk-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | Name of colour from the colour palette (`$govuk-colours`)  |  `String` or `Colour`  | —  |  
|  `$legacy`  | Either the name of colour from the legacy palette or a colour literal, to return instead when in ‘legacy mode’ - matching the palette from GOV.UK Template, Elements or Frontend Toolkit  | `String`  | —  |  
#####  [](./v4/sass-api-reference/#example-using-legacy-colours-from-the-palette.md)Example: Using legacy colours from the palette

```
.foo {
  background-colour: govuk-colour("mid-grey", $legacy: "grey-2");
}

```

#####  [](./v4/sass-api-reference/#example-using-legacy-colour-literals.md)Example: Using legacy colour literals

```
.foo {
  background-colour: govuk-colour("green", $legacy: #BADA55);
}

```

[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L31-L49)
####  [](./v4/sass-api-reference/#govuk-organisation-colour.md)govuk-organisation-colour
Get the colour for a government organisation
#####  [](./v4/sass-api-reference/#govuk-organisation-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$organisation`  | Organisation name, lowercase, hyphenated  | `String`  | —  |  
|  `$websafe`  | By default a ‘websafe’ version of the colour will be returned which meets contrast requirements . If you want to use the non-websafe version you can set this to `false` but your should ensure that you still meets contrast requirements for accessibility - for example, do not use the non-websafe version for text.  | `Boolean`  | `true`  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L64-L76)
####  [](./v4/sass-api-reference/#govuk-shade.md)govuk-shade
Make a colour darker by mixing it with black
#####  [](./v4/sass-api-reference/#govuk-shade-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | colour to shade  | `Colour`  | —  |  
|  `$percentage`  | percentage of black to mix with $colour  | `Number`  | —  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L85-L87)
####  [](./v4/sass-api-reference/#govuk-tint.md)govuk-tint
Make a colour lighter by mixing it with white
#####  [](./v4/sass-api-reference/#govuk-tint-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | colour to tint  | `Colour`  | —  |  
|  `$percentage`  | percentage of white to mix with $colour  | `Number`  | —  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L96-L98)
###  [](./v4/sass-api-reference/#layout.md)Layout
####  [](./v4/sass-api-reference/#govuk-clearfix.md)govuk-clearfix
Clear floated content within a container using a pseudo element
#####  [](./v4/sass-api-reference/#govuk-clearfix-usage.md)Usage

```
@include govuk-clearfix;

```

[ View source code for _clearfix.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_clearfix.scss#L9-L15)
####  [](./v4/sass-api-reference/#govuk-grid-width.md)govuk-grid-width
Grid width percentage
#####  [](./v4/sass-api-reference/#govuk-grid-width-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$key`  | Name of grid width (e.g. two-thirds)  | `String`  | —  |  
[ View source code for _grid.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_grid.scss#L12-L18)
####  [](./v4/sass-api-reference/#govuk-grid-column.md)govuk-grid-column
Generate grid column styles
Creates a grid column with standard gutter between the columns.
Grid widths are defined in the `$govuk-grid-widths` map.
By default the column width changes from 100% to specified width at the ‘tablet’ breakpoint, but other breakpoints can be specified using the `$at` parameter.
#####  [](./v4/sass-api-reference/#govuk-grid-column-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$width`  | name of a grid width from $govuk-grid-widths  | `String`  | `full`  |  
|  `$float`  | left | right  | `String`  | `left`  |  
|  `$at`  | mobile | tablet | desktop | any custom breakpoint  | `String`  | `tablet`  |  
#####  [](./v4/sass-api-reference/#govuk-grid-column-usage.md)Usage

```
@include govuk-grid-column($width: "full", $float: "left", $at: "tablet");

```

#####  [](./v4/sass-api-reference/#example-default.md)Example: Default

```
.govuk-grid-column-two-thirds {
  @include govuk-grid-column(two-thirds)
}

```

#####  [](./v4/sass-api-reference/#example-customising-the-breakpoint-where-width-percentage-is-applied.md)Example: Customising the breakpoint where width percentage is applied

```
.govuk-grid-column-one-half-at-desktop {
  @include govuk-grid-column(one-half, $at: desktop);
}

```

#####  [](./v4/sass-api-reference/#example-customising-the-float-direction.md)Example: Customising the float direction

```
.govuk-grid-column-one-half-right {
  @include govuk-grid-column(two-thirds, $float: right);
}

```

[ View source code for _grid.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_grid.scss#L51-L61)
####  [](./v4/sass-api-reference/#govuk-media-query.md)govuk-media-query
Media Query
This is a currently a wrapper for sass-mq - abstracted so that we can replace it in the future if we so choose.
#####  [](./v4/sass-api-reference/#govuk-media-query-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$from`  | One of $govuk-breakpoints  |  `String` or `Boolean`  | `false`  |  
|  `$until`  | One of $govuk-breakpoints  |  `String` or `Boolean`  | `false`  |  
|  `$and`  | Additional media query parameters  |  `String` or `Boolean`  | `false`  |  
|  `$media-type`  | Media type: screen, print…  | `String`  | `all`  |  
#####  [](./v4/sass-api-reference/#govuk-media-query-usage.md)Usage

```
@include govuk-media-query($from: false, $until: false, $and: false, $media-type: "all") {
  //..
}

```

#####  [](./v4/sass-api-reference/#govuk-media-query-example.md)Example

```
.element {
  @include govuk-media-query($from: mobile) {
    color: red;
  }
  @include govuk-media-query($until: tablet) {
    color: blue;
  }
  @include govuk-media-query(mobile, tablet) {
    color: green;
  }
  @include govuk-media-query($from: tablet, $and: '(orientation: landscape)') {
    color: teal;
  }
  @include govuk-media-query(950px) {
    color: hotpink;
  }
  @include govuk-media-query(tablet, $media-type: screen) {
    color: hotpink;
  }
}

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L87-L91)
###  [](./v4/sass-api-reference/#helpers-links.md)Links
####  [](./v4/sass-api-reference/#govuk-link-common.md)govuk-link-common
Common link styles
Provides the typography and focus state, regardless of link style.
#####  [](./v4/sass-api-reference/#govuk-link-common-usage.md)Usage

```
@include govuk-link-common;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L11-L22)
####  [](./v4/sass-api-reference/#govuk-link-decoration.md)govuk-link-decoration
Link decoration
Provides the text decoration for links, including thickness and underline offset. Use this mixin only if you cannot use the `govuk-link-common` mixin.
#####  [](./v4/sass-api-reference/#govuk-link-decoration-usage.md)Usage

```
@include govuk-link-decoration;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L30-L42)
####  [](./v4/sass-api-reference/#govuk-link-hover-decoration.md)govuk-link-hover-decoration
Link hover decoration
Provides the text decoration for links in their hover state, for you to use within a `:hover` pseudo-selector. Use this mixin only if you cannot use the `govuk-link-common` mixin.
#####  [](./v4/sass-api-reference/#govuk-link-hover-decoration-usage.md)Usage

```
@include govuk-link-hover-decoration;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L52-L62)
####  [](./v4/sass-api-reference/#govuk-link-style-default.md)govuk-link-style-default
Default link styles
Makes links use the default unvisited, visited, hover and active colours.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-default-usage.md)Usage

```
@include govuk-link-style-default;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-default-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-default;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L79-L112)
####  [](./v4/sass-api-reference/#govuk-link-style-error.md)govuk-link-style-error
Error link styles
Makes links use the error colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-error-usage.md)Usage

```
@include govuk-link-style-error;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-error-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-error;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L130-L160)
####  [](./v4/sass-api-reference/#govuk-link-style-success.md)govuk-link-style-success
Success link styles
Makes links use the success colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-success-usage.md)Usage

```
@include govuk-link-style-success;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-success-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-success;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L178-L208)
####  [](./v4/sass-api-reference/#govuk-link-style-muted.md)govuk-link-style-muted
Muted link styles
Makes links use the secondary text colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-muted-usage.md)Usage

```
@include govuk-link-style-muted;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-muted-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-muted;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L226-L251)
####  [](./v4/sass-api-reference/#govuk-link-style-text.md)govuk-link-style-text
Text link styles
Makes links use the primary text colour, in all states. Use this mixin for navigation components, such as breadcrumbs or the back link.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-text-usage.md)Usage

```
@include govuk-link-style-text;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-text-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-text;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L269-L296)
####  [](./v4/sass-api-reference/#govuk-link-style-inverse.md)govuk-link-style-inverse
Inverse link styles
Makes links white, in all states. Use this mixin if you’re displaying links against a dark background.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-inverse-usage.md)Usage

```
@include govuk-link-style-inverse;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-inverse-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-inverse;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L314-L339)
####  [](./v4/sass-api-reference/#govuk-link-style-no-visited-state.md)govuk-link-style-no-visited-state
Default link styles, without a visited state
Makes links use the default unvisited, hover and active colours, with no distinct visited state.
Use this mixin when it’s not helpful to distinguish between visited and non-visited links. For example, when you link to pages with frequently-changing content, such as the dashboard for an admin interface.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v4/sass-api-reference/#govuk-link-style-no-visited-state-usage.md)Usage

```
@include govuk-link-style-no-visited-state;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-no-visited-state-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-no-visited-state;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L361-L383)
####  [](./v4/sass-api-reference/#govuk-link-style-no-underline.md)govuk-link-style-no-underline
Remove underline from links
Remove underlines from links unless the link is active or a user hovers their cursor over it. This has no effect in Internet Explorer 8 (IE8), because IE8 does not support `:not`.
#####  [](./v4/sass-api-reference/#govuk-link-style-no-underline-usage.md)Usage

```
@include govuk-link-style-no-underline;

```

#####  [](./v4/sass-api-reference/#govuk-link-style-no-underline-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-default;
  @include govuk-link-style-no-underline;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L400-L404)
####  [](./v4/sass-api-reference/#govuk-link-print-friendly.md)govuk-link-print-friendly
Include link destination when printing the page
If the user prints the page, add the destination URL after the link text, if the URL starts with `/`, `http://` or `https://`.
#####  [](./v4/sass-api-reference/#govuk-link-print-friendly-usage.md)Usage

```
@include govuk-link-print-friendly;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L413-L429)
###  [](./v4/sass-api-reference/#shapes.md)Shapes
####  [](./v4/sass-api-reference/#govuk-shape-arrow.md)govuk-shape-arrow
Arrow mixin
Generate Arrows (triangles) by using a mix of transparent (1) and coloured borders. The coloured borders inherit the text colour of the element (2).
Ensure the arrow is rendered correctly if browser colours are overridden by providing a clip path (3). Without this the transparent borders are overridden to become visible which results in a square.
We need both because older browsers do not support clip-path.
#####  [](./v4/sass-api-reference/#govuk-shape-arrow-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$direction`  | Direction for arrow: up, right, down, left.  | `String`  | —  |  
|  `$base`  | Length of the triangle ‘base’ side  | `Number`  | —  |  
|  `$height`  | Height of triangle. Omit for equilateral.  | `Number`  | `null`  |  
|  `$display`  | CSS display property of the arrow  | `String`  | `block`  |  
#####  [](./v4/sass-api-reference/#govuk-shape-arrow-usage.md)Usage

```
@include govuk-shape-arrow($direction, $base, $height: null, $display: "block");

```

[ View source code for _shape-arrow.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_shape-arrow.scss#L38-L80)
###  [](./v4/sass-api-reference/#spacing.md)Spacing
####  [](./v4/sass-api-reference/#govuk-spacing.md)govuk-spacing
Single point spacing
Returns measurement corresponding to the spacing point requested.
#####  [](./v4/sass-api-reference/#govuk-spacing-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$spacing-point`  | Point on the spacing scale (set in `settings/_spacing.scss`)  | `Number`  | —  |  
#####  [](./v4/sass-api-reference/#govuk-spacing-example.md)Example

```
.element {
  padding: govuk-spacing(5);
}

```

#####  [](./v4/sass-api-reference/#example-using-negative-spacing.md)Example: Using negative spacing

```
.element {
  margin-top: govuk-spacing(-1);
}

```

#####  [](./v4/sass-api-reference/#example-marking-spacing-declarations-as-important.md)Example: Marking spacing declarations as important

```
.element {
  margin-top: govuk-spacing(1) !important;
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L33-L53)
####  [](./v4/sass-api-reference/#govuk-responsive-margin.md)govuk-responsive-margin
Responsive margin
Adds responsive margin by fetching a ‘spacing map’ from the responsive spacing scale, which defines different spacing values at different breakpoints. Wrapper for the `_govuk-responsive-spacing` mixin.
#####  [](./v4/sass-api-reference/#govuk-responsive-margin-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$responsive-spacing-point`  | Point on the responsive spacingscale, corresponds to a map of breakpoints and spacing values  | `Number`  | —  |  
|  `$direction`  | Direction to add spacing to (`top`, `right`, `bottom`, `left`, `all`)  | `String`  | `all`  |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `false`  |  
|  `$adjustment`  | Offset to adjust spacing by  | `Number`  | `false`  |  
#####  [](./v4/sass-api-reference/#govuk-responsive-margin-usage.md)Usage

```
@include govuk-responsive-margin($responsive-spacing-point, $direction: "all", $important: false, $adjustment: false);

```

#####  [](./v4/sass-api-reference/#govuk-responsive-margin-example.md)Example

```
.element {
   @include govuk-responsive-margin(6, "left", $adjustment: 1px);
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L143-L145)
####  [](./v4/sass-api-reference/#govuk-responsive-padding.md)govuk-responsive-padding
Responsive padding
Adds responsive padding by fetching a ‘spacing map’ from the responsive spacing scale, which defines different spacing values at different breakpoints. Wrapper for the `_govuk-responsive-spacing` mixin.
#####  [](./v4/sass-api-reference/#govuk-responsive-padding-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$responsive-spacing-point`  | Point on the responsive spacing scale, corresponds to a map of breakpoints and spacing values  | `Number`  | —  |  
|  `$direction`  | Direction to add spacing to (`top`, `right`, `bottom`, `left`, `all`)  | `String`  | `all`  |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `false`  |  
|  `$adjustment`  | Offset to adjust spacing  | `Number`  | `false`  |  
#####  [](./v4/sass-api-reference/#govuk-responsive-padding-usage.md)Usage

```
@include govuk-responsive-padding($responsive-spacing-point, $direction: "all", $important: false, $adjustment: false);

```

#####  [](./v4/sass-api-reference/#govuk-responsive-padding-example.md)Example

```
.element {
   @include govuk-responsive-padding(6, "left", $adjustment: 1px);
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L169-L171)
###  [](./v4/sass-api-reference/#helpers-typography.md)Typography
####  [](./v4/sass-api-reference/#govuk-typography-common.md)govuk-typography-common
‘Common typography’ helper
Sets the font family and associated properties, such as font smoothing. Also overrides the font for print.
#####  [](./v4/sass-api-reference/#govuk-typography-common-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$font-family`  | Font family to use  | `List`  | `$govuk-font-family`  |  
#####  [](./v4/sass-api-reference/#govuk-typography-common-usage.md)Usage

```
@include govuk-typography-common($font-family: $govuk-font-family);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L15-L33)
####  [](./v4/sass-api-reference/#helpers-typography-govuk-text-colour.md)govuk-text-colour
Text colour helper
Sets the text colour, including a suitable override for print.
#####  [](./v4/sass-api-reference/#helpers-typography-govuk-text-colour-usage.md)Usage

```
@include govuk-text-colour;

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L41-L47)
####  [](./v4/sass-api-reference/#govuk-typography-weight-regular.md)govuk-typography-weight-regular
Regular font weight helper
#####  [](./v4/sass-api-reference/#govuk-typography-weight-regular-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./v4/sass-api-reference/#govuk-typography-weight-regular-usage.md)Usage

```
@include govuk-typography-weight-regular($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L55-L57)
####  [](./v4/sass-api-reference/#govuk-typography-weight-bold.md)govuk-typography-weight-bold
Bold font weight helper
#####  [](./v4/sass-api-reference/#govuk-typography-weight-bold-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./v4/sass-api-reference/#govuk-typography-weight-bold-usage.md)Usage

```
@include govuk-typography-weight-bold($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L65-L67)
####  [](./v4/sass-api-reference/#govuk-typography-responsive.md)govuk-typography-responsive
Responsive typography helper
Takes a point from the responsive ‘font map’ as an argument (the size as it would appear on tablet and above), and uses it to create font-size and line-height declarations for different breakpoints, and print.
Example font map:
19: ( null: ( font-size: 16px, line-height: 20px ), tablet: ( font-size: 19px, line-height: 25px ), print: ( font-size: 14pt, line-height: 1.15 ) );
#####  [](./v4/sass-api-reference/#govuk-typography-responsive-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the spacing scale (the size as it would appear on tablet and above)  | `Number`  | —  |  
|  `$override-line-height`  | Non responsive custom line height. Omit to use the line height from the font map.  | `Number`  | `false`  |  
|  `$important`  | Whether to mark declarations as `!important`.  | `Boolean`  | `false`  |  
#####  [](./v4/sass-api-reference/#govuk-typography-responsive-usage.md)Usage

```
@include govuk-typography-responsive($size, $override-line-height: false, $important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L121-L170)
####  [](./v4/sass-api-reference/#govuk-font.md)govuk-font
Font helper
#####  [](./v4/sass-api-reference/#govuk-font-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the spacing scale (the size as it would appear on tablet and above). Use `false` to avoid setting a size.  |  `Number` or `Boolean`  | —  |  
|  `$weight`  | Weight: `bold` or `regular`  | `String`  | `regular`  |  
|  `$tabular`  | Whether to use tabular numbers or not  | `Boolean`  | `false`  |  
|  `$line-height`  | Line-height, if overriding the default  | `Number`  | `false`  |  
#####  [](./v4/sass-api-reference/#govuk-font-usage.md)Usage

```
@include govuk-font($size, $weight: "regular", $tabular: false, $line-height: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L185-L212)
##  [](./v4/sass-api-reference/#components.md)Components
###  [](./v4/sass-api-reference/#button.md)Button
####  [](./v4/sass-api-reference/#govuk-button-background-colour.md)$govuk-button-background-colour
Button component background colour
#####  [](./v4/sass-api-reference/#govuk-button-background-colour-default-value.md)Default value

```
$govuk-button-background-colour: govuk-colour("green", $legacy: #00823b);

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L10-L10)
####  [](./v4/sass-api-reference/#govuk-button-text-colour.md)$govuk-button-text-colour
Button component text colour
#####  [](./v4/sass-api-reference/#govuk-button-text-colour-default-value.md)Default value

```
$govuk-button-text-colour: govuk-colour("white");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L17-L17)
##  [](./v4/sass-api-reference/#objects.md)Objects
###  [](./v4/sass-api-reference/#objects-layout.md)Layout
####  [](./v4/sass-api-reference/#govuk-width-container.md)govuk-width-container
Width container mixin
Used to create page width and custom width container classes.
#####  [](./v4/sass-api-reference/#govuk-width-container-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$width`  | Width in pixels  | `String`  | `$govuk-page-width`  |  
#####  [](./v4/sass-api-reference/#govuk-width-container-usage.md)Usage

```
@include govuk-width-container($width: "$govuk-page-width");

```

#####  [](./v4/sass-api-reference/#example-creating-a-1200px-wide-container-class.md)Example: Creating a 1200px wide container class

```
.app-width-container--wide {
  @include govuk-width-container(1200px);
}

```

[ View source code for _width-container.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/objects/_width-container.scss#L20-L78)
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/sass-api-reference/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Sass+API+reference+%28v4.x%29%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Fsass-api-reference%2F%29&labels=bug&title=Re%3A+%27Sass+API+reference+%28v4.x%29%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
