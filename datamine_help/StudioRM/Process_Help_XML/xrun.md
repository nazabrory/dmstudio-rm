# XRUN Process  
  
To access this process:

  * **Home** ribbon **> > Process >> Macro >> Run Macro**.

  * Enter "XRUN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **XRUN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_X.md#XRUN>).

## Process Introduction

Starts execution of a macro or menu. The macro or menu should be in a character-format system file.

#### Prompts

AAAAAAAA (Optional) The macro or menu name in the library.

>SYSFILE> Character-format system macro or menu file. The name may be up to 56 characters long.

If there is more than one macro or menu, and no macro or menu name was specified:-

>NAME> Enter required macro or menu name

## Example
    
    
    !>>>xrun m,$1='13.2' SYSFILE>mymac.mac  
  
---