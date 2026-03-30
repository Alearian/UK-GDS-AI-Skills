#  Headings 
  * [ Headings with captions ](./styles/headings/#headings-with-captions.md)

GOV.UK Frontend v6.0.0 and later includes an updated the type scale to increase the size of text on small screens, improving legibility and accessibility.
[See an overview of the changes to the type scale](./get-started/new-type-scale.md).
Use heading tags, such as `<h1>`, `<h2>` and so on, to tag the headings on a page. Apply a heading class, such as `govuk-heading-l`, to style them visually. Style headings consistently to create a clear content structure throughout your service.
For [Question pages in your service](./patterns/question-pages.md), or pages with long headings, follow the usual hierarchy of heading levels and styles associated with them. For example, `govuk-heading-l` for an `<h1>`, followed by `govuk-heading-m` for an `<h2>` and so on. In rare cases, you might want to alter how you use the headings hierarchy to achieve a better visual balance. An example of this is in [the design system’s notification banner](./components/notification-banner/success.md) which uses heading levels in a different order to emphasise the most important information. If you do change the heading hierarchy in a similar way, it needs to go through accessibility testing before use.
Write all headings in sentence case.
[ Open this example in a new tab: headings – default ](./styles/headings/default.md)
  * [HTML](./styles/headings/#headings-default-example-open-html.md)

HTML
Copy code
```
<h1 class="govuk-heading-l">govuk-heading-l</h1>
<h2 class="govuk-heading-m">govuk-heading-m</h2>
<h3 class="govuk-heading-s">govuk-heading-s</h3>
```

If your page has lots of long form content, start with `govuk-heading-xl` for an `<h1>`, `govuk-heading-l` for an `<h2>`, and so on.
[ Open this example in a new tab: headings for pages with long form content – typography ](./styles/headings/headings-xl.md)
  * [HTML](./styles/headings/#headings-for-pages-with-long-form-content-typography-example-open-html.md)

HTML
Copy code
```
<h1 class="govuk-heading-xl">govuk-heading-xl</h1>
<h2 class="govuk-heading-l">govuk-heading-l</h2>
<h3 class="govuk-heading-m">govuk-heading-m</h3>
```

## Headings with captions
Sometimes you may need to make it clear that a page is part of a larger section or group. To do this, you can use a heading with a caption above it.
[ Open this example in a new tab: headings with captions – typography ](./styles/headings/captions.md)
  * [HTML](./styles/headings/#headings-with-captions-typography-example-open-html.md)

HTML
Copy code
```
<span class="govuk-caption-xl">govuk-caption-xl</span>
<h1 class="govuk-heading-xl">govuk-heading-xl</h1>
<span class="govuk-caption-l">govuk-caption-l</span>
<h1 class="govuk-heading-l">govuk-heading-l</h1>
<span class="govuk-caption-m">govuk-caption-m</span>
<h1 class="govuk-heading-m">govuk-heading-m</h1>
```

If the caption should be considered part of the page heading, you can also nest the caption within the `<h1>`.
[ Open this example in a new tab: headings with captions nested – typography ](./styles/headings/captions-inside.md)
  * [HTML](./styles/headings/#headings-with-captions-nested-typography-example-open-html.md)

HTML
Copy code
```
<h1 class="govuk-heading-l">
  <span class="govuk-caption-l">govuk-caption-l</span>
  govuk-heading-l
</h1>
```

## Help improve this style
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Headings’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/64) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/styles/headings/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./styles/headings/#top.md)
