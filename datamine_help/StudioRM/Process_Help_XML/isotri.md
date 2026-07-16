# ISOTRI Process  
  
To access this process:

  * Enter "ISOTRI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ISOTRI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#ISOTRI>).

## Process Overview

Generate a plot file of an isometric view of a triangulated (wireframe) model, at any desired orientation.

  * Scaling is completely automatic in this process, and any plot file or null prototype may be used; all that need be defined is the paper size.

  * The hidden line removal algorithm can be slow when using large data sets, so it is recommended that an initial plot with @**HIDDEN** set to 1 be produced to check the view parameters.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Prototype plot file. |  Input |  Yes |  Plot Prototype File  
WIRETR |  Input wireframe triangle file . |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PXMIN |  Minimum data X value to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PXMAX |  Maximum data X value to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PYMIN |  Minimum data Y value to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PYMAX |  Maximum data Y value to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PZMIN |  Minimum data Z value to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PZMAX |  Maximum data Z value to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
ROTATE |  The rotation angle of the direction of view, in degrees horizontally and clockwise from the data Y axis. Default (45). E.g. if model Y and X axes are parallel to North 45 = Looking North-East 225 = Looking South-West |  No |  45 |  0,360 |  Undefined  
ELEVATE |  The rotation angle of the direction of view, in degrees vertically from data X-Y plane. Default (30). E.g. if model Y and X axes are parallel to North 0 = Looking horizontally, along X-Y plane. +90 = Looking vertically downwards -90 = Looking vertically upwards |  No |  30 |  -90,90 |  Undefined  
HIDDEN |  Control of hidden line display. |  Option |  Description  
---|---  
0 |  Hidden lines are NOT displayed.  
1 |  Hidden lines are displayed.  
No |  0 |  0,1 |  0,1  
CHARSIZE |  Character size in millimetres. |  No |  3 |  |   
ASPRATIO |  Aspect ratio, width / ht. for chars. |  No |  0.9 |  |   
|  Colour [as 'pen' number] for plot. |  No |  1 |  |   
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file. N.B. Scaling is fully automatic in this process. |  No |  0 |  |   
  
## Example
    
    
    !ISOTRI     &PROTO(WISOPROT),&WIREPT(ZON1PT),&WIRETR(ZON1TR)   
  
---  
      
    
     &PLOT(WISOZON1)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED. |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR \- CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced  
>>> ERROR IN READING INPUT FILE <<< >>> ERR 121 <<< ( n) IN ISOTRI |  An error has occurred when reading the input point or triangle file e.g. one or more of the essential fields in the file is absent or of the wrong type. Fatal; the process is exited.