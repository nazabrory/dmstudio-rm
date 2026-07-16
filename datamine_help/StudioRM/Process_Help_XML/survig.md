# SURVIG Process

To access this process:

  * Enter "SURVIG" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SURVIG** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SURVIG>).

## Command Overview

**SURVIG** is an interactive graphic process, that allows the surveyor to view, edit, merge and interrogate a database of surveyed point and string data representing surface and underground mining excavations.

The input to the process may include coordinated point and string data computed from survey measurements of an update survey, a previous period survey and planned limits of excavation that the surveyor requires to establish for control of production. The processes that may have been used to create this data include:-

  * [SURTAC](<surtac.md>)

Reduction of survey tacheometry measurements.

  * **SURVIG**

Interactive graphic survey editor. Note that the output from the same process, probably representing the complete survey for the period, would be input for further modification after subsequent surveys.

  * [SURVIN](<survin.md>)

  * Convert an input perimeter file into survey format. Output perimeters representing planned limits of mining would be converted for use by the editor (**SURVIG**). The processes generating these perimeters include:-

Open pit mine-planning:

  * [LAYOUT](<layout.md>)

Blast-hole layout within a blast.

  * COMPEV

Composite design and evaluation in a blast.

Input to the process may also consist of previously defined sections and section profiles perimeters, to be used for viewing of the data and the analysis of areas and volumes.

The process utilizes up to four graphics windows that are established by the user, any of which can display sectional or isometric views at any orientation. The user can define a boundary, and this can be used to extract all points and partial segments that lie within the area updated by the survey. Having merged the update survey into the previous survey, the user can quickly generate a digital terrain model of the survey on the graphics screen.

This can be validated with assistance from the on-screen contouring, and a profile string can be produced for each of the sections defined in the section definition file. These can also be used for terrain model validation and also to carry out period volume calculations using the end-area method.

The points and strings may be queried and their display attributes or position changed. The distance, azimuth and gradient between two points can be easily found, as well as the total distance of a string of connected points and the mean gradient.

The output from the process will consist of a file containing all the unique points for the area survey, and a file containing the segments that link the points to form strings, representing features such as bench toe and crests, or roof, floor and sidewall strings of underground development. This output may then be used by the mine-planning processes listed above, after processing to create Datamine perimeter/string file:-

  * [SURVOU](<survou.md>) Convert an input perimeter file into survey format.

A plot file of the survey can be produced at any time from the current screen display. A higher quality of plot, with the addition of text and user-defined symbols and company grid, legend and title boxes can be accomplished by processing the plot file with the following processes:-

  * [PLOTFX](<plotfx.md>) Base plan plot.

### File Handling

The files associated with the **SURVIG** process are summarized below:-

  * Optional input point and segment files that represent the survey data to be updated.

  * Optional input point and segment files that represent the update survey data.

  * Output point and segment files of the survey data stored during the interactive session. This would normally represent a merge of the previous period and the update survey data.

  * Optional input/output section definition file.

  * Optional input/output profile string file, which will store the strings generated from slicing the terrain model with the defined section planes, and also any boundary or interpolated strings.

### Input survey point and string files

**SURVIG** allows the output of a section definition file containing the position, azimuth and dip of a series of section planes, to be used for viewing or the production of section profiles. As this is an input and output file, sections defined in **SURVIG** may be used in future runs of the process.

Section profiles that represent the outline of the surveyed surface where it intersects the section plane, can be produced and output for use in volume analysis between survey periods, or for use in mine planning processes where visualization of the actual excavation in relation to the planned cut is desired.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
POINTIN |  Optional input point file or prototype. |  Input |  No |  Undefined  
SEGIN |  Optional input string segment file or prototype. |  Input |  No |  Undefined  
POINTUP |  Optional input point file of update data. |  Input |  No |  Point Data  
SEGUP |  Optional input string segment file of update data. |  Input |  No |  Undefined  
SECTION |  Overwritten |  No |  Undefined |  Optional input/output section file defining sections for display, profile string generation and volume analysis, containing fields: SVALUE Section number XCENTRE X Coordinate of section centre point YCENTRE Y Coordinate of section centre point ZCENTRE Z Coordinate of section centre point SAZI Azimuth of the direction of dip. SDIP Dip of the section plane (90). STHICK Horizontal distance between adjacent sections. HSIZE Horizontal extent of section. VSIZE Vertical extent of section.  
PROFILE |  Overwritten |  No |  Undefined |  Optional input/output file of strings formed from section/terrain model slicing This file will contain standard perimeter fields XP, YP, ZP, PTN, PVALUE, and additional fields PTYPE, P, PTEXT and PERIOD.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
POINTOU |  Output |  Yes |  Point Data |  Output point file.  
SEGOU |  Output |  Yes |  Undefined |  Output string segment file.  
EVAL |  Output |  No |  Undefined |  File for output evaluations in format for input to **TABRES** process.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PERIOD |  Integer period number for storing with the updated point/string data and section profiles. |  Yes |  Undefined |  Undefined |  Undefined  
IPRCOL |  Colour of primary perimeters (5). |  No |  5 |  1,64 |  Undefined  
ISCCOL |  Colour of secondary perimeters (7). |  No |  7 |  1,64 |  Undefined  
ADDPOINT |  Maximum number additional points/strings that are likely to be required to be defined in the process (500). |  No |  500 |  Undefined |  Undefined  
COORTYP |  Parameter to be set to 1 for the use of the LO coordinate system (0). |  No |  0 |  0,1 |  0,1  
LOXORIG |  Local X origin to be used for internal coordinate calculations (0). |  No |  0 |  Undefined |  Undefined  
LOYORIG |  Local Y origin to be used for internal coordinate calculations (0). |  No |  0 |  Undefined |  Undefined  
LOZORIG |  Local Z origin to be used for internal coordinate calculations (0). |  No |  0 |  Undefined |  Undefined  
  
## Example

Open Pit Survey Update.

The following represents the command syntax required to run the SURVIG process to update a topographic survey with an open pit excavation survey and would be the required entry in a macro of commands to enter the survey editor. Note that the ** macro entry allows control to pass from the macro to the screen cursor.
    
    
    !SURVIG &POINTIN(TOPCP1),   
  
---  
      
    
    &SEGIN(TOPCS1), &POINTUP(TOPCP0), &SEGUP(TOPCS0),&POINTOU(TEMP),   
      
    
    &SEGOU(TEMP1), &SECTION(TOPCSE), &PROFILE(TOPCPR),@PERIOD=2.0,   
      
    
    @UPDCOL=1.0, @ADDPOINT=500.0, @LOADPER=1.0  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
*** Error - Field ffffffff missing in point file. |  An input point file has a missing essential field ffffffff. The file name supplied may not be a survey point file as output by the SURTAC process. |  Check the fields of the file with process DDLIST. Fatal; the process is exited.  
*** Error - Field ffffffff in point file implicit or alpha. |  An input point file has an essential numeric and explicit field ffffffff that is of the incorrect type. Fatal; the process is exited. |  If the contents of the field are correct, use ALFNUM to convert the field to numeric. If the field is implicit, it can be converted to explicit type using process FILEXP.  
*** Error - Field ffffffff missing in string segment file. |  An input segment file has a missing essential field ffffffff. The file name supplied may not be a survey segment file as output by the SURTAC process. Fatal; the process is exited |  Check the fields of the file with process DDLIST.  
*** Error - Field ffffffff in string segment file implicit or alpha. |  An input segment file has an essential numeric and explicit field ffffffff that is of the incorrect type. Fatal; the process is exited. |  If the contents of the field are correct, use ALFNUM to convert the field to numeric. If the field is implicit, it can be converted to explicit type using process FILEXP.  
*** Error - field ffffffff missing in profile file. |  The input profile file has a missing essential field ffffffff. The file may not be a standard DATAMINE perimeter file, or may be missing the PERIOD field, used to identify different surveys. fatal; the process is exited. |  In the latter case, the field can be added using the ADDDD process.  
*** Error - Storage required for points (NNNNNNNN) exceeds limit. |  The input point files and @ADDPOINT parameter require internal storage space that exceeds the limitations of the process. Fatal; the process is exited. |  Refer to the Notes section.  
*** Error - Contour minimum greater than maximum supplied. |  The minimum contour value must be less than the maximum contour value. |  Check the input values and re-run the CONTOUR [/WC] command.  
*** Error - Interval supplied does not match limits. |  The difference between the contour minimum and maximum values must be divisible by the contour interval, with no remainders. |   
*** Error - Unacceptable value : variable unchanged. |  A value has been supplied by the user that does not fall within acceptable limits. These limits vary according to the default being changed. |   
*** Error - No section file has been defined. |  A section definition file name &SECTION must be supplied by the user when running the process, to enable storage of section definitions created by this command. |   
*** Error - Cannot do this operation when snapping to grid. |  The user must be in point or line snap mode, so that the edit can be conducted on selected point or string attributes. |   
*** Error - Input point file not supplied. |  An attempt has been made to input data from input or update files that have not been supplied by the user at run-time. |   
*** Error - Input point file not supplied. |  An attempt has been made to input data from input or update files that have not been supplied by the user at run-time. |   
*** Error - String sssss.ss not found in file. |  The selected string does not exist in the input or update segment file. |  This can be checked on exit from SURVIG by using process COUNT on the input segment files, on keyfield PVALUE. This will give a listing of all string numbers in the file.  
*** Error - no more room in memory to load more strings. |  An attempt has been made to load a string when the @ADDPOINT parameter has been exceeded. |  Write all of the survey data to the output files with the WRITE SURVEY DATA [/FW] command and re-enter SURVIG with a larger @ADDPOINT value.  
*** Error - No more room available to store new point. |  The @ADDPOINT parameter has been exceeded. This error will not cause a failure in the process. |  Write all of the survey point and segment data to the output files with the WRITE SURVEY DATA [/FW] command and then re-enter SURVIG with a larger @ADDPOINT value to continue input of new data.  
*** ERROR - Out of point storage space, cannot complete new string. |  The @ADDPOINT parameter has been exceeded. This error will not cause a failure in the process. |  Write all of the survey point and segment data to the output files with the WRITE SURVEY DATA [/FW] command and then re-enter SURVIG with a larger @ADDPOINT value to continue input of new data.  
*** Error - Unacceptable value : variable unchanged. |  A value has been supplied by the user that does not fall within acceptable limits. these limits vary according to the default being changed. |   
*** This is not a standard plot file <<< |  A plot file which is superimposed must have all of the normal DATAMINE plot file fields. |   
*** Cannot find section definition fields in the plot file <<< |  A plot file which is superimposed must have all of the normal DATAMINE plot file fields, in addition to the implicit fields SAZI, SDIP, XCENTRE, YCENTRE and ZCENTRE. The default value(s) of these extra fields define the orientation and position of the plot being superimposed. |   
*** Cannot find a sectional window with the same orientation as the plot file <<< |  The implicit values of the fields SAZI, SDIP, XCENTRE, YCENTRE, ZCENTRE define the position and orientation of the plot file. |   
*** Error - Profile file not defined on input. |  Cannot use SV sub-command. |  Supply a profile file name when executing the SURVIG process, that will allow storage of section profiles to be used in volume calculations.  
*** Error - Section file not defined on input. |  Cannot use SV sub-command. |  Supply a section file name when executing the SURVIG process. The section definitions, used to generate the section profiles, are required in this command to close each profile to the upper limit of the section plane, for the computation of profile area.  
*** Error - No profiles stored in file FFFFFFFF |  |  Update profiles with sub-command UP before using SV sub-command. Section profiles for the current PERIOD must be produced by command UPDATE PROFILES [/PU] prior to using the COMPUTE VOLUMES [/PV] command.  
*** Error - reading profile file. |  The process has been unable to read section profiles from the input file. This may have been caused by internal corruption of the file or by its accidental removal since execution of the SURVIG process, on operating systems that support multiple users. |   
*** Error - Less than two sections within the limits supplied. Check the limits are correct and that sections are stored for the range in the input/output section file FFFFFFFF. |  The process must be able to find two or more section definitions and profiles in order to compute a volume. The range of sections supplied must be found in both the section definition and the profile file. |   
*** Error - reading section file. |  The process has been unable to read section definitions from the input file. This may have been caused by internal corruption of the file or by its accidental removal since execution of the SURVIG process, on operating systems that support multiple users. |   
*** Cannot change isometric view with the TP sub-command. Must use XY or SO. |  This warning message results from the use of the PLANE BY 2 POINTS [/D2] command when the current window is an isometric view. |   
*** Pointless to toggle window if only one window in current window set-up <<< |  This warning message results from the use of the TOGGLE WINDOW [/DT] command when there is only one active window. TOGGLE WINDOW [/DT] toggles between a multi-window and single window set-up. |   
*** Error - Cannot do this operation without a section file. *** Error - Cannot do this operation without a profile file. |  In order for section profiles to be produced for the current PERIOD, the user must supply a file of section definitions and a file of section profiles, on input. If these file names have been supplied, but do not exist, they will be created. The user will then have to create a series of section definitions with command DEFINE SECTIONS [/PD], prior to using this command. |   
*** Error - Out of point storage space, cannot complete new string. |  The @ADDPOINT parameter value has been exceeded. This error will not cause a failure in the process. |  Write all of the survey point and segment data to the output files with the WRITE SURVEY DATA [/FW] command and then re-enter SURVIG with a larger @ADDPOINT value to continue input of new data.  
*** Error - Window definition error or no windows defined. |  |   
  
Related topics and activities

  * [SURCAL Process](<surcal.md>)

  * [SURFIP Process](<surfip.md>)

  * [SURLOG Process](<surlog.md>)

  * SURVIG Process

  * [SURPOI Process](<surpoi.md>)

  * [SURTAC Process](<surtac.md>)

  * [SURTRI Process](<surtri.md>)

  * [SURVIN Process](<survin.md>)

  * [SURVOU Process](<survou.md>)