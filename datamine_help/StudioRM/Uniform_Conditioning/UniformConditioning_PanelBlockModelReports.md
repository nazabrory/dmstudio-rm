# Uniform Conditioning: UC Model Reports

To access this screen:

  1. Display the **[Uniform Conditioning](<UniformConditioning_Introduction.md>)** wizard.

  2. Select the **UC Model Reports** tab.

Apply [kriged](<../STUDIO_RM/Grade%20Estimation%20Kriging.md>) grade estimates at the panel scale into the model file selected on the [Input Data](<UniformConditioning_InputData.md>) screen of the **Uniform Conditioning** wizard.

To recap, the inputs to Uniform Conditioning are:

  * The kriged panel estimate of raw grades (either from a [samples file or an input geological model](<UniformConditioning_InputData.md>))
  * The [dispersion variance](<UniformConditioning_Decluster.md>) of estimated models
  * A point anamorphosis (transformation) function
  * A [variogram model](<UniformConditioning_Variograms.md>)

The output from this phase is an updated geological model file containing grade estimates relevant to predefined panel and Selective Mining Unit (SMU) dimensions - this is referred to as the 'Panel Model'. This captures the proportion of the SMU distribution above each cut-off grade. This is done by transforming the panel estimate and cutoff grade to Gaussian units, then calculating the tonnage of the mining units that are above the cutoff but within the target panel. The metal quantity is also calculated above the same cutoff grade.

See [Uniform Conditioning](<About_Uniform_Conditioning.md>)

The size of each SMU is determined by specifying a number of mining units in the X, Y and Z directions. You also use this screen to define the grade 'bins' for the panel model, using a simple process of defining the minimum grade and size of interval. The grade cutoffs will represent areas of interest for analysis. These could be chosen based on economic or mining parameters (e.g. low, medium, and high grade cutoff values).

You can choose to calculate kriged panel estimates using the input data model (and predefined search volumes located in a [Search Volume Parameter File](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Introduction.md>)) or to use existing kriged values that are already held within the input model file. If you choose the latter option, you will also need to select the kriged estimate and kriged variance column using the available drop-down lists.

The remainder of the screen is used to define panel size and SMU parameters to prepare for the generation of the panel block model. The SMU size will be based on the deposit type and mining equipment limitations. The panel size should be based on drillhole/sample spacing.

### Dispersion Variance

Dispersion variance (Variance of Z*) is an approximation of the variance of estimated block grades.

Using **COKRIG** or advanced estimation, Dispersion variance can be calculated directly by setting the field Variance of Z*. This is calculated when field **VARZSTR** is set in the COKRIG field parameter file.

Dispersion variance can also be calculated from the Kriging Variance, Block Variance (**BLOCKVAR**) and Lagrange parameter(**LAGRANGE**); where `DISPVAR= BLOCKVAR VAR + (2*LAGRANGE)`.

### Iso-Frequency Classes

The term iso-frequency (sometimes called _equiprobable_ classes) means that the classes are defined such that each one contains the same proportion of the global grade distribution (for example, each class represents 5% of the data if you choose 20 classes).

In other words: Instead of splitting grades into fixed numeric intervals (like 00.5%, 0.51.0%, etc.), UC defines classes based on quantiles of the global distribution, So that each class has an equal frequency of occurrence.

These classes are then used to calculate variance terms (dispersion variances, local/global CCDF relationships) that underpin the UC model.

Why does this matter?

  * Too few classes → the conditional distributions are coarse, and the recoverable resource estimates may be inaccurate.

  * Too many classes → computationally expensive and sometimes unstable.

Typically, practitioners might choose anywhere from 10 to 20 iso-frequency classes as a balance between resolution and stability, though the "best" number depends on your data, grade distribution, and block size.

Activity steps

  1. Choose how kriged values are calculated:

     * Calculate kriged values Calculate kriged panel estimates 'on the fly', you can select this option and a predefined Search Volume Parameter file.

     * Use kriged values from input model Use kriged values created from a previously kriged model, as found in the **Input Model** defined on the **[Input Data](<UniformConditioning_InputData.md>)** screen. 

       * Define **Kriged estimate** and Dispersion variance fields.

  2. Review the calculated **Panel Size** which represents the dimensions in XYZ of the input model parent cell size.

  3. Define the number of SMUs per panel. Enter the number of SMUs in XYZ directions within each panel. This is used to determine the size of the Selective Mining Unit (SMU).

  4. Review the SMU size, the calculated size in XYZ of the SMUs within each panel.

  5. Define cutoff values:

     * Use fixed cutoffs The number (and by implication, range) of grade intervals to report. Minimum defines a starting grade from which to create subsequent grade intervals. By default, it is zero. The Maximum value is automatically calculated based on the No. of cutoffs specified, and the size of each Interval. 

For example, a Minimum setting of '0', an Interval of '2' and No. of cutoffs of '6' will generate a Maximum cutoff grade of '10' (zero is classed as an interval).

     * Use custom cutoffs If you have a list of cutoff values in an external file (this file must contain at least one numeric attribute - CUTOFF, and at least one record), you can load it using this option and selecting a file.

  6. Set the Number of iso-frequency (variance) classes. Into how many equal-frequency bins should the global grade distribution be divided, for use in computing the conditional distributions in UC? See "Iso-Frequency Classes", above, for more information.

  7. Click Create UC block model to generate the panel model on disk when you are happy the parameters you have specified are correct.

  8. Click UC block model summary to display summary information relating to the generated panel model in the Studio Output window.

  9. Click View UC block model to load the generated panel model into Studio and display it.

  10. Progress to the [LUC Model Reports](<UniformConditioning_SmuBlockModelReports.md>) tab if you wish to investigate [localized uniform conditioning](<About_Localized_Uniform_Conditioning.md>) options, otherwise, close the **Uniform Conditioning** wizard and save your project.

Related topics and activities

  * [Uniform Conditioning - Introduction](<UniformConditioning_Introduction.md>)

  * [Uniform Conditioning \- Input Data](<UniformConditioning_InputData.md>)

  * [Uniform Conditioning \- Decluster](<UniformConditioning_Decluster.md>)

  * [Uniform Conditioning \- Variograms](<UniformConditioning_Variograms.md>)

  * [Uniform Conditioning - Grade Tonnage Curves](<UniformConditioning_GlobalGradeTonnageCurves.md>)

  * [Uniform Conditioning - SMU Model Reports](<UniformConditioning_SmuBlockModelReports.md>)

  * [Grade Estimation Search Volume Introduction](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Introduction.md>)

  * [Grade Estimation Search Volume Parameter File](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)

  * [Grade Estimation Kriging](<../STUDIO_RM/Grade%20Estimation%20Kriging.md>)

  * [About Uniform Conditioning](<About_Uniform_Conditioning.md>)

  * [About Localized Uniform Conditioning](<About_Localized_Uniform_Conditioning.md>)

  * [Uniform Conditioning Error Codes](<UC%20Error%20Codes.md>)