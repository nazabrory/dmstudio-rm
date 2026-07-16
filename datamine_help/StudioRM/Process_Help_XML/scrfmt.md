# SCRFMT Process  
  
To access this process:

  * Enter "SCRFMT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SCRFMT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SCRFMT>).

## Process Overview

Legacy process used to format text using format controls defined in the **SCREEN** command.

The output is sent to the screen, and optionally the print file and/or a Datamine file. The text to be formatted can be entered directly, or supplied from an external text file, with an optional keyword. Only one external file (and key if supplied) can be referenced.

In the external file the key is prefixed by the characters . Specification of an external file is as follows:
    
    
    sysfile [,key [,prepended fmt_txt]]

**Note** : The maximum number of formatted text lines allowed is 500.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  Output database file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
TEXT |  Optional name for the field that is to contain the formatted text. The default is "TEXT". |  OUT |  No |  Character |  TEXT  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
WIDTH |  Width of output text in characters in the range 1-132 (80). | No | 80 | 1,132 | Undefined  
PRINT |  Control whether output should be sent to the print file, with the default as none (0). | No | 0 | 0,1 | 0,1