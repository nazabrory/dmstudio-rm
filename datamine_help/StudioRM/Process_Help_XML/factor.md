# FACTOR Process

To access this process:

  * **Sample Analysis** ribbon **> > Geochemical Processes >> R Mode Factor Analysis**.
  * Enter "FACTOR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FACTOR** and click **Run**.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_F.md#FACTOR>)](<../command_help/COMMAND%20TABLE_E.md#EXTEND>).

## Process Overview

Define a number of factors from the common inter-correlation between variables using the correlation (R) matrix.

R - mode factor analysis using the unrotated, varimax and promax rotated correlation matrix to classify variables into groups (factors) and calculate factor scores. This defines a number of factors from the common inter-correlation between variables using the correlation (R) matrix.

Note the difference from the principal components analysis which uses variance. The number of factors selected is usually less than the number of variables. Three types of factor loadings are calculated, a) the un-rotated solution, ie principal components, b) the rotated varimax solution and c) the oblique promax solution. 

Statistical factor analysis is completed by iterative calculation of the un-rotated factor matrix. Non- statistical factor analysis is completed by a single pass only, ie. the varimax and promax rotations are non statistical. The number of factors selected can be forced by defining a given eigen value or a given number of factors. Significance levels are calculated using the Burt-Banks equation.

### FACTOR and PCA Processes

Note the difference from the [principal components analysis](<pca.md>) calculation, which uses variance. 

The number of factors selected is usually less than the number of variables. Three types of factor loadings are calculated, a) the un-rotated solution, ie principal components, b) the rotated varimax solution and c) the oblique promax solution. Statistical factor analysis is completed by iterative calculation of the un-rotated factor matrix. Non- statistical factor analysis is completed by a single pass only, ie. the varimax and promax rotations are non statistical. The number of factors selected can be forced by defining a given eigen value or a given number of factors. Significance levels are calculated using the Burt-Banks equation.

### File Handling

The input data file (&**IN**) must have sample identifier field (@**SAMPID**) which has to be declared on input. Optional output files, for un-rotated (&**SCORES**), rotated (**RSCORES**) and oblique rotated (&**OSCORES**) are available for farther processing.

If the user wishes to plot maps of the output scores then the scores files can be joined to the original input file using the **[JOIN](<join.md>)** process and defining **SAMPID** as the keyfield.

**Note** : There is a limit of 45 variables. There is no limit on the number of samples.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
USCORES |  Output |  No |  Undefined |  Optional output file for unrotated factor scores.  
RSCORES |  Output |  No |  Undefined |  Optional output file for varimax factor scores.  
OSCORES |  Output |  No |  Undefined |  Optional output file for promax factor scores.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPID |  Field containing sample identification |  IN |  Yes |  Any |  Undefined  
F1 |  First field to be used. No fields specified means all. |  IN |  No |  Numeric |  Undefined  
F2-F10 |  Second and subsequent fields to be used. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MAXIT |  Number of iterations required, valid only for the unrotated PCA option in factor analysis. =(0) Non statistical factor analysis. =10 Maximum number of iterations allowed for statistical factor analysis. |  No |  0 |  0,10 |  0,1,2,3,4,5,6,,7,8,9,10  
EIGENMIN |  |  Option |  Description  
---|---  
(1) |  Eigenvalue required to select the number of components.  
No |  1 |  Undefined |  Undefined  
NUMEIGEN |  |  Option |  Description  
---|---  
(0) |  Maximum number of eigenvalues is set to the number of fields or to 10, whichever is the lower.  
No |  0 |  Undefined |  Undefined  
PROMAXCF |  |  Option |  Description  
---|---  
(3) |  Promax oblique rotation exponent. Range is 1-9.  
No |  3 |  1,9 |  Undefined  
PRINT |  > 0 Display scores on the screen (0). Note - Do not use for large files. |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !FACTOR &IN(SEDDET),&USCORES(USCORES),&OSCORES(OSCORES),  
  
---  
      
    
    @SAMPID='ID',@MAXIT=0,@EIGENMIN=1,@NUMEIGEN=0,  
      
    
    @PROMAXCF=3,@PRINT= 0  
  
## Error and Warning Messages

Message |  Description  
---|---  
*** Warning *** GROUPID field has more than three words. Only the first 3 will be used. |   
>>> ERR 122 <<< ( fileno.) IN FACTOR |  No numeric fields on file (filename)  
>> ERR 120 <<< ( fileno.) IN FACTOR |  Compulsory file, field or parameter missing.  
*** Error *** Failure in matrix inversion, check data. |   
*** Error *** Failure in inversion during oblique rotation, check data. |   
  
Related topics and activities

  * [PCA Process](<pca.md>)

  * [JOIN Process](<join.md>)