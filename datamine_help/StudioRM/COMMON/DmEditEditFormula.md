# Edit Formula

The Edit Formula screen lets you create, edit and test a formula for generating the values in a specific column (field) of a table.

Dialog Item | Purpose  
---|---  
Formula: |  Displays the current state of the formula, which can be edited.  
Columns: |  Lists all columns in the table. Used to select columns containing values that may be used in the construction of the formula. Select by double-clicking.  
Operators |  Lists the permissible (supported) mathematical operators that may be used in the formula. Select by clicking.  
Functions |  Lists the defined mathematical functions that may be used in the formula. Select by double-clicking.  
Constants |  Lists the defined constants. Select by double-clicking.  
  
  
**Note** : Formulae are not saved to the table - only the values are saved. Formulae only exist until they have been run, and the cells contain values.

### Operators, Functions and Constants

#### Defined Operators

Operator |  Example Usage (Syntax) |  Description  
---|---|---  
+ |  x + y |  Addition operator  
- |  x - y |  Minus operator  
* |  x * y |  Multiplication operator  
/ |  x / y |  Division operator  
^ |  x ^ y |  Calculates x raised to the power of y  
- |  \- x |  Unary minus operator  
% |  x % y |  Modulo; find remainder of the division of x by y  
== |  x == y |  Equal logical operator. Return 1 if true, 0 if false.  
!= |  x != y |  Not equal logical operator. Return 1 if true, 0 if false.  
>= |  x >= y |  Greater than or equal logical operator. Return 1 if true, 0 if false.  
<= |  x <= y |  Less than or equal logical operator. Return 1 if true, 0 if false.  
> |  x > y |  Greater than logical operator. Return 1 if true, 0 if false.  
< |  x < y |  Lesser than logical operator. Return 1 if true, 0 if false.  
  
#### Define Functions

Operator |  Example Usage (Syntax) |  Description  
---|---|---  
sin |  sin(x) |  Sine  
asin |  asin(x) |  Arcsine  
sinh |  sinh(x) |  Hyperbolic sine  
cos |  cos(x) |  Cosine  
acos |  acos(x) |  Arccosine  
cosh |  cosh(x) |  Hyperbolic cosine  
tan |  tan(x) | Tangent  
atan |  atan(x) |  Arctangent  
tanh |  tanh(x) |  Hyperbolic tangent  
sqrt |  sqrt(x) |  Square root  
min |  min(x,y) |  Return smaller of two values  
max |  max(x,y) |  Return larger of two values  
abs |  abs(x) |  Absolute value  
rand |  rand() |  Random value between 0 and 1  
ceil |  ceil(x) |  Ceiling  
floor |  floor(x) | Floor  
log |  log(x) |  Natural logarithm (base-e)  
log10 |  log10(x) |  Logarithm to base-10  
avg |  avg(v1,v2,v3,...) |  Returns the average of a set of values  
sum |  sum(v1,v2,v3,...) |  Returns the sum of a set of values  
div |  div(x,y) |  Div; returns the nearest round number from the division of x by y  
mod |  mod(x,y) |  Modulo; find the remainder of the division of x by y  
pow |  pow(x,y) |  Returns x to the power of y  
if |  if(v1,v2,v3) |  Returns v2 if v1 is true (equals 1) otherwise returns v3  
  
#### Defined Constants

Constant | Value |  Description  
---|---|---  
PI, pi |  3.141593 |  pi is the ratio of the circumference of a circle to its diameter, a mathematical constant.  
E, e |  2.718282 |  e is Euler's number, a mathematical constant.  
TR, DL |  +1e-30 |   
TOP |  +1e+30 |   
BOTTOM |  -1e-30 |   
  
Related Topics and Activities

  * [Run Formula](<DMEditRunFormula.md>)