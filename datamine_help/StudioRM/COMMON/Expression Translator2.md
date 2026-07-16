# Expression Translator (EXTRA)

To access this screen:

  * Run the **[EXTRA](<../Process_Help_XML/extra.md>)** process from the command line by typing 'extra'. Specify an input file, output file and (optionally) retrieval criteria and click OK \- the Expression Translator displays.

For more information on the **EXTRA** process, see [EXTRA](<../Process_Help_XML/extra.md>).

## EXTRA Key Concepts

##### Transform

**EXTRA** applies a transform to the contents of a file. It does this through one or more statements.

##### Statements

A transform consists of multiple statements. Statements are separated by spaces or new-lines. There are three kinds of statements

##### Assignment statements

Assignment statements evaluate an expression and assign the result to a field.

##### IF statements

If statements use the value of one or more expressions to execute other statements conditionally.

##### Procedure statements

Procedure statements do something but do not return a value. Some procedures (erase, keep, saveonly) require a list of field names (not expressions). The other procedures (delete, exit) dont require any other information.

##### Expressions

Expressions are used in assignment and If statements. There are 4 types.

##### Simple expressions

A simple expression is a number, text string or field reference.

##### Arithmetic expressions

The value of an arithmetic expression is the result of applying the arithmetic operator (+, -, * or /) to the expressions on the left and right of the operator.

##### Relational expressions

The value of a relational expression, like X < 2, is 1.0 if the expression is true and 0.0 if it is false. They may be used anywhere an arithmetic expression may be used.

##### Function expressions

A function expression takes zero or more expressions in brackets to calculate a new value. For example, the value of min(X, 2) is the smaller of the values of the two expressions X and 2.

## Entering Expressions 

Logical expressions can be entered using either (or both) of the following methods:

  * Type the expression you want directly into the **Expression** field.

  * Construct an expression by selecting various parameter components, such as field names, operations, functions and procedures.

For examples and further guidance on using expressions in Studio products, see .

To define a logical expression for the EXTRA process:

  1. Enter all or part of a logical expression into the **Transform** field.

  2. To add preformatted text to the current cursor position (in the **Transform** field):

     * Add one or more **Input Fields** to the transform using the list provided. The fields are derived from the **IN** file of the **EXTRA** process.

     * Add one of the **Operators** to the expression using the buttons provided:

== |  equal to  
---|---  
!= |  not equal to  
< |  less than  
<= |  less than or equal to  
> |  greater than  
>= |  greater than or equal to  
  3. Choose one of the **Functions and Procedures** , categorized into Numeric Functions, String Functions, **Logic Constructs** , Procedures and Record Selection functions:

     * **Numeric Functions** are used to perform mathematical functions on explicit or data-stored values, including:

Function name |  Arguments |  Returns  
---|---|---  
abs |  X |  The absolute (positive) value of X  
absent |  none |  The Datamine "absent data" value  
acos |  X |  The angle whose cosine is X  
asin |  X |  The angle whose sine is X  
atan |  X |  The angle whose tangent is X  
atan2 |  X |  A two-argument arctangent function. It calculates the angle ( \theta ) between the positive x-axis and the point ((x, y)) in the Cartesian plane. This angle is measured in radians and ranges from (-\pi) to (\pi) 12. See [EXTRA examples](<Expression%20Translator%20Examples.md>).  
azimuth |  X |  The azimuth in degrees of a line from (0, 0) to (dx, dy). See [EXTRA examples](<Expression%20Translator%20Examples.md>).  
cos |  X |  The cosine of X  
decode |  X |  The numeric value of the first set of numeric characters embedded in X  
default | X | The default value of X  
exp |  X |  The constant "_e_ " raised to the power of X  
ijkget |  X,X |  Returns values encoded into the block model index. See [EXTRA examples](<Expression%20Translator%20Examples.md>).  
ijknum | I,J,K | Combines separate I, J and K indexes into a single IJK index  
int |  X |  The integer part of X  
len |  A |  The length (up to the first trailing space) of A  
log |  X |  The base-10 logarithm of X  
loge, logn |  X |  The base-"_e_ " logarithm of X  
match |  A, P |  The position where a regular expression P matches characters in A  
max |  X1, X2, X3, ... |  The maximum value of X1, X2, X3, ...  
maxia |  X1, X2, X3, ... |  The maximum value of X1, X2, X3, ... ignoring absent arguments.  
min |  X1, X2, X3, ... |  The minimum value of X1, X2, X3, ... ignoring absent arguments. For example:
       * minia(absent(), 100, 2) = 2
       * min(absent(), 100, 2) = absent)  
minia |  X1, X2, X3, ... |  The minimum value of X1, X2, X3, ...  
mod, modc |  X, Y |  The remainder when X is divided by Y  
phi |  X |  The inverse normal distribution function  
pow, rais |  X, Y |  The value of X raised to the power of Y  
round |  X, Y |  Round off the value X to the nearest multiple of Y. Equivalent to Y*int(X/Y \+ 0.5)  
sin |  X |  The sine of X  
special |  X |  One of your application's "special" values.  
sqrt |  X |  The square root of X  
tan |  X |  The tangent of X  
xyzijk |  X,X,X |  Creates an IJK index number from X, Y and Z model coordinates. See [EXTRA examples](<Expression%20Translator%20Examples.md>)  
     * **String Functions** can be applied to alphanumeric values, including:

Function name |  Arguments |  Returns  
---|---|---  
concat | A1,A2 |  The concatenation of the alphanumeric values A1, A2.  
default | X | The default value of X  
field |  F1 |  The contents of a field. The field name must be supplied as a string - for example, field ("AU"). This allows field names with otherwise prohibited characters, such as '-', to be referenced. This function can only be used for getting the value of a field \- not for setting it.  
join |  A1, A2, A3, ... |  The concatenation of the alphanumeric values A1, A2, A3, ...  
lcase |  A |  Returns the string given as an argument, with all upper case letters converted to lower case  
string |  N, M |  The numeric value N, converted to a string with M decimals. If M is omitted, the function uses a general-purpose numeric format.  
substr |  A, N, M |  Returns a sub-string, consisting of M characters taken from A, starting with character N. If M is omitted, all characters from N to the end are returned.  
trim |  A |  Returns the value of A with trailing spaces removed  
type |  A | Returns a string of characters that describe the type of the field. See [EXTRA examples](<Expression%20Translator%20Examples.md>)  
ucase |  A |  Returns the string given as an argument, with all lower case letters converted to upper case  
     * **Procedures** unlike functions, don't return a value. They just carry out an action. EXTRA provides the following procedures:

Procedure |  Arguments |  Description  
---|---|---  
delete |  none |  Deletes the current record  
erase |  F1, F2, F3, ... |  Erases the fields F1, F2, F3, ... from the output file  
exit |  none |  Immediately terminate processing before the current record has been written. See [EXTRA examples](<Expression%20Translator%20Examples.md>).  
keep |  F1, F2, F3, ... |  Define the fields that will be in the output file. See [EXTRA examples](<Expression%20Translator%20Examples.md>).  
saveonly |  F1, F2, F3, ... |  Erases all fields except F1, F2, F3, ... from the output file. If used more than once, only the values in the last saveonly are honoured. See [EXTRA examples](<Expression%20Translator%20Examples.md>).  
     * **Logic Constructs** create conditional statements using the following options:

Procedure |  Arguments |  Description  
---|---|---  
if() end |  Condition |  If the condition filter passes, functions before the next `end` are performed, if possible.  
if() else end |  Condition |  If the condition filter passes, functions before the next `else` are performed, otherwise the instructions between else and end are performed.  
if() elseif end | Condition |  Similar to `if() else` but evaluate against multiple conditions. IF-ELSEIF-END type statements are efficient as EXTRA only needs to evaluate the condition once (as opposed to multiple times if multiple IF-END statements are used). For example:
           
           IF(SLPCODE==0)
           
           SLOPE=0
           
           ELSEIF(SLPCODE==1)
           
           SLOPE=50
           
           ELSEIF(SLPCODE==99)
           
           SLOPE=33
           
           END  
  
if() elseif else end | Condition | An extension of `if() elseif` end. If data does not match any previous `elseif `condition, the logic after else (and before end) is executed if possible.  
not() |  Condition |  Used typically as part of an if() type statement to exclude passing conditions. For example:
           
           IF(SLPCODE==0)NOT(SLPCODE==999)
           
           SLOPE=1000
           
           END

If the argument is zero, it returns 1.0, otherwise it returns 0.0. So, to invert the statement
           
           if (X > 1 and Y < 0) ...

You could use:
           
           if (X <= 1 or Y >= 0) ...

...or simply:
           
           if (not( X > 1 and Y < 0) ) ...  
  
  
For all of the above, see [EXTRA examples](<Expression%20Translator%20Examples.md>).
     * Record Selection functions allow you to navigate throughout the specified **IN** database. They include:

Function name |  Arguments |  Returns  
---|---|---  
first |  none |  If processing the first record, returns 1.0, otherwise returns 0.0  
last |  none |  If processing the last record, returns 1.0, otherwise returns 0.0  
prev |  X |  The value of field X from the previous record  
next |  X |  The value of field X from the next record  
  4. Click the respective **Add** button to transfer preformatted text to the **Expression** field.

  5. **Test** the validity of your expression. You are told if the expression is valid ("OK") or not. 

If a syntax error occurs, the **Status** field indicates which line is problematic.

**Note** : to restart your expression, use **Clear**. You can't undo this.

  6. Execute your expression using the **EXTRA** process. 

Related topics and activities

  * [EXTRA](<../Process_Help_XML/extra.md>) (process)

  * [EXTRA examples](<Expression%20Translator%20Examples.md>)