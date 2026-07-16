# ESTIMATE: Files

To access this screen:

  * Display the **ESTIMATE** screen and select the **Files** tab.

ESTIMATE is an interactive version of the [ESTIMA](<../Process_Help_XML/estima.md>) process, with additional functions provided by **[INDEST](<../Process_Help_XML/indest.md>)**.

The **Files** screen is used to define the geological model, unfold and sample input files, and the grade model; as well as the sample and parameter output files for a grade estimation.

## ESTIMATE Inputs

To configure input files for ESTIMATE:

  1. Display the **ESTIMATE** screen.

  2. Select the **Files** tab.

  3. Select the **Input** tab.

  4. Choose an **Input Model**. All estimation methods require an input prototype block model into which the sample grades are interpolated. For more information on input model files, see [Grade Estimation Input Model Files](<Advanced%20Estimation%20Validation.md>).

  5. Optionally, select a parameter file created by the [Unfold Wizard](<UnfoldWizard.md>). This file contains settings specified in the wizard, and the names of the relevant files produced by it. 

Selecting a parameter file and clicking **Apply** automatically updates settings elsewhere, including the **[Unfolding](<Estimate_Unfolding.md>)** tab.

  6. Select a Sample Data File containing grade information to interpolate into the **Input Model** prototype.

  7. The sample file must contain three coordinate fields. Set these for **X** , **Y** and **Z** (see below). See [Grade Estimation Input Sample Files](<Advanced%20Estimation%20Validation.md>).

**Note** : if an unfolded samples file is specified, the coordinates in the Unfolded Coordinate System (UCS) must be selected.

  8. Optionally, select one or two **Zone Control Fields**.

In some cases it may be necessary to use different parameters for the same grade field in different areas. One or two zones can be defined (**Zone 1** and **Zone 2**) and they can have different parameters. See [Grade Estimation Zonal Control](<Grade%20Estimation%20Methods.md#Zonal>). 

**Note** : you do not have to specify zone control fields. In this case, there will be no zone control fields in the estimation parameter file.

  9. If each record in the sample data file is identified by a key field, then the number of samples per key field value can be restricted to a single **Sample Key Field** **Column**. This field is used to define the data column in the loaded sample file that represents that key field. See [Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>).

## ESTIMATE Outputs

ESTIMATE generates interpolated grade information in a block model prototype, specified on the **Input** tab (see above). The resulting model is a new file, specified on the **Output** tab.

Note: in addition to the grade field, some estimation methods also calculate _secondary fields_. For example, [kriging](<Grade%20Estimation%20Kriging.md>) also calculates the number of samples used for kriging and the kriged variance. In order for grade estimation to write these secondary fields to the output model file the field names must be defined using the **Estimation Parameter** file. See [Grade Estimation Secondary Fields](<Grade%20Estimation%20Methods.md#Secondary>).

To define ESTIMATE outputs:

  1. Display the **ESTIMATE** screen.

  2. Select the **Files** tab.

  3. Select the **Output** tab.

  4. Choose a **Grade Model** file. See [Grade Estimation Output Models](<Advanced%20Estimation%20Validation.md>).

  5. The Sample Output File is optional, and records the weight of each sample for each cell, for each grade estimated. See [Grade Estimation Output and Results](<Grade%20Estimation%20Output%20and%20Results.md>).

  6. **ESTIMATE** uses a set of parameter files to control the estimation process, and it generates these beforehand. Some estimation methods require specific parameter files. 

Here, you define the names of the files created and used by **ESTIMATE** :

     * If **Use Defaults** is **checked** , parameter files are generated with default names (estparsv, estparep and estparvm).

     * If **Use Defaults** is **unchecked** , you can choose either an existing parameter file to control estimation, or set a custom parameter file name to be input and output. The content of each file is determined by settings made later, using the **[Search Volumes](<Estimate_Search.md>)** , **[Variogram Models](<Estimate_Variogram.md>)** and **[Estimation](<Estimate_Estimation.md>)** tabs.

  7. Click **Next** to proceed to the **[Unfolding](<Estimate_Unfolding.md>)** screen.

Related topics and activities

  * [ESTIMATE: Unfolding](<Estimate_Unfolding.md>)

  * [ESTIMATE: Search Volumes](<Estimate_Search.md>)

  * [ESTIMATE: Variogram Models](<Estimate_Variogram.md>)

  * [ESTIMATE: Estimation](<Estimate_Estimation.md>)

  * [ESTIMATE: Controls](<estimate_controls.md>)

  * [ESTIMATE: Preview](<Estimate_Preview.md>)

  * [Introduction to Grade Estimation and Interpolation](<Advanced%20Estimation%20Validation.md>)

  * [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)

  * [Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>)

  * [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)

  * [Grade Estimation Output and Results](<Grade%20Estimation%20Output%20and%20Results.md>)