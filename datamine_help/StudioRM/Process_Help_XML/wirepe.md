# WIREPE Process

To access this process:

  * **Wireframe** ribbon **> > Process >> Section Strings from Wireframe**.
  * Enter "WIREPE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **WIREPE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WIREPE>).

## Process Overview

"Section" a wireframe to produce a set of perimeters (closed strings) at various section positions.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
SECTION |  Optional section definition file. Required fields: SVALUE - used to select specific section. XCENTRE,YCENTRE - coords of centre of section. SDIP - dip of section (degrees). SAZI - azimuth of dip direction (degrees). STHICK - influence of section (not used). |  Input |  No |  Section  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  Output perimeter file. File contains XP, YP, ZP, PVALUE, PTN and fields copied from the triangle file as specified by optional field specifications ATTRIB1, ATTRIB2, ATTRIB3 and ATTRIB4.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ATTRIB1 |  Field #1 to be copied from triangle to perimeter file. |  WIRETR |  No |  |  Undefined  
ATTRIB2 |  Field #2 to be copied from triangle to perimeter file. |  WIRETR |  No |  |  Undefined  
ATTRIB3 |  Field #3 to be copied from triangle to perimeter file. |  WIRETR |  No |  |  Undefined  
ATTRIB4 |  Field #4 to be copied from triangle to perimeter file. Section increments may be defined by : |  WIRETR |  No |  |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
XINCR |  Increment along the X axis. Parameter is used, in conjunction with YINCR and ZINCR to calculate an offset from the specified section to create a family of sections. |  No |  Undefined |  Undefined |  Undefined  
YINCR |  Increment along the Y axis. See XINCR. |  No |  Undefined |  Undefined |  Undefined  
ZINCR |  Increment along the Z axis. See XINCR. |  No |  Undefined |  Undefined |  Undefined  
PINCR |  An alternate form of specifiying an offset from the specified section to form a family of parallel sections. |  No |  Undefined |  Undefined |  Undefined  
AZINCR |  Increment azimuth from 0 to 180 about the centre point of the section, including the section defined by AZI. |  No |  Undefined |  0,180 |  Undefined  
DIPINCR |  Increment dip from - 90 to + 90 about the centre point of the section, including the section defined by DIP. |  No |  Undefined |  -90, 90 |  Undefined