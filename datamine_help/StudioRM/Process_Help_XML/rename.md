# RENAME Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Rename**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **RENAME** and click **Run**.
  * Enter "RENAME" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RENAME>).

## Process Overview

Rename a Datamine file in the project.

The new name must not exist in the project folder. If it does, an error message is produced, and the process is abandoned, unless the optional @DELETE parameter has been set to 1 and the user has write access to the output file.

With work-file structure databases, when a file is renamed, a check is made to see if any database pages are still in existence with the new name chosen. This could happen if the file name had previously been used for a longer file. If this is the case, the message is produced:
    
    
    >>> DELETING ANY REMAINING PAGES OF ffffffff

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be renamed. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  New file name (must not exist).  
  
## Example
    
    
    !RENAME     &IN(NAME),&OUT(NEWNAME)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERROR - FILE ffffffff ALREADY EXISTS <<< >>> ERR 41 <<< ( fileno) IN RENAME |  Rename attempt fails. Fatal; the process is exited.  
>>> ERROR - FILE ffffffff ALREADY EXISTS AND CANNOT BE DELETED FIRST <<< >>> ERR 42 <<< ( fileno) IN RENAME |  Rename attempt fails as user does not have write access to the output file, which therefore cannot be deleted first. Fatal; the process is exited.  
  
Related topics and activities

  * [LIST Process](<list.md>)

  * [LISTC Process](<listc.md>)

  * [LISTDR Process](<listdr.md>)