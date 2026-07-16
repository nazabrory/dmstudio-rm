# SUDTTR Process  
  
To access this process:

  * Enter "SUDTTR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUDTTR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUDTTR>).

## Process Overview

Read in a legacy SURPAC .DTM system file (SURPAC v1) and create two related Datamine files.

&**WIREPT** is a file containing a list of point coordinates. &**WIRETR** is a file containing point triples which define triangles. These files are the same as those output by **[SURTRI](<surtri.md>)**.

* * *

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETR |  Output |  Yes |  Wireframe Triangle |  Wireframe triangle data file with the fields **TRI-NO,PT1,PT2,PT3**.  
WIREPT |  Output |  Yes |  Wireframe Points |  Wireframe point data file with the fields **PTN,XP,YP,ZP**.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SID |  Surface identifier with a lower surface having the value -1, and a top surface the value +1 (-1). |  Yes |  -1 |  Undefined |  -1,1  
  
## Example
    
    
    !SUDDTR    &WIREPT(SURVPT), &WIRETR(SURVTR),@SID=-1SYSFILE >UPD.DTM  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SYSTEM FILE NOT FOUND |  The SURPAC .DTM file has not been found. Fatal; the process is exited.  
>>> NOT ENOUGH ROOM FOR THE REQUIRED FIELDS |  Not enough room for the required fields in the output point file or triangle file. Fatal; the process is exited.  
>>> UNEXPECTED END-OF-FILE WHEN READING .DTM FILE |  Fatal; the process is exited.  
>>> DTM HAS INVALID VALUE(S) OR IS CORRUPT >>> LINE IS ..... |  Fatal; the process is exited.