# SUSTPE Process

To access this process:

  * Enter "SUSTPE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUSTPE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUSTPE>).

## Command Overview

Imports a SURPAC string file (assumed to be closed perimeters, but only the case if the last and first SURPAC points are duplicated) into a Datamine perimeter file.

Uses the STRing number as the perimeter number and depending on the value of @DIRECT will load the string file into the perimeter file XP,YP,ZP fields appropriately.

The user is required to know the orientation of the string file coordinates ie section or plan.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  String |  Output perimeter file with the standard fields PVALUE,PTN,XP,YP,ZP.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DIRECT |  Parameter to specify the plane of the STRing file: 1=XY, 2=XZ, 3=YZ. | Yes | 1 | 1,3 | 1,2,3  
  
## Example
    
    
    !SUSTPE    &OUT(UPDSTR), @DIRECT=1SYSFILE >UPD.STR  
  
---  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> SYSTEM FILE NOT FOUND |  The SURPAC *.str file has not been found. Fatal; the process is exited. |  Check the filename and path for the *.str file.  
>>> NOT ENOUGH ROOM FOR THE REQUIRED FIELDS |  Not enough room for the required fields in the output perimeter file. Fatal; the process is exited. |  Check the number and size of the fields in the &OUT file.  
>>> UNEXPECTED END-OF-FILE WHEN READING .STR FILE |  Fatal; the process is exited. |  Check the *.str file format.  
>>> .STR HAS INVALID VALUE(S) OR IS CORRUPT LINE IS ..... |  Fatal; the process is exited. |  Check the *.str file data.  
>>> @DIRECT DOES NOT HAVE THE VALUE 1,2 OR 3 |  Fatal; the process is exited. |  Specify a value of 1, 2,or 3 for the @DIRECT parameter.  
  
Related topics and activities

  * [SUSTP2 Process](<sustp2.md>)