# FDOUT Process

To access this process:

  * **Data** ribbon **> > Transfer >> Whittle >> Output FOUR-D**.
  * Enter "FDOUT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FDOUT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FDOUT>).

## Process Overview

Output a Datamine model in a format suitable for input to Whittle FOUR-D.

The processes **FDOUT** and [FDIN](<fdin.md>) provide the interface between your application and the standalone Whittle FOUR-D program for pit optimization.

The process **FDOUT** takes a Datamine model and creates two ASCII output files, which can be read by FOUR-D. When FOUR-D is run an output results file is created which can be read by FDIN along with the associated parameter file. A Datamine model is created.

Your application creates external model and parameter files, and reads external result and parameter files. All optimization procedures are carried out within Whittle FOUR-D

The FOUR-D results file has a record per block with the following information:

  * Block coordinates \- IX, IY, IZ

  * Total tonnes of ROCK in the block

  * Mining cost adjustment factor

  * Processing cost adjustment factor

  * Parcel information

Zero or more parcels can be defined for each block on separate records. Up to 50 parcels are allowed.

Each parcel has the following information:

  * Rock type code (1-4 characters). This should not contain a period('.'), be 'ROCK' or start with 'GR_'. It is case sensitive and should be left justified

  * Tonnage of the parcel

  * Metal content of the parcel

Metal content is measured in metal units, not grade. A parcel is allowed to have a tonnage and zero metal content, to allow multiple 'waste' material types to be identified.

The block dimensions are defined by the Datamine model cell structure.

The rock type code must be supplied as an alphanumeric field. Only the first 4 characters are accepted.

The required field names are supplied interactively. An explicit field for tonnes of rock and metal content in the cell/sub-cell is required, together with optional explicit fields for mining cost adjustment, and processing cost adjustment. Where subcells are supplied, then block averages are calculated for the optional mining and processing cost adjustment factors. Two methods are available to specify the tonnage and metal content of the cell/sub-cell:

#### Method A:

Pairs of explicit fields are provided, where each pair gives the tonnage, and metal content for a particular rock type. Thus, if there are N rock types in the model, there must be 2N such fields.

If the total tonnes of rock is zero, these pairs of fields are ignored and no parcels are output for the cell/sub-cell. If tonnage is less than TOLTON or metal is less than TOLMET, no parcel is output for the pair. 

#### Method B:

Three explicit fields are provided. One field is alphanumeric (only the first four characters are used), and is used for the rock type identification. Two other numeric fields contain the tonnage and the metal content.

If total tonnes of rock is zero, the rock type code, tonnage and metal fields are ignored. If tonnage is less than TOLTON or metal is less than TOLMET, the rock type field is ignored and no parcel is output for the cell/sub-cell.

You can choose whether multiple sub-cells of the same rock type code within a cell are to be summed into one parcel or not. If sub-cells are being output as separate parcels, a limit can be set on the total number of parcels output for a block. If necessary, parcels are combined with the same rules as the FOUR-D FDRB reblocking program. If a subcell model is supplied it must be in sorted (IJK) order. 

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
TOLTON |  Minimum tonnage in parcel to be output (0.5) |  No |  0.5 |  Undefined |  Undefined  
FORMAT |  Output format for economic file (0). |  Option |  Description  
---|---  
0 |  Fixed format.  
1 |  Comma separated.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !FDOUT &IN(MODEL1),@TOLTON=0.1Enter FOUR-D parameter file   
  
---  
      
    
     name:  
      
    
    SYSFILE>    run1.mpa  
      
    
    Enter FOUR-D model file   
      
    
     name:  
      
    
    SYSFILE>    model1.eco  
      
    
    There are two methods of   
      
    
     specifying parcel fields:  
      
    
    Method   
      
    
         A:   A parcel type code and two numeric fields, for tonnes   
      
    
         and metal content, are specified for each possible parcel type.  Method   
      
    
         B:  Three fields are specified. One contains the parcel type.   
      
    
         The other two are numeric and contain the tonnes and metal content.   
      
    
            
      
    
    Product parcel specification   
      
    
     method A/B [B] >    B  
      
    
    Maximum number of parcels   
      
    
     [50] >     30  
      
    
    Default density [1.0] >   
      
    
        2.7  
      
    
    Merge identical product   
      
    
     parcel types Y/N [N] >    N  
      
    
        The   
      
    
     fields available for selection are:  
      
    
        ROCK-TON   
      
    
         TONNES     METAL     AU   
      
    
         AG  
      
    
    Field for ROCK tonnes >   
      
    
        ROCK-TON  
      
    
        The   
      
    
     fields available for selection are:  
      
    
        TONNES   
      
    
         METAL     AU     AG  
      
    
    Mining cost adjustment field   
      
    
     >  
      
    
        The   
      
    
     fields available for selection are:  
      
    
        TONNES   
      
    
         METAL     AU     AG  
      
    
    Processing cost adjustment   
      
    
     field >  
      
    
        The   
      
    
     fields available for selection are:  
      
    
        TONNES   
      
    
         METAL     AU     AG  
      
    
    Field for tonnes >    TONNES  
      
    
    Field for metal content   
      
    
     >    METAL  
      
    
        The   
      
    
     fields available for selection are:      
      
    
        PPT   
      
    
             R-NAME  
      
    
    Field for product parcel   
      
    
     type >    PPT  
      
    
        The   
      
    
     fields used are as follows:  
      
    
                                 ROCK   
      
    
     field = ROCK-TON  
      
    
        Type   
      
    
     = PPT         Tonnes = TONNES   
      
    
             Metal = METAL  
      
    
    Accept this data specification   
      
    
     Y/N [Y] >    Y  
      
    
    Reading the blocks and writing   
      
    
     the Four-D model file:  
      
    
        >>>   
      
    
         6000 RECORDS WRITTEN:     TIME   
      
    
     14:12:12 <<<  
      
    
                6250   
      
    
     records read  
      
    
                6250   
      
    
     blocks written  
      
    
                6250   
      
    
     product parcels written  
      
    
            The   
      
    
     maximum number of product parcels in a block was 1  
      
    
    --------------------------------------------------------------------------------