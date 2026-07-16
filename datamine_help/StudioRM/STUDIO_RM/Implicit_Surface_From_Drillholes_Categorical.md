# Create Categorical Surfaces

To access this screen:

  * **Implicit** ribbon **> > Surface >> Categorical**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **create-categorical-surfaces** and click **Run**.
  * Enter "create-categorical-surfaces" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

The Create Categorical Surfaces task is the user interface for the [create-categorical-surfaces](<../command_help/create-categorical-surfaces.md>) command. It is used to create a volume that represents a specific key field value within an input samples file, and is typically used for intrusion modelling.

**Note** : You can also access this command [using an automation script](<Implicit_Modelling_Command_Automation.md>).

The input to this command is a loaded desurveyed drillholes file, containing at least one attribute and corresponding value to be modelled. A common use of this command, for example, would be to model a volume representing a particular lithology.

![](../Images_STUDIORM_ONLY/grade_shells1.jpg)

_Example of a clipped 3D section showing drillholes with the profile of categorical volumes_

The volume is generated according to various input parameters that allow you to express; 

  * your confidence in individual sample records and/or the sample database generally.
  * a directional data trend, either globally (using an aligned ellipsoid) or as multiple ellipsoid definitions for structures with complex anisotropy.
  * the density of your output wireframe (NGRID).  

## Categorical vs. Grade Shell Command

[create-categorical-surfaces](<../command_help/create-categorical-surfaces.md>) differs from [create-grade-shells](<../command_help/create-grade-shells.md>) in that the categorical version of the command models a distinct key field value. 

The continuous version of the command models grade shells denoting a specific cut-off grade. 

The user interface for both commands is similar in other respects.

Both commands differ from vein structure modelling in that vein modelling produces a continuous surface representing one HW and one FW surface per structure. Categorical and continuous structural modelling commands produce shells that envelop positive intervals (one or more per sample). This approach is more suitable for modelling non-linear or bifurcating domains.

## Uncertainty - Sample Confidence

For more information on managing data uncertainty, see [Snapping to Contacts](<Implicit_Surface_From_Drillholes_Snap.md>)

### Implicit Modelling Metadata

Implicit modelling tools store metadata to allow previous settings to be reinstated automatically, and for downstream commands to understand the 'legacy' of input data. See [Implicit Modelling Metadata](<../COMMON/Implicit-Modelling-Metadata.md>).

Activity steps:

A typical approach for using this command is:

  1. Load a desurveyed drillholes file.
  2. Launch the command.
  3. Define the scope of your modelling; select the loaded Drillholes object, the Column containing the categorical Value to be modelled.

**Note** : Each unique value is shown alongside its default legend colour.

  4. Specify your confidence in the accuracy of input sample data and associated contact points using **Uncertainty**. This can be set at a **Default** (meaning global) level, or read from a data attribute in the loaded **Drillholes** object.

See [Data Uncertainty](<../COMMON/Implicit_Modelling_4_Uncertainty.md>).

  5. Data can be modelled only if it is **Selected** and/or **Visible** , using a combination of settings. 

     * If **Selected** is **checked** :

       * If no data is selected, everything is modelled.

       * If data is selected, only selected holes are modelled.

If selected is unchecked, all data is modelled regardless of data selection.

     * If Visible is **checked** , only drillhole data that is visible is used for modelling, otherwise data is modelled even if it is filtered from the view.

  6. You can add points to your data to encourage a particular shape or trend. Such points are added onto the current 3D section. You can edit the current section using **Section Controls**.
     * Interactively position the plane used to generate surface data by enabling the **Section Editor** control. See [3D Section Widgets](<../COMMON/Section_Widgets.md>).
     * Alternatively, modify the section using one of the controls in this section. These are replicated on the **3D View** ribbon and **[Navigation toolbar](<../COMMON/Navigation_Toolbar.md>)**.
     * Automatically align the view to be directly at the 'best-fit' plane through the data by enabling **Auto look**. This doesn't affect the definition of a modelling section - only the view is adjusted.
     * **Align** the view with a custom section.
     * **Reset** the modelling section to the automatically-calculated best-fit plane.
  7. To define a trend to impart a guiding direction or directions throughout your structure:

     * Choose **Default from holes** to let Studio calculate the most appropriate trend for your data, using a consistent directional trend throughout your data. In effect, this makes use of a single, global **[search ellipsoid](<Ellipsoids_Overview.md>)** to interpolate a surface between contact points.
     * Choose **Custom** to define one or more ellipsoids that will be used to govern uni- or multi-directional trends throughout your data.
       1. Choose an existing ellipsoids data object, if one exists (if not, one will be created shortly).
       2. If appropriate, select **Pick Drillhole Samples** and select one or more drillholes that will be used to automatically create an ellipsoid. This is usually a set of holes within which a single trend is obvious. Once selected, choose **Create Ellipsoid from Selected Data**.

The generated ellipsoid displays at the centre of the selected drillhole set.

       3. To manually position and define the axis dimensions of an ellipsoid, choose **Create Ellipsoid**. See [New Ellipsoid](<../COMMON/New_Ellipsoid.md>).
       4. Edit any previously-created ellipsoid by clicking **Edit Ellipsoid**. See [Edit Ellipsoid](<../COMMON/Edit_Ellipsoid.md>).
     * Ellipsoids are interpolated throughout the sample data in a uniform 3D grid, gradually morphing between defined ellipsoid shapes.

Preview this grid by first selecting how detailed your preview will be (for example, 3 x 3 x 3 shows a grid of 27 ellipsoids, each in their interpolated shapes and orientations). Then, click **View** to render a temporary preview of ellipsoids on the screen, for example:

![](../Images_STUDIORM_ONLY/Ellipsoids_GRID.jpg)

From here, you can see how each part of the data is likely to connect to neighbouring parts.

  8. Implicit surface modelling is an interpolative process where surface data is fitted (as closely as trends and other modelling parameters permit) to contact points. Enabled by default, the **Snap to contacts** section can enforce a secondary deformation of the generated surface to enforce a closer relationship between the output surface and its contact points. 

**Note** : Snapping to contacts is performed after the initial volume is generated, and works by deforming the mesh so that points within a tolerance distance of a contact position are moved towards that position, affecting neighbouring mesh points to maintain the integrity of the output shape. This is a very intensive operation and, where there are many contact positions to consider (say, the input drillhole file is large, with lots of positive intervals), this can extend processing time significantly.

For more information, see [Snapping to Contacts](<Implicit_Surface_From_Drillholes_Snap.md>).

  9. Define **Surface Generation Controls** :
     * The categorical modelling command needs to subdivide positive samples into smaller units to ensure ellipsoid centroids are positioned at suitable positions within the data set. You can choose to **Subdivide** automatically (**Auto**) or by choosing your own **Fixed** subdivision distance, where smaller values tend towards increased processing, but potentially a more representative result.
  10. Define the Resolution of your output wireframe using the drop-down list (high values = small triangles = longer processing). For more precise control, select **< custom>** and enter your own value.
  11. Choose how far beyond the hull of sample data categorical models can extend. You do this by entering a Percentage extra value, where 50% will allow models to extend beyond the cuboid hull of loaded sample data by up to 50% more, for example. As a worked example, if the bounding cuboid of data is 10 x 20 x 30 meters, the permissible 'space' for categorical modelling is within a cuboid 15 x 30 x 45 meters.
  12. Decide if you want to constrain values that terminate at the collar (**First**), end-of-hole (Last), **Both** ends or **Neither** , using the Constrain ends drop-down list.
  13. Choose if **Additional Points** will be included in the surface calculation. Additional points can be added to influence the creation or removal of surface in a given area, or you add a 'dummy' interval to mimic a load drillhole. This can help to encourage the generation of surface data in a particular area, where a global or local anisotropic trend requires more help to form material in a particular area. 

**Note** : You can generate a categorical surface using only additional points if you want. This facility is available even without loading a drillhole object and defining a value to be modelled.

     1. If an existing loaded string data object contains the points you need (this will have been created previously by the Create Categorical Surfaces command and contain required attributes), select it from the **Object** list.
     2. If no object is loaded, and you wish to create a new one in which to store additional points, enter a unique **Object** name and;
        * Insert **positive** (green) sample points to the 3D window by first clicking the green button then picking one or more points in the 3D view. These points masquerade as the 'positive' material of your scenario and the surface generator will attempt to ensure they are all within the enveloping volume(s) or on the boundary of the categorical value being modelled.
        * Insert **negative** (red) sample points to discourage the generation of categorical volume(s) in a particular area. As above, digitize these wherever you want the surface generator to avoid.
        * Insert full sample **intervals** representing positive material. This is the same as adding a new drillhole to the set, which has a single interval and represents the categorical value being modelled. 

**Tip** : Set up your 3D section before you add points, and if you have reference data that represents landmark positive or negative sample positions, say a collars table, load it first and use it as a basis for snapping (right-clicking) additional point positions.

  14. Define an **Output** **Surface** name. This is the name of the object to be created. If an object of the same name exists, a unique numeric suffix is applied.
  15. Choose to either generate a new data object, or update an existing one:
     * Click New Surface to create a new output wireframe object with default formatting.
     * Click **Update surface** to replace a target object (of the same **Surface** name) with new data. 
       * If **Retain output formatting** is **checked** , any previous overlay customizations to the existing model will be retained. That is, only the shape of the target object can change, not its visual formatting.
       * If **Retain output formatting** is **unchecked** , default wireframe model formatting is reapplied to the target object and any prior overlay customizations are lost. This cannot be undone.
  16. Review your output volume.

**Tip** : Restore the settings from the last modelling run using **Reset**.