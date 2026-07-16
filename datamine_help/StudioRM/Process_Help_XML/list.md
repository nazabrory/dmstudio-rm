# LIST Process  
  
To access this process:

  * Enter "LIST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **LIST** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LIST>).

## Process Overview

Display any database file in a standard format.

The Data Definition is first displayed, followed by each record. If the output line is longer than 80 characters, it is wrapped around.

Each numeric field occupies 12 characters. The format of the field changes with the magnitude of the number, to preserve as much accuracy as possible. Each alphanumeric field occupies as many characters as required, but is preceded by 4 blanks to separate it from the previous field. At the end of the Data Definition and of each page of output, the message:-
    
    
    >>> PRESS <RETURN> TO CONTINUE (OR ! TO TERMINATE) >

is displayed. If the response is !<return> then the **LIST** process is terminated. This allows part of the file to be displayed. This message does not appear if **LIST** is invoked from a macro.

The page length is controlled by the @**PROMPT** parameter. The default is 20 records; this may be altered to, say, 60 records by setting @**PROMPT** =60. @**PROMPT** = 0 removes all prompting, except following the Data Definition. Each page of data is headed by the field names.

If an index file is being displayed, then first the Data Definition of the index will be displayed, followed by all data records to which the index refers.

If the input is a catalogue file (as created by the **[LISTDR](<listdr.md>)** process) then all files in the catalogue are listed in turn.

**Note** : The alias L is the alias for the [LISTC](<listc.md>) command; however, if the file should contain any numeric fields, then **LISTC** branches automatically to the LIST process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be displayed. If IN is a catalogue file, then all the files in the catalogue will be displayed. |  Input |  Yes |  Table  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  Optional first listed field. None specified means all. |  IN |  No |  Any |  Undefined  
F2 |  Optional second listed field. |  IN |  No |  Any |  Undefined  
F3 |  Optional third listed field. |  IN |  No |  Any |  Undefined  
F4 |  Optional fourth listed field. |  IN |  No |  Any |  Undefined  
F5 |  Optional fifth listed field. |  IN |  No |  Any |  Undefined  
F6 |  Optional sixth listed field. |  IN |  No |  Any |  Undefined  
F7 |  Optional seventh listed field. |  IN |  No |  Any |  Undefined  
F8 |  Optional eighth listed field. |  IN |  No |  Any |  Undefined  
F9 |  Optional ninth listed field. |  IN |  No |  Any |  Undefined  
F10 |  Optional tenth listed field. |  IN |  No |  Any |  Undefined  
FIELDNAM |  Field in FIELDLST to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PROMPT |  Page length for display; 0=infinite (20). |  No |  20 |  Undefined |  Undefined  
  
## Example
    
    
    !LIST &IN(ASSAYS)  
  
---  
  
## Error and Warning Messages

If any file in a catalogue does not exist, the file is skipped and the next one opened. A fatal error condition is set.

Related topics and activities

  * [LISTC Process](<listc.md>)

  * [LISTDR Process](<listdr.md>)