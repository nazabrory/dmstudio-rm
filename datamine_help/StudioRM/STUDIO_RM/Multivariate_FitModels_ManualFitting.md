# Fit Models Manually

To access this screen:

  * In the [**Advanced Estimation**](<Multivariate_Dialogs_Overview.md>) wizard, select [**Fit Models**](<Multivariate_Fit_Models.md>). Select the **Auto. Fit** tab.

This tab, part of the **Fit Models** screen, is used to fit a model to the currently selected variogram interactively, by creating structures and adjusting their location on the variogram. 

When doing the manual fit, the primary axis of the ellipsoid (local Y), is aligned with the first selected directional variogram on the model reference plane (local dip == 0). The next selected directional variogram will determine the local XY plane of the model orientation, with preference being given to directional variograms on the model reference plane. 

Once the orientation has been determined, the ellipsoid Y range is set to the maximum average distance of the variogram used to set the primary axis. All other selected variograms are then analysed to find the one with the furthest Z and X coordinates, in local ellipse coordinates. If perpendicular variograms have been selected, this would normally be those, but the calculation can handle non-perpendicular choices as well.

The 2 remaining half-axes of the ellipse are then calculated by pushing the 2 new variograms directions and maximum average distances into a pair of simultaneous equations. If the variograms all lie on the same plane (max ellipsoid Z = 0), then a only the X half axis is calculated and the Z radius is left at zero.

The requested number of structures are then created, using a nugget which is 10% of the variance, a sill which is the variance, and ranges for each axis which are evenly divided between the structures up to half of the ellipse radii.

Providing a model can be fitted manually based on the specified number of structures, the chart on the left-side of the panel will be updated. The [Model Parameters](<Multivariate_FitModels_ModelParameters.md>) tab is also updated. 

Examples of where a manual 3D model fitting may not be possible are:

  * All selected variograms lie on the same plane. This will result in only 2D structures being created.
  * If less than 2 variogram directions have been selected on the [Fit Models](<Multivariate_Fit_Models.md>) panel
  * It is impossible to calculate the model orientation.

The variogram model control points on the variogram chart display are moved by clicking and dragging; the cursor changes to indicate the permitted movement direction(s). These depend on the **Manual Fitting** settings on the **[Format](<Multivariate_FitModels_Format.md>)** screen.

  * Nugget Variance pointMove the point vertically up/down to increase/decrease the value, if permitted.

  * Spatial Variance/Range pointsMove the point(s) vertically up/down to increase/decrease the spatial variance value(s), if permitted.

  * Spatial Variance/Range pointsMove the point(s) horizontally right/left to increase/decrease the range value(s), if permitted.

**Note** : If 2D data is specified, clicking **Manual Fit** produces a Range Z equalling 1.

To manually fit a model to the variogram:

The following activity assumes that a **[scenario has been created](<Multivariate_Scenario_Setup.md>)** , [samples selected](<Multivariate_Select_Samples.md>), [variograms created](<Multivariate_Create_Variograms.md>) and the [Fit Models](<Multivariate_Fit_Models.md>) screen displayed.

  1. Set the No. of structures required to fit a model.

  2. Click **Manual Fit**.

**Note** : This button is only enabled if at least 2 variogram directions are selected on the [Fit Models](<Multivariate_Fit_Models.md>) screen, and at least one grade.

  3. Interactively position the structures on the displayed variogram.

Related topics and activities

  * [Fit Models](<Multivariate_Fit_Models.md>)

  * [Automatic Model Fitting](<Multivariate_FitModels_AutomaticFitting.md>)

  * [Model Parameters](<Multivariate_FitModels_ModelParameters.md>)

  * [Save Models](<Multivariate_FitModels_SaveModels.md>)

  * [Format Models](<Multivariate_FitModels_Format.md>)

  * [Advanced Estimation & Variography](<Multivariate_Introduction.md>)