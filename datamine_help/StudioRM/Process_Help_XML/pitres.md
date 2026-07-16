# PITRES Process

To access this process:

  * Enter "PITRES" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PITRES** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PITRES>).

## Process Overview

Enhanced reserve tabulation of a RESULTS file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
RESULTS |  Input results file. In standard format as per [TABRES](<tabres.md>). |  Input |  Yes |  Undefined  
MODEL |  Optional input model file to obtain spatial location parameters (such as RL) |  Input |  No |  Block Model  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
AUX |  Auxiliary classification field. An additional "rocktype" field. Create separately - often retrieval criteria are used. |  RESULTS |  No |  Any |  Undefined  
AAUX |  Auxiliary area classification field. Creates separate table for each field value, integers only. Mutually exclusive with **BAUX** |  RESULTS |  No |  Numeric |  Undefined  
BAUX |  Auxiliary bench classification field. Creates separate table for each Plane, using values of this field in each one, integers only. Mutually exclusive with **AAUX** |  RESULTS |  No |  Numeric |  Undefined  
GRADE |  Default grade field |  RESULTS |  No |  Numeric |  Undefined  
ROW |  Field to use in place of 'Number' in tables, ie replace RL, East, or North by something else. |  RESULTS |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
POSITION |  Location in cell of reference position. (0) 0 = base of cell 0.5 = centre of cell 1 = top of cell |  No |  0 |  0,1 |  0,0.5,1  
TSQUASH |  An amount subtracted from tonnes field width [10], +ve or -ve. Default is 0 |  No |  0 |  Undefined |  Undefined  
GSQUASH |  An amount subtracted from grade field width [7], +ve or -ve. Default is 0 |  No |  0 |  Undefined |  Undefined  
SQUASH |  An amount subtracted from metal field widths [9 |  No |  Undefined |  Undefined |  Undefined  
GUNIT |  Default grade units, in quotes. One of 'g/t', 'ppm', 'oz/t', '%', or 'dwt' |  No |  Undefined |  Undefined |  Undefined  
MUNIT |  Default metal units, in quotes. One of 'oz', 'kg', or 'tonn' |  No |  Undefined |  Undefined |  Undefined  
ELEMNT |  Default grade element/compound symbol, in quotes. Maximum of 4 characters |  No |  Undefined |  Undefined |  Undefined  
TROUND |  Rounding control for tonnes field. 1 = round to 10's 2 = 100's 3 = 1000's 4 = use units of 1000. Default 0 [none] |  No |  0 |  0,4 |  0,2,3,4  
GDEC |  Decimal places for grade field. 0 = 0 decimal place, 1 = 1 decimal place Default 2 decimal places |  No |  2 |  0,4 |  Undefined  
MROUND |  Rounding control for metal field. 1 = use 0 decimal places for kg units [def 1] 2 = round to 10's, 3 = 100's 4 = 1000's, Default 0 [none] |  No |  0 |  0,4 |  0,1,2,3,4  
SDEC |  Decimal places for strip ratio field. 0 = 0 decimal place Default 1 decimal place |  No |  0 |  Undefined |  Undefined  
LINES |  Number of lines per page, not including headers. (50) |  No |  50 |  Undefined |  Undefined  
WIDTH |  Page width in mm, max of 240. |  No |  Undefined |  Undefined |  Undefined  
NUMTAB |  Optional table number, 1-99, for display. |  No |  Undefined |  1,99 |  Undefined  
VOLUME |  1 = report in volumes rather than tonnes. (0) |  No |  0 |  0,1 |  0,1  
TONNESA |  1 = report individual tonnage components for each grade (ie TonnesA, TonnesB, etc rather than just overall tonnes of a cell, ie Tonnes. (0) |  No |  0 |  0,1 |  0,1  
  
Related topics and activities

  * [TABRES Process](<tabres.md>)