# SETENV Process  
  
To access this process:

  * Enter "SETENV" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SETENV** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SETENV>).

## Process Overview

Updates the environment with new variables.

**SETENV** copies environment file data from a system file or the keyboard to a temporary file, then merges the temporary file with the current environment set of environment variables.

## Example

1.Reading from an environment system file:-
    
    
    !SETENV    @PRINT=0.0SYSFILE>MENU.ENV <return>  
  
---  
  
2\. Reading from the keyboard:-
    
    
    !SETENV    @PRINT=0.0SYSFILE><return>ENV>G_FONT=MEDIUM,25ENV><return>  
  
---  
  
## Error and Warning Messages

>>> |  SYSTEM FILE DOES NOT EXIST <<< The environment system file name supplied was not found (e.g. incorrect path). Fatal; the process is exited.  
---|---  
>>> |  CANNOT OPEN TEMPORARY FILE ffffffff <<< A system error has occurred when trying to open the temporary environment file ffffffff (e.g. disk full). Fatal; the process is exited.  
>>> |  UNEXPECTED ERROR READING ENVIRONMENT SPECIFICATIONS <<< The format of one or more environment variables is not correctly defined (e.g. corrupted data in the system file). Fatal; the process is exited.