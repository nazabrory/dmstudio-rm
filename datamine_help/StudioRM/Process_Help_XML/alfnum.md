# ALFNUM Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Set Value >> Alpha to Numeric.**
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ALFNUM** and click **Run**.
  * Enter "ALFNUM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ALFNUM>).

## Process Overview

Copies a file while converting given alphanumeric fields to numeric.

The new fields are given the same name as the old, and replace them in the output file. Legal characters are 0-9,+,-,., and E. Any other characters are replaced by blanks before conversion. If the resulting string can still not be converted to a legal number, then the output field will contain an absent data value.

A minimum of one explicit alphanumeric field must be in the input file for conversion, but other fields may optionally be specified, up to a maximum of 20 fields.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file containing explicit alphanumeric field(s) to be converted. |  Input |  Yes |  Table  
FIELDLST |  File to supply selected fields. |  Input |  No |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file containing given alphanumeric field(s) converted to numeric.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  Name of alphanumeric field to be converted. |  IN |  Yes |  Character |  Undefined  
F2 |  Optional second explicit alphanumeric field to be converted. |  IN |  No |  Character |  Undefined  
F3 |  Optional third explicit alphanumeric field to be converted. |  IN |  No |  Character |  Undefined  
F4 |  Optional fourth explicit alphanumeric field to be converted. |  IN |  No |  Character |  Undefined  
F5 |  Optional fifth explicit alphanumeric field to be converted. |  IN |  No |  Character |  Undefined  
FIELDNAM |  Field in FIELDLST to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Example
    
    
    !ALFNUM &IN(ALPHAS),&OUT(NUMS),*F1(SAMPLENO)The "SAMPLENO" alphanumeric field in input file alphas is converted to numeric in the output file nums.  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> FIELD NOT IN FILE <<<  
>>> ERR 130 <<< ( fieldno) IN ALFNUM |  An alphanumeric field specified for conversion to numeric does not exist in the input file. Fatal; the process is exited.  
>>> FIELD IS ALREADY NUMERIC <<<  
>>> ERR 131 <<< ( fieldno) IN ALFNUM |  The given field names are checked to see that they are explicit and alphanumeric. If they are not, the process exits with the above error message.  
>>> TOO MANY FIELDS <<<  
>>> ERR 132 <<< ( 64) IN ALFNUM |  There are more than 64 fields in the output file. Fatal; the process is exited.  
|   
>>> TOO MANY FIELDS TO BE CONVERTED <<<  
>>> ERR 133 <<< ( 20) IN ALFNUM |  More than 20 alphanumeric fields have been specified for conversion to numeric. Fatal; the process is exited.  
>>> WARNING - RECORD 999999 FIELD aaaaaaaa - ABSENT DATA SUBSTITUTED <<< |  If a string cannot be converted to a legal number, then the record is displayed together with the above error message. The output field will contain an absent data value '-' and processing continues.