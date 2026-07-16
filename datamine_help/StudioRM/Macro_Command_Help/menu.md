# MENU Macro Command

To access this process:

  * **Home** ribbon >> **Automate >> Macro >> Run Menu**.
  * Enter "MENU" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

Initiates the currently established menu. The menu name is requested. This must be the name of a binary random access menu file which was created using the ![LOADCF](<../Process_Help_XML/loadcf.md>) command.

`!MENU` commands should not be nested. A menu may be called from a macro or another menu, and a menu may call a macro.

On executing the `!MENU` command for the first time for any menu, there will be a delay while the menu is scanned and labels etc. entered into the system stack file. This stack file (of form<name>.STK, where <name> is the menu file name minus the extension) is saved, and on second and subsequent uses of the !MENU command, the stack file is copied for direct execution. This means second and subsequent uses of `!MENU` start execution much faster than the first time.  
  
> If the stack file should not match the menu file, then the menu may not work correctly. This could happen if the binary menu file was overwritten (not by the !**LOADCF** command), leaving an old stack file in place. If this should happen, reload the menu using !**LOADCF**.  
  
The total number of labels used within the menu file should not exceed 250\. If this number is exceeded, all labels beyond that will not be accessible.

## Example
    
    
    !MENU
    
    
    NAME >MYMENU

## Error and Warning Messages

**Message** |  Description |  Solution  
---|---|---  
>>>MENU FILE DOES NOT EXIST <<<  
>>> ERR 78 <<< ( 0) IN RUN |  The menu file either does not exist, or is malformed. Fatal; the process is exited. |  Check to see if the menu file exists; recreate from the original if necessary using LOADCF.  
>>>WARNING - MORE THAN 250 SUBSTITUTION VARIABLES <<<ERR 84 <<< ( 250) IN UPDSTV |  Only 250 variables may be in use at any time. Warning; the excess is ignored and processing continues. |  Reduce the size of the original macro and recreate the menu file using LOADCF.  
>>>MACRO NAME NOT FOUND <<<  
ERR 72 <<< ( 0) IN RUN |  No !**START** command was found to introduce the menu. Fatal; the process is exited. |  Check the original macro file, correct any errors and recreate the menu file using LOADCF.  
  
Related topics and activities:

  * [LOADCF Process](<../Process_Help_XML/loadcf.md>)