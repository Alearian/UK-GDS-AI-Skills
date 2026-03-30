#  Table 
Use the table component to make information easier to compare and scan for users.
[ Open this example in a new tab: table ](./components/table/default.md)
  * [HTML](./components/table/#table-example-html.md)
  * [Nunjucks](./components/table/#table-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <caption class="govuk-table__caption govuk-table__caption--m">Dates and amounts</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header">Date</th>
      <th scope="col" class="govuk-table__header">Amount</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">First 6 weeks</th>
      <td class="govuk-table__cell">£109.80 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 33 weeks</th>
      <td class="govuk-table__cell">£109.80 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Total estimated pay</th>
      <td class="govuk-table__cell">£4,282.20</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-table-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-table-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Dates and amounts",
  captionClasses: "govuk-table__caption--m",
  firstCellIsHeader: true,
  head: [
    {
      text: "Date"
    },
    {
      text: "Amount"
    }
  ],
  rows: [
    [
      {
        text: "First 6 weeks"
      },
      {
        text: "£109.80 per week"
      }
    ],
    [
      {
        text: "Next 33 weeks"
      },
      {
        text: "£109.80 per week"
      }
    ],
    [
      {
        text: "Total estimated pay"
      },
      {
        text: "£4,282.20"
      }
    ]
  ]
}) }}
```

## When to use this component
Use the table component to let users compare information in rows and columns.
## When not to use this component
Never use the table component to layout content on a page. Instead, use the [grid system](./styles/layout/#using-the-grid-system.md).
## How it works
### Table captions
Use the `<caption>` element to describe a table in the same way you would use a heading. A caption helps users find, navigate and understand tables.
There are other styling options for table captions. You can use `govuk-table__caption--s`, `govuk-table__caption--m`, `govuk-table__caption--l` and `govuk-table__caption--xl` classes to make them larger or smaller from the default.
[ Open this example in a new tab: custom caption size – table ](./components/table/caption-l.md)
  * [HTML](./components/table/#custom-caption-size-table-example-html.md)
  * [Nunjucks](./components/table/#custom-caption-size-table-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <caption class="govuk-table__caption govuk-table__caption--l">Months and rates</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header">Month you apply</th>
      <th scope="col" class="govuk-table__header">Rate for vehicles</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">January</th>
      <td class="govuk-table__cell">£95</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">February</th>
      <td class="govuk-table__cell">£55</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">March</th>
      <td class="govuk-table__cell">£125</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-custom-caption-size-table-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-custom-caption-size-table-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Months and rates",
  captionClasses: "govuk-table__caption--l",
  firstCellIsHeader: true,
  head: [
    {
      text: "Month you apply"
    },
    {
      text: "Rate for vehicles"
    }
  ],
  rows: [
    [
      {
        text: "January"
      },
      {
        text: "£95"
      }
    ],
    [
      {
        text: "February"
      },
      {
        text: "£55"
      }
    ],
    [
      {
        text: "March"
      },
      {
        text: "£125"
      }
    ]
  ]
}) }}
```

### Table headers
Use table headers to tell users what the rows and columns represent. Use the `scope` attribute to help users of assistive technology distinguish between row and column headers.
There are 2 ways to use the table component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: table second ](./components/table/default.md)
  * [HTML](./components/table/#table-second-example-html.md)
  * [Nunjucks](./components/table/#table-second-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <caption class="govuk-table__caption govuk-table__caption--m">Dates and amounts</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header">Date</th>
      <th scope="col" class="govuk-table__header">Amount</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">First 6 weeks</th>
      <td class="govuk-table__cell">£109.80 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 33 weeks</th>
      <td class="govuk-table__cell">£109.80 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Total estimated pay</th>
      <td class="govuk-table__cell">£4,282.20</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-table-second-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-table-second-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Dates and amounts",
  captionClasses: "govuk-table__caption--m",
  firstCellIsHeader: true,
  head: [
    {
      text: "Date"
    },
    {
      text: "Amount"
    }
  ],
  rows: [
    [
      {
        text: "First 6 weeks"
      },
      {
        text: "£109.80 per week"
      }
    ],
    [
      {
        text: "Next 33 weeks"
      },
      {
        text: "£109.80 per week"
      }
    ],
    [
      {
        text: "Total estimated pay"
      },
      {
        text: "£4,282.20"
      }
    ]
  ]
}) }}
```

## Numbers in a table
When comparing columns of numbers, align the numbers to the right in table cells.
[ Open this example in a new tab: numbers in a table – table ](./components/table/numbers.md)
  * [HTML](./components/table/#numbers-in-a-table-table-example-html.md)
  * [Nunjucks](./components/table/#numbers-in-a-table-table-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <caption class="govuk-table__caption govuk-table__caption--m">Months and rates</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header">Month you apply</th>
      <th scope="col" class="govuk-table__header govuk-table__header--numeric">Rate for bicycles</th>
      <th scope="col" class="govuk-table__header govuk-table__header--numeric">Rate for vehicles</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">January</th>
      <td class="govuk-table__cell govuk-table__cell--numeric">£85</td>
      <td class="govuk-table__cell govuk-table__cell--numeric">£95</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">February</th>
      <td class="govuk-table__cell govuk-table__cell--numeric">£75</td>
      <td class="govuk-table__cell govuk-table__cell--numeric">£55</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">March</th>
      <td class="govuk-table__cell govuk-table__cell--numeric">£165</td>
      <td class="govuk-table__cell govuk-table__cell--numeric">£125</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-numbers-in-a-table-table-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-numbers-in-a-table-table-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Months and rates",
  captionClasses: "govuk-table__caption--m",
  firstCellIsHeader: true,
  head: [
    {
      text: "Month you apply"
    },
    {
      text: "Rate for bicycles",
      format: "numeric"
    },
    {
      text: "Rate for vehicles",
      format: "numeric"
    }
  ],
  rows: [
    [
      {
        text: "January"
      },
      {
        text: "£85",
        format: "numeric"
      },
      {
        text: "£95",
        format: "numeric"
      }
    ],
    [
      {
        text: "February"
      },
      {
        text: "£75",
        format: "numeric"
      },
      {
        text: "£55",
        format: "numeric"
      }
    ],
    [
      {
        text: "March"
      },
      {
        text: "£165",
        format: "numeric"
      },
      {
        text: "£125",
        format: "numeric"
      }
    ]
  ]
}) }}
```

## Custom column widths
You can use the [width override classes](./styles/layout/#width-override-classes.md) to set the width of table columns.
[ Open this example in a new tab: custom width using override classes – table ](./components/table/column-widths.md)
  * [HTML](./components/table/#custom-width-using-override-classes-table-example-html.md)
  * [Nunjucks](./components/table/#custom-width-using-override-classes-table-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <caption class="govuk-table__caption govuk-table__caption--m">Month you apply</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header govuk-!-width-one-half">Date</th>
      <th scope="col" class="govuk-table__header govuk-!-width-one-quarter">Rate for vehicles</th>
      <th scope="col" class="govuk-table__header govuk-!-width-one-quarter">Rate for bicycles</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">First 6 weeks</th>
      <td class="govuk-table__cell">£109.80 per week</td>
      <td class="govuk-table__cell">£59.10 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 33 weeks</th>
      <td class="govuk-table__cell">£159.80 per week</td>
      <td class="govuk-table__cell">£89.10 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Total estimated pay</th>
      <td class="govuk-table__cell">£4,282.20</td>
      <td class="govuk-table__cell">£2,182.20</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-custom-width-using-override-classes-table-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-custom-width-using-override-classes-table-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Month you apply",
  captionClasses: "govuk-table__caption--m",
  firstCellIsHeader: true,
  head: [
    {
      text: "Date",
      classes: "govuk-!-width-one-half"
    },
    {
      text: "Rate for vehicles",
      classes: "govuk-!-width-one-quarter"
    },
    {
      text: "Rate for bicycles",
      classes: "govuk-!-width-one-quarter"
    }
  ],
  rows: [
    [
      {
        text: "First 6 weeks"
      },
      {
        text: "£109.80 per week"
      },
      {
        text: "£59.10 per week"
      }
    ],
    [
      {
        text: "Next 33 weeks"
      },
      {
        text: "£159.80 per week"
      },
      {
        text: "£89.10 per week"
      }
    ],
    [
      {
        text: "Total estimated pay"
      },
      {
        text: "£4,282.20"
      },
      {
        text: "£2,182.20"
      }
    ]
  ]
}) }}
```

If the [width override classes](./styles/layout/#width-override-classes.md) do not meet your needs you can create your own width classes and apply them to the cells in the table head. These can be added using the `classes` option in the Nunjucks macro or adding the class directly to the individual cells within `govuk-table__head` as below.
To learn more about this, read guidance on [extending and modifying components in production](./get-started/extending-and-modifying-components.md).
[ Open this example in a new tab: custom width using custom classes – table ](./components/table/column-widths-custom-classes.md)
  * [HTML](./components/table/#custom-width-using-custom-classes-table-example-html.md)
  * [Nunjucks](./components/table/#custom-width-using-custom-classes-table-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <caption class="govuk-table__caption govuk-table__caption--m">Month you apply</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header app-custom-class">Date</th>
      <th scope="col" class="govuk-table__header app-custom-class">Rate for vehicles</th>
      <th scope="col" class="govuk-table__header app-custom-class">Rate for bicycles</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">First 6 weeks</th>
      <td class="govuk-table__cell">£109.80 per week</td>
      <td class="govuk-table__cell">£59.10 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 33 weeks</th>
      <td class="govuk-table__cell">£159.80 per week</td>
      <td class="govuk-table__cell">£89.10 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Total estimated pay</th>
      <td class="govuk-table__cell">£4,282.20</td>
      <td class="govuk-table__cell">£2,182.20</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-custom-width-using-custom-classes-table-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-custom-width-using-custom-classes-table-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Month you apply",
  captionClasses: "govuk-table__caption--m",
  firstCellIsHeader: true,
  head: [
    {
      text: "Date",
      classes: "app-custom-class"
    },
    {
      text: "Rate for vehicles",
      classes: "app-custom-class"
    },
    {
      text: "Rate for bicycles",
      classes: "app-custom-class"
    }
  ],
  rows: [
    [
      {
        text: "First 6 weeks"
      },
      {
        text: "£109.80 per week"
      },
      {
        text: "£59.10 per week"
      }
    ],
    [
      {
        text: "Next 33 weeks"
      },
      {
        text: "£159.80 per week"
      },
      {
        text: "£89.10 per week"
      }
    ],
    [
      {
        text: "Total estimated pay"
      },
      {
        text: "£4,282.20"
      },
      {
        text: "£2,182.20"
      }
    ]
  ]
}) }}
```

## Tables with a lot of data
If possible, you should aim to have less data in your tables. If you have a lot of data, try to organise it into multiple tables or multiple pages.
If you cannot split your data, you can use the CSS class `govuk-table--small-text-until-tablet`. This class reduces the size of the text on small screens so large amounts of data has more empty space around it. This makes it easier to visually differentiate between each piece of data when read on small screens.
The CSS class `govuk-table--small-text-until-tablet` is only available in version 5.2 of GOV.UK Frontend and later.
Read about [updating your service to use the new type scale](./get-started/new-type-scale.md).
You should not use this class on tables unless your table has a lot of data, because a smaller amount of data is easier to read if the text is larger.
[ Open this example in a new tab: lots of data – table ](./components/table/lots-of-data.md)
  * [HTML](./components/table/#lots-of-data-table-example-html.md)
  * [Nunjucks](./components/table/#lots-of-data-table-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table govuk-table--small-text-until-tablet">
  <caption class="govuk-table__caption govuk-table__caption--m">Dates and amounts</caption>
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header">Date</th>
      <th scope="col" class="govuk-table__header">First amount</th>
      <th scope="col" class="govuk-table__header">Second amount</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">First 3 weeks</th>
      <td class="govuk-table__cell">£27.45 per week</td>
      <td class="govuk-table__cell">£33.90 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 6 weeks</th>
      <td class="govuk-table__cell">£27.45 per week</td>
      <td class="govuk-table__cell">£33.90 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 24 weeks</th>
      <td class="govuk-table__cell">£27.45 per week</td>
      <td class="govuk-table__cell">£33.90 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Next 33 weeks</th>
      <td class="govuk-table__cell">£27.45 per week</td>
      <td class="govuk-table__cell">£33.90 per week</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Total estimated pay</th>
      <td class="govuk-table__cell">£4,282.20</td>
      <td class="govuk-table__cell">£5,288.40</td>
    </tr>
  </tbody>
</table>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the table component. [ See macro options for rows](./components/table/#options-lots-of-data-table-example--rows.md).   |  
| head  | array  |  Can be used to add a row of table header cells (`<th>`) at the top of the table component. [ See macro options for head](./components/table/#options-lots-of-data-table-example--head.md).   |  
| caption  | string  |  Caption text.   |  
| captionClasses  | string  |  Classes for caption text size. Classes should correspond to the available typography heading classes.   |  
| firstCellIsHeader  | boolean  |  If set to `true`, the first cell in each row will be a table header (`<th>`).   |  
| classes  | string  |  Classes to add to the table container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML for cells in table rows. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table row cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Options for `head` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  If `html` is set, this is not required. Text for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  If `text` is set, this is not required. HTML for table head cells. If `html` is provided, the `text` option will be ignored.   |  
| format  | string  |  Specify format of a cell. Currently we only use “numeric”.   |  
| classes  | string  |  Classes to add to the table head cell.   |  
| colspan  | integer  |  Specify how many columns a cell extends.   |  
| rowspan  | integer  |  Specify how many rows a cell extends.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the table cell.   |  
Copy code
```
{% from "govuk/components/table/macro.njk" import govukTable %}

{{ govukTable({
  caption: "Dates and amounts",
  captionClasses: "govuk-table__caption--m",
  firstCellIsHeader: true,
  classes: "govuk-table--small-text-until-tablet",
  head: [
    {
      text: "Date"
    },
    {
      text: "First amount"
    },
    {
      text: "Second amount"
    }
  ],
  rows: [
    [
      {
        text: "First 3 weeks"
      },
      {
        text: "£27.45 per week"
      },
      {
        text: "£33.90 per week"
      }
    ],
    [
      {
        text: "Next 6 weeks"
      },
      {
        text: "£27.45 per week"
      },
      {
        text: "£33.90 per week"
      }
    ],
    [
      {
        text: "Next 24 weeks"
      },
      {
        text: "£27.45 per week"
      },
      {
        text: "£33.90 per week"
      }
    ],
    [
      {
        text: "Next 33 weeks"
      },
      {
        text: "£27.45 per week"
      },
      {
        text: "£33.90 per week"
      }
    ],
    [
      {
        text: "Total estimated pay"
      },
      {
        text: "£4,282.20"
      },
      {
        text: "£5,288.40"
      }
    ]
  ]
}) }}
```

## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Table’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/61) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/table/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/table/#top.md)
