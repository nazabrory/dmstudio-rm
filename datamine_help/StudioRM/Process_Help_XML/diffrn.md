# DIFFRN Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Relational >> Difference**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DIFFRN** and click **Run**.
  * Enter "DIFFRN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DIFFRN>).

## Process Overview

Perform a relational difference operation.

Records from the first input file are copied to the output file only if there is no match between the key fields of the first and second input files. The effect is to delete records from the first input file if they are matched with the entries in the second input file, using the key fields as the match criteria. Thus differencing is essentially a record deletion mechanism.

At least one key field must be specified and must appear in both input files as an explicit field. The key field may be up to 5 words long, and may be composed of up to 5 fields. If a field is specified which does not exist in both input files, it is ignored, providing at least one field matches.

Both input files must be sorted in the order of the key fields before they can be differenced. If this is not the case, the process will exit with an error message.

A typical use of the **DIFFRN** process is to delete drillholes from a file by supplying a set of borehole identifiers as the second input file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  File to have records deleted (sorted on required keyfields). |  Input |  Yes |  Undefined  
IN2 |  File containing keyfield values for deletion (sorted on required keyfields). |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1 |  Keyfield 1 for file matching. |  IN1, IN2 |  Yes |  Any |  Undefined  
KEY2 |  Keyfield 2. |  IN1, IN2 |  No |  Any |  Undefined  
KEY3 |  Keyfield 3. |  IN1, IN2 |  No |  Any |  Undefined  
KEY4 |  Keyfield 4. |  IN1, IN2 |  No |  Any |  Undefined  
KEY5 |  Keyfield 5. |  IN1, IN2 |  No |  Any |  Undefined  
KEY6 |  Keyfield 6. |  IN1, IN2 |  No |  Any |  Undefined  
KEY7 |  Keyfield 7. |  IN1, IN2 |  No |  Any |  Undefined  
KEY8 |  Keyfield 8. |  IN1, IN2 |  No |  Any |  Undefined  
KEY9 |  Keyfield 9. |  IN1, IN2 |  No |  Any |  Undefined  
KEY10 |  Keyfield 10. |  IN1, IN2 |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
KEYTOL |  **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It must be greater than or equal to zero. It replaces the previous heuristic comparison method.  If **KEYTOL** is set to a negative value then zero is used.  In a macro **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy behaviour and use a heuristic comparison in relational commands and zero in sort.  |  No |  0.00001 |  0,+ |  Undefined  
  
## Example
    
    
    !DIFFRN    &IN1(FILE),   
  
---  
      
    
     &IN2(BHIDS), &OUT(FILE1), *KEY1(BHID)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 47 <<< ( 0) IN FNDKEY |  Warning; none of the specified key fields exist in the input files. An output file is produced consisting only of a Data Definition containing the fields of both input files.  
>>> KEYFIELD nnnnnnnn MISSING FROM FILE ffffffff |  A warning message that is produced if @PRINT >=1. The keyfield is ignored and processing continues.  
>>> ERR 121 <<< ( fileno) IN DIFFRN |  One (or both) of the input files is empty. Fatal; the process is exited.  
>>> INPUT FILE NOT SORTED ON KEYFIELD |  One (or both) of the input files is not sorted on the designated keyfields. Fatal; the process is exited.