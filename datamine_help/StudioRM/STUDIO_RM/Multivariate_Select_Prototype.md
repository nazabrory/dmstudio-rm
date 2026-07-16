# Select Prototype

To access this screen:

  * Using the [Advanced Estimation](<Multivariate_Introduction.md>) dialog, select the Select Prototype menu item.

Use the **Select Prototype** panel to:

  * Select an existing input geological model representing a model prototype, or a dedicated prototype model file, such as produced by [PROTOM](<../Process_Help_XML/protom.md>), for example.
  * Optionally, select a model that will contain calculated estimated angular data. This can either be combined with the input prototype grade model, or specified as a separate output model.
  * Select a name for the output grade and/or angular estimates model containing the estimation data.
  * Review a summary, by zone if previously selected, of the number of samples and the number of model cells.
  * Optionally select the rotation fields required for the dynamic anisotropy estimation method.

To define a prototype model for your estimation scenario:

  1. Choose the **Input Model** prototype for your scenario. Browse for the input geological or prototype model (such as that produced using **[PROTOM](<../Process_Help_XML/protom.md>)**). This model is the input model for angular estimation and can also be used as an input for grade interpolation.

**Note** : The prototype model will usually contain cells but if a zone field has not been selected for the samples then an empty input model is allowed. In this case a full set of parent cells will be created in the output model, covering the entire rectangular model volume.

  2. Optionally, select a prototype **Model with angles** containing the results of angular interpolation and check the box. This is typically produced using the **[Estimate Angles](<Multivariate_Select_Prototype_EstimateAngles.md>)** panel.

  3. Enter the name of the **Output Model** file to be created or browse for an existing file. If the model file exists it will be overwritten.

  4. Review **Summary** statistics of the selected prototype, by zone if zonal control is being used. 

Column 3 shows the number of parent cells in the model and column 4 the number of parent cells plus subcells in the model. The difference between the last two columns is therefore the number of subcells. If there are zero samples or cells for any zone the number 0 will be shown in red. If there are zero samples but non-zero cells then the cells cannot be estimated. 

  5. Optionally, interpolate angle data between recorded 3D data points and convey this trend information during grade estimation. See [Estimate Angles](<Multivariate_Select_Prototype_EstimateAngles.md>).

  6. Optionally, define rotation angles for the search volume and variogram model to be defined individually for each cell in the input geological model, using the [Dynamic Anisotropy](<Multivariate_Select_Prototype_DA.md>) panel.