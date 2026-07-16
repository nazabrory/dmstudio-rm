# 3D Display Templates

To access this panel:

  * On the [Points Properties](<points%20properties%20dialog.md>) screen, click the Templates tab.

  * On the [Pictures Properties](<Pictures%20Properties%20Dialog.md>) screen, click the Templates tab. 

  * On the [Ellipsoids Properties](<Ellipsoids%20Properties.md>) screen, click the Templates tab.

  * On the [Strings Properties](<Traces_Properties.md>) screen, click the Templates tab.

  * On the [Drillholes Properties](<DH_PropDialog_General.md>) screen, click the Templates tab.

  * On the [Block Model Properties](<BlockModels_Properties_Dialog.md>) screen, click the Templates tab.

  * On the [Wireframe Properties](<Wireframe_Properties_Dialog.md>) screen, click the Templates tab.

  * On the [Planes Properties](<Planes%20Properties%20Dialog.md>) screen, click the Templates tab.

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

3D window templates let you capture and restore an object's visual formatting settings in a convenient way. You can save one or more templates for each object type, and templates can be applied to any loaded data object of the same type. They can even be used to format information in the Plots window.

Templates are stored alongside your project file, but can optionally be exported to an external file (.3dtpl) that can be transferred between projects and systems. Each of the respective properties dialog for points, strings, drillholes, block models, wireframes and planes contain the same functions but you are restricted to applying templates only to the object type from which the template was originally created.

You can also specify which template is to be the "default" for each object type; this will represent the formatting that will be applied each time a new object of that type is created or loaded.

To create a 3D display template:

The basic procedure for creating a template is:

  1. Load a data object of the required type.
  2. Use the object properties screen to apply the various formatting options (colour, symbols, labels etc.) and visually check the results.
  3. When you're happy with the visual formatting, open the object properties screen and select the Templates tab.
  4. Select New
  5. Enter a name for the template and press **ENTER**.

The new template captures the current formatting of the overlay.

**Note** : 3D display templates are the same for all Studio products. You can create one in Studio OP and export it for use in Studio RM, for example.  

To apply an existing 3D display template to the current object overlay:

  1. Create a template using the procedure above.
  2. Open the object properties screen and select the Templates tab.
  3. Select a Template from the main list and click Copy Format from Template.

The object properties screen tabs update to match the contents of the template.

  4. Click OK.

The new visual formatting is applied to the target 3D data object overlay.

To update a 3D display template with new visual formatting settings:

  1. Set up the properties of the data object overlay as you want them.
  2. Click the Templates tab.
  3. Optionally, select Import to select an external .3dtpl file containing template information. See [Import 3D Templates](<3D_Templates_Import.md>).
  4. Select the template name you wish to update using the Templates list.
  5. Click Copy Format to Template and confirm to update the selected template.
  6. If you wish to commit your template changes back to an imported .3dtpl file, click Export and overwrite the template you selected previously. Alternatively, create a new template file. See [Export 3D Templates](<3D_Templates_Export.md>).

To set up a default display template:

A _default_ display template is applied automatically to each 3D object type. For example, setting up a default string data template means that all strings newly digitized into a project session, or into a new strings object

  1. Create a template using the procedure above.
  2. Open the object properties screen and select the Templates tab.
  3. Select the required default template from the Default template list. Alternatively, create a new template (see above) and it appears in the list.
  4. Click OK.

The next time a data object overlay for the same data type is created, it will inherit the settings of the default template.

**Note** : template settings are stored in the project. Different projects can have different default templates, for example. You can share templates across multiple projects by exporting and importing template files.  

Related topics and activities

  * [Templates 3D Export](<../3d_templates_export.md>)

  * [Templates 3D Import](<3D_Templates_Import.md>)

  * [3D Design](<Designing_in_VR.md>)

  * [Windows, Sheets, Projections and Overlays](<../COMMON/concept_views%20sheets%20overlays.md>)

  * [The View Hierarchy](<../COMMON/View%20Hierarchy.md>)

  * [3D Window Templates](<../COMMON/3D_Window_Templates.md>)

  * [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>)