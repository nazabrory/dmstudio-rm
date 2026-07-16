# MACST Macro Command

To access this process:

  * **Home** ribbon >> **Automate >> Macro >> Record Macro**.
  * Enter "MACST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

Start the storage of all subsequent interactive input in a character format system macro file.

The macro name may be specified following the **MACST** command name. The macro name supplied is then appended to the !**[START](<start.md>)** command and written to the system macro file. If no macro name is specified in this way, a message is immediately displayed and the user must supply one interactively in response to a prompt.

Once the !**MACST** command has been given it remains in force until the !**[MACEND](<macend.md>)** command is executed.

If the macro name is not specified following the MACST command name, this message displays:
    
    
    MACRO NAME NOT SUPPLIED, PLEASE SUPPLY NAME

This is followed by a prompt for the name:
    
    
    <MACRONAME><macroname>

If no errors are detected the message displays:
    
    
    STORAGE OF INTERACTIVE INPUT TO MACRO STARTED

If the system file specified already exists, all subsequent interactive input is appended to the existing contents of the file. In this way, a number of macros can be created in a macro library (in this case a single *.mac system file) from different interactive sessions.

## Example
    
    
    !MACST M1  
    SYSFILE>MYMAC1.DAT  
      
    STORAGE OF INTERACTIVE INPUT TO MACRO STARTED  
    .  
    .  
    .  
    !MACEND

## Error and Warning Messages

**Message** |  Description |  Solution  
---|---|---  
>>> ERROR READING FROM MACRO SYSTEM FILE ffffffff.fff <<<  
|  An error has been detected in reading from the specified system macro file. Fatal; the process is exited. |  Check that the file exists; check that it has Read/Write attributes; open the file in a text editor and check that it is not corrupt.  
>>> ERROR WRITING TO MACRO SYSTEM FILE ffffffff.fff <<< |  An error has been detected in writing !START <macroname> to the system macro file. Fatal; the process is exited. |  Check that the file exists; check that it has Read/Write attributes; open the file in a text editor and check that it is not corrupt.  
  
Related topics and activities:

  * [END Macro Command](<end.md>)

  * [MACEND Macro Command](<macend.md>)