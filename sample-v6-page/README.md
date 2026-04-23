# GDS v6.1.0 Sample Page

Plain HTML + Sass. No Nunjucks, no v5 fallbacks.

## Build

```bash
npm install
npm run build
```

Produces:
- `dist/main.css` — compiled from `src/styles/main.scss` → `govuk-frontend/dist/govuk/_index.scss`
- `dist/govuk-frontend.min.js` — copied from node_modules
- `dist/assets/` — fonts, images, favicons

Serve the folder (e.g. `npx serve .`) and open `index.html`.

## v6.1.0 compliance checklist

- Header is a `<div class="govuk-header">` with combined Tudor Crown logotype SVG (viewBox `0 0 324 60`), no service name.
- Service name lives in the separate `govuk-service-navigation` section below the header.
- Phase banner uses the v6 wording: *"This is a new service. Help us improve it and give your feedback by email."*
- Footer is a `<div class="govuk-footer">` with standalone Tudor Crown SVG (viewBox `0 0 64 60`) and inline OGL licence SVG.
- Sass compiled from source (`@use "govuk-frontend/dist/govuk"`), not the precompiled `.min.css`.
- `$govuk-assets-path` overridden via the `@use ... with (...)` syntax — no deprecated `!default` reassignment.
