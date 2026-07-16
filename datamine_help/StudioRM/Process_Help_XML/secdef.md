# SECDEF Process  
  
To access this process:

  * Enter "SECDEF" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SECDEF** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SECDEF>).

## Process Overview

Create a section definition file to support the creation and clipping of data in a 3D window. A Section Definition is a numerical representation of a 3D plane. 

See [3D Sections](<../VR_Help/Sections.md>).

The output section definition file contains the following fields, and is recognized in all Studio products as the section definition file type:

SVALUE  |  Section number  
---|---  
XCENTRE  |  X coordinate of the center of the section.  
YCENTRE  |  Y coordinate of the center of the section.  
ZCENTRE  |  Z coordinate of the center of the section.  
SDIP  |  Dip of the section.  
SAZI  |  Azimuth of the section (the dip direction of the section plane).  
STHICK |  The width of the section corridor. This is split equally both in front of and behind the section. Essentially, this is the width of a cross section of data displayed when clipping is set to both front and back.  
DPLUS  |  Extent of the section in the positive (azimuth) direction.  
DMINUS  |  Extent of the section in the negative (opposite to azimuth) direction.  
HSIZE |  Horizontal dimension of the section plane.  
VSIZE |  Vertical dimension of the section plane.  
  
**SECDEF** outputs a 3D section defined using subsequent command line prompts. 

For example, When this process is run, the following messages and prompts are displayed in the **Command** control bar; responses are typed into the **Run Command** field:
    
    
    NUMBER OF SECTIONS (0 TO END >  1
    
    
     >>> NUMBER OF SECTIONS =     1
    
    
     >>> SELECT ONE OF THE FOLLOWING --
    
    
     >>>          1    VERTICAL OR INCLINED SECTION
    
    
     >>>                   DEFINED ABOUT CENTRE POINT
    
    
     >>>          2    VERTICAL SECTION DEFINED BY
    
    
     >>>                   END POINTS
    
    
     >>>          3    PLAN VIEW DEFINED BY CORNER
    
    
     >>>                   POINTS
    
    
    > 1
    
    
    SVALUE > 1
    
    
    XC     > 5000
    
    
    YC     > 6000
    
    
    ZC     > 0
    
    
    DIP    > 90
    
    
    AZI    > 180
    
    
    DMAX   > 50
    
    
    DPLUS  > 25
    
    
    DMINUS > 25
    
    
    HSIZE  > 500
    
    
    VSIZE  > 100
    
    
     >>> SECTION PLANE PARAMETERS ---
    
    
     >>> FIRST SECTION (OF     1)
    
    
     >>> SVALUE >          1.00
    
    
     >>> XC     >       5000.00
    
    
     >>> YC     >       6000.00
    
    
     >>> ZC     >          0.00
    
    
     >>> DIP    >         90.00
    
    
     >>> AZI    >        180.00
    
    
     >>> DMAX   >         50.00
    
    
     >>> DPLUS  >         25.00
    
    
     >>> DMINUS >         25.00
    
    
     >>> HSIZE  >        500.00
    
    
     >>> VSIZE  >        100.00
    
    
    ARE THEY CORRECT (Y/N) > Y
    
    
    NUMBER OF SECTIONS (0 TO END > 0
    
    
     >>>       1 Records in File ... secdef1.dm <<<
    
    
    >>> SECDEF   Complete <<<

If sections already exist in **OUT** , the file is appended. This way, you can easily create a file of multiple definitions.

Note: You can only have one section definition file loaded in the 3D window at any one time, but each file can contain any number of section definitions. Attempts to load another file will result in the current one being closed.

Data is saved to a Section Definition file. This file can contain multiple section views, and previously saved views are accessed using the 3D view ribbon, if your product supports one. You can also step back and forward through loaded section definitions using the following commands:

  * [move-previous-section ("mps")](<../command_help/move-previous-section.md>)

  * [move-next-section ("mns")](<../command_help/move-next-section.md>)

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file of section definitions, containing the fields **SVALUE, XCENTRE, YCENTRE, ZCENTRE, SDIP, SAZI, VAZI, VDIP, HSIZE, VSIZE, DPLUS, DMINUS, SCALE, TEXT, COUNT**  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> NOT A NUMBER <<< x  ^  >>> ERR 57 <<< ( 2) IN STRDCD  ** INVALID SECTION NUMBER |  The section number that has been entered is alphanumeric. Enter a numeric value.  
  
Related topics and activities

  * [3D Sections](<../VR_Help/Sections.md>)

  * [3D Sections Menu](<../VR_Help/workspace_sections.md>)

  * [3D Section Widgets](<../COMMON/Section_Widgets.md>)

  * [move-previous-section ("mps")](<../command_help/move-previous-section.md>)

  * [move-next-section ("mns")](<../command_help/move-next-section.md>)