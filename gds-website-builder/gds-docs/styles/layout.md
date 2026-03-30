#  Layout 
  * [ Screen size ](./styles/layout/#screen-size.md)
  * [ Common layouts ](./styles/layout/#common-layouts.md)
  * [ Setting up page wrappers ](./styles/layout/#setting-up-page-wrappers.md)
  * [ Using the grid system ](./styles/layout/#using-the-grid-system.md)
  * [ Width override classes ](./styles/layout/#width-override-classes.md)
  * [ Override how elements display ](./styles/layout/#override-how-elements-display.md)
  * [ Hide elements and keep them accessible to screen readers ](./styles/layout/#hide-elements-and-keep-them-accessible-to-screen-readers.md)

## Screen size
Design for small screens first, starting with a single-column layout.
For most types of page, we recommend using either a ‘two-thirds’ or a ‘two-thirds and one-third’ layout. That stops lines of text getting so long that the page becomes difficult to read on desktop devices. This would usually mean no more than 75 characters per line.
Never make assumptions about what devices people are using. Design for different screen sizes rather than specific devices.
The default maximum page width is 1020px, but you can make it wider if your content requires it.
## Common layouts
### Two-thirds
[ Open this example in a new tab: common two-thirds – layout ](./styles/layout/common-two-thirds.md)
  * [HTML](./styles/layout/#common-two-thirds-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <a href="#" class="govuk-back-link">Back</a>
  <main class="govuk-main-wrapper">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-xl">Two-thirds column</h1>
        <p class="govuk-body">This is a paragraph inside a two-thirds wide column</p>
      </div>
    </div>
  </main>
</div>
```

### Two-thirds and one-third
[ Open this example in a new tab: common two-thirds / one-third – layout ](./styles/layout/common-two-thirds-one-third.md)
  * [HTML](./styles/layout/#common-two-thirds-one-third-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <a href="#" class="govuk-back-link">Back</a>
  <main class="govuk-main-wrapper">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-xl">Two-thirds column</h1>
        <p class="govuk-body">This is a paragraph inside a two-thirds wide column</p>
      </div>
      <div class="govuk-grid-column-one-third">
        <h2 class="govuk-heading-m">One-third column</h2>
        <p class="govuk-body">This is a paragraph inside a one-third wide column</p>
      </div>
    </div>
  </main>
</div>
```

### Row 1: Two-thirds   
Row 2: Two-thirds and one-third
[ Open this example in a new tab: common two-thirds with two rows – layout ](./styles/layout/common-two-thirds-two-thirds-one-third.md)
  * [HTML](./styles/layout/#common-two-thirds-with-two-rows-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <a href="#" class="govuk-back-link">Back</a>
  <main class="govuk-main-wrapper">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-xl">Two-thirds column</h1>
      </div>
    </div>
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h2 class="govuk-heading-l">Two-thirds column</h2>
        <p class="govuk-body-l">This is a lead paragraph inside a two-thirds wide column</p>
        <p class="govuk-body">This is a paragraph inside a two-thirds wide column</p>
      </div>
      <div class="govuk-grid-column-one-third">
        <h3 class="govuk-heading-m">One-third column</h3>
        <p class="govuk-body">This is a paragraph inside a one-third wide column</p>
      </div>
    </div>
  </main>
</div>
```

## Setting up page wrappers
If you want to build your layout from scratch, or understand what each of the parts are responsible for, here’s an explanation of how the page wrappers work.
### Limiting width of content
To set up your layout you will need to create 2 wrappers. The first should have the class `govuk-width-container`, which sets the maximum width of the content but does not add any vertical margin or padding.
If your design requires them, you should place components such as the [Breadcrumbs component](./components/breadcrumbs.md), [Back link component](./components/back-link.md) and [Phase banner component](./components/phase-banner.md) inside this wrapper so that they sit directly underneath the header.
### Add vertical space
Within `govuk-width-container` you should add the `govuk-main-wrapper` class to your `<main>` element. This adds responsive padding to the top and bottom of the page and will be the container for your main content.
If you’re not using the [Breadcrumbs component](./components/breadcrumbs.md), [Back link component](./components/back-link.md) or [Phase banner component](./components/phase-banner.md) in your design, add the correct amount of vertical padding above the content by adding one of the following to your `<main>` element:
  * the `govuk-main-wrapper--auto-spacing` class
  * the `govuk-main-wrapper--l` class - if `govuk-main-wrapper--auto-spacing` does not work for your service

### Exploded view of page wrappers
[ Open this example in a new tab: page wrapper – layout ](./styles/layout/layout-wrappers.md)
  * [HTML](./styles/layout/#page-wrapper-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <a href="#" class="govuk-back-link">Back</a>
  <main class="govuk-main-wrapper">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-xl">Page title</h1>
      </div>
    </div>
  </main>
</div>
```

### Exploded view of page wrappers without a back link, breadcrumbs or phase banner
[ Open this example in a new tab: page wrapper without content after the header – layout ](./styles/layout/layout-wrappers-l.md)
  * [HTML](./styles/layout/#page-wrapper-without-content-after-the-header-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <main class="govuk-main-wrapper govuk-main-wrapper--l">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-xl">Page title</h1>
      </div>
    </div>
  </main>
</div>
```

## Using the grid system
Use the grid system to lay out the content on your service’s pages.
Most GOV.UK pages follow a ‘two-thirds and one-third’ layout, but the grid system allows for a number of additional combinations when necessary.
Your main content should always be in a two-thirds column even if you’re not using a corresponding one-third column for secondary content.
### Understanding the grid system
The grid is structured with a `govuk-grid-row` wrapper which acts as a row to contain your grid columns.
You can add columns inside this wrapper to create your layout. To define your columns add the class beginning with `govuk-grid-column-` to a new container followed by the width, for example `govuk-grid-column-one-third` to apply your desired width.
The available widths are:
### Full width
[ Open this example in a new tab: full width – layout ](./styles/layout/full-width.md)
  * [HTML](./styles/layout/#full-width-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-full">
    <p>govuk-grid-column-full</p>
  </div>
</div>
```

### One-half
[ Open this example in a new tab: one-half – layout ](./styles/layout/one-half.md)
  * [HTML](./styles/layout/#one-half-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-half">
    <p>govuk-grid-column-one-half</p>
  </div>
</div>
```

### One-third
[ Open this example in a new tab: one-third – layout ](./styles/layout/one-third.md)
  * [HTML](./styles/layout/#one-third-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-third">
    <p>govuk-grid-column-one-third</p>
  </div>
</div>
```

### Two-thirds
[ Open this example in a new tab: two-thirds – layout ](./styles/layout/two-thirds.md)
  * [HTML](./styles/layout/#two-thirds-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-two-thirds">
    <p>govuk-grid-column-two-thirds</p>
  </div>
</div>
```

### One-quarter
[ Open this example in a new tab: one-quarter – layout ](./styles/layout/one-quarter.md)
  * [HTML](./styles/layout/#one-quarter-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-quarter">
    <p>govuk-grid-column-one-quarter</p>
  </div>
</div>
```

### Three-quarters
[ Open this example in a new tab: three-quarters – layout ](./styles/layout/three-quarters.md)
  * [HTML](./styles/layout/#three-quarters-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-three-quarters">
    <p>govuk-grid-column-three-quarters</p>
  </div>
</div>
```

### Example combinations
[ Open this example in a new tab: combinations – layout ](./styles/layout/combinations.md)
  * [HTML](./styles/layout/#combinations-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-full">
    <p>govuk-grid-column-full</p>
  </div>
</div>
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-half">
    <p>govuk-grid-column-one-half</p>
  </div>
  <div class="govuk-grid-column-one-half">
    <p>govuk-grid-column-one-half</p>
  </div>
</div>
<div class="govuk-grid-row">
  <div class="govuk-grid-column-two-thirds">
    <p>govuk-grid-column-two-thirds</p>
  </div>
  <div class="govuk-grid-column-one-third">
    <p>govuk-grid-column-one-third</p>
  </div>
</div>
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-third">
    <p>govuk-grid-column-one-third</p>
  </div>
  <div class="govuk-grid-column-two-thirds">
    <p>govuk-grid-column-two-thirds</p>
  </div>
</div>
<div class="govuk-grid-row">
  <div class="govuk-grid-column-three-quarters">
    <p>govuk-grid-column-three-quarters</p>
  </div>
  <div class="govuk-grid-column-one-quarter">
    <p>govuk-grid-column-one-quarter</p>
  </div>
</div>
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-quarter">
    <p>govuk-grid-column-one-quarter</p>
  </div>
  <div class="govuk-grid-column-three-quarters">
    <p>govuk-grid-column-three-quarters</p>
  </div>
</div>
```

### Desktop specific grid classes
To specify a width at the desktop breakpoint you can use the desktop specific grid classes. For example `govuk-grid-column-two-thirds-from-desktop` will set your column width to be two-thirds width at the desktop breakpoint only.
[ Open this example in a new tab: desktop grid classes – layout ](./styles/layout/desktop.md)
  * [HTML](./styles/layout/#desktop-grid-classes-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-two-thirds-from-desktop">
    <p>govuk-grid-column-two-thirds-from-desktop</p>
  </div>
  <div class="govuk-grid-column-one-third-from-desktop">
    <p>govuk-grid-column-one-third-from-desktop</p>
  </div>
</div>
```

The desktop specific classes also allow you to set the width of the tablet breakpoint by using them in combination with the standard grid classes. For example using `govuk-grid-column-one-half` and `govuk-grid-column-two-thirds-from-desktop` together will mean the column will be one-half at the tablet breakpoint and two-thirds width at desktop.
[ Open this example in a new tab: desktop and tablet grid classes – layout ](./styles/layout/tablet-desktop.md)
  * [HTML](./styles/layout/#desktop-and-tablet-grid-classes-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-one-half govuk-grid-column-two-thirds-from-desktop">
    <p>govuk-grid-column-one-half<br><br>govuk-grid-column-two-thirds-from-desktop</p>
  </div>
  <div class="govuk-grid-column-one-half govuk-grid-column-one-third-from-desktop">
    <p>govuk-grid-column-one-half<br><br>govuk-grid-column-one-third-from-desktop</p>
  </div>
</div>
```

### Nested grids
[ Open this example in a new tab: nested – layout ](./styles/layout/nested.md)
  * [HTML](./styles/layout/#nested-layout-example-open-html.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-two-thirds">
    <p>govuk-grid-column-two-thirds</p>
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-one-half">
        <p>govuk-grid-column-one-half</p>
      </div>
      <div class="govuk-grid-column-one-half">
        <p>govuk-grid-column-one-half</p>
      </div>
    </div>
  </div>
</div>
```

## Width override classes
If you need to constrain the width of an element independently of the grid system, you can use width override classes.
The width override classes start with `govuk-!-width-`, followed by the width on larger screen sizes. For example, `govuk-!-width-one-half` will apply a width of 50% and `govuk-!-width-two-thirds`will apply a width of 66.66%.
These examples are for the generic width override classes - read specific [guidance on setting text input width](./components/text-input/#use-appropriately-sized-text-inputs.md).
[ Open this example in a new tab: overriding input width – spacing ](./styles/layout/width-overrides.md)
  * [HTML](./styles/layout/#overriding-input-width-spacing-example-open-html.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <label class="govuk-label" for="full">
    Full width
  </label>
  <input class="govuk-input govuk-!-width-full" id="full" name="full" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="three-quarters">
    Three-quarters width
  </label>
  <input class="govuk-input govuk-!-width-three-quarters" id="three-quarters" name="threeQuarters" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="two-thirds">
    Two-thirds width
  </label>
  <input class="govuk-input govuk-!-width-two-thirds" id="two-thirds" name="twoThirds" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="one-half">
    One-half width
  </label>
  <input class="govuk-input govuk-!-width-one-half" id="one-half" name="oneHalf" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="one-third">
    One-third width
  </label>
  <input class="govuk-input govuk-!-width-one-third" id="one-third" name="oneThird" type="text">
</div>
<div class="govuk-form-group">
  <label class="govuk-label" for="one-quarter">
    One-quarter width
  </label>
  <input class="govuk-input govuk-!-width-one-quarter" id="one-quarter" name="oneQuarter" type="text">
</div>
```

## Override how elements display
You can use display override classes if you need to override how elements display on the page.
Use:
  * `govuk-!-display-block` to display as a block
  * `govuk-!-display-inline` to display inline
  * `govuk-!-display-inline-block` to display as an inline block
  * `govuk-!-display-none` to remove the element from the page

You can also remove elements from the printed version of the page using `govuk-!-display-none-print`.
## Hide elements and keep them accessible to screen readers
You can stop elements from being displayed on the page and keep their contents available to screen readers using `govuk-visually-hidden`. You can use this to present content to screen reader users that sighted users do not need.
If the element is focusable, such as a link, you can make it become visible when receiving keyboard focus using `govuk-visually-hidden-focusable`.
## Help improve this style
If you spot a problem with this guidance you can [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/styles/layout/index.md). 
If you’re not sure how to do this, read guidance on [how to propose changes in GitHub](./community/propose-a-content-change-using-github.md). 
## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./styles/layout/#top.md)
