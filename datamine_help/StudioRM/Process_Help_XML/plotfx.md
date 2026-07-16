# PLOTFX Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTFX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTFX** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTFX>).

## Process Overview

Generates a frame plot consisting of a frame, annotated grid, title block and legend block. Features include scale bar, north arrow and optional plan window for use with [PLOTSX](<plotsx.md>) (section plotting command).

This is a general process which can be used to add a frame, title block and legend to any plot. Used in conjunction with [PLOTSX](<plotsx.md>) high quality drill hole sections can be produced, including a plan view of drill hole locations and paths. 

For title entry, X offset and Y offset (in mm) can be used to reposition titles from the standard positions. Exclusion of these will result in centered titles as shown in the Figure 1.

The number of characters per line and number of lines in the legend and title blocks vary depending upon block and character sizes.

For wide legend blocks (@**LBLOCK** = 2) two columns of legend may be specified. A code of C will switch to the 2nd side.

The components are:-

##### Frame

A box around the data area, a separate box for section and plan if the plan window is used. An additional box is plotted 2mm outside the data area.

##### Grid

A full grid of intersecting lines spaced according to the @**XINC** and @**YINC** parameters for the horizontal and vertical axes respectively. These grid lines will start from @**XMIN** and @**YMIN** unless the optional parameters @**XGSTART** and @**YGSTART** are specified. (Should not be less than @**XMIN** and @**XMAX** respectively).

##### Annotation

Grid lines are annotated with data values along the lines and inward. In addition a 4 character suffix may be added using the @**XGID** and @**YGID** parameters.

##### Title Block

An optional title block may be added into any corner of the data area. There are 3 sizes that may be specified: standard, basic and small.

  * Standard 145 x 100 mm

  * Basic 130 x 80 mm

  * Small 100 x 60 mm

For sheet sizes less than 400 mm x 400 mm only a small title block is drawn. The title block contains up to 4 lines of text plus date, drawing number and boxes for manual annotation (Drawn, Designed, Checked and Approved).

The standard block, on sheets at least 400mm x 400mm, contains an automatically generated scale bar.

##### Legend Block

A legend block containing varying size and color text and symbols may be added into any corner of the data area.

##### Plan Window

**PLOTFX** may be used in conjunction with [PLOTSX](<plotsx.md>) to produce section plots having a plan window across the top of the section. Using the @**SPLAN** =1 setting and appropriate values for the @**PLDIST** , @**PRDIST** , @**PLX1** , @**PLX2** , @**PLY1** and @**PLY2** parameters will produce separate gridded frames for both the **SECTION** and **PLAN** windows.

The width of the plan window is specified in user data units and should be at least twice the section projection distance. The parameters are @**PLDIST** and @**PRDIST** and must equal the values of @**PLDIST** and @**DISTANCE** specified for the [PLOTSX](<plotsx.md>) command.

The plotted width of the plan window plus 10mm is deducted from the data area. It is therefore necessary to allow for this reduction by increasing @**YMAX**.

If a number of plots are to be generated with the same scales and axes, then it is only necessary to generate a single frame using **PLOTFX**. This can then be joined to any plot by the **APPEND** process.

**PLOTFX** does not require a plot prototype, although one may be used. The @**IBASE** parameter may be used to specify sheet size. If a prototype is used then @**IBASE** =9. If only 4 of **XMIN** , **XMAX** , **YMIN** , **YMAX** , **XSCALE** and **YSCALE** are specified then the other 2 must be set to missing data (i.e. @**XMAX** =-, @**YMAX** =-).

If no prototype is used then all 6 of the scale and size parameters must be set and consistent.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  No |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
XINC |  Grid increment on X axis. |  Yes |  Undefined |  Undefined |  Undefined  
YINC |  Grid increment on Y axis. |  Yes |  Undefined |  Undefined |  Undefined  
IBASE |  Baseplan size: |  Option |  Description  
---|---  
1 |  A0 horizontal - 1000 x 800 mm  
2 |  A0 vertical - 800 x 1000 mm  
3 |  B1 horizontal - 900 x 650 mm  
4 |  B1 vertical - 650 x 900 mm  
5 |  A1 horizontal - 800 x 560 mm  
6 |  A1 vertical - 560 x 800 mm  
7 |  A3 horizontal - 350 x 250 mm  
8 |  A3 vertical - 250 x 350 mm  
9 |  user defined  
10 |  user defined with single thickness title  
11 |  user defined with no outer frame For options 1-8 a plot prototype file is not required, but parameters xmin , xmax , xscale , ymin , ymax , yscale must be entered.  
Yes |  1 |  1,11 |  Undefined  
NDX |  Annotation decimal places on X axis (0). |  No |  0 |  Undefined |  Undefined  
NDY |  Annotation decimal places on Y axis (0). |  No |  0 |  Undefined |  Undefined  
TICKLX |  Length of grid ticks on X axis in mm. = 0 for full lines (0). |  No |  0 |  Undefined |  Undefined  
TICKLY |  Length of grid ticks on Y axis in mm. = 0 for full lines (0). |  No |  0 |  Undefined |  Undefined  
XGSTART |  Start point of X grid, ticks Default is XMIN. To suppress plotting of X-axis set XGSTART to '+'. |  No |  Undefined |  Undefined |  Undefined  
YGSTART |  Start point of Y grid, ticks Default is YMIN. To suppress plotting of Y-axis set YGSTART to '+'. |  No |  Undefined |  Undefined |  Undefined  
TBLOCK |  |  Option |  Description  
---|---  
0 |  for no title block  
1 |  for standard title block  
2 |  for basic title block  
3 |  for small title block (0). Titles are prompted for interactively.  
No |  0 |  0,3 |  0,1,2,3  
EMPTYTB |  |  Option |  Description  
---|---  
0 |  for filled title block  
1 |  for empty title block  
No |  0 |  0,1 |  0,1  
TUNITS |  Units for scale bar in title box. |  No |  1 |  Undefined |  Undefined  
TSCALE |  Scale to be plotted in the title box and used for the scale bar. This is a natural scale i.e. for 1:1000 enter 1000. If **TUNITS** is not specified then units are assumed to be metres. Note if **TUNITS** is used then **TSCALE** is not required. If used it will overwrite the value calculated by **TUNITS**. The default is XSCALE 1000 (-). |  No |  - |  Undefined |  Undefined  
LBLOCK |  |  Option |  Description  
---|---  
0 |  for no legend block  
1 |  for standard legend block [100x100mm]  
2 |  for wide legend block [200x100mm]  
No |  0 |  0,3 |  0,1,2,3  
TPOS |  Title block position; |  Option |  Description  
---|---  
1 |  for bottom right  
2 |  for bottom left  
3 |  for top left  
4 |  for top right; (1)  
No |  1 |  1,4 |  1,2,3,4  
LPOS |  Legend position; |  Option |  Description  
---|---  
1 |  for bottom right  
2 |  for bottom left  
3 |  for top left  
4 |  for top right  
5 |  same as title box but to side  
6 |  same as title box but above/below; (1)  
No |  1 |  1,6 |  1,2,3,4,5,6  
XGID |  Text following grid number on X axis, max 4 characters, enclosed in single quotes if alpha, eg. 'mE' |  No |  Undefined |  Undefined |  Undefined  
YGID |  Text following grid number on X axis, max 4 characters, enclosed in single quotes if alpha, eg. 'mN' |  No |  Undefined |  Undefined |  Undefined  
DRAWNUM |  Plot drawing number, max of 4 characters. |  No |  Undefined |  Undefined |  Undefined  
LOGO |  Plot logo; |  Option |  Description  
---|---  
0 |  for none  
1 |  to plot logo (0). This will be prompted for following titles.  
No |  0 |  0,1 |  0,1  
SPLAN |  Selection of plan window. If selected then the following 6 parameters must also be set. |  Option |  Description  
---|---  
0 |  no section plan window  
1 |  plot plan window. (0)  
No |  0 |  0,1 |  0,1  
PLDIST |  Width of plan window in user data units. Must equal **PLDIST** for corresponding **PLOTSX** command. |  No |  Undefined |  Undefined |  Undefined  
PRDIST |  Section projection distance. Should equal **DISTANCE** on the **PLOTSX** command. Horizontal grid lines are drawn in the plan window along the section line and at **PRDIST** either side of it. |  No |  Undefined |  Undefined |  Undefined  
DMINUS |  Negative distance from section plane. For sections where **PRDIST** differs on either side. If not specified then **PRDIST** will be used. |  No |  Undefined |  Undefined |  Undefined  
DPLUS |  Positive distance from section plane. For sections where PRDIST differs on either side. If not specified then PRDIST will be used. |  No |  Undefined |  Undefined |  Undefined  
PLX1 |  X Co-ordinate at start of section line. Must equal X1 on **PLOTSX** command. |  No |  Undefined |  Undefined |  Undefined  
PLX2 |  X Co-ordinate at end of section line. Must equal **X2** on **PLOTSX** command. |  No |  Undefined |  Undefined |  Undefined  
PLY1 |  Y Co-ordinate at start of section line. Must equal **Y1** on **PLOTSX** command. |  No |  Undefined |  Undefined |  Undefined  
PLY2 |  Y Co-ordinate at end of section line. Must equal **Y2** on **PLOTSX** command. |  No |  Undefined |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres of grid annotation (2.5). |  No |  2.5 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (1.1). |  No |  1.1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, assuming it exists and is a proper plot file. (0) |  No |  0 |  0,1 |  0,1  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.