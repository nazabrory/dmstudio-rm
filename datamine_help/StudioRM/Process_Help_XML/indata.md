# INDATA Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Text Utilities >> Input CSV with Existing DD**.
  * Enter "INDATA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **INDATA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INDATA>).

## Process Overview

Enters free-format data (i.e. with the data items separated by commas) from the keyboard or from a system character file external to the database.

A data definition must already exist, and is read from file &**IN**. Any Datamine file may be used as a data definition. This defines the names of the fields, whether the field is numeric or alphanumeric, and if alphanumeric, the length. It also defines each fields default value, and if a field is an implicit or explicit field.

The _records_ in the &**IN** file are not used (so a block model or a prototype model copied from a block model without records would produce the same result.

The new file is written to &**OUT**. If &**IN** and &**OUT** are the same name then the new data will replace any that may exist in the old (an "in-place update"). Otherwise a new file is created, leaving the old file intact.

Note: Data records may not start with the character "!". This is because the ! symbol acts as the end-of-data character. However, macro files, where the command starts with !, may be read if a blank is inserted prior to the ! symbol.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File containing Data Definition. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File to be created (may be same as IN; if it is, then original data in file is overwritten).  
  
## Example
    
    
    !INDATA &IN(INPROTO),&OUT(DATAFILE)SYSFILE><return>  
  
---  
      
    
    DATA >12.6,DATA1234,15,10,9,ABC,X<return>  
      
    
    DATA >11.2,,15,10.3,8,","<return>  
      
    
    DATA >11.6,DATA5678,15,18,,<return>  
      
    
    DATA >!<return>  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.  
>>> NOT A NUMBER <<<  
>>> ERR 57 <<< (numbposn) IN STRDCD |  An illegal Datamine number has been entered. Warning; the record is ignored.  
  
Related topics and activities

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFIL Process](<inpfil.md>)

  * [INPFML Process](<inpfml.md>)

  * [INPUTC Process](<inputc.md>)

  * [INPUTD Process](<inputd.md>)

  * [INPUTW Process](<inputw.md>)

  * [OUTPUT Process](<output.md>)