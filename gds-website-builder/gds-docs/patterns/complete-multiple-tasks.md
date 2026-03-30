#  Help users to  Complete multiple tasks 
Help users understand:
  * the tasks involved in completing a transaction
  * the order they should complete tasks in
  * when they’ve completed tasks

[ Open this example in a new tab: task list ](./patterns/complete-multiple-tasks/default.md)
  * [HTML](./patterns/complete-multiple-tasks/#task-list-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#task-list-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-width-container">
  <main class="govuk-main-wrapper " id="main-content" role="main">
    <div class="govuk-grid-row">
      <div class="govuk-grid-column-two-thirds">
        <h1 class="govuk-heading-l">Service name</h1>
        <h2 class="govuk-heading-m">Check before you start</h2>
        <ul class="govuk-task-list">
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="before-you-start-1-status">
                Check eligibility
              </a>
            </div>
            <div class="govuk-task-list__status" id="before-you-start-1-status">
              Completed
            </div>
          </li>
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="before-you-start-2-status">
                Read declaration
              </a>
            </div>
            <div class="govuk-task-list__status" id="before-you-start-2-status">
              <strong class="govuk-tag govuk-tag--blue">
                Incomplete
              </strong>
            </div>
          </li>
        </ul>
        <h2 class="govuk-heading-m govuk-!-margin-top-5">Prepare application</h2>
        <ul class="govuk-task-list">
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="prepare-application-1-status">
                Company information
              </a>
            </div>
            <div class="govuk-task-list__status" id="prepare-application-1-status">
              Completed
            </div>
          </li>
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="prepare-application-2-status">
                Your contact details
              </a>
            </div>
            <div class="govuk-task-list__status" id="prepare-application-2-status">
              <strong class="govuk-tag govuk-tag--blue">
                Incomplete
              </strong>
            </div>
          </li>
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="prepare-application-3-status">
                List convictions
              </a>
            </div>
            <div class="govuk-task-list__status" id="prepare-application-3-status">
              Completed
            </div>
          </li>
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="prepare-application-4-status">
                Provide financial evidence
              </a>
            </div>
            <div class="govuk-task-list__status" id="prepare-application-4-status">
              <strong class="govuk-tag govuk-tag--blue">
                Incomplete
              </strong>
            </div>
          </li>
          <li class="govuk-task-list__item govuk-task-list__item--with-link">
            <div class="govuk-task-list__name-and-hint">
              <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="prepare-application-5-status">
                Give medical information
              </a>
            </div>
            <div class="govuk-task-list__status" id="prepare-application-5-status">
              <strong class="govuk-tag govuk-tag--blue">
                Incomplete
              </strong>
            </div>
          </li>
        </ul>
        <div class="govuk-button-group">
          <button type="submit" class="govuk-button" data-module="govuk-button">
            Apply
          </button>
        </div>
      </div>
    </div>
  </main>
</div>
```

Nunjucks
Copy code
```
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}
{% from "govuk/components/button/macro.njk" import govukButton %}

{% block content %}
  <div class="govuk-grid-row">
    <div class="govuk-grid-column-two-thirds">
      <h1 class="govuk-heading-l">Service name</h1>

      <h2 class="govuk-heading-m">Check before you start</h2>

      {{ govukTaskList({
        idPrefix: "before-you-start",
        items: [
          {
            title: {
              text: "Check eligibility"
            },
            href: "#",
            status: {
              text: "Completed"
            }
          },
          {
            title: {
              text: "Read declaration"
            },
            href: "#",
            status: {
              tag: {
                text: "Incomplete",
                classes: "govuk-tag--blue"
              }
            }
          }
        ]
      }) }}

      <h2 class="govuk-heading-m govuk-!-margin-top-5">Prepare application</h2>

      {{ govukTaskList({
        idPrefix: "prepare-application",
        items: [
          {
            title: {
              text: "Company information"
            },
            href: "#",
            status: {
              text: "Completed"
            }
          },
          {
            title: {
              text: "Your contact details"
            },
            href: "#",
            status: {
              tag: {
                text: "Incomplete",
                classes: "govuk-tag--blue"
              }
            }
          },
          {
            title: {
              text: "List convictions"
            },
            href: "#",
            status: {
              text: "Completed"
            }
          },
          {
            title: {
              text: "Provide financial evidence"
            },
            href: "#",
            status: {
              tag: {
                text: "Incomplete",
                classes: "govuk-tag--blue"
              }
            }
          },
          {
            title: {
              text: "Give medical information"
            },
            href: "#",
            status: {
              tag: {
                text: "Incomplete",
                classes: "govuk-tag--blue"
              }
            }
          }
        ]
      }) }}

      <div class="govuk-button-group">
        {{ govukButton({
          text: "Apply"
        }) }}
      </div>

    </div>
  </div>
{% endblock %}
```

Complete multiple tasks pages use a [Task list component](./components/task-list.md) for each group of tasks on the page.
## When to use this pattern
Only use a complete multiple tasks page for longer transactions involving multiple tasks that users may need to complete over a number of sessions.
Try to simplify the transaction before you use a complete multiple tasks page. If you’re able to reduce the number of tasks or steps involved, you might not need one.
## How it works
You should show a complete multiple tasks page:
  * at the start of the transaction
  * at the start of each returning session

If you use a complete multiple tasks page in your service, you’ll need to:
  * group related actions into tasks
  * show the status of the tasks

If there are lots of tasks to complete, you might also need to group them further into steps.
### Show related actions as a task
Summarise a set of related activities and questions into a task, for example, ‘Provide financial evidence’ and ‘Give medical information’. This will help users understand and plan what they need to do.
Where possible, task names should:
  * describe what the task or activity will involve
  * start with verbs, for example, ‘check’, ‘declare’, ‘report’

### Show the status of the tasks
Make it clear to users which tasks they’ve completed and which still need their attention, by labelling them using statuses.
[ Open this example in a new tab: task list statuses example ](./patterns/complete-multiple-tasks/task-list-statuses.md)
  * [HTML](./patterns/complete-multiple-tasks/#task-list-statuses-example-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#task-list-statuses-example-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-grid-row">
  <div class="govuk-grid-column-two-thirds">
    <ul class="govuk-task-list">
      <li class="govuk-task-list__item govuk-task-list__item--with-link">
        <div class="govuk-task-list__name-and-hint">
          <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="task-list-1-status">
            Company information
          </a>
        </div>
        <div class="govuk-task-list__status" id="task-list-1-status">
          Completed
        </div>
      </li>
      <li class="govuk-task-list__item govuk-task-list__item--with-link">
        <div class="govuk-task-list__name-and-hint">
          <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="task-list-2-status">
            Your contact details
          </a>
        </div>
        <div class="govuk-task-list__status" id="task-list-2-status">
          <strong class="govuk-tag govuk-tag--blue">
            Incomplete
          </strong>
        </div>
      </li>
      <li class="govuk-task-list__item govuk-task-list__item--with-link">
        <div class="govuk-task-list__name-and-hint">
          <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="task-list-3-status">
            List convictions
          </a>
        </div>
        <div class="govuk-task-list__status" id="task-list-3-status">
          <strong class="govuk-tag govuk-tag--blue">
            Incomplete
          </strong>
        </div>
      </li>
    </ul>
  </div>
</div>
```

Nunjucks
Copy code
```
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}

<div class="govuk-grid-row">
  <div class="govuk-grid-column-two-thirds">

    {{ govukTaskList({
      items: [
        {
          title: {
            text: "Company information"
          },
          href: "#",
          status: {
            text: "Completed"
          }
        },
        {
          title: {
            text: "Your contact details"
          },
          href: "#",
          status: {
            tag: {
              text: "Incomplete",
              classes: "govuk-tag--blue"
            }
          }
        },
        {
          title: {
            text: "List convictions"
          },
          href: "#",
          status: {
            tag: {
              text: "Incomplete",
              classes: "govuk-tag--blue"
            }
          }
        }
      ]
    }) }}

  </div>
</div>
```

Statuses should be helpful to users. The more you add, the harder it is for users to remember them. Start with the smallest number of different statuses you think might work, for example ‘Completed’ and ‘Incomplete’, then add more if your user research shows there’s a need for them.
Once the user has completed the task, the status should show as ‘Completed’ and be black text with no background colour. This will draw more attention to tasks that require action.
#### Tasks that are in progress
You may find you need additional statuses if your user research shows that users want to be able to distinguish between the tasks they haven’t started at all, and those they’ve started but not completed.
In this instance, instead of ‘Incomplete’, you may want to use ‘Not yet started’ to show which tasks they are yet to start. You should then use ‘In progress’ for tasks they have started but are yet to complete.
Different colours may be used to further differentiate between tags.
[ Open this example in a new tab: task list in progress ](./components/task-list/in-progress.md)
  * [HTML](./patterns/complete-multiple-tasks/#task-list-in-progress-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#task-list-in-progress-example-nunjucks.md)

HTML
Copy code
```
<ul class="govuk-task-list">
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-1-status">
        Contact details
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-1-status">
      Completed
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-2-status">
        Work history
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-2-status">
      <strong class="govuk-tag govuk-tag--teal">
        In progress
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-3-status">
        Qualifications
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-3-status">
      <strong class="govuk-tag govuk-tag--blue">
        Not yet started
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-4-status">
        Supporting statement
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-4-status">
      <strong class="govuk-tag govuk-tag--blue">
        Not yet started
      </strong>
    </div>
  </li>
</ul>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items for each task within the task list component. [ See macro options for items](./patterns/complete-multiple-tasks/#options-task-list-in-progress-example--items.md).   |  
| classes  | string  |  Classes to add to the `ul` container for the task list.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the `ul` container for the task list.   |  
| idPrefix  | string  |  Optional prefix. This is used to prefix the `id` attribute for the task list item tag and hint, separated by `-`. Defaults to `"task-list"`.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  **Required.** The main title for the task within the task list component. [ See macro options for items title](./patterns/complete-multiple-tasks/#options-task-list-in-progress-example--items-title.md).   |  
| hint  | object  |  Can be used to add a hint to each task within the task list component. [ See macro options for items hint](./patterns/complete-multiple-tasks/#options-task-list-in-progress-example--items-hint.md).   |  
| status  | object  |  **Required.** The status for each task within the task list component. [ See macro options for items status](./patterns/complete-multiple-tasks/#options-task-list-in-progress-example--items-status.md).   |  
| href  | string  |  The value of the link’s `href` attribute for the task list item.   |  
| classes  | string  |  Classes to add to the item `div`.   |  
Options for items `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for items `hint` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
Options for items `status` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| tag  | object  |  Can be used to add a tag to the status of the task within the task list component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| text  | string  |  Text to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| html  | string  |  HTML to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the status container.   |  
Copy code
```
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}

{{ govukTaskList({
  idPrefix: "application-details",
  items: [
    {
      title: {
        text: "Contact details"
      },
      href: "#",
      status: {
        text: "Completed"
      }
    },
    {
      title: {
        text: "Work history"
      },
      href: "#",
      status: {
        tag: {
          text: "In progress",
          classes: "govuk-tag--teal"
        }
      }
    },
    {
      title: {
        text: "Qualifications"
      },
      href: "#",
      status: {
        tag: {
          text: "Not yet started",
          classes: "govuk-tag--blue"
        }
      }
    },
    {
      title: {
        text: "Supporting statement"
      },
      href: "#",
      status: {
        tag: {
          text: "Not yet started",
          classes: "govuk-tag--blue"
        }
      }
    }
  ]
}) }}
```

#### Tasks that cannot yet be started
If the user cannot start the task yet, for example because another task must be completed first, use the ‘Cannot start yet’ status. This should be grey text with no background colour, and the ‘task row’ should not be linked.
[ Open this example in a new tab: task list with cannot start yet ](./components/task-list/cannot-start-yet.md)
  * [HTML](./patterns/complete-multiple-tasks/#task-list-with-cannot-start-yet-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#task-list-with-cannot-start-yet-example-nunjucks.md)

HTML
Copy code
```
<ul class="govuk-task-list">
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-1-status">
        Company details
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-1-status">
      Completed
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-2-status">
        Project details
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-2-status">
      <strong class="govuk-tag govuk-tag--blue">
        Incomplete
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item">
    <div class="govuk-task-list__name-and-hint">
      <div>
        Fund applied to
      </div>
      <div id="application-details-3-hint" class="govuk-task-list__hint">
        The funds will be announced on 1 April 2022
      </div>
    </div>
    <div class="govuk-task-list__status govuk-task-list__status--cannot-start-yet" id="application-details-3-status">
      Cannot start yet
    </div>
  </li>
</ul>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items for each task within the task list component. [ See macro options for items](./patterns/complete-multiple-tasks/#options-task-list-with-cannot-start-yet-example--items.md).   |  
| classes  | string  |  Classes to add to the `ul` container for the task list.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the `ul` container for the task list.   |  
| idPrefix  | string  |  Optional prefix. This is used to prefix the `id` attribute for the task list item tag and hint, separated by `-`. Defaults to `"task-list"`.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  **Required.** The main title for the task within the task list component. [ See macro options for items title](./patterns/complete-multiple-tasks/#options-task-list-with-cannot-start-yet-example--items-title.md).   |  
| hint  | object  |  Can be used to add a hint to each task within the task list component. [ See macro options for items hint](./patterns/complete-multiple-tasks/#options-task-list-with-cannot-start-yet-example--items-hint.md).   |  
| status  | object  |  **Required.** The status for each task within the task list component. [ See macro options for items status](./patterns/complete-multiple-tasks/#options-task-list-with-cannot-start-yet-example--items-status.md).   |  
| href  | string  |  The value of the link’s `href` attribute for the task list item.   |  
| classes  | string  |  Classes to add to the item `div`.   |  
Options for items `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for items `hint` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
Options for items `status` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| tag  | object  |  Can be used to add a tag to the status of the task within the task list component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| text  | string  |  Text to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| html  | string  |  HTML to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the status container.   |  
Copy code
```
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}

{{ govukTaskList({
  idPrefix: "application-details",
  items: [
    {
      title: {
        text: "Company details"
      },
      href: "#",
      status: {
        text: "Completed"
      }
    },
    {
      title: {
        text: "Project details"
      },
      href: "#",
      status: {
        tag: {
          text: "Incomplete",
          classes: "govuk-tag--blue"
        }
      }
    },
    {
      title: {
        text: "Fund applied to"
      },
      hint: {
        text: "The funds will be announced on 1 April 2022"
      },
      status: {
        text: "Cannot start yet",
        classes: "govuk-task-list__status--cannot-start-yet"
      }
    }
  ]
}) }}
```

#### Tasks containing an error
You should avoid tasks having an error status by using the [Error summary component](./components/error-summary.md) and [Error message component](./components/error-message.md) displayed at the point that the error is made, so that the user can fix it straight away.
If it is unavoidable that a task may end up saved but containing an error, use the status text ‘There is a problem’ and a red background.
Do not use the red background colour for any status text except errors.
[ Open this example in a new tab: task list with an error ](./components/task-list/error.md)
  * [HTML](./patterns/complete-multiple-tasks/#task-list-with-an-error-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#task-list-with-an-error-example-nunjucks.md)

HTML
Copy code
```
<ul class="govuk-task-list">
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-1-status">
        Contact details
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-1-status">
      Completed
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-2-status">
        Project details
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-2-status">
      <strong class="govuk-tag govuk-tag--blue">
        Incomplete
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-3-status">
        Funding required
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-3-status">
      <strong class="govuk-tag govuk-tag--red">
        There is a problem
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="application-details-4-status">
        Bank account
      </a>
    </div>
    <div class="govuk-task-list__status" id="application-details-4-status">
      Completed
    </div>
  </li>
</ul>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items for each task within the task list component. [ See macro options for items](./patterns/complete-multiple-tasks/#options-task-list-with-an-error-example--items.md).   |  
| classes  | string  |  Classes to add to the `ul` container for the task list.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the `ul` container for the task list.   |  
| idPrefix  | string  |  Optional prefix. This is used to prefix the `id` attribute for the task list item tag and hint, separated by `-`. Defaults to `"task-list"`.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  **Required.** The main title for the task within the task list component. [ See macro options for items title](./patterns/complete-multiple-tasks/#options-task-list-with-an-error-example--items-title.md).   |  
| hint  | object  |  Can be used to add a hint to each task within the task list component. [ See macro options for items hint](./patterns/complete-multiple-tasks/#options-task-list-with-an-error-example--items-hint.md).   |  
| status  | object  |  **Required.** The status for each task within the task list component. [ See macro options for items status](./patterns/complete-multiple-tasks/#options-task-list-with-an-error-example--items-status.md).   |  
| href  | string  |  The value of the link’s `href` attribute for the task list item.   |  
| classes  | string  |  Classes to add to the item `div`.   |  
Options for items `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for items `hint` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
Options for items `status` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| tag  | object  |  Can be used to add a tag to the status of the task within the task list component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| text  | string  |  Text to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| html  | string  |  HTML to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the status container.   |  
Copy code
```
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}

{{ govukTaskList({
  idPrefix: "application-details",
  items: [
    {
      title: {
        text: "Contact details"
      },
      href: "#",
      status: {
        text: "Completed"
      }
    },
    {
      title: {
        text: "Project details"
      },
      href: "#",
      status: {
        tag: {
          text: "Incomplete",
          classes: "govuk-tag--blue"
        }
      }
    },
    {
      title: {
        text: "Funding required"
      },
      href: "#",
      status: {
        tag: {
          text: "There is a problem",
          classes: "govuk-tag--red"
        }
      }
    },
    {
      title: {
        text: "Bank account"
      },
      href: "#",
      status: {
        text: "Completed"
      }
    }
  ]
}) }}
```

#### Status text
Although we recommend using consistent wording across task lists, you can change it if research shows that different text is more suitable to your service or users.
If you are creating your own statuses, use adjectives rather than verbs. Use sentence case, and keep it short, so that it can be easily read and understood.
#### Additional statuses
If your user research shows that there is a need for additional status tags, you can use other colours to help distinguish between them.
[ Open this example in a new tab: task list with all colours ](./components/task-list/all-colours.md)
  * [HTML](./patterns/complete-multiple-tasks/#task-list-with-all-colours-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#task-list-with-all-colours-example-nunjucks.md)

HTML
Copy code
```
<ul class="govuk-task-list">
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-1-status">
        Task A
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-1-status">
      <strong class="govuk-tag govuk-tag--grey">
        Grey
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-2-status">
        Task B
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-2-status">
      <strong class="govuk-tag govuk-tag--green">
        Green
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-3-status">
        Task C
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-3-status">
      <strong class="govuk-tag govuk-tag--teal">
        Teal
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-4-status">
        Task D
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-4-status">
      <strong class="govuk-tag govuk-tag--blue">
        Blue
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-5-status">
        Task E
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-5-status">
      <strong class="govuk-tag govuk-tag--purple">
        Purple
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-6-status">
        Task F
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-6-status">
      <strong class="govuk-tag govuk-tag--magenta">
        Magenta
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-7-status">
        Task G
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-7-status">
      <strong class="govuk-tag govuk-tag--orange">
        Orange
      </strong>
    </div>
  </li>
  <li class="govuk-task-list__item govuk-task-list__item--with-link">
    <div class="govuk-task-list__name-and-hint">
      <a class="govuk-link govuk-task-list__link" href="#" aria-describedby="all-colours-8-status">
        Task H
      </a>
    </div>
    <div class="govuk-task-list__status" id="all-colours-8-status">
      <strong class="govuk-tag govuk-tag--yellow">
        Yellow
      </strong>
    </div>
  </li>
</ul>
```

Nunjucks
Nunjucks macro options
Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. 
Some options are required for the macro to work; these are marked as “Required” in the option description. Deprecated options are marked as “Deprecated”. 
If you’re using Nunjucks macros in production with “html” options, or ones ending with “html”, you must sanitise the HTML to protect against [cross-site scripting exploits](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).   
Primary options  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| items  | array  |  **Required.** The items for each task within the task list component. [ See macro options for items](./patterns/complete-multiple-tasks/#options-task-list-with-all-colours-example--items.md).   |  
| classes  | string  |  Classes to add to the `ul` container for the task list.   |  
| attributes  | object  |  HTML attributes (for example data attributes) to add to the `ul` container for the task list.   |  
| idPrefix  | string  |  Optional prefix. This is used to prefix the `id` attribute for the task list item tag and hint, separated by `-`. Defaults to `"task-list"`.   |  
Options for `items` array objects  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| title  | object  |  **Required.** The main title for the task within the task list component. [ See macro options for items title](./patterns/complete-multiple-tasks/#options-task-list-with-all-colours-example--items-title.md).   |  
| hint  | object  |  Can be used to add a hint to each task within the task list component. [ See macro options for items hint](./patterns/complete-multiple-tasks/#options-task-list-with-all-colours-example--items-hint.md).   |  
| status  | object  |  **Required.** The status for each task within the task list component. [ See macro options for items status](./patterns/complete-multiple-tasks/#options-task-list-with-all-colours-example--items-status.md).   |  
| href  | string  |  The value of the link’s `href` attribute for the task list item.   |  
| classes  | string  |  Classes to add to the item `div`.   |  
Options for items `title` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the title. If `html` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the title wrapper.   |  
Options for items `hint` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| text  | string  |  **Required.** Text to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
| html  | string  |  **Required.** HTML to use within the hint. If `html` is provided, the `text` argument will be ignored.   |  
Options for items `status` object  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| tag  | object  |  Can be used to add a tag to the status of the task within the task list component. [See macro options for tag](./components/tag/#options-tag-example.md).   |  
| text  | string  |  Text to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| html  | string  |  HTML to use for the status, as an alternative to using a tag. If `html` or `tag` is provided, the `text` argument will be ignored.   |  
| classes  | string  |  Classes to add to the status container.   |  
Copy code
```
{% from "govuk/components/task-list/macro.njk" import govukTaskList %}

{{ govukTaskList({
  idPrefix: "all-colours",
  items: [
    {
      title: {
        text: "Task A"
      },
      href: "#",
      status: {
        tag: {
          text: "Grey",
          classes: "govuk-tag--grey"
        }
      }
    },
    {
      title: {
        text: "Task B"
      },
      href: "#",
      status: {
        tag: {
          text: "Green",
          classes: "govuk-tag--green"
        }
      }
    },
    {
      title: {
        text: "Task C"
      },
      href: "#",
      status: {
        tag: {
          text: "Teal",
          classes: "govuk-tag--teal"
        }
      }
    },
    {
      title: {
        text: "Task D"
      },
      href: "#",
      status: {
        tag: {
          text: "Blue",
          classes: "govuk-tag--blue"
        }
      }
    },
    {
      title: {
        text: "Task E"
      },
      href: "#",
      status: {
        tag: {
          text: "Purple",
          classes: "govuk-tag--purple"
        }
      }
    },
    {
      title: {
        text: "Task F"
      },
      href: "#",
      status: {
        tag: {
          text: "Magenta",
          classes: "govuk-tag--magenta"
        }
      }
    },
    {
      title: {
        text: "Task G"
      },
      href: "#",
      status: {
        tag: {
          text: "Orange",
          classes: "govuk-tag--orange"
        }
      }
    },
    {
      title: {
        text: "Task H"
      },
      href: "#",
      status: {
        tag: {
          text: "Yellow",
          classes: "govuk-tag--yellow"
        }
      }
    }
  ]
}) }}
```

### Group tasks into steps
If your transaction involves lots of tasks, make it manageable by splitting it up into steps that represent stages in the process.
For example, you could group all tasks which help users find out if your service is right for them in a step called ‘Check before you start’.
Where possible, allow users to complete tasks in any order. This will help them plan their time and complete sections as and when they can.
### Marking tasks as completed
Sometimes, it’s better to let the user decide when a task is completed.
This can be helpful when a task involves:
  * some questions that are optional
  * writing a long answer (such as in a [Textarea component](./components/textarea.md))
  * looking up information, such as details about previous jobs
  * answers that need to be checked carefully with someone else

Do this by asking a radio question at the end of the task – either as the last question (if the task is a single page) or on the [Check answers page](./patterns/check-answers.md) (if the task involves more than one page).
Ask ‘Have you completed this section?’ with the radio options ‘Yes, I’ve completed this section’ or ‘No, I’ll come back later’.
If the user selects ‘No, I’ll come back to it later,’ mark the task as ‘Incomplete’ or ‘In progress’.
If the user selects ‘Yes, I’ve completed this section,’ mark the task as ‘Completed’.
[ Open this example in a new tab: have you completed this section – task list pages ](./patterns/complete-multiple-tasks/have-you-completed-this-section.md)
  * [HTML](./patterns/complete-multiple-tasks/#have-you-completed-this-section-task-list-pages-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#have-you-completed-this-section-task-list-pages-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group">
  <fieldset class="govuk-fieldset">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--m">
      Have you completed this section?
    </legend>
    <div class="govuk-radios" data-module="govuk-radios">
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="haveYouCompletedThisSection" name="haveYouCompletedThisSection" type="radio" value="yes">
        <label class="govuk-label govuk-radios__label" for="haveYouCompletedThisSection">
          Yes, I’ve completed this section
        </label>
      </div>
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="haveYouCompletedThisSection-2" name="haveYouCompletedThisSection" type="radio" value="no">
        <label class="govuk-label govuk-radios__label" for="haveYouCompletedThisSection-2">
          No, I’ll come back to it later
        </label>
      </div>
    </div>
  </fieldset>
</div>
<button type="submit" class="govuk-button" data-module="govuk-button">
  Continue
</button>
```

Nunjucks
Copy code
```
{% from "govuk/components/button/macro.njk" import govukButton %}
{% from "govuk/components/radios/macro.njk" import govukRadios %}

{{ govukRadios({
  name: "haveYouCompletedThisSection",
  fieldset: {
    legend: {
      text: "Have you completed this section?",
      isPageHeading: false,
      classes: "govuk-fieldset__legend--m"
    }
  },
  items: [
    {
      value: "yes",
      text: "Yes, I’ve completed this section"
    },
    {
      value: "no",
      text: "No, I’ll come back to it later"
    }
  ]
}) }}

{{ govukButton({
  text: "Continue"
}) }}
```

Always allow users to go back into a task to change their answer.
#### Error messages
If the user does not select an option, show an [Error message component](./components/error-message.md) to say: ‘Select whether you’ve completed this section’.
[ Open this example in a new tab: have you completed this section error – task list pages ](./patterns/complete-multiple-tasks/have-you-completed-this-section-error.md)
  * [HTML](./patterns/complete-multiple-tasks/#have-you-completed-this-section-error-task-list-pages-example-html.md)
  * [Nunjucks](./patterns/complete-multiple-tasks/#have-you-completed-this-section-error-task-list-pages-example-nunjucks.md)

HTML
Copy code
```
<div class="govuk-form-group govuk-form-group--error">
  <fieldset class="govuk-fieldset" aria-describedby="haveYouCompletedThisSectionError-error">
    <legend class="govuk-fieldset__legend govuk-fieldset__legend--m">
      Have you completed this section?
    </legend>
    <p id="haveYouCompletedThisSectionError-error" class="govuk-error-message">
      <span class="govuk-visually-hidden">Error:</span> Select whether you&#39;ve completed this section
    </p>
    <div class="govuk-radios" data-module="govuk-radios">
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="haveYouCompletedThisSectionError" name="haveYouCompletedThisSectionError" type="radio" value="yes">
        <label class="govuk-label govuk-radios__label" for="haveYouCompletedThisSectionError">
          Yes, I’ve completed this section
        </label>
      </div>
      <div class="govuk-radios__item">
        <input class="govuk-radios__input" id="haveYouCompletedThisSectionError-2" name="haveYouCompletedThisSectionError" type="radio" value="no">
        <label class="govuk-label govuk-radios__label" for="haveYouCompletedThisSectionError-2">
          No, I’ll come back to it later
        </label>
      </div>
    </div>
  </fieldset>
</div>
<button type="submit" class="govuk-button" data-module="govuk-button">
  Continue
</button>
```

Nunjucks
Copy code
```
{% from "govuk/components/button/macro.njk" import govukButton %}
{% from "govuk/components/radios/macro.njk" import govukRadios %}

{{ govukRadios({
  name: "haveYouCompletedThisSectionError",
  fieldset: {
    legend: {
      text: "Have you completed this section?",
      isPageHeading: false,
      classes: "govuk-fieldset__legend--m"
    }
  },
  errorMessage: {
    text: "Select whether you've completed this section"
  },
  items: [
    {
      value: "yes",
      text: "Yes, I’ve completed this section"
    },
    {
      value: "no",
      text: "No, I’ll come back to it later"
    }
  ]
}) }}

{{ govukButton({
  text: "Continue"
}) }}
```

## Research on this pattern
This pattern was previously named ‘Task list’ and was [developed by a team at the Government Digital Service (GDS)](https://designnotes.blog.gov.uk/2017/04/04/weve-published-the-task-list-pattern/).
It was then iterated by a cross-government collaboration and published as a new [Task list component](./components/task-list.md) with updated guidance and research.
See the [research on the Task list component](./components/task-list#research-on-this-component.md) for details of research done, and known issues and gaps.
## Help improve this pattern
To help make sure that this page is useful, relevant and up to date, you can: 
  * take part in the [ ‘Complete multiple tasks’ discussion on GitHub ](https://github.com/alphagov/govuk-design-system-backlog/issues/72) and share your research 
  * [propose a change on GitHub](https://github.com/alphagov/govuk-design-system/edit/main/src/patterns/complete-multiple-tasks/index.md) – read more about [ how to propose changes in GitHub ](./community/propose-a-content-change-using-github.md)

## Need help?
If you’ve got a question about the GOV.UK Design System, [contact the team](./contact.md). 
[ ](./patterns/complete-multiple-tasks/#top.md)
