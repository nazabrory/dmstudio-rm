# SELCOP Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Copy Fields**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SELCOP** and click **Run**.
  * Enter "SELCOP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SELCOP>).

## Introduction

Selectively copy named fields from the input file to the output file.

The required fields are specified as * **F1** to * **Fn**. Any number of required fields may be chosen, but only one is compulsory.

If retrieval criteria are specified they will be ignored if they are not on the chosen fields. To select records on fields which are not required in the output file requires a two stage process - first **[COPY](<copy.md>)** under retrieval criteria, then **SELCOP** the required fields.

If the optional parameter @**KEEPALL** is zero (default) the output file will only contain one entry for each combination of output field values, provided that the input file is first sorted on these fields. If the input file is not sorted, then the output file will contain one entry for each combination of output field values which occur together in the input file.

The process works by checking the selected field values against the values just written to the output file. If they are identical, the current record is skipped.

**Note** : If the input file is sorted on the selected fields, the result is that **SELCOP** is exactly equivalent to the relational 'projection' operation.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file with selected fields.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  Selected field 1. |  IN |  Yes |  Any |  Undefined  
F2-F25 |  Optional selected fields. |  IN |  No |  Any |  Undefined  
FIELDNAM |  Field in **FIELDLST** to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
KEEPALL |  |  Option |  Description  
---|---  
1 |  copy all records  
(0) |  ignore duplicate successive records.  
No |  0 |  0,1 |  0,1  
KEYTOL |  **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It must be greater than or equal to zero. It replaces the previous heuristic comparison method.  If **KEYTOL** is set to a negative value then zero is used.  In a macro **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy behaviour of a tolerance of zero being used. |  No |  0.00001 |  0,+ |  Undefined  
  
## Example
    
    
    !SELCOP     &IN(ASSAYS),&OUT(CUVALS),*F1(CU  
  
---  
  
Related topics and activities

  * [COPY Process](<copy.md>)

  * [COPYMOD Process](<copymod.md>)

  * [COPYNR Process](<copynr.md>)

  * [SELDEL Process](<seldel.md>)

  * [SELEXY Process](<selexy.md>)

  * [SELPER Process](<selper.md>)

  * [DDCOPY Process](<ddcopy.md>)