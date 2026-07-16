# Define Dynamic Anisotropy Fields

To access this dialog:

  * Using the [Advanced Estimation](<Multivariate_Introduction.md>) dialog, select the Select Prototype menu item. Select the Dynamic Anisotropy tab on the right-hand side of the panel.

## Dynamic Anisotropy

_Dynamic anisotropy_ in the context of grade estimation refers to a method used to account for spatial variations in the orientation of geological features (such as mineralization, ore bodies, or rock layers) during the estimation process. It adjusts the search neighbourhood and variogram model to reflect changes in the direction of continuity (anisotropy) as the estimation point moves through the deposit or study area.

In many geological settings, the spatial continuity of grades or mineral concentrations doesn't follow a single, consistent direction across the entire deposit. Different areas may have varying dominant directions of grade continuity due to geological processes such as folding, faulting, or sediment deposition. Dynamic anisotropy allows these local variations in direction to be incorporated into geostatistical models, typically using kriging or other interpolation methods.

What's the point of it?

  * **Improved Accuracy** It provides more realistic grade estimations in geologically complex areas where mineralization patterns vary spatially.

  * **Better Geological Interpretation** The method can better capture the influence of geological structures, such as faults and folds, which may control ore distribution.

In practical terms in Studio RM, Dynamic Anisotropy is an estimation option that allows the rotation angles for the search volume and variogram model to be defined individually for each cell in the input geological model. 

This means that the search volume and variogram model can be oriented to follow the trend of the mineralization. The method provides an easy to use and fast way of improving the accuracy of grade estimation and is particularly suited to gently folding and rolling orebodies.

### Estimation Methods Support

Dynamic Anisotropy is supported for all estimation methods and should be enabled for orientating search 

Consider the following when defining the angle convention to use in Dynamic Anisotropy:

  * The first angle is a rotation around Z = Dip Direction (typically stored as **TRDIPDIR**).

  * The second angle is the rotation around X = Dip (typically stored as **TRDIP**).

  * The third angle, a rotation around Z = Pitch. This is calculated automatically according to the **Dynamic Anisotropy** setting selected when you [Define an Estimation](<Multivariate_Define_Estimations.md>). Pitch is then calculated with respect to a horizontal or sub-horizontal wireframe (**Flat lying**) or a dipping wireframe (**Inclined**). 

Note: Dynamic Anisotropy support in Advanced Estimation is provided courtesy of the powerful **[ANISOANG](<../Process_Help_XML/anisoang.md>)** process. The @**FLAT** =1 parameter is used in this process to create dynamic anisotropy points for a flat lying structure. Using this mode will align points (orientation defined by **TRDIPDIR** , **TRDIP** and dynamic **ANGLE3** around the axis 3-1-3) with the major direction defined by **SANGLE1** (in **SRCPARM**) or **VANGLE1** (in VMODEL). These points are suitable for locally orientating grade estimation with dynamic anisotropy for a horizontal or sub-horizontal surface.

## Fields Used for Dynamic Anisotropy

A set of up to three angles to be defined for both the search volume and variogram model. Although the method allows for different orientations for search volume and variogram model the two sets of angles will often be the same. In this case, the same field will be selected for each.

All three angles must have corresponding fields in the input model file. If only two angles have been calculated then the third field must still be created in the model and given a value of 0.

To assign dynamic anisotropy fields for use in grade estimation:

  1. If not already selected, pick an **Input model** on the left containing angular data (either search volume, variogram or both).
  2. For the appropriate directional axes (**First** , **Second** , **Third**), pick an attribute containing angular values to orient the search volume during estimation. All numeric fields of the **Input model** are listed.
  3. Similarly, pick appropriate attribute(s) that define orientations for the variogram model. This can be (and often is) the same attribute as used for the search volume, but they can be selected independently.
  4. To use these fields in estimation, you must also tick the appropriate check boxes in the **Estimation Setup** area of the **Define Estimations** panel. See [Estimation Setup Panel](<Multivariate_Define_Estimations.md#Estimation>)

Related Topics and Activities.

  * [Advanced Estimation Introduction](<Multivariate_Introduction.md>)
  * [Advanced Estimation - Automatic Fitting](<Multivariate_FitModels_AutomaticFitting.md>)
  * [Advanced Estimation - Model Parameters](<Multivariate_FitModels_ModelParameters.md>)
  * [Advanced Estimation - Save Models](<Multivariate_FitModels_SaveModels.md>)
  * [Advanced Estimation - Format](<Multivariate_FitModels_Format.md>)
  * [Grade Estimation Variograms](<Grade%20Estimation%20Variograms.md>)
  * [Select Prototype](<Multivariate_Select_Prototype.md>)
  * [Estimate Angles](<Multivariate_Select_Prototype_EstimateAngles.md>)
  * [ANISOANG Process](<../Process_Help_XML/anisoang.md>)