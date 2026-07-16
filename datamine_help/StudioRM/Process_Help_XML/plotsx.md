# PLOTSX Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTSX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTSX** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTSX>).

## Process Overview

Enhanced plotting of drill hole sections and level plans. Used in conjunction with [PLOTFX](<plotfx.md>), PLOTSX will produce high quality section plots.

Features include the following:

  * annotation of any field on either side of trace,

  * variable location/size and orientation of bore hole ID,

  * one or two histograms with or without bar annotation,

  * annotation of downhole distance and/or distance from the section plane,

  * line plots for multiple variables parallel to the trace,

  * end of hole mark and annotation with distance,

  * directional indicators at each end of the trace (entering section or leaving section),

  * an optional plan window showing section line, projection distance and hole trace,

  * parameters are provided to control size, location and color of various annotations, the trace and ticks,

  * several levels of filling and smoothing for plotting the hole trace.

Samples are selected for projection onto the section if they lie partially or totally within the three dimensional rectangular box defining the projection limits. If a sample crosses the box it is clipped at the boundary. The section may be any vertical or horizontal plane and is specified using the end points of the section line @**X1** , @**X2** , @**Y1** , @**Y2** in the case of a section and also the @**BLEVEL** parameter for level plans. For the latter case @**X1** and @**X2** should be the range of the X axis variable and @**Y1** = @**Y2** = the midpoint value along the Y axis. The RL of the plan is specified by @**BLEVEL**.

As with any section plotting, care must be taken when specifying **XMIN, XMAX, YMIN, YMAX**. For sections and RL plans set @**XMIN** = 0 and @**XMAX** = section length. For sections @**YMIN** and @**YMAX** will equal the lower and upper RL(Z) limits. Remember to increase @**YMAX** to allow for the plan window + 10mm if this is being used. In the case of RL plans @**YMIN** and @**YMAX** should be - and + half the range of the Y axis variable.

Complex plots with several annotations may be produced by using multiple **PLOTSX** commands. In all but the initial command plotting of the ticks, trace, end of hole and **BHID** annotation should be disabled using @**TRACE** = 0, @**TIKTYP** = 0 and @**BHSIZE** = 0.

Offsets and plotted values are at right angles to the sample. The offsets are relative to the side as chosen by the @SIDE parameter or the top of the bar in the case of histograms.

In order to use the trace smoothing or gap filling it is necessary to specify a collar and a survey file (@**OPTMSE** = 1, 2 or 3). These options will improve the quality of the hole trace where long samples in curved holes cause problems.

### @PLTYPE

Interaction depends on the value of **PLTYPE** selected:

**PLTYPE** = 0:  |  trace only. no interaction  
---|---  
**PLTYPE** = 1:  |  Annotate sample values. Sections to be annotated with data values Please enter field for annotation << FIELD 1>  
**PLTYPE** = 2:  |  Single side barplot. Bar plot to be generated along boreholes Please enter numeric field for barplot, and corresponding field value for 10mm barchart separated with a comma - no spaces please FIELD 1>  
**PLTYPE** = 3:  |  Double side barplot. Bar plots to be generated along boreholes Please enter 2 numeric fields for barplot (one per line) and field values for 10mm barchart separated with a comma - no spaces please FIELD 1> FIELD 2>  
**PLTYPE** = 4:  |  Line plot Line plots to be generated alongside boreholes Please enter up to 3 numeric fields (one per line) and field values for 10mm lineplot, plus optional color, all separated by commas FIELD 1> FIELD 2> FIELD 3>  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input drillhole file, in standard sample format. If there is a field in this file, then the given colour number will be applied to each sample trace or barplot. |  Input |  Yes |  Drillhole  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
IN2 |  Optional input collar file, in standard collar format. |  Input |  No |  Undefined  
IN3 |  Optional input survey file, in standard survey format. |  Input |  No |  Undefined  
ANNFILE |  Optional annotation input file for specifying annotations as an alternative to the interactive input. If specified then **PLTYPE , XOFFSET , YOFFSET** are ignored. Compulsory fields: 

  * **FIELD** A8- Field to annotate. 
  * **TYPE** N - Annotation type; 1 = annotate relative to trace; 2 = bar plot; 3 = annotate relative to previous bar plot; 4 = line plot; 
  * **SIDE** N - Side of trace 1=RHS,2=LHS. Optional fields: CHARSIZE N - Annotate character size. 
  * **N** \- Annotate/bar/line colour. 
  * **XOFFSET** N - Offset perpendicular to trace. 
  * **YOFFSET** N - Offset along trace. 
  * **NDP** N - Number of decimal places. For bars: 
  * **CUTVAL** N - Value of field for maximum bar. 
  * **CUTMM** N - Optional height of maximum bar, default is 10mm. Optional fields if FIELD is numeric: 
  * **LOWER** N - Lower bound non-inclusive. 
  * **UPPER** N - Upper bound inclusive. **LOWER** and UPPER define the range on **FIELD** for which the particular annotation will plotted. 

Special values - and + may be used. For **TYPE** = 2 and 4 offsets apply to base of bar or line axis. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPCOLR |  Sample colour field, used preferentially for plotting of trace, assays, ticks and barplots. (). |  IN1 |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
X1 |  X co-ordinate of section line start. |  Yes |  Undefined |  Undefined |  Undefined  
Y1 |  Y co-ordinate of section line start. |  Yes |  Undefined |  Undefined |  Undefined  
X2 |  X co-ordinate of section line end. |  Yes |  Undefined |  Undefined |  Undefined  
Y2 |  Y co-ordinate of section line end. |  Yes |  Undefined |  Undefined |  Undefined  
NDP |  Number of decimal places for grade values. |  Yes |  Undefined |  Undefined |  Undefined  
DISTANCE |  Maximum projection distance to section. Must be specifed unless **DPLUS** and **DMINUS** are both specified. |  No |  Undefined |  Undefined |  Undefined  
DMINUS |  Negative distance from section plane. If not specified then **DISTANCE** will be used. |  No |  Undefined |  Undefined |  Undefined  
DPLUS |  Positive distance from section plane. If not specified then **DISTANCE** will be used. |  No |  Undefined |  Undefined |  Undefined  
OPTMSE |  Level of hole trace filling and smoothing:  0=none;  1=join gaps;  2=split long samples  3=automatic splitting; |  No |  0 |  0,3 |  0,1,2,3  
PLTYPE |  Type of plot: 0=plot trace only;  1=annotate sample values;  2=single side barplot;  3=double side barplot;  4=line plot; (1) |  No |  1 |  0,4 |  0,1,2,3,4  
BARANN |  Annotation outside bars on barplot type plots:  0=no;  1=yes; (0) |  No |  0 |  0,1 |  0,1  
PLVIEW |  Plot orientation: 0=standard section plot;  1=section with plan window;  2=plan plot; (0) |  No |  0 |  0,2 |  0,1,2  
PLDIST |  Plan window distance for **PLVIEW** =1 only. default = 2 **DISTANCE** |  No |  Undefined |  Undefined |  Undefined  
BLEVEL |  Bench level for use with **PLVIEW** =2 only. [R.L. of plan plot] |  No |  Undefined |  Undefined |  Undefined  
TRACE |  0 = no hole trace or EOH tick;  1 = plot trace;  2 = plot trace with symbol marking intersection with the plane;  3 = as 1 above with thick line code 1002;  4 = as 2 above with thick line code 1002; |  No |  1 |  0,4 |  0,1,2,3,4  
TIKLEN |  Tick length each side of hole; (1) |  No |  1 |  Undefined |  Undefined  
TIKTYP |  Tick positioning;  0=no ticks;  1=both sides;  2=RHS;  3=LHS;  |  No |  1 |  0,3 |  0,1,2,3  
SIDE |  Side of hole to use in annotation or barplots.  1=RHS;  2=LHS; |  No |  1 |  1,2 |  1,2  
DHD |  Plot downhole distance or distance to section 0=none;  1=plot downhole distance;  2=plot distance of sample from section;  3=both; |  No |  0 |  0,3 |  0,1,2,3  
DHDIST |  Plot DHD parameter[s] at given interval [integer]  |  No |  0 |  Undefined |  Undefined  
DHDOFF |  DHD parameter[s] offset in millimetres from hole trace at the right angles to sample. Value > 0 right h. side, <0 left h. side. (0). |  No |  0 |  Undefined |  Undefined  
EOH |  End of hole annotation:  0=nothing;  1='EOH';  2=downhole distance;  3=both 1 |  No |  0 |  0,3 |  0,1,2,3  
XOFFSET |  Offset in millimetres from sample centre of annotation at rt. angles to sample (0). |  No |  0 |  Undefined |  Undefined  
YOFFSET |  Offset in millimetres from sample centre of annotation along sample (0). |  No |  0 |  Undefined |  Undefined  
BHSIZE |  Borehole id annotation size: 0=suppress; default= **CHARSIZE** value; |  No |  Undefined |  Undefined |  Undefined  
BHCOL |  Borehole id annotation colour: default= value; |  No |  Undefined |  Undefined |  Undefined  
BHANG |  Angle for drillhole id, 0=horizontal, -90=vertically upwards, -= in line with hole trace; += at 90 degrees to hole trace. |  No |  Undefined |  Undefined |  Undefined  
BHPOS |  Borehole id position:  1=top of hole;  2=bottom of hole; (1) |  No |  1 |  1,2 |  1,2  
TRCOL |  Colour of trace: - 1=same as default parameter; 0=use colour field if present;  >=1 any other colour. (-1) |  No |  -1 |  -1,64 |  Undefined  
TIKCOL |  Colour of ticks: - 1=same as default parameter;  0=use colour field if present;  >=1 any other colour. (-1) |  No |  -1 |  -1,64 |  Undefined  
ANNCOL |  Colour of assay [or other] annotation down the side of the hole:  -1=same as default parameter;  0=use colour field if present;  >=1 any other colour. (-1) |  No |  -1 |  -1,64 |  Undefined  
BARCOL |  Colour of bars: - 1=same as default parameter;  0=use colour field if present;  >=1 any other colour. (-1) |  No |  -1 |  -1,64 |  Undefined  
FILGAP |  Controls filling of gaps and splitting of long samples/gaps in straight [1 survey pt] holes:  0=gaps not filled;  1=gaps filled;  2=enables splitting according to **GAPLEN** even if hole is straight. (0) |  No |  0 |  0,1,2 |  0,1,2  
GAPLEN |  Length to split long samples or gaps to for more accurate plotting for **OPTMSE** =2. (1) |  No |  1 |  Undefined |  Undefined  
FILL |  Line density in mm for pseudo colour fill of sample barplot. Zero for no fill (0). |  No |  0 |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (4). |  No |  4 |  Undefined |  Undefined  
CHARSMIN |  Minimum annotation character size. If space available for annotation is less than **CHARSMIN** the annotation is not plotted at all. Otherwise the characters are shrunk to fit in available space. |  No |  Undefined |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, assuming it exists and is a proper plot file. (0) |  No |  0 |  0,1 |  0,1  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
XMIN |  Minimum value of X for plot [Suggest 0]. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot [Suggest section length as defined by **X1 , Y1 , X2 , Y2**]. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot [Lowest Z value]. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot [Highest Z value]. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined