# PERTRA Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Create Perpendicular Strings**.

  * Enter "PERTRA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_P.md#PERTRA>)](<../command_help/COMMAND%20TABLE_E.md#EXPMMW>).

## Process Overview

Generate perimeters in planes across other perimeters.

PERTRA processes a file of input perimeters, and generates the corresponding perimeters for a set of parallel planes which intersect the planes of the input perimeters.

  * Input perimeters need not be convex but must not intersect themselves.

  * There can be more than one perimeter for each input plane.

  * Input perimeters in the same plane can enclose but not intersect each other.

  * Input perimeter planes need not be parallel to each other or perpendicular to the output planes.

  * Each input perimeter can carry an ore-body identification number (TAG) which will ensure that all points on an output perimeter refer to the same ore body.

## Input Files

  
Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  The input perimeter file. This file must contain the fields declared in the command line as **PLANE, PVALUE, PTN, X, Y** and **Z**. Note that X, Y and Z are GLOBAL coordinates. If **TAG** is declared in the command line, it must appear in this file. This file must be sorted into **PLANE, PVALUE, PTN** order. |  Input |  Yes |  String  
INTERSEC |  An optional output file of the lines of points produced where the input perimeters intersect the output perimeter planes. The output perimeters are constructed by arranging these points into lists. This file will contain fields **PLANE, LN, X, Y** and **Z**. Note that X, Y and Z are GLOBAL coordinates. A tag field will only appear if **TAG** is declared in the command line. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  No |  String |  An optional output file of perimeters in the planes indicated by the parameter values below. This file will contain fields **PLANE, PVALUE, PTN, XP, YP** and **ZP**. Note that **XP, YP** and **ZP** are GLOBAL coordinates. A tag field will only appear if **TAG** is declared in the command line. AT LEAST ONE OUTPUT FILE MUST BE SPECIFIED.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
PLANE |  Required field in **PERIMIN**. Plane identifier. This identifier must be such that, when the values are in ascending order, the planes are in sequence. **PLANE** will often be the same as X, Y or Z but cannot be the same field. It may be necessary to copy a field by using **GENTRA**. |  PERIMIN |  Yes |  Any |  Undefined  
PVALUE |  Required field in **PERIMIN**. Perimeter ID value. Note that there can be more than one perimeter in a plane but that, on input, they must not cross either themselves or each other. |  PERIMIN |  Yes |  Any |  Undefined  
PTN |  Required field in **PERIMIN**. Point number in perimeter. |  PERIMIN |  Yes |  Numeric |  Undefined  
X |  Required field in **PERIMIN**. Global X-coordinate. |  PERIMIN |  Yes |  Numeric |  Undefined  
Y |  Required field in **PERIMIN**. Global Y-coordinate. |  PERIMIN |  Yes |  Numeric |  Undefined  
Z |  Required field in **PERIMIN**. Global Z-coordinate. |  PERIMIN |  Yes |  Numeric |  Undefined  
TAG |  Optional field. Ore body identifying value. If declared in the command line, it must appear in **PERIMIN** and will appear in the output file(s). |  PERIMIN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DIRECT |  Required parameter which specifies the plane of the output perimeters. 1 = XY, 2 = XZ, 3 = YZ |  Yes |  1 |  1,3 | 1,2,3  
STARTPOS |  Required parameter which specifies the value of the coordinate perpendicular to the output plane for the first output plane. |  Yes |  Undefined |  Undefined | Undefined  
STIZE |  Required parameter which specifies the distance between output planes. |  Yes |  Undefined |  Undefined | Undefined  
NUMPLANE |  Required parameter which specifies the number of output planes. Note that no harm is done if output planes are requested which do not intersect the input perimeters. |  Yes |  Undefined |  Undefined | Undefined  
MAXDIST |  Optional parameter which specifies a distance between input planes beyond which ore bodies are not to be linked. That is, if two adjacent input planes are more than this distance apart where they intersect an output plane, the perimeters on either side of the gap will be closed off. The distance between two adjacent input planes is defined for this purpose as the distance between the closest pair of points which could logically be joined. |  No |  Undefined |  Undefined | Undefined