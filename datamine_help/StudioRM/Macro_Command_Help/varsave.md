# VARSAVE Macro Command

Saves or merges substitution variables into a file. **VARSAVE** will, (by default) save all substitution variables, but will allow a named set of variables only to be saved or merged into the file.

The general format for this macro command is:
    
    
    !VARSAVE <file>[,@MERGE=<merge>] [,@DESC=<description>][ 
     ,$name# ...]

Where:

  * `<file>` is a system file path name up to 56 chars long. 

  * If the parameter `@MERGE` is not specified, or <merge> is zero, all contents of <file> are cleared first. 

  * If `<merge>` is 1, any variable that already exists in the file is updated with the current macro value, and new variables are added to the file. 

  * Both `<file>` and `<merge>` may be substitution variables. 

  * A description for the contents of the file can be supplied. The description is stored on the first record of the file with the revision number, and can be up to 68 characters long. 

  * Quotes may be used enclose the description. If the optional list of variables is given, only these variables are considered; otherwise all variables are saved. 

  * The list may be extended onto as many lines as necessary; continuation is implied by ending the previous line with a comma.

## Example
    
    
    varsave \Studio 3\projects\$proj, merge=1 , $title1#, 
     $title2#, $xmin#, $xmax#, $ymin#, $ymax#

Related topics and activities:

  * [VARLOAD Macro Command](<varload.md>)

  * [VARINIT Macro Command](<varinit.md>)