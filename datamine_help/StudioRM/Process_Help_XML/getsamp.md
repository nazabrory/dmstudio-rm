# GETSAMP Process

To access this process:

  * Enter "GETSAMP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **GETSAMP** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_G.md#GETSAMP>).

## Process Overview

**GETSAMP** produces a sample file from a desurveyed drillhole file. In one way, it's almost the opposite of **[desurveying](<../COMMON/Drillhole%20Representation%20in%20Studio.md>)** component drillhole files into a **[static drillhole file](<../COMMON/Drillhole%20Representation%20in%20Studio.md>)**.

The output file will contain the BHID, FROM, TO from the input hole(s) with the longest possible intervals for each selected field.

A sample file may be used to save lithology or ore zone interpretations (for example, created with changes to the drillhole file imparted by **[group-lithology](<../command_help/group-lithology.md>)** , [assign-lithology](<../command_help/assign-lithology.md>) or [**edit-dh-attributes**](<../command_help/edit-dh-attributes.md>)).

It may also be used to save interpretations made to drillholes during **implicit modelling** in Studio's resource modelling products. During these activities, specific columns are added to drillholes to indicate enabling and reversing of columns (e.g. _FLAG_VS_ROCK or _FLAG_CS ).

The resulting downhole sample file can then be merged with existing drillhole sample tables during desurveying.

**Note** : data generated with absent values for all of the fields (F1, F2 etc) is automatically removed from the output of GETSAMP.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Desurveyed sample data file. This will include fields BHID, FROM, TO, X, Y, Z, A0, B0, and all other fields which were included in the sample file(s). Expects fields BHID, XCOLLAR, YCOLLAR and ZCOLLAR; optional fields BRG, DIP. | IN | Yes | Static Drillhole File  
  
## Output Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SAMPLE |  Generated sample data file. This file is compulsory and will include fields BHID, FROM, and TO. It will also include at least one sample attribute field, such as grade or lithology. | OUT | Yes | Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  First sample attribute field for saving to sample output. | IN | Yes | Any | Undefined  
F2-F30 |  Sample attribute fields for saving to sample output. | IN | No | Any | Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CSVOUT |  Set to 1 to create a CSV output file of the plot data file specified in GETSAMP. | No | 0 | 0-1 | 0,1  
  
## Example
    
    
    !GETSAMP &IN(HOLES1),&OUT(SAMP1),*KEY1(LITH)  
  
---  
  
Related topics and activities

  * [group-lithology](<../command_help/group-lithology.md>)
  * [assign-lithology](<../command_help/assign-lithology.md>)
  * [edit-dh-attributes](<../command_help/edit-dh-attributes.md>)
  * [Drillhole Representation](<../COMMON/Drillhole%20Representation%20in%20Studio.md>)