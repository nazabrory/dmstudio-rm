# SUPPCORR Process

To access this process:

  * This process is used by the [Uniform Conditioning Wizard](<../Uniform_Conditioning/UniformConditioning_Introduction.md>).

  * Enter "SUPPCORR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUPPCORR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUPPCORR>).

## Process Overview

The core objective of the change of support model is to estimate the histogram of blocks for the entire domain, from the point histogram.

In a discrete gaussian model (DGM), knowing the distribution of sample point values is equivalent to knowing the anamorphosis. The distribution of point data is completely represented by the anamorphosis function.

The distribution of blocks can also be modeled by the block [anamorphosis](<../Uniform_Conditioning/About_Gaussian_Anamorphosis.md>) function. These two anamorphoses are directly related in the framework of DGM as the resulting Gaussian point and block distributions are assumed to be bi-Gaussian and a _coefficient_ can be calculated. This coefficient is directly related to the variance reduction between the raw point distribution and that of a particular support.

[![](../Images/unicon19.gif)](<javascript:void\(0\);>)

Once a change of support model like DGM is implemented one can apply cutoffs to a block histogram model and then calculate the metal,% of grade above cutoff and mean grade above cutoff for the SMU support. This change of support, when applied to the entire domain, is said to be global. Its application on a local basis is also possible (e;g. panel by panel) and then yields local recoverable resource estimates, which can be obtained amongst other methods via [Uniform Conditioning](<../Uniform_Conditioning/About_Uniform_Conditioning.md>).

The distribution of raw Z(x) points is transformed into a Normal distribution Y(x) through a process known as [Gaussian Anamorphosis](<../Uniform_Conditioning/About_Gaussian_Anamorphosis.md>).

Support correction is implemented interactively via the [Uniform Conditioning Wizard](<../Uniform_Conditioning/UniformConditioning_Introduction.md>).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SAMPLES |  A Datamine file that contains sample positional information and supporting attributes. |  Input |  Yes |  Undefined  
VGRAM | A Datamine experimental [variogram parameter file](<../COMMON/filetype.md#VariogramExp>) |  Input |  Yes |  Undefined  
SMUSIZES |  A file containing the sizes of Selective Mining Units (SMUs) |  Input |  Yes |  Undefined  
INFOEFF | You can (optionally) incorporate the information effect to the estimation of the grade tonnage curves: during the production stage, the actual grades are recovered and may then be taken into account so the decision between ore and waste is made upon more accurate estimates of the SMUs. Therefore you can anticipate future decisions before obtaining the production blast-holes results, because only the kriging variance of these SMUs final estimates is necessary. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
GRAPH |  Output |  No |  Undefined |  A file containing the data required to construct scatter plot and histogram graphs relating to a locally-conditioned SMU model.  
STATS |  Output |  No |  Undefined |  A file containing summary statistical data (in Datamine binary format) relating to a locally-conditioned SMU model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
GRADE |  The grade field (present in the samples file) that will be considered during the process of Uniform Conditioning. |  IN |  Yes |  Alphanumeric |  Undefined  
WEIGHT |  An optional weighting field. |  IN |  No |  Alphanumeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VREFNUM |  A reference number relating to an experimental variogram as defined using **[VGRAM](<vgram.md>)**. |  No |  0 |  |   
DISCX |  Number of discretisation points in X direction as used for calculating the covariance of a cell with each of the surrounding samples. This is then used in calculating the kriging weights. | No | 5 |  |   
DISCY | Number of discretisation points in Y direction | No | 5 |  |   
DISCZ | Number of discretisation points in Z direction | No | 5 |  |   
NORMSILL |  Use (1) or; don't use (0) normalized variogram sill values during grade-tonnage curve generation. | No | 0 | 0,1 | 0,1  
ANGLE1/2/3 |  Specify the first, second and/or third rotation angles, in degrees, to specify block anisotropy | No | 0 |  |   
AXIS 1/2/3 | First, second and third rotation axes. 1=X, 2=Y, 3=Z. The first rotation is by **ANGLE1** degrees clockwise around axis **AXIS1** , when viewed along the axis from positive values towards the origin. 2nd is **ANGLE2** and so on. | No | 0 |  |   
  
## Example
    
    
    !SUPPCORR &SAMPLES(samples),  &SMUSIZES(smu),   
  
---  
      
    
       &GRAPH(s_graph),   &STATS(s_stats)*GRADE(AU),   *WEIGHT(DENSITY),  @VREFNUM=2,   
      
    
     @DISCX=5, @DISCY=5, @DISCZ=5, @NUMSMUX=4, @NUMSMUY=4, @NUMSMUZ=4,  
  
Related topics and activities

  * [UC Wizard - Introduction](<../Uniform_Conditioning/UniformConditioning_Introduction.md>)