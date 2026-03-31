#  [](./v5/sass-api-reference/#sass-api-reference.md)Sass API reference
##  [](./v5/sass-api-reference/#settings.md)Settings
###  [](./v5/sass-api-reference/#assets.md)Assets
####  [](./v5/sass-api-reference/#govuk-assets-path.md)$govuk-assets-path
Path to the assets directory, with trailing slash.
This is the directory where the images and fonts subdirectories live. You will need to make this directory available via your application – see the README for details.
#####  [](./v5/sass-api-reference/#default-value.md)Default value

```
$govuk-assets-path: "/assets/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L14-L14)
####  [](./v5/sass-api-reference/#govuk-images-path.md)$govuk-images-path
Path to the images folder, with trailing slash.
#####  [](./v5/sass-api-reference/#govuk-images-path-default-value.md)Default value

```
$govuk-images-path: "#{$govuk-assets-path}images/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L21-L21)
####  [](./v5/sass-api-reference/#govuk-fonts-path.md)$govuk-fonts-path
Path to the fonts folder, with trailing slash.
#####  [](./v5/sass-api-reference/#govuk-fonts-path-default-value.md)Default value

```
$govuk-fonts-path: "#{$govuk-assets-path}fonts/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L28-L28)
####  [](./v5/sass-api-reference/#govuk-image-url-function.md)$govuk-image-url-function
Custom image URL function
If the built-in image URL helper does not meet your needs, you can specify the name of a custom handler – either built in or by writing your own function.
If you are writing your own handler, ensure that it returns a string wrapped with `url()`
#####  [](./v5/sass-api-reference/#govuk-image-url-function-default-value.md)Default value

```
$govuk-image-url-function: false;

```

#####  [](./v5/sass-api-reference/#example-rails-asset-handling.md)Example: Rails asset handling

```
$govuk-image-url-function: 'image-url';

```

#####  [](./v5/sass-api-reference/#example-custom-asset-handling.md)Example: Custom asset handling

```
@function my-url-handler($filename) {
  // Some custom URL handling
  @return url('example.jpg');
}

$govuk-image-url-function: 'my-url-handler';

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L55-L55)
####  [](./v5/sass-api-reference/#govuk-font-url-function.md)$govuk-font-url-function
Custom font URL function
If the built-in font URL helper does not meet your needs, you can specify the name of a custom handler – either built in or by writing your own function.
If you are writing your own handler, ensure that it returns a string wrapped with `url()`
#####  [](./v5/sass-api-reference/#govuk-font-url-function-default-value.md)Default value

```
$govuk-font-url-function: false;

```

#####  [](./v5/sass-api-reference/#govuk-font-url-function-example-rails-asset-handling.md)Example: Rails asset handling

```
$govuk-font-url-function: 'font-url';

```

#####  [](./v5/sass-api-reference/#govuk-font-url-function-example-custom-asset-handling.md)Example: Custom asset handling

```
@function my-url-handler($filename) {
  // Some custom URL handling
  @return url('example.woff');
}

$govuk-font-url-function: 'my-url-handler';

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L82-L82)
###  [](./v5/sass-api-reference/#colours.md)Colours
####  [](./v5/sass-api-reference/#govuk-brand-colour.md)$govuk-brand-colour
Brand colour
#####  [](./v5/sass-api-reference/#govuk-brand-colour-default-value.md)Default value

```
$govuk-brand-colour: govuk-colour("blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L16-L16)
####  [](./v5/sass-api-reference/#govuk-text-colour.md)$govuk-text-colour
Text colour
#####  [](./v5/sass-api-reference/#govuk-text-colour-default-value.md)Default value

```
$govuk-text-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L23-L23)
####  [](./v5/sass-api-reference/#govuk-canvas-background-colour.md)$govuk-canvas-background-colour
Canvas background colour
Used by the footer component and template to give the illusion of a long footer.
#####  [](./v5/sass-api-reference/#usage.md)Usage
! ** Warning
Deprecated: “$govuk-canvas-background-colour has been deprecated and will be removed in the next major version. Use `$govuk-template-background-colour` if you want to change the background of the `<html>` element and background colour of elements that need to match for visual continuity.
**
#####  [](./v5/sass-api-reference/#govuk-canvas-background-colour-default-value.md)Default value

```
$govuk-canvas-background-colour: govuk-colour("light-grey");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L36-L36)
####  [](./v5/sass-api-reference/#govuk-template-background-colour.md)$govuk-template-background-colour
Template background colour
Used by components that want to give the illusion of extending the template background (such as the footer and cookie banner).
#####  [](./v5/sass-api-reference/#govuk-template-background-colour-default-value.md)Default value

```
$govuk-template-background-colour: govuk-colour("light-grey");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L55-L55)
####  [](./v5/sass-api-reference/#govuk-body-background-colour.md)$govuk-body-background-colour
Body background colour
#####  [](./v5/sass-api-reference/#govuk-body-background-colour-default-value.md)Default value

```
$govuk-body-background-colour: govuk-colour("white");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L62-L62)
####  [](./v5/sass-api-reference/#govuk-print-text-colour.md)$govuk-print-text-colour
Text colour for print media
Use ‘true black’ to avoid printers using colour ink to print body text
#####  [](./v5/sass-api-reference/#govuk-print-text-colour-default-value.md)Default value

```
$govuk-print-text-colour: #000000;

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L71-L71)
####  [](./v5/sass-api-reference/#govuk-secondary-text-colour.md)$govuk-secondary-text-colour
Secondary text colour
Used in for example ‘muted’ text and help text.
#####  [](./v5/sass-api-reference/#govuk-secondary-text-colour-default-value.md)Default value

```
$govuk-secondary-text-colour: govuk-colour("dark-grey");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L80-L80)
####  [](./v5/sass-api-reference/#govuk-focus-colour.md)$govuk-focus-colour
Focus colour
Used for outline (and background, where appropriate) when interactive elements (links, form controls) have keyboard focus.
#####  [](./v5/sass-api-reference/#govuk-focus-colour-default-value.md)Default value

```
$govuk-focus-colour: govuk-colour("yellow");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L90-L90)
####  [](./v5/sass-api-reference/#govuk-focus-text-colour.md)$govuk-focus-text-colour
Focused text colour
Ensure that the contrast between the text and background colour passes WCAG Level AA contrast requirements.
#####  [](./v5/sass-api-reference/#govuk-focus-text-colour-default-value.md)Default value

```
$govuk-focus-text-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L100-L100)
####  [](./v5/sass-api-reference/#govuk-error-colour.md)$govuk-error-colour
Error colour
Used to highlight error messages and form controls in an error state
#####  [](./v5/sass-api-reference/#govuk-error-colour-default-value.md)Default value

```
$govuk-error-colour: govuk-colour("red");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L109-L109)
####  [](./v5/sass-api-reference/#govuk-success-colour.md)$govuk-success-colour
Success colour
Used to highlight success messages and banners
#####  [](./v5/sass-api-reference/#govuk-success-colour-default-value.md)Default value

```
$govuk-success-colour: govuk-colour("green");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L118-L118)
####  [](./v5/sass-api-reference/#govuk-border-colour.md)$govuk-border-colour
Border colour
Used in for example borders, separators, rules and keylines.
#####  [](./v5/sass-api-reference/#govuk-border-colour-default-value.md)Default value

```
$govuk-border-colour: govuk-colour("mid-grey");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L127-L127)
####  [](./v5/sass-api-reference/#govuk-input-border-colour.md)$govuk-input-border-colour
Input border colour
Used for form inputs and controls
#####  [](./v5/sass-api-reference/#govuk-input-border-colour-default-value.md)Default value

```
$govuk-input-border-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L136-L136)
####  [](./v5/sass-api-reference/#govuk-hover-colour.md)$govuk-hover-colour
Input hover colour
Used for hover states on form controls
#####  [](./v5/sass-api-reference/#govuk-hover-colour-default-value.md)Default value

```
$govuk-hover-colour: govuk-colour("mid-grey");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L145-L145)
####  [](./v5/sass-api-reference/#govuk-link-colour.md)$govuk-link-colour
Link colour
#####  [](./v5/sass-api-reference/#govuk-link-colour-default-value.md)Default value

```
$govuk-link-colour: govuk-colour("blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L156-L156)
####  [](./v5/sass-api-reference/#govuk-link-visited-colour.md)$govuk-link-visited-colour
Visited link colour
#####  [](./v5/sass-api-reference/#govuk-link-visited-colour-default-value.md)Default value

```
$govuk-link-visited-colour: govuk-colour("purple");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L163-L163)
####  [](./v5/sass-api-reference/#govuk-link-hover-colour.md)$govuk-link-hover-colour
Link hover colour
#####  [](./v5/sass-api-reference/#govuk-link-hover-colour-default-value.md)Default value

```
$govuk-link-hover-colour: govuk-colour("dark-blue");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L170-L170)
####  [](./v5/sass-api-reference/#govuk-link-active-colour.md)$govuk-link-active-colour
Active link colour
#####  [](./v5/sass-api-reference/#govuk-link-active-colour-default-value.md)Default value

```
$govuk-link-active-colour: govuk-colour("black");

```

[ View source code for _colours-applied.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-applied.scss#L177-L177)
####  [](./v5/sass-api-reference/#govuk-new-organisation-colours.md)$govuk-new-organisation-colours
Feature flag for updated organisation list and colours
When set to true, $govuk-colours-organisations will use the new organisation list and colour selection.
Should be removed in 6.0.
#####  [](./v5/sass-api-reference/#govuk-new-organisation-colours-usage.md)Usage
! ** Warning
Deprecated: Using new organisation colours will become the default in Frontend v6.0.
**
#####  [](./v5/sass-api-reference/#govuk-new-organisation-colours-default-value.md)Default value

```
$govuk-new-organisation-colours: false;

```

[ View source code for _colours-organisations.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-organisations.scss#L18-L18)
####  [](./v5/sass-api-reference/#govuk-colours-organisations.md)$govuk-colours-organisations
Set public organisation colours variable to one of the two maps. Users can also pass their own map to this to override it entirely.
#####  [](./v5/sass-api-reference/#govuk-colours-organisations-default-value.md)Default value

```
$govuk-colours-organisations: $_govuk-legacy-organisation-colours;

```

[ View source code for _colours-organisations.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-organisations.scss#L356-L356)
####  [](./v5/sass-api-reference/#govuk-colours.md)$govuk-colours
Colour palette
#####  [](./v5/sass-api-reference/#govuk-colours-default-value.md)Default value

```
$govuk-colours: (
  "red": #d4351c,
  "yellow": #ffdd00,
  "green": #00703c,
  "blue": #1d70b8,
  "dark-blue": #003078,
  "light-blue": #5694ca,
  "purple": #4c2c92,
  "black": #0b0c0c,
  "dark-grey": #505a5f,
  "mid-grey": #b1b4b6,
  "light-grey": #f3f2f1,
  "white": #ffffff,
  "light-purple": #6f72af,
  "bright-purple": #912b88,
  "pink": #d53880,
  "light-pink": #f499be,
  "orange": #f47738,
  "brown": #b58840,
  "light-green": #85994b,
  "turquoise": #28a197
);

```

[ View source code for _colours-palette.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-palette.scss#L14-L35)
###  [](./v5/sass-api-reference/#global-styles.md)Global styles
####  [](./v5/sass-api-reference/#govuk-global-styles.md)$govuk-global-styles
Include ‘global’ styles
Whether to style paragraphs (`<p>`) and links (`<a>`) without explicitly having to apply the `govuk-body` and `govuk-link` classes.
#####  [](./v5/sass-api-reference/#govuk-global-styles-default-value.md)Default value

```
$govuk-global-styles: false;

```

[ View source code for _global-styles.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_global-styles.scss#L13-L13)
###  [](./v5/sass-api-reference/#layout.md)Layout
####  [](./v5/sass-api-reference/#govuk-page-width.md)$govuk-page-width
Width of main container
#####  [](./v5/sass-api-reference/#govuk-page-width-default-value.md)Default value

```
$govuk-page-width: 960px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L14-L14)
####  [](./v5/sass-api-reference/#govuk-grid-widths.md)$govuk-grid-widths
Map of grid column widths
#####  [](./v5/sass-api-reference/#govuk-grid-widths-default-value.md)Default value

```
$govuk-grid-widths: (
  one-quarter: (
    100% / 4
  ),
  one-third: (
    100% / 3
  ),
  one-half: (
    100% / 2
  ),
  two-thirds: (
    200% / 3
  ),
  three-quarters: (
    300% / 4
  ),
  full: 100%
);

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L21-L38)
####  [](./v5/sass-api-reference/#govuk-gutter.md)$govuk-gutter
Width of gutter between grid columns
#####  [](./v5/sass-api-reference/#govuk-gutter-default-value.md)Default value

```
$govuk-gutter: 30px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L45-L45)
####  [](./v5/sass-api-reference/#govuk-gutter-half.md)$govuk-gutter-half
Width of half the gutter between grid columns
#####  [](./v5/sass-api-reference/#govuk-gutter-half-default-value.md)Default value

```
$govuk-gutter-half: $govuk-gutter / 2;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L52-L52)
####  [](./v5/sass-api-reference/#govuk-border-width.md)$govuk-border-width
Standard border width
#####  [](./v5/sass-api-reference/#govuk-border-width-default-value.md)Default value

```
$govuk-border-width: 5px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L63-L63)
####  [](./v5/sass-api-reference/#govuk-border-width-wide.md)$govuk-border-width-wide
Wide border width
#####  [](./v5/sass-api-reference/#govuk-border-width-wide-default-value.md)Default value

```
$govuk-border-width-wide: 10px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L70-L70)
####  [](./v5/sass-api-reference/#govuk-border-width-narrow.md)$govuk-border-width-narrow
Narrow border width
#####  [](./v5/sass-api-reference/#govuk-border-width-narrow-default-value.md)Default value

```
$govuk-border-width-narrow: 4px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L77-L77)
####  [](./v5/sass-api-reference/#govuk-border-width-form-element.md)$govuk-border-width-form-element
Form control border width
#####  [](./v5/sass-api-reference/#govuk-border-width-form-element-default-value.md)Default value

```
$govuk-border-width-form-element: 2px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L84-L84)
####  [](./v5/sass-api-reference/#govuk-border-width-form-group-error.md)$govuk-border-width-form-group-error
Form group border width when in error state
#####  [](./v5/sass-api-reference/#govuk-border-width-form-group-error-default-value.md)Default value

```
$govuk-border-width-form-group-error: $govuk-border-width;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L91-L91)
####  [](./v5/sass-api-reference/#govuk-focus-width.md)$govuk-focus-width
Border width of focus outline
#####  [](./v5/sass-api-reference/#govuk-focus-width-default-value.md)Default value

```
$govuk-focus-width: 3px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L98-L98)
####  [](./v5/sass-api-reference/#govuk-hover-width.md)$govuk-hover-width
Hover width for form controls with a hover state
#####  [](./v5/sass-api-reference/#govuk-hover-width-default-value.md)Default value

```
$govuk-hover-width: 10px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L105-L105)
####  [](./v5/sass-api-reference/#govuk-breakpoints.md)$govuk-breakpoints
Breakpoint definitions
#####  [](./v5/sass-api-reference/#govuk-breakpoints-default-value.md)Default value

```
$govuk-breakpoints: (
  mobile: 320px,
  tablet: 641px,
  desktop: 769px
);

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_media-queries.scss#L12-L16)
####  [](./v5/sass-api-reference/#govuk-show-breakpoints.md)$govuk-show-breakpoints
Show active breakpoint in top-right corner.
Only use this during local development.
#####  [](./v5/sass-api-reference/#govuk-show-breakpoints-usage.md)Usage
! ** Warning
Deprecated: The variable is non-operational and will be removed in Frontend v6.0.
**
#####  [](./v5/sass-api-reference/#govuk-show-breakpoints-default-value.md)Default value

```
$govuk-show-breakpoints: false;

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_media-queries.scss#L26-L26)
###  [](./v5/sass-api-reference/#links.md)Links
####  [](./v5/sass-api-reference/#govuk-link-underline-thickness.md)$govuk-link-underline-thickness
Thickness of link underlines
The default will be either:
  * 1px
  * 0.0625rem, if it’s thicker than 1px because the user has changed the text size in their browser

Set this variable to `false` to avoid setting a thickness.
#####  [](./v5/sass-api-reference/#govuk-link-underline-thickness-default-value.md)Default value

```
$govuk-link-underline-thickness: unquote("max(1px, .0625rem)");

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L18-L18)
####  [](./v5/sass-api-reference/#govuk-link-underline-offset.md)$govuk-link-underline-offset
Offset of link underlines from text baseline
The default is 3px expressed as ems, as calculated against the default body font size (on desktop) of 19px. 3 ÷ 19 = 0.1578
Set this variable to `false` to avoid setting an offset.
#####  [](./v5/sass-api-reference/#govuk-link-underline-offset-default-value.md)Default value

```
$govuk-link-underline-offset: 0.1578em;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L31-L31)
####  [](./v5/sass-api-reference/#govuk-link-hover-underline-thickness.md)$govuk-link-hover-underline-thickness
Thickness of link underlines in hover state
The default for each link will be the thickest of the following:
  * 3px
  * 0.1875rem, if it’s thicker than 3px because the user has changed the text size in their browser
  * 0.12em (relative to the link’s text size)

Set this variable to `false` to avoid setting a thickness.
#####  [](./v5/sass-api-reference/#govuk-link-hover-underline-thickness-default-value.md)Default value

```
$govuk-link-hover-underline-thickness: unquote("max(3px, .1875rem, .12em)");

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L47-L47)
###  [](./v5/sass-api-reference/#typography.md)Typography
####  [](./v5/sass-api-reference/#govuk-font-family.md)$govuk-font-family
Font families to use for all typography on screen media
#####  [](./v5/sass-api-reference/#govuk-font-family-default-value.md)Default value

```
$govuk-font-family: "GDS Transport", arial, sans-serif;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L14-L14)
####  [](./v5/sass-api-reference/#govuk-font-family-print.md)$govuk-font-family-print
Font families to use for print media
We recommend that you use system fonts when printing. This will avoid issues with some printer drivers and operating systems.
#####  [](./v5/sass-api-reference/#govuk-font-family-print-default-value.md)Default value

```
$govuk-font-family-print: sans-serif;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L24-L24)
####  [](./v5/sass-api-reference/#govuk-include-default-font-face.md)$govuk-include-default-font-face
Include the default @font-face declarations
Defaults to true if "GDS Transport” appears in the $govuk-font-family setting.
#####  [](./v5/sass-api-reference/#govuk-include-default-font-face-default-value.md)Default value

```
$govuk-include-default-font-face: if(index($govuk-font-family, "GDS Transport"), true, false);

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L34-L34)
####  [](./v5/sass-api-reference/#govuk-font-weight-regular.md)$govuk-font-weight-regular
Font weight for regular typography
#####  [](./v5/sass-api-reference/#govuk-font-weight-regular-default-value.md)Default value

```
$govuk-font-weight-regular: 400;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L44-L44)
####  [](./v5/sass-api-reference/#govuk-font-weight-bold.md)$govuk-font-weight-bold
Font weight for bold typography
#####  [](./v5/sass-api-reference/#govuk-font-weight-bold-default-value.md)Default value

```
$govuk-font-weight-bold: 700;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L50-L50)
####  [](./v5/sass-api-reference/#govuk-root-font-size.md)$govuk-root-font-size
Root font size
This is used to calculate rem sizes for the typography, and should match the _effective_ font-size of your root (or html) element.
Ideally you should not be setting the font-size on the html or root element in order to allow it to scale with user-preference, in which case this should be set to 16px.
#####  [](./v5/sass-api-reference/#govuk-root-font-size-default-value.md)Default value

```
$govuk-root-font-size: 16px;

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L17-L17)
####  [](./v5/sass-api-reference/#govuk-new-typography-scale.md)$govuk-new-typography-scale
Feature flag for new typography scale
When set to true, $govuk-typography-scale will use the new font map instead of the current/old one as well as apply changes in components to account for the updated scale.
Should be removed in 6.0.
#####  [](./v5/sass-api-reference/#govuk-new-typography-scale-default-value.md)Default value

```
$govuk-new-typography-scale: false;

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L30-L30)
####  [](./v5/sass-api-reference/#govuk-typography-scale.md)$govuk-typography-scale
Responsive typography font map
This is used to generate responsive typography that adapts according to the breakpoints.
Font size and font weight can be defined for each breakpoint. You can define different behaviour on tablet and desktop. The ‘null’ breakpoint is for mobile.
Line-heights will automatically be converted from pixel measurements into relative values. For example, with a font-size of 16px and a line-height of 24px, the line-height will be converted to 1.5 before output.
You can also specify a separate font size and line height for print media.
#####  [](./v5/sass-api-reference/#govuk-typography-scale-default-value.md)Default value

```
$govuk-typography-scale: if(
  $govuk-new-typography-scale,
  $_govuk-typography-scale-modern,
  $_govuk-typography-scale-legacy
);

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L311-L315)
###  [](./v5/sass-api-reference/#warnings.md)Warnings
####  [](./v5/sass-api-reference/#govuk-suppressed-warnings.md)$govuk-suppressed-warnings
Suppressed warnings map
This map is used to determine which deprecation warnings to **not** show to users when compiling sass. This is in place for codebases that do not have the necessary capacity to upgrade and remove the deprecation, particularly if the deprecation is significant. For example, the removal of mixins and functions that were previously available to users of Frontend.
You can add to this map and define which warnings to suppress by appending to it using the warning key, found in the warning message. For example:
#####  [](./v5/sass-api-reference/#govuk-suppressed-warnings-default-value.md)Default value

```
$govuk-suppressed-warnings: ();

```

#####  [](./v5/sass-api-reference/#example.md)Example: :

```
// warning message:
//  $foobar is no longer supported. To silence this warning, update
//  $govuk-suppressed-warnings with key: "foobar"
$govuk-suppressed-warnings: (
  foobar
);

```

[ View source code for _warnings.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_warnings.scss#L27-L27)
##  [](./v5/sass-api-reference/#tools.md)Tools
###  [](./v5/sass-api-reference/#general-tools.md)General tools
####  [](./v5/sass-api-reference/#govuk-exports.md)govuk-exports
Export module
Ensure that the modules of CSS that we define throughout Frontend are only included in the generated CSS once, no matter how many times they are imported across the individual components.
#####  [](./v5/sass-api-reference/#parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$name`  | Name of module - must be unique within the codebase  | `String`  | —  |  
#####  [](./v5/sass-api-reference/#govuk-exports-usage.md)Usage

```
@include govuk-exports($name) {
  //..
}

```

[ View source code for _exports.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_exports.scss#L23-L33)
###  [](./v5/sass-api-reference/#tools-assets.md)Assets
####  [](./v5/sass-api-reference/#govuk-font-url.md)govuk-font-url
Font URL
If a custom font-url handler is defined ($govuk-font-url-function) then it will be called, otherwise a url will be returned with the filename appended to the font path.
#####  [](./v5/sass-api-reference/#govuk-font-url-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$filename`  | Font filename  | `String`  | —  |  
[ View source code for _font-url.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_font-url.scss#L15-L26)
####  [](./v5/sass-api-reference/#govuk-image-url.md)govuk-image-url
Image URL
If a custom image-url handler is defined ($govuk-image-url-function) then it will be called, otherwise a url will be returned with the filename appended to the image path.
#####  [](./v5/sass-api-reference/#govuk-image-url-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$Filename`  | for the image to load  | `String`  | —  |  
[ View source code for _image-url.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_image-url.scss#L15-L26)
###  [](./v5/sass-api-reference/#unit-conversion.md)Unit conversion
####  [](./v5/sass-api-reference/#govuk-em.md)govuk-em
Convert pixels to em
#####  [](./v5/sass-api-reference/#govuk-em-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | Length in pixels  | `Number`  | —  |  
|  `$context-font-size`  | Font size of element  | `Number`  | `$govuk-root-font-size`  |  
[ View source code for _px-to-em.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_px-to-em.scss#L14-L22)
####  [](./v5/sass-api-reference/#govuk-px-to-rem.md)govuk-px-to-rem
Convert pixels to rem
The $govuk-root-font-size (defined in settings/_typography-responsive.scss) must be configured to match the font-size of your root (html) element
#####  [](./v5/sass-api-reference/#govuk-px-to-rem-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | Length in pixels  | `Number`  | —  |  
[ View source code for _px-to-rem.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_px-to-rem.scss#L14-L20)
##  [](./v5/sass-api-reference/#helpers.md)Helpers
###  [](./v5/sass-api-reference/#general-helpers.md)General helpers
####  [](./v5/sass-api-reference/#govuk-device-pixel-ratio.md)govuk-device-pixel-ratio
Media query for retina images (device-pixel-ratio)
#####  [](./v5/sass-api-reference/#govuk-device-pixel-ratio-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$ratio`  | Device pixel ratio  | `Number`  | `2`  |  
#####  [](./v5/sass-api-reference/#govuk-device-pixel-ratio-usage.md)Usage

```
@include govuk-device-pixel-ratio($ratio: 2) {
  //..
}

```

#####  [](./v5/sass-api-reference/#example-providing-a-2x-image-for-screens-that-support-it.md)Example: Providing a @2x image for screens that support it

```
background-image: govuk-image-url("my-image.png");

@include govuk-device-pixel-ratio {
  background-image: govuk-image-url("my-image-2x.png");
}

```

#####  [](./v5/sass-api-reference/#example-using-a-custom-ratio.md)Example: Using a custom ratio

```
background-image: govuk-image-url("my-image.png");

@include govuk-device-pixel-ratio {
  background-image: govuk-image-url("my-image-2x.png");
}

@include govuk-device-pixel-ratio(3) {
  background-image: govuk-image-url("my-image-3x.png");
}

```

[ View source code for _device-pixels.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_device-pixels.scss#L30-L36)
###  [](./v5/sass-api-reference/#accessibility.md)Accessibility
####  [](./v5/sass-api-reference/#govuk-focused-text.md)govuk-focused-text
Focused text
Provides an outline to clearly indicate when the target element is focused. Used for interactive text-based elements.
#####  [](./v5/sass-api-reference/#govuk-focused-text-usage.md)Usage

```
@include govuk-focused-text;

```

#####  [](./v5/sass-api-reference/#example-styling-the-focus-state-for-a-link.md)Example: Styling the focus state for a link

```
.govuk-link:focus {
  @include govuk-focused-text;
}

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L17-L46)
####  [](./v5/sass-api-reference/#govuk-focused-box.md)govuk-focused-box
Focused box
Provides an outline to clearly indicate when the target element is focused. Unlike govuk-focused-text, which only draws an underline below the element, govuk-focused-box draws an outline around all sides of the element. Best used for non-text content contained within links.
#####  [](./v5/sass-api-reference/#govuk-focused-box-usage.md)Usage

```
@include govuk-focused-box;

```

#####  [](./v5/sass-api-reference/#example-styling-the-focus-state-for-a-linked-image.md)Example: Styling the focus state for a linked image

```
.govuk-link-image:focus {
  @include govuk-focused-box;
}

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L62-L67)
####  [](./v5/sass-api-reference/#govuk-focused-form-input.md)govuk-focused-form-input
Focused form input
Provides an outline to clearly indicate when the target element is focused. Used for form inputs.
#####  [](./v5/sass-api-reference/#govuk-focused-form-input-usage.md)Usage

```
@include govuk-focused-form-input;

```

#####  [](./v5/sass-api-reference/#example-styling-the-focus-state-for-a-form-input.md)Example: Styling the focus state for a form input

```
.govuk-input:focus {
  @include govuk-focused-form-input;
}

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L81-L91)
####  [](./v5/sass-api-reference/#govuk-visually-hidden.md)govuk-visually-hidden
Hide an element visually, but have it available for screen readers
#####  [](./v5/sass-api-reference/#govuk-visually-hidden-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `true`  |  
#####  [](./v5/sass-api-reference/#govuk-visually-hidden-usage.md)Usage

```
@include govuk-visually-hidden($important: true);

```

[ View source code for _visually-hidden.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_visually-hidden.scss#L54-L68)
####  [](./v5/sass-api-reference/#govuk-visually-hidden-focusable.md)govuk-visually-hidden-focusable
Hide an element visually, but have it available for screen readers whilst allowing the element to be focused when navigated to via the keyboard (e.g. for the skip link)
#####  [](./v5/sass-api-reference/#govuk-visually-hidden-focusable-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `true`  |  
#####  [](./v5/sass-api-reference/#govuk-visually-hidden-focusable-usage.md)Usage

```
@include govuk-visually-hidden-focusable($important: true);

```

[ View source code for _visually-hidden.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_visually-hidden.scss#L78-L86)
###  [](./v5/sass-api-reference/#colour.md)Colour
####  [](./v5/sass-api-reference/#govuk-colour.md)govuk-colour
Get colour
#####  [](./v5/sass-api-reference/#govuk-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | Name of colour from the colour palette (`$govuk-colours`)  |  `String` or `Colour`  | —  |  
|  `$legacy`  | Deprecated. The `$legacy` parameter is deprecated and is non-operational, as the legacy colour palette has been removed. The parameter will be removed in the next major version.  |  `String` or `Colour` or `Boolean`  | `false`  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L22-L40)
####  [](./v5/sass-api-reference/#govuk-organisation-colour.md)govuk-organisation-colour
Get the colour for a government organisation
#####  [](./v5/sass-api-reference/#govuk-organisation-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$organisation`  | Organisation name, lowercase, hyphenated  | `String`  | —  |  
|  `$websafe`  | Deprecated. Use $contrast-safe instead.  | `Boolean`  | —  |  
|  `$contrast-safe`  | By default a version of the colour will be returned which has a minimum 4.5:1 contrast ratio when used with white, as per the WCAG 2.1 Level AA guidelines. If you want to use the non-contrast safe version you can set this to `false` but your should ensure that you still meets contrast requirements for accessibility - for example, do not use the non-contrast safe version for text.  | `Boolean`  | `true`  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L57-L114)
####  [](./v5/sass-api-reference/#govuk-shade.md)govuk-shade
Make a colour darker by mixing it with black
#####  [](./v5/sass-api-reference/#govuk-shade-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | colour to shade  | `Colour`  | —  |  
|  `$percentage`  | percentage of black to mix with $colour  | `Number`  | —  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L123-L127)
####  [](./v5/sass-api-reference/#govuk-tint.md)govuk-tint
Make a colour lighter by mixing it with white
#####  [](./v5/sass-api-reference/#govuk-tint-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | colour to tint  | `Colour`  | —  |  
|  `$percentage`  | percentage of white to mix with $colour  | `Number`  | —  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L136-L140)
###  [](./v5/sass-api-reference/#helpers-layout.md)Layout
####  [](./v5/sass-api-reference/#govuk-clearfix.md)govuk-clearfix
Clear floated content within a container using a pseudo element
#####  [](./v5/sass-api-reference/#govuk-clearfix-usage.md)Usage

```
@include govuk-clearfix;

```

[ View source code for _clearfix.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_clearfix.scss#L9-L15)
####  [](./v5/sass-api-reference/#govuk-grid-width.md)govuk-grid-width
Grid width percentage
#####  [](./v5/sass-api-reference/#govuk-grid-width-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$key`  | Name of grid width (e.g. two-thirds)  | `String`  | —  |  
[ View source code for _grid.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_grid.scss#L12-L18)
####  [](./v5/sass-api-reference/#govuk-grid-column.md)govuk-grid-column
Generate grid column styles
Creates a grid column with standard gutter between the columns.
Grid widths are defined in the `$govuk-grid-widths` map.
By default the column width changes from 100% to specified width at the ‘tablet’ breakpoint, but other breakpoints can be specified using the `$at` parameter.
#####  [](./v5/sass-api-reference/#govuk-grid-column-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$width`  | name of a grid width from $govuk-grid-widths  | `String`  | `full`  |  
|  `$float`  | left | right  | `String`  | `left`  |  
|  `$at`  | mobile | tablet | desktop | any custom breakpoint  | `String`  | `tablet`  |  
#####  [](./v5/sass-api-reference/#govuk-grid-column-usage.md)Usage

```
@include govuk-grid-column($width: "full", $float: "left", $at: "tablet");

```

#####  [](./v5/sass-api-reference/#example-default.md)Example: Default

```
.govuk-grid-column-two-thirds {
  @include govuk-grid-column(two-thirds)
}

```

#####  [](./v5/sass-api-reference/#example-customising-the-breakpoint-where-width-percentage-is-applied.md)Example: Customising the breakpoint where width percentage is applied

```
.govuk-grid-column-one-half-from-desktop {
  @include govuk-grid-column(one-half, $at: desktop);
}

```

#####  [](./v5/sass-api-reference/#example-customising-the-float-direction.md)Example: Customising the float direction

```
.govuk-grid-column-one-half-right {
  @include govuk-grid-column(two-thirds, $float: right);
}

```

[ View source code for _grid.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_grid.scss#L51-L61)
####  [](./v5/sass-api-reference/#govuk-breakpoint-value.md)govuk-breakpoint-value
Get the value of a breakpoint by name.
#####  [](./v5/sass-api-reference/#govuk-breakpoint-value-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | If a string, the name of a breakpoint in $breakpoints. If a number without units, it will convert to px. If a number with units, it will return the value unaltered.  |  `String` or `Number`  | —  |  
|  `$breakpoints`  | The map to look for $value.  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./v5/sass-api-reference/#govuk-breakpoint-value-example.md)Example

```
.element {
  width: govuk-breakpoint-value(tablet);
  @media (min-width: #{govuk-breakpoint-value(desktop)}) {
    color: red;
  }
  @media (min-width: #{govuk-breakpoint-value(400px)}) {
    color: green;
  }
  $custom-breakpoint-map: (
    small: 350px,
    medium: 769px,
    large: 1100px,
    extra-large: 1600px
  );
  @media (orientation: landscape) and (min-width: #{govuk-breakpoint-value(extra-large, $custom-breakpoint-map)}) {
    color: blue;
  }
}

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L42-L61)
####  [](./v5/sass-api-reference/#govuk-from-breakpoint.md)govuk-from-breakpoint
Generate the `min-width` segment of a media query given a breakpoint key
Pixel values are converted to ems for backwards compatibility with sass-mq. Unlike sass-mq, non-px and em values can be used as well.
#####  [](./v5/sass-api-reference/#govuk-from-breakpoint-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$from`  | If a string, expects the name of a breakpoint in $breakpoints. If a number, it will use that number.  |  `String` or `Number`  | —  |  
|  `$breakpoints`  | The map to look for $from.  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./v5/sass-api-reference/#govuk-from-breakpoint-example.md)Example

```
.example {
  @media #{govuk-from-breakpoint(tablet)} {
    color: red;
  }
  @media #{govuk-from-breakpoint(30em)} {
    color: green;
  }
  @media #{govuk-from-breakpoint(tablet)} and (orientation: landscape) {
    color: blue;
  }
  $custom-breakpoint-map: (
    small: 350px,
    medium: 769px,
    large: 1100px,
    extra-large: 1600px
  );
  @media #{govuk-from-breakpoint(extra-large, $custom-breakpoint-map)} {
    color: cyan;
  }
}

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L97-L105)
####  [](./v5/sass-api-reference/#govuk-until-breakpoint.md)govuk-until-breakpoint
Generate the `max-width` segment of a media query given a breakpoint key
sass-mq converted pixel values to ems, and only performed subtractions on named breakpoints. These have been retained for backwards compatibility, though unlike sass-mq, this also supports using non-px and em values.
#####  [](./v5/sass-api-reference/#govuk-until-breakpoint-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$until`  | If a string, expects the name of a breakpoint in $breakpoints. If a number, it will use that number.  |  `String` or `Number`  | —  |  
|  `$breakpoints`  | The map to look for $until.  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./v5/sass-api-reference/#govuk-until-breakpoint-example.md)Example

```
.example {
  @media #{govuk-until-breakpoint(desktop)} {
    color: red;
  }
  @media #{govuk-until-breakpoint(40em)} {
    color: green;
  }
  @media #{govuk-until-breakpoint(tablet)} and (orientation: landscape) {
    color: blue;
  }
  $custom-breakpoint-map: (
    small: 350px,
    medium: 769px,
    large: 1100px,
    extra-large: 1600px
  );
  @media #{govuk-until-breakpoint(extra-large, $custom-breakpoint-map)} {
    color: cyan;
  }
}

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L142-L156)
####  [](./v5/sass-api-reference/#govuk-media-query.md)govuk-media-query
Media query
#####  [](./v5/sass-api-reference/#govuk-media-query-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$from`  | One of $breakpoints  |  `String` or `Boolean`  | `false`  |  
|  `$until`  | One of $breakpoints  |  `String` or `Boolean`  | `false`  |  
|  `$and`  | Additional media query parameters  |  `String` or `Boolean`  | `false`  |  
|  `$media-type`  | Override media type: screen, print…  | `String`  | `all`  |  
|  `$breakpoints`  | Map of breakpoints to use  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./v5/sass-api-reference/#govuk-media-query-usage.md)Usage

```
@include govuk-media-query($from: false, $until: false, $and: false, $media-type: "all", $breakpoints: $govuk-breakpoints) {
  //..
}

```

#####  [](./v5/sass-api-reference/#govuk-media-query-example.md)Example

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
    color: rebeccapurple;
  }
}

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L192-L219)
###  [](./v5/sass-api-reference/#helpers-links.md)Links
####  [](./v5/sass-api-reference/#govuk-link-common.md)govuk-link-common
Common link styles
Provides the typography and focus state, regardless of link style.
#####  [](./v5/sass-api-reference/#govuk-link-common-usage.md)Usage

```
@include govuk-link-common;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L11-L22)
####  [](./v5/sass-api-reference/#govuk-link-decoration.md)govuk-link-decoration
Link decoration
Provides the text decoration for links, including thickness and underline offset. Use this mixin only if you cannot use the `govuk-link-common` mixin.
#####  [](./v5/sass-api-reference/#govuk-link-decoration-usage.md)Usage

```
@include govuk-link-decoration;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L30-L40)
####  [](./v5/sass-api-reference/#govuk-link-hover-decoration.md)govuk-link-hover-decoration
Link hover decoration
Provides the text decoration for links in their hover state, for you to use within a `:hover` pseudo-selector. Use this mixin only if you cannot use the `govuk-link-common` mixin.
#####  [](./v5/sass-api-reference/#govuk-link-hover-decoration-usage.md)Usage

```
@include govuk-link-hover-decoration;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L50-L60)
####  [](./v5/sass-api-reference/#govuk-link-style-default.md)govuk-link-style-default
Default link styles
Makes links use the default unvisited, visited, hover and active colours.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-default-usage.md)Usage

```
@include govuk-link-style-default;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-default-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-default;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L77-L99)
####  [](./v5/sass-api-reference/#govuk-link-style-error.md)govuk-link-style-error
Error link styles
Makes links use the error colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-error-usage.md)Usage

```
@include govuk-link-style-error;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-error-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-error;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L117-L136)
####  [](./v5/sass-api-reference/#govuk-link-style-success.md)govuk-link-style-success
Success link styles
Makes links use the success colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-success-usage.md)Usage

```
@include govuk-link-style-success;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-success-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-success;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L154-L173)
####  [](./v5/sass-api-reference/#govuk-link-style-muted.md)govuk-link-style-muted
Muted link styles
Makes links use the secondary text colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-muted-usage.md)Usage

```
@include govuk-link-style-muted;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-muted-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-muted;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L191-L207)
####  [](./v5/sass-api-reference/#govuk-link-style-text.md)govuk-link-style-text
Text link styles
Makes links use the primary text colour, in all states. Use this mixin for navigation components, such as breadcrumbs or the back link.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-text-usage.md)Usage

```
@include govuk-link-style-text;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-text-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-text;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L225-L243)
####  [](./v5/sass-api-reference/#govuk-link-style-inverse.md)govuk-link-style-inverse
Inverse link styles
Makes links white, in all states. Use this mixin if you’re displaying links against a dark background.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-inverse-usage.md)Usage

```
@include govuk-link-style-inverse;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-inverse-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-inverse;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L261-L277)
####  [](./v5/sass-api-reference/#govuk-link-style-no-visited-state.md)govuk-link-style-no-visited-state
Default link styles, without a visited state
Makes links use the default unvisited, hover and active colours, with no distinct visited state.
Use this mixin when it’s not helpful to distinguish between visited and non-visited links. For example, when you link to pages with frequently-changing content, such as the dashboard for an admin interface.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./v5/sass-api-reference/#govuk-link-style-no-visited-state-usage.md)Usage

```
@include govuk-link-style-no-visited-state;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-no-visited-state-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-no-visited-state;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L299-L321)
####  [](./v5/sass-api-reference/#govuk-link-style-no-underline.md)govuk-link-style-no-underline
Remove underline from links
Remove underlines from links unless the link is active or a user hovers their cursor over it.
#####  [](./v5/sass-api-reference/#govuk-link-style-no-underline-usage.md)Usage

```
@include govuk-link-style-no-underline;

```

#####  [](./v5/sass-api-reference/#govuk-link-style-no-underline-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-default;
  @include govuk-link-style-no-underline;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L337-L341)
####  [](./v5/sass-api-reference/#govuk-link-print-friendly.md)govuk-link-print-friendly
Include link destination when printing the page
If the user prints the page, add the destination URL after the link text, if the URL starts with `/`, `http://` or `https://`.
#####  [](./v5/sass-api-reference/#govuk-link-print-friendly-usage.md)Usage

```
@include govuk-link-print-friendly;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L350-L367)
####  [](./v5/sass-api-reference/#govuk-link-image.md)govuk-link-image
Image link styles
Prepares and provides the focus state for links that only contain images with no accompanying text.
#####  [](./v5/sass-api-reference/#govuk-link-image-usage.md)Usage

```
@include govuk-link-image;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L376-L389)
###  [](./v5/sass-api-reference/#shapes.md)Shapes
####  [](./v5/sass-api-reference/#govuk-shape-arrow.md)govuk-shape-arrow
Arrow mixin
Generate Arrows (triangles) by using a mix of transparent (1) and coloured borders. The coloured borders inherit the text colour of the element (2).
Ensure the arrow is rendered correctly if browser colours are overridden by providing a clip path (3). Without this the transparent borders are overridden to become visible which results in a square.
We need both because older browsers do not support clip-path.
#####  [](./v5/sass-api-reference/#govuk-shape-arrow-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$direction`  | Direction for arrow: up, right, down, left.  | `String`  | —  |  
|  `$base`  | Length of the triangle ‘base’ side  | `Number`  | —  |  
|  `$height`  | Height of triangle. Omit for equilateral.  | `Number`  | `null`  |  
|  `$display`  | CSS display property of the arrow  | `String`  | `block`  |  
#####  [](./v5/sass-api-reference/#govuk-shape-arrow-usage.md)Usage

```
@include govuk-shape-arrow($direction, $base, $height: null, $display: "block");

```

[ View source code for _shape-arrow.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_shape-arrow.scss#L38-L80)
###  [](./v5/sass-api-reference/#spacing.md)Spacing
####  [](./v5/sass-api-reference/#govuk-spacing.md)govuk-spacing
Single point spacing
Returns measurement corresponding to the spacing point requested.
#####  [](./v5/sass-api-reference/#govuk-spacing-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$spacing-point`  | Point on the spacing scale (set in `settings/_spacing.scss`)  | `Number`  | —  |  
#####  [](./v5/sass-api-reference/#govuk-spacing-example.md)Example

```
.element {
  padding: govuk-spacing(5);
}

```

#####  [](./v5/sass-api-reference/#example-using-negative-spacing.md)Example: Using negative spacing

```
.element {
  margin-top: govuk-spacing(-1);
}

```

#####  [](./v5/sass-api-reference/#example-marking-spacing-declarations-as-important.md)Example: Marking spacing declarations as important

```
.element {
  margin-top: govuk-spacing(1) !important;
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L31-L50)
####  [](./v5/sass-api-reference/#govuk-responsive-margin.md)govuk-responsive-margin
Responsive margin
Adds responsive margin by fetching a ‘spacing map’ from the responsive spacing scale, which defines different spacing values at different breakpoints. Wrapper for the `_govuk-responsive-spacing` mixin.
#####  [](./v5/sass-api-reference/#govuk-responsive-margin-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$responsive-spacing-point`  | Point on the responsive spacingscale, corresponds to a map of breakpoints and spacing values  | `Number`  | —  |  
|  `$direction`  | Direction to add spacing to (`top`, `right`, `bottom`, `left`, `all`)  | `String`  | `all`  |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `false`  |  
|  `$adjustment`  | Offset to adjust spacing by  | `Number`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-responsive-margin-usage.md)Usage

```
@include govuk-responsive-margin($responsive-spacing-point, $direction: "all", $important: false, $adjustment: false);

```

#####  [](./v5/sass-api-reference/#govuk-responsive-margin-example.md)Example

```
.element {
   @include govuk-responsive-margin(6, "left", $adjustment: 1px);
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L143-L145)
####  [](./v5/sass-api-reference/#govuk-responsive-padding.md)govuk-responsive-padding
Responsive padding
Adds responsive padding by fetching a ‘spacing map’ from the responsive spacing scale, which defines different spacing values at different breakpoints. Wrapper for the `_govuk-responsive-spacing` mixin.
#####  [](./v5/sass-api-reference/#govuk-responsive-padding-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$responsive-spacing-point`  | Point on the responsive spacing scale, corresponds to a map of breakpoints and spacing values  | `Number`  | —  |  
|  `$direction`  | Direction to add spacing to (`top`, `right`, `bottom`, `left`, `all`)  | `String`  | `all`  |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `false`  |  
|  `$adjustment`  | Offset to adjust spacing  | `Number`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-responsive-padding-usage.md)Usage

```
@include govuk-responsive-padding($responsive-spacing-point, $direction: "all", $important: false, $adjustment: false);

```

#####  [](./v5/sass-api-reference/#govuk-responsive-padding-example.md)Example

```
.element {
   @include govuk-responsive-padding(6, "left", $adjustment: 1px);
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L169-L171)
###  [](./v5/sass-api-reference/#helpers-typography.md)Typography
####  [](./v5/sass-api-reference/#govuk-typography-common.md)govuk-typography-common
‘Common typography’ helper
Sets the font family and associated properties, such as font smoothing. Also overrides the font for print.
#####  [](./v5/sass-api-reference/#govuk-typography-common-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$font-family`  | Font family to use  | `List`  | `$govuk-font-family`  |  
#####  [](./v5/sass-api-reference/#govuk-typography-common-usage.md)Usage

```
@include govuk-typography-common($font-family: $govuk-font-family);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L15-L29)
####  [](./v5/sass-api-reference/#helpers-typography-govuk-text-colour.md)govuk-text-colour
Text colour helper
Sets the text colour, including a suitable override for print.
#####  [](./v5/sass-api-reference/#helpers-typography-govuk-text-colour-usage.md)Usage

```
@include govuk-text-colour;

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L37-L43)
####  [](./v5/sass-api-reference/#govuk-typography-weight-regular.md)govuk-typography-weight-regular
Regular font weight helper
#####  [](./v5/sass-api-reference/#govuk-typography-weight-regular-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-typography-weight-regular-usage.md)Usage

```
@include govuk-typography-weight-regular($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L51-L53)
####  [](./v5/sass-api-reference/#govuk-typography-weight-bold.md)govuk-typography-weight-bold
Bold font weight helper
#####  [](./v5/sass-api-reference/#govuk-typography-weight-bold-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-typography-weight-bold-usage.md)Usage

```
@include govuk-typography-weight-bold($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L61-L63)
####  [](./v5/sass-api-reference/#govuk-font-tabular-numbers.md)govuk-font-tabular-numbers
Tabular number helper
Switches numerical glyphs (0–9) to use alternative forms with a monospaced bounding box. This ensures that columns of numbers, such as those in tables, remain horizontally aligned with one another. This also has the useful side effect of making numbers more legible in some situations, such as reference codes, as the numbers are more distinct and visually separated from one another.
#####  [](./v5/sass-api-reference/#govuk-font-tabular-numbers-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-font-tabular-numbers-usage.md)Usage

```
@include govuk-font-tabular-numbers($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L78-L80)
####  [](./v5/sass-api-reference/#govuk-text-break-word.md)govuk-text-break-word
Word break helper
Forcibly breaks long words that lack spaces, such as email addresses, across multiple lines when they wouldn’t otherwise fit.
#####  [](./v5/sass-api-reference/#govuk-text-break-word-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-text-break-word-usage.md)Usage

```
@include govuk-text-break-word($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L91-L97)
####  [](./v5/sass-api-reference/#govuk-typography-responsive.md)govuk-typography-responsive
Font size and line height helper
#####  [](./v5/sass-api-reference/#govuk-typography-responsive-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the type scale (the size as it would appear on tablet and above)  | `Number`  | —  |  
|  `$override-line-height`  | Non responsive custom line height. Omit to use the line height from the font map.  | `Number`  | `false`  |  
|  `$important`  | Whether to mark declarations as `!important`.  | `Boolean`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-typography-responsive-usage.md)Usage
! ** Warning
Deprecated: Use `govuk-font-size` instead
**

```
@include govuk-typography-responsive($size, $override-line-height: false, $important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L133-L139)
####  [](./v5/sass-api-reference/#govuk-font-size.md)govuk-font-size
Font size and line height helper
Takes a point from the responsive ‘font map’ as an argument (the size as it would appear on tablet and above), and uses it to create font-size and line-height declarations for different breakpoints, and print.
Example font map:

```
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
);

```

#####  [](./v5/sass-api-reference/#govuk-font-size-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the type scale (the size as it would appear on tablet and above)  |  `Number` or `String`  | —  |  
|  `$line-height`  | Non responsive custom line height. Omit to use the line height from the font map.  | `Number`  | `false`  |  
|  `$important`  | Whether to mark declarations as `!important`.  | `Boolean`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-font-size-usage.md)Usage

```
@include govuk-font-size($size, $line-height: false, $important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L177-L254)
####  [](./v5/sass-api-reference/#govuk-font.md)govuk-font
Font helper
#####  [](./v5/sass-api-reference/#govuk-font-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the type scale (the size as it would appear on tablet and above). Use `false` to avoid setting a size.  |  `Number` or `Boolean` or `String`  | —  |  
|  `$weight`  | Weight: `bold` or `regular`  | `String`  | `regular`  |  
|  `$tabular`  | Whether to use tabular numbers or not  | `Boolean`  | `false`  |  
|  `$line-height`  | Line-height, if overriding the default  | `Number`  | `false`  |  
#####  [](./v5/sass-api-reference/#govuk-font-usage.md)Usage

```
@include govuk-font($size, $weight: "regular", $tabular: false, $line-height: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L270-L286)
##  [](./v5/sass-api-reference/#components.md)Components
###  [](./v5/sass-api-reference/#button.md)Button
####  [](./v5/sass-api-reference/#govuk-button-background-colour.md)$govuk-button-background-colour
Button component background colour
#####  [](./v5/sass-api-reference/#govuk-button-background-colour-default-value.md)Default value

```
$govuk-button-background-colour: govuk-colour("green");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L10-L10)
####  [](./v5/sass-api-reference/#govuk-button-text-colour.md)$govuk-button-text-colour
Button component text colour
#####  [](./v5/sass-api-reference/#govuk-button-text-colour-default-value.md)Default value

```
$govuk-button-text-colour: govuk-colour("white");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L17-L17)
####  [](./v5/sass-api-reference/#govuk-inverse-button-background-colour.md)$govuk-inverse-button-background-colour
Inverted button component background colour
#####  [](./v5/sass-api-reference/#govuk-inverse-button-background-colour-default-value.md)Default value

```
$govuk-inverse-button-background-colour: govuk-colour("white");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L24-L24)
####  [](./v5/sass-api-reference/#govuk-inverse-button-text-colour.md)$govuk-inverse-button-text-colour
Inverted button component text colour
#####  [](./v5/sass-api-reference/#govuk-inverse-button-text-colour-default-value.md)Default value

```
$govuk-inverse-button-text-colour: $govuk-brand-colour;

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L31-L31)
##  [](./v5/sass-api-reference/#objects.md)Objects
###  [](./v5/sass-api-reference/#objects-layout.md)Layout
####  [](./v5/sass-api-reference/#govuk-width-container.md)govuk-width-container
Width container mixin
Used to create page width and custom width container classes.
#####  [](./v5/sass-api-reference/#govuk-width-container-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$width`  | Width in pixels  | `String`  | `$govuk-page-width`  |  
#####  [](./v5/sass-api-reference/#govuk-width-container-usage.md)Usage

```
@include govuk-width-container($width: "$govuk-page-width");

```

#####  [](./v5/sass-api-reference/#example-creating-a-1200px-wide-container-class.md)Example: Creating a 1200px wide container class

```
.app-width-container--wide {
  @include govuk-width-container(1200px);
}

```

[ View source code for _width-container.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/objects/_width-container.scss#L20-L69)
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v5/sass-api-reference/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Sass+API+reference%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv5%2Fsass-api-reference%2F%29&labels=bug&title=Re%3A+%27Sass+API+reference%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
