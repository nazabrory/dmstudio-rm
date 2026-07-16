# Create Isoshells - Volume

To access this screen:

  * Display the [Create Isoshells](<Create_Isoshells.md>)screen and select theVolume tab.

Define a bounding box within which isoshells are calculated. This provides the advantages of restricting the volume to a specific area of interest, and minimizing the effects of extrapolation.

  * Horizontal extents are defined by the intersection of the Inside perimeter and Inside wireframe hulls, if defined. If these files have not been specified, the horizontal extent of the input sample file is used instead.
  * The maximum vertical extent is defined by the lowest maximum elevations of the Below wireframe or Inside wireframe hulls, if defined. If these files have not been specified, the maximum vertical extent of the input sample file is used instead.
  * The minimum vertical extent is defined by the highest minimum elevation of the Above wireframe or Inside wireframe hulls, if defined. If these files have not been specified, the minimum vertical extent of the input sample file is used instead.
  * If Align with search ellipse is selected in the Alignment group, then the bounding box is extended to enable the values specified for Below wireframe, Above wireframe, **Inside Wireframe** and Inside perimeter to be processed in world space. This means that above and below are always relative to the world vertical axis, regardless of any dip in the search ellipse. 

### Bounding Box Guidelines

  * Horizontal extents are defined by the intersection of the Inside perimeter and Inside wireframe hulls, if defined. If these files have not been specified, the horizontal extent of the input sample file is used instead.
  * The maximum vertical extent is defined by the lowest maximum elevations of the **Below wireframe** or **Inside wireframe** hulls, if defined. If these files have not been specified, the maximum vertical extent of the input sample file is used instead.
  * The minimum vertical extent is defined by the highest minimum elevation of the **Above wireframe** or **Inside wireframe** hulls, if defined. If these files have not been specified, the minimum vertical extent of the input sample file is used instead.
  * If **Align with search ellipse** is **checked** , the bounding box is extended to enable the **Below wireframe** , **Above wireframe** , and perimeters to be processed in world space. This means that above and below are always relative to the world vertical axis, regardless of any dip in the search ellipse.

**Tip** : reinstate the values used in the last successful isoshells run using **Restore**.

To constrain the generation of isoshells within a defined cuboid:

  1. Decide if the grid of interpolated points and the bounding box are to be aligned with the defined search ellipse (see [Create Isoshells - Estimation Parameters](<CreateIsoshells_EstParams.md>)):

     * If **Alignment** is **checked** , points and hull are aligned with the search volume. 

**Note** : for an anisotropic search volume, the structure is probably orientated similarly. As such, the grid of interpolated points and the bounding box are, by default, aligned with the search ellipse volume. 

     * If **Alignment** is **unchecked** , points and hull are aligned with the world axes. 

  2. Optionally, further restrict the area within the bounding box by specifying additional reference data in the form of Boundaries:

     * Inside perimeterrestrict the horizontal extents of the isoshells using a perimeter string - this could be an external file (use the browse button), or could be selected previously in any **3D** window, using the **Selected in view** option. With this option, you can't select 3D data whilst the **Create Isoshells** screen is displayed. To select data:

       1. click **Cancel**.

       2. Select string data in any **3D** window.

       3. Redisplay the **Create Isoshells** screen.

       4. Click **Restore**.

       5. Return to the **Volume** tab and continue entering parameters.

**Note** : if more than one perimeter is in the file or selection, the valid region is defined as within _any_ perimeter.

     * Below wireframespecify the maximum elevation of isoshells relative to a DTM wireframe, for example, a topography. Another example is a DTM surface which is created from the coordinates of the top mineralized sample in each drillhole. Select this option and pick a wireframe using the **[Project Browser](<ProjectBrowser.md>)**.

     * Below or Above wireframespecify the minimum elevation of isoshells relative to a DTM wireframe, for example, a DTM surface created from the coordinates of the bottom mineralized sample in each drillhole. 

     * Inside wireframeconfine isoshells to within a closed wireframe. 

  3. Define a Bounding Box if you want to constrain results to a specified 3D cuboid.

To define boundary box constraints:

     1. Choose if you wish to create a constraining cuboid automatically:

        * If Fit to data and boundaries is **checked** , a bounding box is automatically set using the hulls of the sample file and bounding data.

        * If Fit to data and boundaries is **unchecked** , you can define a bounding box manually. In this case, the bounding box must not extend significantly from the original samples: isoshells generated from extrapolated values are significantly less valid than those formed from interpolated values between samples.

If manual selection is chosen, the fields in this section become active. What they are called depends on whether you are automatically aligning data with the defined search ellipse:

          * If Align with search ellipse is **checked** , values are displayed in world coordinates using Origin and Lengths fields.

          * If Align with search ellipse is **unchecked** , world coordinates are shown using Minimum and Maximum fields. An error message is displayed if an invalid bounding box is entered (maximum values less than or equal to minimum values, or length values less than or equal to '0').

If Align with search ellipse is **unchecked** and Fit to data and boundaries is also **unchecked** , the bounding box is automatically set to a minimum of '0', and a maximum of '1' for X, Y and Z, and appropriate minimum and maximum values must be manually specified.

**Note** : although isoshells output is constrained by these parameters, it will not necessarily fit them _precisely_ : the closeness of fit is determined by the coarseness of the Triangle Spacing parameter defined on the [Output](<CreateIsoshells_Output.md>) tab.

Related topics and activities

  * [Create Isoshells](<Create_Isoshells.md>)

  * [Create Isoshells: Input](<CreateIsoshells_Input.md>)
  * [Create Isoshells: Condition](<CreateIsoshells_Condition.md>)

  * [Create Isoshells - Estimation Parameters](<CreateIsoshells_EstParams.md>)

  * [Create Isoshells: Output](<CreateIsoshells_Output.md>)

  * [Isoshells Report](<CreateIsoshells_IsoShellsRep.md>)

  * [Create Categorical Surfaces](<../STUDIO_RM/Implicit_Surface_From_Drillholes_Categorical.md>)

  * [Create Grade Shells](<../STUDIO_RM/Implicit_Surface_From_Drillholes_Continuous.md>)

  * [Search Volumes for Grade Estimation](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Introduction.md>)
  * [Grade Estimation Methods](<../STUDIO_RM/Grade%20Estimation%20Methods.md>)