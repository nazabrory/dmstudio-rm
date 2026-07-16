# IGESOUT Process

To access this process:

  * **Data** ribbon **> > Transfer >> IGES/DXF >> Output in IGES**.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **IGESOUT** and click **Run**.

  * Enter "IGESOUT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#IGESOUT>).

## Process Overview

Outputs a plotfile to an IGES format file. This IGES file can then be read into any CAD package which supports the IGES format.

**Note** : All units in the output IGES file are in millimeters. Once in the CAD package, the drawing can be scaled accordingly.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Database plotfile to be output to AUTOCAD IGES format. |  Input |  Yes |  Plot  
  
## Example
    
    
    !IGESOUT &IN(PLOTFILE)SYSFILE>plotfile.igs  
  
---  
  
## Error and Warning Messages

Message | Description  
---|---  
>>> NOT A VALID PLOTFILE <<< |  The input file was not a valid plotfile. Fatal; the process is exited.  
  
Related topics and activities

  * [IGESIN Process](<igesin.md>)