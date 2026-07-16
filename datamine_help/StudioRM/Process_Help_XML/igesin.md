# IGESIN Process  
  
To access this process:

  * **Data** ribbon **> > Transfer >> IGES/DXF**.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **IGESIN** and click **Run**.

  * Enter "IGESIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#IGESIN>).

## Process Overview

Used to convert CAD drawings which have been previously converted to the IGES format, to Datamine plotfiles. This process can only be used with CAD packages which support the IGES format.

When using this process, it must be remembered that it is often impossible to convey an exact duplicate picture when converting between a CAD package and your application. Certain information may be lost or have to be approximated. For example, hatching, arcs and curves will be ignored in the transfer. Any negative scaling or mirroring used in the CAD drawing will also be ignored.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Overwritten |  Yes |  Plot Prototype |  File containing plot prototype.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Plot |  Plotfile to be created (may be same as IN; if it is, the original data in the file is overwritten).  
  
## Example
    
    
    !IGESIN    &IN(PLOTPROT),&OUT(PLOTFILE)SYSFILE>plotfile.igs  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.  
  
Related topics and activities

  * [IGESOUT Process](<igesout.md>)