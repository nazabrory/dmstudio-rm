# CONTOU Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CONTOU** and click **Run**.
  * Enter "CONTOU" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CONTOU>).

## Process Overview

Generates a contour plot file from an orebody model.

Four different types of contours are possible.

The required contour is chosen by specifying the appropriate parameter(s) from the set @**PLANE** (defining the plane of the contour as 'XY', 'XZ', or 'YZ'); @POSITION (defining the position within the plane at which a contour is required); @**TOP** (defining the top of a seam); and @BOTTOM (defining the bottom of a seam). The choices are:-

  1. For conventional contours, choose @**PLANE** = 'XY', 'XZ' or 'YZ', and then the position in this plane. For the XY plane, @**POSITION** is the required elevation (ZC value). For the XZ plane, @**POSITION** is the required Y co-ordinate (**YC** value). For the YZ plane, @**POSITION** is the required X co-ordinate (XC value). Neither @**TOP** nor @**BOTTOM** are set. The field * **FIELD** defines the field whose values will be contoured at the given position.

  2. For top of seam contours, @**PLANE** = 'XY' (default). @TOP is set to the value of field * **FIELD** defining the required seam. Neither @**BOTTOM** nor @**POSITION** are set.

  3. For bottom of seam contours, @**PLANE** = 'XY' (default). @**BOTTOM** is set to the value of field * **FIELD** defining the required seam. Neither @TOP nor @**POSITION** are set.

  4. For seam isopachs, @**PLANE** = 'XY' (default). @**TOP** and @**BOTTOM** are set to the value of field * **FIELD** defining the required seam. @POSITION is not set.

## Macro Syntax Examples

Here's an example of a full **CONTOU** macro:
    
    
    !CONTOU &IN(FEMODEL),   
  
---  
      
    
    &PLOT(CONTPLOT), *FIELD(Fe), @POSITION=-45, @VMIN= 30, @VMAX=80,   
      
    
    @CINT=5, @GRIDINT=10, @HILIGHT=5, @HI= 4  
  
The following information relates to the **POSITION** and **FIELD** settings, and what they do:
    
    
    @POSITION=-45,*FIELD(Fe)

The contour will pick all those cells or sub-cells which cross the xy plane at -45, and will contour Fe.
    
    
    @TOP=2,*FIELD(SEAMID)

The contour will be generated from the top of the seam identified by field SEAMID=2.
    
    
    @BOTTOM=2,*FIELD(SEAMID)

The contour will be generated from the base of the seam identified by field SEAMID=2.
    
    
    @TOP=2,@BOTTOM=2,*FIELD(SEAMID)

An isopach of seam **SEAMID** =2.

The smoothness of the contour may be controlled by parameter @**GRIDINT**. This defines the grid interval at which points will be sampled or generated for contour threading. It should be set to the grid size (in user data units) or less, preferably a sub-multiple of the grid size. You are recommended to start with @**GRIDINT** equal to half of the grid spacing (the smaller of X or Y, if different). Note, however, that the appearance of the contours will once again get worse if the interval is too small, because of the linear interpolation used between points.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. Must contain fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK, FIELD**. |  Input |  Yes |  Block Model  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. If no plot prototype file, then **XMIN, XMAX, YMIN, YMAX** taken from the model file on **IN**. |  Input |  No |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FIELD |  Field to be contoured. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VMIN |  Minimum contour value. |  Yes |  Undefined |  Undefined |  Undefined  
VMAX |  Maximum contour value. |  Yes |  Undefined |  Undefined |  Undefined  
CINT |  Contour interval. |  Yes |  Undefined |  Undefined |  Undefined  
GRIDINT |  Grid interval for contouring. |  Yes |  Undefined |  Undefined |  Undefined  
PLANE |  Plane, 'XY', 'XZ' or 'YZ' through the model. Default is the **XY** plane. |  No |  'XY' |  Undefined |  'XY','XZ','YZ'  
POSITION |  Position of the plane. For example if the **XY** plane is used a Z position is needed. Only required if neither **TOP** nor **BOTTOM** are specified. |  No |  Undefined |  Undefined |  Undefined  
TOP |  Value of **FIELD** for which top of seam contour required. Only required if neither **POSITION** nor **BOTTOM** appear. |  No |  Undefined |  Undefined |  Undefined  
BOTTOM |  Value of FIELD for which base of seam contour required. Only required if neither **POSITION** nor TOP appear. Both TOP and **BOTTOM** set for an isopach. |  No |  Undefined |  Undefined |  Undefined  
HILIGHT |  Highlight every Nth contour with different colour. |  No |  Undefined |  Undefined |  Undefined  
HI |  Colour for highlighting. |  No |  Undefined |  1,64 |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of **X** for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of **X** for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of **Y** for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of **Y** for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  **X** scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  **Y** scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Error and Warning Message

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE.  
>>> A NEW OUTPUT FILE WILL BE CREATED. |  The @APPEND parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES  
>>> NOT CONTAIN ALL THE REQUIRED FIELDS.  
>>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @APPEND parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.