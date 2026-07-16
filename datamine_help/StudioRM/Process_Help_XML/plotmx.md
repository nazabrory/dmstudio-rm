# PLOTMX Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTMX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTMX** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTMX>).

## Process Overview

Plots the intersection of a block model with any plane.

The plane may be specified by its centre, size, azimuth and dip; end points and vertical limits of a vertical section; corner points and RL for a plan; or a section from a standard section definition file. The polygonal outlines, representing the intersections with model cells and sub-cells, may be colored using a model file field; shaded or solid colour filled using intervals on a model file field with an optional legend; or annotated with one or more field values or a symbol.

Features of **PLOTMX** include; shrinking of block outlines; annotation of up to 10 fields offset from one of 5 reference positions; default and user defined titles; icon showing the orientation of the plane; legend; plotting of grids and control of character size and color for annotations, titles and other plot components.

**PLOTMX** may be used for reproducing views of a block model with additional annotation options. Plots from **PLOTMX** are particularly useful for superimposing when creating outlines for underground design and stope evaluation. It adds to Datamine the ease of producing views of a block model on any general plane.

The process will accept a block model which has been defined using the Rotated Model option in **[PROTOM](<protom.md>)**. A message will be displayed to show that the model has been identified as having the reserved Rotated Model fields. The main restrictions when using rotated models are that the position of the annotation must be relative to the cell centre, and vertical exaggeration is not permitted.

Note: A 'box' is defined as the intersection of the specified plane with a model cell or sub-cell. Such boxes may be irregular in shape if the plane is oblique.

## Input Files 

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. This must contain the fields XC, YC, **ZC, XINX, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK**. If it is a Rotated Model then it must also include the fields **X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2, ROTAXIS2**. |  Input |  Yes |  Block Model  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2, CODE, (numeric, explicit) and XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
SECTION |  Optional section definition file. Must contain the fields **SVALUE,XCENTRE,YCENTRE, ZCENTRE,SDIP,SAZI,DPLUS,DMINUS,HSIZE,VSIZE** |  Input |  No |  Section Definition  
ANNFILE |  Optional annotation input file for specifying annotations as an alternative to the interactive input. Only used if the **ANNOTATE** =1.  Compulsory fields: 

  * **FIELD** A8- Field to annotate. 
  * **CHARSIZE** N - Annotate character size. 
  * **N** \- Annotate colour. 
  * **XOFFSET** N - X offset in mm. 
  * **YOFFSET** N - Y offset in mm. 
  * **ANGLE** N - Angle of annotation. 
  * **NDP** N - Number of decimal places. 

Optional fields if **FIELD** is numeric: 

  * **LOWER** N - Lower bound non-inclusive. 
  * **UPPER** N - Upper bound inclusive. 

**LOWER** and **UPPER** define the range on **FIELD** for which the particular annotation will plotted. Special values - and + may be used. |  Input |  No |  Undefined  
LEGEND |  Optional shading legend input file which may be used as an alternative to interactive input. Only used if the **SHADE** =1.  Compulsory fields: 

  * **FIELD** A8- Field to annotate, must be N. 
  * **CODE** N - Fillcode to use for shading. 
  * **LOWER** N - Lower bound non-inclusive. 
  * **UPPER** N - Upper bound inclusive. 

**LOWER** and **UPPER** define the range on **FIELD** for which the particular shading will plotted.  Special values - and + may be used.  Optional fields: 

  * **N** \- Used if CODE is one of 1100 box outline; 1101-1105 hatchings; to set colour otherwise the shading colour is determined from fillcode. 
  * **SHRINK** N - Amount in mm the shaded box will be shrunk inside the true cell outline. If missing and **BOX** =1 then shrink will be set to 2 times the **SHRINK** value.

|  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
MODCOL |  Model colour field, used preferentially for plotting box outline, symbol and pattern shading. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CHARSIZE |  Default character size in millimetres (2). |  No |  2 |  Undefined |  Undefined  
CHARSMIN |  Minimum character size in millimetres (1.3). |  No |  1.3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (1.0). |  No |  1.0 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
FRAME |  |  No |  1 |  0,1 |  0,1  
SHRINK |  box shrink to avoid overplot, in mm (0.5) |  No |  0.5 |  Undefined |  Undefined  
ANNOTATE |  |  No |  0 |  0,1 |  0,1  
ANNCOL |  Default annotation colour (-). |  No |  - |  Undefined |  Undefined  
ANNPOS |  Reference position for annotation offsets (1). If a Rotated Model is used then **ANNPOS** should be set to 1. |  No |  1 |  1,5 |  1,2,3,4,5  
BOX |  |  No |  1 |  0,1 |  0,1  
BOXCOL |  Default box colour (-). |  No |  - |  Undefined |  Undefined  
SHADE |  |  No |  0 |  0,1 |  0,1  
SYMBOL |  Plotted symbol.  Point symbol number:

  * 91 : Circle (o) 
  * 92 : Cross (+) 
  * 93 : Cross (x) 
  * 94 : Triangle 
  * 95 : Box 
  * 96 : Diamond 
  * 97 : Star ( ) 
  * 98 : Pie Segment

|  No |  92 |  Undefined |  Undefined  
SYMSIZE |  Symbol size in millimetres (0). 0 for no symbol. |  No |  0 |  Undefined |  Undefined  
GRCOLR |  Preferred grid colour (-). |  No |  - |  Undefined |  Undefined  
XGRIDINT |  X grid interval, 0 no X grid (0). |  No |  0 |  Undefined |  Undefined  
YGRIDINT |  Y grid interval, 0 no Y grid (0). |  No |  0 |  Undefined |  Undefined  
ZGRIDINT |  Z grid interval, 0 no Z grid (0). |  No |  0 |  Undefined |  Undefined  
XGRIDNDP |  X grid number of decimal places (0). |  No |  0 |  Undefined |  Undefined  
YGRIDNDP |  Y grid number of decimal places (0). |  No |  0 |  Undefined |  Undefined  
ZGRIDNDP |  Z grid number of decimal places (0). |  No |  0 |  Undefined |  Undefined  
ICONSIZE |  Icon size (25). 0 for no icon. |  No |  25 |  Undefined |  Undefined  
ICONCOL1 |  Preferred icon box colour (-). |  No |  - |  Undefined |  Undefined  
ICONCOL2 |  Preferred icon section colour (-). |  No |  - |  Undefined |  Undefined  
TITLE |  |  Option |  Description  
---|---  
0 |  default title only  
1 |  default plus prompted title  
2 |  prompted title only  
3 |  no titles (1).  
No |  1 |  0,3 |  0,1,2,3  
TITCOL |  Preferred title colour (-). |  No |  - |  Undefined |  Undefined  
TITCHS |  Preferred title character size (2). |  No |  2 |  Undefined |  Undefined  
LEGEND |  |  No |  1 |  0,1 |  0,1  
LEGCOL |  Preferred legend colour (-). |  No |  - |  Undefined |  Undefined  
LEGCHS |  Preferred legend character size (-). |  No |  - |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XSCALE |  X scale in user data units per millimetre. If specified here or in **PROTO** this value will override section limits. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. If specified here or in **PROTO** this value will override section limits. |  No |  Undefined |  Undefined |  Undefined  
VERTEXAG |  Controls vertical exaggeration. This must be set to allow different scales. The default is forced equal scales (1). If the input model is a Rotated Model then the process will always set **VERTEXAG** to 1 and display a warning message. = 0 allows different scales for both axes determined by **XSCALE** and **YSCALE** if provided or else by filling the data area to the section limits. > 0 sets value of **XSCALE** /**YSCALE**. = 1 forces equal scales. |  No |  1 |  Undefined |  Undefined  
  
## Examples

### Example 1

This example illustrates the cell annotation features of **PLOTMX**. Two fields are annotated with different character sizes offset from a centered symbol. The plane is a north-south section specified by its end points. The section is scaled into the data are as specified by the plot prototype and the icon is plotted in the margin area:
    
    
    !PROTOP  &OUT(PROTO)  
  
---  
      
    
    1
    
    
    200
    
    
    150
    
    
    10
    
    
    10
    
    
    160
    
    
    110
    
    
    OK
    
    
    !PROTOP  
  
---  
      
    
    1
    
    
    100
    
    
    150
    
    
    10
    
    
    10
    
    
    160
    
    
    110
    
    
    OK
    
    
    !PLOTMX  &IN(MODEL),&PROTO(PROTO),&PLOT(PLOT),   
  
---  
      
    
    @CHARSIZE=1.8,@CHARSMIN=.5,@=1,@FRAME=1, @SHRINK=O.4,@ANNOTATE=1,  
      
    
    @ANNCOL=1,@ANNPOS=1,@BOX=1,@BOXCOL=1,@SHADE=0,@SYMBOL=92,  
      
    
    @SYMSIZE=1.5,@GRCOLR=1.0@YGRIDINT=10,@ZGRIDINT=10,@YGRIDNDP=0,  
      
    
    @ZGRIDNDP=0,@ICONSIZE=25,@ICONCOL1=1, @ICONCOL2=1,@TITLE=1,  
      
    
    @TITCOL=1,@TITCHS=4  
      
    
    PLOTMX 
    		 - Annotated with Au and Rock type.
    
    
    2
    
    
    8140
    
    
    6500
    
    
    8140
    
    
    6530
    
    
    375
    
    
    395
    
    
    Y
    
    
    AU,2,1,-3,1.5,0,1
    
    
    ROCK,3,1,-1,-4,0,0
    
    
    3

### Example 2

This example illustrates the use of PLOTMX for an oblique section as defined by its azimuth, dip centre point and size. The cells have been shaded according to different intervals on the AU field. A legend has been specified and grid lines for both eastings and northings plotted:
    
    
    !PLOTMX   &IN(MODEL),&PROTO(PROTO),&PLOT(PLOT),@CHARSIZE=2,@=1,  
  
---  
      
    
    @FRAME=1,@SHRINK=0.2, @ANNOTATE=0,@BOX=1,@BOXCOL=1,@SHADE=1,   
      
    
    @SYMBOL=92,@SYMSIZE=0,@GRCOLR=1,@XGRIDINT=20, @YGRIDINT=10,  
      
    
    @ZGRIDINT=10,@XGRIDNDP=0, @YGRIDNDP=0,@ZGRIDNDP=0,@ICONSIZE=25,   
      
    
    @ICONCOL1=1,@ICONCOL2=1,@TITLE=1,@TITCOL=1,@TITCHS=3,@LEGEND=1,  
      
    
    @LEGCOL=1,@LEGCHS=2.5  
      
    
    PLOTMX - oblique plane shade by AU
    
    
    1
    
    
    8130 X centre
    
    
    6510 Y centre
    
    
    380 Z centre
    
    
    90 Dip
    
    
    30 Azimuth
    
    
    35 Horizontal size
    
    
    25 Vertical size
    
    
    Y
    
    
    AU
    
    
    1128,0,1.0
    
    
    1130,1,10
    
    
    1138,10,100
    
    
    3

### Example 3

This example illustrates the specification of a general plane (dip = 41 , azimuth = 31 ):
    
    
    !PLOTMX  &IN(MODEL),&PROTO(PROTO),&PLOT(PLOT),   
  
---  
      
    
             @CHARSIZE=1.8,@CHARSMIN=.5,@=1, @FRAME=1,@SHRINK=0.4,@ANNOTATE=1,   
      
    
             @ANNCOL=1,@ANNPOS=1,@BOX=1,@BOXCOL=1, @SHADE=0,@SYMBOL=92,@SYMSIZE=0,   
      
    
             @GRCOLR=1,@XGRIDIN=20,@YGRIDINT=20, @ZGRIDINT=20,@XGRIDNDP=0,@YGRIDNDP=0,   
      
    
             @ZGRIDNDP=0,@ICONSIZE=30,@ICONCOL1=1, @ICONCOL2=1,@TITLE=1,@TITCOL=1,  
      
    
             @TITCHS=4  
      
    
    PLOTMX - Oblique plane annotated with rock type
    
    
    8130 X centre
    
    
    6510 Y centre
    
    
    375 Z centre
    
    
    41 Dip
    
    
    31 Azimuth
    
    
    70 Horizontal size
    
    
    50 Vertical size
    
    
    Y
    
    
    ROCK,2,1,0,0,0,0
    
    
    3