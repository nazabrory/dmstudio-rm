# Import 3D Templates

To access this screen:

  * Display the Templates tab of any 3D object properties screen and click Import.

Control how previously **[exported](<3D_Templates_Export.md>)** 3D visual templates are imported.

**Note** : you can only import template information that relates to the data object type in context. For example, you cannot apply wireframe formatting to a loaded block model overlay.

To import a data display template:

  1. Specify where your template information is coming from:

     * **File(s)** browse for a .3dtpl (3D display) or .tpl (Plots) template file that was previously exported from a Studio application.

**Note** : 3D display templates are the same for all Studio products. You can create one in Studio OP and export it for use in Studio RM, for example.  

     * **Plots** import from any currently active plots templates within your project.

  2. Decide what happens if a template of the same name already exists in the current project:

     * **Replace the existing template** the previous template is replaced (without further prompts). Be careful using this one as you may accidentally overwrite a useful template.

     * Give the new template a unique namethis is recommended. The incoming template is renamed by adding a unique suffix. If you then feel you can replace an existing template after checking results, you can do so via the **Templates** tab options.

     * **Discard the new template** with this choice, the existing template prevails and isn't overwritten.

  3. If importing template data from a file, you can also choose what happens to imported legend data that may conflict with existing legend data (either project or user legends):

     1. **Replace the existing legend** overwrite existing legend data with the newly-imported legend. Use this with caution as you could lose a useful legend already associated with your project.

     2. Discard the new legendleave the existing project and user legends intact and don't overwrite them. In essence, imported legend data is ignored if it conflicts with existing data.

Related topics and activities

  * [3D Display Templates](<3D_Templates.md>)

  * [Object Properties - templates tab](<3D_Templates.md>)

  * [Templates 3D Export](<3D_Templates_Export.md>)

  * [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>)