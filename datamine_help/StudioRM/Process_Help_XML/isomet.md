# ISOMET Process  
  
To access this process:

  * Enter "ISOMET" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ISOMET** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#ISOMET>).

## Process Overview

Generates a plot file of an isometric view of a wireframe surface from a block model, from a user-defined viewpoint, described by rotation and elevation angles.

Four different types of surface may be viewed:

  1. Grade surface of a defined field at a chosen level.

  2. Top of seam structure.

  3. Bottom of seam structure.

  4. Seam isopach (top minus bottom of seam).

The required surface is chosen by specifying the appropriate parameter(s) from the set @**PLANE** (defining the plane of the surface as 'XY', 'XZ', or 'YZ'); @**POSITION** (defining the position within the plane at which a grade surface is required); @**TOP** (defining the top of a seam); and @**BOTTOM** (defining the bottom of a seam). The choices are:-

  1. For conventional grade surfaces, choose @**PLANE** ='XY', 'XZ' or 'YZ', and then the position in this plane. For the XY plane, @**POSITION** is the required elevation (ZC value). For the XZ plane, @**POSITION** is the required Y co-ordinate (YC value). For the YZ plane, @**POSITION** is the required X co-ordinate (XC value). Neither @**TOP** nor @**BOTTOM** are set. The field * **FIELD** defines the field whose values will define the surface at the given position.

  2. For top of seam surfaces, @**PLANE** ='XY' (default). @**TOP** is set to the value of field * **FIELD** defining the required seam. Neither @**BOTTOM** nor @**POSITION** are set.

  3. For bottom of seam surfaces, @**PLANE** ='XY' (default). @**BOTTOM** is set to the value of field * **FIELD** defining the required seam. Neither @**TOP** nor @**POSITION** are set.

  4. For seam isopach surfaces, @**PLANE** ='XY' (default). @**TOP** and @**BOTTOM** are set to the value of field * **FIELD** defining the required seam. @**POSITION** is not set.

Scaling in this program is entirely automatic, thus X and Y minima, maxima, and scales need not be defined even in the prototype. If they are defined, the ISOMET process will merely substitute its own internally generated parameters.

Progress messages are displayed as the model is read and as each column of the isometric view is completed.

#### Process Examples
    
    
    @POSITION=-45,*FIELD(Fe)

The surface will pick all those cells or sub-cells which cross the XY plane at -45, and will show Fe grades.
    
    
    @TOP=2,*FIELD(SEAMID)

The surface will be generated from the top of the seam identified by field _SEAMID_ =2.
    
    
    @BOTTOM=2,*FIELD(SEAMID)

The surface will be generated from the base of the seam identified by field _SEAMID_ =2.
    
    
    @TOP=2,@BOTTOM=2,*FIELD(SEAMID)

An isopach surface of seam _SEAMID_ =2.

The smoothness of the surface may be controlled by parameter @**GRIDINT**. This defines the grid interval at which points will be sampled or generated for the surface mesh. It should be set to the grid size (in user data units) or less, preferably a sub-multiple of the grid size. You are recommended to start with @**GRIDINT** equal to half of the grid spacing (the smaller of X or Y, if different). Note, however, that the appearance of the surface will once again get worse if the interval is too small, because of the linear interpolation used between points.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. Must contain fields XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK + FIELD field. |  Input |  Yes |  Block Model  
PROTO |  Plot prototype file. Must contain the fields X, Y, S1, S2 and CODE (numeric, explicit) and XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE, XORIG, YORIG, XRT, YTP, XPICRT, YPICTP (numeric, implicit). Only the values of fields XORIG, YORIG, XRT, YTP, XPICRT and YPICTP are used. If no PROTO file entered, scaling is fully automatic. |  Input |  No |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot File |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FIELD |  Field to be plotted. |  IN |  Yes |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VMIN |  Minimum mesh value. |  Yes |  Undefined |  Undefined |  Undefined  
VMAX |  Maximum mesh value. |  Yes |  Undefined |  Undefined |  Undefined  
VERTEXAG |  Vertical exaggeration required. |  Yes |  Undefined |  Undefined |  Undefined  
GRIDINT |  Grid interval for mesh. |  Yes |  Undefined |  Undefined |  Undefined  
ROTATE |  The rotation angle in degrees horizontally of the viewpoint, clockwise from the model Y axis (45). |  No |  45 |  0,360 |  Undefined  
ELEVATE |  The rotation angle in degrees vertically of the viewpoint, upwards from model X-Y plane (45). |  No |  45 |  -90,90 |  Undefined  
PLANE |  Plane, 'XY', 'XZ' or 'YZ' through the model. Default is the XY plane. |  No |  'XY' |  Undefined |  'XY','XZ','YZ'  
POSITION |  Position of the plane. For example if the XY plane is used a Z position is needed. Only required if neither TOP nor BOTTOM are specified. |  No |  Undefined |  Undefined |  Undefined  
TOP |  Value of FIELD for which top of seam surface required. Only required if neither POSITION nor BOTTOM appear. |  No |  Undefined |  Undefined |  Undefined  
BOTTOM |  Value of FIELD for which base of seam surface required. Only required if neither POSITION nor TOP appear. Both TOP and BOTTOM set for an isopach. |  No |  Undefined |  Undefined |  Undefined  
PXMIN |  Minimum X value for area covered by mesh. |  No |  Undefined |  Undefined |  Undefined  
PXMAX |  Maximum X value for area covered by mesh. |  No |  Undefined |  Undefined |  Undefined  
PYMIN |  Minimum Y value for area covered by mesh. |  No |  Undefined |  Undefined |  Undefined  
PYMAX |  Maximum Y value for area covered by mesh. |  No |  Undefined |  Undefined |  Undefined  
XINC |  Grid increment on the X axis. Default is PXMAX- PXMIN. |  No |  Undefined |  Undefined |  Undefined  
YINC |  Grid increment on the Y axis. Default is PYMAX- PYMIN. |  No |  Undefined |  Undefined |  Undefined  
ZINC |  Grid increment on the Z axis. Default is VMAX- VMIN. |  No |  Undefined |  Undefined |  Undefined  
NDX |  Number of decimal places for grid annotation on the X axis (0). |  No |  0 |  Undefined |  Undefined  
NDY |  Number of decimal places for grid annotation on the Y axis (0). |  No |  0 |  Undefined |  Undefined  
NDZ |  Number of decimal places for grid annotation on the Z axis (0). |  No |  0 |  Undefined |  Undefined  
COLINT |  Mesh interval for colour. If 0 then all of mesh is plotted in (0). |  No |  0 |  Undefined |  Undefined  
COLST |  Start colour for mesh (1). |  No |  1 |  1,64 |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). N.B. Scaling is fully automatic in this process. |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !ISOMET   &IN(FEMODEL), &PLOT(ISOMPLOT), *FIELD(Fe),  
  
---  
      
    
    @POSITION=-45, @VMIN=30, @VMAX=80, @VERTEXAG=10,   
      
    
    @ROTATE=50,   
      
    
             @ELEVATE=60, @GRIDINT=10  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE.  
>>> A NEW OUTPUT FILE WILL BE CREATED. |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced. |   
>>> ERROR \- CANNOT APPEND TO PLOT FILE AS IT DOES  
>>> NOT CONTAIN ALL THE REQUIRED FIELDS.  
>>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced. |