# WFTREND Process

To access this process:

  * **Wireframe** ribbon **> > Process >> Wireframe Proceses >> Trend Surface**.

  * Enter "WFTREND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **WFTREND** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WFTREND>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

This process creates a DTM wireframe surface which can be extended beyond the data limits by a specified distance using a planar trend surface.

The data limits are detected automatically and the trend surface is only used beyond the limits of the actual data. The input data is a set of points which should be sorted.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
POINTIN |  Input point data file. |  Input |  Yes |  Point Data  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETR |  Output |  Yes |  Wireframe Triangle |  Output wireframe triangle file.  
WIREPT |  Output |  Yes |  Wireframe Points |  Output wireframe point file.  
POINTOU |  Output |  No |  Point Data |  Output point data file. This includes both the input point data, and the points which were extrapolated using the trend surface.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
XPT |  X field in input point data file. |  POINTIN |  Yes |  Numeric |  XPT  
YPT |  Y field in input point data file. |  POINTIN |  Yes |  Numeric |  YPT  
ZPT |  Z field in input point data file. |  POINTIN |  Yes |  Numeric |  ZPT  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
EXTN |  The extension distance required beyond the data points for the triangulation. |  Yes |  Undefined |  0.1,+ |  Undefined  
GRIDINC |  Grid interval for the interpolated points beyond the limits of the original point data. |  Yes |  Undefined |  0.1,+ |  Undefined  
TR |  Flag to indicate whether the field in the wireframe triangle file should have different values depending on whether or not the triangle is in the extrapolated area: 0 = all triangles have colour defined by parameter 1 . 1 = triangles in the area covered by **POINTIN** data are coloured 1 and those in the extrapolated area are coloured 2. |  No |  0 |  0,1 |  0,1  
1 |  Colour field for the output points and wireframe triangles for data lying within the area covered by **POINTIN** data. |  No |  1 |  1,64 |  Undefined  
2 |  Colour field for the output point data file for data points which have been extrapolated. If parameter **TR** is set to 1, then triangles in the extrapolated area will also have this colour; otherwise they is 1. If the parameter 2 is undefined then it is set equal to 1. |  No |  Undefined |  1,64 |  Undefined  
  
Related topics and activities

  * [MAKEDTM Process](<makedtm.md>)