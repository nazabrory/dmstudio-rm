# Create Vein Surface

To access this screen:

  * Activate the **Implicit** ribbon and select **Surface >> Vein**.
  * Enter "vein-from-samples" into the **[Command Line](<Command_Toolbar.md>)**.

The **Create Vein Surface** screen is the interactive interface for the **[vein-from-samples](<../command_help/vein-from-samples.md>)** design command, used to model linear, continuous structures representing vein or vein-like structures according to the presence of [Positive and Negative Samples](<Create_Vein_Surfaces_5_PositiveNegative.md>). See [Vein Modelling](<Create_Vein_Surfaces_Overview.md>).

**Note** : The **Create Vein Surface** screen can be used in conjunction with other application functions. 

The screen is split into setting categories. Many sections can be expanded or collapsed to make it easier to define settings for a modelling run. Expand or collapse a screen section by clicking its title bar.

The following sections are available:

  * **Data Selection** Choose a loaded drillhole object and a value to model. Typically, this is a categorical model representing a linear structure throughout the sample data. This area also provides useful 3D section tools to let you view your sample data in an appropriate way before reviewing and editing hangingwall (HW) and footwall (FW) points. 

Data can be preselected before displaying the **Create Vein Surfaces** screen. See [Select Data for Implicit Modelling](<Create_Vein_Surfaces_1_Data.md>).

You can also choose to only model **Selected** and/or **Visible** data. 

  * **Section Controls** A 3D plane controls generation of normals in output vein models. Configure the 3D window section here if you plan to use it as the "best fit plane" (see below) when generating vein data. See [Create a Vein Model](<Create_Vein_Surfaces_2_Activity.md>).

  * **Best Fit Plane** Choose how the best fit plane is calculated for the generation of wireframe normal data. See [Create a Vein Model](<Create_Vein_Surfaces_2_Activity.md>).

  * **Edit Samples** Adjust sample HW and FW points, including reversing and ignoring samples to encourage a modelling outcome. This section also includes global settings to determine how sample gaps are treated (the Create Vein Surfaces tool expects a single continuous sample). End-of-hole data options are also available. See [Edit Samples](<Create_Vein_Surfaces_6_Reversal.md>).

  * **Additional Points** Encourage an expected surface or volume shape by adding HW and FW samples. You can also add additional samples to the trend surface; this is the surface generated throughout the midpoint of positive samples. Adding points can influence the shape of both HW and FW surfaces. See [Add Extra Vein Points & Intervals](<Create_Vein_Surfaces_9_Adding.md>).

  * **Boundary** Constrain your output shape(s) using a boundary. This can either be calculated automatically in relation to the exterior hull of your loaded sample data, or using a custom string outline or block model prototype. See [Boundary Options](<Vein_Modelling_Boundary_Clipping.md>).

  * **Faults** Model fault blocks by introducing wireframe sheets to your modelling scenario. Faults can fully or partly intersect the drillhole data, and you can optionally automatically extend fault wireframes to ensure a clean intersection with the data extents. See [Model Faults](<Create_Vein_Surfaces_10_Faults.md>).

  * **Controls** Define global modelling settings that constrain the thickness of an output volume and the density (size) of output wireframe data. See [Vein Generation Controls](<Create_Vein_Surfaces_7_Thickness.md>)

  * **Output** Choose the data to create; HW, FW or a combined volume. You can also generate a trend surface and a string representing the boundary of the output vein data (which can subsequently be used with modification as an input boundary to refine the overall shape). See [Vein Modelling Outputs](<Create_Vein_Surfaces_Output.md>).

**Tip** : You can also automate this command through a script. See [Create Vein Surface: Automation](<Create_Vein_Surfaces_10_Automation.md>)

## Batch Processing

A batch run option is available to recreate previous settings for each **Column** and **Value** combination. This can be useful, for example, to assess the sensitivity of a parameter to the output vein shape. See [Process a Batch of Vein Models](<Create_Vein_Surfaces_11_Batch_Processing.md>).

If you define modelling settings and close the **Create Vein Surface** screen, those settings are reinstated when the screen is next displayed. This applies to the current project session only.

Related topics and activities

  * [Vein Modelling](<Create_Vein_Surfaces_Overview.md>)

  * [Create a Vein Model](<Create_Vein_Surfaces_2_Activity.md>)

  * [Select Data for Implicit Modelling](<Create_Vein_Surfaces_1_Data.md>)

  * [Positive and Negative Samples](<Create_Vein_Surfaces_5_PositiveNegative.md>)

  * [Edit Samples](<Create_Vein_Surfaces_6_Reversal.md>)

  * [Add Extra Vein Points & Intervals](<Create_Vein_Surfaces_9_Adding.md>)

  * [Boundary Options](<Vein_Modelling_Boundary_Clipping.md>)

  * [Model Faults](<Create_Vein_Surfaces_10_Faults.md>)

  * [Vein Generation Controls](<Create_Vein_Surfaces_7_Thickness.md>)

  * [Vein Modelling Outputs](<Create_Vein_Surfaces_Output.md>)

  * [Process a Batch of Vein Models](<Create_Vein_Surfaces_11_Batch_Processing.md>)

  * [vein-from-samples ](<../command_help/vein-from-samples.md>)(command)

  * [Create Vein Surface: Automation](<Create_Vein_Surfaces_10_Automation.md>)