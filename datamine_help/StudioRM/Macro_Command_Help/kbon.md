# KBON Macro Command

Take prompted information from the keyboard.

Causes the response to prompted information to be read from the keyboard in place of the macro file. The `!KBON` command is used when it is necessary to enter data for a process via the keyboard from within a macro or menu.

The `!KBON` condition is retained in force until a ![KBOFF](<kboff.md>) command is executed, or the ![PROMPT](<prompt.md>) command is executed, which carries out an implicit `!KBOFF`. Note that the ![MENU](<menu.md>) and ![XRUN](<../Process_Help_XML/xrun.md>) also carry out an implicit `!KBOFF`. This upon return from a macro the state (`!KBON` or `!KBOFF`) returned will be that established at the end of the called macro.

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
  
The same processes, but using **KBON** /**KBOFF** to using keyboard input to define the block model prototype parameters:
    
    
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

  * [KBOFF Macro Command](<kboff.md>)