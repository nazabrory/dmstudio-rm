# PICFLD Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Select Fields**.
  * Enter "PICDIR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PICDIR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PICFLD>).

## Process Overview

Writes field names to an output file if the field names in the input file match the given pattern expressions.

### Expression Syntax

In the following text all keywords are capitalized. When running PICFLD, any keyword may be entered in either uppercase or lowercase and abbreviated to its first three (or more) characters.

The syntax of a pattern matching expression is:

|  [FILE] |  [REGEXP] |  <pattern> |   
---|---|---|---|---  
or |  FIELD |  [REGEXP] |  <pattern> |   
or |  FIELD |  <kind> |  |   
or |  FIELD |  [REGEXP] |  <pattern> , |  <kind>  
  
The keyword "FILE" is optional. If a pattern is to be matched against field names, the keyword "FIELD" must be included. The field "kind" will be matched against the type (numeric or alphanumeric) and storage class (explicit or implicit) of the fields in any file.

The keyword "REGEXP" is normally omitted, in which case "pattern" may consist of literal characters to be matched, or one of the following elements:

? |  Any single character  
---|---  
* |  Wildcard. A group of zero or more characters  
[...] |  Any one of the characters enclosed in the square brackets. The short hand notation "a-z" means any lowercase letter; refer to the examples below for more details.  
[^...] |  Any character except one of these  
  
The special meaning of a character (e.g. "*") is lost if the character is preceded by "\", hence the match a literal "*", use "\\*". Quotes (double or single) may be used to enclose patterns if desired.

Where a pattern is applied to file names, lowercase letters are translated into uppercase before the pattern is used.

If the keyword "REGEXP" is used, the pattern specifies a full regular expression. Regular expressions allow advanced users to make more complex selections than are possible by using the pattern elements specified above.

A regular expression in PICDIR may contain the following elements.

% |  Matches the beginning of the file or field name  
---|---  
$ |  Matches the end of the file or field name  
* |  Zero or more occurrences of the preceding pattern element.  
? |  As above  
[...] |  As above  
[^...] |  As above  
  
The "kind" is a list of field type or storage class specifiers, separated by commas. Keywords that specify field type are "NUMERIC" or "ALPHANUMERIC". Storage classes are "EXPLICIT" or "IMPLICIT". Of course, any of these may be abbreviated to three (or more) letters.

If more than one type or class keyword is given, the last one specified is used.

### Concatenation of Expressions

The result of a pattern matching expression is either TRUE or FALSE. Any result may be inverted by preceding the expression by the keyword "NOT" (e.g. "NOT XPICRT,IMPLICIT"). Two expressions may be joined together by "AND" or "OR" operators. The result is another expression. The "AND" operator has higher precedence than "OR". Parentheses (brackets) may be used to override the normal order of evaluation of expressions.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file, from which fields are to be selected. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file, containing selected field names.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FIELDNAM |  Optional name for the field in OUT that is to contain the selected field names. The default is "FIELDNAM". |  OUT |  No |  Character |  FIELDNAM  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  |  Option |  Description  
---|---  
0 |  No display of matching field names >0 Display field names as they are matched. (0)  
No |  0 |  0,1 |  0,1  
APPEND |  If set to 1 then selected field names will be appended to the OUT file, provided it exists and has a valid DD (0). |  No |  0 |  0,1 |  0,1  
SORT |  If set to 1 then the output file will be sorted after all field names have been written to it (0). |  No |  0 |  0,1 |  0,1  
  
## Example

  * Select all three-letter fields that begin with "Au" or "AU". The fields must be numeric.
        
        TEST>FIELD A[uU]?,NUMERIC END

  * Select all explicit, numeric fields from a model file, except for the "standard" ones.
        
        TEST>NUMERIC,EXPLICIT AND NOT  
        TEST>([XYZ]C OR [XYZ]INC OR IJK) END

Note that brackets are required to associate the "NOT" with all the seven standard fields.

## Error and Warning Messages

Message |  Description  
---|---  
>>> WARNING: Cannot append to file ffffffff. A new file will be created |  Cannot append fieldnames to the file specified as &OUT. Check the file name given. A new &OUT file will be created.  
>>> ERROR: Files have different DDs, cannot append |  File specified in pattern matching expression and the file specified as &OUT have different DDs. Fatal; the process is exited.  
>>> ERROR: Unexpected execution error |  Fatal; the process is exited.  
>>> ERROR: Illegal instruction found |  Fatal; the process is exited.  
>>> SYNTAX ERROR AT " " |  Syntax of pattern matching expression is incorrect. Fatal; the process is exited.