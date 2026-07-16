# EXTRA examples

To access this screen:

  * Run the **[EXTRA](<../Process_Help_XML/extra.md>)** process from the command line by typing 'extra'. Specify an input file, output file and (optionally) retrieval criteria and click OK \- the Expression Translator displays.

For more information on the **EXTRA** process, see [EXTRA](<../Process_Help_XML/extra.md>).

## EXTRA Background

The ways in which **EXTRA** can be used are endless. This section provides a few ideas of what it can do.

Before **EXTRA** starts to process records from the input file, it must define which fields will appear in the output file. It is important to understand that _all_ decisions about fields in the output file are made _before_ any records are processed.

Normally, the fields that appear in the output are:

  * All fields that are in the input file

  * Fields created in the transforms you specify.

You can reduce the number of fields in the output file by using **saveonly()** , **keep()** and **erase()** functions. There are examples of these functions below.

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

## Examples

### Add comments

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
  
**Note** : Comments are _not_ supported within IF statements. 

### Alphanumeric field functions

The following example illustrates the functions for alphanumeric fields. It creates a new alphanumeric field, `s1`, with a length of 40 characters and assigns to it the comma-separated list of field values. The `trim()` function is used to remove trailing spaces from the `BHID` field. The `string()` function is used to convert numeric fields to character strings (with two decimal places), and the `join()` function is used to concatenate the various bits into a single alphanumeric value. Note that all unwanted fields can be erased with a single use of the `erase()` procedure:
    
    
    s1;a40 = concat(BHID, ",", string(FROM, 2), ",", string(TO, 2), ",", string(Cu, 2), ",", string(Zn, 2))
    
    
    saveonly(s1)

The resulting file could be **OUTPUT** , and then loaded into Microsoft Excel or another package as a comma-separated values (CSV) file. (This function is available directly in **OUTPUT** , but this method gives finer control on the number of decimals, etc.)

#### Apply capping in a new field
    
    
    AU_C=AU
    
    
    if(AU_C>35) AU_C=35 end

..and here's another way:
    
    
    AU_C = min(AU, 35)

#### atan2 (arctangent with two arguments)

The atan2 function calculates the angle (in degrees) from the origin to the point (X, Y) from the positive X-axis, considering the correct quadrant. It takes two arguments: `X` (horizontal) and `Y` (vertical), and returns the angle in degrees. Unlike `atan(Y/X)`, it handles cases where X is zero or negative, ensuring correct angles in all cases.

Note the order of the arguments is (X, Y), not (Y, X) as in some programming languages.

The result is an angle in degrees within the range -180.0 and +180.0.

Examples:
    
    
    atan2(1, 1)

Returns ( π/4 ) (45 degrees), which is the angle in the first quadrant.
    
    
    atan2(-1, -1) 

Returns (-3π/4 ) (-135 degrees), which is the angle in the third quadrant.

**Note** : the order of the arguments is (x, y) (as in Microsoft Excel) and not (y, x) as used in other programming languages.

#### azimuth()

**EXTRA** provides **azimuth(dx, dy)** to return the azimuth in degrees of a line from (0, 0) to (dx, dy). The result is a value between 0.0 and 360.0. If dx and dy are both zero, the absent data indicator is returned. For example, to find the azimuth of each segment in a string:
    
    
    AZI = azimuth(next(XP)-XP, next(YP)-YP)

#### concat(a1,a2...)

Join two strings, trimming leading and trailing spaces off of each argument before concatenating them. Any number of arguments are accepted.
    
    
    A1;a4 = "X"
    
    
    A2;a4 = "Y"
    
    
    A3;a8 = join(A1, A2)
    
    
    A4;a8 = concat(A1, A2)

In the above example, A3 maintains the padding for each (4 character) alphanumeric argument in the result. whilst A4 removes all leading and trailing spaces, padding out to the full width of the A4 variable (8 characters).

  * A3 will be "X Y " 

  * A4 will be "XY "

#### Create a new field

You define a new field by typing its name, a specification for its type and the value to be assigned. If the field is numeric and explicit, you do not need to specify the type. 

For example:
    
    
    C = (A + B)/2 # C is an explicit, numeric field

You add the specification for other types of fields after the field name, like this:
    
    
    BHID;a12 = "RC1000" # explicit alphanumeric field, 12 characters
    
    
    XMORIG;ni = 10200 # implicit numeric field
    
    
    VERSION;a24i = "Resource estimate 2Q24" # implicit alphanumeric field, 24 characters

The letter "a" means "create an alpha field" and "i" means "create an implicit field". For an alphanumeric field, you should specify the maximum size of the field, in characters. It you omit it, the field size will be 4 characters.

You can also create a field with the same specification as an existing field:
    
    
    BHID2;[BHID] = BHID # BHID2 has the same specification as BHID

This means "Create a field called BHID2, make it the same type as the existing BHID field and then set it to the same value as the BHID field".

#### Create an Implicit Field

**EXTRA** can also create implicit fields. Consider this example:
    
    
    XMORIG;ni = 10200.0
    
    
    YMORIG;i  = 20100.0
    
    
    ZMORIG;i  =   273.0
    
    
    REVISION;a20i = "Resource study 2Q24"

This will create four new _implicit_ fields: three numeric fields and one alphanumeric field. The "i" character can be placed anywhere in the specification except inside the length specification. For example, the following all achieve the same result:
    
    
    REVISION;a20i = "Resource study 2Q24"
    
    
    REVISION;ia20 = "Resource study 2Q24"
    
    
    REVISION;ai20 = "Resource study 2Q24"
    
    
    REVISION;i20a = "Resource study 2Q24"
    
    
    REVISION;20ai = "Resource study 2Q24"
    
    
    REVISION;20ia = "Resource study 2Q24"

#### Degrees, minutes and seconds

**EXTRA** can convert degrees, minutes and seconds to decimal degrees and _vice-versa_. Starting with fields **dd** , **mm** , and **ss** , EXTRA can easily create a field containing decimal degrees:
    
    
    # Change dd, mm, ss to decimal degrees  
    dms = dd + mm/60 + ss/3600

The field `dms` now contains decimal degrees. To change them back, use the following:
    
    
    dd = int(dms)  
    mm = mod(int(60*dms), 60)  
    ss = int(10*mod(3600*dms, 60) + 0.5)/10

The final expression rounds-off the seconds field, `ss`, to the nearest 1/10th.

Don't forget that if you are writing the expressions in a script or a macro then the keyword `go` must be entered on the last line.

#### Delete all but the last record in a drillhole
    
    
    if(BHID==next(BHID)) delete() end

#### erase(), saveonly() and keep()

The **erase()** procedure specifies a list of fields that you do not want in the output file. Like **keep()** , you can specify multiple erase instances, and you can erase in combination with both **saveonly()** and **keep()** calls.

For example, this call to **saveonly()** requests that 9 fields are written to the output file.
    
    
    saveonly(BHID, FROM, TO, LENGTH, X, Y, Z, A0, B0)

Add 3 fields to this list using **keep()** , which is like **saveonly()** , but adds to an existing list:
    
    
    keep(CU, PB, ZN)

Now use erase() to remove items from the list. In this case, the three coordinate fields:
    
    
    erase(X, Y, Z)

Here, **saveonly()** specifies 9 fields that will be written and **keep()** specifies three more. Then, **erase()** removes three fields from the list (X, Y and Z).

#### exit()

The procedure **exit()** immediately terminates processing before the current record has been written. This may be useful if a condition is found that means processing further records in unnecessary. For example:
    
    
    if (BHID != prev(BHID)
    
    
    exit()
    
    
    end

#### IF - ELSEIF

Conditional statements are supported in **EXTRA**. Conditions must be specified in brackets.

For example, to change the numeric value of **SLOPE** to 33 based on a numeric code stored in **SLPCODE** (99):
    
    
    IF (SLPCODE==99)
    
    
    SLOPE=33
    
    
    END

In the above example, EXTRA evaluates the condition provided and executes a single data change. Now consider the following example, where three conditional statements are processed:
    
    
    IF (SLPCODE==0)
    
    
    SLOPE=0
    
    
    END
    
    
    IF (SLPCODE==1)
    
    
    SLOPE=50
    
    
    END
    
    
    IF (SLPCODE==99)
    
    
    SLOPE=33
    
    
    END

Whilst there isn't anything syntactically wrong with setting up independent IF-END clauses, it will slow down processing as every statement must be evaluated before an action occurs. For a long list of statements, this is equivalent to running **EXTRA** many times and only triggering an action for one of those runs.

It's better to use IF-ELSEIF-END in these situations as **EXTRA** only has to evaluate once and then skip to the "END" once a matching condition is found, for example:
    
    
    IF (SPLCODE==0)
    
    
    SLOPE=0
    
    
    ELSE IF (SPLCODE == 1)
    
    
    SLOPE=50
    
    
    ELSE IF (SLPCODE == 99)
    
    
    SLOPE=33
    
    
    END

...executes more quickly than the previous example but achieves the same result.

**Note** : "ELSEIF" is one word. There are no spaces.

### IJK Block Model Field Functions

EXTRA has a set of functions for creating and querying a block model index field, IJK.

To use these functions, you must be processing a block model file. Otherwise, **EXTRA** will fail.

#### ijkget()

**ijkget()** returns values encoded into the block model index. Here are some examples:

Return the x-direction parent cell index:
    
    
    II = ijkget(IJK, "I")

Return the y-direction parent cell index
    
    
    JJ = ijkget(IJK, "J")	

Return the z-direction parent cell index
    
    
    KK = ijkget(IJK, "K")	

Return the x-coordinate of the parent cell
    
    
    XX = ijkget(IJK, "X")	

Return the y-coordinate of the parent cell
    
    
    YY = ijkget(IJK, "Y")	

Return the z-coordinate of the parent cell
    
    
    ZZ = ijkget(IJK, "Z")	

The second argument may be upper or lower case.

If you are processing a rotated block model, all X, Y, and Z coordinates are in the model coordinate system.

#### ijknum()

**ijknum()** combines separate I, J and K indices into a single IJK index. For example:
    
    
    IJK = ijknum(II, JJ, KK)

#### keep()

**keep()** is used to define the fields that will be in the output file. It is like **saveonly()** , but the field lists are cumulative. If you specify:
    
    
    keep(BHID, FROM, TO, LENGTH, X, Y, Z, A0, B0)

followed by
    
    
    keep(CU, PB, ZN)

then all 12 fields are written to the output. You can use as many keep lists as you like. All the fields in all the lists are saved.

The "keep" procedure may be useful if you need to save different fields in different circumstances, for example:
    
    
    saveonly("BHID", "FROM", "TO", "LENGTH", "X", "Y", "Z", "A0", "B0")
    
    
    if (type("AU") != "") keep("AU") end
    
    
    if (type("CU") != "") keep("CU") end

Here, all the standard static drill hole fields are saved, plus "AU" and/or "CU" if they exist.

#### xyzijk()

xyzijk() creates an IJK index number from X, Y and Z model coordinates. For example:
    
    
    IJK = xyzijk(XX, YY, ZZ)

Here's a worked example to shift a cell eastwards by one parent block size:
    
    
    II = ijkget(IJK, "I")     
    
    
    JJ = ijkget(IJK, "J")
    
    
    KK = ijkget(IJK, "K")
    
    
    II = II + 1
    
    
    IJK = ijknum(II, JJ, KK)
    
    
    XC = XC + XINC

### Missing Fields Management

If **EXTRA** tries to use a field that does not exist, it will report an error and stop processing the file. This can be an inconvenience if you want to erase a field and are not sure if it exists.

There are now two ways to deal with this.

#### @FLDFAIL

You can specify **@FLDFAIL=0** in the command line. This means "don't fail if a field does not exist". Alternatively, @**FLDFAIL** =1 (the default setting) means that EXTRA will fail if it tries to use a missing field.

When you specify **@FLDFAIL=0** and **EXTRA** encounters a missing field, it creates the field and set its value to the absent data indicator (for example, "-").

**Note** : **@FLDFAIL=0** does not just apply to the arguments to erase; if **@FLDFAIL=0** , EXTRA never fails because of a missing field. This means that if your transform contains "A=B+C" and either of the fields **B** or **C** do not exist in the file, they are created and assigned a "missing" value. In this example, the value assigned to field A will also be an absent data indicator.

#### type()

The second way to avoid missing field errors is to use the **type()** function.

**type()** returns a string of characters that describe the type of the field. If a field does not exist, **type()** returns an empty string (""). So, to detect if a field exists, you could specify something like this:
    
    
    if (type("B") == "") B = 0 end

**Note** : the argument passed to type is a text string and therefore you must enclose it in double-quotes. If you just pass the field name (i.e. "type(B)" ), **EXTRA** may report that the field does not exist and stop.

Since **EXTRA** must determine the names of all fields before starting processing, the following will not work, unless `@FLDFAIL=0` is set:
    
    
    if (type("B") == "") erase(B) end

### not(expr)

The function **not(expr)** inverts the truth of the expression. In **EXTRA** , a numeric expression is "false" if its value is zero and "true" if its value is not zero. You usually use relational expressions in conditional (if) statements. Often, inverting the sense of the expression makes it easier to read:
    
    
    if (not(last())) delete() end

This deletes every record in the file except the last one, which could be useful if **EXTRA** is used to accumulate values.

#### Random numbers

Extra can generate pseudo random numbers.

You can return a uniformly distributed pseudo-random number between 0.0 and 1.0 using rand():
    
    
    rand()

To generate normally-distributed random numbers, you can use rand() together with the phi() function. For example, to generate a random number R from a normally-distributed population with mean M and standard deviation S, use
    
    
    R = S*phi(rand()) + M

Similarly, lognormally-distributed random numbers can be calculated using
    
    
    R = exp(S*phi(rand()) + M)

**EXTRA** also permits generation of a random value between two bounds. For example, to generate a random integer value between 10 and 20, use;
    
    
    randbetween(10,20)

There is an, optional process parameter **@SEED** which you may use to control the starting value for the pseudo-random sequence. This may be useful when debugging a procedure, for example. If **@SEED=0** , or is negative or is not specified, EXTRA uses a starting number based on the current date and time.

**Note** : the **[RANDOM](<../Process_Help_XML/random.md>)** process can also be used to generate random values.

#### rownum()

Sometimes it is useful to add a row number field to a file. You can now do this simply by using the **rownum()** function:
    
    
    RECORD = rownum()

You could also use this in conditional statements:
    
    
    if (rownum() > 1000) exit() end

Or, to retain only every 10th record:
    
    
    if (mod(rownum(), 10) != 0) delete() end

This means "if the remainder you get when you divide the row number by 10 is not zero, delete the record".

#### saveonly()

**saveonly()** specifies a list containing all the fields you want in the output. For example:
    
    
    saveonly(BHID, FROM, TO, LENGTH, X, Y, Z, A0, B0)

If you specify **saveonly()** more than once, the list of fields in the last saveonly is the one used. So if you specify:
    
    
    saveonly(BHID, FROM, TO, LENGTH, X, Y, Z, A0, B0)

followed by:
    
    
    saveonly(CU, PB, ZN)

**EXTRA** will only save the fields **CU** , **PB** and **ZN**.

**Note** : **keep()** is like **saveonly()** but fields are added cumulatively.

#### Sort fields

The [SORTX](<../Process_Help_XML/sortx.md>) or [MGSORT](<../Process_Help_XML/mgsort.md>) process can be used to sort records into increasing or decreasing order. 

That said, consider the example of five fields, `a`, `b`, `c`, `d` and `e`, and you want to shuffle their values such that the value assigned to `a` is less than or equal to the value assigned to `b`, and `b` is <= `c`, `c` <= `d` and `d` <= `e`. 

The following **EXTRA** transformations do this, and also show that it is not necessary to place every transformation on a separate line:
    
    
    if (a > b) t = a a = b b = t end  
    if (b > c) t = b b = c c = t end  
    if (c > d) t = c c = d d = t end  
    if (d > e) t = d d = e e = t end  
      
    if (a > b) t = a a = b b = t end  
    if (b > c) t = b b = c c = t end  
    if (c > d) t = c c = d d = t end  
      
    if (a > b) t = a a = b b = t end  
    if (b > c) t = b b = c c = t end  
      
    if (a > b) t = a a = b b = t end  
    erase(t)

#### special()

The special function is used to decode any reserved values of your application. For example, MININT and MAXINT. These are the smallest and largest 32-bit integers. They may be useful in conjunction with **randbetween()**, for example:
    
    
    R0 = randbetween(0, special(MAXINT))

This returns a positive random value of the entire integer range supported by your application.

#### type(name)

EXTRA provides a **type(name)** function which returns the type of the named field. 

For example, for a field called "X", then `type("X")` returns:

"n" if X is a numeric, explicit field.

"ni" if X is numeric and implicit.

"a8" if X is an alphanumeric field of length eight.

"a8i" if X is an alphanumeric, implicit field with length eight.

"" if the field X does not exist.

Important: the argument to type must be a _string_ and _not_ the name of a field. This is so that type does not fail if the field does not exist (and **@FLDFAIL=1**). For example, "A;a4=type("BHID")" is probably correct whilst "A;a4=type(BHID) evaluates the field BHID to obtain the name of a field, and is probably incorrect.

### Unusual field names

If a field name contains characters that are part of the **EXTRA** syntax, you should enclose the name in square brackets, like this:
    
    
    [AU-FINAL] = (AUOK + AU_IPD)/2

You must enclose AU-FINAL in square brackets because it contains a minus-sign, which would be interpreted incorrectly.

**Note** : the legacy method for allowing unusual field names was to enclose the name in single quotes. This is still supported but we recommend using square brackets in new scripts or macros. You should also use this form if **EXTRA** would interpret the field name as a number.

Related topics and activities

  * [EXTRA](<../Process_Help_XML/extra.md>) (process)