# Uniform Conditioning: LUC Model Reports

To access this screen:

  1. Display the **[Uniform Conditioning](<UniformConditioning_Introduction.md>)** wizard.

  2. Select the **LUC Model Reports** tab.

Resource model grades are traditionally estimated into blocks whose size is representative of the drillhole/sample spacing. However, recoverable reserves depend in part on the variability of grade at a Selective Mining Unit (SMU) size. The main idea is based on assigning to each block (SMU) a grade such that the distribution of block grades in the panel finds back the local grade tonnage curve estimated by Uniform Conditioning (UC).

Once a panel model has been generated (on the [previous screen](<UniformConditioning_PanelBlockModelReports.md>)) as a result of Uniform Conditioning, you can post-process the model to estimate resources at a more granular level - the SMU using a process known as Localised Uniform Conditioning or LUC. 

This is a post-processing phase to UC which assigns within each Panel a grade value to each SMU (Selective Mining Unit) whilst preserving the local grade tonnage curve of SMUs estimated by the preceding process. The goal of Localized Uniform Conditioning is to provide a more 'intuitive' presentation of uniform conditioning result, for example this could be a higher dispersion of grade obtained in LUC than direct block kriging.

The overall goal is provide a more 'intuitive' presentation of the results of Uniform Conditioning.

See [Localized Uniform Conditioning](<About_Localized_Uniform_Conditioning.md>).

Activity steps

  1. Display the **Uniform Conditioning** wizard.

  2. Define input data. See [Uniform Conditioning: Input Data](<UniformConditioning_InputData.md>).

  3. Decluster the input data. See [Uniform Conditioning: Decluster](<UniformConditioning_Decluster.md>)

  4. Specify variograms for conditioning. See [Uniform Conditioning: Variograms](<UniformConditioning_Variograms.md>).

  5. Specify global grade tonnage curve parameters. See [Uniform Conditioning: Global G/T Curves](<UniformConditioning_GlobalGradeTonnageCurves.md>).

  6. Generate model reports. See [Uniform Conditioning: UC Model Reports](<UniformConditioning_PanelBlockModelReports.md>).

  7. Display the **LUC Model Reports** screen.

  8. Choose how a localized model prototype is generated:

     * Create Prototype from SMU block sizes: if the selective mining unit dimensions are known, select this option to enter them manually, using the following field:

       * Define the SMU Size. These are the dimensions of the mining units within each panel that will ultimately receive a locally (and uniformly) conditioned grade value.

     * Create Prototype from SMU model: to extract SMU dimensions from an existing SMU model, select this option and browse for a file.

       * If you select this option, you can also use estimates within the SMU model during localized uniform conditioning (Use estimates from SMU model for localisation). If you do this, you'll need to define a Grade field within the selected model.

  9. Browse for a [Search Volume Parameter File](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>) or enter the name of a file in the current project directory.

  10. Select a Reference Number. The selected **Search Volume Parameter file** will contain an **SREFNUM** data column (effectively, the identifier for a search volume within the data file - there can be more than one). 

  11. Review the LUC block model automatically-generated name of the SMU model (the locally-conditioned model) that will be created on disk when Create SMU block model is selected.

  12. Click Create LUC block model to perform localized uniform conditioning on the previous panel model and generate an SMU model on disk.

  13. Click LUC block model summary to generate a scatter plot (as a new plot sheet) showing the distribution of locally-conditioned grades throughout the SMU model. Another sheet is also generated, showing 3 histograms:

     * The frequency of Kriged values (above a zero cut-off) as represented by the panel model.

     * The frequency of grades resulting from ordinary Kriging as stored in the SMU model - this is provided for comparison against the locally-conditioned output (below). Note that, as the locally conditioned output is bound by the kriged value at the panel support level, the mean value across the range should be very close or identical between top and bottom graphs.

     * The frequency of grades in the locally-conditioned model.

  14. Click View LUC block model to load the generated SMU model into memory and display it in Studio.

  15. Close the Uniform Conditioning wizard.

  16. Save your project.

Related topics and activities

  * [Uniform Conditioning - Introduction](<UniformConditioning_Introduction.md>)

  * [Uniform Conditioning \- Input Data](<UniformConditioning_InputData.md>)

  * [Uniform Conditioning \- Decluster](<UniformConditioning_Decluster.md>)

  * [Uniform Conditioning \- Variograms](<UniformConditioning_Variograms.md>)

  * [Uniform Conditioning - Grade Tonnage Curves](<UniformConditioning_GlobalGradeTonnageCurves.md>)

  * [Uniform Conditioning - Panel Model Reports](<UniformConditioning_PanelBlockModelReports.md>)

  * Uniform Conditioning - SMU Model Reports

  * [About Localized Uniform Conditioning](<About_Localized_Uniform_Conditioning.md>)

  * [Grade Estimation Search Volume Introduction](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Introduction.md>)

  * [Grade Estimation Search Volume Parameter File](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)

  * [Uniform Conditioning Error Codes](<UC%20Error%20Codes.md>)