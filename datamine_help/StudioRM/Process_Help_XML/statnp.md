# STATNP Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Statistics Processes >> Nonparametric Statistics**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **STATNP** and click **Run**.
  * Enter "STATNP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#STATNP>).

## Process Overview

Calculates non-parametric summary statistics on numeric fields in a file.

The following statistics are calculated for each numeric variable in turn:-

  * total number of records in the file.
  * number of samples (excluding absent data).
  * number of absent data values.
  * minimum, maximum and range.
  * mid-range.
  * median and median deviation.
  * 10th and 90th percentile.

Note: By default, statistics are calculated for all numeric variables (up to 10 fields can be defined; more than 10 if a &**FIELDLST** is specified).

These results are displayed on the terminal, and can be copied to the print device. In addition a cumulative frequency plot on a normal probability scale can be calculated for each variable, and sent to the printer or a file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1-10 |  Fields for statistics. No fields specified means all. |  IN |  No |  Numeric |  Undefined  
FIELDNAM |  Field in FIELDLST to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLOT |  |  Option |  Description  
---|---  
1 |  send cumulative frequency plots to printer or print file (0).  
No |  0 |  0,1 |  0,1  
  
## Examples

### Example 1

Statistics are calculated for the field **Au**.
    
    
    !STATNP     &IN(ASSAYS), F1(Au)  
  
---  
  
### Example 2

Statistics are calculated for all numeric fields in the file.
    
    
    !STATNP     &IN(ASSAYS)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 121 <<< ( fileno) IN STATNP |  File read error. Fatal; the process is exited. Check the &IN file and its fields.  
>>> ERR 122 <<< ( fileno) IN STATNP |  No numeric fields in file, or fields specified were not numeric. Fatal; the process is exited. Check that the &IN file contains numeric fields.  
DATA FILE EMPTY - PROCESS TERMINATED |  The input file contains no data. Fatal; the process is exited. Check that the &IN file contains data.  
  
Related topics and activities

  * [STATS Process](<stats.md>)

  * [STATCOM Process](<statcom.md>)