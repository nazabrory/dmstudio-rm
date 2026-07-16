# LAYOUT Process

To access this process:

  * Enter "LAYOUT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **LAYOUT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LAYOUT>).

Note: This process is not actively developer, and has been superseded by Datamine's Ore Controller solution. Contact your local Datamine office for details.

## Process Overview

Lay out a blast pattern.

You pick a blast from the input file to work on; this defines both the Bench and Blast numbers which will remain in force until a new blast is chosen.

If the blast specified is not on file (for example, blast 0) then all holes on the input file will be read, and a dummy rectangular outline constructed around them. The program automatically works out the co-ordinate limits of this blast, and will compute a rotation angle to align the major axis of the blast along the screen X axis; the user may override this if required. The blast is then shown on the graphics screen.  
A set of grid lines in the original co-ordinate system is also shown, rotated if the blast was rotated. Different colours may be chosen (under user control) for the two axes, to give an indication of which axis is which. A suitable grid size is chosen automatically, but the user may change or suppress this if required (DEFAULTS [/CF] command).

If there are any existing blast-holes on file, these may be read in (GET HOLES [/FO] command) and displayed. A set of colours is automatically chosen to display blast-hole grades in, based upon the first grade field found in the blast-hole file (if any). The user may choose different fields, colours, grade ranges etc. by use of the BLASTHOLE DISPLAY [/CD] command.

A title is automatically generated giving the Bench and Blast numbers; again, this may be substituted by use of the TITLE [/DT] command.

## Laying Out Blast Holes

The LAY DOWN PATTERN [/BP] command is used to place one of the defined blast-hole patterns into the Blast outline. The orientation of the blast rows is chosen either by defining two points with the cursor, or by selecting an existing line. The position of the first hole is chosen by cursor and an optional offset may also be entered. The chosen pattern is then laid down within the Blast outline.

Because different parts of the blast often require different patterns, a perimeter may also be defined (DIGITISER [/CD] or NEW PERIMETER [/EN]) before the holes are laid out. The pattern will then be laid within this perimeter as well as within the Blast Outline.

Perimeters may also be used to selectively remove holes either inside or outside any defined region (the CUT HOLES IN PERIM [/DC] command). These perimeters may be stored on the OUTLINES file for future use.

Individual holes may be entered or removed as required through the DEFINE HOLE [/BD] command. A useful feature here, especially when joining two patterns which are at an angle to each other, is the ability to define a new hole halfway between two existing holes.

All holes for the current Blast are stored in an internal working array. These may be written to the HOLES file at any time by the WRITE BLAST HOLES [/FL] command, or retrieved by the GET HOLES [/FO] command. There is no limit to the number of holes that may be defined in a Blast.

Holes may be sequentially numbered by the NUMBER HOLES [/BN] command. If the automatic method of numbering is chosen, then holes are numbered from the top row (as displayed on the screen) to the bottom, on the assumption that the user has oriented the Blast appropriately. A manual method of numbering is also supplied. A third method allows holes to be numbered according to distance from a user-supplied line or string.

## Coordinate Systems

**LAYOUT** can handle either a conventional right-handed co-ordinate system, or the inverted LO co-ordinate system as used in many parts of Africa. If the LO system is used, then all co-ordinates (for perimeters, blast-holes and geology) must be input in this system. The optional parameter COORDTYP is set to 1, and the parameters LOYORIG and LOXORIG must be set to provide a reference point for the system to use for internal data transformation. This internal system is completely transparent to the user, who does not need to use it; all input/output is in the LO system.

## Stopping and Restarting

Because most files are keyed by Bench, Blast and Composite number, many different blasts may safely be dealt with in a single set of files. Since LAYOUT will set up any output files with all the appropriate fields if they do not exist on input, there is no need to worry about the format of the output files the first time around. The system has been designed to use these files for both input and output, so that a blast layout can be halted (and LAYOUT exited) mid-way through; re-entry into LAYOUT with the same files and parameters as before will allow the blast layout to be restarted from exactly where it stopped.

## Patterns

Up to 12 blast-hole layout patterns may be defined and stored in the PATTERNS file for use as required. These patterns are defined by row and column spacing and row offsets for up to 5 different rows. For a simple rectangular pattern, only a single row is required. These patterns may be stored in the PATTERNS file and selected as required. The SELECT PATTERN [/BS] command selects a particular pattern, while the UPDATE PATTERN [/BU] command updates patterns. Both commands show all available patterns on the graphics screen, at the scale currently selected.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Blast outline for composite design. The file must contain the fields:- XP,YP,ZP,PTN,PVALUE (numeric, explicit). It may also contain the field BENCH; if it does not contain this field, all bench numbers will be taken as 1\. The PVALUE field contains a Blast number. The file may contain many blasts; one is selected at the start of the process. |  Input |  Yes |  String  
TEXT |  Input/output text file for text added to the drawing. If this file does not exist, it will be created. If it does exist, it must have the fields BENCH, BLAST, COMPOSIT, XT, YT, ANGLE, CHARSIZE, ASPRAT, (all numeric) and TEXT (40 characters).  Any existing text in the file for the current bench and blast will be plotted on the screen. |  Overwritten |  Yes |  Undefined  
OUTLINES |  Input/output perimeters. If this file does not exist, it will be created. It must contain the fields XP, YP, ZP, PTN, PVALUE, P, PTYPE, BENCH, BLAST. The PVALUE field will contain the perimeter number.  Any perimeter defined with the DIGITISER [/CD] or NEW PERIMETER [/EN] commands may be written to the OUTLINES file by the WRITE PERIMETER [/FW] command. Perimeters will be overwritten if they match the perimeter number (PVALUE) of the perimeter being written. |  Overwritten |  Yes |  String  
PATTERNS |  Input/output pattern file. If this file does not exist, it will be created. It must contain the fields ROW, XS, XSPACING, YSPACING, PATTERN (all numeric) and PATTEXT (16 character alphanumeric). |  Overwritten |  Yes |  Undefined  
COLLARS |  Input/output collars file. Fields required are XCOLLAR, YCOLLAR, ZCOLLAR, BENCH, BLAST and BHID (A/N). Additional fields used if available are BRG, DIP, HLENGTH, PATTERN, NSAMP and SNFIRST. If this file does not exist it will be created with all the above fields. At least one of the COLLARS or HOLES files must be specified. |  Overwritten |  No |  Undefined  
HOLES |  Blast hole samples file. Fields required are X, Y, Z and BHID (A/N). Additional fields used if available are BENCH, BLAST, A0, B0, LENGTH, SAMPLE, FROM and TO. If this file does not exist it will be created with all the above fields.  If it contains any grade values, these may be displayed either numerically or by colour besides each blast-hole. This file will be written to by the WRITE BLAST HOLES [/FL] command. If any entries exist on the file for the current Bench and Blast they will first be overwritten.  If the BENCH and BLAST fields do not exist, then all entries will be deleted before the new holes are written. At least one of the COLLARS or HOLES files must be specified. |  Overwritten |  No |  Undefined  
GEOL |  Geological boundaries. This file must contain the fields X,Y,Z,PTN and PVALUE.  The values are assumed to be (unclosed) strings rather than perimeters. Any strings on this file may be plotted over the blast. |  Input |  No |  String  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
COORDMOD |  Coordinate verification mode, controls the prompting for coordinates in the LAY DOWN PATTERN [/BP] and DEFINE HOLE [/BD] commands. |  Option |  Description  
---|---  
0 |  No coordinate prompting  
1 |  Coordinates are prompted for.  
No |  0 |  0,1 |  0,1  
COORDTYP |  Coordinate type: |  Option |  Description  
---|---  
0 |  Conventional rhs  
1 |  LO co-ordinate system.  
No |  0 |  0,1 |  0,1  
LOYORIG |  For **COORDTYP** =1 only; the LO Y co-ordinate origin [including \- sign] for internal co-ordinate conversion. |  No |  Undefined |  Undefined |  Undefined  
LOXORIG |  For **COORDTYP** =1 only; the LO X co-ordinate origin for internal co-ordinate conversion. |  No |  Undefined |  Undefined |  Undefined  
HAXISCOL |  Colour for horizontal axis lines; these are X axis lines [ **COORDTYP** =0] or LO Y lines [ **COORDTYP** =1] (8). |  No |  8 |  1,64 |  Undefined  
VAXISCOL |  Colour for vertical axis lines; these are Y axis lines [ **COORDTYP** =0] or LO X lines [ **COORDTYP** =1] (10). |  No |  10 |  1,64 |  Undefined  
CHARSIZE |  Character size for display in mm (3). |  No |  3 |  Undefined |  Undefined  
DIMENU |  Toggle between cursor and digitiser mode. |  Option |  Description  
---|---  
0 |  Cursor mode.  
1 |  Digitiser mode. All commands available from digitiser. Default is 0  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !LAYOUT  &IN(BLASTLAY), &TEXT(BLASTTXT), &OUTLINES(OUTL),   
  
---  
      
    
             &PATTERNS(PATTERNS), &COLLARS(COLLARS), &HOLES(BLSTHOLE),   
      
    
             &GEOL(GEOL),@COORDTYP=0, @HAXISCOL=8, @VAXISCOL=10, @CHARSIZE=3  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> FIELD ffffffff MISSING FROM BLAST OUTLINE FILE <<< |  &IN file must contain the fields XP, YP, ZP, PTN, PVALUE (numeric, explicit). Fatal; the process is exited.  
>>> COLLARS AND HOLES FILE MISSING <<< |  At least one of the &COLLARS or the &HOLES file must be specified. Fatal; the process is exited.  
>>> FIELD ffffffff MISSING FROM COLLARS FILE OR EXISTS BUT WRONG TYPE <<< |  &COLLARS file (if specified) must contain the fields XCOLLAR, YCOLLAR, ZCOLLAR, BENCH, BLAST and BHID (A/N). Fatal; the process is exited.  
>>> FIELD ffffffff MISSING FROM HOLES FILE OR EXISTS BUT WRONG TYPE <<< |  *HOLES file (if specified) must contain the fields X, Y, Z and BHID (A/N). Fatal; the process is exited.  
>>> FIELD ffffffff MISSING FROM TEXT FILE OR EXISTS BUT WRONG TYPE <<< |  &TEXT file must contain the fields BENCH, BLAST, COMPOSIT, XT, YT, ANGLE, CHARSIZE, ASPRAT, (all numeric) and TEXT (40 characters). Fatal; the process is exited.  
>>> FIELD ffffffff MISSING FROM OUTLINES FILE OR EXISTS BUT WRONG TYPE <<< |  &OUTLINES file must contain the fields XP, YP, ZP, PTN, PVALUE, P, PTYPE, BENCH, BLAST. fatal; the process is exited.  
>>> FIELD ffffffff MISSING FROM PATTERN FILE OR EXISTS BUT WRONG TYPE <<< |  &PATTERNS file must contain the fields ROW, XS, XSPACING, YSPACING, PATTERN (all numeric) and PATTEXT (16 character alphanumeric). Fatal; the process is exited.  
>>> FIELD ffffffff MISSING FROM GEOL FILE <<< |  &GEOL file must contain the fields X, Y, Z, PTN and PVALUE. Fatal; the process is exited. Not available without a COLLARS file.  
>>> No holes to remove <<< |  No holes to cut have been found inside or outside the perimeter. the command is exited.  
\---- Warning - perimeter is malformed ----  
Do you want to continue ? |  Defined current perimeter is malformed.  
\--- Perimeter unacceptable. You may either re-edit or discard it ----  
Re-edit it ? |  Defined current perimeter is still malformed.  
>>> No holes on file for this blast <<< |  No holes have been found for the current bench and blast. The command is exited.  
>>> PERIMETER NOT ON FILE <<< |  The perimeter specified is not in the &OUTLINES file. The prompt for perimeter number is reissued.  
>>> No holes to list <<< |  No holes to list were found in the working array. the command is exited.  
>>> No patterns on file - use UP to define <<< |  No patterns were found in the &PATTERNS file. The command is exited.  
>>> Pattern not on file <<< |  The pattern number specified does not exist in the &PATTERNS file. The prompt is reissued.  
>>> INVALID BLAST VALUE <<< |  An invalid blast value has been specified. The user is prompted again for the blast.  
>>> ERROR - BLAST OUTLINE NOT ON FILE <<< |  The command is exited.  
>>> ERROR - ILLEGAL BLAST OUTLINE: SCALING NOT POSSIBLE <<< |  The command is exited.  
>>> No holes to edit <<< |  No holes in the &COLLARS file have been found to edit or the &COLLARS file has not been specified. The command is exited.  
>>> No holes to number <<< |  The command is exited.  
>>> Missing orientation fields <<< >>> Invalid azimuth <<< >>> Invalid dip <<< >>> Holes do not intersect bench - HLENGTH not set. |  The command is exited  
>>> Only row numbers in the range 1 to 5 permitted |  The row number prompt is reissued.