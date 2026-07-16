# COUNT Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Statistics Processes >> Bivariate Statistics**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COUNT** and click **Run**.
  * Enter "COUNT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COUNT>)

## Process Overview

Outputs a file containing each different value of a set of keyfields, and the number of occurrences of each value.

An up to five word keyfield is specified as 1-5 keyfield names. The output file contains these fields, together with a new field COUNT. This contains the number of occurrences of each set of keyfield values.

A typical use of COUNT is to find the number of samples in each drillhole (keyed on drillhole ID).

**Note** : the field "COUNT", if it exists in the input file, must not be used as a keyfield.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file, sorted on required keyfields. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  File containing counts. Will contain specified keyfields + field COUNT holding number of keyfield combinations found.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1 |  Keyfield 1 for counting. |  IN |  Yes |  Any |  Undefined  
KEY2 |  Keyfield 2. |  IN |  No |  Any |  Undefined  
KEY3 |  Keyfield 3. |  IN |  No |  Any |  Undefined  
KEY4 |  Keyfield 4. |  IN |  No |  Any |  Undefined  
KEY5 |  Keyfield 5. |  IN |  No |  Any |  Undefined  
KEY6 |  Keyfield 6. |  IN |  No |  Any |  Undefined  
KEY7 |  Keyfield 7. |  IN |  No |  Any |  Undefined  
KEY8 |  Keyfield 8. |  IN |  No |  Any |  Undefined  
KEY9 |  Keyfield 9. |  IN |  No |  Any |  Undefined  
KEY10 |  Keyfield 10. |  IN |  No |  Any |  Undefined  
  
## Example
    
    
    !COUNT    &IN(FILE1), &OUT(COUNT), *KEY1(BHID), @PRINT=1  
  
---  
      
    
    (Listing of input file DD)  
      
    
    (Listing of output file DD)  
      
    
    320 RECORDS READ  
      
    
    135 DIFFERENT KEY OCCURRENCES FOUND.  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 47 <<< ( 0) IN FNDKEY |  Warning; none of the specified key fields exist in the input file. An output file is produced with the field COUNT containing the number of records in the input file.  
>>> KEYFIELD nnnnnnnn MISSING FROM FILE ffffffff |  A warning message that is produced if @PRINT >=1. The keyfield is ignored and processing continues.