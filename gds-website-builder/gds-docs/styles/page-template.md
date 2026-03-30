#  Page template 
  * [ Default ](./styles/page-template/#default.md)
  * [ Customised page template ](./styles/page-template/#customised-page-template.md)
  * [ Changing template content ](./styles/page-template/#changing-template-content.md)
  * [ Template blocks and options ](./styles/page-template/#template-blocks-and-options.md)

Use this template to keep your pages consistent with the rest of GOV.UK.
This page template combines the boilerplate markup and [components](./components.md) needed for a basic GOV.UK page. It includes:
  * JavaScript that adds a `.govuk-frontend-supported` class, which is required by components with JavaScript behaviour
  * the [Skip link component](./components/skip-link.md), [Header component](./components/header.md) and [Footer component](./components/footer.md)
  * the favicon, and other related theme icons

In the examples provided, we show both HTML and [Nunjucks](https://frontend.design-system.service.gov.uk/use-nunjucks/).
You can use the HTML examples if you are not able to use Nunjucks. If you use HTML you’ll need to update it manually when new versions are released.
If you’re using Nunjucks you can get this page template by installing GOV.UK Frontend.  
You’ll get updates to the page template when we update GOV.UK Frontend.
## Default
This example shows the minimum required for a GOV.UK page.
[ Open this example in a new tab: default – page template ](./styles/page-template/default.md)
  * [HTML](./styles/page-template/#default-page-template-example-html.md)
  * [Nunjucks](./styles/page-template/#default-page-template-example-nunjucks.md)

HTML
Copy code
```
<!DOCTYPE html>
<html lang="en" class="govuk-template">

<head>
  <meta charset="utf-8">
  <title>GOV.UK - The best place to find government services and information</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#1d70b8">
  <link rel="stylesheet" href="/stylesheets/govuk-frontend.min.css">
  <link rel="icon" sizes="48x48" href="/assets/images/favicon.ico">
  <link rel="icon" sizes="any" href="/assets/images/favicon.svg" type="image/svg+xml">
  <link rel="mask-icon" href="/assets/images/govuk-icon-mask.svg" color="#1d70b8">
  <link rel="apple-touch-icon" href="/assets/images/govuk-icon-180.png">
  <link rel="manifest" href="/assets/manifest.json">
</head>

<body class="govuk-template__body">
  <script>
    document.body.className += ' js-enabled' + ('noModule' in HTMLScriptElement.prototype ? ' govuk-frontend-supported' : '');
  </script>
  <a href="#main-content" class="govuk-skip-link" data-module="govuk-skip-link">Skip to main content</a>
  <header class="govuk-template__header">
    <div class="govuk-header">
      <div class="govuk-header__container govuk-width-container">
        <div class="govuk-header__logo">
          <a href="//gov.uk" class="govuk-header__homepage-link">
            <svg
              focusable="false"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 324 60"
              height="30"
              width="162"
              fill="currentcolor" class="govuk-header__logotype" aria-label="GOV.UK">
              <title>GOV.UK</title>
              <g>
                <circle cx="20" cy="17.6" r="3.7" />
                <circle cx="10.2" cy="23.5" r="3.7" />
                <circle cx="3.7" cy="33.2" r="3.7" />
                <circle cx="31.7" cy="30.6" r="3.7" />
                <circle cx="43.3" cy="17.6" r="3.7" />
                <circle cx="53.2" cy="23.5" r="3.7" />
                <circle cx="59.7" cy="33.2" r="3.7" />
                <circle cx="31.7" cy="30.6" r="3.7" />
                <path d="M33.1,9.8c.2-.1.3-.3.5-.5l4.6,2.4v-6.8l-4.6,1.5c-.1-.2-.3-.3-.5-.5l1.9-5.9h-6.7l1.9,5.9c-.2.1-.3.3-.5.5l-4.6-1.5v6.8l4.6-2.4c.1.2.3.3.5.5l-2.6,8c-.9,2.8,1.2,5.7,4.1,5.7h0c3,0,5.1-2.9,4.1-5.7l-2.6-8ZM37,37.9s-3.4,3.8-4.1,6.1c2.2,0,4.2-.5,6.4-2.8l-.7,8.5c-2-2.8-4.4-4.1-5.7-3.8.1,3.1.5,6.7,5.8,7.2,3.7.3,6.7-1.5,7-3.8.4-2.6-2-4.3-3.7-1.6-1.4-4.5,2.4-6.1,4.9-3.2-1.9-4.5-1.8-7.7,2.4-10.9,3,4,2.6,7.3-1.2,11.1,2.4-1.3,6.2,0,4,4.6-1.2-2.8-3.7-2.2-4.2.2-.3,1.7.7,3.7,3,4.2,1.9.3,4.7-.9,7-5.9-1.3,0-2.4.7-3.9,1.7l2.4-8c.6,2.3,1.4,3.7,2.2,4.5.6-1.6.5-2.8,0-5.3l5,1.8c-2.6,3.6-5.2,8.7-7.3,17.5-7.4-1.1-15.7-1.7-24.5-1.7h0c-8.8,0-17.1.6-24.5,1.7-2.1-8.9-4.7-13.9-7.3-17.5l5-1.8c-.5,2.5-.6,3.7,0,5.3.8-.8,1.6-2.3,2.2-4.5l2.4,8c-1.5-1-2.6-1.7-3.9-1.7,2.3,5,5.2,6.2,7,5.9,2.3-.4,3.3-2.4,3-4.2-.5-2.4-3-3.1-4.2-.2-2.2-4.6,1.6-6,4-4.6-3.7-3.7-4.2-7.1-1.2-11.1,4.2,3.2,4.3,6.4,2.4,10.9,2.5-2.8,6.3-1.3,4.9,3.2-1.8-2.7-4.1-1-3.7,1.6.3,2.3,3.3,4.1,7,3.8,5.4-.5,5.7-4.2,5.8-7.2-1.3-.2-3.7,1-5.7,3.8l-.7-8.5c2.2,2.3,4.2,2.7,6.4,2.8-.7-2.3-4.1-6.1-4.1-6.1h10.6,0Z" />
              </g>
              <circle class="govuk-logo-dot" cx="226" cy="36" r="7.3" />
              <path d="M93.94 41.25c.4 1.81 1.2 3.21 2.21 4.62 1 1.4 2.21 2.41 3.61 3.21s3.21 1.2 5.22 1.2 3.61-.4 4.82-1c1.4-.6 2.41-1.4 3.21-2.41.8-1 1.4-2.01 1.61-3.01s.4-2.01.4-3.01v.14h-10.86v-7.02h20.07v24.08h-8.03v-5.56c-.6.8-1.38 1.61-2.19 2.41-.8.8-1.81 1.2-2.81 1.81-1 .4-2.21.8-3.41 1.2s-2.41.4-3.81.4a18.56 18.56 0 0 1-14.65-6.63c-1.6-2.01-3.01-4.41-3.81-7.02s-1.4-5.62-1.4-8.83.4-6.02 1.4-8.83a20.45 20.45 0 0 1 19.46-13.65c3.21 0 4.01.2 5.82.8 1.81.4 3.61 1.2 5.02 2.01 1.61.8 2.81 2.01 4.01 3.21s2.21 2.61 2.81 4.21l-7.63 4.41c-.4-1-1-1.81-1.61-2.61-.6-.8-1.4-1.4-2.21-2.01-.8-.6-1.81-1-2.81-1.4-1-.4-2.21-.4-3.61-.4-2.01 0-3.81.4-5.22 1.2-1.4.8-2.61 1.81-3.61 3.21s-1.61 2.81-2.21 4.62c-.4 1.81-.6 3.71-.6 5.42s.8 5.22.8 5.22Zm57.8-27.9c3.21 0 6.22.6 8.63 1.81 2.41 1.2 4.82 2.81 6.62 4.82S170.2 24.39 171 27s1.4 5.62 1.4 8.83-.4 6.02-1.4 8.83-2.41 5.02-4.01 7.02-4.01 3.61-6.62 4.82-5.42 1.81-8.63 1.81-6.22-.6-8.63-1.81-4.82-2.81-6.42-4.82-3.21-4.41-4.01-7.02-1.4-5.62-1.4-8.83.4-6.02 1.4-8.83 2.41-5.02 4.01-7.02 4.01-3.61 6.42-4.82 5.42-1.81 8.63-1.81Zm0 36.73c1.81 0 3.61-.4 5.02-1s2.61-1.81 3.61-3.01 1.81-2.81 2.21-4.41c.4-1.81.8-3.61.8-5.62 0-2.21-.2-4.21-.8-6.02s-1.2-3.21-2.21-4.62c-1-1.2-2.21-2.21-3.61-3.01s-3.21-1-5.02-1-3.61.4-5.02 1c-1.4.8-2.61 1.81-3.61 3.01s-1.81 2.81-2.21 4.62c-.4 1.81-.8 3.61-.8 5.62 0 2.41.2 4.21.8 6.02.4 1.81 1.2 3.21 2.21 4.41s2.21 2.21 3.61 3.01c1.4.8 3.21 1 5.02 1Zm36.32 7.96-12.24-44.15h9.83l8.43 32.77h.4l8.23-32.77h9.83L200.3 58.04h-12.24Zm74.14-7.96c2.18 0 3.51-.6 3.51-.6 1.2-.6 2.01-1 2.81-1.81s1.4-1.81 1.81-2.81a13 13 0 0 0 .8-4.01V13.9h8.63v28.15c0 2.41-.4 4.62-1.4 6.62-.8 2.01-2.21 3.61-3.61 5.02s-3.41 2.41-5.62 3.21-4.62 1.2-7.02 1.2-5.02-.4-7.02-1.2c-2.21-.8-4.01-1.81-5.62-3.21s-2.81-3.01-3.61-5.02-1.4-4.21-1.4-6.62V13.9h8.63v26.95c0 1.61.2 3.01.8 4.01.4 1.2 1.2 2.21 2.01 2.81.8.8 1.81 1.4 2.81 1.81 0 0 1.34.6 3.51.6Zm34.22-36.18v18.92l15.65-18.92h10.82l-15.03 17.32 16.03 26.83h-10.21l-11.44-20.21-5.62 6.22v13.99h-8.83V13.9" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </header>
  <div class="govuk-width-container">
    <main class="govuk-main-wrapper" id="main-content">
      <h1 class="govuk-heading-xl">Default page template</h1>
    </main>
  </div>
  <footer class="govuk-template__footer">
    <div class="govuk-footer">
      <div class="govuk-width-container">
        <svg
          focusable="false"
          role="presentation"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 64 60"
          height="30"
          width="32"
          fill="currentcolor" class="govuk-footer__crown">
          <g>
            <circle cx="20" cy="17.6" r="3.7" />
            <circle cx="10.2" cy="23.5" r="3.7" />
            <circle cx="3.7" cy="33.2" r="3.7" />
            <circle cx="31.7" cy="30.6" r="3.7" />
            <circle cx="43.3" cy="17.6" r="3.7" />
            <circle cx="53.2" cy="23.5" r="3.7" />
            <circle cx="59.7" cy="33.2" r="3.7" />
            <circle cx="31.7" cy="30.6" r="3.7" />
            <path d="M33.1,9.8c.2-.1.3-.3.5-.5l4.6,2.4v-6.8l-4.6,1.5c-.1-.2-.3-.3-.5-.5l1.9-5.9h-6.7l1.9,5.9c-.2.1-.3.3-.5.5l-4.6-1.5v6.8l4.6-2.4c.1.2.3.3.5.5l-2.6,8c-.9,2.8,1.2,5.7,4.1,5.7h0c3,0,5.1-2.9,4.1-5.7l-2.6-8ZM37,37.9s-3.4,3.8-4.1,6.1c2.2,0,4.2-.5,6.4-2.8l-.7,8.5c-2-2.8-4.4-4.1-5.7-3.8.1,3.1.5,6.7,5.8,7.2,3.7.3,6.7-1.5,7-3.8.4-2.6-2-4.3-3.7-1.6-1.4-4.5,2.4-6.1,4.9-3.2-1.9-4.5-1.8-7.7,2.4-10.9,3,4,2.6,7.3-1.2,11.1,2.4-1.3,6.2,0,4,4.6-1.2-2.8-3.7-2.2-4.2.2-.3,1.7.7,3.7,3,4.2,1.9.3,4.7-.9,7-5.9-1.3,0-2.4.7-3.9,1.7l2.4-8c.6,2.3,1.4,3.7,2.2,4.5.6-1.6.5-2.8,0-5.3l5,1.8c-2.6,3.6-5.2,8.7-7.3,17.5-7.4-1.1-15.7-1.7-24.5-1.7h0c-8.8,0-17.1.6-24.5,1.7-2.1-8.9-4.7-13.9-7.3-17.5l5-1.8c-.5,2.5-.6,3.7,0,5.3.8-.8,1.6-2.3,2.2-4.5l2.4,8c-1.5-1-2.6-1.7-3.9-1.7,2.3,5,5.2,6.2,7,5.9,2.3-.4,3.3-2.4,3-4.2-.5-2.4-3-3.1-4.2-.2-2.2-4.6,1.6-6,4-4.6-3.7-3.7-4.2-7.1-1.2-11.1,4.2,3.2,4.3,6.4,2.4,10.9,2.5-2.8,6.3-1.3,4.9,3.2-1.8-2.7-4.1-1-3.7,1.6.3,2.3,3.3,4.1,7,3.8,5.4-.5,5.7-4.2,5.8-7.2-1.3-.2-3.7,1-5.7,3.8l-.7-8.5c2.2,2.3,4.2,2.7,6.4,2.8-.7-2.3-4.1-6.1-4.1-6.1h10.6,0Z" />
          </g>
        </svg>
        <div class="govuk-footer__meta">
          <div class="govuk-footer__meta-item govuk-footer__meta-item--grow">
            <svg
              aria-hidden="true"
              focusable="false"
              class="govuk-footer__licence-logo"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 483.2 195.7"
              height="17"
              width="41">
              <path
                fill="currentColor"
                d="M421.5 142.8V.1l-50.7 32.3v161.1h112.4v-50.7zm-122.3-9.6A47.12 47.12 0 0 1 221 97.8c0-26 21.1-47.1 47.1-47.1 16.7 0 31.4 8.7 39.7 21.8l42.7-27.2A97.63 97.63 0 0 0 268.1 0c-36.5 0-68.3 20.1-85.1 49.7A98 98 0 0 0 97.8 0C43.9 0 0 43.9 0 97.8s43.9 97.8 97.8 97.8c36.5 0 68.3-20.1 85.1-49.7a97.76 97.76 0 0 0 149.6 25.4l19.4 22.2h3v-87.8h-80l24.3 27.5zM97.8 145c-26 0-47.1-21.1-47.1-47.1s21.1-47.1 47.1-47.1 47.2 21 47.2 47S123.8 145 97.8 145" />
            </svg>
            <span class="govuk-footer__licence-description">
              All content is available under the
              <a
                class="govuk-footer__link"
                href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
                rel="license">Open Government Licence v3.0</a>, except where otherwise stated
            </span>
          </div>
          <div class="govuk-footer__meta-item">
            <a
              class="govuk-footer__link govuk-footer__copyright-logo"
              href="https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/">
              © Crown copyright
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
  <script type="module" src="/javascripts/govuk-frontend.min.js"></script>
  <script type="module">
    import {
      initAll
    } from '/javascripts/govuk-frontend.min.js'
    initAll()
  </script>
</body>

</html>
```

Nunjucks
Copy code
```
{% block head %}
  <link rel="stylesheet" href="/stylesheets/govuk-frontend.min.css">
{% endblock %}

{% block content %}
  <h1 class="govuk-heading-xl">Default page template</h1>
{% endblock %}

{% block bodyEnd %}
  {# Run JavaScript at end of the <body>, to avoid blocking the initial render. #}
  <script type="module" src="/javascripts/govuk-frontend.min.js"></script>
  <script type="module">
    import { initAll } from '/javascripts/govuk-frontend.min.js'
    initAll()
  </script>
{% endblock %}
```

## Customised page template
You can customise the page template, for example, by:
  * adding a service name and navigation
  * including a [Back link component](./components/back-link.md) or [Phase banner component](./components/phase-banner.md)

[ Open this example in a new tab: customised – page template ](./styles/page-template/custom.md)
  * [HTML](./styles/page-template/#customised-page-template-example-html.md)
  * [Nunjucks](./styles/page-template/#customised-page-template-example-nunjucks.md)

HTML
Copy code
```
<!DOCTYPE html>
<html lang="en" class="govuk-template app-html-class">

<head>
  <meta charset="utf-8">
  <title>GOV.UK - Customised page template</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="blue">
  <link rel="stylesheet" href="/stylesheets/govuk-frontend.min.css">
  <link rel="icon" sizes="48x48" href="/assets/images/favicon.ico">
  <link rel="icon" sizes="any" href="/assets/images/favicon.svg" type="image/svg+xml">
  <link rel="mask-icon" href="/assets/images/govuk-icon-mask.svg" color="blue">
  <link rel="apple-touch-icon" href="/assets/images/govuk-icon-180.png">
  <link rel="manifest" href="/assets/manifest.json">
  <meta property="og:image" content="YOUR-DOMAIN/images/govuk-opengraph-image.png">
</head>

<body class="govuk-template__body app-body-class" data-test="My value" data-other="report:details">
  <script>
    document.body.className += ' js-enabled' + ('noModule' in HTMLScriptElement.prototype ? ' govuk-frontend-supported' : '');
  </script>
  <form action="/form-handler" method="post" novalidate>
    <div class="govuk-cookie-banner" data-nosnippet role="region" aria-label="Cookies on [name of service]">
      <div class="govuk-cookie-banner__message govuk-width-container">
        <div class="govuk-grid-row">
          <div class="govuk-grid-column-two-thirds">
            <h2 class="govuk-cookie-banner__heading govuk-heading-m">
              Cookies on [name of service]
            </h2>
            <div class="govuk-cookie-banner__content">
              <p class="govuk-body">We use some essential cookies to make this service work.</p>
              <p class="govuk-body">We’d also like to use analytics cookies so we can understand how you use the service and make improvements.</p>
            </div>
          </div>
        </div>
        <div class="govuk-button-group">
          <button type="submit" value="yes" name="cookies[analytics]" class="govuk-button" data-module="govuk-button">
            Accept analytics cookies
          </button>
          <button type="submit" value="no" name="cookies[analytics]" class="govuk-button" data-module="govuk-button">
            Reject analytics cookies
          </button>
          <a class="govuk-link" href="#">View cookies</a>
        </div>
      </div>
    </div>
  </form>
  <a href="#main-content" class="govuk-skip-link" data-module="govuk-skip-link">Skip to main content</a>
  <header class="govuk-template__header">
    <div class="govuk-header">
      <div class="govuk-header__container govuk-width-container">
        <div class="govuk-header__logo">
          <a href="//gov.uk" class="govuk-header__homepage-link">
            <svg
              focusable="false"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 324 60"
              height="30"
              width="162"
              fill="currentcolor" class="govuk-header__logotype" aria-label="GOV.UK">
              <title>GOV.UK</title>
              <g>
                <circle cx="20" cy="17.6" r="3.7" />
                <circle cx="10.2" cy="23.5" r="3.7" />
                <circle cx="3.7" cy="33.2" r="3.7" />
                <circle cx="31.7" cy="30.6" r="3.7" />
                <circle cx="43.3" cy="17.6" r="3.7" />
                <circle cx="53.2" cy="23.5" r="3.7" />
                <circle cx="59.7" cy="33.2" r="3.7" />
                <circle cx="31.7" cy="30.6" r="3.7" />
                <path d="M33.1,9.8c.2-.1.3-.3.5-.5l4.6,2.4v-6.8l-4.6,1.5c-.1-.2-.3-.3-.5-.5l1.9-5.9h-6.7l1.9,5.9c-.2.1-.3.3-.5.5l-4.6-1.5v6.8l4.6-2.4c.1.2.3.3.5.5l-2.6,8c-.9,2.8,1.2,5.7,4.1,5.7h0c3,0,5.1-2.9,4.1-5.7l-2.6-8ZM37,37.9s-3.4,3.8-4.1,6.1c2.2,0,4.2-.5,6.4-2.8l-.7,8.5c-2-2.8-4.4-4.1-5.7-3.8.1,3.1.5,6.7,5.8,7.2,3.7.3,6.7-1.5,7-3.8.4-2.6-2-4.3-3.7-1.6-1.4-4.5,2.4-6.1,4.9-3.2-1.9-4.5-1.8-7.7,2.4-10.9,3,4,2.6,7.3-1.2,11.1,2.4-1.3,6.2,0,4,4.6-1.2-2.8-3.7-2.2-4.2.2-.3,1.7.7,3.7,3,4.2,1.9.3,4.7-.9,7-5.9-1.3,0-2.4.7-3.9,1.7l2.4-8c.6,2.3,1.4,3.7,2.2,4.5.6-1.6.5-2.8,0-5.3l5,1.8c-2.6,3.6-5.2,8.7-7.3,17.5-7.4-1.1-15.7-1.7-24.5-1.7h0c-8.8,0-17.1.6-24.5,1.7-2.1-8.9-4.7-13.9-7.3-17.5l5-1.8c-.5,2.5-.6,3.7,0,5.3.8-.8,1.6-2.3,2.2-4.5l2.4,8c-1.5-1-2.6-1.7-3.9-1.7,2.3,5,5.2,6.2,7,5.9,2.3-.4,3.3-2.4,3-4.2-.5-2.4-3-3.1-4.2-.2-2.2-4.6,1.6-6,4-4.6-3.7-3.7-4.2-7.1-1.2-11.1,4.2,3.2,4.3,6.4,2.4,10.9,2.5-2.8,6.3-1.3,4.9,3.2-1.8-2.7-4.1-1-3.7,1.6.3,2.3,3.3,4.1,7,3.8,5.4-.5,5.7-4.2,5.8-7.2-1.3-.2-3.7,1-5.7,3.8l-.7-8.5c2.2,2.3,4.2,2.7,6.4,2.8-.7-2.3-4.1-6.1-4.1-6.1h10.6,0Z" />
              </g>
              <circle class="govuk-logo-dot" cx="226" cy="36" r="7.3" />
              <path d="M93.94 41.25c.4 1.81 1.2 3.21 2.21 4.62 1 1.4 2.21 2.41 3.61 3.21s3.21 1.2 5.22 1.2 3.61-.4 4.82-1c1.4-.6 2.41-1.4 3.21-2.41.8-1 1.4-2.01 1.61-3.01s.4-2.01.4-3.01v.14h-10.86v-7.02h20.07v24.08h-8.03v-5.56c-.6.8-1.38 1.61-2.19 2.41-.8.8-1.81 1.2-2.81 1.81-1 .4-2.21.8-3.41 1.2s-2.41.4-3.81.4a18.56 18.56 0 0 1-14.65-6.63c-1.6-2.01-3.01-4.41-3.81-7.02s-1.4-5.62-1.4-8.83.4-6.02 1.4-8.83a20.45 20.45 0 0 1 19.46-13.65c3.21 0 4.01.2 5.82.8 1.81.4 3.61 1.2 5.02 2.01 1.61.8 2.81 2.01 4.01 3.21s2.21 2.61 2.81 4.21l-7.63 4.41c-.4-1-1-1.81-1.61-2.61-.6-.8-1.4-1.4-2.21-2.01-.8-.6-1.81-1-2.81-1.4-1-.4-2.21-.4-3.61-.4-2.01 0-3.81.4-5.22 1.2-1.4.8-2.61 1.81-3.61 3.21s-1.61 2.81-2.21 4.62c-.4 1.81-.6 3.71-.6 5.42s.8 5.22.8 5.22Zm57.8-27.9c3.21 0 6.22.6 8.63 1.81 2.41 1.2 4.82 2.81 6.62 4.82S170.2 24.39 171 27s1.4 5.62 1.4 8.83-.4 6.02-1.4 8.83-2.41 5.02-4.01 7.02-4.01 3.61-6.62 4.82-5.42 1.81-8.63 1.81-6.22-.6-8.63-1.81-4.82-2.81-6.42-4.82-3.21-4.41-4.01-7.02-1.4-5.62-1.4-8.83.4-6.02 1.4-8.83 2.41-5.02 4.01-7.02 4.01-3.61 6.42-4.82 5.42-1.81 8.63-1.81Zm0 36.73c1.81 0 3.61-.4 5.02-1s2.61-1.81 3.61-3.01 1.81-2.81 2.21-4.41c.4-1.81.8-3.61.8-5.62 0-2.21-.2-4.21-.8-6.02s-1.2-3.21-2.21-4.62c-1-1.2-2.21-2.21-3.61-3.01s-3.21-1-5.02-1-3.61.4-5.02 1c-1.4.8-2.61 1.81-3.61 3.01s-1.81 2.81-2.21 4.62c-.4 1.81-.8 3.61-.8 5.62 0 2.41.2 4.21.8 6.02.4 1.81 1.2 3.21 2.21 4.41s2.21 2.21 3.61 3.01c1.4.8 3.21 1 5.02 1Zm36.32 7.96-12.24-44.15h9.83l8.43 32.77h.4l8.23-32.77h9.83L200.3 58.04h-12.24Zm74.14-7.96c2.18 0 3.51-.6 3.51-.6 1.2-.6 2.01-1 2.81-1.81s1.4-1.81 1.81-2.81a13 13 0 0 0 .8-4.01V13.9h8.63v28.15c0 2.41-.4 4.62-1.4 6.62-.8 2.01-2.21 3.61-3.61 5.02s-3.41 2.41-5.62 3.21-4.62 1.2-7.02 1.2-5.02-.4-7.02-1.2c-2.21-.8-4.01-1.81-5.62-3.21s-2.81-3.01-3.61-5.02-1.4-4.21-1.4-6.62V13.9h8.63v26.95c0 1.61.2 3.01.8 4.01.4 1.2 1.2 2.21 2.01 2.81.8.8 1.81 1.4 2.81 1.81 0 0 1.34.6 3.51.6Zm34.22-36.18v18.92l15.65-18.92h10.82l-15.03 17.32 16.03 26.83h-10.21l-11.44-20.21-5.62 6.22v13.99h-8.83V13.9" />
            </svg>
          </a>
        </div>
      </div>
    </div>
    <section aria-label="Service information" class="govuk-service-navigation"
      data-module="govuk-service-navigation">
      <div class="govuk-width-container">
        <div class="govuk-service-navigation__container">
          <span class="govuk-service-navigation__service-name">
            <a href="#" class="govuk-service-navigation__link">
              Service name
            </a>
          </span>
          <nav aria-label="Menu" class="govuk-service-navigation__wrapper">
            <button type="button" class="govuk-service-navigation__toggle govuk-js-service-navigation-toggle" aria-controls="navigation" hidden aria-hidden="true">
              Menu
            </button>
            <ul class="govuk-service-navigation__list" id="navigation">
              <li class="govuk-service-navigation__item govuk-service-navigation__item--active">
                <a class="govuk-service-navigation__link" href="#" aria-current="true">
                  <strong class="govuk-service-navigation__active-fallback">Navigation item 1</strong>
                </a>
              </li>
              <li class="govuk-service-navigation__item">
                <a class="govuk-service-navigation__link" href="#">
                  Navigation item 2
                </a>
              </li>
              <li class="govuk-service-navigation__item">
                <a class="govuk-service-navigation__link" href="#">
                  Navigation item 3
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </section>
    <div class="govuk-phase-banner govuk-width-container">
      <p class="govuk-phase-banner__content">
        <strong class="govuk-tag govuk-phase-banner__content__tag">
          Alpha
        </strong>
        <span class="govuk-phase-banner__text">
          This is a new service – your <a class="govuk-link" href="#">feedback</a> will help us to improve it.
        </span>
      </p>
    </div>
  </header>
  <div class="govuk-width-container app-width-container">
    <a href="#" class="govuk-back-link">Back</a>
    <main class="govuk-main-wrapper app-main-class" id="main-content">
      <h1 class="govuk-heading-xl">Customised page template</h1>
    </main>
  </div>
  <footer class="govuk-template__footer">
    <div class="govuk-footer">
      <div class="govuk-width-container">
        <svg
          focusable="false"
          role="presentation"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 64 60"
          height="30"
          width="32"
          fill="currentcolor" class="govuk-footer__crown">
          <g>
            <circle cx="20" cy="17.6" r="3.7" />
            <circle cx="10.2" cy="23.5" r="3.7" />
            <circle cx="3.7" cy="33.2" r="3.7" />
            <circle cx="31.7" cy="30.6" r="3.7" />
            <circle cx="43.3" cy="17.6" r="3.7" />
            <circle cx="53.2" cy="23.5" r="3.7" />
            <circle cx="59.7" cy="33.2" r="3.7" />
            <circle cx="31.7" cy="30.6" r="3.7" />
            <path d="M33.1,9.8c.2-.1.3-.3.5-.5l4.6,2.4v-6.8l-4.6,1.5c-.1-.2-.3-.3-.5-.5l1.9-5.9h-6.7l1.9,5.9c-.2.1-.3.3-.5.5l-4.6-1.5v6.8l4.6-2.4c.1.2.3.3.5.5l-2.6,8c-.9,2.8,1.2,5.7,4.1,5.7h0c3,0,5.1-2.9,4.1-5.7l-2.6-8ZM37,37.9s-3.4,3.8-4.1,6.1c2.2,0,4.2-.5,6.4-2.8l-.7,8.5c-2-2.8-4.4-4.1-5.7-3.8.1,3.1.5,6.7,5.8,7.2,3.7.3,6.7-1.5,7-3.8.4-2.6-2-4.3-3.7-1.6-1.4-4.5,2.4-6.1,4.9-3.2-1.9-4.5-1.8-7.7,2.4-10.9,3,4,2.6,7.3-1.2,11.1,2.4-1.3,6.2,0,4,4.6-1.2-2.8-3.7-2.2-4.2.2-.3,1.7.7,3.7,3,4.2,1.9.3,4.7-.9,7-5.9-1.3,0-2.4.7-3.9,1.7l2.4-8c.6,2.3,1.4,3.7,2.2,4.5.6-1.6.5-2.8,0-5.3l5,1.8c-2.6,3.6-5.2,8.7-7.3,17.5-7.4-1.1-15.7-1.7-24.5-1.7h0c-8.8,0-17.1.6-24.5,1.7-2.1-8.9-4.7-13.9-7.3-17.5l5-1.8c-.5,2.5-.6,3.7,0,5.3.8-.8,1.6-2.3,2.2-4.5l2.4,8c-1.5-1-2.6-1.7-3.9-1.7,2.3,5,5.2,6.2,7,5.9,2.3-.4,3.3-2.4,3-4.2-.5-2.4-3-3.1-4.2-.2-2.2-4.6,1.6-6,4-4.6-3.7-3.7-4.2-7.1-1.2-11.1,4.2,3.2,4.3,6.4,2.4,10.9,2.5-2.8,6.3-1.3,4.9,3.2-1.8-2.7-4.1-1-3.7,1.6.3,2.3,3.3,4.1,7,3.8,5.4-.5,5.7-4.2,5.8-7.2-1.3-.2-3.7,1-5.7,3.8l-.7-8.5c2.2,2.3,4.2,2.7,6.4,2.8-.7-2.3-4.1-6.1-4.1-6.1h10.6,0Z" />
          </g>
        </svg>
        <div class="govuk-footer__meta">
          <div class="govuk-footer__meta-item govuk-footer__meta-item--grow">
            <h2 class="govuk-visually-hidden">Support links</h2>
            <ul class="govuk-footer__inline-list">
              <li class="govuk-footer__inline-list-item">
                <a class="govuk-footer__link" href="#">
                  Help
                </a>
              </li>
              <li class="govuk-footer__inline-list-item">
                <a class="govuk-footer__link" href="#">
                  Cookies
                </a>
              </li>
              <li class="govuk-footer__inline-list-item">
                <a class="govuk-footer__link" href="#">
                  Contact
                </a>
              </li>
              <li class="govuk-footer__inline-list-item">
                <a class="govuk-footer__link" href="#">
                  Terms and conditions
                </a>
              </li>
            </ul>
            <svg
              aria-hidden="true"
              focusable="false"
              class="govuk-footer__licence-logo"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 483.2 195.7"
              height="17"
              width="41">
              <path
                fill="currentColor"
                d="M421.5 142.8V.1l-50.7 32.3v161.1h112.4v-50.7zm-122.3-9.6A47.12 47.12 0 0 1 221 97.8c0-26 21.1-47.1 47.1-47.1 16.7 0 31.4 8.7 39.7 21.8l42.7-27.2A97.63 97.63 0 0 0 268.1 0c-36.5 0-68.3 20.1-85.1 49.7A98 98 0 0 0 97.8 0C43.9 0 0 43.9 0 97.8s43.9 97.8 97.8 97.8c36.5 0 68.3-20.1 85.1-49.7a97.76 97.76 0 0 0 149.6 25.4l19.4 22.2h3v-87.8h-80l24.3 27.5zM97.8 145c-26 0-47.1-21.1-47.1-47.1s21.1-47.1 47.1-47.1 47.2 21 47.2 47S123.8 145 97.8 145" />
            </svg>
            <span class="govuk-footer__licence-description">
              All content is available under the
              <a
                class="govuk-footer__link"
                href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
                rel="license">Open Government Licence v3.0</a>, except where otherwise stated
            </span>
          </div>
          <div class="govuk-footer__meta-item">
            <a
              class="govuk-footer__link govuk-footer__copyright-logo"
              href="https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/">
              © Crown copyright
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
  <script type="module" src="/javascripts/govuk-frontend.min.js"></script>
  <script type="module">
    import {
      initAll
    } from '/javascripts/govuk-frontend.min.js'
    initAll()
  </script>
</body>

</html>
```

Nunjucks
Copy code
```
{# Example that changes every setting in the template #}

{% from "govuk/components/back-link/macro.njk" import govukBackLink %}
{% from "govuk/components/cookie-banner/macro.njk" import govukCookieBanner %}
{% from "govuk/components/skip-link/macro.njk" import govukSkipLink %}
{% from "govuk/components/header/macro.njk" import govukHeader %}
{% from "govuk/components/phase-banner/macro.njk" import govukPhaseBanner %}
{% from "govuk/components/footer/macro.njk" import govukFooter %}

{% set htmlClasses = "app-html-class" %}
{% set htmlLang = "en" %}
{% set assetUrl = "YOUR-DOMAIN" %}
{% set themeColor = "blue" %}
{% set bodyClasses = "app-body-class" %}
{% set bodyAttributes = {
  "data-test": "My value",
  "data-other": "report:details"
} %}
{% set containerClasses = "app-width-container" %}
{% set mainClasses = "app-main-class" %}

{% block pageTitle %}GOV.UK - Customised page template{% endblock %}

{% block headIcons %}
  {{ super() }}
{% endblock %}

{% block head %}
  <link rel="stylesheet" href="/stylesheets/govuk-frontend.min.css">
{% endblock %}

{% block bodyStart %}
  <form action="/form-handler" method="post" novalidate>
    {{ govukCookieBanner({
      ariaLabel: "Cookies on [name of service]",
      messages: [
        {
          headingText: "Cookies on [name of service]",
          html: '<p class="govuk-body">We use some essential cookies to make this service work.</p>
            <p class="govuk-body">We’d also like to use analytics cookies so we can understand how you use the service and make improvements.</p>',
          actions: [
            {
              text: "Accept analytics cookies",
              type: "submit",
              name: "cookies[analytics]",
              value: "yes"
            },
            {
              text: "Reject analytics cookies",
              type: "submit",
              name: "cookies[analytics]",
              value: "no"
            },
            {
              text: "View cookies",
              href: "#"
            }
          ]
        }
      ]
    }) }}
  </form>
{% endblock %}

{% block govukSkipLink %}
  {{ govukSkipLink({
    href: "#main-content",
    text: "Skip to main content"
  }) }}
{% endblock %}

{% block govukServiceNavigation %}
  {{ govukServiceNavigation({
    serviceName: "Service name",
    serviceUrl: "#",
    navigation: [
      {
        href: "#",
        text: "Navigation item 1",
        active: true
      },
      {
        href: "#",
        text: "Navigation item 2"
      },
      {
        href: "#",
        text: "Navigation item 3"
      }
    ]
  }) }}
{% endblock %}

{% block headerEnd %}
  {{ govukPhaseBanner({
    tag: {
      text: "Alpha"
    },
    html: 'This is a new service – your <a class="govuk-link" href="#">feedback</a> will help us to improve it.'
  }) }}
{% endblock %}

{% block containerStart %}
  {{ govukBackLink({
    href: "#",
    text: "Back"
  }) }}
{% endblock %}

{% block main %}
  {{ super() }}
{% endblock %}

{% block content %}
  <h1 class="govuk-heading-xl">Customised page template</h1>
{% endblock %}

{% block govukFooter %}
  {{ govukFooter({
    meta: {
      items: [
        {
          href: "#",
          text: "Help"
        },
        {
          href: "#",
          text: "Cookies"
        },
        {
          href: "#",
          text: "Contact"
        },
        {
          href: "#",
          text: "Terms and conditions"
        }
      ]
    }
  }) }}
{% endblock %}

{% block bodyEnd %}
  <script type="module" src="/javascripts/govuk-frontend.min.js"></script>
  <script type="module">
    import { initAll } from '/javascripts/govuk-frontend.min.js'
    initAll()
  </script>
{% endblock %}
```

## Changing template content
If you’re using Nunjucks, you can change the template’s content using options.
How you set an option depends on whether it’s a ‘variable’ option or a ‘block’ option.
To set a ‘variable’ option, use `set` to pass in a single value or string. For example, to add a class to the `<body>` element using the `bodyClasses` option:

```
{% set bodyClasses = "EXAMPLE-CLASS" %}
```

By default, the template contains a [Skip link component](./components/skip-link.md), [Header component](./components/header.md) and [Footer component](./components/footer.md), all of which require ‘blocks’ to change.
To set a ‘block’ option, use `block` to pass in a multiline value or HTML markup. For example, to add a block of HTML before the closing `</body>` element in the page template using the `bodyEnd` option:

```
{% block bodyEnd %}
  <div>
     <p>Example text</p>
  </div>
{% endblock %}
```

To change the components that are included in the page template by default, set their equivalent blocks. For example:

```
{% block govukHeader %}
  {{ govukHeader ({
    homepageUrl: "/custom-url"
  }) }}
{% endblock %}
```

## Template blocks and options
Options are listed within the template blocks where they’re used:
  * [`<html>` and `<body>`](./styles/page-template/#html-and-body.md)
  * [`<head>` and metadata](./styles/page-template/#head-and-metadata.md)
  * [page header](./styles/page-template/#page-header.md)
  * [width container and main content](./styles/page-template/#width-container-and-main-content.md)
  * [footer](./styles/page-template/#footer.md)
  * [other options](./styles/page-template/#other-options.md)

###  `<html>` and `<body>`
Use options in `<html>` and `<body>` to:
  * [configure classes and attributes on the `<html>` element](./styles/page-template/#configure-classes-and-attributes-on-the-html-element.md)
  * [configure classes and attributes on the `<body>` element](./styles/page-template/#configure-classes-and-attributes-on-the-body-element.md)
  * [add content at the start or end of the `<body>` element](./styles/page-template/#add-content-at-the-start-or-end-of-the-body-element.md)

[ Open this example in a new tab: html and body template areas – page template ](./styles/page-template/html-body-template-areas.md)
####  Configure classes and attributes on the `<html>` element  `htmlClasses` (Variable) 
    
Add a class to the `<html>` element. `htmlLang` (Variable) 
    
Set the language of the whole document. If your `<title>` and `<main>` element are in a different language to the rest of the page, use `htmlLang` to set the language of the rest of the page.
####  Configure classes and attributes on the `<body>` element  `bodyClasses` (Variable) 
    
Add a class to the `<body>` element. `bodyAttributes` (Variable) 
    
Add attributes to the `<body>` element. Add each attribute and its value in the `bodyAttributes` object.
####  Add content at the start or end of the `<body>` element  `bodyStart` (Block) 
    
Add content after the opening `<body>` element.  
For example: the [Cookie banner component](./components/cookie-banner.md). `bodyEnd` (Block) 
    
Add content just before the closing `</body>` element.
###  `<head>` and metadata
Use options in `<head>` and metadata to:
  * [configure where your page can access GOV.UK Frontend assets](./styles/page-template/#configure-where-your-page-can-access-govuk-frontend-assets.md)
  * [customise icons and theme colours](./styles/page-template/#customise-icons-and-theme-colours.md)
  * [set the page’s title](./styles/page-template/#set-the-pages-title.md)
  * [add custom metadata to the `<head>` element](./styles/page-template/#add-custom-metadata-to-the-head-element.md) (like a `<link>` to your services stylesheet)

####  Configure where your page can access GOV.UK Frontend assets  `assetPath` (Variable) 
    
Specify a path to the [GOV.UK Frontend assets](https://frontend.design-system.service.gov.uk/import-font-and-images-assets/) (icons, images, font files). If you’re using the refreshed GOV.UK brand, you may need to update this path to point to the updated assets. `assetUrl` (Variable) 
    
Set the domain for assets where an absolute URL is required, for example the Open Graph image.
####  Customise icons and theme colours  `opengraphImageUrl` (Variable) 
    
Set the URL for the Open Graph image meta tag. The URL must be absolute, including the protocol and domain name. If you’re using the refreshed GOV.UK brand, you may need to update this path to point to the updated assets. `themeColor` (Variable) 
    
Set the [toolbar colour on some devices](https://developer.chrome.com/blog/support-for-theme-color-in-chrome-39-for-android). `headIcons` (Block) 
    
Override the default icons used for GOV.UK branded pages.  
For example: `<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />`.
####  Set the page’s title  `pageTitle` (Variable) 
    
Override the default page title (`<title>` element). `pageTitleLang` (Variable) 
    
Set the language of the `<title>` element if it’s different to [`htmlLang`](./styles/page-template/#htmllang-variable.md).
####  Add custom metadata to the `<head>` element  `head` (Block) 
    
Add additional items inside the `<head>` element.  
For example: `<meta name="description" content="My page description">`.
### Page header
Use options in page header to:
  * [replace the Skip Link rendered before the `<header>`](./styles/page-template/#replace-the-skip-link-rendered-before-the-header.md)
  * [add classes or attributes to the `<header>` element](./styles/page-template/#add-classes-or-attributes-to-the-header-element.md)
  * [add extra content at the start or end of the `<header>` element](./styles/page-template/#add-extra-content-at-the-start-or-end-of-the-header-element.md)
  * [add a Service Navigation component](./styles/page-template/#add-a-service-navigation-component.md)
  * [replace the default content from the header](./styles/page-template/#replace-the-default-content-from-the-header.md)

[ Open this example in a new tab: header template areas – page template ](./styles/page-template/header-template-areas.md)
####  Replace the Skip Link rendered before the `<header>` `skipLink` (Block) 
    
Deprecated - use [`govukSkipLink`](./styles/page-template/#govukskiplink-block.md) instead.  
Override the default [Skip link component](./components/skip-link.md). `govukSkipLink` (Block) 
    
Override the default [Skip link component](./components/skip-link.md).
####  Add classes or attributes to the `<header>` element  `headerClasses` (Variable) 
    
Add a class to the `<header>` element. `headerAttributes` (Variable) 
    
Add attributes to the `<header>` element. Add each attribute and its value in the `headerAttributes` object.
####  Add extra content at the start or end of the `<header>` element  `headerStart` (Block) 
    
Add content after the opening `<header>` element. `headerEnd` (Block) 
    
Add content just before the closing `</header>` element.  
For example: the [Phase banner component](./components/phase-banner.md).
####  Add a Service Navigation component  `serviceName` (Variable) 
    
Renders a Service Navigation with the given `serviceName` if present.  
If you need to add navigation items, you’ll need to [replace the default Service Navigation with your own](./styles/page-template/#govukservicenavigation-block.md). `govukServiceNavigation` (Block) 
    
Override the Service Navigation rendered if [`serviceName`](./styles/page-template/#servicename-variable.md) is set or add your custom Service Navigation without affecting the rest of the `<header>` element.
####  Replace the default content from the header  `header` (Block) 
    
Override the `<header>` element and the [`headerStart`](./styles/page-template/#headerstart-block.md), [`govukHeader`](./styles/page-template/#govukheader-block.md), [`govukServiceNavigation`](./styles/page-template/#govukservicenavigation-block.md), and [`headerEnd`](./styles/page-template/#headerend-block.md) blocks. `govukHeader` (Block) 
    
Override the GOV.UK Header without changing the rest of the `<header>` element.
### Width container and main content
The page template [renders your content](./styles/page-template/#render-your-content-inside-the-template.md) in a `<main>` tag, wrapped in a container limiting the content’s width.
Use options in width container and main content to:
  * [add classes to the container limiting the content’s width](./styles/page-template/#add-classes-or-attributes-to-the-container.md)
  * [add content at the start or end of the container](./styles/page-template/#add-extra-content-at-the-start-or-end-of-the-container.md)
  * [add classes or attributes to the `<main>` element](./styles/page-template/#add-classes-or-attributes-to-the-main-element.md)
  * [replace the container or `<main>` element](./styles/page-template/#replace-the-container-or-main-element.md) with your own

[ Open this example in a new tab: main content areas – page template ](./styles/page-template/main-content-template-areas.md)
####  Render your content inside the template  `content` (Block) 
    
Add content that needs to appear in the `<main>` element.
####  Add classes or attributes to the container  `containerClasses` (Variable) 
    
Add a class to the container. This is useful if you want to make the page wrapper a fixed width. `containerAttributes` (Variable) 
    
Add other attributes than `class` to the container element. Add each attribute and its value in the `containerAttributes` object.
####  Add extra content at the start or end of the container  `containerStart` (Block) 
    
Add content after the opening `<div class=”govuk-width-container”>` element that limits the width of the page.  
For example: the [Back link component](./components/back-link.md), [Breadcrumbs component](./components/breadcrumbs.md). `beforeContent` (Block) 
    
Deprecated - Use [`containerStart`](./styles/page-template/#containerstart-block.md) instead.  
Add content that needs to appear outside the `<main>` element.  
For example: the [Back link component](./components/back-link.md), [Breadcrumbs component](./components/breadcrumbs.md). `containerEnd` (Block) 
    
Add content just before the closing `</div>` of the width container.
####  Add classes or attributes to the `<main>` element  `mainClasses` (Variable) 
    
Add a class to the `<main>` element. `mainLang` (Variable) 
    
Set the language of the `<main>` element if it’s different to [`htmlLang`](./styles/page-template/#htmllang-variable.md). `mainAttributes` (Variable) 
    
Add other attributes than `class` and `lang` to the `<main>` element. Add each attribute and its value in the `mainAttributes` object.
####  Replace the container or `<main>` element  `container` (Block) 
    
Override the default container limiting the width of the page, including the `<main>` element it wraps. `main` (Block) 
    
Override the whole `<main>` element.
### Footer
Use options in footer to:
  * [add classes or attributes to the `<footer>` element](./styles/page-template/#add-classes-or-attributes-to-the-footer-element.md)
  * [add extra content at the start or end of the `<footer>` element](./styles/page-template/#add-extra-content-at-the-start-or-end-of-the-footer-element.md)
  * [replace the default content from the footer](./styles/page-template/#replace-the-default-content-from-the-footer.md)

[ Open this example in a new tab: footer template areas – page template ](./styles/page-template/footer-template-areas.md)
####  Add classes or attributes to the `<footer>` element  `footerClasses` (Variable) 
    
Add a class to the `<footer>` element. `footerAttributes` (Variable) 
    
Add attributes to the `<footer>` element. Add each attribute and its value in the `footerAttributes` object.
####  Add extra content at the start or end of the `<footer>` element  `footerStart` (Block) 
    
Add content after the opening `<footer>` element. `footerEnd` (Block) 
    
Add content just before the closing `</footer>` element.
####  Replace the default content from the footer  `footer` (Block) 
    
Override the `<footer>` element and the `govukFooter`, `footerStart`, and `footerEnd` blocks. `govukfooter` (Block) 
    
Override the GOV.UK Footer without changing the rest of the `<footer>` element.
### Other options
####  Security  `cspNonce` (Variable) 
    
Add a nonce attribute to the script for your Content Security Policy (CSP). Provide a nonce that hostile actors cannot guess, as otherwise they can easily find a way around your CSP. However, you should use this attribute only if you’re not able to include the hash for the inline scripts in your service’s CSP.
## Help improve this style
If you spot a problem with this guidance you can [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/styles/page-template/index.md). 
If you’re not sure how to do this, read guidance on [how to propose changes in GitHub](./community/propose-a-content-change-using-github.md). 
## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./styles/page-template/#top.md)
