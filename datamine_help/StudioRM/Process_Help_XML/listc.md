# LISTC Process

To access this process:

  * Enter "LISTC" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **LISTC** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LISTC>).

## Process Overview

Display any Datamine file with only alphanumeric fields.

If the file should contain numeric fields, an automatic transfer is made to the **[LIST](<list.md>)** process. If the output line is longer than 80 characters, it is wrapped around. Each alphanumeric field occupies as many characters as required, but is preceded by 4 blanks to separate it from the previous field.

At the end of each page of output, the message:
    
    
    >>> PRESS <RETURN> TO CONTINUE (OR ! TO TERMINATE) >

is displayed. If the response is !<return> then the **LISTC** process is terminated. This allows part of the file to be displayed. This message does not appear if **LISTC** is being invoked from a macro.

The page length is controlled by the @**PROMPT** parameter. The default is 20 records; this may be altered to, say, 60 records by setting @**PROMPT** =60. @**PROMPT** = 0 removes all prompting, except following the Data Definition. Each page of data is headed by the field names.

If the @**ECHO** parameter is set to 1, the listing is copied to the printer or print file. This assumes a carriage width of 132 characters, rather than the 80 of the normal display.

Only explicit fields are listed. Implicit fields appear only in the Data Definition.

If an index file is being displayed, the data records will be displayed as if they were joined in a single file.

**Note** : The alias L is the alias for the **LISTC** command; however, if the file should contain any numeric fields, then **LISTC** branches automatically to the **[LIST](<list.md>)** process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Character file to be displayed. If IN is a catalogue file, then all files in the catalogue will be displayed. |  Input |  Yes |  Table  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PROMPT |  Page length for display; 0=infinite (20). |  No |  20 |  Undefined |  Undefined  
  
## Example
    
    
    !LISTC &IN(MACROS)  
  
---  
  
Related topics and activities

  * [LIST Process](<list.md>)

  * [LISTDR Process](<listdr.md>)