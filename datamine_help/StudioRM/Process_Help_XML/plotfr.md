# PLOTFR Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTFR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTFR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTFR>).

## Process Overview

Generates a frame plot, consisting of a frame, a grid or tick marks, with annotation on each axis, and user defined titles on each axis.

This is a general process, which may be used to add a frame and axes to any plot. The usual method of operation is to generate a frame plot when the user is satisfied with the plot of the data to which the frame is to be added. The components are:-

##### Frame

A box around the data area (the X and Y axes) and an optional box around the full plot area (negative values of @**IGRID** parameter). The data and picture area sizes are taken from the prototype, or defined to be the screen size if the null plot prototype plotprot is used.

##### Numbering

Annotation at each tick mark or each grid mark.

##### Tick Marks

Out: Tickmarks outwards from the box around the data area.

In: Tickmarks inwards from the box around the data area.

##### Grid

A full grid of intersecting lines in place of the tickmarks.

##### Interior Crosses

A set of interior crosses marking the intersection points of the grid lines.

In addition, up to 80 characters of label are permitted on each axis. These are prompted for. The labels start from the origin (bottom left-hand corner of the data area), so that spaces should be inserted at the start of the label to space the text along the axes.

Normally tickmarks and grids start from the **XMIN, YMIN** values; however these may optionally be started at any required position by use of the optional parameters @**XGSTART** , @**YGSTART**.

If a number of plots are to be generated with the same scales and axes, then it is only necessary to generate a single frame using **PLOTFR**. This can then be joined to any data plot required by using the APPEND process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype File  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
XINC |  Grid increment on X axis. |  Yes |  Undefined |  Undefined |  Undefined  
YINC |  Grid increment on Y axis. |  Yes |  Undefined |  Undefined |  Undefined  
NDX |  Annotation decimal places on X axis. |  Yes |  Undefined |  Undefined |  Undefined  
NDY |  Annotation decimal places on Y axis. |  Yes |  Undefined |  Undefined |  Undefined  
IGRID |  |  Option |  Description  
---|---  
0 |  frame only;  
1 |  frame + outwards ticks;  
2 |  frame + crosses at grid intersections;  
3 |  frame + inwards ticks;  
4 |  grid;  
5-9 |  as 0-4 minus frame.  
10 |  as 4 but anno- tation parallel to grid lines.  
11-2 |  0 as 1-10 with annotation on right and top as well. Negative values of IGRID give an additional frame around the full plot area.  
Yes |  0 |  0,20 |  Undefined  
NOXAXIS |  Suppresses plotting of X-axis. |  No |  Undefined |  Undefined |  Undefined  
NOYAXIS |  Suppresses plotting of Y-axis. |  No |  Undefined |  Undefined |  Undefined  
XGSTART |  Start point of X grid, ticks Default is **XMIN**. |  No |  Undefined |  Undefined |  Undefined  
YGSTART |  Start point of Y grid, ticks Default is **YMIN**. |  No |  Undefined |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Example

### Example 1

The following example generates a frame with scaling information supplied on the command line. If a plot file already exists, then the scale may be taken from it in the following way:
    
    
    !PLOTFR  &PROTO(PLOTPROT),&PLOT(FRAME),@XMIN=300,@XMAX=600,   
  
---  
      
    
    @YMIN=300,@YMAX=600,@XINC=50,@YINC=50,@NDX=1,@NDY=1, @IGRID=4  
      
    
    XLABEL > Collar X Co-ordinate.  
      
    
    YLABEL > Collar Y Co-ordinate.  
  
### Example 2

The following example generates a frame for an existing histogram plot file:
    
    
    !PLOTFR  &PROTO(HISTPLOT),&PLOT(HISTFRAM),@XINC=50,@YINC=10, @NDX=0,@NDY=0,@IGRID=3  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.