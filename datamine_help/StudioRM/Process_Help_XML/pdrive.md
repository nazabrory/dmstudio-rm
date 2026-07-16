# PDRIVE Process  
  
To access this process:

  * Enter "PDRIVE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PDRIVE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PDRIVE>).

## Process Overview

Note: This process is largely superseded by **Plots** window printer support options. It is included here for legacy macro support.

Sends a plot file to the plotter. 

This process is machine specific and details vary from installation to installation.

Plots may either be plotted at true size, by specifying absent data (-) to the @**SCALE** parameter, or they may be re-scaled by specifying the required factor.

## Input Files

  
Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Plot file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE, XORIG, YORIG, XRT, YTP, XPICRT, YPICTP, CHARSIZE** and **ASPRATIO** (numeric, implicit). |  Input |  Yes |  Plot  
PENFILE |  Colour number to plotter pen mapping file. Must contain the fields and **PEN**. During plotting, the field in the plotfile will be translated into the **PEN** number in the **PENFILE**. The field may also contain the code 1126-1140 and will cause any fill codes in the plotfile to be plotted by the **PEN** number in the **PENFILE**. |  Input |  No |  Plotter Pen File  
FILTER |  Filter file to replace data values in the plot file, such as , with values more appropriate for the plotter. Expects fields **FIELD, TEST, IN** and **OUT**. |  Input |  No |  Plotter Filter  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLOTTYPE |  Type code for plotter. Select from the following list of plotters. |  Option |  Description  
---|---  
1. |  HCBS text file output  
10\. HP centre origin |  7585,Draftmaster etc.  
15\. HP corner origin |  7475,7550 etc  
16. |  HP Designjet 650C  
20. |  DMP 52,56,58 30. CalComp with 906 controller  
31. |  CalComp with 907 controller  
60\. Oce,Schlumberger,Benson |  VDF Format  
Yes |  Undefined |  1,60 |  1,10,15,16,20,31,60  
SPOOL |  The plotfile may automatically be sent to the plotter once the plot file is generated. Spooled plotting is normally done in background mode. |  Option |  Description  
---|---  
0 |  To not spool the plot file.  
1 |  To spool the plot file to the plotter.  
2 |  To spool the plot file to the plotter, and then delete the plot file. This assumes the plot file spooler you are using makes a copy of the plot file (1).  
Yes |  1 |  0,2 |  0,1,2  
DFLTFILE |  Used to determine how the name of the plot file is generated. |  Option |  Description  
---|---  
0 |  Force a prompt for a system filename.  
1 |  Force the use the default filename.  
2 |  Prompt for a system file if SPOOL is equal to 0 or 1, but to use the default system file if SPOOL  
No |  2 |  0,2 |  0,1,2  
NUM.PENS |  The number of pens to be used. If a field is in the plot file, then the number will be used as the required pen, unless this number exceeds **NUM.PENS** , when pen 1 will be used. The default is (64). |  No |  64 |  Undefined |  Undefined  
HATCHWID |  This defines the method of plotting the fill codes [1126-1140]. If this value is absent then different cross hatching styles will be generated using the first available pen. If a value is specified then it will be used as the spacing between horizontal hatch lines. To get a solid fill, specify a hatch width equal to the size of the pen. |  No |  Undefined |  Undefined |  Undefined  
SQUEEZE |  Reduce the size of fill codes [1126-] by this amount. Useful for avoiding the overlapping of the edges of fill codes during plotting. If a fill code is squeezed out completely on any axis, it will not be plotted. |  No |  Undefined |  Undefined |  Undefined  
ANGLE |  Rotate the plot by a given number of degrees. The default is (0) degrees. This is a replacement for the **ROTATE** parameter used on older versions of **PDRIVE**. |  No |  0 |  0,360 |  Undefined  
SCALE |  The scale factor. For example, enter 1000 for a scale of 1:1000. Note that user data units of metres are assumed; if metres are not the unit, then the scale must be multiplied by factor f, where f=no. of metres in 1 user data unit [e.g. 0.3048 for feet]. If - [absent data] is entered, then the plot will be the true size [as defined in the prototype]. |  No |  Undefined |  Undefined |  Undefined  
FACTOR |  A scaling factor used to change the size of the plot by multiplying the values in the plot file by this value. The default value is (1). |  No |  1 |  Undefined |  Undefined  
XOFFSET |  The X offset [along the paper] from the paper origin [mm] at which this plot will start (0). |  No |  0 |  Undefined |  Undefined  
YOFFSET |  The Y offset [along the paper] from the paper origin [mm] at which this plot will start (0). |  No |  0 |  Undefined |  Undefined  
PXEND |  The X offset from the current plot at which the pen will be left when the plot completes, and the origin for the next plot established here if the plotter supports new origins. The default is (0). |  No |  0 |  Undefined |  Undefined  
PYEND |  The Y offset from the current plot at which the pen will be left when the plot completes, and the origin for the next plot established here if the plotter supports new origins. The default is (0). |  No |  0 |  Undefined |  Undefined  
PENDMODE |  Determines the corner on the plot the **PXEND** and **PYEND** offsets from. |  Option |  Description  
---|---  
0 |  for bottom left [0,0],  
1 |  for bottom right [XPICRT,0],  
2 |  for top left [0,YPICTP]  
3 |  for top right [XPICRT,YPICTP]. The default is the bottom left corner (0).  
No |  0 |  0,3 |  0,1,2,3  
RASTER |  Determines whether a pen or a raster (HPGL2 capable) plotter is used. Use for any HPGL2 capable plotter. HPGL2 polygon plotting features are used for plot codes 1126-1189,2000/2001,3000-3155. Suppresses sorting of plot by colour. For pen plotters, PDRIVE plots the various colours in numerical order to save time. The default is pen plotter (0) |  Option |  Description  
---|---  
0 |  plotter is a pen type.  
1 |  plotter is a raster or inkjet type. Only for PLOTTYPE =10-19.  
No |  0 |  0,1 |  0,1  
FILLOPT |  |  Option |  Description  
---|---  
1 |  No polygon filling will take place.  
2 |  Polygon filling will use fill types defined in the plot file for each polygon.  
3 |  Polygon filling will use fill types defined in the pen file for polygons with matching colours in the plot file. Only for RASTER =1 (1)  
No |  1 |  1,3 |  1,2,3  
TRMODE |  |  Option |  Description  
---|---  
1 |  White polygon fill is transparent.  
0 |  White polygon fill is opaque. Only for RASTER =1 (1)  
No |  1 |  0,1 |  0,1  
EMPTYCOL |  |  Option |  Description  
---|---  
0 |  All polygons will be filled using the colour in the plotfile. >0: Polygons of this colour will be treated as empty [i.e. as if they had =0] Only for RASTER =1 (0)  
>0 |  Polygons of this colour will be treated as empty [i.e. as if they had =0] Only for RASTER =1 (0)  
No |  0 |  Undefined |  Undefined  
EDGEOPT |  |  Option |  Description  
---|---  
0 |  No polygon edging will take place.  
1 |  Edge polygons using colour from plot file or EDGECOL  
2 |  Force edging of empty polygons, using either EDGECOL or 1  
3 |  Force edging of all polygons without edging, using either EDGECOL or 1  
4 |  Force edging of all polygons using either EDGECOL or 1 Only for RASTER =1 (1)  
No |  1 |  0,4 |  0,1,2,3,4  
EDGECOL |  Default colour for polygon edging [see EDGEOPT ] Only for RASTER =1 (0) |  No |  0 |  Undefined |  Undefined  
CHARBGR |  Default colour for text background. |  Option |  Description  
---|---  
0 |  Opaque white background for text.  
>0 |  Coloured background for text.  
Undefined |  No background for text. Only for RASTER =1  
No |  Undefined |  Undefined |  Undefined  
SYMBGR |  Default colour for symbol background. |  Option |  Description  
---|---  
0 |  Opaque white background for symbols.  
>0 |  Coloured background for symbols.  
Undefined |  No background for symbols. Only for RASTER =1  
No |  Undefined |  Undefined |  Undefined  
FITPAPER |  Fit to paper. |  Option |  Description  
---|---  
0 |  Plot at nominated scale.  
1 |  Fit onto paper - preserve relative sheet dimensions.  
2 |  Fit onto paper - adjust scales in X and Y independently. Only for PLOTTYPE =10-19 (0)  
No |  0 |  0,2 |  0,1,2  
SHADEPCT |  The percentage shading required for solid-filled polygons Only for PLOTTYPE =10-19 (0) |  No |  100.0 |  1,100.0 |  Undefined  
  
## Example
    
    
    !PDRIVE &IN(PLOTFILE),@NUM.PENS=1,@SCALE= -  
  
---  
  
Will plot file plotfile at its true size (no re-scaling) with 1 pen only. This means that pen 1 will be used continuously, even if the field exists.

## Error and Warning Messages

Message |  Description  
---|---  
>>> NOT A VALID PLOTTER TYPE <<< |  An illegal value of the @**PLOTTYPE** parameter has been entered. Fatal; the process is exited.  
>>> NOT A VALID PLOT FILE <<< |  The file associated with &**IN** is not a valid plot file. Fatal; the process is exited.  
>>> NOT A VALID FILTER FILE <<< |  The filter file does not contain one or more of the required fields **FIELD, TEST, IN, OUT**. The **FILTER** file is ignored.  
>>> FIELD ffffffff MUST BE OF TYPE ALPHANUMERIC <<< |  The required fields **FIELD** and **TEST** must be alphanumeric. The **FILTER** file is ignored.  
>>> FIELD ffffffff MUST BE OF TYPE NUMERIC <<< |  The required fields **IN** and **OUT** must be numeric. The **FILTER** file is ignored.  
>>> FIELD ffffffff IS NOT VALID |  Filter field ffffffff is not present in the plot file. The particular record in the **FILTER** file is ignored.  
>>> TEST tttt IS NOT VALID |  The values of the test field must be one of **EQ, NE, LE, LT, GE, GT**. The particular record in the **FILTER** file is ignored.  
>>> NO VALID FILTERS IN FILTER FILE <<< |  No valid filters have been established. The **FILTER** file is ignored.  
>>> THE NUMBER OF FILTERS ESTABLISHED HAS REACHED THE MAXIMUM PERMISSABLE (64) <<< |  A maximum of 64 filters is allowed, all others are ignored.