# SURVOU Process

To access this process:

  * Enter "SURVOU" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SURVOU** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SURVOU>).

## Command Overview

**SURVOU** is a data format conversion process. It requires as input a point file containing the coordinates of each unique point in the survey database and a string segment file containing the links between those points to form strings. These files are output by [SURTAC](<surtac.md>) and [SURVIG](<survig.md>).

**SURVOU** creates an output perimeter file of the type used in mine planning, and surface modeling processes. Points that are stored in the input point file but are not linked within a string will be output to a points file. This allows a file of unconnected points to be supplied as input to the surface digital terrain modelling process [SURTRI](<surtri.md>). 

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
POINTIN |  Input point file. This will contain fields PID, X, Y, Z, PSYMBOL, PSYMSZE, P and PERIOD (numeric, explicit). |  Input |  Yes |  Undefined  
SEGIN |  Input string segment file. This will contain PID1, PID2, PVALUE, PTYPE, PCODE, P. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOU |  Output |  Yes |  String |  Output perimeter file. This will contain the fields XP, YP, ZP, PTN, PVALUE, PTYPE, PCODE, P, PSYMBOL, and PSYMSZE. Additional fields found in the input files will be added to the output perimeter file.  
POINTOU |  Output |  Yes |  Undefined |  Output point file. This will contain fields PID, XP, YP, ZP, PSYMBOL, PSYMSZE, P and PERIOD (numeric, explicit).  
  
## Example
    
    
    !SURVOU &POINTIN(PTIN1), &SEGIN(SEGIN1), &PERIMOU   
  
---  
      
    
     (PEROU1), &POINTOU(PTOU1)  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
*** Error - one or more of the required files have not been specified. &POINTIN , &STRINGIN, &PERIMOU must be specified by the user. |  One or more of the required file names have not been supplied by the user, when running the process.Fatal; the process will be exited. |  Re-enter the process and supply all compulsory file names.  
*** Error - reading input point file XXXXXXXX. |  An error has occurred when reading the input point file. Fatal; the process will be exited. |  Check the integrity of this file by listing the data definition and data in the editor (AED).  
*** Error - reading input string segment file XXXXXXXX. |  An error has occurred when reading the input string segment file. Fatal; the process will be exited. |  Check the integrity of this file by listing the data definition and data in the editor (AED).  
*** Error - missing field FFFFFFFF in input point file XXXXXXXX. |  The input point file XXXXXXXX is missing an essential field, named FFFFFFFF. Fatal; the process is exited. |   
*** Error - missing field FFFFFFFF in input string file XXXXXXXX. |  The input string segment file XXXXXXXX is missing an essential field, named FFFFFFFF. Fatal; the process is exited. |   
*** Error - writing output perimeter file XXXXXXXX. |  This error may occur as a result of a full hard disk. Fatal; the process is exited. |   
*** Error - writing output point file XXXXXXXX. |  This error may occur as a result of a full hard disk. Fatal; the process is exited. |   
  
Related topics and activities

  * [SURCAL Process](<surcal.md>)

  * [SURFIP Process](<surfip.md>)

  * [SURLOG Process](<surlog.md>)

  * SURVOU Process

  * [SURPOI Process](<surpoi.md>)

  * [SURTAC Process](<surtac.md>)

  * [SURTRI Process](<surtri.md>)

  * [SURVIG Process](<survig.md>)

  * [SURVIN Process](<survin.md>)