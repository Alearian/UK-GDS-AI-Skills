#  Pagination 
Help users navigate forwards and backwards through a series of pages. For example, search results or guidance that’s divided into multiple website pages – like [the GOV.UK mainstream guide format](https://prototype-kit.service.gov.uk/docs/templates/mainstream-guide).
[ Open this example in a new tab: pagination ](./components/pagination/default.md)
  * [HTML](./components/pagination/#pagination-example-html.md)
  * [Nunjucks](./components/pagination/#pagination-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-pagination" aria-label="Pagination">
  <div class="govuk-pagination__prev">
    <a class="govuk-link govuk-pagination__link" href="#" rel="prev">
      <svg class="govuk-pagination__icon govuk-pagination__icon--prev" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m6.5938-0.0078125-6.7266 6.7266 6.7441 6.4062 1.377-1.449-4.1856-3.9768h12.896v-2h-12.984l4.2931-4.293-1.414-1.414z"></path>
      </svg>
      <span class="govuk-pagination__link-title">
        Previous<span class="govuk-visually-hidden"> page</span>
      </span>
    </a>
  </div>
  <ul class="govuk-pagination__list">
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 1">
        1
      </a>
    </li>
    <li class="govuk-pagination__item govuk-pagination__item--current">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 2" aria-current="page">
        2
      </a>
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 3">
        3
      </a>
    </li>
  </ul>
  <div class="govuk-pagination__next">
    <a class="govuk-link govuk-pagination__link" href="#" rel="next">
      <span class="govuk-pagination__link-title">
        Next<span class="govuk-visually-hidden"> page</span>
      </span>
      <svg class="govuk-pagination__icon govuk-pagination__icon--next" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m8.107-0.0078125-1.4136 1.414 4.2926 4.293h-12.986v2h12.896l-4.1855 3.9766 1.377 1.4492 6.7441-6.4062-6.7246-6.7266z"></path>
      </svg>
    </a>
  </div>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The items within the pagination component. [ See macro options for items](./components/pagination/#options-pagination-example--items.md).   |  
| previous  | object  |  A link to the previous page, if there is a previous page. [ See macro options for previous](./components/pagination/#options-pagination-example--previous.md).   |  
| next  | object  |  A link to the next page, if there is a next page. [ See macro options for next](./components/pagination/#options-pagination-example--next.md).   |  
| landmarkLabel  | string  |  The label for the navigation landmark that wraps the pagination. Defaults to `"Pagination"`.   |  
| classes  | string  |  The classes you want to add to the pagination `nav` parent.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the pagination `nav` parent.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| number  | string  |  The pagination item text – usually a page number. Required unless the item is an ellipsis.   |  
| visuallyHiddenText  | string  |  The visually hidden label for the pagination item, which will be applied to an `aria-label` and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example “Page 1”.   |  
| href  | string  |  The link’s URL. Required unless the item is an ellipsis.   |  
| current  | boolean  |  Set to `true` to indicate the current page the user is on.   |  
| ellipsis  | boolean  |  Use this option if you want to specify an ellipsis at a given point between numbers. If you set this option as `true`, any other options for the item are ignored.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `previous` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the previous page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The previous page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `next` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the next page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The next page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Copy code
```
{% from "govuk/components/pagination/macro.njk" import govukPagination %}

{{ govukPagination({
  previous: {
    href: "#"
  },
  next: {
    href: "#"
  },
  items: [
    {
      number: 1,
      href: "#"
    },
    {
      number: 2,
      current: true,
      href: "#"
    },
    {
      number: 3,
      href: "#"
    }
  ]
}) }}
```

## When to use this component
Consider using pagination when:
  * showing all the content on a single page makes the page take too long to load
  * most users will only need the content on the first page or first few pages

## When not to use this component
Only break up content onto separate pages if it improves the performance or usability of your service.
Avoid using the ‘infinite scroll’ technique to automatically load content when the user approaches the bottom of the page. This causes problems for keyboard users.
Do not use this Pagination component for linear journeys – for example, where you’re asking the user to complete a form. Instead, use the [Button component](./components/button.md) (usually a ‘Continue’ button) to let the user move to the next page – and a [Back link component](./components/back-link.md) to let them move to the previous page.
## How it works
Add the pagination component after the content on each page that you’re paginating.
[View an example of Pagination in a standard GOV.UK page template](./components/pagination/in-page.md).
Do not show pagination if there’s only one page of content.
Redirect users to the first page if they enter a URL of a page that no longer exists.
## For navigating between content pages
Use the ‘block’ style of pagination to let users navigate through related content that has been split across multiple pages. Stack the links vertically, so they’re more obvious to screen magnifier users when they’re zoomed in.
You can use link labels to give context on what the neighbouring pages are about.
[ Open this example in a new tab: pagination with text labels – pagination ](./components/pagination/for-content-pages.md)
  * [HTML](./components/pagination/#pagination-with-text-labels-pagination-example-html.md)
  * [Nunjucks](./components/pagination/#pagination-with-text-labels-pagination-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-pagination govuk-pagination--block" aria-label="Pagination">
  <div class="govuk-pagination__prev">
    <a class="govuk-link govuk-pagination__link" href="#" rel="prev">
      <svg class="govuk-pagination__icon govuk-pagination__icon--prev" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m6.5938-0.0078125-6.7266 6.7266 6.7441 6.4062 1.377-1.449-4.1856-3.9768h12.896v-2h-12.984l4.2931-4.293-1.414-1.414z"></path>
      </svg>
      <span class="govuk-pagination__link-title">
        Previous<span class="govuk-visually-hidden"> page</span>
      </span>
      <span class="govuk-visually-hidden">:</span>
      <span class="govuk-pagination__link-label">Applying for a provisional lorry or bus licence</span>
    </a>
  </div>
  <div class="govuk-pagination__next">
    <a class="govuk-link govuk-pagination__link" href="#" rel="next">
      <svg class="govuk-pagination__icon govuk-pagination__icon--next" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m8.107-0.0078125-1.4136 1.414 4.2926 4.293h-12.986v2h12.896l-4.1855 3.9766 1.377 1.4492 6.7441-6.4062-6.7246-6.7266z"></path>
      </svg>
      <span class="govuk-pagination__link-title">
        Next<span class="govuk-visually-hidden"> page</span>
      </span>
      <span class="govuk-visually-hidden">:</span>
      <span class="govuk-pagination__link-label">Driver CPC part 1 test: theory</span>
    </a>
  </div>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The items within the pagination component. [ See macro options for items](./components/pagination/#options-pagination-with-text-labels-pagination-example--items.md).   |  
| previous  | object  |  A link to the previous page, if there is a previous page. [ See macro options for previous](./components/pagination/#options-pagination-with-text-labels-pagination-example--previous.md).   |  
| next  | object  |  A link to the next page, if there is a next page. [ See macro options for next](./components/pagination/#options-pagination-with-text-labels-pagination-example--next.md).   |  
| landmarkLabel  | string  |  The label for the navigation landmark that wraps the pagination. Defaults to `"Pagination"`.   |  
| classes  | string  |  The classes you want to add to the pagination `nav` parent.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the pagination `nav` parent.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| number  | string  |  The pagination item text – usually a page number. Required unless the item is an ellipsis.   |  
| visuallyHiddenText  | string  |  The visually hidden label for the pagination item, which will be applied to an `aria-label` and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example “Page 1”.   |  
| href  | string  |  The link’s URL. Required unless the item is an ellipsis.   |  
| current  | boolean  |  Set to `true` to indicate the current page the user is on.   |  
| ellipsis  | boolean  |  Use this option if you want to specify an ellipsis at a given point between numbers. If you set this option as `true`, any other options for the item are ignored.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `previous` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the previous page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The previous page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `next` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the next page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The next page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Copy code
```
{% from "govuk/components/pagination/macro.njk" import govukPagination %}

{{ govukPagination({
  previous: {
    labelText: "Applying for a provisional lorry or bus licence",
    href: "#"
  },
  next: {
    labelText: "Driver CPC part 1 test: theory",
    href: "#"
  }
}) }}
```

## For navigating between pages of items
Use a list-type layout if users need to navigate through pages of similar items. For example, a list of search results or a list of cases in a case working system.
[ Open this example in a new tab: pagination with numbered labels – pagination ](./components/pagination/for-list-pages.md)
  * [HTML](./components/pagination/#pagination-with-numbered-labels-pagination-example-html.md)
  * [Nunjucks](./components/pagination/#pagination-with-numbered-labels-pagination-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-pagination" aria-label="Pagination">
  <div class="govuk-pagination__prev">
    <a class="govuk-link govuk-pagination__link" href="#" rel="prev">
      <svg class="govuk-pagination__icon govuk-pagination__icon--prev" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m6.5938-0.0078125-6.7266 6.7266 6.7441 6.4062 1.377-1.449-4.1856-3.9768h12.896v-2h-12.984l4.2931-4.293-1.414-1.414z"></path>
      </svg>
      <span class="govuk-pagination__link-title">
        Previous<span class="govuk-visually-hidden"> page</span>
      </span>
    </a>
  </div>
  <ul class="govuk-pagination__list">
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 1">
        1
      </a>
    </li>
    <li class="govuk-pagination__item govuk-pagination__item--ellipsis">
      &ctdot;
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 6">
        6
      </a>
    </li>
    <li class="govuk-pagination__item govuk-pagination__item--current">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 7" aria-current="page">
        7
      </a>
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 8">
        8
      </a>
    </li>
    <li class="govuk-pagination__item govuk-pagination__item--ellipsis">
      &ctdot;
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 42">
        42
      </a>
    </li>
  </ul>
  <div class="govuk-pagination__next">
    <a class="govuk-link govuk-pagination__link" href="#" rel="next">
      <span class="govuk-pagination__link-title">
        Next<span class="govuk-visually-hidden"> page</span>
      </span>
      <svg class="govuk-pagination__icon govuk-pagination__icon--next" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m8.107-0.0078125-1.4136 1.414 4.2926 4.293h-12.986v2h12.896l-4.1855 3.9766 1.377 1.4492 6.7441-6.4062-6.7246-6.7266z"></path>
      </svg>
    </a>
  </div>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The items within the pagination component. [ See macro options for items](./components/pagination/#options-pagination-with-numbered-labels-pagination-example--items.md).   |  
| previous  | object  |  A link to the previous page, if there is a previous page. [ See macro options for previous](./components/pagination/#options-pagination-with-numbered-labels-pagination-example--previous.md).   |  
| next  | object  |  A link to the next page, if there is a next page. [ See macro options for next](./components/pagination/#options-pagination-with-numbered-labels-pagination-example--next.md).   |  
| landmarkLabel  | string  |  The label for the navigation landmark that wraps the pagination. Defaults to `"Pagination"`.   |  
| classes  | string  |  The classes you want to add to the pagination `nav` parent.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the pagination `nav` parent.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| number  | string  |  The pagination item text – usually a page number. Required unless the item is an ellipsis.   |  
| visuallyHiddenText  | string  |  The visually hidden label for the pagination item, which will be applied to an `aria-label` and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example “Page 1”.   |  
| href  | string  |  The link’s URL. Required unless the item is an ellipsis.   |  
| current  | boolean  |  Set to `true` to indicate the current page the user is on.   |  
| ellipsis  | boolean  |  Use this option if you want to specify an ellipsis at a given point between numbers. If you set this option as `true`, any other options for the item are ignored.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `previous` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the previous page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The previous page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `next` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the next page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The next page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Copy code
```
{% from "govuk/components/pagination/macro.njk" import govukPagination %}

{{ govukPagination({
  previous: {
    href: "#"
  },
  next: {
    href: "#"
  },
  items: [
    {
      number: 1,
      href: "#"
    },
    {
      ellipsis: true
    },
    {
      number: 6,
      href: "#"
    },
    {
      number: 7,
      current: true,
      href: "#"
    },
    {
      number: 8,
      href: "#"
    },
    {
      ellipsis: true
    },
    {
      number: 42,
      href: "#"
    }
  ]
}) }}
```

Show the page number in the page `<title>` so that screen reader users know they’ve navigated to a different page. For example, ‘Search results (page 1 of 4)’.
Show an appropriate number of pages to fit the horizontal space available.
For smaller screens, show page numbers for:
  * the current page
  * previous and next pages
  * first and last pages

For larger screens, show page numbers for:
  * the current page
  * at least one page immediately before and after the current page
  * first and last pages

Use ellipses (…) to replace any skipped pages. For example:
  * **[1]** 2 … 100
  * 1 **[2]** 3 … 100
  * 1 2 **[3]** 4 … 100
  * 1 2 3 **[4]** 5 … 100
  * 1 … 4 **[5]** 6 … 100
  * 1 … 97 **[98]** 99 100
  * 1 … 98 **[99]** 100
  * 1 … 99 **[100]**

### First and last pages
Do not show the previous page link on the first page – and do not show the next page link on the last page.
[ Open this example in a new tab: first page – pagination ](./components/pagination/first-page.md)
  * [HTML](./components/pagination/#first-page-pagination-example-html.md)
  * [Nunjucks](./components/pagination/#first-page-pagination-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-pagination" aria-label="Pagination">
  <ul class="govuk-pagination__list">
    <li class="govuk-pagination__item govuk-pagination__item--current">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 1" aria-current="page">
        1
      </a>
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 2">
        2
      </a>
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 3">
        3
      </a>
    </li>
  </ul>
  <div class="govuk-pagination__next">
    <a class="govuk-link govuk-pagination__link" href="#" rel="next">
      <span class="govuk-pagination__link-title">
        Next<span class="govuk-visually-hidden"> page</span>
      </span>
      <svg class="govuk-pagination__icon govuk-pagination__icon--next" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m8.107-0.0078125-1.4136 1.414 4.2926 4.293h-12.986v2h12.896l-4.1855 3.9766 1.377 1.4492 6.7441-6.4062-6.7246-6.7266z"></path>
      </svg>
    </a>
  </div>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The items within the pagination component. [ See macro options for items](./components/pagination/#options-first-page-pagination-example--items.md).   |  
| previous  | object  |  A link to the previous page, if there is a previous page. [ See macro options for previous](./components/pagination/#options-first-page-pagination-example--previous.md).   |  
| next  | object  |  A link to the next page, if there is a next page. [ See macro options for next](./components/pagination/#options-first-page-pagination-example--next.md).   |  
| landmarkLabel  | string  |  The label for the navigation landmark that wraps the pagination. Defaults to `"Pagination"`.   |  
| classes  | string  |  The classes you want to add to the pagination `nav` parent.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the pagination `nav` parent.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| number  | string  |  The pagination item text – usually a page number. Required unless the item is an ellipsis.   |  
| visuallyHiddenText  | string  |  The visually hidden label for the pagination item, which will be applied to an `aria-label` and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example “Page 1”.   |  
| href  | string  |  The link’s URL. Required unless the item is an ellipsis.   |  
| current  | boolean  |  Set to `true` to indicate the current page the user is on.   |  
| ellipsis  | boolean  |  Use this option if you want to specify an ellipsis at a given point between numbers. If you set this option as `true`, any other options for the item are ignored.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `previous` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the previous page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The previous page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `next` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the next page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The next page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Copy code
```
{% from "govuk/components/pagination/macro.njk" import govukPagination %}

{{ govukPagination({
  next: {
    href: "#"
  },
  items: [
    {
      number: 1,
      current: true,
      href: "#"
    },
    {
      number: 2,
      href: "#"
    },
    {
      number: 3,
      href: "#"
    }
  ]
}) }}
```

[ Open this example in a new tab: last page – pagination ](./components/pagination/last-page.md)
  * [HTML](./components/pagination/#last-page-pagination-example-html.md)
  * [Nunjucks](./components/pagination/#last-page-pagination-example-nunjucks.md)

HTML
Copy code
```
<nav class="govuk-pagination" aria-label="Pagination">
  <div class="govuk-pagination__prev">
    <a class="govuk-link govuk-pagination__link" href="#" rel="prev">
      <svg class="govuk-pagination__icon govuk-pagination__icon--prev" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
        <path d="m6.5938-0.0078125-6.7266 6.7266 6.7441 6.4062 1.377-1.449-4.1856-3.9768h12.896v-2h-12.984l4.2931-4.293-1.414-1.414z"></path>
      </svg>
      <span class="govuk-pagination__link-title">
        Previous<span class="govuk-visually-hidden"> page</span>
      </span>
    </a>
  </div>
  <ul class="govuk-pagination__list">
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 1">
        1
      </a>
    </li>
    <li class="govuk-pagination__item">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 2">
        2
      </a>
    </li>
    <li class="govuk-pagination__item govuk-pagination__item--current">
      <a class="govuk-link govuk-pagination__link" href="#" aria-label="Page 3" aria-current="page">
        3
      </a>
    </li>
  </ul>
</nav>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  The items within the pagination component. [ See macro options for items](./components/pagination/#options-last-page-pagination-example--items.md).   |  
| previous  | object  |  A link to the previous page, if there is a previous page. [ See macro options for previous](./components/pagination/#options-last-page-pagination-example--previous.md).   |  
| next  | object  |  A link to the next page, if there is a next page. [ See macro options for next](./components/pagination/#options-last-page-pagination-example--next.md).   |  
| landmarkLabel  | string  |  The label for the navigation landmark that wraps the pagination. Defaults to `"Pagination"`.   |  
| classes  | string  |  The classes you want to add to the pagination `nav` parent.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the pagination `nav` parent.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| number  | string  |  The pagination item text – usually a page number. Required unless the item is an ellipsis.   |  
| visuallyHiddenText  | string  |  The visually hidden label for the pagination item, which will be applied to an `aria-label` and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example “Page 1”.   |  
| href  | string  |  The link’s URL. Required unless the item is an ellipsis.   |  
| current  | boolean  |  Set to `true` to indicate the current page the user is on.   |  
| ellipsis  | boolean  |  Use this option if you want to specify an ellipsis at a given point between numbers. If you set this option as `true`, any other options for the item are ignored.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `previous` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the previous page. Defaults to `"Previous page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the previous page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The previous page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Options for `next` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  The text content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  The HTML content of the link to the next page. Defaults to `"Next page"`, with ‘page’ being visually hidden. If `html` is provided, the `text` option will be ignored.   |  
| labelText  | string  |  The optional label that goes underneath the link to the next page, providing further context for the user about where the link goes.   |  
| href  | string  |  **Required.** The next page’s URL.   |  
| attributes  | object  |  The HTML attributes (for example, data attributes) you want to add to the anchor.   |  
Copy code
```
{% from "govuk/components/pagination/macro.njk" import govukPagination %}

{{ govukPagination({
  previous: {
    href: "#"
  },
  items: [
    {
      number: 1,
      href: "#"
    },
    {
      number: 2,
      href: "#"
    },
    {
      number: 3,
      current: true,
      href: "#"
    }
  ]
}) }}
```

### Filtering and sorting
Consider adding filtering or sorting options if it helps users to find what they need in a long list of pages. For example, [the business support finder on GOV.UK](https://www.gov.uk/business-finance-support) has filtering options.
If the user filters or sorts the list of pages, apply this to the whole list (not just the current page) and redirect them back to the first page of the new results.
Set defaults to minimise how many pages most users have to click through to find what they need.
## Research on this component
This component is based on similar ones developed and used successfully by the Government Digital Service, Ministry of Justice and the Home Office, and on feedback in the Design System backlog.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Pagination’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/77) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/pagination/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/pagination/#top.md)
