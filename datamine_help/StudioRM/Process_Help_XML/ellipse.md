# ELLIPSE Process  
  
To access this process:

  * Estimate ribbon >> Estimate >> Ellipse

  * **Model** ribbon **> > Estimate >> Ellipse**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ELLIPSE** and click **Run**.
  * Enter "ELLIPSE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ELLIPSE>)](<../command_help/_COMMAND%20TABLE_A.md#ACCMLT>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

This process can be used to generate an ellipsoid wireframe and/or an ellipsoid point file.

The lengths of the axes and the orientation of the generated ellipsoid (point- or wireframe-type) can be defined either through a search volume parameter file, as used for input to the **[ESTIMA](<estima.md>)** process, or by parameter. Although the description here is in terms of a search volume ellipsoid, the ellipsoid could also represent the anisotropic ranges of a variogram model.

Output ellipsoid data can be loaded into a 3D window and used to verify that the lengths of the axes and the orientation are as expected, in reference to other data. This is true for either the output wireframe (pt/tr) or the **[ellipse data point file](<../STUDIO_RM/Ellipsoids_Overview.md>)** , if one is generated.

There are three components to the wireframe, each with a different value for field ZONE in the triangle file:

1 - The outside surface of the ellipsoid;

2 - The three planes parallel to the axes of the ellipsoid;

3 - A set of axes for the world coordinate system.

If wireframe data is generated, each octant of the ellipsoid is created using a different field (1 to 8), and the axes are 13. Therefore you can use the **filter-wireframe-triangles** (fwt) command or similar filtering mechanisms to select components of the wireframe.

The coordinates of the centre of the ellipsoid can be defined using the @**XCENTRE** , @**YCENTRE** and @**ZCENTRE** parameters. The default values of these parameters are zero.

## Generating an Ellipsoid With SRCPARM Input

If a search volume parameter file (**SRCPARM**) is specified, then the definition of the ellipsoid will be taken from this file. If the file contains more than one definition, then the required definition can be selected using the @**SREFNUM** parameter. If the file only contains one definition, and @SREFNUM is set to absent data (the default), then that definition will be used. Details of the search volume parameter file and its fields can be found in the Reference Manual entry for the process **ESTIMA**.

If **SRCPARM** is specified, **VMODEL** is not permitted.

If **SRCPARM** is specified, an output ellipsoid data object is generated and * **WIRETR** and * **WIREPT** are ignored.

## Generating an Ellipsoid With VMODEL Input

As an alternative to **SRCPARM** input, a variogram model file can be used to create an ellipse of the sum of the valid variogram ranges (up to a maximum of 10). Ellipsoid calculation will only consider ranges (**STnPAR1** as Length Y; **STnPAR2** as Length Y, **STnPAR3** as Length Y) including those where STn is set to 1. Essentially, an ellipsoid will be created to enclose the shape of the variogram model.

If **VMODEL** is specified, **SRCPARM** is not permitted.

If **VMODEL** is specified, an output ellipsoid data object is generated and * **WIRETR** and * **WIREPT** are ignored.

## Generating Multiple Ellipsoids

**ZONE** is an optional attribute field (numeric or alphanumeric) in input search volume parameters or variogram model. This creates an output ellipse for each record in the **SREFNUM** and **VREFNUM** , and **ZONE** is assigned to the output wireframe or ellipsoid. If **ZONE** is set, parameters **SREFNUM** and **VREFNUM** are ignored.

When multiple ellipsoids are generated, **CENTRE** determines where each ellipsoid is positioned in 3D space. If multiple ellipsoids are created and no **CENTRE** file is specified, all ellipsoids are generated with the same centroid location.

**CENTRE** is used with **SRCPARM** or **VMODEL** is defined and a field **ZONE** is specified. It must contain a **ZONE** field matching **SRCPARM** or **VMODEL** contents. If set, parameters **XCENTRE** , **YCENTRE** and **ZCENTRE** are ignored as the midrange position of coordinates in that file (for the designated **ZONE**) is used for the corresponding ellipsoid, if multiple coordinate records per **ZONE** exist. An example input could be a table of coordinate positons for each **ZONE** where ellipsoids are centred or a drillhole file where each ellipsoid is centred at the midrange of the sample positions.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SRCPARM |  Input search volume parameter file, as used in the ESTIMA process. This file must contains the fields SREFNUM, SANGLE1, SANGLE2, SANGLE3, SAXIS1, SAXIS2, SAXIS3, SDIST1, SDIST2, and SDIST3, which define the orientation and dimensions of the search volume. If SRCPARM is specified, VMODEL is not permitted. |  Input |  No |  Undefined  
VMODEL |  Input search volume parameter file, as used in the ESTIMA process. This file must contains the fields SREFNUM, SANGLE1, SANGLE2, SANGLE3, SAXIS1, SAXIS2, SAXIS3, SDIST1, SDIST2, and SDIST3, which define the orientation and dimensions of the search volume. If VMODEL is specified, SRCPARM is not permitted. |  Input |  No |  Undefined  
CENTRE |  Optional input file for the centre position of each ellipsoids. IF a ZONE field is used, CENTRE must match ZONE field in SRCPARM or VMODEL.  If set, parameters XCENTRE, YCENTRE and ZCENTRE are ignored. If multiple coordinate records in file or per ZONE exist, the midrange coordinate is used.  An example input could be a table of coordinate positions for each ZONE where ellipsoids should be centred or a drillhole file where each ellipsoids is centred at the midrange of the sample positions. | Input | No | Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETR |  Output |  No |  Wireframe Triangle File |  Optional output wireframe triangle file. If this file is not specified a file with the name ELTR will be created. The wireframe will be created to enclose the limits of the input search or variogram model.  
WIREPT |  Output |  No |  Wireframe Points File. |  Optional output wireframe points file.   
ELLIPSE |  Output |  No |  Ellipsoid File. |  Optional output ellipsoid file. The wireframe will be created to enclose the limits of the input search or variogram model. Also see "Generating Multiple Ellipsoids", above.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ZONE |  An optional attribute field (numeric or alphanumeric) in the input search volume parameters or variogram model.  This creates an output ellipse for each record in the **SREFNUM** and **VREFNUM** , and **ZONE** is assigned to the output wireframe or ellipsoid.  If **ZONE** is set, parameters **SREFNUM** and **VREFNUM** are ignored. If input file **CENTRE** with matching **ZONE** is set, ellipsoids are positioned at midrange of input data |  SRCPARM or VMODEL |  No |  Any |  Undefined  
X/Y/Z | Field in input CENTRE file that defines the X/Y/Z coordinate. | CENTRE |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SREFNUM |  If a search volume parameter file (SRCPARM) is specified, then it must include a field SREFNUM which defines a unique reference number for each search volume. The SREFNUM parameter then defines which search volume will be used. If the SREFNUM parameter is set to absent data (the default), then the first search volume in the file will be used. |  No |  - |  Undefined |  Undefined  
VREFNUM |  If a variogram model (VMODEL) is specified, then it must include a field VREFNUM which defines a unique reference number for each variogram model. The VMODEL parameter then defines which variogram model will be used. If the VREFNUM parameter is set to absent data (the default), then the first variogram model in the file will be used. |  No |  - |  Undefined |  Undefined  
SANGLE1 |  First rotation angle clockwise in degrees, around axis SAXIS1 . It must lie between -360.0 and +360.0. A value of zero indicates no rotation. |  No |  0 |  -360,360 |  Undefined  
SANGLE2 |  Second rotation angle clockwise in degrees, around axis SAXIS2 . It must lie between 360.0 and +360.0. A value of zero indicates no rotation. |  No |  0 |  -360,360 |  Undefined  
SANGLE3 |  Third rotation angle clockwise in degrees, around axis SAXIS3 . It must lie between -360.0 and +360.0. A value of zero indicates no rotation. |  No |  0 |  -360,360 |  Undefined  
SAXIS1 |  Axis around which first rotation angle will occur. 0 for no rotation, 1 for X axis, 2 for Y axis, 3 for Z axis. |  No |  3 |  0,3 |  0,1,2,3  
SAXIS2 |  Axis around which second rotation angle will occur. 0 for no rotation, 1 for X axis, 2 for Y axis, 3 for Z axis. |  No |  1 |  0,3 |  0,1,2,3  
SAXIS3 |  Axis around which third rotation angle will occur. 0 for no rotation, 1 for X axis, 2 for Y axis, 3 for Z axis. |  No |  3 |  0,3 |  0,1,2,3  
SDIST1 |  The length of the first axis of the ellipsoid. Initially, before any rotation, SDIST1 is along the X axis. |  No |  10 |  Undefined |  Undefined  
SDIST2 |  The length of the second axis of the ellipsoid. Initially, before any rotation, SDIST2 is along the Y axis. |  No |  10 |  Undefined |  Undefined  
SDIST3 |  The length of the third axis of the ellipsoid. Initially, before any rotation, SDIST3 is along the Z axis. |  No |  10 |  Undefined |  Undefined  
XCENTRE |  The X coordinate of the centre of the ellipsoid. Not used if file **CENTRE** and field **ZONE** specified. |  No |  0 |  Undefined |  Undefined  
YCENTRE |  The Ycoordinate of the centre of the ellipsoid. Not used if file **CENTRE** and field **ZONE** specified. |  No |  0 |  Undefined |  Undefined  
ZCENTRE |  The Z coordinate of the centre of the ellipsoid. Not used if file **CENTRE** and field **ZONE** specified. |  No |  0 |  Undefined |  Undefined  
PRINT |  Print flag: =0 for minimum output. =1 for runtime information messages. |  No |  0 |  0,1 |  0,1  
  
## Example

Create a wireframe ellipsoid corresponding to search volume reference number 7 in file SPAR1:
    
    
    !ELLIPSE &SRCPARM(SPAR1), &WIRETR(WTR1), &WIREPT(WPT1),         @SREFNUM=7, @PRINT=0.0  
  
---  
  
Create a wireframe ellipsoid which is rotated 30o around axis 1 (X), followed by 60o around axis 3 (Z). The lengths of the axes are 100m along axis 1, 50m along axis 2, and 20m along axis 3. 
    
    
    !ELLIPSE &WIRETR(WTR1), &WIREPT(WPT1), @SANGLE1=30, @SANGLE2=60,   
  
---  
      
    
       
      
    
            @SAXIS1=1, @SAXIS2=3,  
      
    
    @SDIST1=100, @SDIST2=50, @SDIST3=20,  
      
    
    @PRINT=0.0  
  
## Error and Warning Messages

Message |  Description  
---|---  
ERROR: SRCPARM file FFFFFFFF does not exist. |  Search volume parameter file FFFFFFFF has been specified, but it does not exist.  
ERROR: No records in SRCPARM file FFFFFFFF. |  Search volume parameter file FFFFFFFF has been specified, and it exists, but it does not contain any records.  
ERROR: SRCPARM file FFFFFFFF does not include field SREFNUM. |  Search volume parameter file FFFFFFFF has been specified, and it exists and contains records, but it does not contain field SREFNUM .  
ERROR: file FFFFFFFF does not contain SREFNUM=SSSSSSSS. |  Search volume parameter file FFFFFFFF has been specified, and it exists and contains records and has a field SREFNUM, but none of the values for field SREFNUM are equal to SSSSSSSS.   
ERROR: one of the following fields is missing from FFFFFFFF.  
SDIST1, SANGLE1, SAXIS1  
SDIST2, SANGLE2, SAXIS2  
SDIST3, SANGLE3, SAXIS3 |  Search volume parameter file FFFFFFFF has been specified, and it exists and contains records, but one or more of the fields shown above are missing.  
ERROR: SANGLEn is specified as NNNNNN.NN. |  It must lie between -360 and +360.The SANGLEn parameter has been specified with an invalid value.  
ERROR: Rotation axis n has been specified as R. |  Only values 0, 1, 2 or 3 are permitted.  
An invalid value for parameter SAXISn has been specified.  
  
ERROR: parameter SDISTn is missing or is less than zero. |  All three SDISTn parameters must be specified and must be greater than zero.  
ERROR in Process ELLIPSE >>> PRESS <RETURN> TO CONTINUE (OR ! TO TERMINATE) > |  An error has occurred. An unidentifiable error has been encountered.