# Logical Expressions

Logical expressions (commonly referred to as 'filter expressions) are used throughout your application to specify rules of varying complexity that will determine, generally, how data within a file is to be managed (normally, filtered) during import or display.

Filtering uses logical comparisons for which the answer may be TRUE (1) or FALSE (0). If the item of data being tested is TRUE to the selection criteria then it will be accepted, but if it is FALSE, it will be rejected. Filter arguments may be applied to the selection of records from files or to the selection of data by attributes in the Design window.

An expression may be a relational expression or a pattern matching expression.

## Relational Expressions

A relational expression compares the value of something with another value in a specific way. The syntax for a relational expression must be one of the following: 
    
    
    <fieldname> <operator> < value>
    
    
    <value> <operator> <fieldname>

The following operators may be used:

Element |  Meaning  
---|---  
=, == |  Equal to  
> |  Greater than  
< |  Less than  
>= |  Greater than or equal to  
<= |  Less than or equal to  
<>, ! |  Not equal to  
  
The following examples assume that the data set has a column called "Au" containing numeric values for gold assays:

  * The expression: `Au >= 2.35` will select all the records for which the `Au` value is greater than or equal to 2.35. In the context of legends, a particular appearance may be defined and assigned for the display of the data satisfying the condition.

  * The following expression will result in the selection of all records for which the borehole ID (BHID) has the value "`RC056`". String data should always be in double quotation marks:
        
        BHID = "RC056

## Pattern Matching

Pattern matching involves the comparison of one value with another, as above, but uses a pattern and permits this comparison using less rigid rules. The syntax for a pattern matching expression is:
    
    
    < fieldname > MATCHES < pattern >
    
    
    < fieldname > REGEXP < pattern >

A "pattern" may consist of a set of characters to be matched exactly such as a specific BHID value, or it may be a mixture of text characters and one or more of the following elements:

Wildcard| Meaning in MATCHES| Meaning in REGEXP  
---|---|---  
?| Any single character| Any single character.  
+| n/a| Matches the preceding pattern element one or more times.  
*| Matches the preceding pattern element one or more times.| Matches the preceding pattern element zero or more times.  
  
For example, the following expression is TRUE for data where the first 4 characters of the BHID field are "DH28":
    
    
    BHID MATCHES "DH28*"

## Wildcards in the MATCHES and REGEXP Statements

Wildcards have slightly different, but important differences when used in the MATCHES and REGEXPR statements. In the following example, retrieving a subset of drillholes using a wildcard would yield different results:

  * The original list of drillholes: VB2675, VB2737, VB2812, VB2813, VB283, VB4272

  * The expression `BHID REGEXPR "VB28*"` results in the following subset: VB2675, VB2737, VB2812, VB2813 & VB2832. Here, all drillholes with a BHID starting with 'VB2' are retrieved.

  * Using `BHID MATCHES "VB28*"` and `BHID REGEXPR "VB28+"` results in the following subset: VB2812, VB2813 & VB2832. Here, all drillholes with a BHID starting with 'VB28' are retrieved.

## Using More Than One Expression

Multiple expressions can be joined (concatenated) using the operators "AND", "OR" and "NOT" (also described as "!")

  * Two or more expressions may be concatenated by using the "AND" or "OR" operators.

  * The "NOT" operator inverts the meaning of the expression. 

For example, if you wished to use the earlier example of matching the first four characters of the BHID field, but wanted to exclude any results that related to a drillhole segment that were shorter than 200 meters in length, you would use the following expression: `BHID MATCHES "DH28*" AND LENGTH < 200`

When using the AND and OR operators, it is useful to remember the following statements:

  * When using AND, only results that match ALL of the statements that are conjoined will be permitted. If results match either of the expressions, but not all, then they will not be permitted.

  * When using OR, any result that matches any of the statements made will be permitted.

  * When using a combination of AND and OR statements, think of the AND as an argument separator. Any conditions on either side of the AND, if conjoined by OR statements, will be thought of as a single condition.

It is important to remember that the descriptions 'BHID' and 'LENGTH' are both column names in the file being analyzed (filtered).

**Tip** : if you are familiar with regular expressions, you can use this format of data matching, using the REGEXP opening statement instead of MATCHES. Alternatively, use the Regular Expression button in the Expression Builder dialog.

## Operator Precedence

The operators have an order of precedence which is adhered to when a filter expression is evaluated. The operators are listed below in their order of precedence, from highest to lowest:

  1. ( ), !, NOT

  2. <, <=, =, >, >=, <>

  3. AND

  4. OR

In an expression using more than one operator, the precedence determines the order in which the operations should be performed.

For more information on building filter expressions, please refer to your Expression Wizard online Help (this can be accessed by pressing <F1> whilst in the Expression builder dialog).

#### Ambiguity Resolution

Some expressions can be ambiguous, for instance:
    
    
    My Field = ABC

In this case is difficult for the parser to know with string refers to the Field Name and which refers to the Value. Therefore, the parser has a default behaviour to deal with this ambiguity and also extra commands to override it:

  * Default Behaviour: Treat the Left Hand Side as the Field Name and the Right Hand Side as the Value

  * Override behaviour: Precede a string with the literal expression "FIELD" to treat it as a Field Name, or "CONST" to treat it as Value. Only one side can have the "FIELD" or "CONST" literal (comparisons between two Fields Names or Values are not accepted). For example, the expression:
        
        	CONST "My Field" = FIELD "ABC"

is the reverse of the initial example, treating "My Field" as the value to be applied to a field named "ABC".

## Filter Expressions and Scripting

You can emulate the effect of multiple line filter expressions in scripts by joining expression parameters with "AND". For example, the following scripted command:
    
    
    oDmApp.parseCommand(filter-drillholes AU > 0.5 AND M4DDESC =2 );

Represents the following expression filter:
    
    
    AU > 0.5 AND M4DDESC = 2

Note: The third parameter (empty single quotes) is used to indicate that no further expressions are specified.

Related topics and activities

  * [Expression Translator (EXTRA)](<Expression%20Translator2.md>)

  * [Expression Builder](<Expression%20Builder%20Dialog.md>)