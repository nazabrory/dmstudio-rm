# IF Macro Command

Evaluates one or more logical expressions involving substitution variables and constants in a macro or menu.

There are two categories of IF command, namely:

  1. SIMPLE

  2. BLOCKED

### Simple IF command

General Format:
    
    
    !IF <CONDITION>, ... ,GOTO XXXX   
  
---  
      
    
    !IF <CONDITION>, ... ,GOSUB XXXX  
      
    
    !IF <CONDITION>, ... ,LET <EXPR>  
  
Where:

  * `XXXX `is a 16 character label in the macro or menu.

  * `<EXPR>` is any valid expression recognized by the LET command.

A series of comma separated conditions may be supplied. If all conditions evaluate to "true", an attached [GOTO](<goto.md>), [GOSUB](<gosub.md>) or [LET](<let.md>) statement is executed.

`<CONDITION>` can be one of either : `<VAR1> <OP> <VAR2>` or : `<LVAR>`.

Where:

  * `<VAR1>` is a substitution variable

  * `<VAR2>` is a substitution variable or a constant.

  * `<OP>` is one of the following operators:

    * `<` less than.

    * `<=` less than or equal to.

    * `=` equal to.

    * `>=` greater than or equal to.

    * `>` greater than.

    * `<>` not equal to.

  * `<LVAR>` is a "logical" variable. The expression is "false" if `<LVAR>` = 0 or 0.0, and "true" for all other values. Note : All alphanumeric values evaluate as "true".

If `<VAR1>` and `<VAR2>` are numeric they are compared as numbers. Otherwise they are compared character by character using the collating sequence. Variables and values may be enclosed in single quotes ' to preserve spaces.

Note: Substitution variables must be defined for comparison, as a macro error results if comparison is attempted on undefined variables.

### Blocked IF command

General Format:
    
    
    !IF <CONDITION>, ... ,THEN statement(s)  
  
---  
      
    
    !ELSEIF <CONDITION>, ...,THEN statement(s)  
      
    
    !ELSEIF <CONDITION>, ...,THEN statement(s)  
      
    
    !ELSE statement(s)  
      
    
    !ENDIF  
  
The "blocked" IF statement is an extension of the simple IF statement. Each `<CONDITION>` line is evaluated in turn. The block of statements associated with the FIRST `<CONDITION>` line to evaluate "true" is executed. Once this block is finished, control passes to the first statement after the `!ENDIF`.

`<CONDITION>`s are specified in the same way as for "simple" IF statements.

Zero or more `!ELSEIF ...,THEN` branches may be supplied.

An optional `!ELSE` branch may be supplied. This is executed only when all preceding branches fail.

`!ENDIF` must be supplied to terminate the "block".

IF blocks may be nested.

It is legal to **GOSUB** from within a branch. The branch will be "pending", and control will resume with the `!RETURN`.

It is illegal to **GOSUB** or **GOTO** a label contained within an IF statement block either from outside the whole IF block, or to a label within a different or deeper branch of the whole block.

Because testing is abandoned if any individual test fails, syntax errors further to the right in the line (such as an illegal label) will not be picked up unless all tests pass.

During character tests, blanks will be stripped out from the `<val1>` string unless it is enclosed in quotes. This is true even if `<val1>` is a second substitution variable. 

Tip: If in doubt, enclose `<val1>` in quotes.

## Examples

GOTO the label "END" if variable $1 contains the numeric value '3' (for example, 3, 3.0 and so on) AND if variable $2 is NOT set to the string "Xyz Project". Capitals are significant for string comparison:
    
    
    !IF  $1 = 3, $2 <> 'Xyz Project', GOTO END  
  
---  
  
Check the variable "$value#" and initialize it to the string "New Value" if it has not already been defined (note the use of single quotes):
    
    
    !LET  $test#=$value#  
  
---  
      
    
    !IF  $test#='$value' '#', LET $value#='New Value'   
  
This example will delete file DRILL.M if it exists. A message is also displayed:
    
    
    !FILE   $exists#=DRILL.M,$recs#=recs  
  
---  
      
    
    !IF  $exists#, THEN  
      
    
    !DELETE  &IN(DRILL.M)  
      
    
    !ECHO   file DRILL.M deleted.  
      
    
    !ENDIF  
  
Classify a plot as either A4, A3 or A0 depending on the plot dimensions $min#, $max#. Indentation may be used to make the branching clearer:
    
    
    !IF  $min#>0, $min#<=210, $max#<=297,   
  
---  
      
    
    THEN         
      
    
    !LET  $media#='A4'  
      
    
    !ELSEIF  $min#<=297, $max#<=420,   
      
    
    THEN         
      
    
    !LET  $media#='A3'  
      
    
    !ELSEIF  $min#<=841, $max#<=1189,   
      
    
    THEN         
      
    
    !LET  $media#='A0'  
      
    
    !ELSE         
      
    
    !LET  $media#='Plot size error.'  
      
    
    !ENDIF   
  
  * [ELSE Macro Command](<else.md>)

  * [ELSEIF Macro Command](<elseif.md>)

  * [ENDIF Macro Command](<endif.md>)