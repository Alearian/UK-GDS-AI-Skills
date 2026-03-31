#  [](./staying-up-to-date/#staying-up-to-date-with-changes.md)Staying up to date with changes
Staying up to date with the latest version of GOV.UK Frontend helps make sure your service:
  * continues to look, feel and behave consistently with GOV.UK
  * benefits from the latest accessibility and usability improvements
  * works correctly in the latest browsers and assistive technologies, and benefits from any new improvements made possible in those versions

As with all software dependencies, you should have a plan to regularly update GOV.UK Frontend as part of the ongoing maintenance of your service.
##  [](./staying-up-to-date/#getting-updates-when-we-publish-a-new-release.md)Getting updates when we publish a new release
To make sure you’re notified when we publish a new release, you can:
  * [watch the govuk-frontend repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository) on GitHub
  * join the [#govuk-design-system Slack channel](https://ukgovernmentdigital.slack.com/app_redirect?channel=govuk-design-system)
  * [sign up for email updates](https://mailchi.mp/707ce8dec373/get-updated-by-email-govuk-design-system)
  * use an automated dependency monitoring tool like [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates)

##  [](./staying-up-to-date/#find-out-which-version-you-39-re-currently-using.md)Find out which version you’re currently using
If you installed GOV.UK Frontend using npm, find out which version of GOV.UK Frontend you’re using by running npm list govuk-frontend from the root of your project:

```
$ npm list govuk-frontend
your_project@/path/to/your/project
└──govuk-frontend@4.6.0

```

If you installed GOV.UK Frontend using precompiled files, the CSS and JavaScript files should include the version number as part of the filename.
##  [](./staying-up-to-date/#understanding-what-has-changed.md)Understanding what has changed
How to interpret the version numbering and the release notes.
###  [](./staying-up-to-date/#how-the-version-numbering-works.md)How the version numbering works
GOV.UK Frontend’s version number follows the format `MAJOR.MINOR.PATCH` where `MAJOR`, `MINOR` and `PATCH` are numbers.
We aim to follow [semantic versioning](https://semver.org/). This means we will:
  * increase the `PATCH` number if a release only includes bug fixes, for example going from v4.6.0 to v4.6.1
  * increase the `MINOR` number and reset the `PATCH` number to 0 if a release includes new features, for example going from v4.6.1 to v4.7.0
  * increase the `MAJOR` number and reset the `MINOR` and `PATCH` numbers to 0 if a release might require you to make changes to your service when you update (see [breaking changes](./staying-up-to-date/#breaking-changes.md)), for example going from v4.7.0 to v5.0.0

The intention is to make sure you can easily update to new minor and patch releases without needing to make any changes to your service.
However, what you consider a breaking change can depend on how you are using GOV.UK Frontend in your service. You should always read the release notes and test your service when upgrading to a new version.
###  [](./staying-up-to-date/#using-the-release-notes.md)Using the release notes
We publish release notes for every release. They document the changes we’ve made, including both technical and design changes.
When upgrading to a newer version of GOV.UK Frontend you should read all the release notes from the version you are currently using, up to and including the version you are upgrading to.
The release notes can be quite long, especially for new major versions. It’s important to read them carefully, but you might find many of the changes do not affect your service.
####  [](./staying-up-to-date/#breaking-changes.md)Breaking changes
We’ll only include breaking changes in major releases.
Breaking changes might require you to take some action so your service continues to work.
You might find many of the breaking changes do not affect you, especially if you have a process for dealing with deprecations and upgrading versions when upgrading between minor and patch releases.
Some breaking changes involve making changes to your HTML. If you’re using our Nunjucks macros to generate the HTML for your service, the changes are usually automatically applied.
####  [](./staying-up-to-date/#recommended-changes.md)Recommended changes
We might include recommended changes in any release.
You do not need to make recommended changes for your service to keep working, but these changes often provide improvements of some kind. For example, making something more accessible.
####  [](./staying-up-to-date/#new-features.md)New features
We’ll only include new features in major or minor releases.
Some features will require you to make changes to your service, if you want to use them.
####  [](./staying-up-to-date/#deprecations.md)Deprecations
We might include deprecations in any release.
We deprecate things to communicate a future breaking change, usually scheduled to be made in the next major version.
For example, we would deprecate something in v4.6.0 before we remove it in v5.0.0 at which point we would include it as a breaking change in the release notes.
If you deal with deprecations as they come up you can reduce the amount of work required to upgrade to the next major version.
####  [](./staying-up-to-date/#fixes.md)Fixes
We might include fixes in any release.
Fixes include bug fixes and small improvements that do not require you to do anything.
If a fix requires you to do something, we will include it as a recommended or breaking change.
##  [](./staying-up-to-date/#updating-to-the-latest-version.md)Updating to the latest version
Once you know what has changed, you’re ready to upgrade to the latest version.
You’re responsible for making sure your service continues to work as expected after upgrading.
You might want to consider using automated testing or visual regression tests to increase your confidence and minimise the amount of manual testing required.
###  [](./staying-up-to-date/#updating-to-the-latest-version-if-you-installed-gov-uk-frontend-using-npm.md)Updating to the latest version if you installed GOV.UK Frontend using npm
If you need to update GOV.UK Frontend for a specific package in a monorepo project (for example using Lerna, npm workspaces, Yarn workspaces, or pnpm workspaces), please make sure to adapt the commands to the tool you are using. 
To update to the most recent version, run:

```
npm install govuk-frontend@latest

```

If you want to install an earlier version, replace latest with the version that you want to update to. For example:

```
npm install govuk-frontend@4.6.0

```

If you want to install the most recent version of GOV.UK Frontend v4.x, run:

```
npm install govuk-frontend@latest-v4

```

###  [](./staying-up-to-date/#updating-to-the-latest-version-if-you-installed-gov-uk-frontend-using-precompiled-files.md)Updating to the latest version if you installed GOV.UK Frontend using precompiled files
Follow the instructions on the page [‘Try GOV.UK Frontend using precompiled files’](./install-using-precompiled-files.md), replacing any files that already exist.
You should also remove older versions of the precompiled CSS and JavaScript, and any other files that no longer exist in the latest release.
  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/staying-up-to-date/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Staying+up+to+date+with+changes%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fstaying-up-to-date%2F%29&labels=bug&title=Re%3A+%27Staying+up+to+date+with+changes%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
