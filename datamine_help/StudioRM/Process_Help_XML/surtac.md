# SURTAC Process

To access this process:

  * Enter "SURTAC" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SURTAC** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SURTAC>).

## Command Overview

SURTAC is a survey measurement reduction process.

This command computes the three-dimensional coordinates of points located by angle and distance measurements from a coordinated survey station. This constitutes the second stage in survey data processing. The user will have created a file containing the survey measurements, prior to running this process, by one of the following processes:

  * [AED](<aed.md>)

Editor for file creation and modification.

The AED process may be used to input survey observations from the keyboard, from data written in a field note book.

  * [SURLOG](<surlog.md>)

Input of survey data from a character system file.

The SURLOG process is used to input a file of measurements that has been transferred from a digital data recorder.

The user can assign display elements of symbol, color and line style for point and strings of points, according to the descriptive code recorded in the survey.

The output files of coordinated points and string segments will then be used as input to the interactive survey editor, in order to visualize and edit the survey in three-dimensions and update the survey database.

  * [SURVIG](<survig.md>)

Interactive graphic survey data editor.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
CONTROL |  Input control survey station file. This must contain the numeric fields X, Y and Z. A field identifying the station name is required and may be of type numeric or alpha-numeric. The default station naming field is STATION of type numeric. |  Input |  Yes |  Undefined  
IN |  |  Input |  Yes |  Undefined  
ATTRIBUT |  Input attribute file. This must contain PTYPE, PTEXT, PSYMBOL, PSYMSZE, PCODE and P. May also contain an alpha-numeric string type field. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
POINTOU |  Output |  Yes |  Undefined |  Output point file. This will contain fields PID, X, Y, Z, PSYMBOL, PSYMSZE, P and PERIOD (numeric, explicit).  
SEGOU |  Output |  Yes |  Undefined |  Output string segment file. This will contain fields PID1, PID2, PVALUE, PTYPE, PTEXT, PCODE, P and PERIOD.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
STYPE |  Optional key field in ATTRIBUT and IN file for assignment of point and string attributes. If this field is not supplied by the user, PTYPE will be used by default and must exist in the input file. |  IN, ATTRIBUT |  No |  Any |  Undefined  
SVALUE |  Optional key field in IN file for assignment of numeric string identifiers to the output string file. If this field is not supplied, field PVALUE will be used and must exist in the input file. |  IN |  No |  Numeric |  Undefined  
STATION |  Optional alphanumeric survey station identifier in the input CONTROL survey station file. If this field is not supplied the default numeric field STATION will be used. |  CONTROL |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
OBTYPE |  Input tacheometry observation type. This will be one of: 1 = Horizontal, vertical angles and slope distance measurements.  2 = Horizontal angle and distance and vertical difference.  3 = Horizontal, vertical angles and staff/stadia intercepts.  4 = Reduced X,Y,Z coordinates. The default observation type will be (1). |  Yes |  1 |  1,4 |  1,2,3,4  
ANGLE |  Angle units used. This will be one of: 1 = Degrees, minutes and seconds; 0-360 2 = Gradians; 0-400 The default angle unit will be Degrees, minutes and seconds (1). |  No |  1 |  1,2 |  1,2  
VOFFSET |  Measurement method for UP/DOWN offsets. This will be one of:-  1 = UP/DOWN offsets measured vertically above/below distance measurement.  2 = UP/DOWN offsets measured perpendicular to the distance measurement.  The default method will be vertical offset measurements (1). |  No |  1 |  1,2 |  1,2  
PERIOD |  Numeric integer period number to be stored with output point and string segment data. |  No |  Undefined |  Undefined |  Undefined  
PIDSTART |  Optional start point number for output to point file, field PID, if a numeric TARGET field does not exist in the input file. The default start number is 1.(1) |  No |  1 |  Undefined |  Undefined  
PIDINCR |  Optional point number increment, if no TARGET field exists in the input file. The default increment is 1.(1) |  No |  1 |  Undefined |  Undefined  
PVSTART |  Optional start string number for output to string file, field PVALUE, if no PVALUE field exists in the input file. The default start number is 1.(1) |  No |  1 |  Undefined |  Undefined  
PVINCR |  Optional string number increment, if no PVALUE field exists in the input file. The default increment is 1.(1) |  No |  1 |  Undefined |  Undefined  
PLANE |  Optional reference plane elevation to which horizontal distances will be reduced prior to computation of grid distance and point coordinates. The default is absent data [-], no futher reductions are made to the horizontal distance.(-) |  No |  - |  Undefined |  Undefined  
FACTOR |  Optional scale factor to be applied to the plane distance, to compute the grid distance, prior to computation of point coordinates. The default value is 1.(1) |  No |  1 |  Undefined |  Undefined  
ROCHECK |  Optional flag = 1 to compare computed base line distance components with check measurements made. The default is 0, not to compare check base measurements, if present .(0) |  No |  0 |  0,1 |  0,1  
UPDATE |  Optional flag = 1 to append computed points to the CONTROL file, if they are subsequently occupied by the survey instrument for continuation of the detail survey during execution of the process. The default is 0, not to append any computed points to the input CONTROL file. (0) |  No |  0 |  0,1 |  0,1  
  
Related topics and activities

  * [SURCAL Process](<surcal.md>)

  * [SURFIP Process](<surfip.md>)

  * [SURLOG Process](<surlog.md>)

  * SURTAC Process

  * [SURPOI Process](<surpoi.md>)

  * [SURTRI Process](<surtri.md>)

  * [SURVIG Process](<survig.md>)

  * [SURVIN Process](<survin.md>)

  * [SURVOU Process](<survou.md>)