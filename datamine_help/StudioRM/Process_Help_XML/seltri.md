# SELTRI Process

To access this process:

  * Enter "SELTRI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SELTRI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SELTRI>).

## Process Overview

Copies records of a file which have X, Y and Z co-ordinates lying above/ below a wireframe surface or inside/outside a wireframe volume.

Note: Surfaces and wireframes should not both be present in the triangles file unless individual models are specified for selection by setting a **ZONE** parameter. In-place operations are not permitted.

### @SELECT Options

  * **@SELECT = 1 OR 2**

There may be points that are neither above or below if they are outside the range of triangles.  

  * **@SELECT = 3**

A point may lie inside more than one wireframe model. If this is the case it will appear more than once in the output file.  

  * **@SELECT = 4**

An outside point is outside all wireframe models. Attribute fields will not be copied in this case.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input point file for selection. Must have explicit numeric fields X , Y and Z. Processing is quicker if this file is sorted on X. |  Input |  Yes |  Undefined  
WIRETR |  Input wireframe triangle file |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file of selected records. File may contain additional fields, including the **ZONE** field.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field in **IN** file defining the X co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Y |  Field in **IN** file defining the Y co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Z |  Field in **IN** file defining the Z co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
ZONE |  Field in **WIRETR** file used to identify individual surfaces and solid models. If there is more than one surface or solid model and **ZONE** is not specified, a point may be selected more than once, one for each model. If this field is specified and **ZONE** is not, the **ZONE** field is copied to the output file. |  WIRETR |  No |  Any |  Undefined  
ATTRIB1 |  Field from the **WIRETR** file to be placed into the output file for all records which are selected. Up to 4 words may be entered, which may be 4 numeric fields or a mixture of alphanumeric and numeric fields totalling 4 words. |  WIRETR |  No |  Any |  Undefined  
ATTRIB2 |  Second field from the **WIRETR** file to be placed into the output file for all records selected. |  WIRETR |  No |  Any |  Undefined  
ATTRIB3 |  Third field from the **WIRETR** file to be placed into the output file for all records selected. |  WIRETR |  No |  Any |  Undefined  
ATTRIB4 |  Fourth field from the WIRETR file to be placed into the output file for all records selected. |  WIRETR |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ZONE |  Used to select one of a number of surface or wireframe models. This parameter must be specified if **WIRETR** contains a mix of surface and solid models. The SELECT parameter will determine whether a model is treated as a surface or wireframe. |  No |  Undefined |  Undefined |  Undefined  
SELECT |  |  Option |  Description  
---|---  
1 |  select points above a surface  
2 |  select points below a surface  
3 |  select points inside a solid  
4 |  select points outside a solid.  
Yes |  3 |  1,4 |  1,2,3,4  
TOLERANC |  Tolerance for selection criteria. A positive tolerance will enhance point selection (0.001). |  No |  0.001 |  Undefined |  Undefined  
  
## Example
    
    
    !SELTRI    &IN(POINTS),&OUT(POUT),&WIREPT(PT),&WIRETR(TR),          
  
---  
      
    
    *X(XP),*Y(YP),*Z(ZP),@SELECT=3  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> TRIANGLE POINT FIELDS MISSING <<< |  The &**WIREPT** file is missing the required fields. Check that the &**WIREPT** file contains the standard wireframe points filed fields.  
>>> TRIANGLE FIELDS MISSING <<< |  The &**WIRETR** file is missing the required fields. Check that the &**WIRETR** file contains the standard wireframe triangles file fields.  
>>> POINT SELECT FIELDS MISSING <<< |  The selected X, Y and Z coordinate fields are not present in the &IN file. Check that the defined *X, *Y, *Z coordinate fields exist in the &IN file.  
>>> INVALID PARAMETERS - PROCESS ABORT <<< |  Value for @**SELECT** is <1 or >4. Select an @**SELECT** value which of 1, 2, 3 or 4.  
>>> TRIANGLES HAVE INVALID POINT IDENTIFIERS <<< |  The points and triangles files are not consistent. Check that the defined wireframe triangle and wireframe points files are consistent. This can be done by loading them into the 3D window i.e. drag-and-drop the wireframe triangle file into the 3D window. If they load without error, then they are valid wireframe triangles and points files pair.   
>>> MISSING TRIANGLE POINTS <<< |  The points and triangles files are not consistent.  
  
Related topics and activities

  * [SELWF Process](<selwf.md>)