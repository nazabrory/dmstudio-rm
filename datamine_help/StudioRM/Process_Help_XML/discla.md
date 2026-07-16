# DISCLA Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Geochemical Processes >> Multiple Discriminant Classify**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DISCLA** and click **Run**.
  * Enter "DISCLA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DISCLA>).

## Process Overview

Multiple discriminant classification of unknown samples into groups using the discriminant functions and group centroids calculated in the [DISCAN](<discan.md>) process.

Discriminant analysis is a classification problem, where two or more groups or clusters or populations are known a priori and one or more new observations are classified into one of the known populations based on the measured characteristics.

Multiple discriminant analysis using trial (test) data sets to calculate scores and discriminant functions with group centroids for use in the **DISCLA** process.

The calculation of discriminant functions (Discriminant analysis) will establish a set of rules using geological control groups or training sets which can then be applied to the classification of unknown samples using the **DISCLA** process.

For example, test data from DISCAN will calculate discriminant functions and group centroids to classify known samples into mineralized and non-mineralized. DISCLA will then use the discriminant functions and group centroids and apply them to unknown samples in order to identified them into the classes mineralized and non-mineralized, plus a third class, to include the samples which are not classifiable.

**Note** : there is a maximum limit of 45 variables and 10 classifier groups with an extra group for non classifiable samples. Samples containing absent data are ignored.

### File Handling

The input file (&**IN**), of samples for classification must contain a sample identifier field (@**SAMPID**). The input files (&**INFUNCTS**) discriminant functions and (&**INCENTRD**) group centroids are obligatory. File &**INCENTRD** must contain a group identifier specified in @**GROUPID**. The output file of classified samples (&**OUT**) contains a new field named in @**GROUPID** identifying the group classifier or a flag to note that the sample is not classifiable using the data given in files &**INFUNCTS** and &**INCENTRD**.

The output file containing the discriminant scores for each sample can be joined to the original data containing the grid coordinates using the **SAMPID** as a key field. The scores can then be plotted as a map.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. Must contain sample identity field. |  Input |  Yes |  Undefined  
INFUNCTS |  Input file containing discriminant functions. Produced from process **DISCAN**. |  Input |  Yes |  Undefined  
INCENTRD |  Input file containing group centroids. Produced from process **DISCAN**. Must contain a group identity field specified in **GROUPID**. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file containing samples classified into groups identified by the GROUPID field and the discriminant scores..  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
GROUPID |  Compulsory group identifier field contained in **INCENTRD**. |  INCENTRD |  Yes |  Alphanumeric |  Undefined  
SAMPID |  Compulsory sample identifier field in input file **IN**. |  IN |  Yes |  Any |  Undefined  
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
  
## Example
    
    
    DISCLA! &IN(AREAZ), &INFUNCTS(GGFUNCTS),   
  
---  
      
    
    &INCENTRD(GGCENT),   
      
    
    &OUT(AREAZCL), @GROUPID='ID', @SAMPID= 'ID'  
      
    
       
  
## Error and Warning Messages

Message  
---  
*** Warning *** GROUPID field has nn words. Only the first 3 will be used.  
*** Warning *** SAMPID field has nn words. Only the first 3 will be used.  
*** Error *** GROUPID field (fieldname) is not in input file.  
*** Error *** No numeric fields on file (filename)>>> ERR 122 <<< ( fileno.) IN DISCLA  
*** Error *** SAMPID field (fieldname) is not in input file.  
*** Error *** Compulsory file, field or perimeter missing.  
>>> ERR 120 <<< ( fileno.) IN DISCLA