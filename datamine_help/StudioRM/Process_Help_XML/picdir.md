# PICDIR Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Make Fields Implicit**.
  * Enter "PICDIR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PICDIR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PICDIR>).

## Process Overview

Writes file names to an output file (catalogue file) if the file name or field names within the file match the given pattern expressions.

### Expression Syntax

In the following text all keywords are capitalized. When running **PICDIR** , any keyword may be entered in either uppercase or lowercase and abbreviated to its first three (or more) characters.

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

Where a pattern is applied to file names, lower case letters are translated into upper case before the pattern is used.

If the keyword "REGEXP" is used, the pattern specifies a full regular expression. Regular expressions allow advanced users to make more complex selections than are possible by using the pattern elements specified above.

A regular expression in **PICDIR** may contain the following elements.

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

The result of a pattern matching expression is either TRUE or FALSE. 

Any result may be inverted by preceding the expression by the keyword "NOT" (for example, "NOT XPICRT,IMPLICIT"). Two expressions may be joined together by "AND" or "OR" operators. The result is another expression. 

The "AND" operator has higher precedence than "OR". Parentheses (brackets) may be used to override the normal order of evaluation of expressions.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Catalogue |  Output catalogue file, giving list of files.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FILE |  Optional name for the field that is to contain the file names. The default is "'FILENAM", i.e. PICDIR will produce a catalogue file. |  OUT |  No |  Character |  FILENAM  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
APPEND |  If set to 1 then selected field names will be appended to the **OUT** file, provided it exists and has a valid DD (0). |  No |  0 |  0,1 |  0,1  
PRINT |  |  Option |  Description  
---|---  
0 |  No display of matching file names >0 Display file names as they are selected. (0)  
No |  0 |  0,1 |  0,1  
SORT |  If set to 1 then the output file will be sorted after all file names have been written to it (0). |  No |  0 |  0,1 |  0,1  
LONGNAME |  If set to 1 then the fields **LOGICAL** (5A4) and **SYSTEM** (32A4) will be added to the output file. **LOGICAL** is the full, logical (long) name of the file. **SYSTEM** contains the full path name of the file. The default for **LONGNAME** is (0). |  No |  0 |  0,1 |  0,1  
  
## Example

  * Select files whose name ends in "S", except for the file "PRECIOUS".
        
        TEST>*S AND NOT PRECIOUS END

  * Select all perimeter files.
        
        TEST>FIELD XP,NUMERIC,EXPLICIT AND  
        TEST>FIELD YP,NUMERIC,EXPLICIT AND  
        TEST>FIELD ZP,NUMERIC,EXPLICIT AND  
        TEST>FIELD PTN,NUMERIC,EXPLICIT AND  
        TEST>FIELD PVALUE,NUMERIC,EXPLICIT END

  * A database contains a series of section plots. Sections are spaced 50 meters apart. A file naming convention has been used, such that the name is made up from a five-digit section coordinate, followed by a direction code ("N" or "E"), followed by ".P". Select (by name only) all such files for sections 10200N to 10700N and 20800E to 21150E.
        
        TEST>10[2-7]00N.P OR 10[2-6]50N.P OR  
        TEST>20[89][05]0E.P OR 21[01][05]0E.P END

  * Select all files that contain implicit alphanumeric fields. (This will select all RESULTS files).
        
        TEST>ALPHA,IMPLICIT END

## Error and Warning Messages

Message |  Description  
---|---  
>>> WARNING: Cannot append to file ffffffff. A new file will be created |  Cannot append fieldnames to the file specified as &OUT. A new &OUT file will be created. Check the specified file name.  
>>> ERROR: Unable to open file ffffffff |  File will be ignored by PICDIR Cannot open file specified in pattern matching expression. Ignored.  
>>> ERROR: PICDIR works with native file databases |  Fatal; the process is exited.  
>>> ERROR: Files have different DDs, cannot append |  File specified in pattern matching expression and the file specified as &OUT have different DDs. Fatal; the process is exited.  
>>> ERROR: Unexpected execution error |  Fatal; the process is exited.  
>>> ERROR: Illegal instruction found |  Fatal; the process is exited.  
>>> SYNTAX ERROR AT " " |  Syntax of pattern matching expression is incorrect. Fatal; the process is exited.