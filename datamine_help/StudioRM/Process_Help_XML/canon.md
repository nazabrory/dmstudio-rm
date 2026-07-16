# CANON Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Geochemical Processes >> Canonical Correlation**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CANON** and click **Run**.
  * Enter "CANON" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CANON>).

## Process Overview

Canonical analysis can be used to define possible mineralized and background samples by the calculation of canonical vectors and scores on the basis of two variates, left (mineralized) and right (background).

The number of fields for the left hand variate e.g.. mineralization, is specified by the user (@**NLEFT**). Obviously, it helps to have a pre-conceived idea of the data structure prior to analysis, i.e.. the number of fields to define for the left hand variate and the relevant fields to include as significant in defining the variates in the analysis.

Two variates are calculated from the linear correlation matrix (R) by the progressive selection of eigen values and eigen vectors. Once obtained, they are used to calculate the canonical vectors and canonical scores for each sample.

File Handling

Input data (&**IN**) has to contain a sample identifier (@**SAMPID**) which must be specified on input. The left hand variate fields must be the first fields occurring in the datafile &**IN**. If not, the data has to be sorted on the required left hand variate fields (keyfields) prior to analysis. Extra control can be applied by the selection of fields using field and/or retrieval criteria. The calculated correlation matrix (R), canonical vectors and significance tests are displayed and/or sent to a print file.

Canonical scores may be sent to an optional output file (&**SCORES**) which can be joined to the primary data using the **SAMPID** as a keyfield. The canonical scores with their associated grid coordinates can now be used for later data manipulation and map plotting.

**Note** : There is a restriction of 45 variables but there is no limit on the number of samples. If missing data values are present in the sample then the sample record is ignored. It is necessary to have the fields for the left hand variate defined as the first fields in the datafile.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
SCORES |  Output |  No |  Undefined |  Optional output file for canonical root scores.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPID |  Field containing sample identification |  IN |  Yes |  Undefined |  Undefined  
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
NLEFT |  Number of fields or variables in left hand part of the variate (1). | No | 1 | 0,64 | Undefined  
PRINT |  > 0 Display results on the screen (0). | No | 0 | 0,1 | 0,1  
  
## Example
    
    
    !CANON  
  
---  
      
    
    &IN(SEDDET), &SCORES(SCORES), @SAMPID='ID', >@NLEFT= 5  
  
## Error and Warning Messages

Message  
---  
*** Error *** No numeric fields on file (filename) >>> ERR 122 <<< ( fileno.) IN CANON  
*** Error *** Failure in matrix inversion, check data. *** Error *** Compulsory file, field or parameter missing. >>> ERR 120 <<< ( fileno.) IN CANON