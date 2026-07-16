# INPUTW Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Text Utilities >> Input Fixed Format Data**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **INPUTW** and click **Run**.
  * Enter "INPUTW" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INPUTW>).

## Process Overview

Enters wide (maximum 4096 characters) formatted data from keyboard or from a system character file external to the database.

A Data Definition must already exist, and is read from file &IN. The new file is written to &**OUT**. If &**IN** and &**OUT** are the same name then the new data will replace any that may exist in the old. Otherwise a new file is created, leaving the old file intact.

The data may come either from the keyboard, or from a character system file external to the database. The maximum width of the data record is 240 characters.

The data format may come either from the file description, entered when the Data Definition was originally set up, or from the format line.

Note: Incorrect data records (those not matching the specified format statement) are ignored.

### Prompts

**INPUTW** is an interactive process and displays the following prompts in the Command toolbar:

  * > SYSFILE >

External file name (max 56 characters). Blank for none.

  * > FORMAT >

FORTRAN format in brackets. Max 80 chars, with character data in A4 units (e.g. 3A4,A2) and E or F format for numbers (e.g. 3F12.0). Integers as F format (e.g. F6.0). If format is already in the file description of the file on **IN** , then just <return> is entered to use the format.

  * > DATA >

Data lines if no **SYSFILE** , in defined format. ! terminates.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File containing Data Definition. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File to be created (may be same as **IN** ; if it is, the original data in file is overwritten).  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  >=1 Display each record (0). |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !INPUTW    &IN(SAMPLEDD),&OUT(SAMPLES),@PRINT=1  SYSFILE>data.dat  
  
---  
      
    
    (Listing of DD)  
      
    
    FORMAT >(20A4,3F7.2,F7.2,F8.3)  
      
    
    (Listing of each record)  
  
This example takes the existing Data Definition from file **sampleDD** , and writes the data records into file samples. The formatted input records are taken from character format file data.dat external to the database, and the format is entered directly as a response to the **FORMAT** prompt. The @**PRINT** parameter lists each record as it is read in.

## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited. |   
>>> FORMAT CONVERSION ERROR <<<  
(listing of record) >>> ERR 80 <<< ( 0) IN FMTDCW |  The given record did not match the format entered. Warning; the record is ignored. |   
>>> ERR 94 <<< (charposn) IN INPFMT >>> ERROR IN FORMAT AT CHARACTER POSITION nnn  
>>> FORMAT >>>  
>>>>>>(listing of format) |  The format was illegal. Only A, E, F, G and X descriptors are allowed. Fatal; the process is exited. |   
  
Related topics and activities

  * INPUTW Process

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFIL Process](<inpfil.md>)

  * [INPFML Process](<inpfml.md>)

  * [INPUTC Process](<inputc.md>)

  * [INPUTD Process](<inputd.md>)

  * [OUTPUT Process](<output.md>)