# ESTIMATE: Controls

To access this screen:

  * Display the **ESTIMATE** screen and click through to the **Estimation** tab.

Control [parent cell estimation](<Grade%20Estimation%20Additional%20Features.md#Parent>), [discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>) and unconstrained modelling options for the purposes of grade estimation.

This screen is split into two areas:

  * Parameters Specify parent cell estimation, discretisation and unconstrained modeling options.

  * Model Update Specify how your model volume is updated, and any field copying settings.

### Parameters Tab

The following fields are available on this tab:

  * Parent Cell Estimation When creating the geological block model, cell splitting is generally applied so that the cells give a good volumetric representation of the geological boundaries. It is then common practice to estimate a separate grade for each cell, so that grades differ between cells in the same parent cell. The following parent cell estimation options are available:

    * Sub-cells estimation If selected, then grades are estimated and assigned to each sub-cell, potentially resulting in different grades occurring for each sub-cell within a parent cell. Zonal control is still applicable, so that if, for example, the parent cell contains 4 cells of rock A, and 5 cells of rock B, then the parent cell would first be estimated using rock A samples, and this value applied to the 4 cells. Then, the parent would be estimated for rock B in an identical way.
    * Parent cell estimation using a full 3D matrix of points The parent cell is represented by a full set of [discretised](<Grade%20Estimation%20Cell%20Discretisation.md>) points covering the entire parent cell.

    * Parent cell estimation using only points which fall inside the subcells The full set of discretisation points is still calculated, but only those points which lie within one of the corresponding cells are selected and used.

Note: For more information on parent cell estimation, see [Grade Estimation Parent Cell Estimation](<Grade%20Estimation%20Additional%20Features.md#Parent>). For more general information on cell discretisation, see [Grade Estimation Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>).

  * Cell Discretisation There are two core methods for defining discretisation points:

    * Number of points in X, Y and Z Select this option to enable the three Number of points... fields below. These fields are used to define the number of discretisation points in the X, Y and Z directions respectively.

Note: If an even number of points in a direction are defined, the points will be spaced around the centre line. If an odd number of points are defined then there will be a point on the centre line and the others will be spaced regularly towards the edges.

    * Spacing between points in X, Y and Z Select this option to define discretisation points according to a minimum distance between points in X, Y and Z directions; these fields are activated when this option is selected. The distance between discretisation points is defined rather than the number of points.

Using this method, there is always one point at the cell centre and all other points are located at the specified distance from it. If a point is calculated to lie exactly on a cell boundary, then it will not be created.

Note: For more information on cell discretisation methods, and the advantages of each, see [Grade Estimation Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>).

  * Unconstrained Modeling If there are no cells in the input geological model then the estimation process will create cells if there are sufficient data within the search volume. If sub-cells are required, then the number of sub-cells per cell in each of the three directions can be defined, using the Number of subcells in... fields shown.

### Model Update Tab

In certain circumstances, it may be necessary to update the grades in one part of the block model. One method is to copy the part of the model which requires updating into a separate sub-model, run the grade estimation on the sub-model and then add the models back together. Alternatively, if the part of the model to be updated can be defined as a cuboid, then it is possible to use parameters and do the updating 'in place', using the options on this tab.

  * Use update limits Select this check box to specify the minimum and maximum X, Y and Z fields to define a cuboid representing the model, using the enabled table matrix. You can also reset the table values to zero using the Reset Defaults button.

Note: Whatever values are provided in the **Update Limits** table, they will be adjusted to the nearest parent cell boundary before updating begins. 

  * If there are insufficient sample to estimate a grade If the Input Prototype Model has cells and already includes the field being estimated, and there is insufficient data within the search volume to estimate a cell, then the following choice of actions is available:

    * Assign absent data values An absent data grade value is assigned to the Output Model.
    * Copy the grade value from the geological model The existing value in the Input Prototype Model is copied to the Output Model.

You can also:

  * Restore Restore the settings added prior to the last Run of the screen. This will restore all settings on all screens.

  * Clear Reset all fields on all screens to their default values.

  * Previous/Next Move backwards or forwards one screen in the order of Estimate screens

  * Run Run the current grade estimation.

  * Cancel Cancel the ESTIMATE process without running an estimation.

Related topics and activities

  * [ESTIMATE: Unfolding](<Estimate_Unfolding.md>)

  * [ESTIMATE: Search Volumes](<Estimate_Search.md>)

  * [ESTIMATE: Variogram Models](<Estimate_Variogram.md>)

  * [ESTIMATE: Files](<Estimate_Files.md>)

  * [ESTIMATE: Estimation](<Estimate_Estimation.md>)

  * [ESTIMATE: Preview](<Estimate_Preview.md>)

  * [Introduction to Grade Estimation and Interpolation](<Advanced%20Estimation%20Validation.md>)

  * [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)

  * [Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>)

  * [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)

  * [Grade Estimation Output and Results](<Grade%20Estimation%20Output%20and%20Results.md>)