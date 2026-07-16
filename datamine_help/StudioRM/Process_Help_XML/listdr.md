# LISTDR Process

To access this process:

  * Enter "LISTDR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **LISTDR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LISTDR>).

## Process Overview

Creates a list of all Datamine files within the project folder.

Wildcarding is supported and an output catalogue file can be generated. Filenames or filename templates may be entered as retrieval criteria. The form is:- ?<string>?.<string> or:- ?<string>?.? Please Note: This command is only available from macros. The use of a catalogue file is backwards compatible but note that file names are restricted to a maximum of twenty (20) characters.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Catalogue |  Output catalogue file, giving list of files to be used by processes **[APPEND](<append.md>)** , **[DELETE](<delete.md>)** , [DISPLA](<displa.md>), [INPDDF](<inpddf.md>), [LIST](<list.md>) and [OUTPUT](<output.md>).  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FIELDNAM |  Name of field in **OUT** containing file paths |  |  No |  Any |  Undefined  
  
## Example

The following lines in a macro create a catalog file containing the names of all Datamine files starting with the four characters TEMP and then delete all the files.
    
    
    !LISTDR  &OUT(TEMP1), TEMP?  
  
---  
      
    
    !DELETE &IN(TEMP1)  
      
    
    !LISTDR *FIELDNAM(MYFIELD), &OUT(MYOUT)  
  
Related topics and activities

  * [LIST Process](<list.md>)

  * [LISTC Process](<listc.md>)