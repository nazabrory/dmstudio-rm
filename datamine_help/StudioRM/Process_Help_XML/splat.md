# SPLAT Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Relational >> Add Side by Side**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SPLAT** and click **Run**.
  * Enter "SPLAT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SPLAT>).

## Process Overview

Perform a simple sideways merge of two files.

The process works by simply adding each record of the second file onto the end of the record for the first file. If matching fields are found, then the value from the second file replaces that of the first; but there is no requirement for matching fields. The records are assumed to be in the same order in each file (not necessarily sorted on any field) and there is no check for missing or matching records. The user must ensure that records in each file match each other, or the output will be meaningless.

If one file is exhausted before the other, the remaining records from the other file are written to the output file, with absent data fill.

A typical use for SPLAT is to add fields onto the end of existing records in a file.

**Note** : This process carries out very limited checks, and you are advised to use SPLAT only on files with exactly the same number of records.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  First input file. |  Input |  Yes |  Table  
IN2 |  Second input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output merged file.  
  
## Example
    
    
    !SPLAT     &IN1(ASSAYS),&IN2(NEWASSAY),&OUT(ALLASSAY)  
  
---  
  
Related topics and activities

  * [APPEND Process](<append.md>)

  * [JOIN Process](<join.md>)

  * [WEAVE Process](<weave.md>)

  * [SUBWVE Process](<subwve.md>)