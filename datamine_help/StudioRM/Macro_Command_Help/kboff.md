# KBOFF Macro Command

Take prompted information from the macro or menu file.

Causes the response to prompted information to be read from the macro file. This is the default method of operation, in force when a macro or menu is run. The `!KBOFF` condition is set when you wish to use macros as pseudo batch runs, in which all files, fields and parameters are satisfied in the command line, and all data read by the process is contained in the macro.

## KBOFF & Other Commands

The ![PROMPT](<prompt.md>) command executes an implicit `!KBOFF` command whenever it is entered; however, the `!PROMPT` command itself always expects responses to come from the keyboard. 

The ![XRUN](<../Process_Help_XML/xrun.md>) and ![MENU](<menu.md>) processes also execute an implicit `!KBOFF` command when they are entered. This is because the default condition at the start of a menu or macro is `!KBOFF`. Upon return from a macro the state (`!KBOFF` or ![KBON](<kbon.md>)) returned will be that established at the end of the called macro.

## Examples

The following example shows how input to a process can be taken from the keyboard instead of from lines in the macro.

Defining and displaying a block model prototype using fixed parameters:
    
    
    !START 1        
  
---  
      
    
    !PROTOM   &OUT(modp1),@ROTMOD=0.0  
      
    
    n  
      
    
    n  
      
    
    0  
      
    
    0  
      
    
    0  
      
    
    10  
      
    
    10  
      
    
    10  
      
    
    100  
      
    
    100  
      
    
    1  
      
    
    !DDLIST   &IN(modp1)  
      
    
    !END  
  
The same processes, but using KBON/KBOFF to using keyboard input to define the block model prototype parameters:
    
    
    !START 1  
  
---  
      
    
    # Switch Keyboard ON:  
      
    
    !KBON  
      
    
    !PROTOM   &OUT(modp1),@ROTMOD=0.0  
      
    
    # ...  
      
    
    # Here you will be prompted for the various block model prototype parameters  
      
    
    # ...    
      
    
    # Switch Keyboard OFF:  
      
    
    !KBOFF  
      
    
    !DDLIST   &IN(modp1)  
      
    
    !END  
  
This could also be written as follows:
    
    
    !START 1  
  
---  
      
    
    # Switch Keyboard ON  
      
    
    # You will be prompted for the various block model prototype parameters.  
      
    
    # The parameters currently listed in the macro will be ignored.  
      
    
    !KBON  
      
    
    !PROTOM   &OUT(modp1),@ROTMOD=0.0  
      
    
    n  
      
    
    n  
      
    
    0  
      
    
    0  
      
    
    0  
      
    
    10  
      
    
    10  
      
    
    10  
      
    
    100  
      
    
    100  
      
    
    1  
      
    
    # Switch Keyboard OFF:  
      
    
    !KBOFF  
      
    
    !DDLIST   &IN(modp1)  
      
    
    !END  
  
Related topics and activities:

  * [KBON](<kbon.md>)