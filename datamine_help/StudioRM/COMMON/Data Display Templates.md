# Format Display: Templates

To access this screen:

  * Show the **[Format Display](<Format%20Overlays%20Dialog.md>)** screen. Activate the Overlays tab and click **Overlay Objects >> Show: Overlays**.

This screen displays a list of the available templates for [2D plot projections](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>). 

**Note** : For information on applying templates in 3D projections, see [3D Display Templates](<../VR_Help/3D_Templates.md>).

More templates can be added, and any template can be edited, when in template editing mode.

A template is associated with a particular category of data (points, strings, wireframes and so on). You can only apply a template to data of the corresponding type.

If a template is ticked, the template is applied whenever data of the associated type is loaded. You can apply more than one template if you like (say, a general template to define one batch of settings and a more specific one for a sub-category of data).

Once a template is defined, it can be applied to an overlay using the [Format Display: Style](<Format%20Display%20Dialog_Overlays_Style.md>) screen.

**Note** : You can also use this screen to update an existing template by picking it and configuring the settings on the right. You can also update a template using the [Format Display: Style](<Format%20Display%20Dialog_Overlays_Style.md>) screen.

Data display templates can be used to:

  * Apply the same display format to multiple objects in memory (subject to limitations, see below)

  * Apply the same display format to objects in different projects (subject to limitations)

  * Automatically create an overlay or overlays each time data of a particular type is loaded into memory

Data display templates are saved with the project file, so will be available the next time a project file is loaded. You can also elect to save template information to an external template (.tpl) file for import into any project.

You can pick an existing template and **Delete** it, **Reset** it to default settings or **Rename** it using the [Rename Overlay](<RenamePlotItem.md>) screen.

To create a new data display template:

  1. Display the **Templates** list.

  2. Click **Add**.

The **Add Template** screen displays.

  3. Create a template for a data type. See [Add a Display Template](<add_template_dialog.md>).

Related topics and activities

  * [Formatting Object Overlays](<Formatting%203D%20Objects.md>)

  * [Format Display Screen](<Format%20Overlays%20Dialog.md>)

  * [Add a Display Template](<add_template_dialog.md>)

  * [3D Display Templates](<../VR_Help/3D_Templates.md>)

  * [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>)