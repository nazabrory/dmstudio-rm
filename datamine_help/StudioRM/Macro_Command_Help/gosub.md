# GOSUB Macro Command

Stores the current macro position and branches to a specified command label within a macro or menu.

Format :
    
    
    GOSUB <LABEL NAME>

A subroutine is any portion of a macro or menu that:

  1. Begins on a label line `!<LABEL NAME>`:
  2. Ends with a `!RETURN` statement.

The label may consist of up to 16 characters, and must be present in the current macro or menu or an error will result. Labels are denoted by using the special char ":" (colon).

See also: [RETURN](<return.md>), [GOTO](<goto.md>), [IF](<if.md>).

When an executing macro or menu encounters a **GOSUB** statement, it saves the current line number and then branches to the specified label. Execution continues normally until a [RETURN](<return.md>) statement is executed, at which point the macro or menu jumps back and resumes execution at the line after the GOSUB statement.

Execution of a RETURN statement without a corresponding **GOSUB** will give an error. For nested macros, the **RETURN** statement must be in the same macro or menu as the corresponding **GOSUB** statement. 

Note: Up to sixteen **RETURN** 's may be pending at any time within the currently executing macro or menu.

## Example

The following macro fragment will divert macro processing to the label "PLOT_INIT". When "!RETURN" is encountered, control will be diverted to the next line after "!GOSUB":
    
    
    !GOSUB PLOT_INIT  
  
---  
      
    
    .....................  
      
    
    .....................  
      
    
    !PLOT_INIT:REM - Subroutine : clean plot  
      
    
    .....................  
      
    
    .....................  
      
    
    !RETURN  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> ERR 75 <<< (3) IN ADDSFT >>> Incorrect label XXXX in GOSUB XXXX or XXXX not found <<< !gosub PLOT_INIT >>> Macro "plot ", line 54. |  The label PLOT_INIT encountered within the macro plot.mac at line 54 cannot be found within the macro. |  Check the name and syntax of the listed label.  
  
Related topics and activities:

  * [RETURN](<return.md>)

  * [GOTO](<goto.md>)

  * [IF](<if.md>)