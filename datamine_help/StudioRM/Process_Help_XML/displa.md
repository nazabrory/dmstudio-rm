# DISPLA Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DISPLA** and click **Run**.
  * Enter "DISPLA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DISPLA>).

## Process Overview

Displays a previously created Datamine plot file on the graphics screen.

This is a system specific process, and the details may vary from implementation to implementation. The full plot area, as defined in the plot file, is normally mapped to the screen. The plot will be rescaled if necessary to fit it on the screen, unless the @**TRUESIZE** parameter is set. In this case, the portion of the plot that will fit on the screen will be displayed at the true size of the plot. The bottom left hand corner of the true size plot is at the bottom left hand corner of the graphics screen, unless offsets are specified by use of @**XOFFSET** and @**YOFFSET** parameters.

**Note** : suitable use of @**TRUESIZE** , @**XOFFSET** and @**YOFFSET** together with * **XSCALE** and * **YSCALE** in the plot file allow the user to output scale maps which are larger than the area of the dump or print device, by dividing the plot into pieces.

### Catalogue file input

If the input file is a catalogue file (as produced by the !LISTDR process) then each plot file in the catalogue will be displayed in turn. The following message is displayed:
    
    
    >>> OPERATING ON A CATALOGUE FILE INPUT <<<

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Plot file. Must contain the fields X, Y, S1, S2 and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE, XORIG, YORIG, XRT, YTP, XPICRT, YPICTP, CHARSIZE** and **ASPRATIO** (numeric, implicit). **IN** may also be a catalogue file, in which case all files in the catalogue will be displayed in sequence. |  Input |  Yes |  Plot  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
HARDCOPY |  |  Option |  Description  
---|---  
1 |  Graphics dump to printer [if available].  
No |  0 |  0,1 |  0,1  
TRUESIZE |  |  Option |  Description  
---|---  
1 |  Plot at true size in millimetres.  
No |  0 |  0,1 |  0,1  
XOFFSET |  Origin offset in X in millimetres (0). Only required if TRUESIZE used. |  No |  0 |  Undefined |  Undefined  
YOFFSET |  Origin offset in Y in millimetres (0). Only required if TRUESIZE used. |  No |  0 |  Undefined |  Undefined  
PAUSE |  Pause given number of units after displaying plot. -1 will prompt for <return> while in a macro. |  No |  Undefined |  Undefined |  Undefined  
SCALE |  The scale factor. E.g. enter 1000 for a scale of 1:1000. Note that user data units of metres are assumed; if metres are not the unit, then the scale must be multiplied by factor f, where f=no. of metres in 1 user data unit [e.g. 0.3048 for feet]. If - [absent data] is entered, then the plot will be the true size [as defined in the prototype]. |  No |  Undefined |  Undefined |  Undefined  
  
## Example

Display the plot file BENCH1.P on the screen:
    
    
    !DISPLA  &IN(BENCH1.P)  
  
---  
      
    
    Display the plot file SECPLOT1 on the screen, at a scale of 1:2000:  
      
    
    !DISPLA    &IN(SECPLOT1),@SCALE=2000  
  
## Error and Warning Message

Message |  Description  
---|---  
>>> ZERO OR NEGATIVE PLOT AREA DIMENSIONS -  
>>> DEFAULTING TO SCREEN DIMENSIONS. |  Error in plot area dimensions. Plot scaled for screen and processing continues.  
>>> NOT A VALID PLOT FILE <<< |  Fatal. If input is from a catalogue file, then the next file is examined and plotted if valid. However, the fatal error is still flagged at the end of the process.