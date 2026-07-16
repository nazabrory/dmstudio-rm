# PCA Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Geochemical Processes >> Principal Components Analysis**.

  * Enter "PCA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PCA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PCA>).

## Process Overview

Principal Components Analysis groups fields together into components on the basis of the correlation (R) or variance/covariance (C) matrix.

Each component is determined to maximize the total variance. Note, this is different to Factor Analysis which maximizes the inter-correlation between components. Multiple options are available by selecting the type of matrix, type of principal component loading and type of scores to calculate for each sample.

The number of groups or components required can be set directly by setting the number of eigen values (@**NUMEIGN**). If the default value of zero is entered then the number of components selected will be as follows:

  * R-matrix, number of eigen values exceeding @**EIGENMIN** , default is 1.0.

  * C-matrix, number of eigen values whose cumulative percentage of variance exceeds @**MAXVAR** , default is 95 percent.

  * Number of fields selected for analysis.

### File Handling

The input file (&**IN**) must have a separate sample identifier field (* **SAMPID**) which has to be declared on input. There is the optional facility (&**SCORES**) to output the calculated principal component scores for farther processing.

If the user wishes to plot maps of the output scores then the **SCORES** file can be joined to the original input file using the **[JOIN](<join.md>)** process and defining **SAMPID** as the keyfield.

### Process Limits

There is currently a restriction of 45 variables. There is no limit on the number of samples. 

On the basis of **MATXTYPE, LOADEIGN** and **SCNORM** there are eight options available for PCA analysis, the following five are recommended:

MATXTYPE |  LOADEIGN |  SCNORM  
---|---|---  
0: R-Matrix  |  1: Eigen vector scores  |  1: Scores not normalized  
0: R-Matrix  |  0: PC factor loadings  |  0: Normalized scores  
1: C-Matrix  |  1: Eigen vector scores  |  1: Scores not normalized  
1: C-Matrix  |  1: Eigen vector scores  |  0: Normalized scores  
1: C-matrix  |  0: PC factor loadings  |  0: Normalized scores  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
SCORES |  Output |  No |  Undefined |  Optional output file for principal component scores.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPID |  Field containing sample identification |  IN |  Yes |  Any |  Undefined  
F1 |  First field to be used. No fields specified means all. |  IN |  No |  Numeric |  Undefined  
F2 |  Second field to be used. |  IN |  No |  Numeric |  Undefined  
F3 |  Third field to be used. |  IN |  No |  Numeric |  Undefined  
F4 |  Fourth field to be used. |  IN |  No |  Numeric |  Undefined  
F5 |  Fifth field to be used. |  IN |  No |  Numeric |  Undefined  
F6 |  Sixth field to be used. |  IN |  No |  Numeric |  Undefined  
F7 |  Seventh field to be used. |  IN |  No |  Numeric |  Undefined  
F8 |  Eighth field to be used. |  IN |  No |  Numeric |  Undefined  
F9 |  Ninth field to be used. |  IN |  No |  Numeric |  Undefined  
F10 |  Tenth field to be used. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MATXTYPE |  Matrix type to be used to calculate components. |  Option |  Description  
---|---  
(0) |  R matrix, standardised Z values of original data.  
No |  0 |  0,1 |  0,1  
EIGENMIN |  |  Option |  Description  
---|---  
(1) |  Eigenvalue required to select the number of components. Used in the R-matrix only, ie. when MATXTYPE = 0. Used also when NUMEIGEN = 0.  
No |  1 |  Undefined |  Undefined  
NUMEIGEN |  |  Option |  Description  
---|---  
(0) |  Maximum number of eigenvalues is set to the number of fields or to 10, whichever is the lower. Note that if a non default value of MAXVARPC is used, NUMEIGEN must be 0.  
No |  0 |  Undefined |  Undefined  
MAXVARPC |  Specific to the selection of the variance/covariance matrix for analysis ie. MATXTYPE=1. The cumulative percentage of variation (95) required from the eigen values to select the number of eigen values for the analysis. Used when NUMEIGEN=0. |  No |  95 |  Undefined |  Undefined  
SCNORM |  |  Option |  Description  
---|---  
(0) |  Normalised scores calculated.  
1 |  Scores are not normalised.  
No |  0 |  0,1 |  0,1  
LOADEIGN |  |  Option |  Description  
---|---  
(0) |  Use factor loadings to calculate scores.  
1 |  Use eigenvalues to calculate scores.  
No |  0 |  0,1 |  0,1  
PRINT |  > 0 Display scores on the screen (0). Note - Do not use for large files. |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !PCA &IN(SEDDET), &SCORES(SCORES), @SAMPID='ID',   
  
---  
      
    
    @MATXTYPE=0, @EIGENMIN=1, @NUMEIGEN=0,@SCNORM=0,   
      
    
    @LOADEIGN=0, @PRINT=0  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERROR 120 <<< ( fileno.) IN PCA |  Compulsory file, field or parameter missing.  
>>> ERROR 122 <<< ( fileno.) IN PCA |  No numeric fields in the file.