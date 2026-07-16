# UNIFCOND Process

To access this process:

  * Enter "UNIFCOND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **UNIFCOND** and click **Run**.

  * Accessed via the **[Uniform Conditioning Wizard](<../Uniform_Conditioning/About_Uniform_Conditioning.md>)**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_U.md#UNIFCOND>).

## Process Overview

UNIFCOND performs uniform conditioning (UC).

UC is a non-linear estimation technique which is used to determine the distribution of SMU grades above specified values (cut-off-grades), inside a panel. The principle of the tool is that data exists to accurately estimate grade at a larger resource-level panel scale - but - you cannot accurately estimate the selective mining unit (SMU). This is more likely to be the case where sample data is limited, which is often the case at the start of operations such as during the exploration phase of a project. Linear estimation at this stage will commonly have the effect of smoothing estimates and displaying an apparent loss of ore and metal tonnage at high cut-off grades.

It is implemented interactively via the [Uniform Conditioning Wizard](<../Uniform_Conditioning/UniformConditioning_Introduction.md>).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SAMPLES |  A Datamine file that contains sample positional information and supporting attributes. |  Input |  Yes |  Undefined  
VGRAM | A Datamine experimental [variogram parameter file](<../COMMON/filetype.md#VariogramExp>) |  Input |  Yes |  Undefined  
INFOEFF | You can (optionally) incorporate the information effect to the estimation of the grade tonnage curves: during the production stage, the actual grades are recovered and may then be taken into account so the decision between ore and waste is made upon more accurate estimates of the SMUs. Therefore you can anticipate future decisions before obtaining the production blast-holes results, because only the kriging variance of these SMUs final estimates is necessary. |  Input |  No |  Undefined  
PANMODEL | A file containing the panel model to be conditioned. |  Input |  Yes |  Undefined  
CUTOFF |  A file specifying variably-spaced cut-off values.  The file should contain a field titled **CUTOFF** , which is a list of values to use instead of those in **CUTMIN** , **CUTINT** and **CUTNUM**. If @**CUTOFF** is specified, **CUTMIN** , **CUTINT** and **CUTNUM** parameters are ignored. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
UCMODEL |  Output |  Yes |  Undefined |  The output file containing the uniform conditioned panel model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
GRADE |  The grade field (present in the samples file) that will be considered during the process of Uniform Conditioning. |  IN |  Yes |  Alphanumeric |  Undefined  
WEIGHT |  An optional weighting field. |  IN |  No |  Alphanumeric |  Undefined  
KRIGING |  The field in the input (panel) model containing kriged values to be conditioned. |  IN |  Yes |  Alphanumeric |  Undefined  
DISPVAR |  The field in the input (panel) model containing kriging variance data. |  IN |  Yes |  Alphanumeric |  Undefined  
ERRCODE |  The field in the input model containing [error code information](<../Uniform_Conditioning/UC%20Error%20Codes.md>), if present. |  IN |  No |  Alphanumeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VREFNUM |  A reference number relating to an experimental variogram as defined in **[VGRAM](<vgram.md>)**. |  No |  0 |  |   
DISCX |  Number of discretisation points in X direction as used for calculating the covariance of a cell with each of the surrounding samples. This is then used in calculating the kriging weights. | No | 5 |  |   
DISCY | Number of discretisation points in Y direction | No | 5 |  |   
DISCZ | Number of discretisation points in Z direction | No | 5 |  |   
NORMSILL |  If @**NORMSILL** =1 then the input variogram needs to be normalized by the process If @**NORMSILL** =0 then the input variogram model does not need to be normalized by the process | No | 0 | 0,1 | 0,1  
CLASSES |  Number of panel classes | No |  1 |  |   
CUTMIN | The minimum cutoff grade to be considered during Uniform Conditioning | No | 0 |  |   
CUTINT | The size of each grade cutoff interval | No | 10 |  |   
CUTNUM | The number of grade cutoff intervals to considered during Uniform Conditioning | No | 10 |  |   
NUMSMUX | Number of selective mining units (per panel) in the X direction | No | 1 |  |   
NUMSMUY | Number of selective mining units (per panel) in the Y direction | No | 1 |  |   
NUMSMUZ | Number of selective mining units (per panel) in the Z direction | No | 1 |  |   
GAOUT |  Set to 1 to include grade-above cutoffs in the output model. Set 0 to exclude grade-above cutoffs which allows 50% more cutoff intervals to be specified. | No | 1 | 0,1 | 0,1  
  
## Example
    
    
    !UNIFCOND   &SAMPLES(samples),   
  
---  
      
    
    &VGRAM(vgram1), &PANMODEL1(pan_mod), &SMUMODEL(SMU_mod)  
      
    
    *GRADE(AU), *KRIGING(OK),   *DISPVAR(DISP),   
      
    
    @CUTMIN=0, @CUTINT=0.5,   @CUTNUM=48,   
      
    
    @DISCX=5, @DISCY=5, @DISCZ=5, @NUMSMUX=4, @NUMSMUY=4,   
      
    
    @NUMSMUZ=4  
  
## Error Codes

Code | Description  
---|---  
0 | No tonnage correction was applied, all grades are consistent with the model  
1 | A tonnage correction has been applied and grades are still consistent with the model  
2 | A tonnage correction has been applied which has led to grade inconsistencies. This could be due to either: 

  * a mean grade below the specified cut-off
  * the grade of an interval is not lying between two cut-off values

  
3 | The difference between the panel grade and the grade calculated at the zero cut-off is larger than 1/10000, so that all metal quantities have been normalized before calculation.  
4 | The backtransformation of the panel's Kriged Value was not possible to calculate because the value falls outside the expected (Zmin, Zmax) interval of the model. All block/SMU values within such a panel are considered equal to the Kriged panel value Z to ensure that grades remain consistent within the model  
  
Related topics and activities

  * [UC Wizard - Introduction](<../Uniform_Conditioning/UniformConditioning_Introduction.md>)

  * [Uniform Conditioning: Error Codes](<../Uniform_Conditioning/UC%20Error%20Codes.md>)

  * [Change of Support](<../Uniform_Conditioning/About_Change_of_Support.md>)

  * [Gaussian Anamorphosis](<../Uniform_Conditioning/About_Gaussian_Anamorphosis.md>)

  * [Localized Uniform Conditioning](<../Uniform_Conditioning/About_Localized_Uniform_Conditioning.md>)

  * [The Information Effect](<../Uniform_Conditioning/About_Information_Effect.md>)

  * [VGRAM Process](<vgram.md>)