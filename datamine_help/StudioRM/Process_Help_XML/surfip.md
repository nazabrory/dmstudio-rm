# SURFIP Process

To access this process:

  * Enter "SURFIP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SURFIP** and click **Run**.

  * **Estimate** ribbon **> > Estimate >> Seams**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SURFIP>).

## Process Overview

Interpolates a set of point data into a pair of surfaces expressed as sub-cells in a 3-D model with any number of cells in the Z direction.

The surfaces are modeled as sub-cell divisions in the Z direction, at the exact surface position. **SURFIP** also allows simultaneous division of cells into sub-cells in the X and Y directions, under user control, in places where the local slope of the surface is steep.

The use of an optional trend file permits interpolation of residuals around a trend surface, and faults and sub-crop limits may be specified by use of an optional perimeter file defining interpolation regions.

### Input data and interpolation

Data are entered from file &**IN** as a series of X and Y co-ordinates together with elevations of upper and lower surfaces. These are the * **X** , * **Y** , * **UPPER** and * **LOWER** fields. A prototype model is required to define the model parameters (the &**PROTO** file), but no data records from the prototype model are used (even if they exist), since **SURFIP** constructs an entirely new model.

This prototype file may be constructed by process [PROTOM](<protom.md>), or it may be a previously existing model. Note that **SURFIP** always represents its surfaces as sub-cells, and therefore the **XINC** , **YINC** and **ZINC** fields should be explicit (sub-cells used); however, if the input prototype should contain implicit values of these fields, they are converted to explicit automatically.

The elevation of the upper surface and the distance between the surfaces are interpolated using the inverse power of distance method. The optional @**POWER** parameter controls this power; note that 0 should not be used; however, averaging of points may be effectively obtained by setting @**POWER** to some small value, such as 0.00001. The higher the value of @**POWER** , the more the output surface will be close to the input data points near the points. However, values of @**POWER** greater than about 5 may give rise to arithmetic errors during processing as numbers become too large. The position of the lower surface is calculated by subtraction of the interpolated thickness from the top. This method prevents any cross-overs of the top and bottom surfaces.

The sample data file usually contains two elevation fields - * **UPPER** and * **LOWER**. However, if only one surface is required (as in a model of topography) then the other elevation field may be entered as - or dummy; SURFIP will then set the top of the model as the * **UPPER** field, or the bottom of the model as the * **LOWER** field.

### Splitting into sub-cells in X and Y

Interpolation is carried out initially at the centres (in the X-Y plane) of each cell. In a second pass, for any pair of adjacent columns of cells where the maximum vertical distance between corresponding (upper or lower) surface points exceeds a defined threshold value, the sub-cells required at the positions of the upper and lower surfaces are sub-divided further by vertical divisions to give, in plan view, 2, 4, or 8 sub-cells in either X or Y independently, the number increasing with increasing estimated slope in X or Y. Thus, where the slope is high, a cell may be split into as many as 8*8 sub-cells. This method ensures that the surface is accurately defined where it changes rapidly, without imposing this level of detail (and a large storage overhead) on the entire model. The maximum split possible is controlled by optional parameter @SPLITS; this may have the following values:-

  * = 0 No splitting possible (cells only)

  * = 1 A maximum of 2 possible in X or Y

  * = 2 A maximum of 4 possible in X or Y

  * = 3 A maximum of 8 possible in X or Y. This is the default.

The default value for the threshold is 0.5 of the average seam thickness as obtained during the first pass. This may be overridden by specifying a value for the optional @**MAXSTEP** parameter, which can be set to the maximum thickness difference (the threshold) permitted between adjacent cell centre surface values before splitting takes place.

Note that setting @**MAXSTEP** =0 has a special meaning. All cells will be divided into the maximum number of sub-cells allowed by the @**SPLITS** parameter (default 8*8) in the output model. If @**MAXSTEP** >0, then whole cells lying completely between, above or below the surfaces will be output as complete cells, even if cells lying on the surface are sub-divided in X and/or Y.

Although one of the two fields * **UPPER** and * **LOWER** may be implicit, it is not permissible to have both fields so. If a seam model is required with both surfaces horizontal then the sample data file should contain a single record with the appropriate * **UPPER** and * **LOWER** values, @**RADIUS** should be set sufficiently large, and @**MINNOP** should be set to l.

Interpolation proceeds by column. A progress message is produced at the start and end of interpolation of each column, in each interpolation pass. 

If the &IN file is sorted on X, then **SURFIP** recognises this and searches the data faster. The saving in execution time on interpolating a surface from a large amount of data can be substantial.

If multiple perimeters have been used in interpolation, the following message is displayed:
    
    
    >>> Interpolation has been with more than one  
    >>> perimeters, and therefore the model may require  
    >>> sorting on IJK before proceeding

### Surface identification in the output file

The output surface model file contains a numeric field (the * **LABEL** field) used to encode seam name or rock type. The user supplies values for this field for sub-cells lying above, within, or below the seam (the @**ABOVE** , @**WITHIN** or @**BELOW** parameters). Any one or more (but not all three) of these codes may be 'absent data' (-) if desired. For conventional seam modeling, to allow combination of multiple seams, it will usually be appropriate to code 'above' as the number chosen for a waste rock type, 'within' as the particular seam code, and 'below' as missing data; the process **OVRMOD** may then be used to combine seam models.

For surface topography models, conventionally only the @WITHIN parameter is set, and the @**ABOVE** and @BELOW parameters set to absent data (-). Often the code 99 is used for air (@**WITHIN** =99), but the user may choose his or her own value.

### The Trend File

The **SURFIP** process also has the capability to use a trend surface file as input (optional file &**TREND**). This file, consisting of a **DD** only, is output by process **TREND** ; it contains the coefficients of the trend surface computed from the same data points to be input to **SURFIP** on symbolic file &**IN**.

It is used in the following way: first, all the data points have the value of the trend surface at that point subtracted from them. Then these residuals are interpolated, giving estimates of trend surface residuals at cell and sub-cell centers; finally the value of the trend surface at each cell or sub-cell centre is added back to the residuals, to give elevations. The resulting surface has the general curvature of the trend surface, but passes through the original points.

Thus it is possible to obtain interpolated values which are higher than the highest data point (e.g. an anticline), or lower than the lowest data point (e.g. a syncline), and outside the region of data extrapolation will give a surface with the same shape as the trend surface, not a flat plane as would otherwise be the case.

### The Perimeter File

SURFIP may optionally use a perimeter file to control interpolation. This file should be in standard perimeter file format (containing numeric fields **XP** , **YP** , **ZP** , **PTN** and **PVALUE**) and can contain any number of perimeters, unclosed, and entered clockwise.

A separate interpolation will be carried out for each perimeter in the file; for the upper surface (hanging wall) only data points lying within the perimeter will be selected, and only cells and sub-cells lying inside the perimeter will be generated. However, thickness values will be taken from data points not only within the perimeter, but also from points lying within an @**RADIUS** from the (sub-)cell centre outside the perimeter. This is to allow continuity in thickness interpolation across a fault boundary.

This feature permits sub-crop or interpolation limits to be entered as a perimeter; or faults may be specified as a set of adjacent perimeters, so that each fault zone can be separately interpolated. The trend surface (&**TREND** file) may be used at the same time as the &**PERIMIN** file.

Cells will always be divided into sub-cells along the boundary of each perimeter, to the maximum number specified by the @**SPLITS** parameter; only those sub-cells whose centers lie within the perimeter will be interpolated and output.

Perimeters must abut each other accurately to ensure that there are not missing parts of the surface at the boundary; and perimeters must not overlap, or the same sub-cells will appear twice in the output file.

The output surface model file will require sorting on field IJK after generation, if more than one perimeter was in the input file. This is because the cells and sub-cells are generated in separate passes for each perimeter, and added to the end of the file. However, within each perimeter, cells and sub-cells will be generated in IJK order.

If a perimeter file was used, the output surface model will contain an extra field **PVALUE** , giving the perimeter identifier **PVALUE** within which the part of the surfaces lie. This may be used for surface classification or selection of part of the model later.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Prototype model. Must contain at least the fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK.** |  Input |  Yes |  Block Model Prototype  
IN |  Input intersection data. Must contain the fields **X , Y , UPPER , LOWER**. |  Input |  Yes |  Undefined  
TREND |  Trend coefficients file (as produced from process TREND) defining a surface to be subtracted from the data before interpolation and added back to the interpolated values for each cell or sub-cell. The field names are **C0, CX, CY, CXY, CX2, CY2, CX2Y, CY2X** etc. |  Input |  No |  Undefined  
PERIMIN |  Input perimeter file defining fault boundaries, or surface limits. One pass through the interpolation process is made for each perimeter on file, using only data lying within the perimeter, and generating only (sub-)cells lying within this perimeter. At the boundary, cells will be split into sub-cells, controlled by the **SPLITS** parameter. |  Input |  No |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model |  Output interpolated seam model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Name of intersection X field. |  IN |  Yes |  Numeric |  Undefined  
Y |  Name of intersection Y field. |  IN |  Yes |  Numeric |  Undefined  
UPPER |  Name of intersection roof elevation field. Enter - or dummy if only **LOWER** supplied. |  Undefined |  Yes |  Numeric |  Undefined  
LOWER |  Name of intersection floor elevation field. Enter - or dummy if only **UPPER** supplied. |  Undefined |  Yes |  Numeric |  Undefined  
LABEL |  Name of numeric field to be generated with values corresponding to **ABOVE , WITHIN , BELOW**. |  MODEL |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
RADIUS |  Search radius. |  Yes |  Undefined |  Undefined |  Undefined  
ABOVE |  Value of **LABEL** above seam. |  No |  Undefined |  Undefined |  Undefined  
WITHIN |  Value of **LABEL** within seam. |  No |  Undefined |  Undefined |  Undefined  
BELOW |  Value of **LABEL** below seam. |  No |  Undefined |  Undefined |  Undefined  
POWER |  Weighting power (2). |  No |  2 |  Undefined |  Undefined  
MINNOP |  Minimum number of samples (5). |  No |  5 |  Undefined |  Undefined  
MAXSTEP |  Max. elevation difference before sub-cells interpolated in horizontal plane [0.5 seam thickness]. If **MAXSTEP** is exactly 0, then splitting will take place over the entire model generated, as controlled by SPLITS. |  No |  Undefined |  Undefined |  Undefined  
SPLITS |  Controls splitting of sub-cells. The maximum number of sub-cells will be 2** **SPLITS** in X and Y. Default =3 [i.e. 2**3] = a max of 8*8 subcells in the XY plane (3). |  No |  3 |  1,3 |  1,2,3  
PRINT |  |  Option |  Description  
---|---  
1 |  summary of parameters and average seam thickness displayed (0).  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !SURFIP    &PROTO(SEAMPROT),&IN(ELEVATION),&MODEL(SURFMOD),          
  
---  
      
    
    *X(EAST),*Y(NORTH),*UPPER(HANGWALL),*LOWER(FOOTWALL),          
      
    
    *LABEL(SEAMCODE),@RADIUS=100,@ABOVE=99,@WITHIN=15,          
      
    
    @BELOW=-,@SPLITS=0  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> WARNING - RECORD HAS UPPER BELOW LOWER - IGNORED <<< >>> ERR 131 <<< ( n) in SURFIP |  The sample data file &**IN** contains a record for which the upper surface value * **UPPER** is less than the lower surface value * **LOWER**. n is the number of valid records read before the current record. Warning; this record is ignored.  
>>> WARNING - UPPER DATA ABOVE TOP OF MODEL <<< >>> ERR 132 <<< ( n) IN SURFIP |  The sample data file &**IN** contains n records for which the upper surface value * **UPPER** is above the top of the model. Warning; processing continues.  
>>> WARNING - UPPER DATA BELOW BOTTOM OF MODEL <<< >>> ERR 133 <<< ( n) IN SURFIP |  The sample data file &**IN** contains n records for which the upper surface value *UPPER lies below the bottom of the model. Warning; processing continues.  
>>> WARNING - LOWER DATA ABOVE TOP OF MODEL <<< >>> ERR 134 <<< ( n) IN SURFIP |  The sample data file &**IN** contains n records for which the lower surface value * **LOWER** lies above the top of the model. Warning; processing continues.  
>>> WARNING - LOWER DATA BELOW BOTTOM OF MODEL <<< >>> ERR 135 <<< ( n) IN SURFIP |  The sample data file &**IN** contains n records for which the lower surface value * **LOWER** lies below the bottom of the model. Warning; processing continues.  
>>> NO DATA IN INPUT FILE <<< >>> ERR 136 <<< ( n) IN SURFIP |  There are no valid data records in the input sample data file &IN. Fatal; the process is exited.  
>>> NON-NUMERIC FIELD(S) IN INPUT FILE <<< >>> ERR 137 <<< ( n) IN SURFIP |  One of the four input fields * **X** , * **Y** , * **UPPER** or * **LOWER** in the sample data file &IN is not numeric, or one or more of the fields are missing. Fatal; the process is exited.  
>>> WARNING - 999999 RECORDS IGNORED - ONE VALUE >>> ABSENT <<< >>> ERR 138 <<< ( n) IN SURFIP |  no data records have been read from sample data file &IN for which *X and *Y fields contain valid data, but one or both of the *UPPER and *LOWER fields contain the missing data value. Warning; these n records are ignored.  
>>> NO DATA POINTS WITHIN RANGE OF MODEL <<< >>> ERR 140 <<< ( n) IN SURFIP |  On the first interpolation pass, no interpolation could be carried out as less than @**MINNOP** points were found within @**RADIUS** of each cell centre. Fatal; the process is exited. Increase @**RADIUS** and/or reduce @**MINNOP**.  
>>> BOTH LOWER AND UPPER FIELDS MISSING FROM FILE <<< >>> ERR 141 <<< ( fileno) IN SURFIP |  The &**IN** file fileno contained neither an * **UPPER** nor a * **LOWER** field. Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELD(S) IN MODEL PROTOTYPE <<< >>> ERR 142 <<< ( fieldno) IN SURFIP |  One or more of the essential numeric fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK** was missing or alpha in the &**PROTO** file. Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELD(S) IN PERIMETER FILE <<< >>> ERR 143 <<< ( fieldno) IN SURFIP |  One or more of the essential numeric fields **XP, YP, ZP, PTN, PVALUE** was missing or alpha in the &**PERIMIN** file.  
>>> ABOVE, WITHIN AND BELOW PARAMETERS ALL ABSENT DATA <<< >>> ERR 144 <<< ( n) IN SURFIP |  The values for parameters @**ABOVE** , @**WITHIN** and @**BELOW** were all absent data. This would give rise to a null model, so the process is terminated.  
>>> WARNING - PERIMETER HAS LESS THAN THREE POINTS \- >>> IGNORED <<< |  The perimeter, whose **PVALUE** value is given in a previous message, has less than three points. Warning; the perimeter is ignored, and the next one taken from file.  
>>> WARNING - PERIMETER HAS TOO MANY POINTS - IGNORED <<< |  The perimeter, whose **PVALUE** value is given in a previous message, has more than 1199 points. Warning; the perimeter is ignored, and the next one taken from file.  
  
Related topics and activities

  * [SURCAL Process](<surcal.md>)

  * [SURLOG Process](<surlog.md>)

  * SURFIP Process

  * [SURPOI Process](<surpoi.md>)

  * [SURTAC Process](<surtac.md>)

  * [SURTRI Process](<surtri.md>)

  * [SURVIG Process](<survig.md>)

  * [SURVIN Process](<survin.md>)

  * [SURVOU Process](<survou.md>)