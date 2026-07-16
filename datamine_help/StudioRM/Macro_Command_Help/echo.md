# ECHO Macro Command

Display a message in the **Command** control bar during macro playback.

Only one line of text can be displayed with each `!ECHO` command line; multiple ECHO commands are required in sequence to lay out multiple lines of message, with the possibility of including blank lines.

Note: The[PROMPT](<prompt.md>)command can also be used to display multiple lines of message.

Note: Macro commands are used within macros to provide more complex behaviour when running processes.

## Example
    
    
    !ECHO!ECHO Sample File  
  
---  
      
    
    !ECHO -----------  
      
    
    !ECHO  
      
    
    !ECHO Filename: $Var1#  
  
Related topics and activities:

  * [PROMPT](<prompt.md>)