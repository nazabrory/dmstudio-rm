# SPLIT Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Relational >> Split**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SPLIT** and click **Run**.
  * Enter "SPLIT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SPLIT>).

## Process Overview

Take a single input file and copy the data within it to multiple output files.

A new file is generated for every unique value of a selected key field. An optional &**FNAMES** file can be used to define the output filename for each unique value in the * **KEY** field.

If the &**FNAMES** file is not defined then the output filenames will be created from the actual value of the KEY field.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. This file does not have to be sorted on the key field. |  Input |  Yes |  Table  
FNAMES |  Input file defining the file names to be used for each unique value in the **KEYVALUE** field. Must be sorted by **FILENAME** and have the fields; **FILENAME** A - Output file name to be created.  **KEYVALUE** A/N- Value of the key field which will be written to the file defined in FILENAME. This field can be either alphanumeric or numeric but must be the same type as the KEY field.  A record in the IN file may be written to more than one output file by having multiple records with the same **KEYVALUE** and different **FILENAMEs** in the **FNAMES** file. Similarly, records with different key values can be written to the same file by having multiple records with different **KEYVALUEs** and the same **FILENAME**. |  Input |  No |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY |  Alphanumeric or numeric key field in the **IN** file used for selecting data. |  IN |  Yes |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NDP |  Number of decimal places to be used for creating file names from a numeric **KEY** field (0). |  Option |  Description  
---|---  
0 |  do not display any digits after the decimal point. >0= replace the decimal point by the letter 'D' and display the specified number of digits following it. -1= create a file name using scientific notation.  
No |  0 |  -1,1 |  -1,0,1  
MAXFILES |  Maximum number of files which will be created (50). If this maximum is exceeded an error message is printed and the process is terminated. The maximum allowed value is 250 files.  Rules for creating file names from **KEY** field;  If KEY field is alphanumeric: \- only the first 24 characters will be used.  \- if a blank is encountered in the **KEY** value only those characters preceding the blank will be used.  \- if a decimal point is encountered only the character immediately following the decimal point will be used.  If KEY field is numeric: \- all file names are preceeded by one of two letters; P = plus M = minus  \- file names that are too long due to a large number of decimal places will use only the first eight characters.  \- all numbers with more than 7 digits preceeding the decimal point will be converted to scientific notation (for example, 1.23456E+09 becomes P1235P06) - trace (TR) are written to the file TRACE.  \- maximum values (+) are written to PLUS.  \- undefined values (-) are written to MINUS. |  No |  50 |  Undefined |  Undefined  
  
## Examples

### Example 1

Filenames created from a numeric *KEY field. The resultant file names, for different keyfield values are listed below for each of the 5 possible @NDP parameter values.
    
    
    !SPLIT &IN(ASSAYS), *KEY(BHID)  
  
---  
  
### Example 2

Writing multiple drillholes to a file:
    
    
    !SPLIT &IN(ASSAYS), &FNAMES(FILENAME), *KEY(BHID)  
  
---  
      
    
    &FNAMES(FILENAME)  
  
### Example 3

Writing identical drillholes to multiple files:
    
    
    !SPLIT &IN(ASSAYS), &FNAMES(FILENAME), *KEY(BHID)&FNAMES(FILENAME)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERROR: @MAXFILES outside of range 1 to 250 <<< |  The number of output files have exceeded the defined @**MAXFILES** parameter value. Increase the @**MAXFILES** parameter value (to a maximum of 250); select a different * **KEY** field; create a new keyfield in the input data file which will reduce the number of output files.  
>>> ERROR: &IN file does not exist <<< |  The &**IN** file does not exist. Check that the specified &**IN** file exists.  
>>> ERROR: Missing KEY field in &IN() <<< |  The specified * **KEY** field is incorrect or missing from &**IN**. Check that the specified * **KEY** field exists in the &**IN** file.  
>>> WARNING: &FNAMES file does not exist <<< |  The &**FNAMES** file does not exist. Check that the specified &**FNAMES** file exists.  
>>> ERROR: Missing KEYVALUE field in &FNAMES() <<< |  The field **KEYVALUE** is missing from the &**FNAMES** file. Check that the field KEYVALUE exists in the &**FNAMES** file.  
>>> ERROR: KEY and KEYVALUE fields incompatible <<< |  The * **KEY** and **KEYVALUE** fields are not the same field type. Check that the specified *KEY field and the field **KEYVALUE** are either both numeric or alphanumeric.  
>>> ERROR: Missing FILENAME field in &FNAMES() <<< |  The **FILENAME** field is missing from the &**FNAMES** file. Check that the field **FILENAME** exists in the &FNAMES file.  
>>> ERROR: FILENAME field in &FNAMES() is not alphanumeric <<< |  **FILENAME** field in &**FNAMES**() is not alphanumeric. Check that the field **FILENAME** in the &**FNAMES** file is alphanumeric.  
>>> ERROR: &FNAMES() not sorted <<< |  The &**FNAMES** file is not sorted by the **FILENAME** field. Sort the &**FNAMES** file on the **FILENAME** field.  
>>> ERROR: Too many output files >nn <<< |  Too many output files. Increase the @**MAXFILES** parameter value (to a maximum of 250); select a different * **KEY** field; create a new keyfield in the input data file which will reduce the number of output files.  
>>> ERROR: No valid output files - process aborted <<< |  No valid output files - process aborted. Check all files and parameters.  
>>> ERROR: Key fields don't match output files <<< |  Key fields don't match output files. Check all files and parameters.  
>>> ERROR: Cannot open file - process aborted <<< |  The selected input data file cannot be opened. It may be being used by another process. Complete the existing process and close the data file.