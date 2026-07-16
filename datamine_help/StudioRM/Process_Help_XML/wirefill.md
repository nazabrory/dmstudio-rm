# WIREFILL Process

To access this process:

  * **Model** ribbon **> > Create >> Fill Wireframes >> From Wireframe**.

  * Enter "WIREFILL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **WIREFILL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WIREFILL>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**Note** : This process supports **[retrieval criteria](<../COMMON/Retrieval_Criteria_Overview.md>)**.

This process generates a block model from a wireframe model.

The optional input block model prototype file (**PROTO**) may be either an existing block model or a block model prototype file and can be regular or rotated. 

The process only uses the model extent and cell size fields as specified in the data definition - any actual cells/subcells and their associated data columns are ignored. If a prototype model is not specified, then the model dimensions are calculated automatically from the parameter described below and the extent of the wireframe points data. The input wireframe file (**WIRETR** , **WIREPT**) may consist of one or more solid wireframes, or one or more single surface DTMs. It may not contain both solid wireframes and DTMs. An optional attribute field can be defined (**ZONE**) and added to the output model file (**MODEL**). If this field exists in the wireframe triangle file then the wireframe attribute values are passed from the wireframes to the block model cells.

The **CELLXMIN** , **CELLYMIN** and **CELLZMIN** parameters define the minimum cell size in the X, Y and Z directions. If set to zero then seam filling is used, that is, cells are split once at the wireframe boundary. Only one of the values **CELLXMIN** , **CELLYMIN** , and **CELLZMIN** may be zero.

The following parameters are optional:

  * A zone code parameter (**ZCODE**) can be defined for insertion in the output block model ZONE field. This parameter is ignored if the field ZONE exists in the wireframe triangle file.

  * The **CELLXMAX** , **CELLYMAX** and **CELLZMAX** parameters define the maximum (ie parent) cell size in the X, Y and Z directions. These are ignored if a prototype block model (**PROTO**) is defined.

### Cell Creation Methods

The **WIRETYPE** parameter is used to define the type of wireframe model to be filled with cells as follows:

1: Solid - create cells inside.

2: Surface - create cells below.

3: Surface - create cells above.

4: Surface - create cells to the South.

5: Surface - create cells to the North.

6: Surface - create cells to the West.

7: Surface - create cells to the East.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Model prototype file. You may specify the name of an existing block model to define the model prototype settings. The process only uses the model extent and cell size fields as specified in the data definition - any actual cells or subcells are ignored. If a prototype model is not specified, then the model dimensions are calculated automatically from the parameter described below and the extent of the wireframe points data. |  Input |  No |  Block Model Prototype File  
WIRETR |  Input wireframe triangle file. The wireframe may consist of one or more solid wireframes, or one or more single surface DTMs. It may not contain both solid wireframes and DTMs. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe points file. |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model File |  Output block model file. This will include the 13 standard model fields plus the **ZONE** field, if specified.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ZONE |  Name of the attribute field to be created in the output model file. If this field exists in the wireframe file then the wireframe attribute values are passed from the wireframes to the model cells. |  Undefined |  yes |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ZCODE |  Zone code to be inserted in the output model **ZONE** field. This parameter is ignored if the field **ZONE** exists in the wireframe triangle file. |  No |  1 |  Undefined |  Undefined  
WIRETYPE |  Type of wireframe model to be filled with cells. Select one of the following options, with the default being 1. See **Cell Creation Methods**. |  Yes |  1 |  1,7 |  1,2,3,4,5,6,7  
CELLXMIN |  Minimum cell size in the X direction. If it is set to zero then seam filling is used - ie the cell is split once at the wireframe boundary. Only one of the values **CELLXMIN** , **CELLYMIN** , and **CELLZMIN** may be zero. |  yes |  2.5 |  0,10000 |  Undefined  
CELLXMAX |  Maximum (ie parent) cell size in the X direction. This is ignored if **PROTO** is defined. |  No |  10 |  0.5,10000 |  Undefined  
CELLYMIN |  Minimum cell size in the Y direction. If it is set to zero then seam filling is used - ie the cell is split once at the wireframe boundary. Only one of the values **CELLXMIN** , **CELLYMIN** , and **CELLZMIN** may be zero. |  yes |  2.5 |  0,10000 |  Undefined  
CELLYMAX |  Maximum (ie parent) cell size in the Y direction. This is ignored if **PROTO** is defined. |  No |  10 |  0.5,10000 |  Undefined  
CELLZMIN |  Minimum cell size in the Z direction. If it is set to zero then seam filling is used - ie the cell is split once at the wireframe boundary. Only one of the values **CELLXMIN** , **CELLYMIN** , and **CELLZMIN** may be zero. |  yes |  2.5 |  0,10000 |  Undefined  
CELLZMAX |  Maximum (parent) cell size in the Z direction. This is ignored if **PROTO** is defined. |  No |  10 |  0.5,1000 |  Undefined  
CHECKROT |  Set to 1 to automatically detect and correctly process rotated models. Using this parameter means that the input wireframe points file no longer needs to be transformed into the model space before using this process. |  No |  0 |  0, 1 |  Undefined  
  
Related topics and activities

  * [TRIFIL Process](<trifil.md>)