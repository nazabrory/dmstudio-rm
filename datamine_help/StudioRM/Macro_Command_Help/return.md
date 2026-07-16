# RETURN Macro Command  
  
Transfers control back to the next statement following a [GOSUB](<gosub.md>) statement in a macro or menu.

There may be a number of **GOSUB** 's in the same subroutine, and a **RETURN** occurring in that subroutine returns control to the statement following the specific **GOSUB** used to get to the subroutine.

Note: A subroutine should only be entered by using a **GOSUB**. Otherwise, the **RETURN** statement will cause an error when it is executed.

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
  
Related topics and activities:

  * [GOSUB Macro Command](<gosub.md>)