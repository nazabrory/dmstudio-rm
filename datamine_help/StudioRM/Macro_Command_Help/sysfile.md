# SYSFILE Macro Command

Checks if a system file exists.

The command format is similar to the ![FILE](<file.md>) command:
    
    
    !sysfile <var>=<pathname>

where `<var>` is a substitution variable which is set to '1' if the file indicated by `<pathname>` exists, otherwise `<var>` is set to 0.

The `<pathname>` may optionally be specified by means of a substitution variable. If necessary, its length will be truncated to 56 characters. Note that the existence of a file does not imply that the file is readable.

## Example
    
    
    !sysfile $exists#=COLLARS.ASC  
  
---  
  
If the file `COLLARS.ASC` exists, $exists# will be set to '1', otherwise, `$exists#` will contain '0'.

Related topics and activities:

  * [STKPAR Macro Command](<stkpar.md>)

  * [STKSAV](<stksav.md>)

  * [FILE Macro Command](<file.md>)