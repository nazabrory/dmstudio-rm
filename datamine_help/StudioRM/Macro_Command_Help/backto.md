# BACKTO Macro Command

Unconditionally branch to a specified screen name or label within a macro or menu (a menu is a compiled macro).

Note: Macro commands are used within macros to provide more complex behaviour when running processes.

## Example
    
    
    BACKTO <LABEL NAME> BACKTO <SCREEN NAME>  
  
---  
  
  * `LABEL` may consist of up to 16 characters, and must be present in the current macro/menu or an error will result. Labels are denoted by the special char ":" (colon). 

  * `SCREEN NAME` must have been defined within the current or an ancestor of the current macro/menu as part of a [SCREEN](<screen.md>) command. The name may consist of up to 16 characters. If the name is not a known screen name in the list of screens traversed in the current session, the name is treated as a local macro label, and a [GOTO](<goto.md>) is attempted.

## Macro Command Example
    
    
    !Plot:rem... (further processing)  
  
---  
      
    
    !SCREEN NAME:Plot_param  
      
    
    ... (further processing)  
      
    
    !BACKTO:Plot  
      
    
    ... (further processing)  
      
    
    !BACKTO:Plot_param  
  
Related topics and activities:

  * [Commands and Processes](<../command_help/commandtable.md>)

  * [SCREEN](<screen.md>)

  * [GOTO](<goto.md>)

  * [GOSUB](<gosub.md>)

  * [RETURN](<return.md>)

  * [Accessing Commands and Processes](<../COMMON/Studio%203%20Commands%20and%20Processes.md>)