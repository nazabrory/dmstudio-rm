# COMBTRI Process  
  
To access this process:

  * **Wireframe** ribbon **> > Process >> Combine Wireframe**.

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COMBTRI** and click **Run**.
  * Enter "COMBTRI" into the****[Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COMBTRI>).

## Process Overview

Combines up to 20 pairs of wireframe model files, into a single pair of output files (a single wireframe).

This process is similar to [ADDTRI](<addtri.md>), however that process is restricted to combining two wireframe pair files at a time.

Note: **COMBTRI** does not check for interpenetration of the two wireframes, but simply combines them into a single wireframe model.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR1-20 |  Input wireframe triangle file 1 to 20 |  Input |  Yes |  Wireframe Triangle  
WIREPT1-20 |  Input wireframe point file 1 to 20 |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUTTR |  Output |  Yes |  Wireframe Triangle |  Output wireframe triangle file.  
OUTPT |  Output |  Automatically detected if not specified (if same name without suffix is found), otherwise must be specified. |  Wireframe Points |  Output wireframe point file.  
  
## Example
    
    
    !COMBTRI &WIREPT1(ZON1PT), &WIRETR1(ZON1TR), &WIREPT2(ZON2PT),   
  
---  
      
    
               
      
    
    &WIRETR2(ZON2TR), &OUTTR(TOTPT), &OUTPT(TOTTR)  
  
Related topics and activities

  * [ADDTRI Process](<addtri.md>)

  * [COMBMOD Process](<combmod.md>)

  * [Merge Tables](<../COMMON/Merge%20Tables%20Dialog.md>)

  * [Boolean and Plane Calculations](<../COMMON/boolean_operations.md>)