#  [](./v4/migration-reference/#migration-reference.md)Migration reference
This is part of [migrating from our old frameworks to GOV.UK Frontend](./v4/migrating-from-legacy-products.md).
The tables below show the old and new names for components, classes and mixins, to help you find what you need.
##  [](./v4/migration-reference/#nunjucks.md)Nunjucks
Where possible we have kept the new page template the same as GOV.UK Template.
The main change is changing variables from [snake_case](https://en.wikipedia.org/wiki/Snake_case) to [camelCase](https://en.wikipedia.org/wiki/Camel_case).  
| GOV.UK Template  | GOV.UK Frontend  |  
| --- | --- |  
| `:top_of_page`  | Deprecated: putting content above the `<!DOCTYPE html>` will result in broken pages for users of older Internet Explorer versions.  |  
| `:html_lang`  | `htmlLang`  |  
| `:page_title`  | `pageTitle`  |  
| `:asset_path`  | `assetPath`  |  
| `:head`  | `head`  |  
| `:body_classes`  | `bodyClasses`  |  
| `:body_start`  | `bodyStart`  |  
| `:skip_link_message`  |  [Override the skip link block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own skip link which can include custom `text`.   |  
| `:cookie_message`  |  See the [cookie banner component](https://design-system.service.gov.uk/components/cookie-banner/) for more details.   |  
| `header_class`  |  [Override the header block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own header which can include custom `classes`.   |  
| `homepage_url`  |  [Override the header block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own header which can include a custom `homepageUrl`.   |  
| `global_header_text`  |  No equivalent. [Raise an issue](https://github.com/alphagov/govuk-frontend/issues/new/choose) if you need this.   |  
| `inside_header`  |  [Override the header block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own header which can include a custom `serviceName`.   |  
| `proposition_header`  |  [Override the header block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own header which can include a custom `navigation`.   |  
| `:after_header`  | `beforeContent`  |  
| `:content`  |  `main` Setting `content` in the new template will put it inside a `<main>` element.  In the old GOV.UK Template there was no default `<main>` element.  You can restructure your content so that it does not use a `<main>` element, or override the `main` block.   |  
| `:footer_top`  |  [Override the footer block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own footer which can include a custom `navigation`.   |  
| `:footer_support_links`  |  [Override the footer block in the page template](https://design-system.service.gov.uk/styles/page-template/#changing-template-content), passing your own footer which can include custom `meta` links.   |  
| `:licence_message`  |  No equivalent. [Raise an issue](https://github.com/alphagov/govuk-frontend/issues/new/choose) if you need this.   |  
| `:body_end`  | `bodyEnd`  |  
##  [](./v4/migration-reference/#component-names.md)Component names  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
| `link-back`  | [Back link component](https://design-system.service.gov.uk/components/back-link/)  |  
| Button  | [Button component](https://design-system.service.gov.uk/components/button/)  |  
| Checkboxes  | [Checkboxes component](https://design-system.service.gov.uk/components/checkboxes/)  |  
| Date pattern  | [Date input component](https://design-system.service.gov.uk/components/date-input/)  |  
| Hidden text (Progressive disclosure)  | [Details component](https://design-system.service.gov.uk/components/details/)  |  
| Errors and validation  |  [Error message component](https://design-system.service.gov.uk/components/error-message/)  
[Error summary component](https://design-system.service.gov.uk/components/error-summary/)  |  
| `<fieldset>`  | [Fieldset component](https://design-system.service.gov.uk/components/fieldset/)  |  
| File upload  | [File upload component](https://design-system.service.gov.uk/components/file-upload/)  |  
| Alpha and beta banners  | [Phase banner component](https://design-system.service.gov.uk/components/phase-banner/)  |  
| Radio buttons  | [Radios component](https://design-system.service.gov.uk/components/radios/)  |  
| Select boxes  | [Select component](https://design-system.service.gov.uk/components/select/)  |  
| Phase tag  | [Tag component](https://design-system.service.gov.uk/components/tag/)  |  
| Form fields  | [Text input component](https://design-system.service.gov.uk/components/text-input/)  |  
| `<textarea>`  | [Textarea component](https://design-system.service.gov.uk/components/textarea/)  |  
| Warning text (previously Legal text)  | [Warning text component](https://design-system.service.gov.uk/components/text-input/)  |  
| govuk-box-highlight  | [Panel component](https://design-system.service.gov.uk/components/panel/)  |  
| Inset text  | [Inset text component](https://design-system.service.gov.uk/components/inset-text/)  |  
| panel (object)  
panel-border-wide  
panel-border-narrow  | Deprecated: this style is now contained within each component that needs it   |  
##  [](./v4/migration-reference/#class-names.md)Class names
GOV.UK Frontend uses [“Block, Element, Modifier” (BEM)](http://getbem.com/) and [Inverted Triangle CSS (ITCSS)](https://www.creativebloq.com/web-design/manage-large-scale-web-projects-new-css-architecture-itcss-41514731) to structure CSS and define class names. This means all of the existing class names have changed.
###  [](./v4/migration-reference/#typography-class-names.md)Typography class names  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
| `heading-xlarge`  | `govuk-heading-xl`  |  
| `heading-large`  | `govuk-heading-l`  |  
| `heading-medium`  | `govuk-heading-m`  |  
| `heading-small`  | `govuk-heading-s`  |  
| `lede`  | `govuk-body-l`  |  
| `<p>  
body-text`  | `govuk-body`  |  
| `font-xsmall`  | `govuk-body-s`  |  
| `<a>`  | `govuk-link`  |  
| `<hr>`  |  `govuk-section-break`  
`govuk-section-break--visible`  
`govuk-section-break--xl`  
`govuk-section-break--l`  
`govuk-section-break--m`  |  
###  [](./v4/migration-reference/#lists.md)Lists  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
| `list`  | `govuk-list`  |  
|  `list`  
`list-bullet`  |  `govuk-list`  
`govuk-list--bullet`  |  
|  `list`  
`list-number`  |  `govuk-list`  
`govuk-list--number`  |  
###  [](./v4/migration-reference/#layout-and-grid-system-class-names.md)Layout and grid system class names  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
| `grid-row`  | `govuk-grid-row`  |  
| `column-full`  | `govuk-grid-column-full`  |  
| `column-one-half`  | `govuk-grid-column-one-half`  |  
| `column-one-third`  | `govuk-grid-column-one-third`  |  
| `column-two-thirds`  | `govuk-grid-column-two-thirds`  |  
| `column-one-quarter`  | `govuk-grid-column-one-quarter`  |  
| `#content`  | [Page wrappers](https://design-system.service.gov.uk/styles/layout/#setting-up-page-wrappers)  |  
###  [](./v4/migration-reference/#form-related-class-names.md)Form related class names  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
| `form-group`  | `govuk-form-group`  |  
| `form-hint`  | Specific to component, for example  
`govuk-label__hint`  |  
| `form-label`  | Specific to component, for example  
`govuk-label`  
`govuk-radios__label`  |  
| `form-label-bold`  | `govuk-label--s`  |  
|  `form-control`  
`form-control-3-4`  
`form-control-2-3`  
`form-control-1-2`  
`form-control-1-3`  
`form-control-1-4`  
`form-control-1-8`  | [Width override classes](https://design-system.service.gov.uk/styles/layout/#width-override-classes)  |  
| `form-section`  | Deprecated: not required with new spacing implementation  |  
| `form-group-related`  | Deprecated: not required with new spacing implementation  |  
| `form-group-compound`  | Deprecated: not required with new spacing implementation  |  
###  [](./v4/migration-reference/#helper-class-names.md)Helper class names  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
|  `visually-hidden`, `visuallyhidden`  |  `govuk-visually-hidden`  
`govuk-visually-hidden-focusable`  |  
###  [](./v4/migration-reference/#override-class-names.md)Override class names  
| GOV.UK Elements  | GOV.UK Frontend  |  
| --- | --- |  
| `font-xxlarge`  | `govuk-!-font-size-80`  |  
| `font-xlarge`  | `govuk-!-font-size-48`  |  
| `font-large`  | `govuk-!-font-size-36`  |  
| `font-medium`  | `govuk-!-font-size-24`  |  
| `font-small`  | `govuk-!-font-size-19`  |  
| `font-xsmall`  | `govuk-!-font-size-16`  |  
| `bold-xxlarge`  |  `govuk-!-font-size-80`  
`govuk-!-font-weight-bold`  |  
| `bold-xlarge`  |  `govuk-!-font-size-48`  
`govuk-!-font-weight-bold`  |  
| `bold-large`  |  `govuk-!-font-size-36`  
`govuk-!-font-weight-bold`  |  
| `bold-medium`  |  `govuk-!-font-size-24`  
`govuk-!-font-weight-bold`  |  
| `bold-small`  |  `govuk-!-font-size-19`  
`govuk-!-font-weight-bold`  |  
| `bold-xsmall`  |  `govuk-!-font-size-16`  
`govuk-!-font-weight-bold`  |  
| `bold`  | `govuk-!-font-weight-bold`  |  
##  [](./v4/migration-reference/#mixins-and-variables.md)Mixins and variables
###  [](./v4/migration-reference/#typography.md)Typography  
| GOV.UK Frontend Toolkit  | GOV.UK Frontend  |  
| --- | --- |  
| `@include core-80`  | `@include govuk-font(80)`  |  
| `@include core-48`  | `@include govuk-font(48)`  |  
| `@include core-36`  | `@include govuk-font(36)`  |  
| `@include core-27`  | `@include govuk-font(27)`  |  
| `@include core-24`  | `@include govuk-font(24)`  |  
| `@include core-19`  | `@include govuk-font(19)`  |  
| `@include core-16`  | `@include govuk-font(16)`  |  
| `@include core-14`  | `@include govuk-font(14)`  |  
| `@include bold-80`  | `@include govuk-font(80, $weight: bold)`  |  
| `@include bold-48`  | `@include govuk-font(48, $weight: bold)`  |  
| `@include bold-36`  | `@include govuk-font(36, $weight: bold)`  |  
| `@include bold-27`  | `@include govuk-font(27, $weight: bold)`  |  
| `@include bold-24`  | `@include govuk-font(24, $weight: bold)`  |  
| `@include bold-19`  | `@include govuk-font(19, $weight: bold)`  |  
| `@include bold-16`  | `@include govuk-font(16, $weight: bold)`  |  
| `@include bold-14`  | `@include govuk-font(14, $weight: bold)`  |  
| `@include heading-80`  | Deprecated: 80px headings are not used, `@include govuk-font(80, $weight: bold)` should be used instead  |  
| `@include heading-48`  | `@extend %govuk-heading-xl`  |  
| `@include heading-36`  | `@extend %govuk-heading-l`  |  
| `@include heading-27`  | Deprecated: 27px headings are not used, `@include govuk-font(27, $weight: bold)` should be used instead  |  
| `@include heading-24`  | `@extend %govuk-heading-m`  |  
| `@include copy-19`  | `@extend %govuk-body-m`  |  
| `@include copy-14`  | `@extend %govuk-body-xs`  |  
###  [](./v4/migration-reference/#layout.md)Layout  
| GOV.UK Frontend Toolkit  | GOV.UK Frontend  |  
| --- | --- |  
| `@extend site-width-container`  | `@include govuk-width-container`  |  
| `@include grid-column( 1/4 )`  | Deprecated: you cannot apply grid properties to other elements using GOV.UK Frontend  |  
| `@include grid-column( 1/2 )`  | Deprecated: you cannot apply grid properties to other elements using GOV.UK Frontend  |  
| `@include grid-column( 1/3 )`  | Deprecated: you cannot apply grid properties to other elements using GOV.UK Frontend  |  
| `@include grid-column( 2/3 )`  | Deprecated: you cannot apply grid properties to other elements using GOV.UK Frontend  |  
| ` @include grid-column( 1/3, $full-width: desktop );`  | Deprecated: you cannot apply grid properties to other elements using GOV.UK Frontend  |  
| `$gutter`  |  `$govuk-gutter`, only use for the gaps in between grid columns, otherwise use the [spacing scale](https://design-system.service.gov.uk/styles/spacing/#applying-spacing-in-your-own-css).  |  
| `$gutter-half`  |  `$govuk-gutter-half`, only use for the gaps in between grid columns, otherwise use the [spacing scale](https://design-system.service.gov.uk/styles/spacing/#applying-spacing-in-your-own-css).  |  
###  [](./v4/migration-reference/#media-queries.md)Media queries  
| GOV.UK Frontend Toolkit  | GOV.UK Frontend  |  
| --- | --- |  
| `@include media(desktop)`  |  `@include govuk-media-query($from: desktop)`  
`@include govuk-media-query($until: desktop)`  |  
| `@include media(tablet)`  |  `@include govuk-media-query($from: tablet)`  
`@include govuk-media-query($until: tablet)`  |  
| `@include media(mobile)`  |  `@include govuk-media-query($from: mobile)`  
`@include govuk-media-query($until: mobile)`  |  
###  [](./v4/migration-reference/#images.md)Images  
| GOV.UK Frontend Toolkit  | GOV.UK Frontend  |  
| --- | --- |  
| `@include device-pixel-ratio($ratio: 2)`  | `@include govuk-device-pixel-ratio($ratio: 2)`  |  
###  [](./v4/migration-reference/#shims.md)Shims  
| GOV.UK Frontend Toolkit  | GOV.UK Frontend  |  
| --- | --- |  
| `@include inline-block`  | Deprecated: inline-block is now the default for any components  |  
| `@extend %contain-floats`  | `@include govuk-clearfix`  |  
###  [](./v4/migration-reference/#internet-explorer.md)Internet Explorer  
| GOV.UK Frontend Toolkit  | GOV.UK Frontend  |  
| --- | --- |  
| `@include ie(8)`  | `@include govuk-if-ie8`  |  
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/v4/migration-reference/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Migration+reference%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fv4%2Fmigration-reference%2F%29&labels=bug&title=Re%3A+%27Migration+reference%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
