#  TRIVOL Process  
  
To access this process:

  * **Wireframe** ribbon **> > Process >> Wireframe Proceses >> Volume**.

  * Enter "TRIVOL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **TRIVOL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TRIVOL>).

## Process Overview

Reports volume and other statistics of a wireframe model.

Note that the NOSID parameter will have an effect on wireframe volume calculations.

Parameters

TRIVOL contains several parameters to control the process of generating statistics, including:

  * NOSID: This can be set to 1 to disable the checking of internal surfaces. This can be used on verified wireframes or DTMs, even if the triangle file does not contain the fields NORMAL-X, NORMAL-Y and NORMAL-Z.  
  
Using a value of NOSID on a previously verified wireframe makes processing much faster.  
  
If the fields NORMAL-X, NORMAL-Y and NORMAL-Z are present in the triangle file they will be used for detection of internal surfaces in preference to the NOSID parameter. These fields can be optionally output when using the wireframe-verify command.
  * DTM: This can be set to 1 to make the processing time faster if you are confident that the input wireframe is a DTM with no overlaps.
  * ZONE: TRIVOL supports alpha ZONE fields of up to 10 characters long. Records with absent ZONE values are counted and reported as a warning but a volume is still calculated for absent ZONES.

**Note** : The name of the input triangle file to **TRIVOL** is recorded in an implicit field in the output results fille..

The information output includes:

  * Total volume above minimum elevation

  * Volume above @ZBASE value

  * Projected lower area

  * Projected upper area

  * Total surface area

  * Minimum elevation

  * Maximum elevation

  * Minimum X co-ordinate

  * Maximum X co-ordinate

  * Minimum Y co-ordinate

  * Maximum Y co-ordinate

  * Minimum surface dip

  * Maximum surface dip

  * Number of triangles

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
PERIMIN |  Optional input perimeter file containing **XP,YP,ZP** fields, defining perimeter(s) within which volume is to be computed. |  Input |  No |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  Optional output file, which will contain the fields **VOLUME, UPPERVOL, LOWAREA, UPAREA, TOTAREA, MINZ, MAXZ, MINX, MAXX, MINY, MAXY, MINDIP, MAXDIP, NUMTRI** , and the optional zone definition file, if one is specified.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ZONE |  Zone definition field in triangle file. |  WIRETR |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ZBASE |  Base elevation above which volumes are computed. |  Yes |  Undefined |  Undefined |  Undefined  
NOSID |  |  Option |  Description  
---|---  
1 |  Disables checking of SIDs for increased speed. Use for single surfaces only.  
No |  1 |  0,1 |  0,1  
DTM |  |  Option |  Description  
---|---  
1 |  Disables checking of overlaps for specified DTM input files (quicker)  
No |  1 |  0,1 |  0,1  
  
## Example
    
    
    !TRIVOL  &WIREPT(TOPOPT),&WIRETR(TOPOTR),*ZONE(ROCK),@ZONE=1,          
  
---  
      
    
    @ZBASE=110.0  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> NO DATA IN INPUT FILE <<< >>> ERR 136 <<< ( n) IN TRIVOL |  The input wireframe point data file has no data. Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELDS IN PERIMETER FILE <<< >>> ERR 143 <<< ( n) IN TRIVOL |  Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELDS IN WIREPT FILE <<< >>> ERR 145 <<< ( n) IN TRIVOL |  Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELDS IN WIRETR FILE <<< >>> ERR 146 <<< ( n) IN TRIVOL |  Fatal; the process is exited.