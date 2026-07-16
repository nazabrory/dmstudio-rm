# SUPOOB Process

To access this process:

  * Enter "SUPOOB" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUPOOB** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUPOOB>).

## Process Overview

Converts a Datamine point file to a legacy SURPAC (v1) observation file.

A point number field can be supplied, or by default the point number will be incremented from 100.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input point file. |  Input |  Yes |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
PTN |  Point number field. |  IN |  No |  Numeric |  Undefined  
XP |  Easting coordinate field. |  IN |  Yes |  Numeric |  Undefined  
YP |  Northing coordinate field. |  IN |  Yes |  Numeric |  Undefined  
ZP |  RL coordinate field. |  IN |  Yes |  Numeric |  Undefined  
DESC1 |  First field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
DESC2 |  Second field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
DESC3 |  Third field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
  
## Example
    
    
    !SUPOOB     &IN(UPDPTS),*PTN(NEWPTS),*XP(North),*YP(East),  
  
---  
      
    
    *ZP (Elev)SYSFILE >UPDOBS  
      
    
    >JOBID >  
      
    
    >DATE >  
      
    
    >PURPOSE >  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> REQUIRED FILE NOT FOUND <<< |  The file specified as the &IN point file was not found. Fatal; the process is exited.  
>>> RECORD rrrrrrrr IS NOT A VALID SURPAC OBSERVATION POINT <<< |  The point from the DATAMINE point file is not a valid SURPAC observation point. Fatal; the process is exited.  
>>> ERROR READING POINT DATA FILE <<< |  An error occurred in reading the file specified as the &IN point file. Fatal; the process is exited.  
>>> ERROR OPENING SYSTEM FILE <<< |  An error occurred in opening the file specified as the SURPAC observation system file. Fatal; the process is exited.  
>>> FIELD ffffffff DOES NOT EXIST <<< |  One of the fields specified for *XP, *YP, *ZP does not exist in the &IN point file specified. Fatal; the process is exited.  
>>> POINT NUMBER OUTSIDE INTEGER RANGE (LINE = nnnnnnnnn) <<< |  The point from the DATAMINE point file is outside the valid integer range. Fatal; the process is exited.  
>>> POINT NUMBER mmmmmmmmm SHOULD BE >99 (LINE = nnnnnnnnn) <<< |  The SURPAC point number should be in the range 100 on for an observation file. Fatal; the process is exited.  
  
Related topics and activities

  * [SUPES2 Process](<supes2.md>)

  * [SUPEST Process](<supest.md>)