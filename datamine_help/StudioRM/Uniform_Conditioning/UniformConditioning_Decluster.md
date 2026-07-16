# Uniform Conditioning: Decluster

To access this dialog:

  * Display the **[Uniform Conditioning](<UniformConditioning_Introduction.md>)** wizard.

  * Select the **Decluster** tab.

Set up declustering options to uniformly distribute sample points as an aide to the [Uniform Conditioning](<About_Uniform_Conditioning.md>) process.

## Declustering Options

Declustering is the process of weighting data points in densely sampled areas, to obtain a more representative distribution of grades. This phase of the process will create a temporary points file (as indicated) containing declustered sample information.

You can decluster data using the following options:

  * Samples are already declustered

Use the [DECLUST](<../Process_Help_XML/declust.md>) process beforehand. In this situation, the input samples file (as specified on the [Input Data](<UniformConditioning_InputData.md>) screen) already contain a numeric field containing declustered values for each data row. Selecting this option, and the predefined declustered data field, will ensure these values are fed into the Uniform Conditioning process that follows.

  * Samples are on a regular grid; an equal weight will be applied to all samples

In this case, samples are already dispersed across a regular grid and you wish to select a single sample from each grid cell. An equal weighting (in effect, a weighting of '1') is applied to all samples.

  * Decluster samples to produce declustered weight

The "in process" option. Decluster samples to calculate a weight - where you wish toassign every sample a target weight based on the number of samples in the grid cell, which is defined manually in terms of size and origin. 

Note: This option actually runs **DECLUST** as a precursor to the Uniform Conditioning calculation.

If the **Decluster samples...** method is chosen then the weight, **DCWEIGHT** , for a sample is calculated as:

DCWEIGHT = NDATA / NCELLS / NPERCELL

where:

  * NDATA is the total number of samples

  * NCELLS is the number of grid cells containing one or more samples

  * NPERCELL is the number of samples in the grid cell

The sum of the weights over all samples equals the total number of samples (**NDATA**). Therefore if a sample lies in a high density area it will have a weight of less than 1, and if it is in a low density area it will have a weight of more than 1. The output file from this method can be used to transform data into a normal distribution, for input to the **NSCORE** or **SGSIM** processes.

This stage of the process will model the declustered multivariate sample histogram in the form of a declustered samples data file. This is used in the next stage, creating [variograms](<UniformConditioning_Variograms.md>) and [global grade/tonnage curves](<UniformConditioning_GlobalGradeTonnageCurves.md>).

### Dispersion Variance

Dispersion variance (Variance of Z*) is an approximation of the variance of estimated block grades.

Using **COKRIG** or advanced estimation, Dispersion variance can be calculated directly by setting the field Variance of Z*. This is calculated when field **VARZSTR** is set in the COKRIG field parameter file.

Dispersion variance can also be calculated from the Kriging Variance, Block Variance (**BLOCKVAR**) and Lagrange parameter(**LAGRANGE**); where `DISPVAR= BLOCKVAR VAR + (2*LAGRANGE)`.

Activity steps

  1. Display the Uniform Conditioning screen.

  2. Define your input data. See [Uniform Conditioning: Input Data](<UniformConditioning_InputData.md>).

  3. Select the **Decluster** tab.

  4. Choose a declustering option (see "Declustering Methods", above.

     * Samples are already declustered

       * Choose a Declustered weight field.

     * Samples are on a regular grid

     * Decluster samples to produce declustered weight

Define a regular 3D grid that is used to calculate the declustered weight values for each data row, based on the number of samples contained within each grid cell. One of the problems with the declustering method is that different grid sizes will generate different statistics. However, in general a regular grid about the size of the average sample spacing is suggested.

  5. Click **Run** to create the output declustered samples file based on either the values in the input samples file, a static weighting value or the calculation of weighting as performed by the **DECLUST** process.

  6. Review Declustered samples are stored in: This is the name of the temporary file created that contains declustered sample information, ready for use in generating global Grade Tonnage curves.

  7. Continue to the **[Variograms](<UniformConditioning_Variograms.md>)** screen.

Related topics and activities

  * [Uniform Conditioning - Introduction](<UniformConditioning_Introduction.md>)

  * [Uniform Conditioning - Input Data](<UniformConditioning_InputData.md>)

  * [Uniform Conditioning - Variograms](<UniformConditioning_Variograms.md>)

  * [Uniform Conditioning - Grade Tonnage Curves](<UniformConditioning_GlobalGradeTonnageCurves.md>)

  * [Uniform Conditioning - Panel Model Reports](<UniformConditioning_PanelBlockModelReports.md>)

  * [Uniform Conditioning - SMU Model Reports](<UniformConditioning_SmuBlockModelReports.md>)

  * [The Studio DECLUST process](<../Process_Help_XML/declust.md>)

  * [About Uniform Conditioning](<About_Uniform_Conditioning.md>)