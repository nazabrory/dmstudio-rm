# CONPOL Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Convex Polygon**.
  * **Data** ribbon **> > Data Tools >> 3D Utilities >> Convex Polygon**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CONPOL** and click **Run**.
  * Enter "COMRES" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CONPOL>).

## Process Overview

Create a convex polygon around an X,Y point data set.

To prevent large areas within the polygon having no data, a maximum chord length can be specified for the perimeter, so that the perimeter clings to the limits of the data creating a concave perimeter. The perimeter is established wih a PVALUE of 1.0, and a ZP value of 0.0. The standard perimeter file that is output will only have one perimeter.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  Output Perimeter file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate field on input file. |  IN |  Yes |  Numeric |  Undefined  
Y |  Y coordinate field on input file. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MAXLEN |  Maximum chord length, which should be greater than the distance between separate groups of data if all groups are to be included in the one perimeter and greater than the average point separation.  
|  No |  Undefined |  Undefined |  Undefined  
EXTDIS |  Distance to extend the perimeter (0).  
  
|  No |  0 |  Undefined |  Undefined  
CHECKDUP |  Check for duplicate points in the input file. If this is turned on (set to 1) then processing takes much longer. For data sets with more than a few thousand points it is recommended that this is turned off (set to 1). Duplicate points can be removed from the input data file by using the FILTPO process before running CONPOL. =0 : Do not check for duplicate points - processing is much faster. =1 : Check for duplicate points. |  No |  0 |  Undefined |  Undefined