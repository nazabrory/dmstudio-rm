# show-samples

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#show-samples>)

To access this command:

  * **Estimate** ribbon **> > Validate >> Show Samples**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "show-samples"

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **show-samples** and click **Run**.

## Command Overview

See which samples contributed to the estimation of a parent cell. This command can be used to interrogate regular models or sub-celled models, although only parent cell information is reported.

**Note** : To view samples contributing to sub-cell estimation, see [show-samples-subcells](<show-samples-subcells.md>).

Before you run this command, both these data objects must be loaded:

  * A block model (regular or sub-cell type).
  * A **SAMPOUT** points file, such as that produced by [ESTIMA](<../Process_Help_XML/estima.md>) (and also by the [Advanced Estimation](<../STUDIO_RM/Multivariate_Run_Estimation.md>) wizard, where [SAMPOUT](<../STUDIO_RM/Multivariate_Run_Estimation.md>) is an optional output file).

The loaded model can be rendered using any display type, although an intersection with a nominated 3D section is recommended. Once both the model and the corresponding **SAMPOUT** file are loaded, you can run the command to activate 'block selection mode'. Click anywhere within a model cell (parent or sub-cell) and left-click to display a 3D hull representing the boundary of the selected cell in 3D (see image above). 

Also displayed are the sample points that contribute to the estimation of the selected cell.

Tip: Display the **SAMPOUT** file using scaled symbols in either 2D or 3D to make them easier to see. It can also be useful to apply labels to the **SAMPOUT** points as well, for example, to show the **FIELD** name, or the **XC** /**YC** /**ZC** values. See [Points Properties: Symbols](<../VR_Help/Point_PropDialog_Symbols.md>).

If a sub-cell is selected, the hull of the respective parent cell is displayed plus information relating to the parent cell.

Command steps

  1. Load a block model and a SAMPOUT file.

  2. If you plan to filter displayed samples to show samples relating to a particular grade field or estimation reference, it may be useful to create a legend showing the EREFNUM values in the SAMPOUT file.

  3. Using the **Estimate** ribbon, select the **Field** (and optionally **Estimate** reference number) to provide a more filtered view of contributing samples when a cell is next selected.

**Note** : Filtering is applied immediately after value selection.

  4. Run the **Show Samples** command. 

**Note** : If run from the **Command** toobar, filtering is still applied according to Estimate ribbon settings (by default, filtering is not specified).

  5. Left-click the cell you wish to interrogate. An outline of the parent cell displays and the displayed **SAMPOUT** points filters to show samples contributing to that cell's estimation.

If a grade **Field** , or **Field** and **Estimate** are selected, the sample points are further filtered to show only the samples contributing to the estimation and field combination for the selected cell.

![](../Images_STUDIORM_ONLY/ShowSamples1.jpg)

Note: If no **Field** or **Estimate** is selected, all contributing samples display when a cell is picked.

  6. When you are finished, click Done.

Related topics and activities

  * [show-samples-subcells](<show-samples-subcells.md>)

  * [ESTIMA](<../Process_Help_XML/estima.md>)

  * [Advanced Estimation - Run Estimation](<../STUDIO_RM/Multivariate_Run_Estimation.md>)