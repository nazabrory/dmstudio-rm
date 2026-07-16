# wf-select-filter-switch ("sbfl")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wf-select-filter-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wf-select-filter-switch"

  * Use the quick key combination "sbfl".

  * **[Project Settings](<../COMMON/ProjectSettings.md>)** screen **> > [Wireframes](<../COMMON/Project%20Settings_Wireframing.md>) >> Select by Filter**.

  * **Home** ribbon **> > Select** menu and pick _WF: Filter_. Ensure toggle is active.

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wf-select-filter-switch** and click **Run**.

## Command Overview

Control the selection of wireframe data by custom data [filters](<../COMMON/Filtering_Data.md>).

Select wireframe data by a predefined data filter. Filters can relate to either system or custom fields in the wireframe point or triangle object. 

The wireframe group and surface numbers are ignored on input, and new group and surface numbers are generated on output.

For example, if your wireframe object contains multiple stope volumes, each attributed with a numeric BENCH_Z attribute value, you could choose to only permit selection of stope data above a particular bench elevation.

Note: The system fields available in the point file are **GROUP, PID, XP, YP, ZP**. The fields available in the triangle files are **GROUP, SURFACE, LINK, TRE1ADJ, TRE2ADJ, T, , NORMAL-X, NORMAL-Y, NORMAL-Z**.

  

Related topics and activities:

  * [Project Settings: Wireframing](<../COMMON/Project%20Settings_Wireframing.md>)

  * [Selecting Wireframe Data](<../COMMON/Wireframe_Selection_Concept.md>)

  * [Selecting 3D Data Interactively](<../COMMON/Selecting3DDataInteractively.md>)

  * wf-select-filter-switch ("sbfl")

  * [wf-select-field-switch ("sbfd")](<wf-select-field-switch.md>)

  * [wf-select-file-switch ("sbfi")](<wf-select-file-switch.md>)

  * [wf-select-group-switch ("sbg")](<wf-select-group-switch.md>)

  * [wf-select-settings ("sbp")](<wf-select-settings.md>)

  * [wf-select-surface-switch ("sbs")](<wf-select-surface-switch.md>)

  * [wf-select-triangles-switch ("sbt")](<wf-select-triangles-switch.md>)