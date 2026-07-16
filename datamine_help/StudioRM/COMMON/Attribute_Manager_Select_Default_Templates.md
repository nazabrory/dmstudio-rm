# Select Default Attribute Template

To access this screen:

  * Using the [Attribute Manager](<Attribute_Manager.md>), select Select Default Templates.

This screen is used to define which attribute template (previously-defined) is applied when an object of a particular data type is created. You can select a default template for point, string, drillhole, wireframe and/or block model data types.

Unless a template has been set up, it will not appear in any drop-down list. You can apply the same template to more than one data type, or you can specify [<None>], meaning a template will not be used, and only default fields are created for that object type.

To assign an attribute template to a data type (for automatic attribute creation):

When a template has been defined, it can either be assigned to an existing object in memory (see below) or it can be used to created user attributes for every object that is created for a given object type. This procedure shows you how to assign a template to an object type so that each new object that is created, the defined user attributes will be added. This procedure assumes that an attribute template has already been created (see above):

  1. Open the Attribute Manager using one of the methods set at the start of this page.

  2. The lower half of the dialog is dedicated to the setup of templates.

  3. Assuming that an attribute template already exists (as indicated by the presence of a table row in the Template Table section), left-click a cell in a template table row to activate it, and click Select Default Templates.

  4. Using the Select Default Templates screen, select the drop-down list next to the data type to which you wish to assign a template.

  5. All attribute templates are available for all visual table types, so select the template you wish to assign.

**Note** : You can assign the same template to more than one data type.

  6. Click OK.

  7. Click OK on the Attribute Manager screen to dismiss it.

Related topics and activities

  * [Attribute Manager](<Attribute_Manager.md>)