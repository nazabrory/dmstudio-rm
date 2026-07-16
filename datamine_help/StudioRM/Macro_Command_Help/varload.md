# VARLOAD Macro Command

Reads substitution variables from a file.

The variables read from file are added to the current list if the parameter `@MERGE` equals 1, otherwise any current variables are erased. **VARLOAD** will, (by default) load all substitution variables, but will allow a named set of variables only to be loaded or merged from the file.

The general format for this macro command is:
    
    
    !VARLOAD <file>[,@MERGE=<merge>] [,@DESC=$dname#][ ,$name# 
     ...]

Where:

  * `<file>` is a system file path name up to 56 chars long.

  * If the parameter `@MERGE` is not specified, or `<merge>` is zero, all current variables are erased.

    * If `<merge>` is 1, any variable that already exists in memory is updated with the file value, and new variables are added to those in memory.

  * Both `<file>` and `<merge>` may be substitution variables.

  * The description supplied when the file was created can optionally be restored into a supplied variable `<$dname>`.

  * If the optional list of variables is given, only these variables are considered; otherwise all variables are loaded. The list may be extended onto as many lines as necessary; continuation is implied by ending the previous line with a comma.

## Example
    
    
    !varload \Studio 3\projects\$proj, merge=1,   
  
---  
      
    
    $title1#, $title2#, $xmin#, $xmax#, $ymin#, $ymax#  
  
Related topics and activities:

  * [VARSAVE](<varsave.md>)