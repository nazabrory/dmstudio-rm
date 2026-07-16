# FDIN Process

To access this process:

  * **Data** ribbon **> > Transfer >> Whittle >> Input FOUR-D**.
  * Enter "FDIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FDIN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FDIN>).

## Process Overview

Create a Datamine model from a Whittle FOUR-D results file.

The processes [FDOUT](<fdout.md>) and FDIN provide the interface between your application and the standalone Whittle FOUR-D program for pit optimization.

The process [FDOUT](<fdout.md>) takes a Datamine model and creates two ASCII output files, which can be read by FOUR-D. When FOUR-D is run an output results file is created which can be read by FDIN along with the associated parameter file. A Datamine model is created. 

Your application creates external model and parameter files, and reads external result and parameter files. All optimization procedures are carried out within Whittle FOUR-D

The FOUR-D results file has a record per block with the following information:

  * Block coordinates - IX, IY, IZ

  * Total tonnes of ROCK in the block

  * Mining cost adjustment factor

  * Processing cost adjustment factor

  * Parcel information

  * Pit number.

The block model origin and cell structure is defined by the FOUR-D parameter file. The only additional field created in the output model is PIT for the Pit Number.

The process will read fixed format or comma separated results file formats.

The output model file is not written in IJK order, and must subsequently be sorted.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output model file.  
  
## Example
    
    
    !FD IN    &OUT(lg4model)  
  
---  
      
    
    Enter FOUR-D parameter file name:  
      
    
    >SYSFILE>    run1.prm  
      
    
    Enter FOUR-D results file name:  
      
    
    >SYSFILE >    model2.res  
      
    
    >>> 6000 RECORDS PROCESSED : TIME 14:12:12   
      
    
     <<<  
      
    
    6250 blocks read and then written to model file.  
      
    
    >>> 6250 RECORDS IN FILE LG4MODEL <<<  
  
Related topics and activities

  * [FDOUT Process](<fdout.md>)

  * [FXIN Process](<fxin.md>)

  * [FXOUT Process](<fxout.md>)