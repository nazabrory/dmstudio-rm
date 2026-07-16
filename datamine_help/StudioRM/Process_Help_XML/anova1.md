# ANOVA1 Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics Processes >> One Way Analysis of Variance**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ANOVA1** and click **Run**.
  * Enter "ANOVA1" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ANOVA1>).

## Process Overview

Carries out one-way analysis of variance on groups of replicate values of a numeric field in a file.

All results are output as an analysis of variance (ANOVA) table. This lists the sources of variation, a column of the corrected sums of squares resulting from the various sources, degrees of freedom associated with each, a column of mean squares which are the sample-based estimates of the variances, and the F-value.

**Note** : The total keyfield must be no more than 5 words long. Remember that an alphanumeric field should be no more than two words long.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file, sorted on required keyfields. |  Input |  Yes |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Field for analysis of variance. |  IN |  Yes |  Numeric |  Undefined  
KEY1 |  Keyfield 1 for replicate observations. |  IN |  Yes |  Numeric |  Undefined  
KEY2 |  Keyfield 2. |  IN |  No |  Numeric |  Undefined  
KEY3 |  Keyfield 3. |  IN |  No |  Numeric |  Undefined  
KEY4 |  Keyfield 4. |  IN |  No |  Numeric |  Undefined  
KEY5 |  Keyfield 5. |  IN |  No |  Numeric |  Undefined  
KEY6 |  Keyfield 6. |  IN |  No |  Numeric |  Undefined  
KEY7 |  Keyfield 7. |  IN |  No |  Numeric |  Undefined  
KEY8 |  Keyfield 8. |  IN |  No |  Numeric |  Undefined  
KEY9 |  Keyfield 9. |  IN |  No |  Numeric |  Undefined  
KEY10 |  Keyfield 10. |  IN |  No |  Numeric |  Undefined  
  
## Example
    
    
    !ANOVA1 &IN(SEDREG),*VALUE(MN),*KEY1(SNUM)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> VALUE FIELD DOES NOT EXIST <<< |  The numeric field specified for *VALUE does not exist. Fatal; the process is exited.  
>>> ERR 47 <<< ( 0) IN FNDKEY |  None of the keys specified were in the file. Fatal; the process is exited.  
>>> INPUT FILE NOT SORTED ON KEYFIELD(S) <<< |  Fatal; the process is exited.  
>>> ERR 121 <<< ( fileno) IN ANOVA1 |  File read error. Fatal; the process is exited.  
>>> MORE THAN 1000 REPLICATES <<<  
>>> ONLY THE FIRST 1000 USED <<< |  The maximum number of points which may be processed is 1000. All other points are ignored, and processing continues with the first 1000.  
>>> MORE THAN 250 GROUPS <<<  
>>> ONLY THE FIRST 250 USED <<< |  The maximum number of groups of points which may be processed is 250. All other groups of points are ignored, and processing continues with the first 250.  
>>> TOO FEW REPLICATES AND/OR GROUPS <<<  
>>> CANNOT CARRY OUT ANALYSIS OF VARIANCE <<<  
>>> MINIMUM REQUIREMENT IS FOR 2 REPLICATES <<<  
>>> IN EACH OF 2 GROUPS <<< |  Insufficient data in input file for analysis of variance. Fatal; the process is exited.