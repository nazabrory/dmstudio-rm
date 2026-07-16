# RESTRI Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Relational >> Restrict Records**.

  * Enter "RESTRI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **RESTRI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RESTRI>).

## Process Overview

Perform a relational restriction operation.

Records from the first input file are copied to the output file only if there is a match between the key fields of the first and second input files. The effect is to select records from the first input file if they are matched with the entries in the second input file, using the keyfields as the match criteria. Thus restriction is essentially a record selection mechanism.

At least one keyfield must be specified and must appear in both input files as an explicit field. The key field may be up to 5 words long, and may be composed of up to 5 fields. If a field is specified which does not exist in both input files, it is ignored, providing at least one field matches.

Both input files must be sorted in the order of the keyfields before they can be processed by **RESTRI**. If this is not the case, the process will exit with an error message.

A typical use of the **RESTRI** process is to select drillholes from a file by supplying a set of borehole identifiers as the second input file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  File to have records selected (sorted on required keyfields). |  Input |  Yes |  Table  
IN2 |  File with required values of keyfields (sorted on required keyfields). |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1-10 |  Keyfields for matching. |  IN1, IN2 |  Yes |  Any |  Undefined  
  
## Example
    
    
    !RESTRI     &IN1(FILE),&IN2(BHIDS),&OUT(FILE1),*KEY1(BHID)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> INPUT FILE NOT SORTED ON KEYFIELD <<< |  One (or both) of the input files is not sorted on the designated keyfield(s). Fatal; the process is exited.  
>>> ERR 47 <<< ( 0) IN FNDKEY |  Warning; none of the specified key fields exist in the input files. An output file is produced consisting only of a Data Definition containing the fields of both input files.  
>>> KEYFIELD aaaaaaaa MISSING FROM FILE ffffffff |  A warning message that is produced if @PRINT >=1. The keyfield is ignored and processing continues.  
>>> ERR 121 <<< ( fileno) IN RESTRI |  One (or both) of the input files is empty. Fatal; the process is exited.