# ENDIF Macro Command

Terminates one or more logical expressions involving substitution variables and constants in a macro or menu.

Note: This is used as part of the `!IF` command.

Note: Macro commands are used within macros to provide more complex behaviour when running processes.

## Example
    
    
    !IF <CONDITION>, ... ,THEN statement(s)     
  
---  
      
    
      !ELSEIF <CONDITION>, ...,THEN statement(s)  
      
    
      !ELSEIF <CONDITION>, ...,THEN statement(s)  
      
    
    !ELSE statement(s)  
      
    
    !ENDIF  
  
Related topics and activities:

  * [ELSE Macro Command](<else.md>)

  * [ELSEIF Macro Command](<elseif.md>)

  * [IF](<include.md>)