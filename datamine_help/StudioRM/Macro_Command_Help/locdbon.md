# LOCDBON Macro Command

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LOCDBON>).

Force macro commands to only use the local project folder (Default behaviour).

Macro command notes:

  * The default behaviour for macros is to use `LOCDBON`. If neither `LOCDBON` or [LOCDBOFF](<locdboff.md>) has been specified files will only be searched for locally. This ensures backward compatibility for macro behaviour prior to June 2019.

By default, macros created prior to June 2019 will run identically in Studio products released before and after June 2019.

  * When saving interactive commands to a macro the `LOCDBOFF` command is added to the start of the macro automatically. This ensures the macro will locate the same file that has been selected from the project when using the interactive command. This is not the case for saving to macros and running them prior to June 2019.

  * When automatically saving to a macro the first few lines of the macro will be something like:
        
        !START MACRO1  
        # - Use !LOCDBOFF to look for files outside the local folder   
        # - Use local files by deleting the next line or use !LOCDBON  
        !LOCDBOFF

  * The `LOCDBON` and `LOCDBOFF` commands can be used anywhere in a macro and will affect all subsequent commands in the macro. A single process can be bracketed by `LOCDBON` and `LOCDBOFF`, for example:
        
        # Get list of rock types from reference file on 
        # network. File REFROCKTYPES must be added to project  
        !LOCDBOFF  
        !COUNT &IN(REFROCKTYPES), &OUT(ROCKTYPECOUNT), *KEY1(ROCKTYPE_LIST)  
        # Revert to processing only local files  
        !LOCDBON  
        

  * When using files outside the local project folder (using `LOCDBOFF`), if a command uses a remote file that is added to the project but has the same name as a file in the local folder, the remote file will be used.

Related topics and activities:

  * LOCDBON Macro Command
  * [LINK Process](<../Process_Help_XML/link.md>)