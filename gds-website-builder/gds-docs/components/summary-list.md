#  Summary list 
Use a summary list to summarise information, for example, a user’s responses at the end of a form.
[ Open this example in a new tab: summary list ](./components/summary-list/default.md)
  * [HTML](./components/summary-list/#summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#summary-list-example-nunjucks.md)

HTML
Copy code
```
<dl class="govuk-summary-list">
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Name
    </dt>
    <dd class="govuk-summary-list__value">
      Sarah Philips
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> name</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Date of birth
    </dt>
    <dd class="govuk-summary-list__value">
      5 January 1978
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> date of birth</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Address
    </dt>
    <dd class="govuk-summary-list__value">
      72 Guild Street<br>London<br>SE23 6FH
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> address</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Contact details
    </dt>
    <dd class="govuk-summary-list__value">
      <p class="govuk-body">07700 900457</p>
      <p class="govuk-body">sarah.phillips@example.com</p>
    </dd>
    <dd class="govuk-summary-list__actions">
      <ul class="govuk-summary-list__actions-list">
        <li class="govuk-summary-list__actions-list-item">
          <a class="govuk-link" href="#">Add<span class="govuk-visually-hidden"> contact details</span></a>
        </li>
        <li class="govuk-summary-list__actions-list-item">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> contact details</span></a>
        </li>
      </ul>
    </dd>
  </div>
</dl>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  rows: [
    {
      key: {
        text: "Name"
      },
      value: {
        text: "Sarah Philips"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "name"
          }
        ]
      }
    },
    {
      key: {
        text: "Date of birth"
      },
      value: {
        text: "5 January 1978"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "date of birth"
          }
        ]
      }
    },
    {
      key: {
        text: "Address"
      },
      value: {
        html: "72 Guild Street<br>London<br>SE23 6FH"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "address"
          }
        ]
      }
    },
    {
      key: {
        text: "Contact details"
      },
      value: {
        html: '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Add",
            visuallyHiddenText: "contact details"
          },
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "contact details"
          }
        ]
      }
    }
  ]
}) }}
```

## When to use this component
Use a summary list to show information as a list of key facts.
You can use it to display metadata like ‘Last updated’ with a date like ‘22 June 2018’, or to summarise a user’s responses at the end of a form like the [Check answers pattern](./patterns/check-answers.md).
[Summary cards are a variant within this component](./components/summary-list/#summary-cards.md). You can use summary cards to show multiple summary lists that describe the same type of thing, such as people. You can also add card actions that apply to the entire summary list.
## When not to use this component
The summary list uses the description list (`<dl>`) HTML element, so only use it to present information that has a key and at least one value.
Do not use it for tabular data or a simple list of information or tasks, like a [Task list component](./components/task-list.md). For those use a `<table>`, `<ul>` or `<ol>`.
## How it works
Each row of a summary list is made up of a:
  * ‘key’ that’s a description or label of a piece of information, like “Name”
  * ‘value’ which is the piece of information itself, such as “John Smith”

You can show a single or multiple summary lists on a page. If you’re showing multiple summary lists on a page, you can add structure by using headings or summary cards.
There are 2 ways to use the summary list component. You can use HTML or, if you’re using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: without actions – summary list ](./components/summary-list/without-actions.md)
  * [HTML](./components/summary-list/#without-actions-summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#without-actions-summary-list-example-nunjucks.md)

HTML
Copy code
```
<dl class="govuk-summary-list">
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Name
    </dt>
    <dd class="govuk-summary-list__value">
      Sarah Philips
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Date of birth
    </dt>
    <dd class="govuk-summary-list__value">
      5 January 1978
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Address
    </dt>
    <dd class="govuk-summary-list__value">
      72 Guild Street<br>London<br>SE23 6FH
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Contact details
    </dt>
    <dd class="govuk-summary-list__value">
      <p class="govuk-body">07700 900457</p>
      <p class="govuk-body">sarah.phillips@example.com</p>
    </dd>
  </div>
</dl>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-without-actions-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-without-actions-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-without-actions-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-without-actions-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-without-actions-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-without-actions-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-without-actions-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-without-actions-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-without-actions-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  rows: [
    {
      key: {
        text: "Name"
      },
      value: {
        text: "Sarah Philips"
      }
    },
    {
      key: {
        text: "Date of birth"
      },
      value: {
        text: "5 January 1978"
      }
    },
    {
      key: {
        text: "Address"
      },
      value: {
        html: "72 Guild Street<br>London<br>SE23 6FH"
      }
    },
    {
      key: {
        text: "Contact details"
      },
      value: {
        html: '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      }
    }
  ]
}) }}
```

### Adding actions to each row
You can add ‘row actions’ to a summary list. For example, you can help users go back and edit an answer by adding a ‘change’ link.
When navigating visually, the borders above and below each row help to show which row action is tied to which piece of information.
Assistive technology users, including those who use a screen reader, might hear a row action link out of context and might not know what it will do. To give more context, add visually hidden text to the links. This means a screen reader user will hear the row action and the ‘key’ label for the information it will affect, like ‘Change name’ or ‘Change date of birth’.
If a user decides to go back to a previous answer through a card or row action, make sure information they’ve already entered is pre-populated.
[ Open this example in a new tab: summary list second ](./components/summary-list/default.md)
  * [HTML](./components/summary-list/#summary-list-second-example-html.md)
  * [Nunjucks](./components/summary-list/#summary-list-second-example-nunjucks.md)

HTML
Copy code
```
<dl class="govuk-summary-list">
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Name
    </dt>
    <dd class="govuk-summary-list__value">
      Sarah Philips
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> name</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Date of birth
    </dt>
    <dd class="govuk-summary-list__value">
      5 January 1978
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> date of birth</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Address
    </dt>
    <dd class="govuk-summary-list__value">
      72 Guild Street<br>London<br>SE23 6FH
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> address</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Contact details
    </dt>
    <dd class="govuk-summary-list__value">
      <p class="govuk-body">07700 900457</p>
      <p class="govuk-body">sarah.phillips@example.com</p>
    </dd>
    <dd class="govuk-summary-list__actions">
      <ul class="govuk-summary-list__actions-list">
        <li class="govuk-summary-list__actions-list-item">
          <a class="govuk-link" href="#">Add<span class="govuk-visually-hidden"> contact details</span></a>
        </li>
        <li class="govuk-summary-list__actions-list-item">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> contact details</span></a>
        </li>
      </ul>
    </dd>
  </div>
</dl>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-summary-list-second-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-summary-list-second-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-summary-list-second-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-summary-list-second-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-summary-list-second-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-summary-list-second-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-summary-list-second-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-summary-list-second-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-summary-list-second-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  rows: [
    {
      key: {
        text: "Name"
      },
      value: {
        text: "Sarah Philips"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "name"
          }
        ]
      }
    },
    {
      key: {
        text: "Date of birth"
      },
      value: {
        text: "5 January 1978"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "date of birth"
          }
        ]
      }
    },
    {
      key: {
        text: "Address"
      },
      value: {
        html: "72 Guild Street<br>London<br>SE23 6FH"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "address"
          }
        ]
      }
    },
    {
      key: {
        text: "Contact details"
      },
      value: {
        html: '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Add",
            visuallyHiddenText: "contact details"
          },
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "contact details"
          }
        ]
      }
    }
  ]
}) }}
```

#### Showing rows with and without actions
If you’re showing a mix of rows (where some rows include actions and some do not), add the `govuk-summary-list__row--no-actions` modifier class to the rows without actions. This is to ensure the bottom border is drawn correctly in some browsers.
[ Open this example in a new tab: summary list with a mix of rows with and without actions – summary list ](./components/summary-list/mixed-actions.md)
  * [HTML](./components/summary-list/#summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example-nunjucks.md)

HTML
Copy code
```
<dl class="govuk-summary-list">
  <div class="govuk-summary-list__row govuk-summary-list__row--no-actions">
    <dt class="govuk-summary-list__key">
      Name
    </dt>
    <dd class="govuk-summary-list__value">
      Sarah Philips
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Date of birth
    </dt>
    <dd class="govuk-summary-list__value">
      5 January 1978
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> date of birth</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Address
    </dt>
    <dd class="govuk-summary-list__value">
      72 Guild Street<br>London<br>SE23 6FH
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> address</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Contact details
    </dt>
    <dd class="govuk-summary-list__value">
      <p class="govuk-body">07700 900457</p>
      <p class="govuk-body">sarah.phillips@example.com</p>
    </dd>
    <dd class="govuk-summary-list__actions">
      <ul class="govuk-summary-list__actions-list">
        <li class="govuk-summary-list__actions-list-item">
          <a class="govuk-link" href="#">Add<span class="govuk-visually-hidden"> contact details</span></a>
        </li>
        <li class="govuk-summary-list__actions-list-item">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> contact details</span></a>
        </li>
      </ul>
    </dd>
  </div>
</dl>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-summary-list-with-a-mix-of-rows-with-and-without-actions-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  rows: [
    {
      key: {
        text: "Name"
      },
      value: {
        text: "Sarah Philips"
      }
    },
    {
      key: {
        text: "Date of birth"
      },
      value: {
        text: "5 January 1978"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "date of birth"
          }
        ]
      }
    },
    {
      key: {
        text: "Address"
      },
      value: {
        html: "72 Guild Street<br>London<br>SE23 6FH"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "address"
          }
        ]
      }
    },
    {
      key: {
        text: "Contact details"
      },
      value: {
        html: '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Add",
            visuallyHiddenText: "contact details"
          },
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "contact details"
          }
        ]
      }
    }
  ]
}) }}
```

### Removing the borders
The summary list includes separating borders to help users by joining the information on each row and its action together.
Think carefully before you remove row borders. Borders help many users find and read information that’s laid out in rows, especially users who zoom in on pages or use assistive technologies to magnify their screen.
If your summary list does not have any actions, you can choose to remove the separating borders with the `govuk-summary-list--no-border` class.
[ Open this example in a new tab: without borders – summary list ](./components/summary-list/without-borders.md)
  * [HTML](./components/summary-list/#without-borders-summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#without-borders-summary-list-example-nunjucks.md)

HTML
Copy code
```
<dl class="govuk-summary-list govuk-summary-list--no-border">
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Name
    </dt>
    <dd class="govuk-summary-list__value">
      Sarah Philips
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Date of birth
    </dt>
    <dd class="govuk-summary-list__value">
      5 January 1978
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Address
    </dt>
    <dd class="govuk-summary-list__value">
      72 Guild Street<br>London<br>SE23 6FH
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Contact details
    </dt>
    <dd class="govuk-summary-list__value">
      <p class="govuk-body">07700 900457</p>
      <p class="govuk-body">sarah.phillips@example.com</p>
    </dd>
  </div>
</dl>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-without-borders-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-without-borders-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-without-borders-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-without-borders-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-without-borders-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-without-borders-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-without-borders-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-without-borders-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-without-borders-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  classes: "govuk-summary-list--no-border",
  rows: [
    {
      key: {
        text: "Name"
      },
      value: {
        text: "Sarah Philips"
      }
    },
    {
      key: {
        text: "Date of birth"
      },
      value: {
        text: "5 January 1978"
      }
    },
    {
      key: {
        text: "Address"
      },
      value: {
        html: "72 Guild Street<br>London<br>SE23 6FH"
      }
    },
    {
      key: {
        text: "Contact details"
      },
      value: {
        html: '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      }
    }
  ]
}) }}
```

To remove borders on a single row, use the `govuk-summary-list__row--no-border` class.
### Showing missing information
In some contexts, you might need to show rows that have missing information. This can happen when:
  * a user returns to an incomplete journey
  * you’ve added or changed the questions in a service.

Show a link to the appropriate question page in the `value` column so the user can enter the missing information, instead of showing a ‘change’ link on that row.
[ Open this example in a new tab: summary list with missing information – summary list ](./components/summary-list/with-missing-information.md)
  * [HTML](./components/summary-list/#summary-list-with-missing-information-summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#summary-list-with-missing-information-summary-list-example-nunjucks.md)

HTML
Copy code
```
<dl class="govuk-summary-list">
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Name
    </dt>
    <dd class="govuk-summary-list__value">
      Sarah Philips
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> name</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row">
    <dt class="govuk-summary-list__key">
      Date of birth
    </dt>
    <dd class="govuk-summary-list__value">
      5 January 1978
    </dd>
    <dd class="govuk-summary-list__actions">
      <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> date of birth</span></a>
    </dd>
  </div>
  <div class="govuk-summary-list__row govuk-summary-list__row--no-actions">
    <dt class="govuk-summary-list__key">
      Contact information
    </dt>
    <dd class="govuk-summary-list__value">
      <a href="#" class="govuk-link">Enter contact information</a>
    </dd>
  </div>
  <div class="govuk-summary-list__row govuk-summary-list__row--no-actions">
    <dt class="govuk-summary-list__key">
      Contact details
    </dt>
    <dd class="govuk-summary-list__value">
      <a href="#" class="govuk-link">Enter contact details</a>
    </dd>
  </div>
</dl>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-summary-list-with-missing-information-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  rows: [
    {
      key: {
        text: "Name"
      },
      value: {
        text: "Sarah Philips"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "name"
          }
        ]
      }
    },
    {
      key: {
        text: "Date of birth"
      },
      value: {
        text: "5 January 1978"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "date of birth"
          }
        ]
      }
    },
    {
      key: {
        text: "Contact information"
      },
      value: {
        html: '<a href="#" class="govuk-link">Enter contact information</a>'
      }
    },
    {
      key: {
        text: "Contact details"
      },
      value: {
        html: '<a href="#" class="govuk-link">Enter contact details</a>'
      }
    }
  ]
}) }}
```

## Summary cards
If you’re showing multiple summary lists on a page, you can show each list within a summary card. This lets you visually separate each summary list and give each a title and some actions.
Use summary cards when you need to show:
  * multiple summary lists that all describe the same type of thing, such as people
  * actions that will apply to all the items in a list

Summary cards are often used in case working systems to help users quickly view a set of information and related actions.
Do not use summary cards if you only need to show a small amount of related information. Use summary lists instead, and structure them with headings if needed.
If you’re showing summary cards at the end of a longer journey, you might want to familiarise the user with them earlier on – such as when the user reviews individual sections.
### Card titles
Use the summary card’s header area to give each summary list a title.
Each title must be unique and help identify what the summary list describes. For example, this could be the name of a specific person, organisation or professional qualification.
Try to keep titles short and relevant. You can use one or two important values in the summary list – such as the first and last name of a person.
[ Open this example in a new tab: summary in a card with a title – summary list ](./components/summary-list/card-with-title.md)
  * [HTML](./components/summary-list/#summary-in-a-card-with-a-title-summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#summary-in-a-card-with-a-title-summary-list-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-summary-card">
  <div class="govuk-summary-card__title-wrapper">
    <h2 class="govuk-summary-card__title">
      Lead tenant
    </h2>
  </div>
  <div class="govuk-summary-card__content">
    <dl class="govuk-summary-list">
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Age
        </dt>
        <dd class="govuk-summary-list__value">
          38
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> age (Lead tenant)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Nationality
        </dt>
        <dd class="govuk-summary-list__value">
          UK national resident in UK
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> nationality (Lead tenant)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Working situation
        </dt>
        <dd class="govuk-summary-list__value">
          Part time – less than 30 hours a week
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> working situation (Lead tenant)</span></a>
        </dd>
      </div>
    </dl>
  </div>
</div>
<div class="govuk-summary-card">
  <div class="govuk-summary-card__title-wrapper">
    <h2 class="govuk-summary-card__title">
      Person 2
    </h2>
  </div>
  <div class="govuk-summary-card__content">
    <dl class="govuk-summary-list">
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Details known
        </dt>
        <dd class="govuk-summary-list__value">
          Yes
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> whether details are known (Person 2)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Relationship to lead tenant
        </dt>
        <dd class="govuk-summary-list__value">
          Partner
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> relationship to lead tenant (Person 2)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Age
        </dt>
        <dd class="govuk-summary-list__value">
          42
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> age (Person 2)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Working situation
        </dt>
        <dd class="govuk-summary-list__value">
          Unable to work because of long-term sickness or disability
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> working situation (Person 2)</span></a>
        </dd>
      </div>
    </dl>
  </div>
</div>
<div class="govuk-summary-card">
  <div class="govuk-summary-card__title-wrapper">
    <h2 class="govuk-summary-card__title">
      Person 3
    </h2>
  </div>
  <div class="govuk-summary-card__content">
    <dl class="govuk-summary-list">
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Details known
        </dt>
        <dd class="govuk-summary-list__value">
          Yes
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> whether details are known (Person 3)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Relationship to lead tenant
        </dt>
        <dd class="govuk-summary-list__value">
          Child
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> relationship to lead tenant (Person 3)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Age
        </dt>
        <dd class="govuk-summary-list__value">
          7
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> age (Person 3)</span></a>
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Working situation
        </dt>
        <dd class="govuk-summary-list__value">
          Child under 16
        </dd>
        <dd class="govuk-summary-list__actions">
          <a class="govuk-link" href="#">Change<span class="govuk-visually-hidden"> working situation (Person 3)</span></a>
        </dd>
      </div>
    </dl>
  </div>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-summary-in-a-card-with-a-title-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  card: {
    title: {
      text: "Lead tenant"
    }
  },
  rows: [
    {
      key: {
        text: "Age"
      },
      value: {
        html: "38"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "age"
          }
        ]
      }
    },
    {
      key: {
        text: "Nationality"
      },
      value: {
        html: "UK national resident in UK"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "nationality"
          }
        ]
      }
    },
    {
      key: {
        text: "Working situation"
      },
      value: {
        html: "Part time – less than 30 hours a week"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "working situation"
          }
        ]
      }
    }
  ]
}) }}

{{ govukSummaryList({
  card: {
    title: {
      text: "Person 2"
    }
  },
  rows: [
    {
      key: {
        text: "Details known"
      },
      value: {
        html: "Yes"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "whether details are known"
          }
        ]
      }
    },
    {
      key: {
        text: "Relationship to lead tenant"
      },
      value: {
        html: "Partner"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "relationship to lead tenant"
          }
        ]
      }
    },
    {
      key: {
        text: "Age"
      },
      value: {
        html: "42"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "age"
          }
        ]
      }
    },
    {
      key: {
        text: "Working situation"
      },
      value: {
        html: "Unable to work because of long-term sickness or disability"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "working situation"
          }
        ]
      }
    }
  ]
}) }}

{{ govukSummaryList({
  card: {
    title: {
      text: "Person 3"
    }
  },
  rows: [
    {
      key: {
        text: "Details known"
      },
      value: {
        html: "Yes"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "whether details are known"
          }
        ]
      }
    },
    {
      key: {
        text: "Relationship to lead tenant"
      },
      value: {
        html: "Child"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "relationship to lead tenant"
          }
        ]
      }
    },
    {
      key: {
        text: "Age"
      },
      value: {
        html: "7"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "age"
          }
        ]
      }
    },
    {
      key: {
        text: "Working situation"
      },
      value: {
        html: "Child under 16"
      },
      actions: {
        items: [
          {
            href: "#",
            text: "Change",
            visuallyHiddenText: "working situation"
          }
        ]
      }
    }
  ]
}) }}
```

### Adding card actions
You can add card actions in the header, which will be shown after the summary card’s title.
For example, if you have multiple rows with “change” actions that all take the user to the same place, you can show a single “change” card action instead. This helps avoid repeating the same row action on every row.
Card actions are shown in bold text to make them visually distinct from row actions – and help alert the user that the card action will affect the entire summary card.
Write link text for card actions to tell the user what the card action will do and that it will apply to the entire summary card. It should also be as short as possible, usually 2 words.
Example card actions include:
  * Remove tenant
  * Edit qualification
  * Update issue
  * Approve application
  * Cancel order

Keep it short and do not add more than 2 to 3 actions in a header.
If a card action cannot easily be undone or might have serious consequences, consider adding a warning or asking the user for confirmation.
[ Open this example in a new tab: summary in a card with a title and actions – summary list ](./components/summary-list/card-with-actions.md)
  * [HTML](./components/summary-list/#summary-in-a-card-with-a-title-and-actions-summary-list-example-html.md)
  * [Nunjucks](./components/summary-list/#summary-in-a-card-with-a-title-and-actions-summary-list-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-summary-card">
  <div class="govuk-summary-card__title-wrapper">
    <h2 class="govuk-summary-card__title">
      University of Gloucestershire
    </h2>
    <ul class="govuk-summary-card__actions">
      <li class="govuk-summary-card__action">
        <a class="govuk-link" href="#">Delete choice<span class="govuk-visually-hidden"> (University of Gloucestershire)</span></a>
      </li>
      <li class="govuk-summary-card__action">
        <a class="govuk-link" href="#">Withdraw<span class="govuk-visually-hidden"> (University of Gloucestershire)</span></a>
      </li>
    </ul>
  </div>
  <div class="govuk-summary-card__content">
    <dl class="govuk-summary-list">
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Course
        </dt>
        <dd class="govuk-summary-list__value">
          English (3DMD)<br>PGCE with QTS full time
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Location
        </dt>
        <dd class="govuk-summary-list__value">
          School name<br>Road, City, SW1 1AA
        </dd>
      </div>
    </dl>
  </div>
</div>
<div class="govuk-summary-card">
  <div class="govuk-summary-card__title-wrapper">
    <h2 class="govuk-summary-card__title">
      University of Bristol
    </h2>
    <ul class="govuk-summary-card__actions">
      <li class="govuk-summary-card__action">
        <a class="govuk-link" href="#">Delete choice<span class="govuk-visually-hidden"> (University of Bristol)</span></a>
      </li>
      <li class="govuk-summary-card__action">
        <a class="govuk-link" href="#">Withdraw<span class="govuk-visually-hidden"> (University of Bristol)</span></a>
      </li>
    </ul>
  </div>
  <div class="govuk-summary-card__content">
    <dl class="govuk-summary-list">
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Course
        </dt>
        <dd class="govuk-summary-list__value">
          English (Q3X1)<br>PGCE with QTS full time
        </dd>
      </div>
      <div class="govuk-summary-list__row">
        <dt class="govuk-summary-list__key">
          Location
        </dt>
        <dd class="govuk-summary-list__value">
          School name<br>Road, City, SW2 1AA
        </dd>
      </div>
    </dl>
  </div>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| rows  | array  |  **Required.** The rows within the summary list component. [ See macro options for rows](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--rows.md).   |  
| card  | object  |  Can be used to wrap a summary card around the summary list component. If any of these options are present, a summary card will wrap around the summary list. [ See macro options for card](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--card.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for `rows` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the row `div`.   |  
| key  | object  |  **Required.** The reference content (key) for each row item in the summary list component. [ See macro options for rows key](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--rows-key.md).   |  
| value  | object  |  **Required.** The value for each row item in the summary list component. [ See macro options for rows value](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--rows-value.md).   |  
| actions  | object  |  The action link content for each row item in the summary list component. [ See macro options for rows actions](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--rows-actions.md).   |  
Options for rows `key` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each key. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the key wrapper.   |  
Options for rows `value` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each value. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the value wrapper.   |  
Options for rows `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items within the row item of the summary list component. [ See macro options for rows actions items](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--rows-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for rows actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Options for `card` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  Data for the summary card header. [ See macro options for card title](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--card-title.md).   |  
| actions  | object  |  The action link content shown in the header of each summary card wrapped around the summary list component. [ See macro options for card actions](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--card-actions.md).   |  
| classes  | string  |  Classes to add to the container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the container.   |  
Options for card `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  Text to use within each title. If `html` is provided, the `text` option will be ignored.   |  
| headingLevel  | integer  |  Heading level, from `1` to `6`. Default is `2`.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for card `actions` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The action link items shown in the header within the summary card wrapped around the summary list component. [ See macro options for card actions items](./components/summary-list/#options-summary-in-a-card-with-a-title-and-actions-summary-list-example--card-actions-items.md).   |  
| classes  | string  |  Classes to add to the actions wrapper.   |  
Options for card actions `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| href  | string  |  **Required.** The value of the link’s `href` attribute for an action item.   |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within each action item. If `html` is provided, the `text` option will be ignored.   |  
| visuallyHiddenText  | string  |  Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use `html` for more complicated scenarios.   |  
| classes  | string  |  Classes to add to the action item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the action item.   |  
Copy code
```
{% from "govuk/components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  card: {
    title: {
      text: "University of Gloucestershire"
    },
    actions: {
      items: [
        {
          href: "#",
          text: "Delete choice"
        },
        {
          href: "#",
          text: "Withdraw"
        }
      ]
    }
  },
  rows: [
    {
      key: {
        text: "Course"
      },
      value: {
        html: "English (3DMD)<br>PGCE with QTS full time"
      }
    },
    {
      key: {
        text: "Location"
      },
      value: {
        html: "School name<br>Road, City, SW1 1AA"
      }
    }
  ]
}) }}

{{ govukSummaryList({
  card: {
    title: {
      text: "University of Bristol"
    },
    actions: {
      items: [
        {
          href: "#",
          text: "Delete choice"
        },
        {
          href: "#",
          text: "Withdraw"
        }
      ]
    }
  },
  rows: [
    {
      key: {
        text: "Course"
      },
      value: {
        html: "English (Q3X1)<br>PGCE with QTS full time"
      }
    },
    {
      key: {
        text: "Location"
      },
      value: {
        html: "School name<br>Road, City, SW2 1AA"
      }
    }
  ]
}) }}
```

## Research on this component
This component was developed and tested by the Government Digital Service as part of the [check answers pattern](./patterns/check-answers.md).
The Department for Education contributed the summary card. It’s being used in some of their services, such as:
  * [Apply for teacher training](https://www.gov.uk/apply-for-teacher-training), used by the general public
  * [Register trainee teachers](https://www.register-trainee-teachers.service.gov.uk/), used by people that work for training providers

The summary card is also used in services run by other departments, such us:
  * manage supervisions (Ministry of Justice)
  * submit social housing lettings and sales data (Department for Levelling Up, Housing & Communities)

### Next steps
We still want to learn more about when this component works well.
If you use this component in your service, we’d like to hear about how you use the summary list and summary card, as well as any research findings you might have.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Summary list’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/182) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/summary-list/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/summary-list/#top.md)
