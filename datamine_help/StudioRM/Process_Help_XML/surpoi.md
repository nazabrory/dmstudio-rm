# SURPOI Process

To access this process:

  * Enter "SURPOI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SURPOI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SURPOI>).

## Command Overview

Interpolate upper and/or lower elevation values onto a file of two-dimensionally defined points.

The **SURPOI** process can be used to interpolate a variable onto a set of point data. The common application of this process for underground mine planning is to interpolate a set of Z elevations from survey points onto a digitized set of strings and perimeters, which have the correct X and Y coordinates but not the correct elevations. 

The output will be completely three dimensional strings or perimeter that can be subsequently used in **DRIVES** to generate wireframe models of existing excavations.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  The input data file, which must contain at least two fields which define the two- dimensional position of a series of points. |  Input |  Yes |  Undefined  
ELEV |  Input file containing elevation data that will be used to control the interpolation. It must contain the fields **X** , **Y** and **UPPER** , and may optionally contain the field **LOWER**. |  Input |  Yes |  Undefined  
TREND |  Optional input trend file. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file that will contain all the fields that were in the input file, plus the interpolated elevation fields.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
XIN |  Name of the X field in the input data file. |  IN |  Yes |  Numeric |  Undefined  
YIN |  Name of the Y field in the input data file. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
RADIUS |  Search radius for interpolation [the default is the mean spacing between the elevation data points]. |  No |  Undefined |  Undefined |  Undefined  
POWER |  Power to be used for inverse power of distance weighting (2). |  No |  2 |  Undefined |  Undefined  
MINNOP |  Minimum number of samples required for interpolation (1). |  No |  1 |  Undefined |  Undefined  
  
## Example
    
    
    !SURPOI       &IN(SURV21), &ELEV(ELEV21), &OUT(NEW21), *XIN(XL),  
  
---  
      
    
                 *YIN(YL), @RADIUS=150, @POWER=2, @MINNOP=3  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> Field ffffffff missing from input elevation file |  One of the compulsory fields **X** , **Y** or **UPPER** is missing from the file specified as &**ELEV**.  
>>> Explicit field ffffffff missing from input data file |  One of the fields specified as * **XIN** or * **YIN** is missing from the file specified as &**IN**.  
>>> WARNING - RECORD HAS UPPER BELOW LOWER - IGNORED <<< |  The value of the field **UPPER** is less than the value of the field **LOWER** in the file specified as &**ELEV**.  
>>> WARNING \- nnnnnn RECORDS IGNORED - ONE VALUE ABSENT <<< |  Records with missing data values are ignored.  
>>> NO DATA IN INPUT FILE <<< |  Check the name and content of the file specified as &**IN**.  
>>> NON-NUMERIC FIELD(S) IN INPUT FILE <<< |  The fields specified as * **XIN** or * **YIN** in the file specified as &IN must be numeric.  
>>> ESSENTIAL FIELDS IN THE INPUT ELEVATION FILE ARE EITHER MISSING OR IMPLICIT <<< |  One or more of the compulsory fields **X** , **Y** or **UPPER** is either missing or implicit in the file specified as &**ELEV**.  
  
Related topics and activities

  * [SURCAL Process](<surcal.md>)

  * [SURFIP Process](<surfip.md>)

  * [SURLOG Process](<surlog.md>)

  * SURPOI Process

  * [SURTAC Process](<surtac.md>)

  * [SURTRI Process](<surtri.md>)

  * [SURVIG Process](<survig.md>)

  * [SURVIN Process](<survin.md>)

  * [SURVOU Process](<survou.md>)