# SURVIN Process

To access this process:

  * Enter "SURVIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SURVIN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SURVIN>).

## Command Overview

**SURVIN** is a data format conversion process.

**SURVIN** requires as input a file of perimeters and/or strings of points that may represent boundaries of planned or actual mine development. The file may have been output from a mine planning process, or digitized from mine plans.

**SURVIN** creates a file containing a record for each unique point within the perimeter file, with associated point attributes, and a file containing the links between points in the same string and the string identification values. The point and segment files may then be used as input to the survey editor to enable interaction of planned development with survey stations and surveyed features, thus allowing listings to be produced of the measurements required by the surveyor to set out excavation lines for operational production control.

If two points in the perimeter file are within the tolerance distance parameter @**TOL** supplied by the user, it is not duplicated in the output point file but the link is stored in the string segment file for the string concerned. The distance between points is computed between their three-dimensional coordinate positions.

If the input perimeter file does not contain the fields **PSYMBOL** , **PSYMSZE** , **P** , **PTYPE** , **PCODE** , the corresponding parameters must be supplied by the user, and will be assigned as constants in the output point and string files.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  Input perimeter file. Must contain the fields XP, YP, ZP, PTN and PVALUE (numeric, explicit). Optional fields PTYPE, PCODE, P, PSYMBOL, and PSYMSZE will be used, if present. Additional fields found will be added to the output point and string files. |  Input |  Yes |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
POINTOU |  Output |  Yes |  Undefined |  Output point file. This will contain fields PID, X, Y, Z, PSYMBOL, PSYMSZE, P and PERIOD (numeric, explicit).  
SEGOU |  Output |  Yes |  Undefined |  Output string segment file. This will contain the fields PID1, PID2, PVALUE, PTYPE, PCODE, P and PERIOD (numeric, explicit).  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PERIOD |  Numeric integer period number for to be assigned to the input perimeters. |  Yes |  Undefined |  Undefined |  Undefined  
TOL |  Points in the perimeter file less than TOL distance apart will be deemed duplicate and rejected.(0.1) |  No |  0.1 |  Undefined |  Undefined  
PTYPE |  PTYPE field value [numeric] to be stored in the string file, representing a string type, if not found in perimeter file.(1) |  No |  1 |  Undefined |  Undefined  
PCODE |  PCODE field value to be stored in string file, representing a line code 1001-1008, if not found in the perimeter file.(1001) |  No |  1001 |  Undefined |  Undefined  
P |  P field value [numeric] to be stored in point and string files, representing a point symbol and string line colour, if not found in perimeter file.(1) |  No |  1 |  Undefined |  Undefined  
PSYMBOL |  PSYMBOL field value [numeric] to be stored in the point file, representing a point symbol number 91-98, if not found in the perimeter file.(92) Point symbol number 91 : Circle (o) 92 : Cross (+) 93 : Cross (x) 94 : Triangle 95 : Box 96 : Diamond 97 : Star ( ) |  No |  92 |  91,98 |  91,92,93,94,95,96,97,98  
PSYMSZE |  PSYMSZE field value [numeric] to be stored in the point file, representing a point symbol size in mm, if not found in the perimeter file.(1.5) |  No |  1.5 |  Undefined |  Undefined  
  
## Example
    
    
    !SURVIN    &PERIMIN(PERUPD1), &POINTOU(PNTUPD1), &SEGOU(SEGUPD1),          
  
---  
      
    
    @PERIOD=3, @TOL=0.05, @PTYPE=3, @PCODE=1004,          
      
    
    @P=4, @PSYMBOL=94, @PSYMSZE=2.5  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
*** Error - The input file AAAAAAAA is not a valid perimeter file. |  The input perimeter file does not contain the compulsory numeric fields XP,YP,ZP,PTN,PVALUE. Fatal; the process is exited. |  Ensure that the perimeter file &PERIMIN contains the compulsory numeric fields XP, YP, ZP, PTN, PVALUE.  
*** Warning - Record NN in input perimeter file AAAAAAAA contains absent data for one of the fields XP,YP,ZP,PVALUE. |  This record is ignored. |  Check the data.  
  
Related topics and activities

  * [SURCAL Process](<surcal.md>)

  * [SURFIP Process](<surfip.md>)

  * [SURLOG Process](<surlog.md>)

  * SURVIN Process

  * [SURPOI Process](<surpoi.md>)

  * [SURTAC Process](<surtac.md>)

  * [SURTRI Process](<surtri.md>)

  * [SURVIG Process](<survig.md>)

  * [SURVOU Process](<survou.md>)