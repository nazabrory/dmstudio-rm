# ADDTRI Process

To access this process:

  * **Wireframe** ribbon **> > Process >> Add Wireframes**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ADDTRI** and click **Run**.
  * Enter "ADDTRI" into the****[Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ADDTRI>).

## Process Overview

Combines two pairs of wireframe model files, into a single pair of output files.

The names of the first two wireframe files may be the same as the output file names, similar to the [APPEND](<append.md>) process. This process combines the files correctly, and renumbers the PID numbers so that the output wireframe files may be subsequently processed.

Normally, a ZONE field in the input triangle files will exist, so that the structures in the different files may still be identifiable in the combined triangle file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR1 |  Input wireframe triangle file 1. |  Input |  Yes |  Wireframe Triangle  
WIREPT1 |  Input wireframe point file 1. |  Input |  Yes |  Wireframe Points  
WIRETR2 |  Input wireframe triangle file 2. |  Input |  Yes |  Wireframe Triangle  
WIREPT2 |  Input wireframe point file 2. |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETROU |  Output |  Yes |  Wireframe Triangle |  Output wireframe triangle file.  
WIREPTOU |  Output |  Yes |  Wireframe Points |  Output wireframe point file.  
  
## Note

Effectively an 'append', ADDTRI does not check for interpenetration of the two wireframes, but simply combines them into a single wireframe model.

## Example
    
    
    !ADDTRI    &WIREPT1(ZON1PT), &WIRETR1(ZON1TR), &WIREPT2(ZON2PT),   
  
---  
      
    
    &WIRETR2(ZON2TR), &WIREPTOU(TOTPT), &WIRETROU(TOTTR)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> aaaaaaaa AND bbbbbbbb FILENAMES ARE THE SAME - ILLEGAL |  The &WIREPT1 and &WIRETR1, &WIREPT2 and WIRETR2, or &WIREPTOU and &WIRETROU file names are the same. aaaaaaaa is the name of the file on &WIREPT1, &WIREPT2 or &WIREPTOU; bbbbbbbb is the name of the file on &WIRETR1, &WIRETR2 or &WIRETROU. Fatal; the process is exited.  
>>> FATAL ERROR -- ATTEMPTING ILLEGAL IN-PLACE OPERATION |  An illegal in-place operation has been attempted i.e. the name of the file on &WIREPTOU is the same as that on &WIREPT2 or the file on &WIRETROU is the same as that on &WIRETR2. Fatal; the process is exited.   
>>> ERR 121 <<< ( n) IN ADDTRI |  An error has occurred when reading one the input point or triangle files e.g. one or more of the essential fields in the file is absent or of the wrong type. Fatal; the process is exited.   
  
Related topics and activities

  * [COMBTRI Process](<combtri.md>)

  * [COMBMOD Process](<combmod.md>)

  * [Merge Tables](<../COMMON/Merge%20Tables%20Dialog.md>)

  * [Boolean and Plane Calculations](<../COMMON/boolean_operations.md>)