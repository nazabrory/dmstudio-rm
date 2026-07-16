# Project Settings: Wireframing

To access this screen:

  * On the [Project Settings](<ProjectSettings.md>) screen, select the Wireframes tab.

  * **Home** ribbon **> > Select >> Default >> Wireframe Settings**

  * Run the command wf-select-settings.

  * Use the quick key combination 'sbp'

Configure wireframe data selection methods associated with wireframing commands.

### Wireframe Selection Commands

Wireframe selection settings are also available using command line instructions and quick key combinations (shown in brackets):

  * [wf-select-settings](<../command_help/wf-select-settings.md>) (sbp) - opens Wireframe Settings dialog
  * [wf-select-attribute-switch](<../command_help/wf-select-attribute-switch.md>) (sba) - set selection method to Select by Attribute
  * [wf-select-file-switch](<../command_help/wf-select-file-switch.md>) (sbfi) - set selection method to Select by Object
  * [wf-select-field-switch](<../command_help/wf-select-field-switch.md>) (sbfd) - set selection method to Select by Field
  * [wf-select-filter-switch](<../command_help/wf-select-file-switch.md>) (sbfl) - set selection method to Select by Filter
  * [wf-select-group-switch](<../command_help/wf-select-group-switch.md>) (sbg) - set selection method to Select by Group
  * [wf-select-surface-switch](<../command_help/wf-select-surface-switch.md>) (sbs) - set selection method to Select by Surface
  * [wf-select-triangles-switch](<../command_help/wf-select-triangles-switch.md>) (sbt) - set selection method to Select Individual Triangles

See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

To configure wireframe selection settings on this screen:

  1. Display the **Wireframe Settings** screen.

  2. Set the maximum accepted **Tolerance** for accepting the results of boolean operations. Smaller values will give rise to lower tolerances and, potentially, more processing time required when performing boolean operations.

  3. Choose how wireframe data is selected by defining one **Selection Method** :

     * Select Individual Triangleseither select individual wireframe triangles by left-clicking, or use the drag-box-select method to select a group of contiguous triangles. Many wireframing commands can operate on selected triangles only.
     * Select Objectcontrols the selection of wireframe data by object. Select all triangles belonging to the object selected with the cursor.

     * Select by Groupcontrols the selection of wireframe data by picked wireframe group. Select wireframe data matching the wireframe GROUP number of the triangle selected with the cursor.

Note: GROUP fields are not added to wireframe data by default. 

     * Select by Surfacecontrols the selection of wireframe data by picked wireframe surface. Select wireframe data matching the wireframe SURFACE number of the triangle selected with the cursor.

     * Select by Attribute: controls the selection of wireframe data by user attributes. Select wireframe data by all user-defined (non-system) attributes associated with the triangle selected with the cursor. Note that only triangles matching all user defined attributes of the triangle picked will be selected.

     * Select by Fieldcontrols the selection of wireframe data by specifying a field in the selected file. Select wireframe data matching the specified field attribute of the triangle selected with the cursor (e.g. LINK will cause the wireframe to be selected by link). If the requested field is not present in the selected wireframe, and error message will be generated.

     * Select by Filtercontrols the selection of wireframe data by a user defined filter. Select all the triangles of the object selected with the cursor, providing they pass the filter expression.

Related topics and activities

  * [Project Settings](<ProjectSettings.md>)

  * [Project Settings: Wireframe Linking](<Project%20Settings_%20Wireframe%20Linking.md>)

  * [Selecting 3D Data Interactively](<Selecting3DDataInteractively.md>)

  * [wf-select-settings](<../command_help/wf-select-settings.md>)

  * [wf-select-attribute-switch](<../command_help/wf-select-attribute-switch.md>)

  * [wf-select-field-switch](<../command_help/wf-select-field-switch.md>)

  * [wf-select-file-switch](<../command_help/wf-select-file-switch.md>)

  * [wf-select-filter-switch](<../command_help/wf-select-filter-switch.md>)

  * [wf-select-group-switch](<../command_help/wf-select-group-switch.md>)

  * [wf-select-surface-switch](<../command_help/wf-select-surface-switch.md>)

  * [wf-select-triangles-switch](<../command_help/wf-select-triangles-switch.md>)