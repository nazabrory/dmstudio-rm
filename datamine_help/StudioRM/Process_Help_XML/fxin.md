# FXIN Process  
  
To access this process:

  * **Data** ribbon **> > Transfer >> Whittle >> Input FOUR-X**.
  * Enter "FXIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FXIN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FXIN>).

## Introduction

The process creates a Datamine block model from a Whittle FOUR-X output file.

The records in the output block model file are written in the order read from the input data file. If this block model is to be further used for viewing or design purposes, it first needs to be sorted on IJK using the process **[MGSORT](<mgsort.md>)**.

The **FOUR-X Results** file has a record per block with the following information:

  * Block coordinates - IX, IY, IZ
  * Total tonnes of ROCK in the block
  * Mining cost adjustment factor
  * Processing cost adjustment factor
  * Number of parcel lines to follow. Pit number (Columns 50-59)

The **Pit List** file is like the Results file without the detail of the block contents, recording only: 

  * Block coordinates - IX, IY, IZ
  * Number of the smallest pit that the block is part of, orzero for an air block (Columns 13-15)

The **Mining Sequence** file is identical in format to the Results file except that a period and fraction is added to each block header, and a processing method is added to each parcel: 

  * Period in which the following fraction of this block was mined (Columns 50-52)
  * Fraction of the block mined in the period (Columns53-59)

The processing method code for the method used to process the parcel is available in Columns 39-42 of each parcel line, but cannot be loaded into the model file as the subcell positional datails not available. The DATAMINE model cell structure is defined by the FOUR-X parameter file. The additional fields created in the output model are as follows: 

  * PIT for the Results file
  * PIT for the Pit List file
  * PERIOD and FRACTION for the Mining Sequence file.

The process inputs either a fixed format or comma separated format text file (the user is prompted for the path and filename once OK is clicked). The parameter **FILETYPE** indicates the type of FOUR-X data file as follows:

1 = Results file,

2 = Pit List file,

3 = Mining Sequence file

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output model file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
FILETYPE |  Type of input data file. 1 = Results file 2 = Pit List file 3 = Mining Sequence file |  No |  1 |  1,3 |  1,2,3  
  
Related topics and activities

  * [FDOUT Process](<fdout.md>)

  * FXIN Process

  * [FXOUT Process](<fxout.md>)