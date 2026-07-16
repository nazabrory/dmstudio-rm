![](../HeaderCell.jpg) |  Macro Commands Macro-specific commands  
---|---  
  
# Macro Commands

The following commands, except where indicated with *, are used only within macros in order to provide enhanced functionality and control within the macro processing environment.

Macro Command |  **Description** |  Links to Examples  
---|---|---  
ECHO |  Display a single line of text from within a macro. |  [Example 1](<../Exercises/messages.md#ECHO_Example1>)  
END |  Ends a macro or menu within a macro library. |  [Example 1](<../Exercises/basic_macro_layout.md#END_Example1>)  
ELSE |  Conditionally branches to a specified command label within a macro or menu. |  [Example 1](<../Exercises/conditional_statements.md#ELSE_Example1>)  
ELSEIF |  Conditionally branches to a specified command label within a macro or menu. |  [Example 1](<../Exercises/conditional_statements.md#ELSEIF_Example1>)  
ENDIF |  Ends a conditional branching sequence. |  [Example 1](<../Exercises/conditional_statements.md#ENDIF_Example1>)  
FIELD |  Sets up substitution variables to the values of fields in a Datamine file, for a particular record. Default values may also be found. |  [Example 1](<../Exercises/accessing_a_datamine_file_s_data.md#FIELD_Example1>), [Example 2](<../Exercises/accessing_a_datamine_file_s_data.md#FIELD_Example2>)  
FILE |  Checks for the existence of a Datamine file, and sets number of records. |  [Example 1](<../Exercises/accessing_a_datamine_file_s_data.md#FILE_Example1>), [Example 2](<../Exercises/accessing_a_datamine_file_s_data.md#FILE_Example2>)  
GOSUB |  Stores the current macro position and branches to a specified command label within a macro or menu. |  [Example 1](<../Exercises/Subroutines.md#GOSUB_Example1>)  
GOTO |  Unconditionally branches to a specified command label within a macro or menu. |  [Example 1](<../Exercises/Subroutines.md#GOTO_Example1>), [Example 2](<../Exercises/loops.md#GOTO_Example2>)  
HOLD |  Prevents exit from a macro if a DATAMINE fatal error occurs. |  [Example 1](<../Exercises/Diverting_Command_Control_Bar_Text_to_a_System_File.md#HOLD_Example1>)  
IF |  Conditionally branches to a specified command label within a macro or menu. |  [Example 1](<../Exercises/conditional_statements.md#IF_Example1>)  
INCLUDE |  Enables records from a DATABASE file to be included as normal data and/or statement lines within a Macro or Menu. |  [Example 1](<../Exercises/including_datamine_file_records_as_lines_in_a_macro.md#INCLUDE_Example1>)  
LET |  Sets values of substitution variables. Arithmetic and functions are provided. |  [Example 1](<../Exercises/working_with_variables.md#LET_Example1>)  
LINK |  Links a Datamine file, located outside the project folder, to a Datamine link file located in the project folder. |  [Example 1](<../Exercises/Creating_a_New_Project.md#LINK_Example1>)  
NOHOLD |  Allows exit from a macro, if a fatal error occurs, previously prevented by a !HOLD command. |   
ONERR |  Transfers control to a given label if a fatal error occurs. |  [Example 1](<../Exercises/error_trapping.md#ONERR_Example1>), [Example 2](<../Exercises/Diverting_Command_Control_Bar_Text_to_a_System_File.md#ONERR_Example2>)  
OPSYS |  Run an operating system Command Prompt dialog from within your application. |  [Example 1](<../Exercises/Using_an_Operating_System_Command_Prompt_in_Macros.md#OPSYS_Example1>)  
PROMPT |  Displays lines on screen and prompts for input. |  [Example 1](<../Exercises/prompting_for_data.md#PROMPT_Example1>), [Example 2](<../Exercises/messages.md#PROMPT_Example2>), [Example 3](<../Exercises/working_with_variables.md#PROMPT_Example3>)  
REM |  Allows comments to be put anywhere in a macro. |  [Example 1](<../Exercises/comments.md#REM_Example1>)  
RETURN |  Transfers control back to the next statement following the GOSUB. |  [Example 1](<../Exercises/Subroutines.md#RETURN_Example1>), [Example 2](<../Exercises/loops.md#RETURN_Example2>)  
SCROFF |  Diverts Command control bar text output into a system file during macro execution. |  [Example 1](<../Exercises/Diverting_Command_Control_Bar_Text_to_a_System_File.md#SCROFF_Example1>)  
SCRON |  In a macro, restores Command control bar text output previously diverted by a !SCROFF command. |  [Example 1](<../Exercises/Diverting_Command_Control_Bar_Text_to_a_System_File.md#SCRON_Example1>)  
START |  Names a macro in a macro library i.e. in a *.mac text file. |  [Example 1](<../Exercises/basic_macro_layout.md#START_Example1>)  
SYSFILE |  Checks for the existence of a system file. |  [Example 1](<../Exercises/conditional_statements.md#SYSFILE_Example1>)  
UNLINK |  Unlinks a Datamine link file that was created by the macro command LINK. |  [Example 1](<../Exercises/Creating_a_New_Project.md#UNLINK_Example1>)  
VARLOAD |  Reads substitution variables from a file i.e. a *.var text file. |  [Example 1](<../Exercises/working_with_variables.md#VARLOAD_Example1>)  
VARSAVE |  Saves or merges substitution variables into a file i.e. a *.var text file. |  [Example 1](<../Exercises/working_with_variables.md#VARSAVE_Example1>)  
XRUN |  Starts execution of a macro in a character format system file. |  [Example 1](<../Exercises/running_macros_from_scripts.md#XRUN_Example1>)  
  
![note.gif \(1017 bytes\)](../Images/note.gif) |  These commands are not available as toolbar menu options and cannot be run from the command line in the Command Toolbar.  
---|---  
  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Macro Writing Tools](<macro_writing_tools.md>)