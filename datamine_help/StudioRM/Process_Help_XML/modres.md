# MODRES Process

To access this process:

  * **Report** ribbon **> > Report >> Calculate Reserves**.

  * Enter "MODRES" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MODRES** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MODRES>).

## Process Overview

Evaluate an ore body model through one or more sets of perimeters defining an open pit, using full or partial block evaluation, and writes an output file of results.

This file may be read by the [TABRES](<tabres.md>) process to produce various reserve tabulations. An output model, containing a MINED field, may be produced. Multiple pits may be evaluated in a single run. Benches for evaluation need not match the levels in the model.

### Input and Output Model

The input model is in standard DATAMINE model file format, and may contain cells and sub-cells, in any order; the model does not have to be sorted on IJK to be processed by **MODRES**. 

The fraction of the cell or sub-cell mined may be stored in the **MINED** field of the optional output model file, as a value in the range 0 to 1\. 

The output model file will be an exact copy of the input file, with the **MINED** field added if it does not already exist in the input file. The output model file may be the same as the input model file (in-place updating) if the **MINED** field exists in the input model file.

### No Perimeter File

If no perimeter file is entered, the entire model is evaluated bench by bench and the results written to the &**RESULTS** file. Note that the process constructs a dummy perimeter in this case, and will therefore still record that 1 perimeter was read.

### Perimeter Conventions

If a perimeter file is specified, the perimeters must apply to benches. All perimeters must be specified clockwise; they must not be closed. The perimeter file is in the standard Datamine perimeter format. It must contain the numeric and explicit fields **XP** , **YP** , **ZP** , **PTN** and **PVALUE** , where **PTN** is the point number in the perimeter and PVALUE is a numeric perimeter identifier. Each perimeter must have a unique **PVALUE** identifier. All points for the same perimeter must be together in the file.

There are two forms of the perimeter file, specified by the value of the @PAIRS parameter.

### Bench Centre Perimeters

If @**PAIRS** =0 (default) then each perimeter is assumed to lie at the bench centre. 

If @**ZVALUE** =0 (default) then the **ZP** field is ignored and the bench that each perimeter relates to is determined by its PVALUE. The perimeter identifier **PVALUE** must have the form _bbbbbb.nn_ where _bbbbbb_ is the bench number and _nn_ is an identifier on the bench. For example, two perimeters for bench 6 could have **PVALUE** s of 6.0 and 6.1. There can be multiple perimeters on one bench, as long as each is separately identified in this way. Note that Bench 1 refers to the uppermost level of model cells.

If @**ZVALUE** =1 then the bench to which each perimeter belongs will be identified by its **ZP** value, and not by its **PVALUE**. Normally, all points in a single perimeter would have the same **ZP** value, but if the **ZP** values vary, then the bench number is derived from the **ZP** value of the last point in the perimeter string.

The order of perimeters in the file does not matter, but within one run of **MODRES** , perimeters are _ADDITIVE_ , and therefore should not overlap. However, between different runs of **MODRES** , perimeters are _INCREMENTAL_ on what has been previously mined (although additive on each other) and therefore should overlap. 

### Bench Bottom and Top Perimeters

If parameter @**PAIRS** =1, then benches are no longer defined by the model cells in Z; they are defined by consecutive pairs of perimeters, one for the bottom of the bench and one for the top. The elevation of each perimeter is defined by the **ZP** value, and the bench number by the _bbbbbb_ component of the **PVALUE** field. 

For example, two consecutive perimeters in the file could have **PVALUE** s of 3.00 and 3.01, with ZP values of 275 and 282. These would define bench 3 as lying between elevations 275 and 282, irrespective of the model dimensions. Note that, as before, each perimeter must have a different **PVALUE**. 

The bench bottom and top perimeters may be different, allowing a pit to be defined in as much detail as required. The perimeter defining the top of one bench to be mined may be different from the perimeter defining the bottom of the next bench up. Thus **MODRES** may be used to evaluate highly detailed open pits, which can include haul roads or other features. Where bench top and bottom perimeters are different, **MODRES** interpolates intermediate perimeters as required, allowing accurate evaluation.

### Evaluation Parameters

Evaluation parameters are specified interactively. All results may be classified by rocktype, either as selected values of a rocktype field, or by classing these field values as one of a set of **ORE, WSTE, AIR, S1, S2, S3, S4, S5, S6, S7**. The S1 - S7 classifications are designed for stockpile material, but they may also be used as alternate ore or waste classifications if required.

When classifying reserves by selected values of rocktype, unnamed rocktypes will be assigned to the final rocktype in the list. It is good practice to add a dummy rocktype to the list (e.g. XXXX or 9999) so that the presence of unnamed rocktypes will be easily detected.

When classifying reserves by **ORE, WSTE** (and so on) unnamed rocktypes are assigned to **WSTE**.

The results may also be classified by grade intervals for a selected main grade field. These grade intervals do not have to be uniform.

The full possible hierarchic classification of results is:-

Bench \- Perimeter - Rocktype - Grade interval.

All numeric fields which are not standard model or perimeter fields, and which are not chosen as the rocktype or main grade field, are also evaluated automatically. See the Errors section for exceptions to this.

### Balancing Volumes

**MODRES** also produces, for each perimeter, a balancing volume, which is the difference between the volume within the perimeter (computed accurately) and the sum of volumes of the cells and sub-cells mined within the perimeter.

If the perimeters lie wholly within the modelled region, for partial block evaluation (default) these balancing volumes are caused by small arithmetic inaccuracies; for full block evaluation (parameter @**FULLCELL** =1) they will be both positive and negative, caused by the difference in volume between the sum of all cells and sub-cells whose center lies within the perimeters and the actual volume calculated as bench height * the perimeter area.

If the perimeters cover volumes greater than those modelled (either because the perimeters go outside the model region, or because cells or sub-cells within the model are absent) then the balancing volumes represent as accurately as possible the volume contained within the perimeter which is mined but not modelled. Modelled volumes which were mined at evaluation time are excluded from these balances.

Small negative balancing volumes can occur, particularly if full cell evaluation is being used. However, large negative balances are an indication of errors in either the input model or in the perimeters. A model that contains duplicate or overlapping cells will cause negative balances, because the total volume of the cells is greater than the space they occupy. The [PROMOD](<promod.md>) command can be used to check for such errors.

Perimeters that contain crossovers (i.e. "figure eight" shapes) can also cause negative balances. Such perimeters contain both clockwise and anti-clockwise sections. If the enclosed area of the clockwise sections is greater than that of the anti-clockwise sections, then the perimeter is treated as clockwise, but the anti-clockwise sections will be reported as negative balancing volumes. If the reverse is true, then the perimeter is treated as anti-clockwise or malformed and a fatal error occurs. See Errors below.

### Densities

In computation of tonnages from volumes, any **DENSITY** field within the input model is used. If the **DENSITY** field exists, then unmodelled regions will use the default value of the **DENSITY** field. If the **DENSITY** field does not exist or if its value is absent, then an overall density may be supplied by use of the @**DENSITY** parameter. If this was not supplied, then the density used is 1.0.

### Passes through the Model File

The process reads in as many perimeters from the optional input perimeter file as possible (maximum 100, or the number of points to occupy half the virtual array space. This space is 2,000,000 words (1,000,000 points).

The model is then read (sub-)cell by (sub-)cell, and each evaluated in turn against all the perimeters.

Therefore, if the number of perimeters is less than 100 and all perimeter points fit in half the virtual array space, then the model is read just once to perform all evaluations (a single pass).  
Otherwise, the model is read once for each set of perimeters (multiple passes). If multiple passes are required, and incremental perimeters are entered (i.e. they overlap on a bench) then an output model must be specified, as it is used to store the intermediate results from each pass.

## Command Line Input

On completion of the initial Files, Fields and Parameters screen, you are prompted for the following information:

>ENTER EVALUATION PARAMETERS  |  Standard evaluation consists of mean grades and tonnages for each <bench or section>

  * Enter Y or Yes (or <RETURN>) for standard evaluation:
  * Enter N or No to specify evaluation parameters.

  
---|---  
>ROCKTYPE CLASSIFICATION  |  Each evaluation (within a perimeter on a <bench or section> may be classified by rocktype. There are two types of classification possible:- by ore, waste, air, stockpile and so on, or by given values of the rocktype field: Results may only be classified by rocktype if there is a suitable rocktype field.

  * Enter Y or Yes (or <RETURN>) for classification.
  * Enter N or No to omit classification by rocktype;

If Y or Yes: >Enter name of field defining rocktype:- >FIELD > Enter required field name.  
>CLASSIFICATIONS POSSIBLE ON FIELD nnnnnnnn OF TYPE n  |  You may either specify up to 20 values of the field, each of which will be separately identified in the results; or you may classify rocktypes as ore, waste, air, stockpile, etc.

  * Enter Y or Yes (or <RETURN>) to classify by ore etc:
  * Enter N or No to classify by rocktype field value.

Do you wish to classify by ore etc.? >YES/NO >  
If Y, Yes or <return>  
>CLASSIFICATION BY ORE, WASTE ETC.  |  Enter pairs of values in form:- <rocktype value>,<class> where the class may be one of the following:- ORE WSTE AIR S1 S2 S3 S4 S5 S6 S7 The rocktype field is of type n End by entering (blank) or (blank,blank) Maximum entries is 40: unnamed rocktypes will be classified as waste (WSTE).  
If N or No:  
>CLASSIFICATION BY VALUES OF FIELD nnnnnnnn  |  Enter one value per line of this field of type n Terminate with (blank) or (blank,blank) Maximum number or entries is 20 >VALUE > Enter required rocktype field value; terminate with blank.  
After rocktype classification, or if no rocktype classification, and if the model contains grade fields:  
>GRADE INTERVALS  |  If no grade intervals are specified then means are calculated. Otherwise you may specify grade ranges of a named numeric field. Enter Y or Yes (or <RETURN>) to specify grade ranges. Enter N or No to compute means only.

  * If Y, Yes or <return>;

>Enter name of main grade field. >FIELD > Enter field name.  
>GRADE INTERVALS FOR MAIN GRADE nnnnnnnn  |  Enter (lower,upper) limits separated by commas: E.g. 0.1,0.25 <RETURN>. The lower bound is included and the upper bound is excluded in the range. Enter 0,0 (or blank) to end. Max bins 20 Under- and over-flow bins are added automatically.  
>Is this satisfactory? | 

  * Enter Y or Yes (or <RETURN>) if satisfactory
  * Enter N or No to restart entries.

  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Model file for evaluation. Must contain at least the fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK**. |  Input |  Yes |  Block Model  
PERIMIN |  Optional input perimeter file. Must contain at least the fields **XP, YP, ZP, PTN, PVALUE**. The **PVALUE** field contains the bench number as the integer part: e.g. 3.0 for first perim on bench 3, 3.1 for second etc. If the **PAIRS** option is set, then the ZP value must contain the bench bottom elevation in one perimeter, then the bench top in the next. All points for one perimeter must be together. Perimeters must be clockwise, unclosed. |  Input |  No |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
RESULTS |  Output |  Yes |  Undefined |  The output results file, in a format suitable for input into the **TABRES** process.  
OUT |  Output |  No |  Block Model |  Optional output model file. This may be the same as the input, if the **MINED** field exists in the input file. The **MINED** field will be created in the output file if it does not exist.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DENSITY |  Set required density value. This will only be used if there is no **DENSITY** field in the input model. If there is no **DENSITY** field, and no **DENSITY** parameter, then a value of 1.0 is used. |  Yes |  1 |  0.000001,+ |  Undefined  
ZVALUE |  |  Option |  Description  
---|---  
1 |  For single perimeters at bench centres, take the Z value from the **ZP** field instead of using the level number in the **PVALUE** field.  
No |  0 |  0,1 |  0,1  
PAIRS |  |  Option |  Description  
---|---  
1 |  Use pairs of perimeters to define bench bottoms and tops, as defined by ZP field.  
No |  0 |  0,1 |  0,1  
FULLCELL |  |  Option |  Description  
---|---  
1 |  whole cell evaluation in place of partial cell evaluation.  
No |  0 |  0,1 |  0,1  
PRINT |  |  Option |  Description  
---|---  
1 |  Show a line for each cell evaluated in each perimeter.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !MODRES &IN(MODEL), &PERIMIN(PITPERMS),   
  
---  
      
    
    &OUT(MODEL1), &RESULTS(RESULTS), @DENSITY=1  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> INPUT AND OUTPUT MODEL FILE MAY NOT BE SAME <<<>>> WHERE NO MINED FIELD EXISTS IN INPUT FILE  <<<>>> ERR 123 <<< ( 0) in MODRES |  Fatal; the process is exited.  
>>> BAD MODEL FILE: FIELD IMPLICIT OR WRONG TYPE <<< >>> ERR 122 <<< ( n) IN MODRES |  Fatal; the process is exited.  
>>> BAD PERIMETER FILE: FIELD IMPLICIT OR WRONG TYPE <<< >>> ERR 122 <<< ( n) IN MODRES |  Fatal; the process is exited.  
>>> MISSING ESSENTIAL FIELD IN MODEL FILE <<< >>> ERR 103 <<< ( n) IN MODRES |  Fatal; the process is exited.  
>>> MISSING ESSENTIAL FIELD IN PERIMETER FILE <<< >>> ERR 103 <<< ( n) IN MODRES |  Fatal; the process is exited. In the above messages, n is the internal file number.  
>>> WARNING INPUT MODEL FIELD FFFFFFFF IGNORED <<< |  Input model field matches standard Results field name To transfer this grade field to results file please rename the field in the input model fil. Warning; the process continues, but field FFFFFFF in the input model file is ignored. The standard results field names referred to are: TYPE, PLANE, NUMBER, SEQUENCE, PERIMID, VOLUME, TONNES, INTERVAL, LOWER, UPPER, MODEL, PERIMIN.   
>>> TOO MANY FIELDS, ONLY n ALLOWED <<< >>> m FIELDS USED ON ENTRY TO RESDD<<< >>> ERR132 <<< (n) IN RESDD |  Fatal; the process is exited. Means that there are too many numeric fields in the model and a valid results file cannot be created. Each numeric field chosen for evaluation generates two fields in the results file. The maximum number of evaluation fields is between 23 and 25, depending on the evaluation options that have been selected. The numbers n and m are not of direct relevance to this error.  
>>> ERROR \- INCOMPATIBLE FIELD TYPES <<< |  Fatal; the process is exited. Means that a field in the perimeter file has the same name as one in the input model, but they are of differing types e.g. one is Numeric and the other is Alphanumeric.  
>>> ERROR - PERIMETER n,PVALUE m.mmm ANTICLOCKWISE OR MALFORMED<<< |  Fatal; the process is exited.