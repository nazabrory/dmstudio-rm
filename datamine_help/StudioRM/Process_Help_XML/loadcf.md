# LOADCF Process

To access this process:

  * **Home** ribbon **> > Automate >> Macro >> Convert to Menu**.
  * Enter "LOADCF" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LOADCF>).

## Process Overview

Convert a macro file (*.mac) into a standard menu file (*.men) for faster execution.

LOADCF pre-processes macros to increase their general runtime performance. Specific optimization can be performed for customized SCREEN based menu applications. Three levels of processing (controlled by setting parameter LEVEL in the dialog) are available:  

LEVEL = 0 Converts the macro file into the standard .STK and .MEN files.  

LEVEL = 1 Optimizes the performance for screen based menus with the following:

  1. Pre-processes and verifies !SCREEN definitions to create 'tokenized' SCreen Code (.SCC) and SCreen Text (.SCT) files for the menu.
  2. Replaces !SCREEN code with references to relevant entries in .SCC file.
  3. Strips !REM and # inline remarks, remove indentation.

**Note** : If there is more than one macro in the file to be loaded, only the first macro will be loaded. .

You can choose the name of the binary random access menu file to be created. This may be up to 56 characters long, and may include pathnames. It must not contain the character '.', except as part of an up to three character extension. If an extension is given, it will be used; otherwise an extension of form .MEN will be appended. The following are legal menu names:-

  * mymenu.men

  * Datamine/mymenu.dat

If the response to the menu name question is blank<return> or just <return>, then a name MENUFILE.DAT will be assumed. This is for compatibility with earlier releases of Datamine products.

The menu name set up in !**LOADCF** is the one that must be specified in the !**menu** or !**nomenu** commands.

Note: The !**LOADCF** process deletes the stack file <name>.STK, where <name> is the requested macro name minus the extension. 

## Aliased menus, or "Supercommands"

It is possible to provide aliases for menus. If this is done, then a menu can be executed simply by entering its name at the command prompt. In order to establish the alias, you must edit the file "dmalias.dat". The primary copy of this file is supplied in the helpfile directory. You can either edit this copy, or make a local version in your database directory. A menu which has an alias is referred to as a "supercommand". The alias file contains three columns, each eight characters wide. The first column contains an alias that may be used. The second column contains the name of the command or menu to be executed. If the third column is "**MENU** ", then the alias refers to a menu file produced by **LOADCF**. Otherwise, if the third column is blank, the alias refers to a command. If any entry in the alias (first) column is blank, then that line specifies the "default" command to be executed if the user enters an invalid command. For example, the line " **DOHELP MENU** " would cause the menu "**DOHELP** " to be executed if the user enters something that cannot be recognized as either the name of a built-in command or an alias. If multiple lines refer to the same alias, then the last one is used.

A _supercommand_ can have its own help file. The help file format must follow that of established processes (like this one), and will be read and interpreted by the command processor. Files, field and parameter assignments will be passed to the menu, where they will appear as pre-assigned substitution variables. The names of such variables will refelct the type and symbolic name of the file, field or parameter assignment.

For example, if an aliased menu (or "**supercommand** ") is assigned an input file ("**IN** ") , then the actual file name is passed in a variable called "**$IN#** ". Similarly, if a field is assigned using the symbolic name "**X** " , the value assigned is passed in the variable "**$X#** ". These names follow the convention of ending in "**#** " that is followed by the authors of most macros. Supercommands do not accept retrieval criteria.

## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  Macro line display (0). =0 Do not display.=1 Display each line of the macro file as loaded. |  No |  0 |  0,1 |  0,1  
LEVEL |  Level of menu compilation . =0 Standard compilation. =1 'Optimise' for !SCREEN processing (0). |  No |  0 |  0,1 |  0,1  
ENCRYPT |  Encryption level (0). =0 None. =1 Macro is encrypted |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !LOADCF>>> ENTER NAME OF CHARACTER SYSTEM FILE FOR INPUT <<<  
  
---  
      
    
    SYSFILE>menu.mac  
      
    
    >>> ENTER MENU NAME <<<  
      
    
    NAME >mymenu  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> INPUT SYSTEM FILE DOES NOT EXIST <<<  
|  The input macro file (*.mac) does not exist. Fatal; the process is exited. |  Check the existence, location and name of the relevant macro file.  
>>> ERROR IN CREATING OUTPUT FILE <<<  
|  There is a system problem in trying to open the output file. Fatal; the process is exited.  |  If the menu file already exists, it should be deleted and the process restarted.