# Macros and File References

Studio products are frequently used amongst teams in networked environments so the ability to deal with files in locations other than the local project folder has improved.

Many Studio implementations enable remote files to be used in macros by copying the files from the network to the local project folder. This has the advantage of then processing the file locally but incurs the overhead of copying the file to the local machine and, depending on the nature of processing, possibly copying files back to the network.

This note outlines Studio macro changes made to Studio products released after June 2019 that assist with managing files outside the local Studio project folder.

## Studio Versions Prior to June 2019

In Studio product versions released prior to June 2019 macros can run processes using files that reside in the local project folder, but they cannot use files that are outside the local project folder.

For the sake of performance, macros do not require a local file to be added to the current project for the file to be found, but the file must be in the local project folder.

## Studio Versions After June 2019

In Studio versions after June 2019 (Studio RM 1.5 onwards), macros can be configured to locate files outside the project folder as long as the files have been added to the project.

Macros will still process files in the local project folder even if they have not been added to the project.

## !LOCDBON and !LOCDBOFF

Two macro commands have been added which be used to control whether a macro will look for files outside the local project folder

  * **[LOCDBON](<../Macro_Command_Help/locdbon.md>)** : Force macro commands to only use the local project folder (Default behaviour).

  * **[LOCDBOFF](<../Macro_Command_Help/locdboff.md>)** : Force macro commands to look for files that have been added to the project that may be outside the project folder.

## Notes

  * The default behaviour for macros is to use **LOCDBON**. If neither **LOCDBON** or **LOCDBOFF** has been specified files will only be searched for locally. This ensures backward compatibility for macro behaviour prior to June 2019.

  * When saving interactive commands to a macro the **!LOCDBOFF** command is added to the start of the macro. This ensures the macro will locate the same file that has been selected from the project when using the interactive command. This is not the case for saving to macros and running them prior to June 2019.  
  
By default, macros created prior to June 2019 will run identically in Studio products released before and after June 2019.

  * When automatically saving to a macro the first few lines of the macro will be something like:
        
        !START MACRO1  
        # - Use !LOCDBOFF to look for files outside the local folder  
        # - Use local files by deleting the next line or use !LOCDBON  
        !LOCDBOFF

  * The **LOCDBON** and **LOCDBOFF** commands can be used anywhere in a macro and will affect all subsequent commands in the macro. A single process can be bracketed by **LOCDBOFF** and **LOCDBON** , for example:
        
        .  
        # Get list of rock types from reference file on network.   
        # File REFROCKTYPES must be added to project  
        !LOCDBOFF  
        !COUNT &IN(REFROCKTYPES), &OUT(ROCKTYPECOUNT), *KEY1(ROCKTYPE_LIST)  
        # Revert to processing only local files  
        !LOCDBON  
          
        

  * When using files outside the local project folder, (using **LOCDBOFF**), if a command uses a remote file that is added to the project but has the same name as a file in the local folder, the remote file will be used.

Related topics and activities

  * [LOCDBON Macro Command](<../Macro_Command_Help/locdbon.md>)

  * [LOCDBOFF Macro Command](<../Macro_Command_Help/locdboff.md>)