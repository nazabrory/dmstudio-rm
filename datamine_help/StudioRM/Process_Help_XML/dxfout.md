# DXFOUT Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DXFOUT** and click **Run**.
  * Enter "DXFOUT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DXFOUT>).

## Process Overview

Output a Datamine database plotfile to an external system file in Autocad DXF format.

To use the created DXF file under Autocad, invoke Autocad with the new drawing option, and use the DXFIN command to import the DXF file. Note that the DXF file created contains the Entities section only, and hence can only be overlaid onto another drawing (including an empty drawing).

As well as giving the same visual representation of the generated graphics on an Autocad display, this process also attempts to reconstruct base graphic primitives into intelligent Autocad entities. This allows for connected lines to be treated as single entities within Autocad. Textual characters are also combined into "strings" wherever possible such that text strings may be treated as single entities. Textual characters can only be combined into a single string entity if all text properties (colour, width, angle) are equivalent. Some processes currently use an inter-word gap of the height of the character, rather than the width. In such instances **DXFOUT** will not combine the text words. (If it did, your application's text representation would differ from what would be displayed on an Autocad screen).

The colour table is set as for your application.

The following Datamine special markers are supported as entities:

  * Code 91 = Circle

  * Code 92 = Cross "+"

  * Code 93 = Cross "x"

  * Code 94 = Triangle

  * Code 95 = Square

  * Code 96 = Diamond

  * Code 97 = Star "*"

Marker types 98 and 99 are currently undefined by your application and hence are ignored.

Shaded ornamentation codes are implemented using fill colors.

The broad line thickness is set to produce a line thickness of 0.7.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Database plotfile to be output to AUTOCAD DXF format. |  Input |  Yes |  Plot  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
LAYER |  Field containing layer identification. DXF entities will be allocated to layers numbered from 1 to n, depending on how many unique identifiers are present in IN. The default field name is LAYER |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
TOLERNCE |  Tolerance used in determining if lines can be reconstructed into polylines and individual characters into text strings (0.001). |  No |  0.001 |  Undefined |  Undefined  
REALWRLD |  If set to 1, back converts plotted millimeters to real world co-ordinates based on the scaling information provided in the XMIN, XMAX, YMIN, YMAX, XSCALE and YSCALE fields in the plot file (0). |  No |  0 |  0,1 |  0,1  
DM |  If set to 1, copies DATAMINE colour numbers to the DXF file without translation. Otherwise, colours are converted according to a table which is suitable for AUTOCAD. (0) |  No |  0 |  0,1 |  0,1  
MAXVERT |  Maximum allowable vertices in a single polygon in the DXF file. The default is 2000, but this may be too large for some CAD systems. |  No |  2000 |  Undefined |  Undefined  
LAYERNAM |  Set to 1 to put layer names into the output file without translation. The default is 0. |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !DXFOUT    &IN(PLOT)SYSFILE>PLOT.DXF  
  
---  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> NOT A VALID PLOT FILE <<< |  The specified input file is not a valid Datamine plotfile. Fatal; the process is exited. |