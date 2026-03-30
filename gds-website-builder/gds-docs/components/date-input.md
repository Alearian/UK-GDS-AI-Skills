#  Date input 
Use the date input component to help users enter a memorable date or one they can easily look up.
[ Open this example in a new tab: date input ](./components/date-input/default.md)
  * [HTML](./components/date-input/#date-input-example-html.md)
  * [Nunjucks](./components/date-input/#date-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-hint">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">
        When was your passport issued?
      </h1>
    </legend>
    <div id="passport-issued-hint" class="govuk-hint">
      For example, 27 3 2007
    </div>
    <div class="govuk-date-input" id="passport-issued">
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-day">
            Day
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-day" name="passport-issued-day" type="text" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-month">
            Month
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-month" name="passport-issued-month" type="text" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-year">
            Year
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-4" id="passport-issued-year" name="passport-issued-year" type="text" inputmode="numeric">
        </div>
      </div>
    </div>
  </fieldset>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  **Required.** This is used for the main component and to compose the ID attribute for each item.   |  
| namePrefix  | string  |  Optional prefix. This is used to prefix each item `name`, separated by `-`.   |  
| items  | array  |  The inputs within the date input component. [ See macro options for items](./components/date-input/#options-date-input-example--items.md).   |  
| hint  | object  |  Can be used to add a hint to a date input component. [ See macro options for hint](./components/date-input/#options-date-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the date input component. [ See macro options for formGroup](./components/date-input/#options-date-input-example--form-group.md).   |  
| fieldset  | object  |  Can be used to add a fieldset to the date input component. [See macro options for fieldset](./components/fieldset/#options-fieldset-example.md).   |  
| classes  | string  |  Classes to add to the date-input container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date-input container.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  Item-specific ID. If provided, it will be used instead of the generated ID.   |  
| name  | string  |  **Required.** Item-specific name attribute.   |  
| label  | string  |  Item-specific label text. If provided, this will be used instead of `name` for item label text.   |  
| value  | string  |  If provided, it will be used as the initial value of the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| classes  | string  |  Classes to add to date input item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date input tag.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInputs  | object  |  Content to add before the inputs used by the date input component. [ See macro options for formGroup beforeInputs](./components/date-input/#options-date-input-example--form-group-before-inputs.md).   |  
| afterInputs  | object  |  Content to add after the inputs used by the date input component. [ See macro options for formGroup afterInputs](./components/date-input/#options-date-input-example--form-group-after-inputs.md).   |  
Options for formGroup `beforeInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "passport-issued",
  namePrefix: "passport-issued",
  fieldset: {
    legend: {
      text: "When was your passport issued?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: {
    text: "For example, 27 3 2007"
  }
}) }}
```

## When to use this component
Use the date input component when you’re asking users for a date they’ll already know, or can look up without using a calendar.
## When not to use this component
Do not use the date input component if users are unlikely to know the exact date of the event you’re asking about.
Read more in the [Ask users for dates pattern](./patterns/dates.md).
## How it works
The date input component consists of 3 fields to let users enter a day, month and year.
The 3 date fields are grouped together in a `<fieldset>` with a `<legend>` that describes them, as shown in the examples on this page. This is usually a question, like ‘What is your date of birth?’.
If you’re asking [one question per page in your service](./patterns/question-pages/#start-by-asking-one-question-per-page.md), you can set the contents of the `<legend>` as the page heading. This is good practice as it means that users of screen readers will only hear the contents once.
Read more about [why and how to set legends as headings](./get-started/labels-legends-headings.md).
Make sure that any example dates you use in hint text are valid for the question being asked.
Accept month names written out in full or abbreviated form (for example, ‘january’ or ‘jan’) as some users may enter months in this way.
There are 2 ways to use the date input component. You can use HTML or, if you’re using [Nunjucks](https://mozilla.github.io/nunjucks/) or the [GOV.UK Prototype Kit](https://prototype-kit.service.gov.uk), you can use the Nunjucks macro.
[ Open this example in a new tab: date input second ](./components/date-input/default.md)
  * [HTML](./components/date-input/#date-input-second-example-html.md)
  * [Nunjucks](./components/date-input/#date-input-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-hint">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">
        When was your passport issued?
      </h1>
    </legend>
    <div id="passport-issued-hint" class="govuk-hint">
      For example, 27 3 2007
    </div>
    <div class="govuk-date-input" id="passport-issued">
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-day">
            Day
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-day" name="passport-issued-day" type="text" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-month">
            Month
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-month" name="passport-issued-month" type="text" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-year">
            Year
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-4" id="passport-issued-year" name="passport-issued-year" type="text" inputmode="numeric">
        </div>
      </div>
    </div>
  </fieldset>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  **Required.** This is used for the main component and to compose the ID attribute for each item.   |  
| namePrefix  | string  |  Optional prefix. This is used to prefix each item `name`, separated by `-`.   |  
| items  | array  |  The inputs within the date input component. [ See macro options for items](./components/date-input/#options-date-input-second-example--items.md).   |  
| hint  | object  |  Can be used to add a hint to a date input component. [ See macro options for hint](./components/date-input/#options-date-input-second-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the date input component. [ See macro options for formGroup](./components/date-input/#options-date-input-second-example--form-group.md).   |  
| fieldset  | object  |  Can be used to add a fieldset to the date input component. [See macro options for fieldset](./components/fieldset/#options-fieldset-example.md).   |  
| classes  | string  |  Classes to add to the date-input container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date-input container.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  Item-specific ID. If provided, it will be used instead of the generated ID.   |  
| name  | string  |  **Required.** Item-specific name attribute.   |  
| label  | string  |  Item-specific label text. If provided, this will be used instead of `name` for item label text.   |  
| value  | string  |  If provided, it will be used as the initial value of the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| classes  | string  |  Classes to add to date input item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date input tag.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInputs  | object  |  Content to add before the inputs used by the date input component. [ See macro options for formGroup beforeInputs](./components/date-input/#options-date-input-second-example--form-group-before-inputs.md).   |  
| afterInputs  | object  |  Content to add after the inputs used by the date input component. [ See macro options for formGroup afterInputs](./components/date-input/#options-date-input-second-example--form-group-after-inputs.md).   |  
Options for formGroup `beforeInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "passport-issued",
  namePrefix: "passport-issued",
  fieldset: {
    legend: {
      text: "When was your passport issued?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: {
    text: "For example, 27 3 2007"
  }
}) }}
```

Never automatically tab users between the fields of the date input because this can be confusing and may clash with normal keyboard controls.
### If you’re asking more than one question on the page
If you’re asking more than one question on the page, do not set the contents of the `<legend>` as the page heading. Read more about [asking multiple questions on question pages](./patterns/question-pages/#asking-multiple-questions-on-a-page.md).
[ Open this example in a new tab: date input without a heading – date input second ](./components/date-input/without-heading.md)
  * [HTML](./components/date-input/#date-input-without-a-heading-date-input-second-example-html.md)
  * [Nunjucks](./components/date-input/#date-input-without-a-heading-date-input-second-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-hint">
    <legend class="govuk-fieldset__legend">
      When was your passport issued?
    </legend>
    <div id="passport-issued-hint" class="govuk-hint">
      For example, 27 3 2007
    </div>
    <div class="govuk-date-input" id="passport-issued">
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-day">
            Day
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-day" name="passport-issued-day" type="text" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-month">
            Month
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-month" name="passport-issued-month" type="text" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-year">
            Year
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-4" id="passport-issued-year" name="passport-issued-year" type="text" inputmode="numeric">
        </div>
      </div>
    </div>
  </fieldset>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  **Required.** This is used for the main component and to compose the ID attribute for each item.   |  
| namePrefix  | string  |  Optional prefix. This is used to prefix each item `name`, separated by `-`.   |  
| items  | array  |  The inputs within the date input component. [ See macro options for items](./components/date-input/#options-date-input-without-a-heading-date-input-second-example--items.md).   |  
| hint  | object  |  Can be used to add a hint to a date input component. [ See macro options for hint](./components/date-input/#options-date-input-without-a-heading-date-input-second-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the date input component. [ See macro options for formGroup](./components/date-input/#options-date-input-without-a-heading-date-input-second-example--form-group.md).   |  
| fieldset  | object  |  Can be used to add a fieldset to the date input component. [See macro options for fieldset](./components/fieldset/#options-fieldset-example.md).   |  
| classes  | string  |  Classes to add to the date-input container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date-input container.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  Item-specific ID. If provided, it will be used instead of the generated ID.   |  
| name  | string  |  **Required.** Item-specific name attribute.   |  
| label  | string  |  Item-specific label text. If provided, this will be used instead of `name` for item label text.   |  
| value  | string  |  If provided, it will be used as the initial value of the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| classes  | string  |  Classes to add to date input item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date input tag.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInputs  | object  |  Content to add before the inputs used by the date input component. [ See macro options for formGroup beforeInputs](./components/date-input/#options-date-input-without-a-heading-date-input-second-example--form-group-before-inputs.md).   |  
| afterInputs  | object  |  Content to add after the inputs used by the date input component. [ See macro options for formGroup afterInputs](./components/date-input/#options-date-input-without-a-heading-date-input-second-example--form-group-after-inputs.md).   |  
Options for formGroup `beforeInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "passport-issued",
  namePrefix: "passport-issued",
  fieldset: {
    legend: {
      text: "When was your passport issued?"
    }
  },
  hint: {
    text: "For example, 27 3 2007"
  }
}) }}
```

### Use the autocomplete attribute for a date of birth
Use the `autocomplete` attribute on the date input component when you’re asking for a date of birth. This lets browsers autofill the information on a user’s behalf if they’ve entered it previously.
To do this, set the `autocomplete` attribute on the 3 fields to `bday-day`, `bday-month` and `bday-year`. See how to do this in the HTML and Nunjucks tabs in the following example.
[ Open this example in a new tab: date input to ask for date of birth – date input ](./components/date-input/date-of-birth.md)
  * [HTML](./components/date-input/#default-2-open-html.md)
  * [Nunjucks](./components/date-input/#default-2-open-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset" role="group" aria-describedby="dob-hint">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">
        What is your date of birth?
      </h1>
    </legend>
    <div id="dob-hint" class="govuk-hint">
      For example, 31 3 1980
    </div>
    <div class="govuk-date-input" id="dob">
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="dob-day">
            Day
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="dob-day" name="dob-day" type="text" autocomplete="bday-day" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="dob-month">
            Month
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="dob-month" name="dob-month" type="text" autocomplete="bday-month" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="dob-year">
            Year
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-4" id="dob-year" name="dob-year" type="text" autocomplete="bday-year" inputmode="numeric">
        </div>
      </div>
    </div>
  </fieldset>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  **Required.** This is used for the main component and to compose the ID attribute for each item.   |  
| namePrefix  | string  |  Optional prefix. This is used to prefix each item `name`, separated by `-`.   |  
| items  | array  |  The inputs within the date input component. [ See macro options for items](./components/date-input/#options-default-2-open--items.md).   |  
| hint  | object  |  Can be used to add a hint to a date input component. [ See macro options for hint](./components/date-input/#options-default-2-open--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the date input component. [ See macro options for formGroup](./components/date-input/#options-default-2-open--form-group.md).   |  
| fieldset  | object  |  Can be used to add a fieldset to the date input component. [See macro options for fieldset](./components/fieldset/#options-fieldset-example.md).   |  
| classes  | string  |  Classes to add to the date-input container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date-input container.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  Item-specific ID. If provided, it will be used instead of the generated ID.   |  
| name  | string  |  **Required.** Item-specific name attribute.   |  
| label  | string  |  Item-specific label text. If provided, this will be used instead of `name` for item label text.   |  
| value  | string  |  If provided, it will be used as the initial value of the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| classes  | string  |  Classes to add to date input item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date input tag.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInputs  | object  |  Content to add before the inputs used by the date input component. [ See macro options for formGroup beforeInputs](./components/date-input/#options-default-2-open--form-group-before-inputs.md).   |  
| afterInputs  | object  |  Content to add after the inputs used by the date input component. [ See macro options for formGroup afterInputs](./components/date-input/#options-default-2-open--form-group-after-inputs.md).   |  
Options for formGroup `beforeInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "dob",
  namePrefix: "dob",
  fieldset: {
    legend: {
      text: "What is your date of birth?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: {
    text: "For example, 31 3 1980"
  },
  items: [
    {
      name: "day",
      classes: "govuk-input--width-2",
      autocomplete: "bday-day"
    },
    {
      name: "month",
      classes: "govuk-input--width-2",
      autocomplete: "bday-month"
    },
    {
      name: "year",
      classes: "govuk-input--width-4",
      autocomplete: "bday-year"
    }
  ]
}) }}
```

If you are working in production you’ll need to do this to meet [WCAG 2.2 success criterion 1.3.5: Identify input purpose, level AA](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html).
### Error messages
If you’re highlighting the whole date, style all the fields like this:
[ Open this example in a new tab: date input with errors – date input ](./components/date-input/error.md)
  * [HTML](./components/date-input/#date-input-with-errors-date-input-example-html.md)
  * [Nunjucks](./components/date-input/#date-input-with-errors-date-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-hint passport-issued-error">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">
        When was your passport issued?
      </h1>
    </legend>
    <div id="passport-issued-hint" class="govuk-hint">
      For example, 27 3 2007
    </div>
    <p id="passport-issued-error" class="govuk-error-message">
      <span class="govuk-visually-hidden">Error:</span> The date your passport was issued must be in the past
    </p>
    <div class="govuk-date-input" id="passport-issued">
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-day">
            Day
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2 govuk-input--error" id="passport-issued-day" name="passport-issued-day" type="text" value="6" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-month">
            Month
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2 govuk-input--error" id="passport-issued-month" name="passport-issued-month" type="text" value="3" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-year">
            Year
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-4 govuk-input--error" id="passport-issued-year" name="passport-issued-year" type="text" value="2076" inputmode="numeric">
        </div>
      </div>
    </div>
  </fieldset>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  **Required.** This is used for the main component and to compose the ID attribute for each item.   |  
| namePrefix  | string  |  Optional prefix. This is used to prefix each item `name`, separated by `-`.   |  
| items  | array  |  The inputs within the date input component. [ See macro options for items](./components/date-input/#options-date-input-with-errors-date-input-example--items.md).   |  
| hint  | object  |  Can be used to add a hint to a date input component. [ See macro options for hint](./components/date-input/#options-date-input-with-errors-date-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the date input component. [ See macro options for formGroup](./components/date-input/#options-date-input-with-errors-date-input-example--form-group.md).   |  
| fieldset  | object  |  Can be used to add a fieldset to the date input component. [See macro options for fieldset](./components/fieldset/#options-fieldset-example.md).   |  
| classes  | string  |  Classes to add to the date-input container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date-input container.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  Item-specific ID. If provided, it will be used instead of the generated ID.   |  
| name  | string  |  **Required.** Item-specific name attribute.   |  
| label  | string  |  Item-specific label text. If provided, this will be used instead of `name` for item label text.   |  
| value  | string  |  If provided, it will be used as the initial value of the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| classes  | string  |  Classes to add to date input item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date input tag.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInputs  | object  |  Content to add before the inputs used by the date input component. [ See macro options for formGroup beforeInputs](./components/date-input/#options-date-input-with-errors-date-input-example--form-group-before-inputs.md).   |  
| afterInputs  | object  |  Content to add after the inputs used by the date input component. [ See macro options for formGroup afterInputs](./components/date-input/#options-date-input-with-errors-date-input-example--form-group-after-inputs.md).   |  
Options for formGroup `beforeInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "passport-issued",
  namePrefix: "passport-issued",
  fieldset: {
    legend: {
      text: "When was your passport issued?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: {
    text: "For example, 27 3 2007"
  },
  errorMessage: {
    text: "The date your passport was issued must be in the past"
  },
  items: [
    {
      classes: "govuk-input--width-2 govuk-input--error",
      name: "day",
      value: "6"
    },
    {
      classes: "govuk-input--width-2 govuk-input--error",
      name: "month",
      value: "3"
    },
    {
      classes: "govuk-input--width-4 govuk-input--error",
      name: "year",
      value: "2076"
    }
  ]
}) }}
```

If you’re highlighting just one field - either the day, month or year - only style the field that has an error. The error message must say which field has an error, like this:
[ Open this example in a new tab: dates with errors – date input ](./components/date-input/error-single.md)
  * [HTML](./components/date-input/#dates-with-errors-date-input-example-html.md)
  * [Nunjucks](./components/date-input/#dates-with-errors-date-input-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-hint passport-issued-error">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">
        When was your passport issued?
      </h1>
    </legend>
    <div id="passport-issued-hint" class="govuk-hint">
      For example, 27 3 2007
    </div>
    <p id="passport-issued-error" class="govuk-error-message">
      <span class="govuk-visually-hidden">Error:</span> The date your passport was issued must include a year
    </p>
    <div class="govuk-date-input" id="passport-issued">
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-day">
            Day
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-day" name="passport-issued-day" type="text" value="6" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-month">
            Month
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-month" name="passport-issued-month" type="text" value="3" inputmode="numeric">
        </div>
      </div>
      <div class="govuk-date-input__item">
        <div class="govuk-form-group">
          <label class="govuk-label govuk-date-input__label" for="passport-issued-year">
            Year
          </label>
          <input class="govuk-input govuk-date-input__input govuk-input--width-4 govuk-input--error" id="passport-issued-year" name="passport-issued-year" type="text" inputmode="numeric">
        </div>
      </div>
    </div>
  </fieldset>
</div>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  **Required.** This is used for the main component and to compose the ID attribute for each item.   |  
| namePrefix  | string  |  Optional prefix. This is used to prefix each item `name`, separated by `-`.   |  
| items  | array  |  The inputs within the date input component. [ See macro options for items](./components/date-input/#options-dates-with-errors-date-input-example--items.md).   |  
| hint  | object  |  Can be used to add a hint to a date input component. [ See macro options for hint](./components/date-input/#options-dates-with-errors-date-input-example--hint.md).   |  
| errorMessage  | object  |  Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for `errorMessage`, for example `false` or `null`. [See macro options for errorMessage](./components/error-message/#options-error-message-example.md).   |  
| formGroup  | object  |  Additional options for the form group containing the date input component. [ See macro options for formGroup](./components/date-input/#options-dates-with-errors-date-input-example--form-group.md).   |  
| fieldset  | object  |  Can be used to add a fieldset to the date input component. [See macro options for fieldset](./components/fieldset/#options-fieldset-example.md).   |  
| classes  | string  |  Classes to add to the date-input container.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date-input container.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| id  | string  |  Item-specific ID. If provided, it will be used instead of the generated ID.   |  
| name  | string  |  **Required.** Item-specific name attribute.   |  
| label  | string  |  Item-specific label text. If provided, this will be used instead of `name` for item label text.   |  
| value  | string  |  If provided, it will be used as the initial value of the input.   |  
| autocomplete  | string  |  Attribute to meet [WCAG success criterion 1.3.5: Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html), for instance `"bday-day"`. See the [Autofill section in the HTML standard](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section in the HTML standard for full list of attributes that can be used.   |  
| pattern  | string  |  Attribute to [provide a regular expression pattern](https://html.spec.whatwg.org/multipage/input.html#the-pattern-attribute), used to match allowed character combinations for the input value.   |  
| classes  | string  |  Classes to add to date input item.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the date input tag.   |  
Options for `formGroup` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| classes  | string  |  Classes to add to the form group (for example to show error state for the whole group).   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the form group.   |  
| beforeInputs  | object  |  Content to add before the inputs used by the date input component. [ See macro options for formGroup beforeInputs](./components/date-input/#options-dates-with-errors-date-input-example--form-group-before-inputs.md).   |  
| afterInputs  | object  |  Content to add after the inputs used by the date input component. [ See macro options for formGroup afterInputs](./components/date-input/#options-dates-with-errors-date-input-example--form-group-after-inputs.md).   |  
Options for formGroup `beforeInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add before the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for formGroup `afterInputs` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** HTML to add after the inputs. If `html` is provided, the `text` option will be ignored.   |  
Options for `hint` component  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** If `html` is set, this is not required. Text to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| html  | string  |  **Required.** If `text` is set, this is not required. HTML to use within the hint. If `html` is provided, the `text` option will be ignored.   |  
| id  | string  |  Optional ID attribute to add to the hint span tag.   |  
| classes  | string  |  Classes to add to the hint span tag.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the hint span tag.   |  
Copy code
```
{% from "govuk/components/date-input/macro.njk" import govukDateInput %}

{{ govukDateInput({
  id: "passport-issued",
  namePrefix: "passport-issued",
  fieldset: {
    legend: {
      text: "When was your passport issued?",
      isPageHeading: true,
      classes: "govuk-fieldset__legend--l"
    }
  },
  hint: {
    text: "For example, 27 3 2007"
  },
  errorMessage: {
    text: "The date your passport was issued must include a year"
  },
  items: [
    {
      classes: "govuk-input--width-2",
      name: "day",
      value: "6"
    },
    {
      classes: "govuk-input--width-2",
      name: "month",
      value: "3"
    },
    {
      classes: "govuk-input--width-4 govuk-input--error",
      name: "year"
    }
  ]
}) }}
```

Make sure errors follow the guidance in the [Error message component](./components/error-message.md) and have specific error messages for specific error states.
If there’s more than one error, show the highest priority error message. In order of priority, show error messages about:
  * missing or incomplete information
  * information that cannot be correct (for example, the number ‘13’ in the month field)
  * information that fails validation for another reason

#### If nothing is entered
Highlight the date input as a whole.  

Say ‘Enter [whatever it is]’. For example, ‘Enter your date of birth’.
#### If the date is incomplete
Highlight the day, month or year field where the information is missing or incomplete. If more than one field is missing information, highlight the fields the user needs to fill in.  

Say ‘[whatever it is] must include a [whatever is missing]’.  

For example, ‘Date of birth must include a month’, ‘Date of birth must include a day and month’ or ‘Year must include 4 numbers’.
#### If the date entered cannot be correct
For example, ‘13’ in the month field cannot be correct.  

Highlight the day, month or year field with the incorrect information. Or highlight the date as a whole if there’s incorrect information in more than one field, or it’s not clear which field is incorrect.  

Say ‘[Whatever it is] must be a real date’. For example, ‘Date of birth must be a real date’.
#### If the date is in the future when it needs to be in the past
Highlight the date input as a whole.  

Say ‘[whatever it is] must be in the past’. For example, ‘Date of birth must be in the past’.
#### If the date is in the future when it needs to be today or in the past
Highlight the date input as a whole.  

Say ‘[whatever it is] must be today or in the past’. For example, ‘Date of birth must be today or in the past’.
#### If the date is in the past when it needs to be in the future
Highlight the date input as a whole.  

Say ‘[whatever it is] must be in the future’. For example, ‘The date your course ends must be in the future’.
#### If the date is in the past when it needs to be today or in the future
Highlight the date input as a whole.  

Say ‘[whatever it is] must be today or in the future’. For example, ‘The date your course ends must be today or in the future’.
#### If the date must be the same as or after another date
Highlight the date input as a whole.  

Say ‘[whatever it is] must be the same as or after [date and optional description]’. For example, ‘The date your course ends must be the same as or after 1 September 2017 when you started the course’.
#### If the date must be after another date
Highlight the date input as a whole.  

Say ‘[whatever it is] must be after [date and optional description]’. For example, ‘The day your course ends must be after 1 September 2017’.
#### If the date must be the same as or before another date
Highlight the date input as a whole.  

Say ‘[whatever it is] must be the same as or before [date and optional description]’. For example, ‘The date of Gordon’s last exam must be the same as or before 31 August 2017 when they left school’.
#### If the date must be before another date
Highlight the date input as a whole.  

Say ‘[whatever it is] must be before [date and optional description]’. For example, ‘The date of Gordon’s last exam must be the same as or before 31 August 2017’.
#### If the date must be between two dates
Highlight the date input as a whole.  

Say ‘[whatever it is] must be between [date] and [date and optional description]’. For example, ‘The date your contract started must be between 1 September 2017 and 30 September 2017 when you were self-employed’.
## Research on this component
[Findings from the Apply for teacher training service](https://github.com/alphagov/govuk-design-system-backlog/issues/42#issuecomment-1119724868) showed that hundreds of users were inputting months using full or abbreviated month names and getting an error. They changed the component to accept month names to be consistent with this observed behaviour. Since changing the service the number of errors has dropped dramatically.
Some users with dyscalculia may struggle to convert month names into numbers, but accepting full or abbreviated month names may help these users.
## Help improve this component
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Date input’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/42) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/components/date-input/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./components/date-input/#top.md)
