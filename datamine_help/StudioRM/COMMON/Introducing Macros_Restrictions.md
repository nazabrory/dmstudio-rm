# Macro Restrictions

As with any automation language, constructing a macro in a Studio product requires a particular syntax and format that is expected by your application.

There are some restrictions that should be considered when writing macros in order to avoid unexpected errors or behaviour. For example, there is a limit on the length of a filename specified in a macro (e.g. when defining an input or output file) or where you wish to use substitution variables, which also have a length limit. 

Other restrictions should also be considered when writing macros, for example, attribute field lengths within Studio products are restricted to an [upper length limit](<Attribute_Naming_Convention.md>) (either 8 or 24 characters) in both interactive and automation/macro situations.

## Macro and File Locations

The following information relates to the location of macro (.mac) and files referenced by their symbolic name within macros.

  * Macros and Projects: macros will match a specified symbolic input file name. For example, &IN(MyFile)) uses the symbolic name "MyFile", which is a project file reference (as it appears in the **Project Files** control bar). 

A macro file (.mac) is commonly located in your project folder (but it can be anywhere and can still be referenced - see "Input File Locations", below). A macro will understand current project file references to denote where an input file is located, either within or outside of the project folder.

  * Output file Location: macros will generate output files in the current project directory, regardless of where input files reside, or other parameters.

  * Input File Locations

Macros reference 'symbolic names' that represent project files used for input to a process. In this respect, your system can operate in one of two distinct modes. 

    * **Remote** mode, where a macro and input project file references can relate to files (or link files) either within or outside the current project directory. This is the default setting but can be enabled within a macro using the [!LOCDBOFF](<../Macro_Command_Help/locdboff.md>) switch command, which should appear above the relevant macro content (often at the start of the macro), for example:
          
          !START M1  
          !LOCDBOFF  
          !COPY &IN(source),&OUT(clone)  
          !END

In this example, the symbol file name "source" can be a project file that points to a remote folder location (i.e. outside the current project folder). This remote file can also be a [link file](<../Process_Help_XML/link.md>), pointing to a different location again, if required.

    * **Local** mode, where the macro and any input project file references must relate to files (or link files) within the current project directory. This setting, which reflects legacy Studio system behaviour, can be enabled in a macro using the ![LOCDBON](<../Macro_Command_Help/locdbon.md>) switch command, for example:
          
          !START M1  
          !LOCDBON  
          !COPY &IN(source),&OUT(clone)  
          !END

In this example, the symbolic file name "source" must refer to a file in the current project folder. In this scenario, the only way to access files outside of the project folder is to ensure "source" is a [link file](<../Process_Help_XML/link.md>).

**Tip** : create a local (project folder) linked copy of a Datamine file using the[ !LINK](<../Process_Help_XML/link.md>) macro command.

### Macro General Syntax

The following information relates to the general structure of a macro:

  * Macro names are case-sensitive, e.g. `!START MyMacro` is not the same as `!START MYMACRO`.

  * A macro name cannot exceed 8 characters, e.g. `M1234567` is accepted but `M12345678` is not.

  * A macro name combined with a description must not exceed 256 characters.

  * Generally, alphanumeric characters are case sensitive in macros. This includes references to files variable names, label names and values. 

    * **This does not apply to symbolic names**. For example, `&IN(MyFile)` is considered to be identical to `&IN(myfile)`.

  * If a line in a macro exceeds 256 characters, additional characters are ignored.

  * Don't use <Tab> characters to indent macro lines. Use spaces instead if indentation is required.

  * If specifying a path name in a macro (e.g. to create a link file), use the '\' character to indicate path components, not '/'.

### File Names in Macros

The following information relates to symbolic file names and macro names:

  * A symbolic file name in a macro cannot exceed **55** characters. Symbolic names are not case sensitive.

  * A macro file name (.mac) if located in the current project directory should be no longer than 256 characters.

  * A macro file name (.mac), including both path and name, if located outside the current project directory should be no longer than 256 characters.

### Macro Variables and Labels

The following information relates to the location of substitution variables and labels within macros:

  * The maximum substitution variable **name** length is **16** characters. 

  * The maximum **label** length is **16** characters. 

    * A label consists of a label name and a macro command. 

The label name is preceded by '!' and followed by ":" with no spaces in between. 

Label names are case-sensitive.

  * Variables must start with '$' and end with '#'. For example `$MyVariable#`.

  * The maximum **substituted variable** length is **80** characters. The maximum length applies to the length of the variable after substitution.

  * If loading variables from an external file such as with **[VARLOAD](<../Macro_Command_Help/varload.md>)** , the variable file description cannot exceed 68 characters.

  * The maximum **number of variables** defined in a macro is **1000**.

**Tip** : variables can be saved to an external file using ![VARSAVE](<../Macro_Command_Help/varsave.md>) and loaded from an external file (.var) using ![VARLOAD](<../Macro_Command_Help/varload.md>)

### Filename, Path and Variable Lengths Summary

The following reference table summarizes limits for macro components in terms of character length, and replicates some of the information shown above.

Macro Component |  Maximum Characters |  Notes  
---|---|---  
Datamine filename |  20 |  Name must not include spaces  
Substitution variable name |  16 |  Variables must start with '$' and end with '#'.   
Substituted variable |  80 |  The maximum length applies to the length of the variable after substitution.  
System file (path + filename) |  256 |  If specifying a path name in a macro (e.g. to create a link file), use the '\' character to indicate path components, not '/'  
A line of macro code |  256 |  This includes spaces, including following spaces which may not be visible.  
Labels |  16 |  The label name is preceded by '!' and followed by ":" with no spaces in between. Label names are case-sensitive. Example: `!START 1  
!ONERR goto <label>  
<statements1> # main body of macro  
!<label>: # error handling subroutine  
<statements2> # error handling  
!END`  
Macro file name (in project directory) |  256 |   
Macro file + path name (outside project directory) |  256 |   
Macro name |  8 |  Name must not include spaces and is case-sensitive  
Macro name + macro description |  256 |  Limit includes spaces, for example:  
  
`!START M1 Reference data with no zones`  
Variables file description |  68 |  Length includes filename extensions, such as .var.  
Stack (.stk) file path | 240 | A stack file is typically located in your installation directory's "Menus" folder, although it can also be generated using the LOADCF process.  
Environment variable values | 240 | Environment variables are defined in files stored in the "Environ" subfolder of your installation folder.  
  
**Note** : The information presented here is a brief introduction to macro writing in Studio products. There is a lot more to learn, including how to validate, debug, set up error trapping and much more. A dedicated eLearning course is available on the Datamine eLearning platform that provides a more in-depth view of the powerful macro language.

Related topics and activities

  * [Introducing Macros](<Introducing%20Macros.md>)

  * [Accessing Commands and Processes](<Studio%203%20Commands%20and%20Processes.md>)
  * [Automating Studio Products](<concept_studio%203%20scripting%20overview.md>)