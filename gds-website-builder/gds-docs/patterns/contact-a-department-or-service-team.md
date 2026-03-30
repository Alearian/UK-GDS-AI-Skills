#  Help users to  Contact a department or service team 
Give users contact information within your service.
[ Open this example in a new tab: contact a department or service team ](./patterns/contact-a-department-or-service-team/default.md)
  * [HTML](./patterns/contact-a-department-or-service-team/#contact-a-department-or-service-team-example-html.md)

HTML
Copy code
```
<h2 class="govuk-heading-m">Get help with your application</h2>
<ul class="govuk-list">
  <li>Phone: 020 7946 0101</li>
  <li>Monday to Friday, 9am to 5pm (except public holidays)</li>
</ul>
<p class="govuk-body">
  <a class="govuk-link" href="#">Find out about call charges</a>
</p>
```

## When to use this pattern
Use this pattern whenever you need to help users contact your team or department. Carry out contextual user research to decide exactly where to use this pattern in a page or service.
Read about how and why to [set up user support](https://www.gov.uk/service-manual/helping-people-to-use-your-service/set-up-and-manage-user-support) in the GOV.UK Service Manual.
## How it works
[ Open this example in a new tab: all contact information – contact a department or service team ](./patterns/contact-a-department-or-service-team/all-contact-information.md)
  * [HTML](./patterns/contact-a-department-or-service-team/#all-contact-information-contact-a-department-or-service-team-example-html.md)

HTML
Copy code
```
<h2 class="govuk-heading-m">Get help with your application</h2>
<h3 class="govuk-heading-s">Phone</h3>
<p class="govuk-body">If you have a unique reference number, have it with you when you call.</p>
<ul class="govuk-list">
  <li>Phone: 020 7946 0101</li>
  <li>Textphone: 020 7946 0102</li>
  <li>Monday to Friday, 8am to 6pm</li>
  <li>Saturday and Sunday, 10am to 4pm</li>
  <li class="govuk-!-margin-top-5">Welsh language: 020 7946 0103</li>
  <li>Monday to Friday, 8:30am to 5pm</li>
</ul>
<p class="govuk-body">
  <a class="govuk-link" href="#">Find out about call charges</a>
</p>
<h3 class="govuk-heading-s">Email</h3>
<ul class="govuk-list">
  <li><a class="govuk-link" href="#">name@example.com</a></li>
  <li>We aim to respond within 2 working days</li>
</ul>
<h3 class="govuk-heading-s">Webchat</h3>
<ul class="govuk-list">
  <li><a class="govuk-link" href="#">Speak to an adviser now</a></li>
  <li>Current waiting time is 17 minutes</li>
</ul>
<h3 class="govuk-heading-s">Address</h3>
<p class="govuk-body">
  49 to 53 Cherry Street<br>
  London<br>
  AB1 2DC
</p>
<h3 class="govuk-heading-s">Social media</h3>
<p class="govuk-body">You can use Twitter to get general help. We cannot discuss specific cases or individual applications, so please do not give any personal details.</p>
<p class="govuk-body">
  Twitter: @GOVUK
</p>
```

Order contact channels based on what research shows your users need, and what your service or department can best support.
Show contact channels in the same order throughout your service. This helps users to find what they need more easily.
### Social media
If you have social media channels:
  * list these channels last
  * do not include a link to the social media sites you’re using - read more about this in [GOV.UK’s external linking policy](https://www.gov.uk/guidance/content-design/links#linking-policy)
  * tell users not to share personal information with you

### Write phone numbers in the GOV.UK style
See the [GOV.UK style for writing phone numbers](https://www.gov.uk/guidance/style-guide/a-to-z#telephone-numbers).
### Explain any charges
Tell users if they might have to pay to use any of your contact channels.
For phone call charges, link to the GOV.UK page on [call charges](https://www.gov.uk/call-charges). Include the link after the contact channels list and opening hours.
[ Open this example in a new tab: contact a department or service team second ](./patterns/contact-a-department-or-service-team/default.md)
  * [HTML](./patterns/contact-a-department-or-service-team/#contact-a-department-or-service-team-second-example-html.md)

HTML
Copy code
```
<h2 class="govuk-heading-m">Get help with your application</h2>
<ul class="govuk-list">
  <li>Phone: 020 7946 0101</li>
  <li>Monday to Friday, 9am to 5pm (except public holidays)</li>
</ul>
<p class="govuk-body">
  <a class="govuk-link" href="#">Find out about call charges</a>
</p>
```

### Give opening hours
Follow the GOV.UK style guide format for [time ranges](https://www.gov.uk/guidance/style-guide/a-to-z#times) and [date ranges](https://www.gov.uk/guidance/style-guide/a-to-z#dates).
Explain any exceptions, like bank holidays, or days of the week when your opening hours are different.
For example, ‘Monday to Friday, 9am to midday and 2pm to 4:30pm (closed on bank holidays)’ or ‘24-hour service’.
### Tell users how long they’ll have to wait
Tell users when you’ll respond to them. This helps users choose which contact channel to use.
For example, tell users how long it’ll usually take to:
  * receive a response to their email
  * get to the front of your webchat queue

### Inset contact information
Use the [Inset text component](./components/inset-text.md) to display contact information when you want to differentiate it from the content that surrounds it.
[ Open this example in a new tab: contact information inset text – contact a department or service team ](./patterns/contact-a-department-or-service-team/inset-contact-information.md)
  * [HTML](./patterns/contact-a-department-or-service-team/#contact-information-inset-text-contact-a-department-or-service-team-example-html.md)
  * [Nunjucks](./patterns/contact-a-department-or-service-team/#contact-information-inset-text-contact-a-department-or-service-team-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-inset-text">
  <h2 class="govuk-heading-m">Talk to an advisor</h2>
  <ul class="govuk-list">
    <li>Phone: 020 7946 0101</li>
    <li>Textphone: 020 7946 0102</li>
    <li>Monday to Friday, 9am to 5pm (except public holidays)</li>
  </ul>
  <p class="govuk-body">
    <a class="govuk-link" href="#">Find out about call charges</a>
  </p>
</div>
```

Nunjucks
Copy code
```
{% from "govuk/components/inset-text/macro.njk" import govukInsetText %}

{% set contactInformation %}
  <h2 class="govuk-heading-m">Talk to an advisor</h2>
  <ul class="govuk-list">
    <li>Phone: 020 7946 0101</li>
    <li>Textphone: 020 7946 0102</li>
    <li>Monday to Friday, 9am to 5pm (except public holidays)</li>
  </ul>
  <p class="govuk-body">
    <a class="govuk-link" href="#">Find out about call charges</a>
  </p>
{% endset %}

{{ govukInsetText({
  html: contactInformation
}) }}
```

### Expanding contact information
If contact information is less important than other content on a page, you can enclose contact information inside the [Details component](./components/details.md) to avoid distracting users.
For example, if you need to provide contact information at the bottom of a form page for users who need help completing the form.
Only do this when there’s a lot of contact information to display. When there are only 1 or 2 lines, include the contact information within the body of the page.
[ Open this example in a new tab: contact information details component – contact a department or service team ](./patterns/contact-a-department-or-service-team/expanding-contact-information.md)
  * [HTML](./patterns/contact-a-department-or-service-team/#contact-information-details-component-contact-a-department-or-service-team-example-html.md)
  * [Nunjucks](./patterns/contact-a-department-or-service-team/#contact-information-details-component-contact-a-department-or-service-team-example-nunjucks.md)

HTML
Copy code
```
<details class="govuk-details">
  <summary class="govuk-details__summary">
    <span class="govuk-details__summary-text">
      If you need help completing this form
    </span>
  </summary>
  <div class="govuk-details__text">
    <ul class="govuk-list">
      <li>Phone: 020 7946 0101</li>
      <li>Monday to Friday, 8am to 6pm (except public holidays)</li>
      <li>Saturday and Sunday, 10am to 4pm</li>
    </ul>
    <p class="govuk-body">
      <a class="govuk-link" href="#">Find out about call charges</a>
    </p>
    <ul class="govuk-list">
      <li><a class="govuk-link" href="#">name@example.com</a></li>
      <li>We aim to respond within 2 working days</li>
    </ul>
  </div>
</details>
```

Nunjucks
Copy code
```
{% from "govuk/components/details/macro.njk" import govukDetails %}

{% set contactInformation %}
  <ul class="govuk-list">
    <li>Phone: 020 7946 0101</li>
    <li>Monday to Friday, 8am to 6pm (except public holidays)</li>
    <li>Saturday and Sunday, 10am to 4pm</li>
  </ul>
  <p class="govuk-body">
    <a class="govuk-link" href="#">Find out about call charges</a>
  </p>
  <ul class="govuk-list">
    <li><a class="govuk-link" href="#">name@example.com</a></li>
    <li>We aim to respond within 2 working days</li>
  </ul>
{% endset %}

{{ govukDetails({
  summaryText: "If you need help completing this form",
  html: contactInformation
}) }}
```

## Research on this pattern
This pattern was originally contributed by a team at the Government Digital Service (GDS). The team tested this pattern as part of a government campaign. They ran 2 rounds of research with 12 participants in total.
The examples and guidance here are based on patterns used by the Legal Aid Agency (LAA) and HM Courts & Tribunals Service (HMCTS).
### Next steps
Research is needed to work out:
  * if users who are signed into a service need a different approach
  * how to give contact information to users who need urgent help

## Help improve this pattern
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Contact a department or service team’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/10) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/patterns/contact-a-department-or-service-team/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./patterns/contact-a-department-or-service-team/#top.md)
