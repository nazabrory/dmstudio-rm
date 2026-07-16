# START Macro Command

Starts a macro or menu.

The `!START <macroname>` command must be the first in a macro or menu. The `<macroname>` parameter defines the name of the macro or menu. It must be unique within a macro library. 

Note: A macro name may be up to 8 characters long, and may not start with the characters @, &, * or !. It should not contain embedded blanks or the characters = > < ' or ,. Upper and lower case names are considered different.

Following the macro name, a comment may be placed, separated from the macroname by one or more commas. For example:-

`!START mac1` This is a section plotting macro

The `macroname` and the comment will be shown if you are invited to select the required macro from several.

## Example
    
    
    !start MYMAC Macro to validate data.  
  
---  
  
Related topics and activities:

  * [END Macro Command](<end.md>)

  * [PAUSE Macro Command](<pause.md>)

  * [MACST Macro Command](<macst.md>)

  * [MACEND Macro Command](<macend.md>)