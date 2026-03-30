#  Links 
  * [ Links without a visited state ](./styles/links/#links-without-a-visited-state.md)
  * [ External links ](./styles/links/#external-links.md)
  * [ Opening links in a new tab ](./styles/links/#opening-links-in-a-new-tab.md)
  * [ Links on dark backgrounds ](./styles/links/#links-on-dark-backgrounds.md)
  * [ Links without underlines ](./styles/links/#links-without-underlines.md)
  * [ Links to change a language ](./styles/links/#links-to-change-a-language.md)

Links are blue and underlined by default. If your link is at the end of a sentence or paragraph, make sure that the linked text does not include the full stop.
[ Open this example in a new tab: links – typography ](./styles/links/default.md)
  * [HTML](./styles/links/#links-typography-example-open-html.md)

HTML
Copy code
```
<p class="govuk-body">
  Jump to <a href="#" class="govuk-link">HTML example</a>.
</p>
```

## Links without a visited state
Use the `govuk-link--no-visited-state` modifier class where it is not helpful to distinguish between visited and unvisited states, for example when linking to pages with frequently-changing content such as the dashboard for an admin interface.
[ Open this example in a new tab: links with no visited state – typography ](./styles/links/no-visited-state.md)
  * [HTML](./styles/links/#links-with-no-visited-state-typography-example-open-html.md)

HTML
Copy code
```
<p class="govuk-body">
  <a href="#" class="govuk-link govuk-link--no-visited-state">link text (with no visited state)</a>
</p>
```

## External links
If it’s an external link to a non-government website, make that clear in the link text. For example, ‘read advice on writing link text from [name of organisation]’. There’s no need to say explicitly that you’re linking to an external site. [Do not use an external link icon](https://designnotes.blog.gov.uk/2016/11/28/removing-the-external-link-icon-from-gov-uk/).
## Opening links in a new tab
Avoid opening links in a new tab or window. It can be disorienting - and [can cause accessibility problems for people who cannot visually perceive that the new tab has opened](https://www.w3.org/TR/WCAG20-TECHS/G200.html).
If you need a link to open in a new tab, include the words ‘opens in new tab’ as part of the link. A use case example is to stop the user losing information they’ve entered into a form. There’s no need to tell the user the new tab opens in a new window as this is the default behaviour for most browsers.
Include `rel="noreferrer noopener"` along with `target="_blank"` to reduce the risk of [reverse tabnabbing](https://owasp.org/www-community/attacks/Reverse_Tabnabbing). The following example shows how to do this in HTML.
[ Open this example in a new tab: links that open in a new tab – typography ](./styles/links/opening-in-new-tab.md)
  * [HTML](./styles/links/#links-that-open-in-a-new-tab-typography-example-open-html.md)

HTML
Copy code
```
<p class="govuk-body">
  <a href="#" class="govuk-link" rel="noreferrer noopener" target="_blank">link text (opens in new tab)</a>
</p>
```

If you’re displaying lots of links together and want to save space and avoid repetition, consider doing both of the following:
  * adding a line of text before the links saying ‘The following links open in a new tab’
  * including `<span class="govuk-visually-hidden">(opens in new tab)</span>` as part of the link text, so that part of the link text is visually hidden but still accessible to screen readers

## Links on dark backgrounds
Use the `govuk-link--inverse` modifier class to show white links on dark backgrounds. For example, in headers, custom components, and patterns with darker backgrounds.
Make sure all users can see the links. The white links and background colour [must have a contrast ratio of at least 4.5:1 to [meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
[ Open this example in a new tab: links on dark backgrounds – typography ](./styles/links/on-dark-background.md)
  * [HTML](./styles/links/#links-on-dark-backgrounds-typography-example-open-html.md)

HTML
Copy code
```
<p class="govuk-body">
  <a href="#" class="govuk-link govuk-link--inverse">link text (on dark background)</a>
</p>
```

## Links without underlines
Use the `govuk-link--no-underline` modifier class to remove underlines from links.
Only do this if the context tells the user that the text is a link, even without the underline.
For example, links in a header or side navigation might not need underlines. Users will understand that they’re links because of where they are on the page.
[ Open this example in a new tab: links without underlines – typography ](./styles/links/no-underline.md)
  * [HTML](./styles/links/#links-without-underlines-typography-example-open-html.md)

HTML
Copy code
```
<p class="govuk-body">
  <a href="#" class="govuk-link govuk-link--no-underline">link text (with no underline)</a>
</p>
```

## Links to change a language
You can use links to allow a user to access the current content in a different language.
When offering links to content in other languages, make sure:
  * the link’s text includes the name of the alternative language in both English and the source language
  * the link’s purpose is always clear, even when taken out of context
  * the link element includes an [`hreflang` attribute](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/hreflang) that identifies the language of the linked page.

For example, your link text could be ‘use [Service name] in [language]’.
## Help improve this style
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Links’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/64) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/styles/links/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./styles/links/#top.md)
