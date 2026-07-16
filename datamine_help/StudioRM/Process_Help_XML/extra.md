# EXTRA Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Expressions**.
  * Enter "EXTRA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **EXTRA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_E.md#EXTRA>).

## Process Overview

**EXTRA** is a general purpose EXpression TRAnslator that allows you to _transform_ the contents of files by modifying fields and creating new ones based on the values of existing fields. **EXTRA** also makes it easy to calculate new fields in any file, based on existing fields and values. 

**Tip** : If you're looking for examples of **EXTRA** usage, see [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

Before **EXTRA** starts to process records from the input file, it must define which fields will appear in the output file. It is important to understand that _all_ decisions about fields in the output file are made _before_ any records are processed.

Normally, the fields that appear in the output are:

  * All fields that are in the input file

  * Fields created in the transforms you specify.

See [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

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

## The Expression Translator Screen

As a process, **EXTRA** displays a familiar "files, fields and parameters" type screen to allow an **IN** put and **OUT** put file to be specified (you can also define **[retrieval criteria](<../COMMON/Retrieval_Criteria_Overview.md>)** to filter the records to be processed. EXTRA is unusual as a process in that it triggers the display of another screen, the **[Expression Translator](<../COMMON/Expression%20Translator2.md>)**. This screen is used to determine the actual expression to be applied to the input data records that aren't filtered out by retrieval criteria.

Using the **Expression Translator** , you specify how you want the fields transformed in a simple and natural manner, for example, to create a new field "C" which calculates the average of two fields "A" and "B", you can create the following expression:
    
    
    C = (A + B)/2

Clicking **Execute** in the Expression translator feeds the expression back into the EXTRA process, where the new field is created, and a value for each record is calculated. 

**EXTRA** will continue to accept and compile transformations until you tell it to start processing the file. If you are using **EXTRA** interactively then processing is started by clicking the **Execute** button in the **Expression Translator**. 

Note: If you are recording to a script or a macro then the keyword `go`is inserted automatically after all transformation expressions for you. This isn't strictly necessary, and when creating your own macros, the keyword can be omitted.

See [Expression Translator (EXTRA)](<../COMMON/Expression%20Translator2.md>).

## Expressions and Fields

_Expressions_ can involve _constants_ , _field_ values or _function_ values. These may be either numeric or alphanumeric. If an expression results in a numeric value, it must be assigned to a numeric field. Similarly, alphanumeric expressions must be assigned to alphanumeric fields.

An expression may be assigned to a field that already exists, or a new field may be created. New numeric fields may be created simply by assigning to them. To reinforce the fact that a new numeric field is being created, you may add "**;n** " to the end of the field name. For example:
    
    
    C;n = (A + B)/2

will create a new numeric field called "C" and assign the result of the expression to it. If you are creating a new alphanumeric field, you must append a field specification of the form `a[len]` to the field name, where `[len]` is the maximum number of characters that the field can contain. For example:
    
    
    BHID;a12 = join("BH", string(N, 0))

This creates a new alphanumeric field **BHID** with a maximum of 12 characters ("a12"). 

**Note** : In EXTRA alphanumeric fields are limited to a maximum of 256 characters. 

**EXTRA** can also be used to create implicit fields. See [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

#### Missing Fields

If **EXTRA** tries to use a field that does not exist, it will report an error and stop processing the file. This can be an inconvenience if you want to erase a field and are not sure if it exists.

There are now two ways to deal with this: either using the **@FLDFAIL** parameter or using the **type()** function's return value. See [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

#### Field Name Ambiguity

It is possible for an input file to contain a field name that matches an **EXTRA** function name, and for that function to be used in the transform. Consider the following example:
    
    
    _TMP;a4 = type(BHID)  
  
---  
  
Here, the transform fails because **EXTRA** sees `type` as a field name before it checks if it is a function name.

To avoid this situation, it is necessary to explicitly indicate the presence of a field name using square brackets. For example
    
    
    [type]=0  
  
---  
      
    
    spec1;a4=type("type")  
      
    
    spec2;a4=TYPE("type")  
  
In this case, the transform completes without errors as [type] explicitly declares "type" as a field name and the unbracketed `type`and `TYPE` instances as function names.

## Arithmetic Operations

**EXTRA** allows you to use a set of arithmetic and relational operations on values. There is an inferred precedence of operations:

  * Negation (e.g. **A = -B**)

  * Multiplication and division

  * Addition and subtraction

Therefore, an expression like "`A = B * C + D * E`" first multiplies the values of fields `B` and `C`, then multiplies `D` and `E` together, and adds the two results. You can use brackets where necessary to change the order in which calculations are performed, for example "`A = B * (C + D) * E`". There is no limit to the complexity of the expression that you can use.

Note: extend an expression over as many lines as is necessary. You may insert a line break anywhere, except within a word.

## Character Operations

**EXTRA** offers a range of functions to manipulate alphanumeric (character) fields. The value assigned to a character field must be a character constant, or the result of a character expression, such as
    
    
    concat("RDH", substr(BHID,4,3))

A character constant is a string of characters enclosed in double quotes (e.g. **"RDH034"**). EXTRA does not recognise single quotes as character constant delimiters.

#### Missing, dash or minus?

The character "-" has three meanings within your application and **EXTRA**. In your application, it is used as shorthand for "-infinity", which is the value used to denote missing values of numeric fields. It is a legal character in a field name (such as "NUM-FLDS"), and in EXTRA it is used as a subtraction operator. 

**EXTRA** resolves these ambiguities as follows:

  * Normally, "-" is an arithmetic subtraction operator.

  * If used in a field name, the name must be enclosed in **square brackets** , for example `[NUM-FLDS] = 2`

  * To check for a missing value for a numeric field, compare with the value returned by the **absent()** function (see below).

To create an alphanumeric field, the _field type descriptor_ is required. If you wish to create field of this type containing a minus character, you will need to also include the type descriptor within the quotes, for example:

`'A-1;a4' = "abcd"` is correct, whereas;

`'A-1';a4 = "abcd"` is incorrect, and will generate a syntax error.

Unlike earlier versions of **EXTRA** you can create new fields containing a dash (or any other reserved character) in either of the forms specified below:

`[A-1;a4] = "abcd"`

or;

`[A-1];a4 = "abcd"`

#### Reserved characters

As well as - (minus), the following are reserved characters: + / * = < > ( ). If a field name includes one of these characters it must be enclosed in square brackets. For example: [g/t]. 

Note: The older form for specifying field names containing reserved characters was to enclose the name in single quotes. This form is still allowed but square brackets are the preferred way. 

#### Field or function?

Sometimes, you might want to use or create a field with the same name as one of the built-in functions. For example, your input file might contain a field called "max", and you want to update this by comparing it with another grade field. You need to help EXTRA to tell when `max` is a field name, and when it is a function name. Do this by placing the field name in square brackets, for example:
    
    
    [max] = max([max], grade)

## Relational Operations

In addition to arithmetic operators, **EXTRA** also provides _relational_ operators. These are normally used in evaluating conditions ("if" tests), as described below, but they may be used elsewhere. The relational operators are:
    
    
    ==

|  equal to  
---|---  
      
    
    !=

|  not equal to  
      
    
    <>

| not equal to  
      
    
    <

|  less than  
      
    
    <=

|  less than or equal to  
      
    
    >

|  greater than  
      
    
    >=

|  greater than or equal to  
  
If a relationship is "true", then the relational operator evaluates to 1.0, otherwise if a relationship is "false", the operator evaluates to 0.0. For example, the following creates a new field called **CHECK,** and assigns it the value 1.0 if the value of field **FROM** is greater than or equal to the value of the field **TO** :
    
    
    CHECK = (FROM >= TO)

(It is, in fact, unnecessary to use brackets here, because relational operations have a lower precedence than arithmetic or assignment operations. They appear here to clarify what happens).

#### Combining relational expressions

You can use the keywords "`and`" and "`or`" to combine relational (and other) expressions. For example, you can say
    
    
    CHECK = (FROM >= TO and FROM >= prev(FROM))

This assigns 1.0 to the field `CHECK` if `FROM` is greater than or equal to `TO` and `FROM` is greater than or equal to the same field on the previous record.

## Conditional Execution

EXTRA supports conditional logic using the keywords `if`, `else`, `elseif` and `end`. These let you control which statements are execute based on specific conditions. An example of where this might be used is as follows:
    
    
    ERRORS = 0  
    if (FROM < TO or FROM < prev(FROM))  
      ERRORS = ERRORS + 1  
    end

This fragment begins by initializing a field called `ERRORS` to zero. (If the field does not exist, it is created automatically). **EXTRA** then compares the `FROM` and `TO` fields and the `FROM` field with the value on the previous record. If this is "true", **EXTRA** executes transformations following the `if`, up to a matching `end`. There can, of course, be any number of statements after the `if` test.

The transformations could be extended, for example
    
    
    ERRORS = 0  
    if (FROM < TO or FROM < prev(FROM))  
      ERRORS = ERRORS + 1  
    elseif (GRADE > 20)  
      ERRORS = ERRORS + 1  
    end

Note that for each `if` there must be a matching `end`. There may be as many `elseif`'s as you wish, and one `else` if necessary. 

**Tip** : Use IF-ELSEIF-ELSEIF--ENDIF for checking multiple conditions. Its faster that separate IF-END blocks because EXTRA stops evaluating conditions as soon as any one is true. See EXTRA examples. See [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

**Note** : `elseif` is _one word_. EXTRA will recognise `else if` as the beginning of an `else` followed by a new (nested) `if`. The new `if` must be completed by it's own matching `end`.

`if...end` constructions may be embedded within other `if...end`'s. 

There is no limit to the depth to which you may sink while doing this!

## Logic Constructs

Construct | Description  
---|---  
if (expression)   
statements   
end  |  Evaluate the **expression**. If it is true, execute zero or more **statements** , up to the matching **end**.  In EXTRA, an expression is true if its value is any number except zero. Otherwise, the value of the expression is false.   
if (expression)   
statements1   
else   
statements2   
end  | Evaluate the **expression**. If it is true, execute **statements1** , then continue after the **end**. If the expression is false, execute **statements2**.  
if (expression1)  
statements1  
elseif  
(expression2)  
statements2  
...  
else  
statements3  
end  |  Evaluate **expression1**. If it is true, execute **statements1** , then continue after the matching **end**.  If **expression1** is false, evaluate **expression2** and if it is true, execute the **statements2**. Note: There may be any number of **elseif** statements.  If there is an **else** , execute the statements following it if none of the previous **elseif** expressions is true.   
  
## "Special" Values

The **special(X)** function returns a "special" numeric value, depending on the argument given. The argument must evaluate to a character string.

Argument |  Value returned  
---|---  
"TOP" or "+" |  The Datamine value for +infinity, sometimes referred to as "Top"  
"BOTTOM" or "-" |  The Datamine value for -infinity, sometimes referred to as "Bottom". This is the same value as is used for missing (absent) values for numeric fields.  
"TR" or "DL" |  The Datamine "trace" value (1.0e-30)  
"PI" |  The numeric constant "pi" (3.14159...)  
"E" |  The numeric constant "e" (2.71828...)  
MAXINT | The largest integer value supported by the randbetween function (2,147,483,647)  
MININT | The smallest integer value supported by the randbetween function (-2,147,483,648)  
  
## Using @APPROX

Rounding errors are sometimes introduced by numerical calculations or when legacy single precision files are converted to extended precision. Setting @APPROX=1 specifies that EXTRA will allow for rounding errors when making comparisons between numeric values. 

## Comments

EXTRA statements can be supported by comments, for example:
    
    
    !START M1  
  
---  
      
    
    !EXTRA &IN(MOD2), &OUT(t)  
      
    
    # Comment 1  
      
    
    NEWFLD = 1  
      
    
    # Comment 2  
      
    
    NEWFLD2=9999  
      
    
    # Comment 3  
      
    
    GO  
      
    
    !END  
      
    
       
  
Comments are _not supported within IF loops_. The following statement, for example, will cause EXTRA to fail: 
    
    
    VAL2 = PVALUE*1.5  
  
---  
      
    
    if (VAL2 == 8)  
      
    
    # comment is here  
      
    
    VAL5 = 5  
      
    
    END  
  
## Functions & Procedures

**EXTRA** provides a long list of functions that can be used in transforming fields. A function is identified by its name, followed by a list of zero or more arguments enclosed in brackets. The brackets must be specified, even if the number of values passed to the function is zero. A function always returns a value. This value may be assigned to a field, or it may be used as a term in an expression. 

Examples of **EXTRA** statements using functions are:
    
    
    sx = sqrt(X)  
    c = sqrt(a*a + b*b - 4*a*c*cos(ac))  
    BIGEST = max(G1, (G2+G3)/2, G4, G5)

### Numeric Functions

**EXTRA** provides the following functions which all take numeric values as arguments and return a numeric value. For trigonometrically functions all angles are in degrees.

Function name |  Arguments |  Returns  
---|---|---  
abs |  X |  The absolute (positive) value of X  
absent |  none |  The Datamine "absent data" value.  
acos |  X |  The angle whose cosine is X.  
asin |  X |  The angle whose sine is X.  
atan |  X |  The angle whose tangent is X.  
atan2 | X,Y |  Calculates the angle ( \theta ) between the positive x-axis and the point ((x, y)) in the Cartesian plane.  
azimuth | X,Y | Provides **azimuth(dx, dy)** to return the azimuth in degrees of a line from (0, 0) to (dx, dy).  
cos |  X |  The cosine of X.  
decode | A |  The numeric value of the first set of numeric characters embedded in A.  
default |  X |  The default value of field X. The value returned will be either numeric or alphanumeric, depending on the type of the field passed as the argument. **Note** : `default()` is a function, and it _returns_ the default value of a field; you cannot _set_ the default value of a field using **EXTRA**. In other words, it is incorrect to specify `default(AU) = 10.0#`.  
exp |  X |  The constant "_e_ " raised to the power of X.  
field |  F1 |  The contents of a field. The field name must be supplied as a string - for example, field ("AU"). This allows field names with otherwise prohibited characters, such as '-', to be referenced. This function can only be used for getting the value of a field \- not for setting it.  
ijkget | F1,X | Returns values encoded into the block model index.  
ijknum | I,J,K | Combines separate I, J and K indexes into a single IJK index.  
int |  X |  The integer part of X.  
len |  A |  The length (up to the first trailing space) of A.  
log |  X |  The base-10 logarithm of X.  
loge, logn |  X |  The base-"_e_ " logarithm of X.  
match |  A, P |  The position where a regular expression P matches characters in A.  
max |  X1, X2, X3, ... |  The maximum value of X1, X2, X3, ...  
maxia |  X1, X2, X3, ... |  The maximum value of X1, X2, X3, ... ignoring absent arguments.  
min |  X1, X2, X3, ... |  The minimum value of X1, X2, X3, ... ignoring absent arguments. For example:

  * minia(absent(), 100, 2) = 2
  * min(absent(), 100, 2) = absent)

  
minia |  X1, X2, X3, ... |  The minimum value of X1, X2, X3, ...  
mod, modc |  X, Y |  The remainder when X is divided by Y.  
not | X | Returns 1 if X is zero, otherwise returns 0. Usually used in the expression in an IF or ESEIF statement.  
phi |  X |  The inverse normal distribution function.  
pow, rais |  X, Y |  The value of X raised to the power of Y.  
rand | X | Return a uniformly distributed pseudo-random number between 0.0 and 1.0. For example, 0.0155, 0.9433 and so on.  
randbetween | X,Y | Return an integer value chosen at random between X and Y inclusive. For example, if X = 0 and Y = 1, 5 calculations could be 1, 0, 1, 1, 0  
round |  X, Y |  Round off the value X to the nearest multiple of Y. Equivalent to Y*int(X/Y \+ 0.5).  
rownum |  | Add a row number field to a file.  
sin |  X |  The sine of X.  
special |  X |  One of your application's "special" values (see below).  
sqrt |  X |  The square root of X.  
tan |  X |  The tangent of X.  
xyzijk | X,Y,Z | Creates an IJK index number from X, Y and Z model coordinates.   
  
#### Scientific Notation

EXTRA will interpret numbers like "1.23e-4" as being "1.23 times 10 to the power of -4" = 0.000123. As such "e" can be used to define an exponent of a numeric value.

### String Functions

The following functions are provided for the manipulation of alphanumeric fields:

Function name |  Arguments |  Returns  
---|---|---  
concat | A1, A2... | Join two strings, trimming leading and trailing spaces off of each argument before concatenating them. Any number of arguments are accepted.  
default |  X |  The default value of field X. The value returned will be either numeric or alphanumeric, depending on the type of the field passed as the argument. **Note** : `default()` is a function, and it _returns_ the default value of a field; you cannot _set_ the default value of a field using **EXTRA**. In other words, it is incorrect to specify `default(LITH) = "Basalt"#`.  
field |  F1 |  The contents of a field. The field name must be supplied as a string - for example, field ("AU"). This allows field names with otherwise prohibited characters, such as '-', to be referenced. This function can only be used for getting the value of a field \- not for setting it.  
join |  A1, A2, A3, ... |  The concatenation of the alphanumeric values A1, A2, A3, ... Note: Unlike `concat`, the values are not trimmed automatically.  
lcase |  A |  Returns the string given as an argument, with all upper case letters converted to lower case  
string |  N, M |  The numeric value N, converted to a string with M decimals. If M is omitted, the function uses a general-purpose numeric format.  
substr |  A, N, M |  Returns a sub-string, consisting of M characters taken from A, starting with character N. If M is omitted, all characters from N to the end are returned. If N is negative, the first character is found by counting backwards from the end of A. If M is negative or zero, the result is an empty string.  
trim |  A |  Returns the value of A with trailing spaces removed  
type | F1 |  Returns a string of characters that describe the type of the field.  **Note** : the argument passed to type is a text string and therefore you must enclose it in double-quotes. If you just pass the field name (i.e. "type(B)" ), **EXTRA** may report that the field does not exist and stop. **Tip** : If a field does not exist, **type()** returns an empty string (""). This can be useful to avoid "missing fields" errors.  
ucase |  A |  Returns the string given as an argument, with all lower case letters converted to upper case  
  
#### Notes for string functions

  1. The `match()` function uses character patterns known as "regular expressions". A regular expression consists of a sequence of literal characters to be matched, or one or more of the following elements:

    
    
    %

|  Matches the beginning of the field value  
---|---  
      
    
    $

|  Matches the end of the field value  
      
    
    *

|  Zero or more occurrences of the preceding pattern element  
      
    
    ?

|  Any single character  
      
    
    [...]

|  Any one of the characters enclosed in the square brackets. The shorthand notation "**a-z** " means any lowercase letter.  
      
    
    [^...]

|  Any character except one of these  
  
> The special meaning of a character (e.g. "***** ") is lost if the character is preceded by "**\** ", hence to match a literal "***** ", use "**\\*** ".

  2. Be careful when you use the `trim()` function to create a new character field. Character fields in a Datamine file are _always_ padded out to the declared length with spaces. For example, consider the command:
         
         STRING1;A12 = trim("   ABC   ")

> In this case, the `trim()` function removes both the leading and trailing blanks, but assigning the result to the `STRING1 `field will add 9 trailing spaces to the stored value ("ABC "). 

### Procedures

A "procedure", unlike a function, does not return any value. It just carries out some action. EXTRA provides three procedures:

Procedure |  Arguments |  Description  
---|---|---  
delete |  none |  Deletes the current record  
erase |  F1, F2, F3, ... |  Erases the fields F1, F2, F3, ... from the output file  
exit | none |  Immediately terminates processing before the current record has been written.  
saveonly |  F1, F2, F3, ... |  Erases all fields except F1, F2, F3, ... from the output file. If used more than once, only the values in the last **saveonly** are honoured.  
**keep** | F1, F2, F3, ... | Define the fields that will be in the output file. It is like `saveonly()` (see above), but the field lists are cumulative.   
  
### Record Selection Functions

The following functions may be used to select field values from adjacent records. The functions return a numeric or alphanumeric value, depending on the type of the field supplied as an argument. All values passed to these functions must be the names of fields.

The following functions may be used to test whether a record is the first or last in a file.

Function name |  Arguments |  Returns  
---|---|---  
first |  none |  If processing the first record, returns 1.0, otherwise returns 0.0  
last |  none |  If processing the last record, returns 1.0, otherwise returns 0.0  
  
In all cases with these functions, "first" and "last" mean "the first (or last) record that matches current retrieval conditions".

The `first()` and `last()` functions are normally used within conditional tests, e.g.
    
    
    if (first())  
      sumX = X  
    else  
      sumX = sumX + prev(X)  
    end

Function name |  Arguments |  Returns  
---|---|---  
prev |  X |  The value of field X from the previous record  
next |  X |  The value of field X from the next record  
  
If processing the first record, `prev(X)` returns a "missing value" (i.e. the same value as `absent()`). Similarly, when processing the last record (i.e. the last record that matches current retrieval criteria), `next(X)` returns a missing value.

Do not use the `prev` function if the previous record has been deleted using delete procedure as the result will be undetermined.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
APPROX |  Allow for rounding errors when making comparisons 0 = Exact comparisons 1 = Approximate comparisons |  No |  0 |  0, 1 |  0, 1  
SEED | Seed number for pseudo-random number sequence | No | Undefined | Undefined | Undefined  
FLDFAIL |  Controls if missing fields cause an error or not.  0 = Missing fields do not cause an error. 1 = Missing fields cause an error.  | No | 1 |  0, 1 |  0, 1  
PRINT |  Display output to command processor 0 = do nothing 1 = show all code in the output window during processing. |  No |  0 |  0, 1 |  0, 1  
  
## EXTRA Examples

See [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> Fatal error: No room to create new field: A257  |  Not enough room left in file to add field |  Remove unnecessary fields or consider activating .dmx file support.  
  
Related topics and activities

  * [Expression Translator](<../COMMON/Expression%20Translator2.md>)

  * [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>)

  * [Attribute Naming Convention](<../COMMON/Attribute_Naming_Convention.md>)

  * [MGSORT](<mgsort.md>)

  * [SORTX](<sortx.md>)