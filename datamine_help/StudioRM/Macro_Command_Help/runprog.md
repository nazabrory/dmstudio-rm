# RUNPROG Macro Command

Run any external process from a macro, such as a batch file or executable file, including a batch file.

The general syntax for this macro command is:
    
    
    !runprog $exprog#=MyProgram.exe  
  
---  
      
    
    !if $exprog#=0, then  
      
    
    !echo ERROR: Program file $program_file# not found  
      
    
    !endif  
  
Where:

  * `MyProgram.exe` is the program you wish to execute.

  * The environment variable `$exprog#` will be set to zero or 1 depending on whether the program is found.

The macro will wait until the program has finished running before continuing its own processing (it is not asynchronous).

Tip: The external program should be placed in the current project folder, or you could write a batch file in the project folder that references an executable program elsewhere.

Related topics and activities:

  * [OPSYS Macro Command](<OPSYS.md>)