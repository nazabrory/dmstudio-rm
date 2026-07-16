# NOMENU Macro Command

Checks the syntax of the currently established menu. `!NOMENU` works in the same way as ![MENU](<menu.md>), except that the menu is not executed.

The menu name is requested. This must be the name of a binary random access menu file loaded by the ![LOADCF](<../Process_Help_XML/loadcf.md>) command.

On executing the `!NOMENU` command for the first time for any menu, there will be a delay while the menu is scanned and labels etc. entered into the system stack file. This stack file (of form `<name>.STK`, where `<name>` is the menu file name minus the extension) is saved, and on second and subsequent uses of the `!MENU` command, the stack file is copied for direct execution.  
  
> This means second and subsequent uses of `!NOMENU` start execution much faster than the first time.  
  
If the stack file should not match the menu file, then the menu may not work correctly. This could happen if the binary menu file was overwritten (not by the `!LOADCF` command), leaving an old stack file in place. If this should happen, reload the menu using `!LOADCF.`

Note: The total number of labels allowed is 250. If this number is exceeded, all labels beyond that will not be accessible. 

## Example
    
    
    !NOMENUNAME   
  
---  
      
    
    >MYMENU  
  
## Error and Warning Message

Message |  Description |  Solution  
---|---|---  
>>> MENU FILE DOES NOT EXIST <<< >>> ERR 78 <<< ( 0) IN RUN |  The menu file either does not exist, or is malformed. Fatal; the process is exited.  |  Check that the *.men file exists. Recreate the file from the *.mac file using LOADCF if the file exists.  
>>> MACRO NAME NOT FOUND <<< >>> ERR 72 <<< ( 0) IN RUN |  No macro name supplied. (This message is only produced if !NOXRUN is executed from a macro, and no macro name is supplied; in this case, name prompting does not take place). Fatal; the process is exited. |  Check that the specified macro name is correct.  
>>> WARNING - MORE THAN 250 SUBSTITUTION VARIABLES <<< >>> ERR 84 <<< (250) IN UPDSTV |  Only 250 variables may be in use at any time. Warning; the excess is ignored and processing continues. |  Reduce the number of substitution variables.