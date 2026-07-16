# FILTPO Process

To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Filter Points**.

  * Enter "FILTPO" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FILTPO** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FILTPO>).

## Process Overview

Remove coincident or adjacent points either within a single file or by using a second filter file.

The optional parameter @**RADIUS** allows the user to define a search radius within which points are considered to be coincident the first point will be copied to the output file.

If a filter file is used then points from the &**IN1** file are copied to the &**OUT** file only if they do not lie within @**RADIUS** of a point in the &**IN2** file.

**Note** : The input points file (&**IN1**) must be sorted on the *X coordinate field.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input points file. Must be sorted on X. |  Input |  Yes |  Undefined  
IN2 |  Optional filter points file. Must be sorted on X. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output points file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field used as X coordinate for filter process. |  IN1 |  Yes |  Numeric |  Undefined  
Y |  Field used as Y coordinate for filter process. |  IN1 |  Yes |  Numeric |  Undefined  
Z |  Optional Z coordinate for filter process. |  IN1 |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
RADIUS |  Optional, default = 0.0. Points within RADIUS of one another are filtered out. If Z is not defined, filter test is applied in a circle in the XY plane. If Z is defined filter test is applied within a sphere. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !FILTPO &IN1(POINTS),&OUT(POINTS.F),*X(EAST),*Y(NORTH),  
  
---  
      
    
    *Z(RL),@RADIUS=0.1  
      
    
       
  
## Error and Warning Messages

Message |  Description  
---|---  
!!! MISSING INPUT POINTS FILE (&IN1) !!! |  The input points file was not specified. Fatal; the process is exited.  
!!! INVALID FILTER FILE (&IN2) !!! |  The specified filter file is not a valid filter file. Fatal; the process is exited.  
!!! MISSING OUTPUT POINTS FILE (&OUT1) !!! |  The output points file was not specified. Fatal; the process is exited.  
!!! FILTPO CANNOT FILTER IN-PLACE !!! |  An invalid in-place operation was attempted. Fatal; the process is exited.  
!!! ATTEMPT TO OPEN nnnnn FILE!!! |  The specified file could not be opened. Fatal; the process is exited.  
!!! n FIELD NOT NUMERIC !!! |  One of the fields in the input files which was expected to be numeric is not (e.g. X, Y, Z). Fatal; the process is exited.  
!!! n FIELD NOT AN EXPLICIT FIELD !!! |  One of the fields in the input files which was expected to be explicit is not (e.g. X, Y, Z). Fatal; the process is exited.  
!!! n FIELD MISSING !!! |  The specified field is missing from the input files. Fatal; the process is exited.  
!!! INVALID FILTER RADIUS PARAMETER !!! |  The specified radius parameter is incorrect. Fatal; the process is exited.  
!!! FILTER FILE NOT SORTED ON "X" FIELD !!! |  The input filter file is not sorted on the *X coordinate field. Fatal; the process is exited.