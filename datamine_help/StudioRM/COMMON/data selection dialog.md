# Selection

To access this screen:

  * When editing wireframe attributes, pick a point on the wireframe to update the [Edit Attributes](<edit%20attributes%20pick%20dialog.md>) screen.

The Selection screen displays when the pick tool is used during wireframe attribute editing.

  * Object Name The name of the wireframe modified by any filter defined by the selection methods detailed below.

Selection Method Presents a choice of the following mutually exclusive ways of picking a wireframe, or part of a wireframe.

  * Select Object Selects the whole object and places the object name in the Object Name drop down box.

  * Select by Group Selects the part of the wireframe object bearing the group number of the part clicked (e.g. GROUP=2) and creates a temporary wireframe object which is reported in the Object Name drop down box as the whole object name - split by group (e.g. "red_cube_tr/red_cube_pt (wireframe) - Split (GROUP=2)".

  * Select by Surface Selects the part of the wireframe object bearing the surface number of the part clicked (e.g. SURFACE=3) and creates a temporary wireframe object which is reported in the Object Name drop down box as the whole object name - split by surface (e.g. "red_cube_tr/red_cube_pt (wireframe) - Split (SURFACE=3)".

  * Select by Attribute Selects a part of the wireframe which shares all the same attribute values as the part clicked. (e.g. (=10) AND (BLOCKID=2)) and creates a temporary wireframe object which is reported in the Object Name drop down box as the whole object name - split by attributes (for example "red_cube_tr/red_cube_pt (wireframe) \- Split (=10) AND (BLOCKID=2)".

  * Select by Field This works similarly to Select By Surface, or Select By Group, but allows the user to define the Field name being used (e.g. Select by ). If using default selection mode, the Field name can be defined in the [Project Options](<Options_Project.htm.md>) screen (Wireframe Properties tab). When the selection mode is made on a case-by-case basis, the standard Data Selection dialog allows the field to be selected from the fields present in the currently selected object.

  * Select by Filter Selects a part of the clicked wireframe which agrees with a filter argument set in the [Project Settings](<ProjectSettings.md>) screen.

  * Filter Wizard Displays the [Data Expression Builder](<ExpressionWizardDialog.md>), allowing you to use standard comparative filter expressions to determine the data to be selected.

Related topics and activities

  * [Project Settings](<Project%20Settings_Wireframing.md>)

  * [Selecting Wireframes](<selecting_wireframes.md>)

  * [ Boolean and Plane Wireframe Operations](<boolean_operations.md>)

  * [ Current Objects](<Concept_Current_Object.md>)

  * [ The Data Expression Builder](<ExpressionWizardDialog.md>)