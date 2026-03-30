#  Page not found pages 
A page not found tells someone we cannot find the page they were trying to view. They are also known as 404 pages.
[ Open this example in a new tab: page not found pages ](./patterns/page-not-found-pages/default.md)
  * [HTML](./patterns/page-not-found-pages/#page-not-found-pages-example-html.md)
  * [Nunjucks](./patterns/page-not-found-pages/#page-not-found-pages-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <main class="govuk-main-wrapper govuk-main-wrapper--l" id="main-content" role="main">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-l">Page not found</h1>
        <p class="govuk-body">
          If you typed the web address, check it is correct.
        </p>
        <p class="govuk-body">
          If you pasted the web address, check you copied the entire address.
        </p>
        <p class="govuk-body">
          If the web address is correct or you selected a link or button, <a href="#" class="govuk-link">contact the Tax Credits Helpline</a> if you need to speak to someone about your tax credits.
        </p>
      </div>
    </div>
  </main>
</div>
```

Nunjucks
Copy code
```
{% set mainClasses = "govuk-main-wrapper--l" %}

{% block content %}
  <div class="govuk-grid-row">
    <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-l">Page not found</h1>
        <p class="govuk-body">
          If you typed the web address, check it is correct.
        </p>
        <p class="govuk-body">
          If you pasted the web address, check you copied the entire address.
        </p>
        <p class="govuk-body">
          If the web address is correct or you selected a link or button, <a href="#" class="govuk-link">contact the Tax Credits Helpline</a> if you need to speak to someone about your tax credits.
        </p>
    </div>
  </div>
{% endblock %}
```

## When to use this pattern
Use a page not found if someone is trying to view a page that does not exist. This happens if someone:
  * selects a link or button that takes them to a page that does not exist
  * types or copies a web address for a page that does not exist
  * types or copies a web address incorrectly

Test all links and buttons to make sure they work. Remember to [do the hard work to make it simple](https://www.gov.uk/guidance/government-design-principles#do-the-hard-work-to-make-it-simple).
Make sure any web addresses in your service, letters, forms and on GOV.UK are for pages that exist or redirect to pages that exist.
## How it works
The page should have:
  * ‘Page not found – service name – GOV.UK’ as the page title
  * ‘Page not found’ as the H1
  * contact information, if it exists and helps meet a user need

Contact information should either:
  * be a link to a specific page that includes numbers and opening times
  * include all numbers and opening times

The content should be clear and concise, not blame the user.
Do not use:
  * breadcrumbs
  * technical jargon like 404 or bad request
  * informal or humorous words like oops
  * red text to warn people

[ Open this example in a new tab: page not found pages second ](./patterns/page-not-found-pages/default.md)
  * [HTML](./patterns/page-not-found-pages/#page-not-found-pages-second-example-html.md)
  * [Nunjucks](./patterns/page-not-found-pages/#page-not-found-pages-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <main class="govuk-main-wrapper govuk-main-wrapper--l" id="main-content" role="main">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-l">Page not found</h1>
        <p class="govuk-body">
          If you typed the web address, check it is correct.
        </p>
        <p class="govuk-body">
          If you pasted the web address, check you copied the entire address.
        </p>
        <p class="govuk-body">
          If the web address is correct or you selected a link or button, <a href="#" class="govuk-link">contact the Tax Credits Helpline</a> if you need to speak to someone about your tax credits.
        </p>
      </div>
    </div>
  </main>
</div>
```

Nunjucks
Copy code
```
{% set mainClasses = "govuk-main-wrapper--l" %}

{% block content %}
  <div class="govuk-grid-row">
    <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-l">Page not found</h1>
        <p class="govuk-body">
          If you typed the web address, check it is correct.
        </p>
        <p class="govuk-body">
          If you pasted the web address, check you copied the entire address.
        </p>
        <p class="govuk-body">
          If the web address is correct or you selected a link or button, <a href="#" class="govuk-link">contact the Tax Credits Helpline</a> if you need to speak to someone about your tax credits.
        </p>
    </div>
  </div>
{% endblock %}
```

## Research on this pattern
More research is needed to find out if people:
  * can fix the problem on their own
  * understand what has happened
  * understand the content and if there is anything missing

## Help improve this pattern
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Page not found pages’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/130) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/patterns/page-not-found-pages/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./patterns/page-not-found-pages/#top.md)
