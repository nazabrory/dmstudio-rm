# DDLIST Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DDLIST** and click **Run**.
  * Enter "DDLIST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DDLIST>).

## Process Overview

Displays a file Data Definition (DD). If an index file is input to DDLIST, then the DDs of each of the indexed files are displayed in turn.

**Note** : in interactive use, the **[LIST](<list.md>)** process displays the file DD in an identical format to that provided by DDLIST. However, within a macro, DDLIST should be used instead, as it is not possible to stop LIST displaying all the file records following the DD.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be displayed. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
  
## Example
    
    
    !DDLIST &IN(FILE)  
  
---  
  
Related topics and activities

  * [LIST Process](<list.md>)

  * [LISTC Process](<listc.md>)

  * [LISTDR Process](<listdr.md>)