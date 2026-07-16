# PERFIL Process

To access this process:

  * **Model** ribbon **> > Create >> Fill Perimeters**.

  * Enter "PERFIL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PERFIL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PERFIL>).

## Process Overview

This process creates a set of block model cells and subcells which are bounded in 2 dimensions by a perimeter, and in the third dimension by perpendicular projection distances **DPLUS** and **DMINUS**. Attribute values associated with each perimeter may be transferred to the model cells.

The perimeters in the &**PERIMIN** file must use 3 dimensional coordinates and must lie in one of the orthogonal planes (i.e. one of **XP** , **YP** or **ZP** must be constant). E.g. if the perimeter is an East-West section (XZ plane) then the XP and ZP fields from the &**PERIMIN** file are used to define the perimeter for constant Northing YP. Parameter @**PLANE** should be used to define the plane in which perimeters are to be filled. Any perimeter not in this plane will be ignored. Maximum distances **DPLUS** and **DMINUS** are required to define the influence of each perimeter measured perpendicularly to the perimeter plane. Cells and subcells are created within these limits. The distance **DPLUS** is measured in the increasing direction of the perpendicular axis, and **DMINUS** in the decreasing direction.

**DPLUS** and **DMINUS** may be defined as parameters or as fields in the &**PERIMIN** file. If both are defined then the field values take priority over the parameters. **DPLUS** and **DMINUS** values of zero are not permitted.

The **OVCHECK** parameter can be used to determine what happens in the case of overlapping perimeters:

  * if **OVCHECK** is set to 1 (the default) then the attributes of the last matching perimeter are assigned to the cells. If the _FS_ option is being used then further subcell splitting may occur.

  * if **OVCHECK** is set to zero then it is assumed that the perimeters do not overlap, so if overlapping does occur then overlapping cells and subcells will be created. This will lead to an invalid model. Although use of this option will improve the processing speed it should only be used if it is certain that there are no overlapping perimeters.

The @**RESOL** parameter is used to round the cell dimension to a fractional part of a parent cell dimension when the _FS_ type filling is used. This is particularly useful if two perimeters have a common boundary, but due to inaccuracies in the digitizing the two strings are not exactly coincident. Rounding the subcell dimension in this way will avoid either overlapping subcells or gaps in the model.

If no perimeter file is specified or if no attributes are specified then the process will create a field ZONE in the output model file. By default the value of the field ZONE is 0, but can be reset using optional parameter **ZONE**.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Prototype model file. This defines the model parameters. Records in this file are ignored. |  Input |  Yes |  Block Model Prototype  
PERIMIN |  The input perimeter file. The fields required are **XP,YP,ZP,PTN,** and **PVALUE** (standard perimeter format). All perimeters in the file will be used. Perimeters must lie in the plane as specified by the **PLANE** parameter. The file may contain fields **ATTRIB1-5** which can be carried across to the output model file. All cells within each perimeter will be assigned these values. If no perimeter file is specified, the entire model will be filled with cells (using the **XSUBCELL , YSUBCELL** and **ZSUBCELL** parameters). In the latter case, a field **ZONE** with value **ZONE** is added to the model. |  Input |  No |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model |  Output model file containing all cells and subcells which lie within the perimeters. This file will be sorted on IJK. The **MODEL** file must NOT be the same as the **PROTO** file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
DPLUS |  Field in **PERIMIN** defining the maximum distance measured in the increasing direction of the perpendicular axis. The default field name is **DPLUS** , which will be used if it exists in the **PERIMIN** file. |  PERIMIN |  No |  Numeric |  Undefined  
DMINUS |  Field in **PERIMIN** defining the maximum distance measured in the decreasing direction of the perpendicular axis. The default field name is **DMINUS** , which will be used if it exists in the **PERIMIN** file. |  PERIMIN |  No |  Numeric |  Undefined  
ATTRIB1 |  Field from the perimeter file to be placed into the output model file. This may be a multi- word alpha field. |  PERIMIN |  No |  Numeric |  Undefined  
ATTRIB2 |  Second field from the perimeter file to be placed into the output model file. |  PERIMIN |  No |  Numeric |  Undefined  
ATTRIB3 |  Third field from the perimeter file to be placed into the output model file. |  PERIMIN |  No |  Numeric |  Undefined  
ATTRIB4 |  Fourth field from the perimeter file to be placed into the output model file. |  PERIMIN |  No |  Numeric |  Undefined  
ATTRIB5 |  Fifth field from the perimeter file to be placed into the output model file. |  PERIMIN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MODE |  |  Option |  Description  
---|---  
(0) |  Fill perimeters with regular [sub] cells [as FP subcommand in the Model Editor].  
No |  0 |  0,3 | 0,1,2,3  
DPLUS |  The maximum distance measured in the increasing direction of the perpendicular axis. |  No |  Undefined |  Undefined | Undefined  
DMINUS |  The maximum distance measured in the decreasing direction of the perpendicular axis. |  No |  Undefined |  Undefined | Undefined  
PLANE |  Plane in which perimeters are to be filled. Either 'XY' [plan] or 'XZ' [E-W section] or 'YZ' [N-S section]. The default is 'XY'. |  No |  'XY' |  Undefined | 'XY', 'XZ', 'YZ'  
ZONE |  Value to be inserted in the ZONE field (0). The latter is created if there is no perimeter file or if ATTRIB1-5 are not specified. |  No |  0 |  Undefined | Undefined  
OPTIMISE |  Optimise combination of cells to minimise number of subcells (2). |  Option |  Description  
---|---  
0 |  No combining of subcells.  
1 |  Combine subcells only if they form a complete parent cell.  
2 |  Combine subcells to form minimum number of subcells.  
No |  2 |  0,2 |  0,1,2  
FULLCELL |  Controls splitting of cells perpendicular to the plane of the perimeter. |  Option |  Description  
---|---  
(0) |  \- split cells at projection distance.  
1 |  \- projection distance will be rounded to the nearest parent cell boundary.  
No |  0 |  0,1 |  0,1  
XSUBCELL |  Cell division in X direction (1). Max 100. |  No |  1 |  1,100 |  Undefined  
YSUBCELL |  Cell division in Y direction (1). Max 100. |  No |  1 |  1,100 |  Undefined  
ZSUBCELL |  Cell division in Z direction (1). Max 100. |  No |  1 |  1,100 |  Undefined  
PVALUE |  PVALUE of single perimeter to be selected from the **PERIMIN** file. |  No |  Undefined |  Undefined |  Undefined  
RESOL |  Defines boundary resolution if **MODE** >0 |  Option |  Description  
---|---  
(0) |  \- precise boundary location.  
N |  \- boundary rounded to nearest 1/Nth of parent cell size.  
No |  0 |  Undefined |  Undefined  
OVCHECK |  |  Option |  Description  
---|---  
0 |  \- assumes perimeters do not overlap (i.e. duplicate cells can be created).  
(1) |  \- check for overlapping perimeters.  
No |  1 |  0,1 |  0,1  
  
## Example
    
    
    !PERFIL &PROTO(PROTOMOD), &MODEL(MODEL1), &PERIMIN(PERIMS),   
  
---  
      
    
    *ATTRIB1(ZONE), *ATTRIB2(ROCKTYPE), @MODE=1,   
      
    
    @PLANE= `XZ', @ZSUBCELL=3, @RESOL= 20.  
  
## Error and Warning Messages

**Message** |  Description  
---|---  
>>> INVALID MODE - WRONG SEAM DIRECTION <<< |  The selected @MODE is not consistent with @PLANE.  
>>> &PERIMIN FIELD ERRORS <<< |  A field is missing or contains an invalid data type (i.e. alphanumeric instead of numeric). Check the fields XP, YP, ZP, PVALUE, PTN, DPLUS, DMINUS.  
>>> &PROTO FILE ERROR <<< |  The model prototype file does not exist or has been corrupted.  
>>> &PROTO FIELD ERRORS <<< |  A field is missing or contains an invalid data type (i.e. alphanumeric instead of numeric). Check the fields IJK, XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ.  
>>> &MODEL FIELD ERRORS <<< |  A field is missing or contains an invalid data type (i.e. alphanumeric instead of numeric). Check the fields IJK, XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ.  
>>> TOO MANY POINTS IN PERIMETER <<< |  The storage space allocated during process installation is insufficient. Either reduce the number of points in the perimeter or have the allocated storage space in the process increased.  
  
Related topics and activities

  * [TRIFIL Process](<trifil.md>)

  * [WIREFILL Process](<wirefill.md>)