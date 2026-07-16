# NOXRUN Macro Command  
  
To access this process:

  * **Home** ribbon **> > Automate >> Macro >> Test Macro**.
  * Enter "NOXRUN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

Validates the syntax of a macro(s) or menu(s) in a character format system file.

## How to use

The Select File screen lets you browse for and select the relevant macro file (.mac) before clicking Open. If more than one macro is present within the macro file, then the user is prompted to enter the macro name in the **Command Line**.

The macro library is located in a character format system file external to the database. Each macro command line is validated by the Command Processor, but execution is not passed to the individual process. This makes **NOXRUN** fast to execute, but prevents it from carrying out process specific checks, as for example that files exist and are in the correct format. The format of the **NOXRUN** command exactly matches that of the **[XRUN](<../Process_Help_XML/xrun.md>)** command.

The macro name may be specified following the **NOXRUN** command name. It is located in the macro library name supplied in response to the `SYSFILE> prompt`. If no macro name has been specified, and there is more than one macro in the library, then a list of macro names found in the library is displayed, and the user must select one interactively.

If the macro contains substitution variables to be substituted at run time, these variables may be entered on the command line, exactly as for the RUN command. 

Note: If the `!PROMPT` or `!LET` or `!STKPAR` commands also supply the same substitution variables, these values override those entered on the command line.

**Note** : **NOXRUN** cannot be used to validate nested macros. Each macro must be individually validated. 

## Example

The syntax when run from within a macro would be:
    
    
    !NOXRUN MACRO2,$1='*KEY1(COPPER),*KEY2(GOLD)'
    
    
    SYSFILE>MACRO.MAC

Where the **$1** parameter is a substitution variable which is passed on to the macro when it is run.

## Error and Warning Messages

**Message** |  Description |  Solution  
---|---|---  
>>> SYSTEM FILE NOT FOUND <<< >>> ERR 79 <<< ( 0) IN RUN |  The requested system file does not exist, or is corrupted or is not a character format file. Fatal; the process is exited. |  Check that the *.mac file exists and contains valid content.  
>>> MACRO NAME NOT FOUND <<< >>> ERR 72 <<< ( 0) IN RUN |  No macro name supplied. (This message is only produced if !NOXRUN is executed from a macro, and no macro name is supplied; in this case, name prompting does not take place). Fatal; the process is exited. |  Check that the specified macro name is correct.  
>>> NULL SUBSTITUTION VARIABLE NAME <<< >>> ERR 77 <<< (wordno) IN RUN |  Null or blank substitution variable. Blanks may not be replaced. wordno is the word number in the retrieval fields. Fatal; the process is exited. |  Check that the indicated substitution variable is defined correctly.  
>>> SUBSTITUTION STRING NOT IN QUOTES <<< >>> ERR 76 <<< ( wordno) IN RUN |  Substitution variable was not within quotes. **wordno** is the word number in the retrieval fields. This refers to the $1='$2' command line setting. Fatal; the process is exited. |  Check that the indicated substitution variable is using the correct syntax.  
  
Related topics and activities:

  * [XRUN Process](<../Process_Help_XML/xrun.md>)