# PLOTPA Process

Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTPA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTPA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTPA>).

## Process Overview

Plot all perimeters in a standard perimeter file.

The line type may be chosen by optional parameter. Currently available are broad or narrow. All points are connected in the order in which they appear in the file by the chosen line type. If multiple perimeters exist in the perimeter file, then the required one should be selected by retrieval criteria, e.g. **PVALUE** =3.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. This must contain at least two numeric variables ( X and Y) for plotting against each other. |  Input |  Yes |  Undefined  
PROTO |  The prototype plot file, as input. If this does not contain plot scale information, then this must be provided through the optional parameters **XMIN , XMAX , YMIN , YMAX , XSCALE , YSCALE**. |  Input |  Yes |  Plot Prototype  
DESC |  Optional input description file for the case of **ANNOTATE** =3 |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  The line X co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Y |  The line Y co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
APVALUE |  Field used for **PVALUE** annotation. Default is **PVALUE**. |  IN |  No |  Numeric |  Undefined  
APTN |  Field used for **PTN** annotation. Default is **PTN**. |  IN |  No |  Numeric |  Undefined  
PCODE |  Optional second perimeter keyfield. The field is of type Alphanumeric and 4 characters. Both **PCODE** and **PVALUE** will be annotated by default unless **APVALUE** is specified. |  Undefined |  No |  Any |  Undefined  
F1 |  First annotation field for **ANNOTATE** =3 case |  IN |  No |  Any |  Undefined  
F2 |  Second annotation field. |  IN |  No |  Any |  Undefined  
F3 |  Third annotation field. |  IN |  No |  Any |  Undefined  
F4 |  Fourth annotation field. |  IN |  No |  Any |  Undefined  
F5 |  Fifth annotation field. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINECODE |  |  Option |  Description  
---|---  
1 |  Narrow line.  
2 |  Broad line.  
No |  1 |  1,2 |  1,2  
NOCLOSE |  |  Option |  Description  
---|---  
0 |  joins the first and last points of the perimeter; =1 does not join the first and last points of the perimeter (0).  
No |  0 |  0,1 |  0,1  
SYMBOL |  Plots the symbol specified at each perimeter point (92). 91=o, 92=+, 93=x. |  No |  92 |  Undefined |  Undefined  
SYMSIZE |  Symbol size in millimetres (0). |  No |  0 |  Undefined |  Undefined  
ANNOTATE |  |  Option |  Description  
---|---  
0 |  no annotation  
1 |  annotate within a break in the perimeter boundary  
2 |  annotate along the inside of the perimeter boundary  
3 |  annotate in the 'centre' of the perimeter All fields to be plotted must be included in the Fn list taken from the DESC file. Default (0).  
No |  0 |  0,3 |  0,1,2,3  
NDP |  Number of decimal places in the annotation if the annotation field is numeric (0). |  No |  0 |  Undefined |  Undefined  
NDP1 |  Number of decimal places in the first annotation field **F1**. |  No |  Undefined |  Undefined |  Undefined  
NDP2 |  Number of decimal places in the second annotation field **F2**. |  No |  Undefined |  Undefined |  Undefined  
NDP3 |  Number of decimal places in the third annotation field **F3**. |  No |  Undefined |  Undefined |  Undefined  
NDP4 |  Number of decimal places in the fourth annotation field **F4**. |  No |  Undefined |  Undefined |  Undefined  
NDP5 |  Number of decimal places in the fifth annotation field **F5**. |  No |  Undefined |  Undefined |  Undefined  
PTNANNOT |  |  Option |  Description  
---|---  
0 |  no annotation; =1 annotate the perimeter with the perimeter point number (0).  
No |  0 |  0,1 |  0,1  
EXTDIS |  distance along bisector of perimeter corners for annotation of perimeters. Negative to annotate outside the perimeter (4). |  No |  4 |  Undefined |  Undefined  
PTNSIZE |  annotation size for perimeter point number labelling. (2.5) |  No |  2.5 |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (4). |  No |  4 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as "pen" number] for plot. (14) |  No |  14 |  Undefined |  Undefined  
XMIN |  Minimum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined