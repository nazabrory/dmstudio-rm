# Select Data for Implicit Modelling

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The following information relates to the vein-from-samples and surface-from-samples commands.

The [Create Vein Surface](<Create_Vein_Surfaces_Overview.md>) task is a focussed tool for the calculation of hanging wall (HW) and/or footwall (FW) surfaces that represent vein or vein-like lodes. Similarly, the [Create Contact Surface](<../STUDIO_RM/Surface_From_Samples.md>) task is used to generate contact surfaces between groups of contiguous categorical values.

## Data Selection and Pre-selection

A static drillhole data set must be loaded into memory to use this command.

If no drillholes are selected, all holes within the loaded data object are considered.

Alternatively, you can preselect the samples you wish to use. You can do this using Studio's existing selection methods (left-click, CTRL, bounding box) and this can be performed whilst the modelling task window is displayed.

Sample selection, if performed, accommodates both positive and negative samples: only selected data influences either the generation or retardation of the resulting surface/volume.

If drillholes are pre-selected, at least two individual samples must exist within the selected set. If only one is selected, you are informed that a different selection must be made.

## The Modelling Section Plane

Your application optionally uses a Minimum Curvature method to model surfaces between known data points. This method, based on the principles of contouring, is likely to create a less undulating surface between positive sample points than other surfacing techniques, such as a Gaussian projection, whilst retaining a practical level of continuity between points, unlike a more direct point-to-point approach such as used in tesselation.

To create a hangingwall or footwall surface, which are wireframes, surface normals must be calculated. This determines the relative orientation of surface triangles in relation to the body of positive sample points. As such, when you define a vein modelling scenario, you must define which 3D section plane is used when calculating surface data.

**Section Controls** appear in their own command group on the **[Create Vein Surface](<Create_Vein_Surface.md>)** screen, and are actually shortcuts to commands found elsewhere (mainly on the **3D View** ribbon). By default, a "best fit" section is used.

See [Minimum Curvature Modelling Method](<Delauney%20Tesselation%20Method%20Overview.md>).

To define a 3D section plane for vein modelling:

  1. Load drillhole data containing categorical data.

  2. Display the **Create Vein Surface** screen.

  3. Select the loaded **Drillholes** object.

  4. Select the **Column** containing categorical data to be modelled.

  5. Select the **Value** to be modelled.

  6. Define the 3D section to be used when calculating surface normals, using **Section Controls** :

     * Click **Section Editor** to interactively reposition the currently active **[3D section](<../VR_Help/Sections.md>)**. See [3D Section Widgets](<Section_Widgets.md>).

     * Use the manual section editing tools to adjust the active section:

       * Move Section Forward, Move Section Backwardshift the section position along its primary axis by the current section width (shown in the adjacent field).

       * Enlarge Section, Shrink Sectiononly applicable if **Use Dimensions** is unchecked on the **[Section Properties](<../VR_Help/Section%20Properties%20Dialog.md>)** screen, use these buttons to shrink or enlarge the current section square.

       * **Set Section Using 2 Points** launches the [plane-by-two-points ("2")](<../command_help/plane-by-two-points.md>) command.

       * **Set Section Using 3 Points** launches the [plane-by-three-points ("3")](<../command_help/plane-by-three-points.md>) command.

  7. Decide if the 3D view updates automatically to always show data orthogonal to new section definitions:

     * If **Auto look** is **checked** , each time the section definition changes, the view adjusts to view your data orthogonally to it.

     * If Auto look is **unchecked** , no view adjustments are made when the modelling section changes.

  8. Choose the plane calculation method, or set a manual plane definition using **Plane** options:

     * Choose Auto to use the "best fit" section. This is a section that represents the mean plane through all positive sample intervals.

     * Choose Current section to use whatever the currently active section definition is. Editing the current section affects how vein surfaces are modelled.

     * Choose Custom to set your own **Azimuth** and **Inclination** below. These settings are then associated with the selected Column and Value, meaning you can set any section orientation for values in a **[batch run](<Create_Vein_Surfaces_11_Batch_Processing.md>)**. You can also click **Get Best Fit** to transfer the current best fit orientation values into the **Azimuth** and **Inclination** fields for customization.

Related topics and activities

  * [Create Vein Surface](<Create_Vein_Surface.md>)

  * [Create Contact Surfaces](<../STUDIO_RM/Surface_From_Samples.md>)

  * [Process a Batch of Vein Models](<Create_Vein_Surfaces_11_Batch_Processing.md>)