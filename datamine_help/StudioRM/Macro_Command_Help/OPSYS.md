# OPSYS Macro Command

Run an operating system Command Prompt dialog from within a macro.

Running Command Prompt commands from a macro provides the ability to:

  * Manipulate system files.

  * Run programs.

When a running macro encounters an **OPSYS** command in the lines of code, the macro running is paused until the Command Prompt command or program is complete. At this stage, the macro resumes running by proceeding to the next line of code. 

## Example

The example below copies an existing file to a new file and then opens it in Notepad.
    
    
    !OPSYS  
  
---  
      
    
    copy errorlog.dat macro_error_log.txt  
      
    
    notepad macro_error_log.txt  
  
Related topics and activities:

  * [SYSFILE Macro Command](<sysfile.md>)

  * [RUNPROG](<runprog.md>)