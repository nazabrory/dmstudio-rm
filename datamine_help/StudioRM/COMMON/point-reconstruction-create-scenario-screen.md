# Create Scenario

To access this panel:

  * Display the [Point Reconstruction Console](<point-reconstruction-console.md>) and select the **Create Scenario** panel.

The **Create Scenario** panel is part of the **Point Reconstruction Console** and is used to create, load or delete a point reconstruction scenario. A 'scenario', in this context, represents the settings used to complete one or more stages of the point reconstruction workflow, as indicated by the menu.

Scenarios must be uniquely named within a project. Duplicate names aren't permitted. If a duplicate name is detected as part of a settings import, the [Resolve Duplicate Scenario](<point-reconstruction-import-duplicate-scenario.md>) screen displays, which must be completed before you continue.

Scenarios are saved with your project but can also be independently imported or exported to other systems.

**Tip** : Consider a consistent naming convention when creating scenarios, particularly if other users are likely to load them (say, when exported from one system and imported to another).

* To create a new point reconstruction scenario:

  1. Activate the **Create Scenario** panel.

  2. Click **Create**.

  3. Enter a new scenario name. This must be unique within the active project.

  4. Click **OK**.

The new scenario becomes active and is added to the **Scenario** list below.

  5. To make the scenario available for future project sessions, **Save** your project, or Export Settings to transfer your scenarios to other projects and workstations (file paths to inputs must be the same in both environments).

**Important** : To store the latest scenario changes (creation, deletion or modification), click **OK** in the **Point Cloud Reconstruction** console. If you **Cancel** the console, all scenarios added, deleted or modified during the current console session are lost and previous values are reinstated when the console is next displayed.

To rename an existing scenario:

*   1. Double-click (or tap) an existing scenario description in the list.

The scenario names becomes editable.

  2. Enter a new name for the scenario.

  3. Click or tap away from the scenario name to update it.

* To load an existing scenario:

  1. Activate the **Create Scenario** panel.

  2. Select a **Scenario** from the list provided.

The selected scenario is highlighted.

  3. Click **Load**.

The **Point Reconstruction Console** panels update to reflect the loaded scenario settings.

* To delete the current scenario:

  1. Activate the **Create Scenario** panel.

  2. Select the **Scenario** to delete.

  3. Click **Delete** and confirm.

The active scenario is deleted from your project. 

**Note** : If you delete a scenario by mistake, simply **Cancel** the **Point Cloud Reconstruction** console and reopen it - the deleted scenario will be reinstated.

To import or export data to transfer settings between projects and systems:

  * To export the current scenario's settings, click **Export Settings** and specify an .xml file name. This file can be shared with other point reconstruction users.

  * To import previously exported settings, click **Import Settings** and select a point reconstruction .xml file.

The **Point Reconstruction Console** settings update to reflect the imported information.

Related topics and activities

  * [Point Cloud Reconstruction](<point-reconstruction.md>)

  * [Point Reconstruction Console](<point-reconstruction-console.md>)

  * [Resolve Duplicate Scenario](<point-reconstruction-import-duplicate-scenario.md>)

  * [Define Scenario](<point-reconstruction-define-scenario-screen.md>)

  * [Subsample](<point-reconstruction-subsample-screen.md>)

  * [Calculate Normals](<point-reconstruction-normals-screen.md>)

  * [Configure Surfacing](<point-reconstruction-surfacing-screen.md>)

  * [Calculate Outputs](<point-reconstruction-outputs-screen.md>)

  * [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>)

  * [PTCLD2WF Process](<../Process_Help_XML/ptcld2wf.md>)

  * [wireframe-create-from-points ("cwp")](<../command_help/wireframe-create-from-points.md>)