# COPYNR Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Set Value >> Add Record Number**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COPYNR** and click **Run**.
  * Enter "COPYNR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COPYNR>)

## Process Overview

Copies a database file to a new file with the addition of a field for the record (line) number. This field is named **RECORDNO**. 

By default the record numbers start at 1 and increment in steps of 1, but the start number and increment may optionally be chosen by entering required values for the parameters @**BASE** and @**INCRMENT**. If **RECORDNO** already exists, it will be renumbered. Thus **COPYNR** acts as both a number and a re-number facility.

With retrieval criteria, the output file will contain those records that match the criteria; record numbers will start at @BASE with increment @**INCRMENT** on these output records.

If the @**BASE** and @**INCRMENT** parameters entered are not integers, then they will be truncated to integers. For example, an @INCRMENT of 0.5 will be truncated to 0, leading to all records being given the same **RECORDNO**.  
  
No check is made for the existence of the specified output file, which therefore can be overwritten.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file; same as input with addition of field **RECORDNO**. If **RECORDNO** already exists in the input file, values will be renumbered in the output.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
BASE |  Starting record number (1) [Integer]. | No |  |  |  Undefined  
INCRMENT |  Record number increment (1) [Integer]. | No |  |  |  Undefined  
  
## Example
    
    
    !COPYNR &IN(FILE1), &OUT(NUMFILE), @BASE=100, @INCRMENT= 5  
  
---