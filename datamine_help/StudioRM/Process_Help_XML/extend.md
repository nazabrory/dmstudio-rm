# EXTEND Process

To access this process:

  * Enter "EXTEND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **EXTEND** and click **Run**.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#EXTEND>)](<../command_help/COMMAND%20TABLE_E.md#EXTEND>).

## Process Overview

Extends an existing file with data entered in free format. The method of supplying the new data is described in full in the instructions for process [INDATA](<indata.md>).

Records may not start with the character !. This is because the ! symbol acts as the end-of-data character. However, macro files, where the command starts with !, may be read if a blank is inserted prior to the ! symbol; but because records in a macro file are terminated as soon as the first comma is met, EXTEND is not suitable for extending macro files; [EXTNDF](<extndf.md>) is preferable.

### About SYSFILE

SYSFILE is an external system file name from which the free format data is to be read, or return for entry from the keyboard. Format of the system file name is system specific, with a maximum of 56 characters allowed, including pathnames.

### About DATA 

If no SYSFILE exists, data lines are entered in free format. ! terminates. The rules for free format data entry are:

  1. Data line must not be more than 80 characters in length.

  2. Text or numeric data for each field must be separated by commas. A comma is therefore not a legal character in a text field.

  3. Text fields are automatically filled with blanks to their full length, if the string given is shorter than that required. Text fields which are too long are truncated.

  4. Text fields are not entered in quotes (').

  5. An absent data code is inserted for any field coded just by a comma.

  6. Repetition of the previous value of a field in the previous record is achieved by use of the ditto mark ("). This mark cannot therefore be used within text fields.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be extended. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
  
## Example
    
    
    !EXTEND &IN(SAMPLES.1)  
  
---  
      
    
    <Listing of DD>  
      
    
    SYSFILE><return> to enter from keyboard.  
      
    
    DATA     >10,12,ABC,15<return>  
      
    
    DATA     >11.2,-,XYZ,10<return>  
      
    
    DATA     >1,22,,4<return>  
      
    
    DATA     >!<return>  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.  |   
  
Related topics and activities

  * [EXTNDF Process](<extndf.md>)

  * [INDATA Process](<indata.md>)