# WFCODE Process  
  
To access this process:

  * Enter "WFCODE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **WFCODE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WFCODE>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**WFCODE** codes points in a file that are constrained by one or more wireframes. 

The **POINTS** file to be coded must have X, Y and Z coordinate fields. The **WIRETR** file may contain a **ZONE** field to identify individual wireframes. The **ZONE** field may also be used as an attribute to code the points. 

An optional perimeter file can be supplied to constrain coding of points to be inside or outside perimeters.

An example of the use of **WFCODE** is for coding drillhole samples with wireframe domains or model cells with classification wireframes (e.g.rocktypes)

The POINTS file

The input **POINTS** file contains the point records with X, Y and Z coordinates to be coded by the wireframes. This file may be a standard desurveyed drillhole (X,Y,Z), block model (XC,YC,ZC), or point data (XPT,YPT,ZPT) file

#### The WIRETR and WIREPT files

The wireframe file is compulsory and is used to define the volume(s) within which points must reside to be coded. The wireframe can consist of:

  * A single closed surface.
  * Several separate closed surfaces, each optionally identified with a ZONE field.
  * A single DTM surface.
  * Two DTM surfaces

#### The PERIMIN file

The input perimeter file is optional. If it is specified only points lying inside or outside the perimeter(s) in the file is coded depending on the value of the @OUTSIDE parameter.

#### The X,Y and Z fields

The X,Y and Z fields are used to specify the name of the X, Y and Z coordinate fields in the input POINTS data file.

#### The OUT file

The output file contains the coded values. If the **ALLPTS** parameter is set to 1 then it will contain all the records (subject to any retriueval criteria) that are in the input **POINTS** file. The points that are not selected by the wireframes will have unchanged or absent coded values according to the **SETABSNT** parameter. If the **ALLPTS** parameter is set to zero then the **OUT** file will only contain the coded values that have been selected by the wireframe (and optional perimeter(s))

#### The ZONE field

The optional **ZONE** field can be used to define a field that identifies separate wireframe surfaces in the input wireframe file. The field must exist in the input wireframe file. If specified, **ZONE** values are written to the output file.

#### The ATTRIB fields

The optional **ATTRIB**[1234] fields can be used as code values. They must exist in the input wireframe file and if specified their vlaues are transferred to the output coded points file.

#### The CODE parameter

The **CODE** parameter defines how the wireframes are treated in order to determine which points are to be coded. It can have the following values:

=1 : Code points above a DTM surface.

=2 : Code points below a DTM surface.

=3 : Code points inside a solid.

=4 : Code points outside a solid.

=5 : Code points above a wireframe surface.

=6 : Code points below a wireframe surface.

=7 : Code points between two wireframe surfaces.

=8 : Code points outside two wireframe surfaces..

These options are the same as in the SELWF process

CODE = 1, 2, 5, 6, 7, 8

Points which lie above or below the surface, but which are outside the surface boundary, will not be coded/selected.

CODE = 4

An _outside_ point is outside all wireframe volumes/solids. Attribute fields will not be copied. The output ZONE field will contain absent values.

Setting ALLPTS to a value of 1, to copy all points to the output file, is not allowed.

#### The ALLPTS parameter

The **ALLPTS** parameter defines whether all the records from the input **POINTS** file (subject to any retrieval criteria) are copied to the OUT file, or just those selected by the wireframe.

Permissible values are:

=0 : Copy only the coded points.

=1 : Copy all the points to the output file. The coded points are flagged with the ZONE field values or the attributes.

By using **ALLPTS** =0 the **WFCODE** process can be used to create a file with just those points selected by the wireframe. The advantage of using **WFCODE** over **SELWF** is that the **CHECKROT** parameter can be used to check for rotated models as well as optionaly additionally selecting inside or outside a perimeter.

#### The SETABSNT parameter

The **SETABSNT** parameter controls whether the **ZONE** and attribute values, if they exist in the input **POINTS** file, are set to absent before processing or left unchaged

Permissible values are:

=0 : Do not set the **ZONE** and attribute values to absent before porocessing (Default)

=1 : Set the **ZONE** and attribute values to absent before porocessing.

The **EXCLUDE** and **TOLERANC** parameters

Exclude points that fall on, or within **TOLERANC** , of the wireframe surface.

=0 : Do not exclude points (Default).

=1 : Exclude points to be coded that are within **TOLERANC** of a DTM surface.

#### The CHECKROT parameter: Rotated models

The input points file may be a rotated model. If the **CHECKROT** parameter is set to 1 and if the input file is determined to be a rotated model (it contains the fields **ANGLE1, ANGLE2, ANGLE3, X0, Y0, Z0, ROTAXIS1, ROTAXIS2, ROTAXIS3**) as defined using the **PROTOM** process, then the coordinates of the input points in the &**WIREPT** and **PERIMIN** files are automatically transformed to the rotated model coordinate system during processing.

Permissible values are:

=0 : Do not check for a rotated model.

=1 : Do check for a rotated model.

#### The OUTSIDE parameter

The OUTSIDE parameter is only relevant if an optional perimeter (**PERIMIN**) file is being used to additionally restrict the coding of points to being inside or outside perimeters.

Permissible values are:

=0 : Code only points that lie inside the perimeters in the **PERIMIN** file (Default).

=1 : Code only points that lie outside the perimeters in the **PERIMIN** file.

This option may be useful if you are coding points within classification surfaces but also wish to constrain the coding according to lease or mining exclusion boundaries.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
POINTS |  Input file containing X, Y and Z coordinates to be updated with values from wireframes. This file may be a block model, desurveyed sample file or any points file with X,Y,Z coordinates. |  Input |  Yes |  Point Data  
WIRETR |  Input wireframe triangle file used to define the volume(s) within which to update the input points with new values. |  Input |  Yes |  Wireframe Edges Data  
WIREPT |  Input wireframe point file used to to define the volume(s) within which to update the input points file with new values |  Input |  Yes |  Wireframe Vertices  
Data  
PERIMIN |  Optional perimeter input file to control area over which input points are considered. Only points either inside or outside the supplied perimeters are coded depending on the value of the @**OUTSIDE** parameter. |  Input |  No |  String Data  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Wireframe Triangle |  Output point data file containing the coded values. This is a copy of the input point data file with extra fields added from the wireframe file. If the input point data file already contains fields that are being coded then values within volumes defined by the wireframes are overwritten.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field in **POINTS** file defining the X co-ordinate. |  POINTS |  Yes |  Numeric |  -  
Y |  Field in **POINTS** file defining the Y co-ordinate. |  POINTS |  Yes |  Numeric |  -  
Z |  Field in **POINTS** file defining the Z co-ordinate. |  POINTS |  Yes |  Numeric |  -  
ZONE |  Field in **WIRETR** file used to identify individual surfaces. **WIRETR** does NOT have to be sorted by **ZONE**. This field can be alpha or numeric |  WIRETR |  No |  Numeric or Alphanumeric |  -  
ATTRIB1 |  Field from the **WIRETR** file to be placed into the output file for all records which are selected. |  POINTS |  No |  Numeric or Alphanumeric |  -  
ATTRIB2 |  Field from the **WIRETR** file to be placed into the output file for all records which are selected. |  POINTS |  No |  Numeric or Alphanumeric |  -  
ATTRIB3 |  Field from the **WIRETR** file to be placed into the output file for all records which are selected. |  POINTS |  No |  Numeric or Alphanumeric |  -  
ATTRIB4 |  Field from the **WIRETR** file to be placed into the output file for all records which are selected. |  POINTS |  No |  Numeric or Alphanumeric |  -  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CODE |  Parameter to define how to treat the input wireframes and code the points =1 : Code points above a DTM surface. =2 : Code points below a DTM surface. =3 : Code points inside a solid. =4 : Code points outside a solid. =5 : Code points above a wireframe surface. =6 : Code points below a wireframe surface. |  Yes |  3 |  1, 8 |  1,2,3,4,5,6,7,8  
ALLPTS |  Set to 1 to copy all the input points to the output file. Set to zero to copy only the points selected by the wireframe. This is ignored if @**CODE** =4 =0 : Copy only the coded points. =1 : Copy all the points to the output file. The coded points are flagged with the **ZONE** field values or the attributes. |  No |  0 |  0, 1 |  0,1  
SETABSNT |  Set the specified **ZONE** and attribute fields in the input points file to absent before processing. =0 : Do not set the **ZONE** and attribute values to absent before processing (Default). =1 : Set the **ZONE** and attribute values to absent before porocessing. |  No |  0 |  0,1 |  0,1  
EXCLUDE |  Exclude points that fall on, or within **TOLERANC** , of the wireframe surface. =0 : Do not exclude points (Default). =1 : Exclude points to be coded that are within **TOLERANC** of a wireframe surface. |  No |  0 |  0,1 |  0,1  
TOLERANC |  Tolerance used to determine whether a data point is 'on' a surface or not. |  No |  0 |  Undefined |  Undefined  
CHECKROT |  Set to 1 to automatically check for and correctly process rotated models when the input points file is a block model. The default value is one. If this is not set to 1 and the model is rotated then the wireframe points need to be transformed into the model coordinate space using **[CDTRAN](<cdtran.md>)** before running **[TRIFIL](<trifil.md>)**. =0 : Do not check for input rotated model. If the input model is rotated assume wireframe points are in the rotated space. =1 : Automatically check for an input rotated model and internally transform wireframe points. |  No |  1 |  0,1 |  0,1  
OUTSIDE |  Used if **PERIMIN** has been defined to only code points inside or outside perimeters. =0 : Code only points that lie inside the perimeters in the **PERIMIN** file (Default). =1 : Code only points that lie outside the perimeters in the **PERIMIN** file. |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !WFCODE &MODEL(&POINTS(_vb_mod1), &WIRETR(_vb_mintr),  
  
---  
      
    
    &WIREPT(_vb_minpt),&PERIMIN(wfcode_str),  
      
    
    &OUT(vbout),*X(XC),*Y(YC),*Z(ZC),*ZONE(ZONE),*ATTRIB1(COLOUR),  
      
    
    *ATTRIB2(LINK),@CODE=3.0,@SETABSNT=1.0,@EXCLUDE=0.001,  
      
    
    @TOLERANC=1.0,@CHECKROT=1.0,@OUTSIDE=1.0  
  
Related topics and activities

  * [CDTRAN Process](<cdtran.md>)

  * [TRIFIL Process](<trifil.md>)