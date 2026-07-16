# Define Scenario

To access this panel:

  * Display the [Point Reconstruction Console](<point-reconstruction-console.md>) and select the **Define Scenario** panel.

The **Define Scenario** panel, a mandatory part of t**he Point Reconstruction Console** , is used to define which points data you wish to reconstruct, and by which method. This screen is only accessible once a scenario has been selected, imported or created using the **[Create Scenario](<point-reconstruction-create-scenario-screen.md>)** panel.

The **Define Scenario** panel also provides useful summary statistics about your input point cloud which may guide you when defining settings later on. For example, you can use **Average distance between points** to guide your subsampling parameters.

Your choice of surfacing method can have a significant impact on your output wireframe result. There are many considerations when planning a reconstruction scenario, so have a look at [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>) before you start as it covers all available methods.

Selecting a method updates the help text and summary graphic. Whilst it isn't possible to provide a definitive description of how your data will be surfaced, this information may suggest a suitable reconstruction method.

Regardless of the method chosen, once an input file and reconstruction method are chosen, you have the option of subsampling (reducing) your input points. Subsampling can be useful to reduce the file size of unnecessarily dense inputs, removing noise and encouraging a more consistent point spacing.

Depending on the method chosen, you may have the option to calculate point normals. Point normals are required for some interpolative methods such as the **Poisson** , **SSD** and **Balanced** methods.

Activity Steps:

  1. Display the **[Point Reconstruction Console](<point-reconstruction-console.md>)**.
  2. **Define a Scenario**.
  3. Choose the **Input point cloud** containing data to be surfaced.
  4. Review the **Point cloud statistics**. You can return to this panel later to check them if you need to.
  5. **Choose a surface reconstruction method**. See [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>).
  6. **Define the scope of your reconstruction project** :
     * **Subsample input points** : If **checked** , the **[Subsample](<point-reconstruction-subsample-screen.md>)** panel activates, letting you reduce the number of points of the Input point cloud to be surfaced using one of the available methods. Available for all reconstruction methods.
     * **Calculate normals** : Only available if an interpolative reconstruction method (such as **Poisson** , **SSD** or **Balanced**) is chosen. If checked, the **[Calculate Normals](<point-reconstruction-normals-screen.md>)** panel activates, allow point normal 3D directions to be calculated based on other input parameters. Normals are required for the aforementioned methods.
     * **Compute surface** : Activates the **[Calculate Outputs](<point-reconstruction-outputs-screen.md>)** panel, used to generate your reconstructed wireframe data. Enabled by default, this option is available for all reconstruction methods.

To import or export data to transfer settings between projects and systems:

  * To export the current scenario's settings, click **Export Settings** and specify an .xml file name. This file can be shared with other point reconstruction users.

  * To import previously exported settings, click **Import Settings** and select a point reconstruction .xml file.

The **Point Reconstruction Console** settings update to reflect the imported information.

Related topics and activities

  * [Point Cloud Reconstruction](<point-reconstruction.md>)

  * [Point Reconstruction Console](<point-reconstruction-console.md>)

  * [Resolve Duplicate Scenario](<point-reconstruction-import-duplicate-scenario.md>)

  * [Create Scenario](<point-reconstruction-create-scenario-screen.md>)

  * [Subsample](<point-reconstruction-subsample-screen.md>)

  * [Calculate Normals](<point-reconstruction-normals-screen.md>)

  * [Configure Surfacing](<point-reconstruction-surfacing-screen.md>)

  * [Calculate Outputs](<point-reconstruction-outputs-screen.md>)

  * [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>)

  * [PTCLD2WF Process](<../Process_Help_XML/ptcld2wf.md>)

  * [wireframe-create-from-points ("cwp")](<../command_help/wireframe-create-from-points.md>)