# UK Government Departments — GDS v6 Guidance

Use this file **only when the user explicitly names a department** (MoJ, DfT, MoD, FCDO, HO, HMRC, DWP, HMPPS, etc.). Otherwise, stick to the standard GOV.UK markup in `SKILL.md`.

## Core rule

**The header never changes.** The unified GOV.UK Tudor Crown logotype is mandatory for every central-government service on the GOV.UK platform. No departmental logos in the header — ever. The department name goes in the **Service Navigation** component.

The **footer** is the only place where departmental attribution is permitted, and even then GDS prescribes a **text link in the `meta` slot**, not a logo.

---

## Footer pattern — departmental attribution

Add a `govuk-footer__meta-custom` block inside the existing `govuk-footer__meta` container, or use the `meta.html` slot. The key is: text link only, styled with `govuk-footer__link`.

```html
<div class="govuk-footer">
  <div class="govuk-width-container">
    <!-- Tudor Crown SVG (unchanged — see components/footer.md) -->
    <svg focusable="false" role="presentation" xmlns="http://www.w3.org/2000/svg"
         viewBox="0 0 64 60" height="30" width="32"
         fill="currentcolor" class="govuk-footer__crown">
      <!-- ... crown paths ... -->
    </svg>

    <div class="govuk-footer__meta">
      <div class="govuk-footer__meta-item govuk-footer__meta-item--grow">
        <!-- OGL SVG + licence text (unchanged) -->

        <!-- Departmental attribution: TEXT LINK, not a logo -->
        <p class="govuk-body-s govuk-!-margin-top-4">
          Built by the
          <a class="govuk-footer__link"
             href="https://www.gov.uk/government/organisations/ministry-of-justice">
            Ministry of Justice
          </a>
        </p>
      </div>
      <div class="govuk-footer__meta-item">
        <a class="govuk-footer__link govuk-footer__copyright-logo"
           href="https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/">
          © Crown copyright
        </a>
      </div>
    </div>
  </div>
</div>
```

---

## Department reference

| Department | Full name | gov.uk URL suffix | Frontend library |
|---|---|---|---|
| MoJ | Ministry of Justice | `/ministry-of-justice` | `@ministryofjustice/frontend` (extends GDS) |
| HMPPS | HM Prison and Probation Service | `/hm-prison-and-probation-service` | MoJ Frontend |
| HMCTS | HM Courts & Tribunals Service | `/hm-courts-and-tribunals-service` | MoJ Frontend |
| DfT | Department for Transport | `/department-for-transport` | Pure GDS |
| MoD | Ministry of Defence | `/ministry-of-defence` | Pure GDS |
| FCDO | Foreign, Commonwealth & Development Office | `/foreign-commonwealth-development-office` | Pure GDS |
| HO | Home Office | `/home-office` | Pure GDS |
| HMRC | HM Revenue & Customs | `/hm-revenue-customs` | Pure GDS |
| DWP | Department for Work and Pensions | `/department-for-work-pensions` | Pure GDS |
| DfE | Department for Education | `/department-for-education` | Pure GDS |
| DHSC | Department of Health and Social Care | `/department-of-health-and-social-care` | Pure GDS |
| DESNZ | Department for Energy Security and Net Zero | `/department-for-energy-security-and-net-zero` | Pure GDS |
| Defra | Department for Environment, Food & Rural Affairs | `/department-for-environment-food-rural-affairs` | Pure GDS |
| DBT | Department for Business and Trade | `/department-for-business-and-trade` | Pure GDS |
| DSIT | Department for Science, Innovation and Technology | `/department-for-science-innovation-and-technology` | Pure GDS |

Full URL format: `https://www.gov.uk/government/organisations{suffix}`.

---

## MoJ Frontend — extension components

For MoJ/HMPPS/HMCTS services, **in addition to** GOV.UK Frontend v6.1.0:

```bash
npm install @ministryofjustice/frontend
```

Sass entry:
```scss
@use "govuk-frontend/dist/govuk" with ($govuk-assets-path: "/assets/");
@use "@ministryofjustice/frontend/moj/all";
```

Adds (among others): `moj-filter`, `moj-banner`, `moj-sub-navigation`, `moj-identity-bar`, `moj-multi-file-upload`, `moj-date-picker`, `moj-sortable-table`, `moj-pagination`, `moj-search`, `moj-timeline`.

These sit alongside `govuk-*` components — prefer a `govuk-*` component whenever one exists. Only reach for `moj-*` when GDS has no equivalent.

---

## What NOT to do

1. **Do not add a departmental logo SVG to the header.** Breaks v6 brand rules.
2. **Do not add a departmental logo to the footer.** GDS doesn't distribute official logo SVGs; unofficial ones violate Crown copyright on crests and drift visually from the department's current brand.
3. **Do not replace "© Crown copyright".** It stays verbatim.
4. **Do not omit the OGL licence block** unless the service legitimately publishes under a different licence (rare — requires explicit confirmation).
5. **Do not use a department's own design system** (e.g. an intranet brand) for a public GOV.UK service.
