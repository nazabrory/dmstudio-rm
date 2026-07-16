# ATTCHK Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ATTCHK** and click **Run**.
  * Enter "ATTCHK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ATTCHK>).

## Process Overview

This process is used to check the legend definition file prior to running [ATTSET](<attset.md>).

**ATTCHK** copies values from previous records into blank fields, and reports any inconsistencies in the file.

A hierarchy is verified in each legend specification found in the file :-

  1. Each **LEGEND** can contain one or more **DATFLD** entries

  2. Each **DATFLD** can contain one or more ranges and/or patterns

  3. Each range/pattern can have one or more **ATTRIB** entries.

The values of fields at each key change are propagated down until the next non-blank value in a column. One of the combinations below is expected for each **DATFIELD** /**ATTRIB** entry :-

  * **DATMIN** (discrete value)

  * **DATMIN** , **DATMAX** (data range)

  * **DATEXP** (data pattern)

The validation of the file reports :-

  1. Missing values on a record

  2. Overlapping, missing or over-specified ranges

Alphanumeric range fields for which a blank is intentionally to be specified should have blanks included within single or double quotes within the legend file. A blank field will be output.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Overwritten |  Yes |  Undefined |  Input legend file. The following standard field names are recognized but not all need be present in the file :- LEGEND A8 Legend key. DATFIELD A8 Data field in the input file. DATMIN A12 Minimum value. DATMAX A12 Maximum value. DATEXP A40 Match (regular) expression. ATTFIELD A8 Attribute field. ATTVALUE A12 Attribute field value. Alternate field names can be supplied to the process by specification through the symbolic field names eg DATMIN(MIN).  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  Output legend file. Can be the same as the input file.  
ERROR |  Output |  No |  Undefined |  Optional output error file for invalid records.  
  
Related topics and activities

  * [ATTSET Process](<attset.md>)