# STKSAV Macro Command

Writes substitution variables and their values from a system character format file.

This file may be set up by the !STKSAV command from within a macro or menu. The form of the command is:
    
    
    !STKSAV <filename>

Where `<filename>` is a system file name. It may be up to 56 characters long andy may contain pathnames. The `<filename>` may be substituted in whole or in part by substitution variables. The form of the system file is:
    
    
    nnn     

|  Number of substitution variables on file. Max 50  
---|---  
| 
    
    
    <var1><val1>  
  
| 
    
    
    <var2><val2>  
  
|  .......  
  
Where `<var1>,<var2>` are the names of the substitution variables, and `<val1>,<val2>` are their values. Each `<var>` occupies 8 characters, followed by the value (max 72 characters).

## Example
    
    
    !STKSAV    /Studio 3/projects/$proj  
  
---  
  
## Error and Warning Messages

>>> |  !STKSAV or !STKPAR: ERROR IN ACCESSING SYSTEM FILE <<<  
---|---  
|  <listing of command line>  
>>> |  ERR 90 <<< (0) IN MACGET  
|  The file did not exist, was the wrong type, or a read error was encountered. This message will also occur if no file was specified, or the file name was too long. Fatal; the macro or menu is exited.  
  
Related topics and activities:

  * [STKPAR Macro Command](<stkpar.md>)

  * [SYSFILE](<sysfile.md>)

  * [VARINIT](<varinit.md>)

  * [VARLOAD](<varload.md>)

  * [VARSAVE](<varsave.md>)