# MODSPLIT Process  
  
To access this process:

  * **Model** ribbon **> > Manipulate >> Split**.

  * Enter "MODSPLIT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MODSPLIT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MODSPLIT>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**MODSPLIT** splits a Datamine cell/subcell model using an input wireframe to create a new model that is constrained by the wireframe. 

Either a solid wireframe with multiple closed volumes or a digital terrain model wireframe can be used. The volume of the wireframe is accurately represented in the split model. An optional output model **FULLMOD** may be specified. This is a model that covers the same total volume as the input model but with cell splitting to model the wireframe volumes. The input wireframe may contain multiple wireframes that are identified using the * **ZONE** field in the wireframe triangle file. The * **ZONE** values will then be included in the output model files.

**MODSPLIT** is useful for situations in which you have a mine design or mineable shapes in the form of wireframe and you wish to quickly represent those within a reserve block model. You can choose to output a model containing just the cells constrained by the wireframe shapes (**MODELOUT**) or the whole model (**FULLMOD**). The resulting model can then be used in processes such as **[TONGRAD](<tongrad.md>)** to produce reserves tables.

The input model may be rotated. If the input model &**PROTO** is a Rotated Model, as defined using the **[PROTOM](<protom.md>)** process, then the coordinates of the input points in the &**WIREPT** file are automatically transformed internally to the rotated model coordinate system for processing.

If both the input model file and the input wireframe triangle file include field ZONE then to avoid confusion in the output model files field **ZONE** from the input model file will be renamed as _MD_ZN_ _n in the output model files. n is an index from 0-9. The first replacement name will be _MD_ZN_0_. If it already exists then _MD_ZN_1_ will be used and so on. 

## Field Types

There are two special field types that can be selected as described below. All other non-selected field values will be copied to the output model(s).

#### Additive Fields

If the input model includes additive fields (for example costs or revenues) then these must be explicitly identified using the *ADDF1 - *ADDF9 fields. These fields will then be treated appropriately where the cells are split by the wireframe.

#### Grade Averaged Fields

**MODSPLIT** has the option to adjust the grades in the output model cells to be the average grade within each wireframe zone. To output average grades the fields * **AVGF1** to * **AVGF9** can be specified. 

The calculation of average grades within cells that are not constrained by the wireframes is controlled by the @DEFGRADE parameter.

  * If @**DEFGRADE** >= 0 then unconstrained cell grades are set to that value for all selected fields
  * If @**DEFGRADE** = -1 then unconstrained cells are assigned the average grade of all the unconstrained cells regardless of ZONE.
  * If @**DEFGRADE** is not set or set to absent data (-) then unconstrained cells grades are unchanged from the input model.

**Note** : If @**DEFGRADE** is used to set a default grade when averaging then the total grade of the output model will usually NOT be the same as the input model.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
MODELIN |  Input model file. |  Input |  Yes |  Block Model  
WIRETR |  Input wireframe triangle file used to split the model cells. |  Input |  Yes |  Wireframe  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODELOUT |  Output model file to be created that contains only cells constrained (and split) by the input wireframe. Which cells are written to this model depends on the @**MODLTYPE** parameter. |  Yes if FULLMOD is not specified, otherwise no. |  Input |  Block Model  
FULLMOD |  Output full model file to be created. This model covers the same volume as the input model but it has split cells where the original cells intersect the input wireframes. Cells constrained by the wireframe are flagged with a **ZONE** value depending on field value of * **ZONE** and the parameter @**ZONE**. |  Yes if MODELOUT is not specified, otherwise no. |  Input |  Block Model  
  
Note: **MODSPLIT** will still run if both **FULLMOD** and **MODELOUT** are absent but a message indicating this is displayed in the **Output** window. At least one of the inputs is necessary.

## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ZONE |  Name of zone field, if any, in input wireframe with multiple zones. If the field is specified then it is created in the output model file with the corresponding zone value as defined by the wireframe. The field can be either numeric or 4 character alpha. If not specified and a field **ZONE** exists in **WIRETR** then it will automatically be used. |  WIRETR |  No |  Undefined |  Undefined  
MINED |  Optional field to be added to the output full model. Cells constrained by the wireframes will have a value of 1, cells outside or not constrained by the wireframes will have a value of zero |  |  No |  Numeric |  Undefined  
ADDF1 to ADDF9 |  Field(s) to be treated as additive(s) e.g. cost and revenue values. |  MODELIN |  No |  Numeric |  Undefined  
AVGF1 to AVGF9 |  **MODSPLIT** has the option to adjust the grades in the output model cells to be the average grade within each wireframe zone. To output average grades the fields * **AVGF1** to * **AVGF9** can be specified. The calculation of average grades within cells that are not constrained by the wireframes is controlled by the @**DEFGRADE** parameter. |  MODELIN |  No |  Numeric |  Undefined  
DENSITY |  Density field in the input model file to be used when averaging grade fields. If this is not set and a **DENSITY** field exists in the model file it will be used. Otherwise Density is specified using the **DENSITY** parameter. |  MODELIN |  No |  Numeric |  DENSITY  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MODLTYPE |  Type of wireframe model to be filled; one of the following options, with default of (1) :- =1 : solid 3d, interior to be filled with cells. =2 : solid 3d, exterior to be filled with cells. =3 : surface, cells to be filled below (for XY), to south (for XZ), or to west (for YZ). =4 : surface, cells to be filled above (for XY), to north (for XZ), or to east (for YZ). =5 : fill between two surfaces with cells.. =6 : two surfaces, cells to be filled above upper surface and below lower surface. |  Yes |  1 |  1,6 |  1,2,3,4,5,6  
ZONE |  Zone code to be inserted into output model ZONE field if field does not exist in input wireframe model. |  No |  0 |  |   
MAXDIP |  Reference gradient used to calculate the degree of cell splitting as described in the Full Description (0). | No | 0 | 0,90 |   
SPLITS |  Maximum amount of splitting to be allowed (3). =0 : no splitting: parent cell. =1 : 1 split: 2 x 2 subcells. =2 : 2 splits: 4 x 4 subcells. =3 : 3 splits: 8 x 8 subcells. | No |  3 | 1,3 | 1,2,3  
PLANE |  Optional alpha parameter defining orientation 'XY', 'XZ', or 'YZ', of plane in which subcell splitting is to be performed. Care must be taken in selection of the plane to be used if the ends of the wireframe have not been linked, as the wireframe model is then partially 'hollow' when viewed from certain directions. | No | XY |  | XY, XZ, YZ  
XSUBCELL |  Number of subcells in X direction (1). Max 100. Only used if SPLITS=0. | No | 1 | 1,100 |   
YSUBCELL |  Number of subcells in Y direction (1). Max 100. Only used if SPLITS=0. | No | 1 | 1,100 |   
ZSUBCELL |  Number of subcells in Z direction (1). Max 100. Only used if SPLITS=0. | No | 1 | 1,100 |   
RESOL |  Defines boundary resolution in direction perpendicular to plane of filling. =0 : precise boundary location. =N : boundary rounded to nearest 1/Nth of parent cell size. | No | 0 | 0,N |   
DENSITY |  Default Density value to be used when averaging grades. This is used if there is no **DENSITY** field in the input block model or if Density values in the model are absent. | No | 1 |  |   
DEFGRADE |  The calculation of average grades within cells that are not constrained by the wireframes is controlled by the @**DEFGRADE** parameter.

  * If @**DEFGRADE** >= 0 then unconstrained cell grades are set to that value for all selected fields
  * If @**DEFGRADE** = -1 then unconstrained cells are assigned the average grade of all the unconstrained cells regardless of ZONE.
  * If @**DEFGRADE** is not set or set to absent data (-) then unconstrained cells grades are unchanged from the input model

| No | - |  |   
USEZONE |  If the wireframe triangle file includes field ZONE then by default MODSPLIT will use it for zone control unless a different zone field is explicitly selected. Parameter @**USEZONE** has been introduced to allow field **ZONE** to exist in the triangle file but not used for zone control. 

  * If field **ZONE** exists in the triangle file but is not to be applied set @**USEZONE** =0
  * If field **ZONE** exists in the triangle file and is to be applied then select it explicitly or set @**USEZONE** =1

| No | 1 | 0,1 | 0,1  
TOLERNCE |  Defines the smallest cell that will be included in **OUT**. Defined as a factor **XINC** , **YINC** , **ZINC**. | No | 0.001 | undefined | undefined  
  
## Example
    
    
    !MODSPLIT &MODELIN(MODEL),  
  
---  
      
    
    &WIREPT(TOPOPT), &WIRETR(TOPOTR),  
      
    
    & MODELOUT(SPLITMOD), *ZONE(ROCK),    
      
    
    @MODLTYPE=1, @MAXDIP=0, @SPLITS=0, @PLANE='XY',   
      
    
    @XSUBCELL=2, @YSUBCELL=2, @ZSUBCELL=2, @RESOL=2,  
      
    
    @ZONE=1, @DENSITY=2, @DEFGRADE=-  
  
## Error and Warning Messages

>>> |  WARNING - DATA ABOVE TOP OF MODEL <<<  
---|---  
>>> |  ERR 132 <<< ( n) IN TRIFIL  
|  Data in the input wireframe point data file has been found to be above the top of the model. Warning; processing continues.  
>>> |  WARNING - DATA BELOW BOTTOM OF MODEL <<<  
>>> |  ERR 133 <<< ( n) IN TRIFIL  
|  Data in the input wireframe point data file has been found to be below the bottom of the model. Warning; processing continues.  
>>> |  NO DATA IN INPUT FILE <<<  
>>> |  ERR 136 <<< ( n) IN TRIFIL  
|  The input wireframe point data file has no data. Fatal; the process is exited.  
>>> |  MISSING OR ALPHA FIELDS IN MODEL PROTOTYPE <<<  
>>> |  ERR 142 <<< ( n) IN TRIFIL  
|  Fatal; the process is exited.  
>>> |  ERR 143 <<< ( n) IN TRIFIL  
|  Fatal; the process is exited.  
>>> |  MISSING OR ALPHA FIELDS IN WIREPT FILE <<<  
>>> |  ERR 145 <<< ( n) IN TRIFIL  
|  Fatal; the process is exited.  
>>> |  MISSING OR ALPHA FIELDS IN WIRETR FILE <<<  
>>> |  ERR 146 <<< ( n) IN TRIFIL  
|  Fatal; the process is exited.