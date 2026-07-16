# GOTO Macro Command

Unconditionally branches to a specified command label within a macro or menu.

Format :
    
    
    GOTO <LABEL NAME>

The label may consist of up to 16 characters, and must be present in the current macro/menu or an error will result. Labels are denoted by using the special char ":" (colon).

See also: [BACKTO](<backto.md>), [RETURN](<return.md>), [GOSUB](<gosub.md>), [IF](<if.md>).

## Example

The following macro fragment will force macro processing to ignore all commands until the label "PLOT_INIT".
    
    
    !GOTO PLOT_INIT  
  
---  
      
    
    ...  
      
    
    ...  
      
    
    !PLOT_INIT:REM --- plot startup commands  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> INCORRECT LABEL IN GOTO/GOSUB XXXX OR XXXX NOT FOUND <<< !goto PLOT_INIT >>> ERR 75 <<< ( 3) IN MACGET The label PLOT_INIT encountered within the macro cannot be found. |  The listed label could not be found. |  Check the name and syntax of the listed label.  
  
Related topics and activities:

  * [BACKTO Macro Command](<backto.md>)

  * [RETURN](<return.md>)

  * [GOSUB](<gosub.md>)

  * [IF](<if.md>)