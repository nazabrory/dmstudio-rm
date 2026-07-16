# PLOTWS Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTWS" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTWS** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTWS>).

## Process Overview

Section plot in any direction through a wireframe model.

Scaling is completely automatic in this process, and any plot file or null prototype may be used; all that need be defined is the paper size.

PLOTWS produces an output plot file containing the intersection of a given plane with a wireframe model. The triangles of the wireframe model have not been intersected in any particular sequence, so there is no simple means in this program of generating an output perimeter.

Set section orientation as follows :- 
    
    
    >>> SELECT ONE OF THE FOLLOWING --  
    >>> 1 VERTICAL OR INCLINED SECTION >>> DEFINED ABOUT 
    CENTRE POINT  
    >>> 2 VERTICAL SECTION DEFINED BY >>> END POINTS  
    >>> 3 PLAN VIEW DEFINED BY CORNER >>> POINTS  
    (>>> 4 SECTION FROM SECTION DEFINITION) (>>> FILE(if 
    defined) ) >>> Supply 1,2, or 3 (or 4) as appropriate.

If 1 selected, interaction as follows:
    
    
    XC > X co-ordinate of centre of plane.  
    YC > Y co-ordinate of centre of plane.  
    ZC > Z co-ordinate of centre of plane.  
    DIP> Dip of section plane.  
    AZI> Azimuth of section plane.  
    HSIZE > Horizontal size of section plane.  
    VSIZE > Vertical size of section plane.  

These are then echoed back, followed by the prompt
    
    
    >ARE THESE CORRECT (Y/N) ? If any reply other than Y or y, interaction 
    	 repeated from the beginning.

If 2 selected, interaction as follows -
    
    
    X1 > X co-ordinate of bottom left corner of section plane.
    
    
    Y1 > Y co-ordinate of bottom left corner of section plane.
    
    
    X2 > X co-ordinate of top right corner of section plane.
    
    
    Y2 > Y co-ordinate of top right corner of section plane.
    
    
    Z1 > Z co-ordinate of bottom left corner of section plane.
    
    
    Z2 > Z co-ordinate of top right corner of section plane.

These are then echoed back, followed by the prompt
    
    
    >ARE THESE CORRECT (Y/N) ? If any reply other than Y or y, interaction 
    	 repeated from the beginning.

If 3 selected, interaction as follows -
    
    
    >>> DEFINE XMIN,YMIN,XMAX, AND YMAX
    
    
    X1 > X co-ordinate of bottom left corner of section plane.
    
    
    Y1 > Y co-ordinate of bottom left corner of section plane.
    
    
    X2 > X co-ordinate of top right corner of section plane.
    
    
    Y2 > Y co-ordinate of top right corner of section plane.
    
    
    ZC > Z co-ordinate of section plane.

These are then echoed back, followed by the prompt
    
    
    >ARE THESE CORRECT (Y/N) ? If any reply other than Y or y, interaction 
    	 repeated from the beginning.

If 4 selected, interaction is as follows:
    
    
    >>> WHICH SECTION DO YOU WANT (OR ? FOR A LIST)
    
    
    Enter SVALUE section number, or ? for a list of available sections.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
SECTION |  Optional section definition file. |  Input |  No |  Section Definition  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINECODE |  (1001) Line code for plotting - 1001 faint, or 1002 bold. |  No |  1001 |  1001, 1006 |  Undefined  
FRAME |  (0) Set to 1 if frame required around plot. |  No |  0 |  0,1 |  0,1  
CHARSIZE |  Character size in millimetres (4). |  No |  4 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XSCALE |  X scale in user data units per millimetre. If specified here or in **PROTO** this value will override section limits. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. If specified here or in **PROTO** this value will override section limits. |  No |  Undefined |  Undefined |  Undefined  
VERTEXAG |  Controls vertical exaggeration. This must be set to allow different scales. The default is forced equal scales (1). = 0 allows different scales for both axes determined by **XSCALE** and **YSCALE** if provided or else by filling the data area to the section limits. > 0 sets value of **XSCALE** /**YSCALE**. |  No |  1 |  Undefined |  Undefined  
  
* * *

## Example
    
    
    !PLOTWS &WIREPT(ZON1PT),&WIRETR(ZON1TR),&PROTO(WZON1PRT,  
  
---  
      
    
    &PLOT(WSZN1PLT),&SECTION(ZON1SEC)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ffffffff IS NOT A SECDEF FILE, FIELD aaaaaaaa MISSING |  One of the fields **SVALUE, XCENTRE, YCENTRE, ZCENTRE, SDIP, SAZI** or **STHICK** is missing from the section definition file. Processing continues, but the section definition file is not available.  
>>> ERR 120 <<< ( n) IN PLOTWS |  An error has occurred when reading the input point or triangle file e.g. one or more of the essential fields in the file is absent or of the wrong type. Fatal; the process is exited.