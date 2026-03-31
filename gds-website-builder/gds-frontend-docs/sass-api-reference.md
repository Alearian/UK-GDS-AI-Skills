#  [](./sass-api-reference/#sass-api-reference.md)Sass API reference
##  [](./sass-api-reference/#settings.md)Settings
###  [](./sass-api-reference/#assets.md)Assets
####  [](./sass-api-reference/#govuk-assets-path.md)$govuk-assets-path
Path to the assets directory, with trailing slash.
This is the directory where the images and fonts subdirectories live. You will need to make this directory available via your application – see the README for details.
#####  [](./sass-api-reference/#default-value.md)Default value

```
$govuk-assets-path: "/assets/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L14-L14)
####  [](./sass-api-reference/#govuk-images-path.md)$govuk-images-path
Path to the images folder, with trailing slash.
#####  [](./sass-api-reference/#govuk-images-path-default-value.md)Default value

```
$govuk-images-path: "#{$govuk-assets-path}images/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L21-L21)
####  [](./sass-api-reference/#govuk-fonts-path.md)$govuk-fonts-path
Path to the fonts folder, with trailing slash.
#####  [](./sass-api-reference/#govuk-fonts-path-default-value.md)Default value

```
$govuk-fonts-path: "#{$govuk-assets-path}fonts/";

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L28-L28)
####  [](./sass-api-reference/#govuk-image-url-function.md)$govuk-image-url-function
Custom image URL function
If the built-in image URL helper does not meet your needs, you can specify the name of a custom handler – either built in or by writing your own function.
If you are writing your own handler, ensure that it returns a string wrapped with `url()`
#####  [](./sass-api-reference/#govuk-image-url-function-default-value.md)Default value

```
$govuk-image-url-function: false;

```

#####  [](./sass-api-reference/#example-rails-asset-handling.md)Example: Rails asset handling

```
$govuk-image-url-function: 'image-url';

```

#####  [](./sass-api-reference/#example-custom-asset-handling.md)Example: Custom asset handling

```
@function my-url-handler($filename) {
  // Some custom URL handling
  @return url('example.jpg');
}

$govuk-image-url-function: 'my-url-handler';

```

#####  [](./sass-api-reference/#example-from-an-external-module.md)Example: From an external module

```
@use "sass:meta";
// Include the module containing the handler function
@use "url-handlers";

// Then pass the handler function using `meta.get-function`
$govuk-image-url-function: meta.get-function("image-url", $module: "url-handlers");

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L64-L64)
####  [](./sass-api-reference/#govuk-font-url-function.md)$govuk-font-url-function
Custom font URL function
If the built-in font URL helper does not meet your needs, you can specify the name of a custom handler – either built in or by writing your own function.
If you are writing your own handler, ensure that it returns a string wrapped with `url()`
#####  [](./sass-api-reference/#govuk-font-url-function-default-value.md)Default value

```
$govuk-font-url-function: false;

```

#####  [](./sass-api-reference/#govuk-font-url-function-example-rails-asset-handling.md)Example: Rails asset handling

```
$govuk-font-url-function: 'font-url';

```

#####  [](./sass-api-reference/#govuk-font-url-function-example-custom-asset-handling.md)Example: Custom asset handling

```
@function my-url-handler($filename) {
  // Some custom URL handling
  @return url('example.woff');
}

$govuk-font-url-function: 'my-url-handler';

```

#####  [](./sass-api-reference/#govuk-font-url-function-example-from-an-external-module.md)Example: From an external module

```
@use "sass:meta";
// Include the module containing the handler function
@use "url-handlers";

// Then pass the handler function using `meta.get-function`
$govuk-font-url-function: meta.get-function("font-url", $module: "url-handlers");

```

[ View source code for _assets.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_assets.scss#L100-L100)
###  [](./sass-api-reference/#colours.md)Colours
####  [](./sass-api-reference/#govuk-default-functional-colours.md)$govuk-default-functional-colours
Default definitions of the functional colours
#####  [](./sass-api-reference/#govuk-default-functional-colours-default-value.md)Default value

```
$govuk-default-functional-colours: (
  (
    "brand": (
      name: "blue"
    ),
    "text": (
      name: "black"
    ),
    // The background colour of the template. This is intended to be the same
    // as `surface-background` for the purposes of making the Footer and Cookie
    // banner components merge seamlessly with the template.
    "template-background": (
        name: "blue",
        variant: "tint-95"
      ),
    "body-background": (
      name: "white"
    ),
    // Use 'true black' to avoid printers using colour ink to print body text
    "print-text": #000000,
    // Used in for example 'muted' text and help text.
    "secondary-text": (
        name: "black",
        variant: "tint-25"
      ),
    // Used for outline (and background, where appropriate) when interactive
    // elements (links, form controls) have keyboard focus.
    "focus": (
        name: "yellow"
      ),
    // Ensure that the contrast between the text and background colour passes
    // WCAG Level AA contrast requirements.
    "focus-text": (
        name: "black"
      ),
    // Used to highlight error messages and form controls in an error state
    "error": (
        name: "red"
      ),
    // Used to highlight success messages and banners
    "success": (
        name: "green"
      ),
    // Used in for example borders, separators, rules and keylines.
    "border": (
        name: "black",
        variant: "tint-80"
      ),
    // Used for form inputs and controls
    "input-border": (
        name: "black"
      ),
    // Used for hover states on form controls
    "hover": (
        name: "black",
        variant: "tint-80"
      ),
    // Standard links (on white)
    "link": (
        name: "blue",
        variant: "shade-10"
      ),
    "link-visited": (
      name: "purple"
    ),
    "link-hover": (
      name: "blue",
      variant: "shade-50"
    ),
    "link-active": (
      name: "black"
    ),
    // 'Surfaces' are our name for components that have different colour
    // palettes to typical page content. This is the generic surface.
    "surface-background": (
        name: "blue",
        variant: "tint-95"
      ),
    "surface-text": (
      name: "black"
    ),
    "surface-border": (
      name: "blue",
      variant: "tint-50"
    )
  )
);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L17-L103)
####  [](./sass-api-reference/#govuk-functional-colours.md)$govuk-functional-colours
Functional colours for the GOV.UK palette.
Each functional colour is represented by a name (for example `'brand'`) to which the map associates either:
  * a Sass colour (like `#1d70b8`)
  * a Sass map with a `name` and an optional `variant` properties, referring to one of the colours in the colour palette (like `(name: 'blue', variant: 'primary')`). `variant` defaults to `'primary'` if omitted.

Use the `govuk-functional-colour` function to access these colours.
Customise functional colours by defining $govuk-functional-colours with a map of the colours that you want to change before importing GOV.UK Frontend. These will then be merged with the default colours. You can only redefine existing colours.
#####  [](./sass-api-reference/#govuk-functional-colours-default-value.md)Default value

```
$govuk-functional-colours: $govuk-default-functional-colours;

```

#####  [](./sass-api-reference/#example-redefining-functional-colours-by-setting-them-before-import.md)Example: – Redefining functional colours by setting them before import

```
// These will be merged with the default functional colours
$govuk-functional-colours: (
  // set the 'brand' colour to the 'primary' variant of 'purple'
  brand: (name: 'purple'),
  // set the 'template-background' colour to the 'tint-95' variant of 'purple'
  template-background: (name: 'purple', variant: 'tint-95'),
  // set the 'text' colour to an arbitrary colour `#221133`
  text: #221133
);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L160-L160)
####  [](./sass-api-reference/#govuk-brand-colour.md)$govuk-brand-colour
Brand colour
#####  [](./sass-api-reference/#usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(brand)`.
**
#####  [](./sass-api-reference/#govuk-brand-colour-default-value.md)Default value

```
$govuk-brand-colour: govuk-functional-colour(brand);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L205-L205)
####  [](./sass-api-reference/#govuk-text-colour.md)$govuk-text-colour
Text colour
#####  [](./sass-api-reference/#govuk-text-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(text)`.
**
#####  [](./sass-api-reference/#govuk-text-colour-default-value.md)Default value

```
$govuk-text-colour: govuk-functional-colour(text);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L215-L215)
####  [](./sass-api-reference/#govuk-template-background-colour.md)$govuk-template-background-colour
Template background colour
Used by components that want to give the illusion of extending the template background (such as the footer and cookie banner).
#####  [](./sass-api-reference/#govuk-template-background-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(template-background)`.
**
#####  [](./sass-api-reference/#govuk-template-background-colour-default-value.md)Default value

```
$govuk-template-background-colour: govuk-functional-colour(template-background);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L228-L228)
####  [](./sass-api-reference/#govuk-body-background-colour.md)$govuk-body-background-colour
Body background colour
#####  [](./sass-api-reference/#govuk-body-background-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(body-background)`.
**
#####  [](./sass-api-reference/#govuk-body-background-colour-default-value.md)Default value

```
$govuk-body-background-colour: govuk-functional-colour(body-background);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L238-L238)
####  [](./sass-api-reference/#govuk-print-text-colour.md)$govuk-print-text-colour
Text colour for print media
Use ‘true black’ to avoid printers using colour ink to print body text
#####  [](./sass-api-reference/#govuk-print-text-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(print-text)`.
**
#####  [](./sass-api-reference/#govuk-print-text-colour-default-value.md)Default value

```
$govuk-print-text-colour: govuk-functional-colour(print-text);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L250-L250)
####  [](./sass-api-reference/#govuk-secondary-text-colour.md)$govuk-secondary-text-colour
Secondary text colour
Used in for example ‘muted’ text and help text.
#####  [](./sass-api-reference/#govuk-secondary-text-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(secondary-text)`.
**
#####  [](./sass-api-reference/#govuk-secondary-text-colour-default-value.md)Default value

```
$govuk-secondary-text-colour: govuk-functional-colour(secondary-text);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L262-L262)
####  [](./sass-api-reference/#govuk-focus-colour.md)$govuk-focus-colour
Focus colour
Used for outline (and background, where appropriate) when interactive elements (links, form controls) have keyboard focus.
#####  [](./sass-api-reference/#govuk-focus-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(focus)`.
**
#####  [](./sass-api-reference/#govuk-focus-colour-default-value.md)Default value

```
$govuk-focus-colour: govuk-functional-colour(focus);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L275-L275)
####  [](./sass-api-reference/#govuk-focus-text-colour.md)$govuk-focus-text-colour
Focused text colour
Ensure that the contrast between the text and background colour passes WCAG Level AA contrast requirements.
#####  [](./sass-api-reference/#govuk-focus-text-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(focus-text)`.
**
#####  [](./sass-api-reference/#govuk-focus-text-colour-default-value.md)Default value

```
$govuk-focus-text-colour: govuk-functional-colour(focus-text);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L288-L288)
####  [](./sass-api-reference/#govuk-error-colour.md)$govuk-error-colour
Error colour
Used to highlight error messages and form controls in an error state
#####  [](./sass-api-reference/#govuk-error-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(error)`.
**
#####  [](./sass-api-reference/#govuk-error-colour-default-value.md)Default value

```
$govuk-error-colour: govuk-functional-colour(error);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L300-L300)
####  [](./sass-api-reference/#govuk-success-colour.md)$govuk-success-colour
Success colour
Used to highlight success messages and banners
#####  [](./sass-api-reference/#govuk-success-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(error)`.
**
#####  [](./sass-api-reference/#govuk-success-colour-default-value.md)Default value

```
$govuk-success-colour: govuk-functional-colour(success);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L312-L312)
####  [](./sass-api-reference/#govuk-border-colour.md)$govuk-border-colour
Border colour
Used in for example borders, separators, rules and keylines.
#####  [](./sass-api-reference/#govuk-border-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(border)`.
**
#####  [](./sass-api-reference/#govuk-border-colour-default-value.md)Default value

```
$govuk-border-colour: govuk-functional-colour(border);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L324-L324)
####  [](./sass-api-reference/#govuk-input-border-colour.md)$govuk-input-border-colour
Input border colour
Used for form inputs and controls
#####  [](./sass-api-reference/#govuk-input-border-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(input-border)`.
**
#####  [](./sass-api-reference/#govuk-input-border-colour-default-value.md)Default value

```
$govuk-input-border-colour: govuk-functional-colour(input-border);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L336-L336)
####  [](./sass-api-reference/#govuk-hover-colour.md)$govuk-hover-colour
Input hover colour
Used for hover states on form controls
#####  [](./sass-api-reference/#govuk-hover-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(hover)`.
**
#####  [](./sass-api-reference/#govuk-hover-colour-default-value.md)Default value

```
$govuk-hover-colour: govuk-functional-colour(hover);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L348-L348)
####  [](./sass-api-reference/#govuk-link-colour.md)$govuk-link-colour
Link colour
#####  [](./sass-api-reference/#govuk-link-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(link)`.
**
#####  [](./sass-api-reference/#govuk-link-colour-default-value.md)Default value

```
$govuk-link-colour: govuk-functional-colour(link);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L358-L358)
####  [](./sass-api-reference/#govuk-link-visited-colour.md)$govuk-link-visited-colour
Visited link colour
#####  [](./sass-api-reference/#govuk-link-visited-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(link-visited)`.
**
#####  [](./sass-api-reference/#govuk-link-visited-colour-default-value.md)Default value

```
$govuk-link-visited-colour: govuk-functional-colour(link-visited);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L368-L368)
####  [](./sass-api-reference/#govuk-link-hover-colour.md)$govuk-link-hover-colour
Link hover colour
#####  [](./sass-api-reference/#govuk-link-hover-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(link-hover)`.
**
#####  [](./sass-api-reference/#govuk-link-hover-colour-default-value.md)Default value

```
$govuk-link-hover-colour: govuk-functional-colour(link-hover);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L378-L378)
####  [](./sass-api-reference/#govuk-link-active-colour.md)$govuk-link-active-colour
Active link colour
#####  [](./sass-api-reference/#govuk-link-active-colour-usage.md)Usage
! ** Warning
Deprecated: Variables for applied colours are deprecated. Please use the `govuk-functional-colour` function instead: `govuk-functional-colour(link-active)`.
**
#####  [](./sass-api-reference/#govuk-link-active-colour-default-value.md)Default value

```
$govuk-link-active-colour: govuk-functional-colour(link-active);

```

[ View source code for _colours-functional.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-functional.scss#L388-L388)
####  [](./sass-api-reference/#govuk-colours-organisations.md)$govuk-colours-organisations
Organisation colour palette
#####  [](./sass-api-reference/#govuk-colours-organisations-default-value.md)Default value

```
$govuk-colours-organisations: (
  "attorney-generals-office": (
    colour: #a91c8e
  ),
  "cabinet-office": (
    colour: #0056b8
  ),
  "civil-service": (
    colour: #b2292e
  ),
  "department-for-business-trade": (
    colour: #e52d13,
    contrast-safe: #e02c13
  ),
  "department-for-culture-media-sport": (
    colour: #ed1588,
    contrast-safe: #d6177a
  ),
  "department-for-education": (
    colour: #003764
  ),
  "department-for-energy-security-net-zero": (
    colour: #003479
  ),
  "department-for-environment-food-rural-affairs": (
    colour: #00a33b,
    contrast-safe: #008531
  ),
  "department-for-science-innovation-technology": (
    colour: #00f8f8,
    contrast-safe: #008180
  ),
  "department-for-transport": (
    colour: #006853
  ),
  "department-for-work-pensions": (
    colour: #00bcb5,
    contrast-safe: #00857e
  ),
  "department-of-health-social-care": (
    colour: #00a990,
    contrast-safe: #008674
  ),
  "foreign-commonwealth-development-office": (
    colour: #012069
  ),
  "hm-government": (
    colour: #266ebc
  ),
  "hm-revenue-customs": (
    colour: #008670
  ),
  "hm-treasury": (
    colour: #b2292e
  ),
  "home-office": (
    colour: #732282
  ),
  "ministry-of-defence": (
    colour: #532a45
  ),
  "ministry-of-housing-communities-local-government": (
    colour: #00625e
  ),
  "ministry-of-justice": (
    colour: #000000
  ),
  "northern-ireland-office": (
    colour: #00205c
  ),
  "office-of-the-advocate-general-for-scotland": (
    colour: #00205c
  ),
  "office-of-the-leader-of-the-house-of-commons": (
    colour: #497629
  ),
  "office-of-the-leader-of-the-house-of-lords": (
    colour: #9c182f
  ),
  "prime-ministers-office-10-downing-street": (
    colour: #0b0c0c
  ),
  "scotland-office": (
    colour: #00205c
  ),
  "serious-fraud-office": (
    colour: #82368c
  ),
  "uk-export-finance": (
    colour: #cf102d
  ),
  "wales-office": (
    colour: #a33038
  )
);

```

[ View source code for _colours-organisations.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_colours-organisations.scss#L22-L116)
###  [](./sass-api-reference/#custom-properties.md)Custom properties
####  [](./sass-api-reference/#govuk-output-custom-properties.md)$govuk-output-custom-properties
Output CSS custom properties
Whether to output CSS Custom Properties in the compiled stylesheet.
If you are compiling multiple stylesheets that will be used together on a page, set this to false in any secondary stylesheets to avoid including the Custom Properties multiple times.
#####  [](./sass-api-reference/#govuk-output-custom-properties-default-value.md)Default value

```
$govuk-output-custom-properties: true;

```

[ View source code for _custom-properties.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_custom-properties.scss#L16-L16)
###  [](./sass-api-reference/#global-styles.md)Global styles
####  [](./sass-api-reference/#govuk-global-styles.md)$govuk-global-styles
Include ‘global’ styles
Whether to style paragraphs (`<p>`) and links (`<a>`) without explicitly having to apply the `govuk-body` and `govuk-link` classes.
#####  [](./sass-api-reference/#govuk-global-styles-default-value.md)Default value

```
$govuk-global-styles: false;

```

[ View source code for _global-styles.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_global-styles.scss#L13-L13)
###  [](./sass-api-reference/#layout.md)Layout
####  [](./sass-api-reference/#govuk-grid-widths.md)$govuk-grid-widths
Map of grid column widths
#####  [](./sass-api-reference/#govuk-grid-widths-default-value.md)Default value

```
$govuk-grid-widths: (
  one-quarter: math.div(100%, 4),
  one-third: math.div(100%, 3),
  one-half: math.div(100%, 2),
  two-thirds: math.div(200%, 3),
  three-quarters: math.div(300%, 4),
  full: 100%
);

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L23-L30)
####  [](./sass-api-reference/#govuk-gutter.md)$govuk-gutter
Width of gutter between grid columns
#####  [](./sass-api-reference/#govuk-gutter-default-value.md)Default value

```
$govuk-gutter: 30px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L37-L37)
####  [](./sass-api-reference/#govuk-gutter-half.md)$govuk-gutter-half
Width of half the gutter between grid columns
#####  [](./sass-api-reference/#govuk-gutter-half-default-value.md)Default value

```
$govuk-gutter-half: math.div($govuk-gutter, 2);

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L44-L44)
####  [](./sass-api-reference/#govuk-border-width.md)$govuk-border-width
Standard border width
#####  [](./sass-api-reference/#govuk-border-width-default-value.md)Default value

```
$govuk-border-width: 5px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L55-L55)
####  [](./sass-api-reference/#govuk-border-width-wide.md)$govuk-border-width-wide
Wide border width
#####  [](./sass-api-reference/#govuk-border-width-wide-default-value.md)Default value

```
$govuk-border-width-wide: 10px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L62-L62)
####  [](./sass-api-reference/#govuk-border-width-narrow.md)$govuk-border-width-narrow
Narrow border width
#####  [](./sass-api-reference/#govuk-border-width-narrow-default-value.md)Default value

```
$govuk-border-width-narrow: 4px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L69-L69)
####  [](./sass-api-reference/#govuk-border-width-form-element.md)$govuk-border-width-form-element
Form control border width
#####  [](./sass-api-reference/#govuk-border-width-form-element-default-value.md)Default value

```
$govuk-border-width-form-element: 2px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L76-L76)
####  [](./sass-api-reference/#govuk-border-width-form-group-error.md)$govuk-border-width-form-group-error
Form group border width when in error state
#####  [](./sass-api-reference/#govuk-border-width-form-group-error-default-value.md)Default value

```
$govuk-border-width-form-group-error: $govuk-border-width;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L83-L83)
####  [](./sass-api-reference/#govuk-focus-width.md)$govuk-focus-width
Border width of focus outline
#####  [](./sass-api-reference/#govuk-focus-width-default-value.md)Default value

```
$govuk-focus-width: 3px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L90-L90)
####  [](./sass-api-reference/#govuk-hover-width.md)$govuk-hover-width
Hover width for form controls with a hover state
#####  [](./sass-api-reference/#govuk-hover-width-default-value.md)Default value

```
$govuk-hover-width: 10px;

```

[ View source code for _measurements.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_measurements.scss#L97-L97)
####  [](./sass-api-reference/#govuk-breakpoints.md)$govuk-breakpoints
Breakpoint definitions
#####  [](./sass-api-reference/#govuk-breakpoints-default-value.md)Default value

```
$govuk-breakpoints: (
  mobile: 320px,
  tablet: 641px,
  desktop: 769px
);

```

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_media-queries.scss#L10-L14)
###  [](./sass-api-reference/#links.md)Links
####  [](./sass-api-reference/#govuk-link-underline-thickness.md)$govuk-link-underline-thickness
Thickness of link underlines
The default will be either:
  * 1px
  * 0.0625rem, if it’s thicker than 1px because the user has changed the text size in their browser

Set this variable to `false` to avoid setting a thickness.
#####  [](./sass-api-reference/#govuk-link-underline-thickness-default-value.md)Default value

```
$govuk-link-underline-thickness: string.unquote("max(1px, .0625rem)");

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L19-L19)
####  [](./sass-api-reference/#govuk-link-underline-offset.md)$govuk-link-underline-offset
Offset of link underlines from text baseline
The default is 3px expressed as ems, as calculated against the default body font size (on desktop) of 19px. 3 ÷ 19 = 0.1578
Set this variable to `false` to avoid setting an offset.
#####  [](./sass-api-reference/#govuk-link-underline-offset-default-value.md)Default value

```
$govuk-link-underline-offset: 0.1578em;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L32-L32)
####  [](./sass-api-reference/#govuk-link-hover-underline-thickness.md)$govuk-link-hover-underline-thickness
Thickness of link underlines in hover state
The default for each link will be the thickest of the following:
  * 3px
  * 0.1875rem, if it’s thicker than 3px because the user has changed the text size in their browser
  * 0.12em (relative to the link’s text size)

Set this variable to `false` to avoid setting a thickness.
#####  [](./sass-api-reference/#govuk-link-hover-underline-thickness-default-value.md)Default value

```
$govuk-link-hover-underline-thickness: string.unquote("max(3px, .1875rem, .12em)");

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_links.scss#L48-L48)
###  [](./sass-api-reference/#typography.md)Typography
####  [](./sass-api-reference/#govuk-font-family.md)$govuk-font-family
Font families to use for all typography on screen media
#####  [](./sass-api-reference/#govuk-font-family-default-value.md)Default value

```
$govuk-font-family: "GDS Transport", arial, sans-serif;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L17-L17)
####  [](./sass-api-reference/#govuk-font-family-print.md)$govuk-font-family-print
Font families to use for print media
We recommend that you use system fonts when printing. This will avoid issues with some printer drivers and operating systems.
#####  [](./sass-api-reference/#govuk-font-family-print-default-value.md)Default value

```
$govuk-font-family-print: sans-serif;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L27-L27)
####  [](./sass-api-reference/#govuk-include-default-font-face.md)$govuk-include-default-font-face
Include the default @font-face declarations
Defaults to true if “GDS Transport” appears in the $govuk-font-family setting.
#####  [](./sass-api-reference/#govuk-include-default-font-face-default-value.md)Default value

```
$govuk-include-default-font-face: govuk-if(list.index($govuk-font-family, "GDS Transport"), true, false);

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L37-L37)
####  [](./sass-api-reference/#govuk-font-weight-regular.md)$govuk-font-weight-regular
Font weight for regular typography
#####  [](./sass-api-reference/#govuk-font-weight-regular-default-value.md)Default value

```
$govuk-font-weight-regular: 400;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L47-L47)
####  [](./sass-api-reference/#govuk-font-weight-bold.md)$govuk-font-weight-bold
Font weight for bold typography
#####  [](./sass-api-reference/#govuk-font-weight-bold-default-value.md)Default value

```
$govuk-font-weight-bold: 700;

```

[ View source code for _typography-font.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-font.scss#L53-L53)
####  [](./sass-api-reference/#govuk-root-font-size.md)$govuk-root-font-size
Root font size
This is used to calculate rem sizes for the typography, and should match the _effective_ font-size of your root (or html) element.
Ideally you should not be setting the font-size on the html or root element in order to allow it to scale with user-preference, in which case this should be set to 16px.
#####  [](./sass-api-reference/#govuk-root-font-size-default-value.md)Default value

```
$govuk-root-font-size: 16px;

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L17-L17)
####  [](./sass-api-reference/#govuk-typography-scale.md)$govuk-typography-scale
Responsive typography font map
This is used to generate responsive typography that adapts according to the breakpoints.
Font size and font weight can be defined for each breakpoint. You can define different behaviour on tablet and desktop. The ‘null’ breakpoint is for mobile.
Line-heights will automatically be converted from pixel measurements into relative values. For example, with a font-size of 16px and a line-height of 24px, the line-height will be converted to 1.5 before output.
You can also specify a separate font size and line height for print media.
#####  [](./sass-api-reference/#govuk-typography-scale-default-value.md)Default value

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
      font-size: 27px,
      line-height: 30px
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
    // Made same as 24 on mobile (consider deprecating this size)
    null: (
        font-size: 21px,
        line-height: 25px
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
    // Bump up mobile size from 18/20 to 21/25
    null: (
        font-size: 21px,
        line-height: 25px
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
    // Stay at 19/25 at all sizes
    null: (
        font-size: 19px,
        line-height: 25px
      ),
    print: (
      font-size: 14pt,
      line-height: 1.15
    )
  ),
  16: (
    // Stay at 16/20 at all sizes
    null: (
        font-size: 16px,
        line-height: 20px
      ),
    print: (
      font-size: 14pt,
      line-height: 1.2
    )
  )
);

```

[ View source code for _typography-responsive.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss#L43-L138)
###  [](./sass-api-reference/#warnings.md)Warnings
####  [](./sass-api-reference/#govuk-suppressed-warnings.md)$govuk-suppressed-warnings
Suppressed warnings map
This map is used to determine which deprecation warnings to **not** show to users when compiling sass. This is in place for codebases that do not have the necessary capacity to upgrade and remove the deprecation, particularly if the deprecation is significant. For example, the removal of mixins and functions that were previously available to users of Frontend.
You can add to this map and define which warnings to suppress by appending to it using the warning key, found in the warning message. For example:
#####  [](./sass-api-reference/#govuk-suppressed-warnings-default-value.md)Default value

```
$govuk-suppressed-warnings: ();

```

#####  [](./sass-api-reference/#example.md)Example: :

```
// warning message:
//  $foobar is no longer supported. To silence this warning, update
//  $govuk-suppressed-warnings with key: "foobar"
$govuk-suppressed-warnings: (
  foobar
);

```

[ View source code for _warnings.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/settings/_warnings.scss#L28-L28)
##  [](./sass-api-reference/#tools.md)Tools
###  [](./sass-api-reference/#general-tools.md)General tools
####  [](./sass-api-reference/#govuk-exports.md)govuk-exports
Export module
Ensure that the modules of CSS that we define throughout Frontend are only included in the generated CSS once, no matter how many times they are imported across the individual components.
#####  [](./sass-api-reference/#parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$name`  | Name of module - must be unique within the codebase  | `String`  | —  |  
#####  [](./sass-api-reference/#govuk-exports-usage.md)Usage

```
@include govuk-exports($name) {
  //..
}

```

[ View source code for _exports.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_exports.scss#L24-L34)
###  [](./sass-api-reference/#tools-assets.md)Assets
####  [](./sass-api-reference/#govuk-font-url.md)govuk-font-url
Font URL
If a custom font-url handler is defined ($govuk-font-url-function) then it will be called, otherwise a url will be returned with the filename appended to the font path.
#####  [](./sass-api-reference/#govuk-font-url-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$filename`  | Font filename  | `String`  | —  |  
[ View source code for _font-url.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_font-url.scss#L16-L34)
####  [](./sass-api-reference/#govuk-image-url.md)govuk-image-url
Image URL
If a custom image-url handler is defined ($govuk-image-url-function) then it will be called, otherwise a url will be returned with the filename appended to the image path.
#####  [](./sass-api-reference/#govuk-image-url-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$Filename`  | for the image to load  | `String`  | —  |  
[ View source code for _image-url.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_image-url.scss#L16-L34)
###  [](./sass-api-reference/#if.md)If
####  [](./sass-api-reference/#govuk-if.md)govuk-if
Inline `if` function
Replicates the syntax of the original Sass `if` function to support Sass `>=1.79 <1.95`. Defaults `$if-false` to `null` when not set.
#####  [](./sass-api-reference/#govuk-if-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$condition`  | The condition  | `Boolean`  | —  |  
|  `$if-true`  | The value if the condition is met  | `any`  | —  |  
|  `$if-false`  | The value if the condition is not met, defaults to `null`.  | `any`  | `null`  |  
[ View source code for _if.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_if.scss#L16-L22)
###  [](./sass-api-reference/#unit-conversion.md)Unit conversion
####  [](./sass-api-reference/#govuk-em.md)govuk-em
Convert pixels to em
#####  [](./sass-api-reference/#govuk-em-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | Length in pixels  | `Number`  | —  |  
|  `$context-font-size`  | Font size of element  | `Number`  | `$govuk-root-font-size`  |  
[ View source code for _px-to-em.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_px-to-em.scss#L16-L24)
####  [](./sass-api-reference/#govuk-px-to-rem.md)govuk-px-to-rem
Convert pixels to rem
The $govuk-root-font-size (defined in settings/_typography-responsive.scss) must be configured to match the font-size of your root (html) element
#####  [](./sass-api-reference/#govuk-px-to-rem-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | Length in pixels  | `Number`  | —  |  
[ View source code for _px-to-rem.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/tools/_px-to-rem.scss#L18-L24)
##  [](./sass-api-reference/#helpers.md)Helpers
###  [](./sass-api-reference/#accessibility.md)Accessibility
####  [](./sass-api-reference/#govuk-focused-text.md)govuk-focused-text
Focused text
Provides an outline to clearly indicate when the target element is focused. Used for interactive text-based elements.
#####  [](./sass-api-reference/#govuk-focused-text-usage.md)Usage

```
@include govuk-focused-text;

```

#####  [](./sass-api-reference/#example-styling-the-focus-state-for-a-link.md)Example: Styling the focus state for a link

```
.govuk-link:focus {
  @include govuk-focused-text;
}

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L17-L46)
####  [](./sass-api-reference/#govuk-focused-box.md)govuk-focused-box
Focused box
Provides an outline to clearly indicate when the target element is focused. Unlike govuk-focused-text, which only draws an underline below the element, govuk-focused-box draws an outline around all sides of the element. Best used for non-text content contained within links.
#####  [](./sass-api-reference/#govuk-focused-box-usage.md)Usage

```
@include govuk-focused-box;

```

#####  [](./sass-api-reference/#example-styling-the-focus-state-for-a-linked-image.md)Example: Styling the focus state for a linked image

```
.govuk-link-image:focus {
  @include govuk-focused-box;
}

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L62-L67)
####  [](./sass-api-reference/#govuk-focused-form-input.md)govuk-focused-form-input
Focused form input
Provides an outline to clearly indicate when the target element is focused. Used for form inputs.
#####  [](./sass-api-reference/#govuk-focused-form-input-usage.md)Usage

```
@include govuk-focused-form-input;

```

#####  [](./sass-api-reference/#example-styling-the-focus-state-for-a-form-input.md)Example: Styling the focus state for a form input

```
.govuk-input:focus {
  @include govuk-focused-form-input;
}

```

[ View source code for _focused.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_focused.scss#L81-L92)
####  [](./sass-api-reference/#govuk-visually-hidden.md)govuk-visually-hidden
Hide an element visually, but have it available for screen readers
#####  [](./sass-api-reference/#govuk-visually-hidden-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `true`  |  
#####  [](./sass-api-reference/#govuk-visually-hidden-usage.md)Usage

```
@include govuk-visually-hidden($important: true);

```

[ View source code for _visually-hidden.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_visually-hidden.scss#L56-L70)
####  [](./sass-api-reference/#govuk-visually-hidden-focusable.md)govuk-visually-hidden-focusable
Hide an element visually, but have it available for screen readers whilst allowing the element to be focused when navigated to via the keyboard (e.g. for the skip link)
#####  [](./sass-api-reference/#govuk-visually-hidden-focusable-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `true`  |  
#####  [](./sass-api-reference/#govuk-visually-hidden-focusable-usage.md)Usage

```
@include govuk-visually-hidden-focusable($important: true);

```

[ View source code for _visually-hidden.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_visually-hidden.scss#L80-L88)
###  [](./sass-api-reference/#colour.md)Colour
####  [](./sass-api-reference/#govuk-colour.md)govuk-colour
Get a colour from the palette
Before using this function, check if your use case is covered by a functional colour. For example, use `govuk-functional-colour("link")` for links rather than `govuk-colour("blue")`.
#####  [](./sass-api-reference/#govuk-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | Name of colour from the colour palette (`$_govuk-palette`)  |  `String` or `Colour`  | —  |  
|  `$variant`  | Name of the variant from the colour palette (`$_govuk-palette`)  |  `String` or `Colour`  | —  |  
#####  [](./sass-api-reference/#example-getting-the-primary-variant-of-a-colour.md)Example: Getting the primary variant of a colour

```
.my-component {
  color: govuk-colour("blue");
}

```

#####  [](./sass-api-reference/#example-getting-a-50-shade-of-blue.md)Example: Getting a 50% shade of blue

```
.my-component {
  color: govuk-colour("blue", $variant: "shade-50")
}

```

[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L41-L80)
####  [](./sass-api-reference/#govuk-functional-colour.md)govuk-functional-colour
Get a functional colour
#####  [](./sass-api-reference/#govuk-functional-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$colour`  | Name of the colour from the list of [functional colours](https://design-system.service.gov.uk/styles/colour/)  | `String  | Colour`  |  
#####  [](./sass-api-reference/#example-getting-a-functional-colour.md)Example: Getting a functional colour

```
.branded-element {
  color: govuk-functional-colour('brand');
}

```

#####  [](./sass-api-reference/#example-output-from-getting-a-functional-colour.md)Example: Output from getting a functional colour

```
.branded-element {
  /* Assuming the 'brand' colour is hotpink */
  color: var(--govuk-brand-colour, hotpink);
}

```

[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L126-L141)
####  [](./sass-api-reference/#govuk-organisation-colour.md)govuk-organisation-colour
Get the colour for a government organisation
#####  [](./sass-api-reference/#govuk-organisation-colour-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$organisation`  | Organisation name, lowercase, hyphenated  | `String`  | —  |  
|  `$contrast-safe`  | By default a version of the colour will be returned which has a minimum 4.5:1 contrast ratio when used with white, as per the WCAG 2.1 Level AA guidelines. If you want to use the non-contrast safe version you can set this to `false` but your should ensure that you still meets contrast requirements for accessibility - for example, do not use the non-contrast safe version for text.  | `Boolean`  | `true`  |  
[ View source code for _colour.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_colour.scss#L191-L219)
###  [](./sass-api-reference/#helpers-layout.md)Layout
####  [](./sass-api-reference/#govuk-clearfix.md)govuk-clearfix
Clear floated content within a container using a pseudo element
#####  [](./sass-api-reference/#govuk-clearfix-usage.md)Usage

```
@include govuk-clearfix;

```

[ View source code for _clearfix.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_clearfix.scss#L9-L15)
####  [](./sass-api-reference/#govuk-grid-width.md)govuk-grid-width
Grid width percentage
#####  [](./sass-api-reference/#govuk-grid-width-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$key`  | Name of grid width (e.g. two-thirds)  | `String`  | —  |  
[ View source code for _grid.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_grid.scss#L13-L19)
####  [](./sass-api-reference/#govuk-grid-column.md)govuk-grid-column
Generate grid column styles
Creates a grid column with standard gutter between the columns.
Grid widths are defined in the `$govuk-grid-widths` map.
By default the column width changes from 100% to specified width at the ‘tablet’ breakpoint, but other breakpoints can be specified using the `$at` parameter.
#####  [](./sass-api-reference/#govuk-grid-column-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$width`  | name of a grid width from $govuk-grid-widths  | `String`  | `full`  |  
|  `$float`  | left | right  | `String`  | `left`  |  
|  `$at`  | mobile | tablet | desktop | any custom breakpoint  | `String`  | `tablet`  |  
#####  [](./sass-api-reference/#govuk-grid-column-usage.md)Usage

```
@include govuk-grid-column($width: "full", $float: "left", $at: "tablet");

```

#####  [](./sass-api-reference/#example-default.md)Example: Default

```
.govuk-grid-column-two-thirds {
  @include govuk-grid-column(two-thirds)
}

```

#####  [](./sass-api-reference/#example-customising-the-breakpoint-where-width-percentage-is-applied.md)Example: Customising the breakpoint where width percentage is applied

```
.govuk-grid-column-one-half-from-desktop {
  @include govuk-grid-column(one-half, $at: desktop);
}

```

#####  [](./sass-api-reference/#example-customising-the-float-direction.md)Example: Customising the float direction

```
.govuk-grid-column-one-half-right {
  @include govuk-grid-column(two-thirds, $float: right);
}

```

[ View source code for _grid.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_grid.scss#L52-L62)
####  [](./sass-api-reference/#govuk-breakpoint-value.md)govuk-breakpoint-value
Get the value of a breakpoint by name.
#####  [](./sass-api-reference/#govuk-breakpoint-value-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$value`  | If a string, the name of a breakpoint in $breakpoints. If a number without units, it will convert to px. If a number with units, it will return the value unaltered.  |  `String` or `Number`  | —  |  
|  `$breakpoints`  | The map to look for $value.  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./sass-api-reference/#govuk-breakpoint-value-example.md)Example

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

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L46-L65)
####  [](./sass-api-reference/#govuk-from-breakpoint.md)govuk-from-breakpoint
Generate the `min-width` segment of a media query given a breakpoint key
Pixel values are converted to ems for backwards compatibility with sass-mq. Unlike sass-mq, non-px and em values can be used as well.
#####  [](./sass-api-reference/#govuk-from-breakpoint-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$from`  | If a string, expects the name of a breakpoint in $breakpoints. If a number, it will use that number.  |  `String` or `Number`  | —  |  
|  `$breakpoints`  | The map to look for $from.  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./sass-api-reference/#govuk-from-breakpoint-example.md)Example

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

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L101-L109)
####  [](./sass-api-reference/#govuk-until-breakpoint.md)govuk-until-breakpoint
Generate the `max-width` segment of a media query given a breakpoint key
sass-mq converted pixel values to ems, and only performed subtractions on named breakpoints. These have been retained for backwards compatibility, though unlike sass-mq, this also supports using non-px and em values.
#####  [](./sass-api-reference/#govuk-until-breakpoint-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$until`  | If a string, expects the name of a breakpoint in $breakpoints. If a number, it will use that number.  |  `String` or `Number`  | —  |  
|  `$breakpoints`  | The map to look for $until.  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./sass-api-reference/#govuk-until-breakpoint-example.md)Example

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

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L146-L160)
####  [](./sass-api-reference/#govuk-media-query.md)govuk-media-query
Media query
#####  [](./sass-api-reference/#govuk-media-query-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$from`  | One of $breakpoints  |  `String` or `Boolean`  | `false`  |  
|  `$until`  | One of $breakpoints  |  `String` or `Boolean`  | `false`  |  
|  `$and`  | Additional media query parameters  |  `String` or `Boolean`  | `false`  |  
|  `$media-type`  | Override media type: screen, print…  | `String`  | `all`  |  
|  `$breakpoints`  | Map of breakpoints to use  | `Map`  | `$govuk-breakpoints`  |  
#####  [](./sass-api-reference/#govuk-media-query-usage.md)Usage

```
@include govuk-media-query($from: false, $until: false, $and: false, $media-type: "all", $breakpoints: $govuk-breakpoints) {
  //..
}

```

#####  [](./sass-api-reference/#govuk-media-query-example.md)Example

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

[ View source code for _media-queries.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_media-queries.scss#L196-L221)
###  [](./sass-api-reference/#helpers-links.md)Links
####  [](./sass-api-reference/#govuk-link-common.md)govuk-link-common
Common link styles
Provides the typography and focus state, regardless of link style.
#####  [](./sass-api-reference/#govuk-link-common-usage.md)Usage

```
@include govuk-link-common;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L11-L22)
####  [](./sass-api-reference/#govuk-link-decoration.md)govuk-link-decoration
Link decoration
Provides the text decoration for links, including thickness and underline offset. Use this mixin only if you cannot use the `govuk-link-common` mixin.
#####  [](./sass-api-reference/#govuk-link-decoration-usage.md)Usage

```
@include govuk-link-decoration;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L30-L40)
####  [](./sass-api-reference/#govuk-link-hover-decoration.md)govuk-link-hover-decoration
Link hover decoration
Provides the text decoration for links in their hover state, for you to use within a `:hover` pseudo-selector. Use this mixin only if you cannot use the `govuk-link-common` mixin.
#####  [](./sass-api-reference/#govuk-link-hover-decoration-usage.md)Usage

```
@include govuk-link-hover-decoration;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L50-L60)
####  [](./sass-api-reference/#govuk-link-style-default.md)govuk-link-style-default
Default link styles
Makes links use the default unvisited, visited, hover and active colours.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-default-usage.md)Usage

```
@include govuk-link-style-default;

```

#####  [](./sass-api-reference/#govuk-link-style-default-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-default;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L77-L99)
####  [](./sass-api-reference/#govuk-link-style-error.md)govuk-link-style-error
Error link styles
Makes links use the error colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-error-usage.md)Usage

```
@include govuk-link-style-error;

```

#####  [](./sass-api-reference/#govuk-link-style-error-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-error;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L117-L136)
####  [](./sass-api-reference/#govuk-link-style-success.md)govuk-link-style-success
Success link styles
Makes links use the success colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-success-usage.md)Usage

```
@include govuk-link-style-success;

```

#####  [](./sass-api-reference/#govuk-link-style-success-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-success;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L154-L173)
####  [](./sass-api-reference/#govuk-link-style-muted.md)govuk-link-style-muted
Muted link styles
Makes links use the secondary text colour. The link will darken if it’s active or a user hovers their cursor over it.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-muted-usage.md)Usage

```
@include govuk-link-style-muted;

```

#####  [](./sass-api-reference/#govuk-link-style-muted-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-muted;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L191-L207)
####  [](./sass-api-reference/#govuk-link-style-text.md)govuk-link-style-text
Text link styles
Makes links use the primary text colour, in all states. Use this mixin for navigation components, such as breadcrumbs or the back link.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-text-usage.md)Usage

```
@include govuk-link-style-text;

```

#####  [](./sass-api-reference/#govuk-link-style-text-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-text;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L225-L235)
####  [](./sass-api-reference/#govuk-link-style-inverse.md)govuk-link-style-inverse
Inverse link styles
Makes links white, in all states. Use this mixin if you’re displaying links against a dark background.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-inverse-usage.md)Usage

```
@include govuk-link-style-inverse;

```

#####  [](./sass-api-reference/#govuk-link-style-inverse-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-inverse;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L253-L262)
####  [](./sass-api-reference/#govuk-link-style-no-visited-state.md)govuk-link-style-no-visited-state
Default link styles, without a visited state
Makes links use the default unvisited, hover and active colours, with no distinct visited state.
Use this mixin when it’s not helpful to distinguish between visited and non-visited links. For example, when you link to pages with frequently-changing content, such as the dashboard for an admin interface.
If you use this mixin in a component, you must also include the `govuk-link-common` mixin to get the correct focus and hover states.
#####  [](./sass-api-reference/#govuk-link-style-no-visited-state-usage.md)Usage

```
@include govuk-link-style-no-visited-state;

```

#####  [](./sass-api-reference/#govuk-link-style-no-visited-state-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-no-visited-state;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L284-L306)
####  [](./sass-api-reference/#govuk-link-style-no-underline.md)govuk-link-style-no-underline
Remove underline from links
Remove underlines from links unless the link is active or a user hovers their cursor over it.
#####  [](./sass-api-reference/#govuk-link-style-no-underline-usage.md)Usage

```
@include govuk-link-style-no-underline;

```

#####  [](./sass-api-reference/#govuk-link-style-no-underline-example.md)Example

```
.govuk-component__link {
  @include govuk-link-common;
  @include govuk-link-style-default;
  @include govuk-link-style-no-underline;
}

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L322-L326)
####  [](./sass-api-reference/#govuk-link-print-friendly.md)govuk-link-print-friendly
Include link destination when printing the page
If the user prints the page, add the destination URL after the link text, if the URL starts with `/`, `http://` or `https://`.
#####  [](./sass-api-reference/#govuk-link-print-friendly-usage.md)Usage

```
@include govuk-link-print-friendly;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L335-L351)
####  [](./sass-api-reference/#govuk-link-image.md)govuk-link-image
Image link styles
Prepares and provides the focus state for links that only contain images with no accompanying text.
#####  [](./sass-api-reference/#govuk-link-image-usage.md)Usage

```
@include govuk-link-image;

```

[ View source code for _links.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_links.scss#L360-L373)
###  [](./sass-api-reference/#shapes.md)Shapes
####  [](./sass-api-reference/#govuk-shape-arrow.md)govuk-shape-arrow
Arrow mixin
Generate Arrows (triangles) by using a mix of transparent (1) and coloured borders. The coloured borders inherit the text colour of the element (2).
Ensure the arrow is rendered correctly if browser colours are overridden by providing a clip path (3). Without this the transparent borders are overridden to become visible which results in a square.
We need both because older browsers do not support clip-path.
#####  [](./sass-api-reference/#govuk-shape-arrow-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$direction`  | Direction for arrow: up, right, down, left.  | `String`  | —  |  
|  `$base`  | Length of the triangle ‘base’ side  | `Number`  | —  |  
|  `$height`  | Height of triangle. Omit for equilateral.  | `Number`  | `null`  |  
|  `$display`  | CSS display property of the arrow  | `String`  | `block`  |  
#####  [](./sass-api-reference/#govuk-shape-arrow-usage.md)Usage

```
@include govuk-shape-arrow($direction, $base, $height: null, $display: "block");

```

[ View source code for _shape-arrow.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_shape-arrow.scss#L38-L80)
###  [](./sass-api-reference/#spacing.md)Spacing
####  [](./sass-api-reference/#govuk-spacing.md)govuk-spacing
Single point spacing
Returns measurement corresponding to the spacing point requested.
#####  [](./sass-api-reference/#govuk-spacing-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$spacing-point`  | Point on the spacing scale (set in `settings/_spacing.scss`)  | `Number`  | —  |  
#####  [](./sass-api-reference/#govuk-spacing-example.md)Example

```
.element {
  padding: govuk-spacing(5);
}

```

#####  [](./sass-api-reference/#example-using-negative-spacing.md)Example: Using negative spacing

```
.element {
  margin-top: govuk-spacing(-1);
}

```

#####  [](./sass-api-reference/#example-marking-spacing-declarations-as-important.md)Example: Marking spacing declarations as important

```
.element {
  margin-top: govuk-spacing(1) !important;
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L37-L56)
####  [](./sass-api-reference/#govuk-responsive-margin.md)govuk-responsive-margin
Responsive margin
Adds responsive margin by fetching a ‘spacing map’ from the responsive spacing scale, which defines different spacing values at different breakpoints. Wrapper for the `_govuk-responsive-spacing` mixin.
#####  [](./sass-api-reference/#govuk-responsive-margin-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$responsive-spacing-point`  | Point on the responsive spacingscale, corresponds to a map of breakpoints and spacing values  | `Number`  | —  |  
|  `$direction`  | Direction to add spacing to (`top`, `right`, `bottom`, `left`, `all`)  | `String`  | `all`  |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `false`  |  
|  `$adjustment`  | Offset to adjust spacing by  | `Number`  | `false`  |  
#####  [](./sass-api-reference/#govuk-responsive-margin-usage.md)Usage

```
@include govuk-responsive-margin($responsive-spacing-point, $direction: "all", $important: false, $adjustment: false);

```

#####  [](./sass-api-reference/#govuk-responsive-margin-example.md)Example

```
.element {
   @include govuk-responsive-margin(6, "left", $adjustment: 1px);
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L149-L151)
####  [](./sass-api-reference/#govuk-responsive-padding.md)govuk-responsive-padding
Responsive padding
Adds responsive padding by fetching a ‘spacing map’ from the responsive spacing scale, which defines different spacing values at different breakpoints. Wrapper for the `_govuk-responsive-spacing` mixin.
#####  [](./sass-api-reference/#govuk-responsive-padding-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$responsive-spacing-point`  | Point on the responsive spacing scale, corresponds to a map of breakpoints and spacing values  | `Number`  | —  |  
|  `$direction`  | Direction to add spacing to (`top`, `right`, `bottom`, `left`, `all`)  | `String`  | `all`  |  
|  `$important`  | Whether to mark as `!important`  | `Boolean`  | `false`  |  
|  `$adjustment`  | Offset to adjust spacing  | `Number`  | `false`  |  
#####  [](./sass-api-reference/#govuk-responsive-padding-usage.md)Usage

```
@include govuk-responsive-padding($responsive-spacing-point, $direction: "all", $important: false, $adjustment: false);

```

#####  [](./sass-api-reference/#govuk-responsive-padding-example.md)Example

```
.element {
   @include govuk-responsive-padding(6, "left", $adjustment: 1px);
}

```

[ View source code for _spacing.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_spacing.scss#L175-L177)
###  [](./sass-api-reference/#helpers-typography.md)Typography
####  [](./sass-api-reference/#govuk-typography-common.md)govuk-typography-common
‘Common typography’ helper
Sets the font family and associated properties, such as font smoothing. Also overrides the font for print.
#####  [](./sass-api-reference/#govuk-typography-common-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$font-family`  | Font family to use  | `List`  | `$govuk-font-family`  |  
#####  [](./sass-api-reference/#govuk-typography-common-usage.md)Usage

```
@include govuk-typography-common($font-family: $govuk-font-family);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L28-L42)
####  [](./sass-api-reference/#helpers-typography-govuk-text-colour.md)govuk-text-colour
Text colour helper
Sets the text colour, including a suitable override for print.
#####  [](./sass-api-reference/#helpers-typography-govuk-text-colour-usage.md)Usage
! ** Warning
Deprecated: 
**

```
@include govuk-text-colour;

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L51-L58)
####  [](./sass-api-reference/#govuk-typography-weight-regular.md)govuk-typography-weight-regular
Regular font weight helper
#####  [](./sass-api-reference/#govuk-typography-weight-regular-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./sass-api-reference/#govuk-typography-weight-regular-usage.md)Usage

```
@include govuk-typography-weight-regular($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L66-L68)
####  [](./sass-api-reference/#govuk-typography-weight-bold.md)govuk-typography-weight-bold
Bold font weight helper
#####  [](./sass-api-reference/#govuk-typography-weight-bold-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./sass-api-reference/#govuk-typography-weight-bold-usage.md)Usage

```
@include govuk-typography-weight-bold($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L76-L78)
####  [](./sass-api-reference/#govuk-font-tabular-numbers.md)govuk-font-tabular-numbers
Tabular number helper
Switches numerical glyphs (0–9) to use alternative forms with a monospaced bounding box. This ensures that columns of numbers, such as those in tables, remain horizontally aligned with one another. This also has the useful side effect of making numbers more legible in some situations, such as reference codes, as the numbers are more distinct and visually separated from one another.
#####  [](./sass-api-reference/#govuk-font-tabular-numbers-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally Used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./sass-api-reference/#govuk-font-tabular-numbers-usage.md)Usage

```
@include govuk-font-tabular-numbers($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L93-L95)
####  [](./sass-api-reference/#govuk-text-break-word.md)govuk-text-break-word
Word break helper
Forcibly breaks long words that lack spaces, such as email addresses, across multiple lines when they wouldn’t otherwise fit.
#####  [](./sass-api-reference/#govuk-text-break-word-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$important`  | Whether to mark declarations as `!important`. Generally used to create override classes.  | `Boolean`  | `false`  |  
#####  [](./sass-api-reference/#govuk-text-break-word-usage.md)Usage

```
@include govuk-text-break-word($important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L106-L112)
####  [](./sass-api-reference/#govuk-font-size.md)govuk-font-size
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

#####  [](./sass-api-reference/#govuk-font-size-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the type scale (the size as it would appear on tablet and above)  |  `Number` or `String`  | —  |  
|  `$line-height`  | Non responsive custom line height. Omit to use the line height from the font map.  | `Number`  | `false`  |  
|  `$important`  | Whether to mark declarations as `!important`.  | `Boolean`  | `false`  |  
#####  [](./sass-api-reference/#govuk-font-size-usage.md)Usage

```
@include govuk-font-size($size, $line-height: false, $important: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L168-L252)
####  [](./sass-api-reference/#govuk-font.md)govuk-font
Font helper
#####  [](./sass-api-reference/#govuk-font-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$size`  | Point from the type scale (the size as it would appear on tablet and above). Use `false` to avoid setting a size.  |  `Number` or `Boolean` or `String`  | —  |  
|  `$weight`  | Weight: `bold` or `regular`  | `String`  | `regular`  |  
|  `$tabular`  | Whether to use tabular numbers or not  | `Boolean`  | `false`  |  
|  `$line-height`  | Line-height, if overriding the default  | `Number`  | `false`  |  
#####  [](./sass-api-reference/#govuk-font-usage.md)Usage

```
@include govuk-font($size, $weight: "regular", $tabular: false, $line-height: false);

```

[ View source code for _typography.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/helpers/_typography.scss#L268-L284)
##  [](./sass-api-reference/#components.md)Components
###  [](./sass-api-reference/#button.md)Button
####  [](./sass-api-reference/#govuk-button-background-colour.md)$govuk-button-background-colour
Button component background colour
#####  [](./sass-api-reference/#govuk-button-background-colour-default-value.md)Default value

```
$govuk-button-background-colour: govuk-colour("green");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L12-L12)
####  [](./sass-api-reference/#govuk-button-text-colour.md)$govuk-button-text-colour
Button component text colour
#####  [](./sass-api-reference/#govuk-button-text-colour-default-value.md)Default value

```
$govuk-button-text-colour: govuk-colour("white");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L19-L19)
####  [](./sass-api-reference/#govuk-inverse-button-background-colour.md)$govuk-inverse-button-background-colour
Inverted button component background colour
#####  [](./sass-api-reference/#govuk-inverse-button-background-colour-default-value.md)Default value

```
$govuk-inverse-button-background-colour: govuk-colour("white");

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L26-L26)
####  [](./sass-api-reference/#govuk-inverse-button-text-colour.md)$govuk-inverse-button-text-colour
Inverted button component text colour
#####  [](./sass-api-reference/#govuk-inverse-button-text-colour-default-value.md)Default value

```
$govuk-inverse-button-text-colour: govuk-functional-colour(brand);

```

[ View source code for _index.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/components/button/_index.scss#L33-L33)
##  [](./sass-api-reference/#objects.md)Objects
###  [](./sass-api-reference/#objects-layout.md)Layout
####  [](./sass-api-reference/#govuk-width-container.md)govuk-width-container
Width container mixin
Used to create page width and custom width container classes.
#####  [](./sass-api-reference/#govuk-width-container-parameters.md)Parameters  
| Name  | Description  | Type  | Default value  |  
| --- | --- | --- | --- |  
|  `$width`  | Width in pixels  | `String`  | `$govuk-page-width`  |  
#####  [](./sass-api-reference/#govuk-width-container-usage.md)Usage

```
@include govuk-width-container($width: "$govuk-page-width");

```

#####  [](./sass-api-reference/#example-creating-a-1200px-wide-container-class.md)Example: Creating a 1200px wide container class

```
.app-width-container--wide {
  @include govuk-width-container(1200px);
}

```

[ View source code for _width-container.scss on GitHub ](https://github.com/alphagov/govuk-frontend/tree/v6.1.0/packages/govuk-frontend/src/govuk/objects/_width-container.scss#L21-L70)
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/sass-api-reference/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Sass+API+reference%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fsass-api-reference%2F%29&labels=bug&title=Re%3A+%27Sass+API+reference%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
