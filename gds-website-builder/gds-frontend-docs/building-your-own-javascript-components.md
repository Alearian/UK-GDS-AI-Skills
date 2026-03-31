#  [](./building-your-own-javascript-components/#building-your-own-javascript-components.md)Building your own JavaScript components
To help you build and initialise your own JavaScript components, GOV.UK Frontend provides some of its internal features for you to reuse:
  * a [`Component` class](./building-your-own-javascript-components/#using-the-component-class.md) that handles common logistics across components
  * a [`createAll` function](./building-your-own-javascript-components/#using-createall-with-your-components.md) that can initialise both GOV.UK Frontend and your own components
  * an [`isSupported` function](./building-your-own-javascript-components/#checking-for-gov-uk-frontend-support-with-issupported.md) that checks if GOV.UK Frontend is supported

Using GOV.UK Frontend’s features means you will not have to redevelop these features yourself, and it reduces the size of the [bundled JavaScript](./import-javascript/#import-javascript-using-a-bundler.md).
##  [](./building-your-own-javascript-components/#using-the-component-class.md)Using the `Component` class
JavaScript components in GOV.UK Frontend share a number of behaviours. They:
  * check that GOV.UK Frontend is supported
  * check that the component is not already initialised on its root element
  * store the root element of the component

The `Component` class implements these behaviours in an extensible way, so you can write code for your component that focuses on its specific behaviour.
###  [](./building-your-own-javascript-components/#defining-static-properties-on-components.md)Defining static properties on components
Some of the `Component`’s features are supported by static properties on the component that inherit from it. However, native static properties are not a JavaScript syntax supported by all [browsers that support `<script type="module">`](./import-javascript/#import-javascript.md).
If your project’s tools are able to convert the syntax to code supported by browsers that support `<script type="module">`, you can write these properties as native static ones in your component’s class:

```
class MyComponent extends Component {
  static property = 'value'
}

```

Otherwise, you can add these properties to your component’s class after its definition:

```
class MyComponent extends Component {}
MyComponent.property = 'value'

```

###  [](./building-your-own-javascript-components/#defining-the-modulename-property.md)Defining the `moduleName` property
Components extending the `Component` class need to define a `moduleName` [static property](./building-your-own-javascript-components/#defining-static-properties-on-components.md):

```
class MyComponent extends Component {
  static moduleName = 'app-my-component'
}

```

Doing this helps:
  * [`createAll` initialise the component](./building-your-own-javascript-components/#using-createall-with-your-components.md)
  * support consistent error messaging

###  [](./building-your-own-javascript-components/#customising-initialisation-of-components.md)Customising initialisation of components
When your component is initialised, it’ll need to perform some tasks, such as adding event listeners. You can add these tasks to your component’s `constructor` after calling `super` to set up the base `Component`’s default behaviour.

```
class MyComponent extends Component {
  static moduleName = 'app-my-component'

  constructor($root) {
    super($root)

    // Run component specific initialisation here for example
    this.$root.addEventListener('click', this.handleClick.bind(this))
  }

  handleClick(event) {
    // Handle click inside the component’s root
  }
}

```

###  [](./building-your-own-javascript-components/#accessing-the-root-element-in-the-component.md)Accessing the root element in the component
Within the component’s methods and its constructor, you can access the root element that the component was initialised on using `this.$root`.

```
class MyComponent extends Component {
  static moduleName = 'app-my-component'

  constructor($root) {
    super($root)

    // Run component specific initialisation here, for example:
    this.$root.addEventListener('click', this.handleClick.bind(this))
  }

  handleClick(event) {
    this.$root.classList.add('app-my-component--clicked')
  }
}

```

####  [](./building-your-own-javascript-components/#customising-the-expected-type-of-the-root-element.md)Customising the expected type of the root element
The `Component` class will verify that the root element is of the right type (by default, `HTMLElement`). You can set an `elementType` [static property](./building-your-own-javascript-components/#defining-static-properties-on-components.md) on your component to define a specific type to check against:

```
/**
 * @extends Component<HTMLAnchorElement> 
 */
class LinkEnhancement extends Component {
  static moduleName = 'app-link-enhancement'

  // This will make sure that the component can only be initialised
  // on HTMLAnchorElement
  static elementType = HTMLAnchorElement

  constructor($root) {
    super($root);

    // this.$root is an `HTMLAnchorElement` and you can access specific properties
    // like `href` or `hash`
  }
}

```

####  [](./building-your-own-javascript-components/#using-this-root-with-typescript.md)Using `this.$root` with TypeScript
As `govuk-frontend` does not provide type definitions in its package, TypeScript might show the following error message:
"Property ‘$root’ does not exist on type <NAME_OF_YOUR_CLASS>."
You can work around this issue by adding the following [shorthand ambient module declaration](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#shorthand-ambient-module-declarations) in a `.d.ts` file in your project (for example, `govuk-frontend.d.ts`) and making sure its path is included in your `tsconfig.json` or `jsconfig.json` file.

```
declare module 'govuk-frontend';

```

If you’re interested in better TypeScript support for GOV.UK Frontend, let us know on the GitHub issue for [exporting type declarations](https://github.com/alphagov/govuk-frontend/issues/2835).
###  [](./building-your-own-javascript-components/#customising-how-support-is-checked.md)Customising how support is checked
The `Component` class will check that GOV.UK Frontend is supported during initialisation. However, your component may have different requirements for running properly. For example, it may require specific JavaScript APIs that are not supported by all browsers.
You can redefine the static `checkSupport` method so the component throws an error if these requirements are not met. We recommend adding [the component’s `moduleName`](./building-your-own-javascript-components/#defining-the-modulename-property.md) to help error messages identify which component they relate to without having to search their stack trace.

```
class MyComponent extends Component {
  static moduleName = 'app-my-component'

  static checkSupport() {
    // Run the same checks as the `Component` class
    Component.checkSupport()

    // Check for support of the native clipboard API
    if (!navigator.clipboard) {
      throw new Error('Clipboard API not supported')    
    }
  }
}

```

##  [](./building-your-own-javascript-components/#using-createall-with-your-components.md)Using `createAll` with your components
Use the `createAll` function to initialise your components [the same way GOV.UK Frontend components are initialised](./import-javascript/#import-individual-components.md). The function will look up all the HTML elements on which a given component should be initialised and initialise a component for each of them.

```
import { createAll } from 'govuk-frontend'
import { ProjectComponent, OtherProjectComponent } from './project-components.js'

createAll(ProjectComponent)

// You can provide a config for components that use them
createAll(OtherProjectComponent, {
  anOption: 'itsValue'
})

```

The `createAll` function also lets you:
  * [only search a specific part of the page for elements](./building-your-own-javascript-components/#initialise-only-on-part-of-a-page.md) , such as after adding new content with JavaScript
  * [respond to errors during components initialisation](./building-your-own-javascript-components/#handling-initialisation-errors.md), such as sending them to an error reporting service

To avoid reimplementing features shared across components, we recommend that your components extend [our `Component` class](./building-your-own-javascript-components/#using-the-component-class.md). However, you can choose not to do this. The only requirements for a component to be used with `createAll` are:
  * a [`moduleName` static property](./building-your-own-javascript-components/#defining-the-modulename-property.md)
  * a constructor expecting an HTML element as a first parameter and any necessary configuration options as a second parameter

###  [](./building-your-own-javascript-components/#initialise-only-on-part-of-a-page.md)Initialise only on part of a page
By default, `createAll` looks through the whole page for elements to initialise the components on. If you update a page with new markup, like a modal dialog box, you can initialise components on that part of the page only.

```
import { createAll } from 'govuk-frontend'
import { ProjectComponent } from './project-component.js'

const $element = document.querySelector('.app-dialog')

createAll(ProjectComponent, {SOME_CONFIGURATION}, $element)

// If the component does not need any configuration, pass `undefined` for the configuration
createAll(ProjectComponent, undefined, $element)

```

###  [](./building-your-own-javascript-components/#handling-initialisation-errors.md)Handling initialisation errors
By default, both `createAll` and `initAll` catch errors thrown by components during their initialisation and log them in the console. This makes sure components further down the page still get initialised after an error. You may still want to respond to errors as the components initialise, such as by notifying an error monitoring service, without [manually initialising each component](./import-javascript/#import-individual-components.md).
To respond to errors being thrown while components are being initialised you can use a function as the third argument to `createAll` or the `{ onError }` option for `initAll`. If a component throws an error, the function will be called and will receive:
  * the error that was thrown
  * an object with some more context

The context object will contain the following properties:
  * `component`: The component class being initialised
  * `element`: The element the component is being initialised on
  * `config`: The configuration used for initialisation

```
import { createAll } from 'govuk-frontend'
import { ProjectComponent } from './project-component.js'

function notifyErrorMonitoringService(error, { component, element, config }) {
  // Send relevant details to an error monitoring service
}

createAll(
  ProjectComponent,
  { SOME_CONFIGURATION },
  notifyErrorMonitoringService
)

// If you don’t need any configuration, pass `undefined` for the configuration
createAll(ProjectComponent, undefined, notifyErrorMonitoringService)

```

If you need to [initialise only on part of the page](./building-your-own-javascript-components/#initialise-only-on-part-of-a-page.md) and respond to errors, you can pass an object in that third argument with the following properties:
  * `scope`: The element within which to look for components to initialise
  * `onError`: The callback for responding to errors

```
import { createAll } from 'govuk-frontend'
import { ProjectComponent } from './project-component.js'

const $element = document.querySelector('.app-dialog')

function notifyErrorMonitoringService(error, { component, element, config }) {
  // Do something with initialisation error, like sending relevant details to an error monitoring service
}

createAll(ProjectComponent, {SOME_CONFIGURATION}, {
  scope: $element,
  onError: notifyErrorMonitoringService
})

// If you don’t need any configuration, pass `undefined` for the configuration
createAll(ProjectComponent, undefined, {
  scope: $element,
  onError: notifyErrorMonitoringService
})

```

##  [](./building-your-own-javascript-components/#building-configurable-components.md)Building configurable components
The component you’re building may need some configuration to get the information it needs to:
  * work correctly
  * adapt its behaviour
  * customise the messages JavaScript will show to users

Components that need configuration can extend the `ConfigurableComponent` class. This class accepts configuration from the following sources:
  * defaults defined as a `defaults` [static property](./building-your-own-javascript-components/#defining-static-properties-on-components.md) on the component’s class
  * configuration passed as second argument to the component’s constructor or [`createAll`](./building-your-own-javascript-components/#using-createall-with-your-components.md)
  * data attributes on the root element of the component

These are the same sources as those used by GOV.UK Frontend components. Configuration options from these sources are merged into a single configuration object by the `ConfigurableComponent` class. Note that:
  * configuration options passed to the constructor will override any defaults
  * data attribute values have highest precedence and will override any configuration set elsewhere

Your component will then be able to:
  * [access the merged configuration](./building-your-own-javascript-components/#accessing-the-component-s-configuration.md) using `this.config`
  * use [the`Component` class](./building-your-own-javascript-components/#using-the-component-class.md) features

###  [](./building-your-own-javascript-components/#setting-a-default-configuration-for-your-component.md)Setting a default configuration for your component
The `defaults` static property stores an object that associates option names and their default values. Default values can be any [JavaScript data type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures).
These values can be JavaScript objects, nested as deeply as necessary. We recommend including options for which the default value is `false`, `null` or `undefined`. Including these options clarifies what the component expects and provides this information to TypeScript, if you use it.

```
import { ConfigurableComponent } from 'govuk-frontend'

class MyComponent extends ConfigurableComponent {
  /* … */

  static defaults = {
    anOption: 1,
    anOptionWithNesting: {
      aNestedOption: 'itsValue',
      anotherLevel: {
        aDeeplyNestedOption: true
      }
    }
  }

  /* … */
}

```

To avoid unexpected changes to the component’s default configuration, we recommend you treat the `defaults` property as read-only in your code and use [`createAll`](./building-your-own-javascript-components/#using-createall-with-your-components.md) to configure multiple components simultaneously.
###  [](./building-your-own-javascript-components/#receiving-configuration-during-initialisation.md)Receiving configuration during initialisation
During initialisation, configurable components can receive an object as a second argument to define specific configuration options, either when using `createAll` or instantiating the components manually. This object should only define the options that need to differ from the defaults.
Use `super` to forward the argument received in the component’s constructor to the constructor of `ConfigurableComponent`, along with the root element. After you’ve done that, you can run the [initialisation tasks specific to your component](./building-your-own-javascript-components/#customising-initialisation-of-components.md):

```
import { ConfigurableComponent } from 'govuk-frontend'

class MyComponent extends ConfigurableComponent {
  /* … */

  static defaults = {
    anOption: 1,
    anOptionWithNesting: {
      aNestedOption: 'itsValue',
      anotherLevel: {
        aDeeplyNestedOption: true
      }
    }
  }

  constructor(root, config) {
    super(root, config)

    // Run custom initialisation code here
  }

  /* … */
}

createAll(MyComponent, {
   // This will only override the value for `anOptionWithNesting.aNestedOption`
   // both `anOption` and `anOptionWithNesting.anotherLevel.aDeeplyNestedOption`
   // will keep the values defined in the component’s `defaults`
   anOptionWithNesting: {
    aNestedOption: 'aNewValue'
   }
})

```

###  [](./building-your-own-javascript-components/#receiving-configuration-from-data-attributes.md)Receiving configuration from data attributes
####  [](./building-your-own-javascript-components/#naming-convention-for-data-attributes.md)Naming convention for data attributes
To compute the name of the attribute from the name of the option in the component’s `defaults`, you need to convert the `camelCase` name to a dash (`-`) separated name, following the [steps used by the `dataset` DOM API](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset#camelcase). For example: `anOption` becomes `data-an-option`.
For nested configuration options, use dots (`.`) to separate the names of each level of nesting. For example, to set `aDeeplyNestedOption` in the component from the previous example (which sits within `anotherLevel` inside `anOptionWithNesting`), the attribute name would be `data-an-option-with-nesting.another-level.a-deeply-nested-option`.
####  [](./building-your-own-javascript-components/#configuring-which-data-attributes-are-used-as-configuration.md)Configuring which data attributes are used as configuration
The root element of the component may have many data attributes. Some of these attributes are configuration options for the component, but others may be used for different purposes, such as features from third-party JavaScript libraries.
Your component needs to define a `schema` [static property](./building-your-own-javascript-components/#defining-static-properties-on-components.md) to pick which attributes of the root element to use for the component’s configuration. This property should provide an object that defines the type of the configuration options in its `properties` key.
You need to include each first-level option of the configuration that can be configured through a data attribute on the root element in that schema. The key will be the same name as the one set in [the `defaults` property](./building-your-own-javascript-components/#setting-a-default-configuration-for-your-component.md). The value will be an object with the shape `{type: ‘NAME_OF_THE_TYPE’}`, with `NAME_OF_THE_TYPE` being one of: `number`, `string`, `boolean`, or `object`. Options in nested objects will have their type inferred from the value of the attribute.
We recommend you treat the `schema` property as read-only in your code.

```
import { ConfigurableComponent } from 'govuk-frontend'

class MyComponent extends ConfigurableComponent {
  /* … */

  static defaults = {
    anOption: 1,
    aNumberOption: 1,
    aBooleanOption: false,
    anOptionWithNesting: {
      aNestedOption: 'itsValue',
      anotherLevel: {
        aDeeplyNestedOption: true
      }
    }
  }

  static schema = {
    properties: {
      // As `anOption` is left out of this object
      // it won’t be able to be overridden by `data-an-option`
      aNumberOption: { type: 'number' },
      aBooleanOption: { type: 'boolean' },
      // For nested objects, only the type of the root needs to be defined
      anOptionWithNesting: { type: 'object' }
    }
  }

  constructor(root, config) {
    super(root, config)

    // Run custom initialisation code here
  }

  /* … */
}

```

###  [](./building-your-own-javascript-components/#accessing-the-component-s-configuration.md)Accessing the component’s configuration
You can access the component’s configuration within the component’s methods and its constructor, using `this.config`.

```
import { ConfigurableComponent } from 'govuk-frontend'

class MyComponent extends ConfigurableComponent {
  static moduleName = 'app-my-component'

  static defaults = {
    // Default values go here
  }

  constructor(root, config) {
    super(root, config)

    // Add a class based on the `variant` configuration option
    this.$root.classList.add(`app-my-component–${this.config.variant}`)

    this.$root.addEventListener('click', this.handleClick.bind(this))
  }

  handleClick() {
    if (this.config.variant == 'aSpecificVariant') {
      // Do something specific for the variant defined as a configuration option
    } else {
      // …
    }
  }
}

```

##  [](./building-your-own-javascript-components/#checking-for-gov-uk-frontend-support-with-issupported.md)Checking for GOV.UK Frontend support with `isSupported()`
GOV.UK Frontend components and components that inherit from [our `Component` class](./building-your-own-javascript-components/#using-the-component-class.md) will automatically check if GOV.UK Frontend is supported during their initialisation. However, you may want to separately check for support, to avoid unnecessarily running code if GOV.UK Frontend is not supported.
Use the `isSupported()` function to check whether GOV.UK Frontend is supported in the browser your code is running in.

```
import { isSupported } from 'govuk-frontend'

if (isSupported()) {
  // Do things if GOV.UK Frontend is supported
}

```

  * [View source](https://github.com/alphagov/govuk-frontend-docs/blob/master/source/building-your-own-javascript-components/index.html.md.erb)
  * [Report problem](https://github.com/alphagov/govuk-frontend-docs/issues/new?body=Problem+with+%27Building+your+own+JavaScript+components%27+%28https%3A%2F%2Ffrontend.design-system.service.gov.uk%2Fbuilding-your-own-javascript-components%2F%29&labels=bug&title=Re%3A+%27Building+your+own+JavaScript+components%27)
  * [GitHub Repo](https://github.com/alphagov/govuk-frontend-docs)

  * [Accessibility](https://design-system.service.gov.uk/accessibility/)
  * [GOV.UK Design System](https://design-system.service.gov.uk/)
  * [GOV.UK Prototype Kit](https://govuk-prototype-kit.herokuapp.com/)

All content is available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated 
[© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
