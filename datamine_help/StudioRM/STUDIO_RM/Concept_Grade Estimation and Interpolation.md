# Grade Estimation Processes

Note: This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) library, explaining key concepts relating to grade estimation in Studio RM. Whilst these topics directly reference [ESTIMA](<../Process_Help_XML/estima.md>) and the univariate case, many of these principles apply equally to multivariate estimation with the [COKRIG](<../Process_Help_XML/cokrig.md>) process and [advanced grade estimation](<Multivariate_Introduction.md>).

This topic outlines the different methods of interpolating grades into the model cells using a range of processes available in Studio RM.

A group of file-based processes underpin initial grade estimation in Studio RM.

  * GRADE The simplest command and has the least number of options. It is restricted to Nearest Neighbor (NN), Inverse Power of Distance (IPD) and Ordinary Kriging (OK) using a 1 or 2 structure spherical model variogram model. Only one grade can be estimated at a time. See **[GRADE](<../Process_Help_XML/grade.md>)**.  

  * ESTIMA Multiple grades can be estimated using multi-structure variogram models of different types. The interface is the standard files, fields, parameters dialog. See [[ESTIMA Process](<../Process_Help_XML/estima.md>)  
](<../Process_Help_XML/estima.md>)

  * INDEST Similar to ESTIMA except that it only offers Indicator Estimation. It uses the standard files, fields, parameters dialog. See **[INDEST](<../Process_Help_XML/indest.md>)**.

  * ESTIMATE Offers all the functionality of ESTIMA and INDEST (excluding unfolding) plus more through a tailored dialog. It includes the ability to save and restore search volume, estimation type and variogram model information through the use of parameter files. See **[ESTIMATE](<../Process_Help_XML/estimate.md>)**.

  * **COKRIG** Grade estimation using univariate and multivariate methods, including ordinary, simple kriging, inverse distance weighting and nearest neighbour. This process is used as part of the [Advanced Estimation](<Multivariate_Introduction.md>) wizard, although it can also be accessed independently via the command line as a standalone process. See [COKRIG Process](<../Process_Help_XML/cokrig.md>).

  * **KNA** Optimize the parameters for grade estimation. Typically multiple estimations are performed on a small number of blocks and the results are averaged for each estimation and compared to find an optimal set of parameters. The parameters are then used by the COKRIG process (see above) to estimate grades into a block model by a range of methods including Kriging. See [KNA Process](<../Process_Help_XML/kna.md>).

These commands require an input model to define the cell structure, and an input sample file to define the sample grades to be used for making the estimates. They then create an output model where the estimated grade is a field in the model file.

## The Model Prototype

All estimation methods require an input **prototype** block model into which the sample grades are interpolated. 

Typically, the prototype model will already contain cells and subcells defining the geology, enabling values to be interpolated into the existing cell structure. However, if the prototype model is empty, and sufficient samples exist within the search volume, then cells and subcells can be created easily by downstream processes (typically, in relation to input samples, estimation parameters, zone information, search volume specifications and so on - the extent and type of parameters depends on the type of estimation being performed).

You can use an existing model as a prototype, or create one using [PROTOM](<../Process_Help_XML/protom.md>) or the [Create Model Prototype](<../COMMON/CreateModelPrototype_Dialog.md>) screen.

A prototype model containing cells and sub-cells may also contain one or two classification fields, for example, rock type, lithology, weathering profile, or fault block zone. If the same classification field(s) also exist in the input sample file, then zone control can be selected. This means, for example, that only samples that are rock type A would be used to estimate cells that are rock type A.

## The Output Model

If the input model contains cells and sub-cells, then the output model will contain the same set of cells and sub-cells. It will also include additional fields corresponding to the grades that were estimated.

## The Input Samples

The input sample file must contain the three coordinate fields X, Y and Z, and at least one grade field. This will often be a desurveyed drillhole file which may also contain classification fields, if zone control is to be selected.

You can derive sample information from both static and dynamic drillhole data. For a strong connection to field data (that is, the operational drilling database), consider using the **[Drillhole Importer](<>)** as this allows drillholes to be rebuilt instantly in light of new ground data (and consider **Studio Geo** too, if you haven't already, as this connects the system to implicit and geological block modelling, allowing a true 'one click' solution for absorbing the latest sample information from the field).

## Grade Estimation Supporting Files

Grade estimation is supported by a set of data files that govern how the estimation should be performed. These files can be used interchangeably between ESTIMA and COKRIG (and their associated tools), but there are subtle differences in their interpretation in each case (see [Advanced Estimation - Case Study](<Advanced%20Estimation%20Validation.md>)).

### Search Volume Parameters

A Search Volume (often referred to as the "SPAR" file) is a 3D shape containing the samples to be used for the grade estimation, and is centered on the cell being estimated. The volume may be either a 3D ellipsoid or a cuboid. All methods require a search volume.

For GRADE, a single search volume is defined in the parameters tab, whereas the other commands (**ESTIMA** , **ESTIMATE** , **INDEST**) allow multiple search volumes which are stored in a Search Volume Parameter file. The **ESTIMATE** command provides specific dialogs to facilitate the definition, import and export of search volumes. Multiple search volumes allow different grades to be estimated with different search volumes.

### Variogram Model Parameters

If [kriging](<Grade%20Estimation%20Kriging.md>) is selected as one of the estimation methods, then a variogram model must be defined. As for search volumes, **GRADE** allows a single model to be defined through the parameters tab, whereas **ESTIMA** provides specific dialogs for definition, and import and export to and from the Variogram Model Parameter file. Variograms are calculated using the **VGRAM** command, and models fitted using **[VARFIT](<../Process_Help_XML/varfit.md>)**.

The file used to store this information is often called the "VPAR" file.

### Estimation Type Parameters

It is necessary to provide a set of estimation parameters for each grade to be estimated. For **GRADE** with a single estimate these parameters are defined on the parameters tab. For the other processes, the parameters may be imported as an Estimation Parameter file. **ESTIMATE** provides dialogs to define and save these parameters. The parameters include the estimation method, the search volume reference number and estimation-method-specific data such as the power, if the Inverse Power of Distance method has been selected.

This file is commonly labelled the "EPAR" file. I know right? Acronyms....

## Uniform Conditioning

Uniform Conditioning provides a method for creating a model that is representative of the variability of the deposit for a defined SMU, which if used for mine planning and reserve calculation can increase the confidence in the resulting reports and mine plans. 

The main aim of Localized Uniform Conditioning (LUC) is to assign grades to each SMU within a panel such that the distribution of SMU grades is the same as the distribution of grades for the same panel in the UC model.

Uniform conditioning is managed by the **[Uniform Condition Wizard](<../Uniform_Conditioning/UniformConditioning_Introduction.md>)** , which is supported by another group of processes:

  * **GAUSANAM** Transforms a variable Y with a gaussian distribution in a new variable Z with any distribution. From a pragmatic viewpoint, this means transforming a non-Gaussian distribution into a Gaussian distribution (anamorphosis means transformation). See [GAUSANAM Process](<../Process_Help_XML/gausanam.md>).

  * **LUNICOND** Provide a more 'intuitive' presentation of uniform conditioning result by assigning a unit-level mean average grade based on calculations of the tonnages and grades above each cut-off grade, dispersed within the panel according to their rank. See [LUNICOND Process](<../Process_Help_XML/lunicond.md>).

  * **SUPPCORR** Estimate the histogram of blocks for the entire domain, from the point histogram. See [SUPPCORR Process](<../Process_Help_XML/suppcorr.md>).

  * **UNIFCOND** Use the inputs from the processes above to perform a non-linear estimation technique which is used to determine the distribution of SMU grades above specified values (cut-off-grades), inside a panel. See [UNIFCOND Process](<../Process_Help_XML/unifcond.md>).

For more information, see [Uniform Conditioning](<../Uniform_Conditioning/About_Uniform_Conditioning.md>).

Related topics and activities

  * [ESTIMA Process](<../Process_Help_XML/estima.md>)

  * [ESTIMATE Process](<../Process_Help_XML/estimate.md>)

  * [GRADE Process](<../Process_Help_XML/grade.md>)

  * [INDEST Process](<../Process_Help_XML/indest.md>)

  * [COKRIG Process](<../Process_Help_XML/cokrig.md>)

  * [Grade Estimation with ESTIMA](<Grade%20Estimate%20Overview.md>)

  * [Advanced Estimation & Variography](<Multivariate_Introduction.md>)