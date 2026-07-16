# PLOTTX Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTTX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTTX** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTTX>).

## Process Overview

Generate a plot from a text file. This enables legends, text etc. to be added to any plot file.

The text file is normally set up by the [INPUTC](<inputc.md>) process. However, any file containing explicit alphanumeric fields may be used. All alphanumeric words from the file will be amalgamated together, irrespective of the field name. Any implicit or numeric fields will be ignored with a warning message.

Because a blank line is ignored in a text file, blank lines are simulated by use of a four character combination. This is **** by default; any line starting with **** in the first four characters will be plotted as a blank line. If required, this set of four characters may be redefined using the @**SPACE** parameter.

A box is plotted around the text by default; this may be suppressed by setting @**NOBOX** =1. The box is separated from the text lines by a margin which is 4 millimetres wide by default. This may be changed by setting the @**MARGIN** parameter to the required distance. The size of the box is determined by the longest line of text in the file, rounded up to the nearest word (4 characters).

Positioning of the text is carried out by use of the @**XSTART** and @**YSTART** parameters, which give the position on the plot, in millimetres, of the top left hand corner of the box around the text (whether this box is plotted or not) from the plot origin (bottom left hand corner). The first line of text is plotted a distance of margin size plus 1.3 character sizes below this point, and starting margin size to the right of this point; each subsequent line of text starts 1.3 character sizes below the last, leaving a gap of 23 character sizes between each line of text.

The angle of the text may be specified by use of the optional @**ANGLE** parameter. Rotation angles specified in degrees clockwise about the X axis; 0 is parallel to the axis, 90 is vertically down, and -90 is vertically upwards. The text is rotated around the point @**XSTART** , @**YSTART**.

Because the text is positioned by millimetres on the plot, part of the plot prototype used is the total plot area, defined by the fields **XPICRT** , **YPICTP** in the plot prototype. The data area is ignored, and therefore data area parameters such as @**XMIN** ,........@**YSCALE** are not needed.

The process tests that the point @**XSTART** ,@**YSTART** lies in the plot region; however the user must ensure that there is space for the full text within the region.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input text file. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
XSTART |  X position, in millimetres, for start of text (top left hand corner of box). |  Yes |  Undefined |  Undefined |  Undefined  
YSTART |  Y position, in millimetres, for start of text (top left hand corner of box). |  Yes |  Undefined |  Undefined |  Undefined  
ANGLE |  Angle of text clockwise from the X axis (0). |  No |  0 |  Undefined |  Undefined  
NOBOX |  |  Option |  Description  
---|---  
0 |  a box is plotted around the text, =1 a box is not plotted around the text (0).  
No |  0 |  0,1 |  0,1  
MARGIN |  The margin, in millimetres, between the text and the surrounding box (3). |  No |  3 |  Undefined |  Undefined  
SPACE |  A word which if encountered as the first word in a text record is interpreted as a blank line. Must be between quotes; e.g '----'. Default is ' '. |  No |  Undefined |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
  
## Example

First a text file is generated:
    
    
    !INPUTC &OUT(TEXT)  
  
---  
      
    
    SYSFILE><return>  
      
    
    DATA >****  
      
    
    DATA >XYZ CORPORATION LONDON, U.K.  
      
    
    DATA >****  
      
    
    DATA >-----------------------------------  
      
    
    DATA >****  
      
    
    DATA >RED LION DEPOSIT BENCH PLANS  
      
    
    DATA >****  
      
    
    DATA >-----------------------------------  
      
    
    DATA >Checked by: Date :  
      
    
    DATA >-----------------------------------  
      
    
    DATA >****  
      
    
    DATA > Legend  
      
    
    DATA >****  
      
    
    DATA > 43.5 Fe grade  
      
    
    DATA > 2.7 P2O5 grade  
      
    
    DATA >****  
      
    
    DATA >!!  
  
**Note** : The **** string has been used to denote a blank line. The text file is now plotted using PLOTTX.
    
    
    !PLOTTX &IN(TEXT),&PROTO(BENCH.P),  
  
---  
      
    
    &PLOT(TEXT.P),@XSTART=550,@YSTART=60,@CHARSIZE=2  
  
The plot prototype used is the previously existing bench plan bench.p. Knowing the size of this plot, and the location of the data area, the text (with box) is plotted at a start point of 550,60 millimeters from the plot origin. Since the text size chosen is 2 millimeters, the total length of the text is:

17 (lines) * 1.3 * 2 (each line is charsize * 1.3) + 8 (top and bottom margins) = 52.2 millimeters.

Hence the text starts 60 millimeters from the bottom.

## Error and Warning Messages

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.  
>>> IMPLICIT FIELDS IGNORED <<< |  Implicit fields were found in the input text file. They are ignored, and processing continues.  
>>> NUMERIC FIELDS IGNORED <<< |  Numeric fields were found in the input text file. They are ignored, and processing continues.  
>>> TEXT X,Y START POSITION OUTSIDE THE PLOT AREA <<< |  The @**XSTART** , @**YSTART** parameters define the top left of the text box to be outside the plot region defined by the **XPICRT** , **YPICTP** fields in the plot prototype file. Fatal; the process is exited.