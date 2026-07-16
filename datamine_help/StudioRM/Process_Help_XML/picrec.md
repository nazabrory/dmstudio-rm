# PICREC Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Filter Copy**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ACCMLT** and click **Run**.
  * Enter "ACCMLT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PICREC>).

## Process Overview

Writes records to an output file if the records in the input file match the given input expressions.

### Expression Syntax

An expression may be either a relational expression or a pattern matching expression.

In the following text all keywords are capitalized. When running **PICREC** , any keyword may be entered in either uppercase or lowercase and abbreviated to its first three (or more) characters.

Relational Expressions

The syntax of a relational expression is:

|  [FIELD] |  <fieldname> |  <operator> |  [CONSTANT] |  <value>  
---|---|---|---|---|---  
or |  [FIELD] |  <fieldname> |  <operator> |  [FIELD] |  <fieldname>  
or |  [CONSTANT] |  <value> |  <operator> |  [FIELD] |  <fieldname>  
  
The keywords **FIELD** and **CONSTANT** are optional, and need only be specified where necessary to avoid confusion (e.g. "ROCKTYPE=FIELD T2" or ROCKTYPE=CONSTANT T2").

Any of the six relational operators listed below may be used.

> |  Greater than  
---|---  
>= |  Greater than or equal to  
= |  Equal to  
< |  Less than  
<= |  Less than or equal to  
<> |  Not equal to  
  
### Pattern Matching

The syntax of a pattern matching expression is:

<fieldname> MATCHES [REGEXP] <pattern>

If the keyword **REGEXP** is missing, a "pattern" may consist of literal characters to be matched, or one of the following elements.

? |  Any single character  
---|---  
* |  Wildcard. A group of zero or more characters  
[...] |  Any one of the characters enclosed in the square brackets. The short hand notation "a-z" means any lowercase letter; refer to the examples below for more details.  
[^...] |  Any character except one of these  
  
The special meaning of a character (e.g. "*") is lost if the character is preceded by "\", hence the match a literal "*", use "\\*". Quotes (double or single) may be used to enclose patterns if desired.

If the keyword "REGEXP" is used, the pattern specifies a full regular expression. Regular expressions allow advanced users to make more complex selections than are possible by using the pattern elements specified above.

A regular expression in **PICDIR** may contain the following elements.

% |  Matches the beginning of the file or field name  
---|---  
$ |  Matches the end of the file or field name  
* |  Zero or more occurrences of the preceding pattern element.  
? |  As above  
[...] |  As above  
[^...] |  As above  
  
### Concatenation of Expressions

The result of a pattern matching expression is either TRUE or FALSE. Any result may be inverted by preceding the expression by the keyword "NOT" (e.g. "NOT BHID MATCHES RHD*"). Two expressions may be joined together by "AND" or "OR" operators. The result is another expression. The "AND" operator has higher precedence than "OR". Parentheses (brackets) may be used to override the normal order of evaluation of expressions.

### Disambiguating Values 

Some text strings are interpreted by **PICREC** as being a keyword or operator. For example, "CON" is used to represent a "CONSTANT" keyword. This can cause problems if the same string is detected within variable values. For example, `STRAT="CONCHA"` will generate a parser error as a constant keyword ("CON") is detected but cannot be processed using the following data.

In this situation, you can disambiguate values by prefixing them with a forward slash. Following the above, example, you could use the expression ` STRAT="/CONCHA"` (or even `STRAT=/CONCHA` as the value contains no spaces).

A prefix backslash (prefix the field value with \\) allows for filtering of reserved words (such as "FIL"). Including a prefix \ before a non-reserved word works the same as without the prefix, for example:
    
    
    STRAT = \REGOLITH end  
  
---  
      
    
    \FILTER = 1 end  
      
    
    \FILL = 1 end  
  
As such, this will NOT work:
    
    
    !PICREC   &IN(TestModel),&OUT(picrec_FIL),@APPEND=0.0  
  
---  
      
    
    FIL=1 end  
  
But this will work:
    
    
    !PICREC   &IN(modgrd_test),&OUT(picrec_FIL),@APPEND=0.0  
  
---  
      
    
    \FIL=1 end  
  
Placing "\" before a fieldname avoids the fieldname being interpreted as an OPERATOR or a KEYWORD. This is useful when fieldnames or other text elements start (i.e. the first two or three characters, depending the operator or keyword) with letters matching OPERATOR or KEYWORD names, this includes for example:

  * MAT (MATCHES)

  * REG (REGEXP)

  * AND

  * OR

  * NOT

  * FIE (FIELD)

  * CON (CONSTANT)

This can be demonstrated by means the following example. Here, the test using the following syntax will fail with an error, as the first three letters of the fieldname i.e. 'MAT' are interpreted as the keyword MATCHES:
    
    
    TEST> FIELD MATGC="LSO" END

When written as follows, it works as expected:
    
    
    TEST> FIELD \MATGC="LSO" END

This principle isn't restricted to field names, but applies equally to text within instructions. For example, the following instruction will fail to complete:
    
    
    TEST> 
     DEVFILE MATCHES reg* END

This is because reg is interpreted as regexp. 

The following statement completes successfully, however, as the "\" escape character ensures the following text is interpreted literally:

TEST> DEVFILE MATCHES \reg* END

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  The name of the file from which records are to be selected. |  Input |  Yes |  Table  
FIELDLST |  Optional file to specify fields to output. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  The name of the file to which selected records are to be written.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  The name of the first field to be transferred from the input file to the output file. If no fields are explicitly named, all fields are copied. You may only apply relational and pattern matching tests to fields that are to appear in the output file. |  IN |  No |  Any |  Undefined  
F2 |  Second field to be copied. |  IN |  No |  Any |  Undefined  
F3 |  Third field to be copied. |  IN |  No |  Any |  Undefined  
F4 |  Fourth field to be copied. |  IN |  No |  Any |  Undefined  
F5 |  Fifth field to be copied. |  IN |  No |  Any |  Undefined  
FIELDNAM |  Field in FIELDLST that holds the names of the data fields to output in OUT. |  FIELDLST |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
APPEND |  If set to 1 then selected records will be appended to the OUT file, provided it exists and has the same fields as the input file (0). |  No |  0 |  0,1 | 0,1  
  
* * *

* * *

## Example

Select records from a file where BHID values start with the letters "RDH", or the field XCOLLAR is between 10200 and 11200:
    
    
    TEST>BHID MATCHES "RDH*" OR          
  
---  
      
    
    TEST>XCOLLAR>=10200 AND XCOLLAR<=11200          
      
    
    TEST>END  
  
Select records where the contents of field "Au1" is greater than the contents of field "Au2":
    
    
    TEST>Au1 > Au2 END  
  
---  
  
Select records where the field LOG contains both codes "Cu" and "Pb":
    
    
    TEST>LOG MATCHES *[cC][uU]*[pP][bB]* OR          
  
---  
      
    
    TEST>LOG MATCHES *[pP][bB]*[cC][uU]* END  
  
Note: "[cC][uU]" will match "cu", "cU", "Cu" or "CU".

Select records where CODE is five characters long, but does NOT end in 3 or 4:
    
    
    TEST>CODE MATCHES ????[^34] END  
  
---  
  
Note: This would do the same thing: `TEST>CODE MATCHES ????? AND NOT CODE MATCHES *[34] END`

Select all records where ROCKCODE = 7, and BHID is DDH034, DDH147 or DDH136:
    
    
    TEST>ROCKCODE=7 AND (BHID=DDH034 OR          
  
---  
      
    
    TEST>BHID=DDH147 OR BHID=DDH136) END  
  
Select all records where BHID values begin with zero or more spaces, followed by "RDH":
    
    
    TEST>BHID MATCHES REGEXP "% *RDH" END  
  
---  
  
A full regular expression is required to match possible leading spaces. Note also how quotes are required, since the pattern contains a space.

## Error and Warning Messages

Message |  Description  
---|---  
>>> ERROR: Read error from file ffffffff |  Read error from file specified as &IN. Fatal; the process is exited.  
>>> ERROR: field aaaaaaaa is too long |  Fatal; the process is exited.  
>>> WARNING: Cannot append to file ffffffff. A new file will be created |  Cannot append fieldnames to the file specified as &OUT. Check the file name given. A new &OUT file will be created.  
>>> ERROR: Files have different DDs, cannot append |  File specified in pattern matching expression and the file specified as &OUT have different DDs. Fatal; the process is exited.  
>>> ERROR: Unexpected execution error |  Fatal; the process is exited.  
>>> ERROR: Illegal instruction found |  Fatal; the process is exited.  
>>> SYNTAX ERROR AT " " |  Syntax of pattern matching expression is incorrect. Fatal; the process is exited. Check that filenames do not start with two or three letters that could be interpreted as keywords (see help above).  
>>> ERROR: Incompatible types for " " and " " |  Field types are incompatible in relational expression. Fatal; the process is exited.  
>>> ERROR: " " MATCHES ... Alphanumeric field required |  Alphanumeric field required for pattern matching expression. Fatal; the process is exited.  
>>> ERROR: Illegal pattern: |  Illegal pattern in pattern matching expression. Fatal; the process is exited.  
>>> ERROR: More than nnnnn instructions |  Maximum number of expressions is 100. Fatal; the process is exited.