# MACEND Macro Command

To access this process:

  * **Home** ribbon >> **Automate >> Macro >> End Recording**.
  * Enter "MACEND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

Terminates the storage of interactive input in a character format macro file (*.mac).

The statement !**[END](<end.md>)** is first written to the system file and then the file is closed.

Once the !**MACEND** command has been given it remains in force until the ![MACST](<macst.md>) command is executed.

**Note** : If no errors are detected the message: `STORAGE OF INTERACTIVE INPUT TO MACRO ENDED` displays.

## Error and Warning Messages

**Message** |  Description |  Solution  
---|---|---  
STORAGE OF INTERACTIVE INPUT TO MACRO IS NOT ACTIVATED >>> MACEND Complete <<<  
|  A !**MACST** command had not been issued before !**MACEND**. |  First run MACST, record the required process, then runMACEND.  
  
Related topics and activities:

  * [END Macro Command](<end.md>)

  * [MACST Macro Command](<macst.md>)