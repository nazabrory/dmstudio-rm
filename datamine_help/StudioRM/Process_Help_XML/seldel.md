# SELDEL Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Delete Fields**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SELDEL** and click **Run**.
  * Enter "SELDEL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SELDEL>).

## Process Overview

Selectively deletes named fields from the input file during a copy to the output file.

The fields to be deleted are specified as * **F1** to * **Fn**. Any number of required fields may be deleted, but only one is compulsory.

If retrieval criteria are specified they will be ignored if they are on the deleted fields.

If the optional parameter @**KEEPALL** is zero (default) the output file will only contain one entry for each combination of output field values, provided that the input file is first sorted on these fields. If the input file is not sorted, then the output file will contain one entry for each combination of output field values which occur together in the input file.

The process works by checking the selected field values against the values just written to the output file. If they are identical, the current record is skipped.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file with deleted fields.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  Deleted field 1. |  IN |  No |  Any |  Undefined  
F2-F25 |  Optional selected fields. |  IN |  No |  Any |  Undefined  
FIELDNAM |  Field in **FIELDLST** to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
KEEPALL |  Used to keep or delete records with duplicate successive key field values |  Option |  Description  
---|---  
(0) |  Do not copy successive duplicate records.  
1 |  Copy all records to Output File, even if adjacent records have identical Key Field values.  
No | 0 | 0,1 | 0,1  
KEYTOL |  KEYTOL is the tolerance value used to test whether numeric key values are equal. It must be greater than or equal to zero. It replaces the previous heuristic comparison method.  If KEYTOL is set to a negative value then zero is used.  In a macro KEYTOL can be set to absent using -. "@KEYTOL=-" This will revert to legacy behaviour of a tolerance of zero being used. |  No |  0.00001 |  0,+ |  Undefined  
  
## Example
    
    
    !SELDEL     &IN(ASSAYS),&OUT(CUAU),*F1(BHID),*F2(FROM),*F3(TO)  
  
---  
  
Related topics and activities

  * [COPY Process](<copy.md>)
  * [COPYMOD Process](<copymod.md>)

  * [COPYNR Process](<copynr.md>)

  * [SELCOP Process](<selcop.md>)

  * [SELEXY Process](<selexy.md>)

  * [SELPER Process](<selper.md>)

  * [DDCOPY Process](<ddcopy.md>)