#  Tag 
Use the Tag component to show users the status of something.
[ Open this example in a new tab: tag ](./components/tag/default.md)
  * [HTML](./components/tag/#tag-example-html.md)
  * [Nunjucks](./components/tag/#tag-example-nunjucks.md)

HTML
Copy code
```
<strong class="govuk-tag">
  Completed
</strong>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the tag.   |  
Copy code
```
{%- from "govuk/components/tag/macro.njk" import govukTag -%}

{{ govukTag({
  text: "Completed"
}) }}
```

## When to use this component
Use the Tag component when it’s possible for something to have more than one status and it’s useful for the user to know about that status. For example, you can use a tag to show whether an item in a [Task list component](./components/task-list.md) has been ‘completed’.
## How it works
There are two ways to use the Tag component. You can use HTML or, if you are using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
Tags are only used to indicate a status. Do not make a tag interactive by making it into a link or button. Use adjectives (descriptive words) and not verbs (action words) for the names of your tags. Using a verb might make a user think that clicking on them will do something.
Do not use tags to create links, buttons or other interactive elements, as users:
  * are unlikely to identify the tags as something they’re meant to interact with
  * would see no visual difference between interactive and non-interactive tags

## Showing one or two statuses
Sometimes a single status is enough. For example if you need to tell users which parts of an application they’ve finished and which they have not, you may only need a ‘Completed’ tag. Because the user understands that if something does not have a tag, that means it’s incomplete.
The [Complete multiple tasks pattern](./patterns/complete-multiple-tasks.md) has an example of how to show one status using tags.
Or it can make sense to have two statuses. For example you may find that there’s a need to have one tag for ‘Active’ users and one for ‘Inactive’ users.
[ Open this example in a new tab: multiple tags – tag ](./components/tag/multiple-tags.md)
  * [HTML](./components/tag/#multiple-tags-tag-example-html.md)
  * [Nunjucks](./components/tag/#multiple-tags-tag-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col"> Name of user </th>
      <th class="govuk-table__header" scope="col"> Status </th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachel Silver
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--grey">
          Inactive
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Jesse Smith
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--grey">
          Inactive
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Joshua Wessel
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag">
          Active
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachael Pepper
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag">
          Active
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Stuart Say
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--grey">
          Inactive
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Laura Frith
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag">
          Active
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Tim Harvey
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--grey">
          Inactive
        </strong>
      </td>
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the tag.   |  
Copy code
```
{%- from "govuk/components/tag/macro.njk" import govukTag -%}

<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col"> Name of user </th>
      <th class="govuk-table__header" scope="col"> Status </th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachel Silver
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Inactive",
          classes: "govuk-tag--grey"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Jesse Smith
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Inactive",
          classes: "govuk-tag--grey"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Joshua Wessel
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Active"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachael Pepper
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Active"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Stuart Say
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Inactive",
          classes: "govuk-tag--grey"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Laura Frith
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Active"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Tim Harvey
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Inactive",
          classes: "govuk-tag--grey"
        })}}
      </td>
    </tr>
  </tbody>
</table>
```

## Showing multiple statuses
Tags should be helpful to users. The more you add, the harder it is for users to remember them. So start with the smallest number of statuses you think might work, then add more if your user research shows there’s a need for them.
[ Open this example in a new tab: coloured tags – tag ](./components/tag/coloured-tags.md)
  * [HTML](./components/tag/#coloured-tags-tag-example-html.md)
  * [Nunjucks](./components/tag/#coloured-tags-tag-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col"> Application </th>
      <th class="govuk-table__header" scope="col"> Status </th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Joshua Wessel
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--red">
          Urgent
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachel Silver
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--blue">
          New
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Laura Frith
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--blue">
          New
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Paul French
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--blue">
          New
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Jesse Smith
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--blue">
          New
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachael Pepper
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--green">
          Finished
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Emma Tennant
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--yellow">
          Waiting on
        </strong>
      </td>
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the tag.   |  
Copy code
```
{%- from "govuk/components/tag/macro.njk" import govukTag -%}

<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col"> Application </th>
      <th class="govuk-table__header" scope="col"> Status </th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Joshua Wessel
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Urgent",
          classes: "govuk-tag--red"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachel Silver
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "New",
          classes: "govuk-tag--blue"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Laura Frith
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "New",
          classes: "govuk-tag--blue"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Paul French
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "New",
          classes: "govuk-tag--blue"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Jesse Smith
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "New",
          classes: "govuk-tag--blue"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Rachael Pepper
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Finished",
          classes: "govuk-tag--green"
        })}}
      </td>
    </tr>

    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        Emma Tennant
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Waiting on",
          classes: "govuk-tag--yellow"
        })}}
      </td>
    </tr>
  </tbody>
</table>
```

## Using colour with tags
You can use colour to help distinguish between different tags – or to help draw the user’s attention to a tag if it’s especially important. For example, it probably makes sense to use `govuk-tag--red` for a tag that reads ‘Urgent’.
Do not use colour alone to convey information, because it’s not accessible. If you use the same tag in more than one place, make sure you keep the colour consistent. This is to [meet WCAG 2.2 success criterion 1.4.1 Use of colour](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).
### Additional colours
If you need more tag colours, you can use the following colours.
[ Open this example in a new tab: all tag colours – tag ](./components/tag/all-colours.md)
  * [HTML](./components/tag/#all-tag-colours-tag-example-html.md)
  * [Nunjucks](./components/tag/#all-tag-colours-tag-example-nunjucks.md)

HTML
Copy code
```
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col"> Class name </th>
      <th class="govuk-table__header" scope="col"> Tag </th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--grey </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--grey">
          Inactive
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--green </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--green">
          New
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--teal </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--teal">
          Active
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--blue </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--blue">
          Pending
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--purple </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--purple">
          Received
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--magenta </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--magenta">
          Sent
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--red </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--red">
          Rejected
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--orange </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--orange">
          Declined
        </strong>
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--yellow </code>
      </td>
      <td class="govuk-table__cell">
        <strong class="govuk-tag govuk-tag--yellow">
          Delayed
        </strong>
      </td>
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
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the tag component. If `html` is provided, the `text` option will be ignored.   |  
| classes  | string  |  Classes to add to the tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the tag.   |  
Copy code
```
{%- from "govuk/components/tag/macro.njk" import govukTag -%}

<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col"> Class name </th>
      <th class="govuk-table__header" scope="col"> Tag </th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--grey </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Inactive",
          classes: "govuk-tag--grey"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--green </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "New",
          classes: "govuk-tag--green"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--teal </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Active",
          classes: "govuk-tag--teal"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--blue </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Pending",
          classes: "govuk-tag--blue"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--purple </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Received",
          classes: "govuk-tag--purple"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--magenta </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Sent",
          classes: "govuk-tag--magenta"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--red </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Rejected",
          classes: "govuk-tag--red"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--orange </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Declined",
          classes: "govuk-tag--orange"
        })}}
      </td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">
        <code> govuk-tag--yellow </code>
      </td>
      <td class="govuk-table__cell">
        {{govukTag({
          text: "Delayed",
          classes: "govuk-tag--yellow"
        })}}
      </td>
    </tr>
  </tbody>
</table>
```

## Research on this component
### Colour and style updates from the GOV.UK brand refresh
In February 2026, we updated the Tag component as part of colour changes to the GOV.UK brand. As part of this work, we also improved colour contrast and made the tags easier to distinguish from buttons.
### Colour in tags
The Department for Education first introduced coloured tags into the Design System through a contributions.
They’re being used in:
  * apply for teacher training (used by citizens)
  * manage teacher training applications (used by teacher training providers)

### Text in tags
The Tag component previously used uppercase bold text for the tags. This was changed as some research has shown that uppercase text can be harder to read, particularly for longer tag text.
The Tag component previously used white text on a dark coloured background. Research from multiple teams found that some users perceived these as buttons and tried to click on them. The design was changed to try and avoid this, by using a lighter background colour and darker text.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Tag’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/62) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/tag/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/tag/#top.md)
