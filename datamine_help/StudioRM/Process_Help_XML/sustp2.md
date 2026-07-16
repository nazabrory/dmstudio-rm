# SUSTP2 Process

To access this process:

  * Enter "SUSTP2" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUSTP2** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUSTP2>).

## Command Overview

Create a perimeter file from a SURPAC2 string file.

The last point on a SURPAC string file is not output if it matches the first point (and hence indicates a closed string). Isolations are given unique PVALUEs.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  String |  Output perimeter file with the standard fields PVALUE,PTN,XP,YP,ZP plus STRNO, which contains the SURPAC string number. Additional fields in the SURPAC file are returned as D0,D1,...D9 if they exist.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DIRECT |  Parameter to specify the plane of the STRing file: 1=XY, 2=XZ, 3=YZ. |  Yes |  1 |  1,3 |  1,2,3  
  
Related topics and activities

  * [SUSTPE Process](<sustpe.md>)