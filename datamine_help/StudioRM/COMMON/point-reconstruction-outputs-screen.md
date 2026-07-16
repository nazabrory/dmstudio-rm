# Calculate Outputs

To access this panel:

  * Display the [Point Reconstruction Console](<point-reconstruction-console.md>) and select the **Calculate Outputs** panel. This panel is only accessible if the appropriate input points data has been prepared for the chosen reconstruction method. 

This panel is used to generate wireframe data based on input point cloud information and your specified parameters.

## Method Prerequisites

You can calculate an output surface from point cloud data if:

  * You are using either the **[Watertight](<point-reconstruction-methods.md#Watertight>)** or [**Fast Advance**](<point-reconstruction-methods.md#Fast>) reconstruction method and have defined an input point cloud file name and location using the **[Define Scenario](<point-reconstruction-define-scenario-screen.md>)** panel. Optionally, you have **[Subsample](<point-reconstruction-subsample-screen.md>)** d your data.

  * You are using the **[Ball Pivot](<point-reconstruction-methods.md#Ball>)** reconstruction method and have defined an input point cloud file name and location using the **Define Scenario** panel. You have also defined a **Ball radius** using the **[Configure Surfacing](<point-reconstruction-surfacing-screen.md>)** panel. Optionally, you have **Subsample** d your data.

  * You are using either the **[Poisson](<point-reconstruction-methods.md>)** , **[SSD](<point-reconstruction-methods.md>)** or **[Balanced](<point-reconstruction-methods.md#Balanced>)** reconstruction method, have defined an input point cloud name using the **Define Scenario** panel. You have completed the **[Calculate Normals](<point-reconstruction-normals-screen.md>)** panel and **Configure Surfacing** parameters. Optionally, you have **Subsample** d your data.

**Note** : If you attempt to generate a surface with one of the interpolative methods, and normal information can't be found within the data to be surfaced, a message displays and the surfacing operation is cancelled.

The **Calculate Outputs** panel is identical, regardless of the reconstruction method you have chosen or settings applied.

Activity Steps:

  1. Display the [Point Reconstruction Console](<point-reconstruction-console.md>).
  2. Create, load or import a scenario using the [Create Scenario](<point-reconstruction-create-scenario-screen.md>) panel.
  3. Choose a suitable reconstruction method using the [Define Scenario](<point-reconstruction-define-scenario-screen.md>) panel. Ensure **Subsample input points** is checked.
  4. If required, **[Subsample](<point-reconstruction-subsample-screen.md>)** the input point cloud.
  5. If required for the chosen reconstruction method, specify surface normal calculation parameters using the [Calculate Normals](<point-reconstruction-normals-screen.md>) panel.

  6. If required for the chosen method, [Configure Surfacing](<point-reconstruction-surfacing-screen.md>) parameters.

  7. Activate the **Calculate Outputs** panel.

  8. Confirm the **Point data to be surfaced** is what you expected. If not, select the file to be surfaced. Note that, if using the **Poisson** , **SSD** or **Balanced** methods, point data must be appended with normal information via the fields NORMALX, NORMALY and NORMALZ.

  9. To automatically load the generated wireframe data into the 3D view after creation, check Auto load?

  10. To generate a single wireframe file pair based on the current scenario's settings, click **Generate Surface File**. Surface file generation time will vary but can be several minutes for large or dense data inputs. 

Alternatively, recreate all intermediate data files for the current scenario (potentially a subsampled and normalized points file, depending on the chosen method) using **Recreate All Outputs**. A progress indicator displays during processing.

  11. Review your output wireframe.

  12. **Save** your project and, if prompted, generated data files.

To import or export data to transfer settings between projects and systems:

  * To export the current scenario's settings, click **Export Settings** and specify an .xml file name. This file can be shared with other point reconstruction users.

  * To import previously exported settings, click **Import Settings** and select a point reconstruction .xml file.

The **Point Reconstruction Console** settings update to reflect the imported information.

Related topics and activities

  * [Point Cloud Reconstruction](<point-reconstruction.md>)

  * [Point Reconstruction Console](<point-reconstruction-console.md>)

  * [Resolve Duplicate Scenario](<point-reconstruction-import-duplicate-scenario.md>)

  * [Create Scenario](<point-reconstruction-create-scenario-screen.md>)

  * [Define Scenario](<point-reconstruction-define-scenario-screen.md>)

  * [Subsample](<point-reconstruction-subsample-screen.md>)

  * [Calculate Normals](<point-reconstruction-normals-screen.md>)

  * [Configure Surfacing](<point-reconstruction-surfacing-screen.md>)

  * [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>)

  * [PTCLD2WF Process](<../Process_Help_XML/ptcld2wf.md>)

  * [wireframe-create-from-points ("cwp")](<../command_help/wireframe-create-from-points.md>)