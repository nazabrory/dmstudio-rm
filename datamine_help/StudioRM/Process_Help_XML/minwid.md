# MINWID Process  
  
To access this process:

  * Enter "MINWID" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MINWID** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MINWID>).

## Process Overview

Composite drillhole data into ore and waste intervals that satisfy the specified mining width criteria.

**Note** : To composite drillhole data by optimizing the composite interval using ore and waste criteria, see [COMPSE Process](<compse.md>).

The input file must be in standard sample format (as output by process **[HOLES3D](<holes3d.md>)**). The input file must be in the order of **BHID** and **FROM** , that is, sorted in drillhole order in increasing downhole distance.

This is the order output from the **HOLES3D** process. The output file is in standard drillhole format supplemented with the **VALUE** and **DENSITY** fields. The initial classification of ore and waste is based on whether a specified numeric field in the input file is above or below a specified cutoff.

The contiguous intervals of like samples make up either 'narrow' or 'wide' ore, or 'narrow' or 'wide' waste. If the ore interval is greater than the minimum ore width, then the ore is 'wide'. If the waste is greater than the minimum waste width, then the waste is 'wide'. 'Narrow' ore and waste intervals must be recombined to satisfy the mining width criteria. If 'narrow' ore cannot be recombined with other ore intervals, the option to dilute with adjacent waste is allowed. To allow minimum dilution of 'narrow' ore intervals from adjacent waste a dilution splitting interval can be specified.

Although the ore body orientation is not explicit in the drill hole data, dilution can be added to hanging and/or foot wall contacts. A constant relationship between ore body and hole orientation is assumed, with the dilution width specified as a positive distance up and down the drill hole from an ore interval. An interval file is output to provide a convenient summary of ore intervals, dilution components,and additional material above cutoff that fails to meet the specified criteria. In additional to BHID, FROM and TO fields other category fields output to flag the interval status:

  * **CATA** flags intervals that together satisfying all mining width criteria

  * **CATB** flags intervals that fail the mining width criteria when wall dilution is added

  * **CATC** flags above cutoff material that fails the minimum ore width criteria

  * **CATD** flags the below cutoff material in mining intervals (1 - from DILP. 2 - from DILN, 3 -other internal waste)

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample file, in BHID and FROM order. |  Input |  Yes |  Drillhole  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Drillhole |  Output file of composites in standard  
INTERVAL |  Output |  Yes |  Undefined |  Output file of composite interval and dilution types.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Value which is to control compositing. This may be a grade or a calculated equivalent value from grades of different metals. |  IN |  Yes |  Numeric |  Undefined  
DENSITY |  Density field. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CUTOFF |  Minimum value of **VALUE** which is worth mining (0). |  Yes |  0 |  Undefined | Undefined  
MINORE |  Minimum mining width for ore. |  Yes |  Undefined |  Undefined | Undefined  
MINWASTE |  Minimum width for internal waste (0). |  Yes |  0 |  Undefined | Undefined  
DILUTE |  Allow dilution of composites to create minimum ore width if non-zero (1). |  Yes |  1 |  0,1 | 0,1  
NARWAST1 |  Test for carrying narrow waste to be applied to either [1] or both [2] adjacent wide ores (1). |  Yes |  1 |  1,2 | 1,2  
NARWAST2 |  Allow narrow waste to be expanded into adjacent wide ore to meet the minimum waste width if non-zero (0). |  Yes |  0 |  0,1 | 0,1  
DILP |  Dilution interval added to the ore composite in the down hole direction (0). |  Yes |  0 |  0,+ | Undefined  
DILN |  Dilution interval added to the ore composite in the up hole direction (0). |  Yes |  0 |  0,+ | Undefined  
DILINT |  Dilution splitting interval to be used when diluting narrow ore with adjacent waste (0). |  Yes |  0 |  0,+ | Undefined  
  
Related topics and activities

  * [HOLES3D Process](<holes3d.md>)

  * [COMPSE Process](<compse.md>)

  * [COMPDH Process](<compdh.md>)

  * [COMPBE Process](<compbe.md>)

  * [COMPBR Process](<compbr.md>)