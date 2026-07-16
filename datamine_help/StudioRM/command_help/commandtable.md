# Commands and Processes

The tables shown in this section contain all commands and processes available in all Datamine Studio products. Each table represents a group of commands and processes starting with a particular letter, with design commands shown above file processes.

This Help content will provide availability status for each command or process; some commands are only available in certain applications, such as COKRIG in Studio RM, for example. If you wish to discuss expanding your Datamine software suite, please contact your local [Datamine representative](<http://www.dataminesoftware.com/contact-us/>).

## Using the Command and Process Tables

The leftmost column indicates the name of the command or process, as you would type it into the **[Command Line](<../COMMON/Command_Toolbar.md>)** to launch it.

The next series of columns represent each Studio product, with a symbol indicating command or process availability:

![](../Images/tick.png) A green tick indicates that the module is part of the core system licensing for the specified product - no additional module is required

**X** A red cross indicates the module is not part of the listed system and any commands held within it cannot be run (a separate product is required)

� A blue diamond indicates the module is an optional extra for the specified system  

### What's the difference between a "command" and a "process"?

  * A **command** is a function that works on or with a data object already loaded into memory (e.g. 'new-string', 'edit-attributes') or creates a data object. 

  * A **process** is a file-in-file-out operation; data in memory is unaffected, and where an input file is required, it is selected from disk. Similarly a file is output to disk if the process creates one.

### What is a Superprocess?

Similar to a macro, a **Superprocess** is a series of processes and other macro commands (see below) that can be performed sequentially to achieve a more complex outcome than is possible for a single command. Superprocesses appear as other processes and are created by compiling a superprocess macro via the **[LOADCF](<../Process_Help_XML/loadcf.md>)** process (yes, a process is used to create superprocesses!). 

**[TONGRAD](<../Process_Help_XML/tongrad.md>)** is an example of a superprocess. There are many others.

## Macro Commands

Macro commands are used to support processes. They provide a wide range of options, from manipulating variables to checking the syntax of a macro.

The following is a complete list of all macro commands, available in all Studio applications. A link is provided to each command's help topic.

Command Name |  Description  
---|---  
[BACKTO](<../Macro_Command_Help/backto.md>) |  Unconditionally branches to a specified screen name or label within a macro or menu.  
[ECHO](<../Macro_Command_Help/echo.md>) |  Display a message in the **[Command](<../COMMON/command%20control%20bar%20overview.md>)** control bar.  
[ELSE](<../Macro_Command_Help/else.md>) |  Evaluate one or more logical expressions involving substitution variables and constants in a macro or menu (macro/menu use only).  
[ELSEIF](<../Macro_Command_Help/elseif.md>) |  Evaluate one or more logical expressions involving substitution variables and constants in a macro or menu (macro/menu use only).  
[END](<../Macro_Command_Help/end.md>) |  End a macro or menu within a macro file (macro/menu use only).  
[ENDIF](<../Macro_Command_Help/endif.md>) |  Terminate one or more logical expressions involving substitution variables and constants in a macro or menu (macro/menu use only).  
[FIELD](<../Macro_Command_Help/field.md>) |  Detects the existence of a database field from within a menu or macro (macro/menu use only).  
[FILE](<../Macro_Command_Help/file.md>) |  Detects the existence of a database file from within a menu or macro, and, optionally, the number of records in the file (macro/menu use only).  
[GOSUB](<../Macro_Command_Help/gosub.md>) |  Stores the current macro position and branches to a specified command label within a macro or menu (macro/menu use only).  
[GOTO](<../Macro_Command_Help/goto.md>) |  Unconditionally branches to a specified command label within a macro or menu (macro/menu use only).  
[HOLD](<../Macro_Command_Help/hold.md>) |  Stop exit from macro or menu on fatal error (macro/menu use only).  
[IF](<../Macro_Command_Help/if.md>) |  Evaluate one or more logical expressions involving substitution variables and constants in a macro or menu (macro/menu use only).  
[INCLUDE](<../Macro_Command_Help/include.md>) |  Enable records from a Datamine file to be incorporated as normal data and/or statement lines within a Macro or Menu (macro/menu use only).  
[KBOFF](<../Macro_Command_Help/kboff.md>) |  Toggle OFF the keyboard after using KBON (macro/menu use only).  
[KBON](<../Macro_Command_Help/kbon.md>) |  Toggle ON the use of the keyboard as a means of data entry into a running macro or menu (macro/menu use only).  
[LET](<../Macro_Command_Help/let.md>) |  Set values of substitution variables. Arithmetic and functions are provided (macro/menu use only).  
[LOADCF](<../Process_Help_XML/loadcf.md>) |  Load a macro file (*.mac) into a menu file (*.men) for faster execution.  
[MACEND](<../Macro_Command_Help/macend.md>) |  Terminates the storage of interactive input in a character format system file.  
[MACST](<../Macro_Command_Help/macst.md>) |  Starts the storage of all subsequent interactive input in a character format system macro file.  
[MDEBUG](<../Macro_Command_Help/mdebug.md>) |  Interactively debug macros and menus.  
[MENU](<../Macro_Command_Help/menu.md>) |  Initiate the currently established menu. The menu name is requested. This must be the name of a binary random access menu file loaded by the !LOADCF command.  
[NOHOLD](<../Macro_Command_Help/nohold.md>) |  Exit from a macro or menu when a fatal error is encountered or if '!' is entered by the user (macro/menu use only).  
[NOMENU](<../Macro_Command_Help/nomenu.md>) |  Check the syntax of the currently established menu. !NOMENU works in the same way as !MENU, except that the menu is not executed.  
[NOXRUN](<../Macro_Command_Help/noxrun.md>) |  Check a macro for syntax.  
[ONERR](<../Macro_Command_Help/onerr.md>) |  Transfer control to a specified label in the menu or macro if a fatal error occurs (macro/menu use only).  
[OPSYS](<../Macro_Command_Help/OPSYS.md>) |  Transfer control to a specified label in the menu or macro if a fatal error occurs (macro/menu use only).  
[PAUSE](<../Macro_Command_Help/pause.md>) |  Pause a macro for a time proportional to the @DELAY parameter (macro/menu use only).  
[PROMPT](<../Macro_Command_Help/prompt.md>) |  Display prompts and messages on screen (macro/menu use only).  
[REM](<../Macro_Command_Help/rem.md>) |  Record comments in a macro or menu file (macro/menu use only).  
[RETURN](<../Macro_Command_Help/return.md>) |  Transfer control back to the next statement following a GOSUB statement in a macro or menu (macro/menu use only).  
[RUNPROG](<../Macro_Command_Help/runprog.md>) |  Run any external process from a macro, such as a batch file or executable  
[SCROFF](<../Macro_Command_Help/scroff.md>) |  Divert text screen output into a system file during macro execution (macro/menu use only).  
[SCRON](<../Macro_Command_Help/scron.md>) |  Restore screen output previously diverted by a !SCROFF command (macro/menu use only).  
[START](<../Macro_Command_Help/start.md>) |  Start a macro or menu (macro/menu use only).  
[STKPAR](<../Macro_Command_Help/stkpar.md>) |  Retrieve substitution variables and their values from a system character format file (macro/menu use only).  
[STKSAV](<../Macro_Command_Help/stksav.md>) |  Write substitution variables and their values to a system character format file (macro/menu use only).  
[SYSFILE](<../Macro_Command_Help/sysfile.md>) |  Check if a system file exists (macro/menu use only).  
[VARINIT](<../Macro_Command_Help/varinit.md>) |  Initialize the number of substitution variables to zero for the current macro level (macro/menu use only).  
[VARLOAD](<../Macro_Command_Help/varload.md>) |  Read substitution variables from a system text file (macro/menu use only).  
[VARSAVE](<../Macro_Command_Help/varsave.md>) |  Save or merge substitution variables into a system text file (macro/menu use only).  
[XRUN](<../Process_Help_XML/xrun.md>) |  Run a macro or menu.  
  
Related topics and activities

  * [Accessing Commands and Processes](<../COMMON/Studio%203%20Commands%20and%20Processes.md>)

  * [Retrieval Criteria](<../COMMON/Retrieval_Criteria_Overview.md>)

  * [Command and Processes Table - A](<_COMMAND%20TABLE_A.md>)

  * [Command and Processes Table - B](<commandtable_B.md>)

  * [Command and Processes Table \- C](<_COMMAND%20TABLE_C.md>)

  * [Command and Processes \- D](<COMMAND%20TABLE_D.md>)

  * [Command and Processes Table \- E](<COMMAND%20TABLE_E.md>)

  * [Command and Processes Table \- F](<COMMAND%20TABLE_F.md>)

  * [Command and Processes Table \- G](<COMMAND%20TABLE_G.md>)

  * [Command and Processes Table \- H](<COMMAND%20TABLE_H.md>)

  * [Command and Processes Table \- I](<COMMAND%20TABLE_I.md>)

  * [Command and Processes Table \- J](<COMMAND%20TABLE_J.md>)

  * [Command and Processes Table \- K](<COMMAND%20TABLE_K.md>)

  * [Command and Processes Table \- L](<COMMAND%20TABLE_L.md>)

  * [Command and Processes Table - M](<COMMAND%20TABLE_M.md>)

  * [Command and Processes Table - N](<COMMAND%20TABLE_N.md>)

  * [Command and Processes Table - O](<COMMAND%20TABLE_O.md>)

  * [Command and Processes Table - P](<COMMAND%20TABLE_P.md>)

  * [Command and Processes Table - Q](<COMMAND%20TABLE_Q.md>)

  * [Command and Processes Table - R](<COMMAND%20TABLE_R.md>)

  * [Command and Processes - S](<COMMAND%20TABLE_S.md>)

  * [Command and Processes Table - T](<COMMAND%20TABLE_T.md>)

  * [Command and Processes Table - U](<COMMAND%20TABLE_U.md>)

  * [Command and Processes Table - V](<COMMAND%20TABLE_V.md>)

  * [Command and Processes Table - W](<COMMAND%20TABLE_W.md>)

  * [Command and Processes Table - X](<COMMAND%20TABLE_X.md>)

  * [Command and Processes Table - Y](<COMMAND%20TABLE_Y.md>)

  * [Command and Processes Table - Z](<COMMAND%20TABLE_Z.md>)