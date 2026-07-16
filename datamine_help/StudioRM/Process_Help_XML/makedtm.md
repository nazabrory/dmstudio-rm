# MAKEDTM Process

To access this process:

  * Enter "MAKEDTM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MAKEDTM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MAKEDTM>).

## Process Overview

**MAKEDTM** generates a DTM file from points data in a file, which is optionally subdivided or constrained using one of the following inputs:

  * Closed perimeter data
  * String files

Point coordinate fields will be automatically detected if possible, but can be reviewed/edited using the Fields tab.

Note: For interactive DTM creation from loaded string or point data, see [dtm-create ("md")](<../command_help/dtm-create.md>).

### Make Diagonals Consistent

You can form a DTM from one or more input string or points objects (or a combination). However, where point data is common between multiple objects (meaning there are coincident data points in the set used to form the DTM), it is possible for surface triangulation to be performed in a different way, and often unexpectedly so, compared to the outcome if data were sourced from a single object (without coincident points). 

To mitigate this possibility, the Make Diagonals Consistent option can be checked to ensure the surface generated between disparate data sets is performed identically, ensuring the combined DTM matches the triangulated output from a single data object input.

Note: Selecting this option can introduce a performance hit, so where large coincident data overlaps are known to occur between input objects, it may be more efficient to combine data first into a single object (say, using the [Copy from Object(s)](<../COMMON/CopyDataFromDialog.md>) screen) before generating a DTM.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  Input perimeter file containing XP,YP,ZP,PTN, PVALUE fields. Closed strings will be used as boundaries to the triangulation, and may be included in the triangulation if @INCPERIM is 1. |  Input |  See desc |  Strings  
STRINGIN |  Input string file containing XP,YP,ZP,PTN and PVALUE fields. String segments are included in the triangulation as 3D edge constraints, breaklines. Strings may be open or closed. |  Input |  See desc |  Strings  
POINTSIN |  Input point file containing XPT,YPT,ZPT fields. |  Input |  See desc |  Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETR |  Output |  Yes |  Wireframe triangles |  Output wireframe triangle file.  
WIREPT |  Output |  Yes |  Wireframe points |  Output wireframe points file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
XPT |  X field in input file |  **PERIMIN** , **STRINGIN** or **POINTSIN** |  Yes |  Numeric |  Undefined  
YPT |  Y field in input file |  **PERIMIN** , **STRINGIN** or **POINTSIN** |  Yes |  Numeric |  Undefined  
ZPT |  Z field in input file |  **PERIMIN** , **STRINGIN** or **POINTSIN** |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
BOUNDARY |  Boundary specifier for perimeters:

  * 0 - outermost strings are an external boundary. 
  * 1 - outermost strings are an internal boundary. 

|  No |  0 |  0,1 |  0,1  
INCPERIM |  Include perimeter strings in the triangulation :

  * 0 - perimeter strings are NOT included within the triangulation. 
  * 1 - perimeter strings ARE included within the triangulation. 

|  No |  1 |  0,1 |  0,1  
TOL |  Tolerance distance below which points can be moved to avoid sliver triangles around breaklines |  No |  0.00001 |  Undefined |  Undefined  
FLATTRI |  Avoid flat triangles:

  * 0 - do not avoid flat triangles. 
  * 1 - flip connection to try to avoid flat triangles. 

|  No |  0 |  0,1 |  0,1  
TRIM |  Trim edge triangles:

  * 0 - do not trim edge triangles. 
  * 1 - iteratively remove triangles from the edge of the dtm until the constraints from @**TRIMANG** and @**TRIMLEN** are met. 

|  No |  0 |  0,1 |  0,1  
TRIMANG |  Minimum (2D) angle allowed in an edge triangle to avoid trimming |  No |  0 |  0,360 |  Undefined  
TRIMLEN |  Maximum (2D) edge length allowed in an edge triangle to avoid trimming |  No |  0 |  Undefined |  Undefined  
CREST |  Add automatic crest spurs to minimise upper plateaus:

  * 0 - do not add crest spurs. 
  * 1 - add crest spurs. 

|  No |  0 |  0,1 |  0,1  
CRESADJ |  Vertical distance to offset the crest spurs |  No |  0 |  Undefined |  Undefined  
VALLEY |  Add automatic valley spurs to minimise lower plateaus:

  * 0 - do not add valley spurs. 
  * 1 - add valley spurs. 

|  No |  0 |  0,1 |  0,1  
VALLEYADJ |  Vertical distance to offset the valley spurs |  No |  0 |  0,1 |  0,1  
KEY |  Add automatic key spurs:

  * 0 - do not add key spurs. 
  * 1 - add key spurs. 

|  No |  0 |  0,1 |  0,1  
DIAGONAL |  Manage triangulation between multiple input data objects.

  * 0 Do not attempt to align triangulation between different input data.
  * 1 Ensure triangulation between different objects is consistent.

| No | 0 |  0,1 |  0,1  
  
Related topics and activities

  * [dtm-create ("md")](<../command_help/dtm-create.md>)