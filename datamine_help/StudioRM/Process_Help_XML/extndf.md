# EXTNDF Process

To access this process:

  * Enter "EXTNDF" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **EXTNDF** and click **Run**.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#EXTNDF>)](<../command_help/COMMAND%20TABLE_E.md#EXTEND>).

## Process Overview

Extends an existing file with data entered in fixed format.The data may come either from the keyboard, or from a character system file external to the database (maximum 80 characters wide).

The data format may come either from the file description, entered when the Data Definition was originally set up, or from the format line.

You will be prompted for the following information on running the process:

  * **SYSFILE** Enter the external file name (max 56 characters); Leave blank if there is no external file name.

  * **FORMAT** Enter the FORTRAN format in brackets. Max 80 characters, with character data in A4 units (e.g. 3A4, A2) and E or F format for numbers (e.g. 3F12.0). Integers as F format (e.g. F6.0). If format is already in the FILE DESCRIPTION, then enter _< return>_.

  * **DATA** Data lines, in defined format; ! terminates.

Incorrect data records (those not matching the specified format statement) are ignored, with a message to the display.

Records may not start with the character !. This is because the ! symbol acts as the end-of-data character. However macro files, where the command starts with !, may be read if a space is inserted prior to the ! symbol. The format for macro (or any other files being read into a standard character format database file) is (20A4).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be extended. |  Input |  Yes |  Undefined  
  
## Example
    
    
    !EXTNDF &IN(SAMPLES.1)  
  
---  
      
    
    SYSFILE>data.dat<return>  
      
    
    FORMAT >(2A4,F7.2,F7.2,F8.3)<return>  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.   
>>> FORMAT CONVERSION ERROR <<< (listing of record) |   
ERR 80 <<< ( 0) IN FMTDCD |  The given record did not match the format entered. Warning; the record is ignored.  
ERR 94 <<< (charposn) IN INPFMT ERROR IN FORMAT AT CHARACTER POSITION nnn FORMAT >>> (listing of format) |  The format was illegal. Only A, E, F, G and X descriptors are allowed. Fatal; the process is exited.  
  
Related topics and activities

  * [EXTEND Process](<extend.md>)

  * [INDATA Process](<indata.md>)