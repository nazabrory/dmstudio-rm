# DISCAN Process

To access this process:

  * **Sample Analysis** ribbon **> > Geochemical Processes >> Multiple Discriminant Analysis**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DISCAN** and click **Run**.
  * Enter "DISCAN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DISCAN>).

## Process Overview

The calculation of discriminant functions (Discriminant analysis) will establish a set of rules using geological control groups or training sets which can then be applied to the classification of unknown samples using the [DISCLA](<discla.md>) process.

As a check, the rules as defined by the discriminant functions and group centroids can then be used to reclassify the training sets to see how many mismatches occur.

The linear discriminant function can be considered as a planer separating boundary between the different groups as classified by their input variables (fields) such as CU, PB and ZN. The group centroids are the fixed positions in space locating the centres of each group cluster as defined by the variables.

**Note** : there is a maximum limit of 10 control groups and 45 variables. All individual control groups must also be appended into one file prior to analysis.

### File Handling

The input file (&**IN**) must contain a sample identifier field (@**SAMPID**) and a group identifier field (@**GROUPID**). Data from the different control groups must have a unique identifier common to all samples within the group. All the different control groups must be put into one file using the **APPEND** process before using **DISCAN**. The group identifier will be representative of a geological control group, eg. to identifier them as granite, mineralised zone, background, lithology A or lithology B etc..

There are optional output files for the calculated discriminant functions (&**FUNCTS**), group centroids (&**CENTRDS**) and discriminant scores *&(**SCORES**). If the multiple discriminant functions and group centroids are required to classify unknown data in the **[DISCLA](<discla.md>)** process then the relevant output files must be named. If an output file of the re-classified control data is required then the file &**SCORES** must be used.

If the user wishes to plot maps of the output scores then the scores file can be joined to the original input file using the **[JOIN](<join.md>)** process and defining **SAMPID** as the key field.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. Must contain group and sample identity fields. A maximum of ten groups are evaluated. The file must be sorted on the *GROUPID field. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
CENTRDS |  Output |  No |  Undefined |  Optional output file containing group centroids identified by the field named in GROUPID.  
FUNCTS |  Output |  No |  Undefined |  Optional output file containing discriminant functions.  
SCORES |  Output |  No |  Undefined |  Optional output file containing the calculated scores for the individual samples and a misclassification field.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
GROUPID |  Compulsory group identifier field contained in input file IN. |  IN |  Yes |  Alphanumeric |  Undefined  
SAMPID |  Compulsory sample identifier field contained in input file IN. |  IN |  Yes |  Any |  Undefined  
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
RESUM |  |  Option |  Description  
---|---  
(0) |  Do not print summary statistics.  
1 |  Do print summary statistics.  
No |  0 |  0,1 |  0,1  
PRIMAT |  |  Option |  Description  
---|---  
(0) |  Option to display sums of squares matrices. Set to 1 for matrices to be displayed.  
No |  0 |  0,1 |  0,1  
PRISCO |  |  Option |  Description  
---|---  
(0) |  Option to display group scores. Set to 1 for scores to be displayed. Note: do not use for large files.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !DISCAN &IN(GG), &CENTRDS(GGCENT), &FUNCTS(GGFUNCTS),   
  
---  
      
    
               
      
    
    @GROUPID='GROUPID', @SAMPID= 'ID', @RESUM=1, @PRIMAT=1  
  
## Error and Warning Messages

Message  
---  
*** Warning *** GROUPID field has nn words. Only the first 3 will be used.  
*** Warning *** SAMPID field has nn words. Only the first 3 will be used  
*** Error *** GROUPID field (fieldname) is not in input file.  
*** Error *** No numeric fields on file (filename)  
>>> ERR 122 <<< ( fileno.) IN DISCAN  
*** Error *** SAMPID field (fieldname) is not in input file.  
*** Error *** There is only one group in file (filename)  
Discriminant analysis process terminated.  
*** Error *** There is only one sample in each group  
Discriminant analysis process terminated.  
*** Error *** Compulsory file, field or parameter missing  
>>> ERR 120 <<< ( fileno.) IN DISCAN