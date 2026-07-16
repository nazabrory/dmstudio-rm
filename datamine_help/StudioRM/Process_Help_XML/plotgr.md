# PLOTGR Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTGR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTGR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTGR>).

## Process Overview

Generates a plotted grid, or set of lines, at any user-defined angle to the plot X and Y axes. Annotation on the lines may be defined and positioned by the user.  Single lines may be plotted, or sets of lines at pre-defined intervals.

Typical uses include laying a mine grid over a national grid system, or vice-versa, or plotting section lines on a plan.

The relationship between the plot X and Y axes and the required lines is defined by specifying a point whose co-ordinates are known in both systems (**X0** , **Y0** in the plot system and **XR0** , **YR0** in the rotated system) and an angle between them, measured in degrees clockwise from the rotated system Y axis to the unrotated system Y axis. This is illustrated in the accompanying diagram. Note that the point of coincidence need not be in the plot area.

Lines in the rotated X and Y directions are specified independently by giving co-ordinates of the first and the last line required, and the increment between lines. These parameters are @**XSTART** , @**XINC** and @**XEND** in X; and the equivalent in Y. For no lines in either of the directions, all three are set to 0; for only one line, the co-ordinate is specified as the start (@**XSTART** or @**YSTART**) and end (@**XEND** or @**YEND**) and the increment (@**XINC** or @**YINC**) set to zero.

The given lines are intersected with the data area of the plot, as defined in the prototype, and the intersections plotted. Annotation is placed at the start of each line (unless optional parameter @**NOANNOT** =1). The start point of this annotation, relative to the start of the line, may be controlled if required by specifying the @**XOFFSET** and @**YOFFSET** parameters. If these are not set, then the start is taken as 1 character position along the line and half a position above.

Note: Lines which lie completely outside the plot area will be omitted with no message. Therefore, to plot a full grid, it is easier to specify line start and end co-ordinates which lie well outside the area of interest, and leave the process to compute those that lie inside.

Note: If the grid is parallel to the axis (@**ANGLE** =0) then the first or last lines will sometimes be omitted if they lie exactly along the boundary of the plot region. This is because of slight inaccuracies in the tests for a line lying inside the plot region.

### @FACTOR

The @**FACTOR** parameter may be used to specify that the units of the grid lines are different to those of the plot (which are defined by the @**XMIN** ,... @**YMAX** parameters or taken from the prototype). For example, if @**FACTOR** =0.3048 and user data units are meters, then the grid lines will be in feet. @**FACTOR** is the number of user data units which equals one unit in the plotted grid.

If @**FACTOR** is set, then the @**XSTART** , @**XINC** and @**XEND** parameters are all set in the grid units, (as are the Y equivalents) and the @**XR0** , @**YR0** point is also defined in these units. The annotation is also shown in these units.

Use of the @**FACTOR** parameter allows for example section lines in feet or hundreds of feet to be plotted where the user data units are meters.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ANGLE |  Rotation angle in degrees, measured from the rotated axes towards the X-Y plot axes. |  Yes |  Undefined |  0,360 |  Undefined  
X0 |  X co-ordinate of known point in both systems, in unrotated co-ordinate system. |  Yes |  Undefined |  Undefined |  Undefined  
Y0 |  Y co-ordinate of known point in both systems, in unrotated co-ordinate system. |  Yes |  Undefined |  Undefined |  Undefined  
XR0 |  X co-ordinate of known point in both systems, in rotated co-ordinate system. |  Yes |  Undefined |  Undefined |  Undefined  
YR0 |  Y co-ordinate of known point in both systems, in rotated co-ordinate system. |  Yes |  Undefined |  Undefined |  Undefined  
XSTART |  First required line in rotated co-ordinate system X direction. Set **XSTART , XINC , XEND** all to 0 for no X lines. |  Yes |  Undefined |  Undefined |  Undefined  
XINC |  Increment between grid lines in rotated co-ordinate system X direction. Set to 0 for one line only. |  Yes |  Undefined |  Undefined |  Undefined  
XEND |  Last required line in rotated co-ordinate system X direction. Set to **XSTART** for one line only. |  Yes |  Undefined |  Undefined |  Undefined  
YSTART |  First required line in rotated co-ordinate system Y direction. Set **YSTART , YINC , YEND** all to 0 for no Y lines. |  Yes |  Undefined |  Undefined |  Undefined  
YINC |  Increment between grid lines in rotated co-ordinate system Y direction. Set to 0 for one line only. |  Yes |  Undefined |  Undefined |  Undefined  
YEND |  Last required line in rotated co-ordinate system Y direction. Set to **YSTART** for one line only. |  Yes |  Undefined |  Undefined |  Undefined  
NDEC |  Number of decimal places for annotation. |  Yes |  Undefined |  Undefined |  Undefined  
FACTOR |  The rotated co-ordinate system units will be e.g. 0.3048 for a grid in feet on an unrotated grid in metres (1). |  No |  1 |  Undefined |  Undefined  
NOANNOT |  |  Option |  Description  
---|---  
1 |  do not plot annotation on lines (0).  
No |  0 |  0,1 |  0,1  
XOFFSET |  The offset in millimetres of the start of the annotation from the start of each grid line measured along the line. [Default=1.0 **CHARSIZE**]. |  No |  Undefined |  Undefined |  Undefined  
YOFFSET |  The offset in millimetres of the start of the annotation from the start of each grid line measured at right angles to the line. [Default=0.5 **CHARSIZE**]. |  No |  Undefined |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio [width to ht.] for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !PLOTGR   &PROTO(PLOTPROT),&PLOT(GRID.P),@ANGLE=38,@X0=350,   
  
---  
      
    
    @Y0=400,@XR0=0,@YR0=0,@XSTART=-50,@XINC=50,@XEND=100,   
      
    
    @YSTART=0,@YINC=0,@YEND=0,@NDEC=0,@XMIN=300,@XMAX=600,   
      
    
    @YMIN=300,@YMAX=600  
  
A set of four section lines is plotted at X=-50, X=0, X=50, and X=100. These lines are at an angle of 38 degrees from the plot X axis; the point X=0, Y=0 of the grid corresponds to X=350, Y=400 of the plot. The data region covers the user data range of 300 to 600 on both axes. There are no lines plotted on the grid Y axis.
    
    
    !PLOTGR   &PROTO(PLOTPROT),&PLOT(GRID1.P),@ANGLE=0,@X0=0,   
  
---  
      
    
    @Y0=0,@XR0=0,@YR0=0,@XSTART=900,@XINC=100,@XEND=1800,   
      
    
    @YSTART=900, @YINC=100,@YEND=1800,@FACTOR=0.3048, @CHARSIZE=2.5,  
      
    
    @=8,@NDEC=0,@XMIN=300,@XMAX=600, @YMIN=300,@YMAX=600  
  
A grid in feet is overlain on the metric plot (which runs from 300 to 600 meters in both X and Y). This grid is parallel to the axes. The lines are spaced at 100 foot intervals, starting at 900 feet (which will be outside the plot and therefore omitted) and running to 1800 feet in both directions. The color chosen is 8, with a character size of 2.5 mm.

* * *

## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 411 <<< ( 0) IN TRANDP |  The scale has been defined or calculated as zero. Fatal; the process is exited.  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.