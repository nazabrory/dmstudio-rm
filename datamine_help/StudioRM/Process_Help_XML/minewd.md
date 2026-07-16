# MINEWD Process

To access this process:

  * Enter "MINEWD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MINEWD** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MINEWD>).

## Process Overview

Creates LG 'Additional Arcs' for mining width.

The input file is a block model file containing the ore blocks of the main reef. In addition, it should have an **OREVAL** field which contains a value which is to be compared with the **OREMIN** parameter. The **MINWID** parameter defines the required minimum mining width; the WIDDIR parameter defines the bearing in degrees, clockwise from the positive Y-axis (North) along which the minimum mining width extension is to be made. For example, if the main reef lies North-West to South-East and dips towards the North-East, this parameter would be set to 45 degrees. The **OREMIN** parameter defines the minimum value of the field **OREVAL** for a cell to be treated as ore. 

The input block model must be a regular model with no sub-cells.

This process generates a file of Lerchs-Grossmann structure arcs for input to LGST as 'Additional arcs' for the structure of a block model. These arcs have the effect of ensuring that a required minimum mining width is honoured at the bottom of the pit during the Lerchs-Grossmann optimization. This approach is only appropriate when the main reef meets all of these criteria:

  * Is thin compared with the minimum mining width.

  * Dips at angle which is steeper than the required mining slope.

  * Has a clearly defined strike d

By 'main reef' we mean a reef (ore body) which is mined at the full depth of the mine. 

Other reefs may be mined as 'bonuses', and will be considered in the Lerchs-Grossmann optimization. It is necessary to decide on which side of the main reef the extra waste is to be removed to provide the necessary mining width. 

Given this decision, **MINEWD** will set up structure arcs which cause strings of blocks of the length required to reach the minimum mining width to be treated by the optimization module as though they were one block. That is, either all blocks in a string are mined or none of them are mined. This ensures that the bottom of the pit is at least the minimum mining width across. 

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file containing the ore blocks of the main reef. This must be a regular model with no sub-cells. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output additional arcs file for input to LGST.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
OREVAL |  A field in the model file which contains a value which is to be compared with **OREMIN**. |  Undefined |  No |  Undefined |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MINWID |  Minimum mining width. |  Yes |  Undefined |  Undefined |  Undefined  
WIDDIR |  Bearing in degrees clockwise from the postive Y-direction (North) along which the minimum mining width extension is to be made. e.g. If the main reef lies North-West to South-East and dips down towards the North-East, this might be 45 degrees. |  Yes |  North |  Undefined |  Undefined  
OREMIN |  Minimum value of field **OREVAL** for a cell to be treated as ore. |  No |  Undefined |  Undefined |  Undefined