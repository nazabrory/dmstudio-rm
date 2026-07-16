# PERTAG Process  
  
To access this process:

  * Enter "PERTAG" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PERTAG** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PERTAG>).

## Process Overview

Update the TAGs in a perimeter and a TAG file. 

Updates the values of points in an input perimeter file by comparison with a reference TAG file. A match is found if a reference TAG is within a distance **MAXSEP** , otherwise a new tag is added to the file with the coordinates of the point and the maximum TAG value incremented by 1.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  Input perimeter file. Required fields are XP, YP and ZP. |  Input |  Yes |  String  
TAGFILE |  Overwritten |  Yes |  Undefined |  Input and output tag file - will be created if it doesn't already exist. Required fields are XP, YP, ZP and TAGFIELD.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  Output perimeter file. Will contain all fields in PERIMIN, plus TAGFIELD if not already there.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
TAGFIELD |  Name of numeric field to be used for tag numbers. |  TAGFILE |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MAXSEP |  The maximum distance between two points for them to be regarded as being in the same position. |  Yes |  Undefined |  Undefined |  Undefined