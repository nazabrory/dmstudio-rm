# TBLIN Process  
  
To access this process:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, select **TBLIN** and click **Run**.
  * Enter "TBLIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TBLIN>).

## Process Overview

Table driven "flat-file" data input process.

Enter data of definable format from a system file or the keyboard. The names, types and locations of the input data fields are specified by **EXDEF** , an external definition file. The field layout organization of the input data can be defined with **LAYOUT**. The data may be filtered on input if required. Filtering is optional, and may be specified via fields in **EXDEF** or keywords in **FILTER**.

Note : All filter, end-of-data and page separator matching is case-insensitive. The input data is written to OUT. The data definition is controlled via **PROTODD** , **FIELDLST** and **EXDEF** as follows :

  * If PROTODD is supplied, its data definition is used as a prototype for OUT.

  * If FIELDLST is supplied, it specifies a subset of the fields defined in EXDEF for creation in OUT.

  * If neither PROTODD nor FIELDLST are supplied, all fields defined in EXDEF are output.

Note: PROTODD AND FIELDLST can not be used at the same time. Data records containing errors may be output to ERROR if desired. All files, EXDEF ,OUT ,ERROR ,FILTER ,PROTODD , FIELDLST if specified, must be different.

## System Prompts

>TPLNAME> Name of template to use from EXDEF. Default is only template in EXDEF. Max 8 char, must exist if supplied.

>FILE DESCRIPTION> 60 char text comment for OUT. >PS > Optional page separator. Max 72 chars. Default is Page Feed character. For FINDPG>=1 only.

>SYSFILE> External file name (max 56 chars); blank for none. Organization as per LAYOUT.

>DATA > Data lines if no SYSFILE, in defined LAYOUT. ! or EOD terminates.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
EXDEF |  External field definition table. Specifies names, types and locations of input data fields. Retrieval criteria, if any, operate on **EXDEF**. |  Input |  Yes |  Undefined  
FILTER |  Optional input data filter table. |  Input |  No |  Undefined  
PROTODD |  Optional prototype data definition. Selects fields to be created in **OUT**. If not supplied, data definition is created for all fields defined in **EXDEF**.  Implicit fields defined in **EXDEF** are made explicit. Alpha field lengths are taken from **EXDEF**. |  Input |  No |  Undefined  
FIELDLST |  Optional field subset list. Selects fields to be created in OUT. If not supplied, data definition is define for all fields in EXDEF.  One of **PROTODD** , **FIELDLST** can be specified. **FIELDLST** must contain at least **FIELD** (A8) Name of field for output. (must be subset of **EXDEF**) |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output database file to be created.  
ERROR |  Output |  No |  Undefined |  Optional output file for error records. If not supplied, data which is outside MIN...MAX limits is placed in OUT.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LAYOUT |  Input file organisation method.  1=Char Each field located by START, END.  2=Free Datamine standard "free" format.  3=Comma Fields separated by commas, no quotes  4=Single Fields sep. by commas, quote with '  5=Double Fields sep. by commas, quote with "  6=White Fields separated by spaces/tabs  7=Custom FS and/or DELIM. |  Yes |  1 |  1,7 |  1,2,3,4,5,6,7  
DELIM |  Optional field delimiter. Max 4 chars. |  No |  Undefined |  Undefined |  Undefined  
FS |  Optional field separator. Max 4 chars. |  No |  Undefined |  Undefined |  Undefined  
SKIPHD |  >=1 Omit n lines of header (0). |  No |  0 |  Undefined |  Undefined  
FINDPG |  >=1 Scan for "page breaks" and omit headers and footers from all pages (0). |  No |  0 |  0,1 |  0,1  
EOD |  Optional end of data string. Max 4 char. |  No |  Undefined |  Undefined |  Undefined  
TRACE |  >=1 Display each nth input record (0). |  No |  0 |  0,1 |  0,1  
  
Related topics and activities

  * [TABRES Process](<tabres.md>)