# COMBMOD Process

To access this process:

  * **Model** ribbon **> > Manipulate >> Combine Multiple**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COMBMOD** and click **Run**.
  * Enter "COMBMOD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COMBMOD>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Combine up to 20 block models that may have different parent cells sizes, origins and extents into a single block model.

**COMBMOD** is useful in situations where models that have been generated to model local regions need to be recombined with a larger resource model, or where multiple local models need to be combined to use as a single model for easier reporting or visualisation.

### The Prototype PROTO file

The input model prototype file is optional. If this file is specified then the output model will have the same origin, extents, parent cell size and rotation as this file. All records in this file are ignored, only the data definition is used. If you have a file that defines the required extents of the output model and also has records that need to be combined then you need to specify it as a prototype and as one of the input files.

### The first input model file IN1

If a prototype file is not specified then the first input file is used to determine the parent cell size of the output model. The origin and extents of the output model is determined from the minimum and maximum extents of all the input models. If a prototype file is not specified then origin of the output model will lie on a parent cell boundary of the first input model. If only two input models are specified and they both share the same model definition the process is equivalent to running the ADDMOD process.

### Model Superimposition Order

Models are superimposed on one another according to **ADDMOD** logic. The order in which the input models are specified is therefore important. Input model 2 is superimposed on input model 1. Input model 3 is then superimposed on the combination of 1 and 2. This process is continued for all input models.

Any input model containing zero records, unless it is used as the prototype or causes a rotation conflict, is ignored

### Rotated models

COMBMOD supports rotated models but will only combine models that all share the same model rotation parameters, i.e. models which have identical values for the implicit fields **ANGLE1** , **ANGLE2** , **ANGLE3** , **X0** , **Y0** , **Z0** , **ROTAXIS1** , **ROTAXIS2** and **ROTAXIS3**. If any of the input files do not share the same rotation parameters as either the prototype file, or the first input file if the prototype is not specified, then the process exits with an error.

If the prototype or first model is not rotated and any of the subsequent input files are rotated then the process exist with an error

### TOLERNCE Parameter

The @**TOLERNCE** parameter is used to define the smallest subcell that will be written to the output model file. It is defined as a factor of the parent cell size in the three dimensions. If a subcell has dimensions xs, ys, zs and the parent cell has dimensions xp, yp, zp, then if xs<@**TOLERNCE** *xp or ys<@**TOLERNCE** *yp or zs<@**TOLERNCE** *zp then the subcell is considered too small and will not be written to the output model. Care should be taken if the output model is a seam type model with just a single cell in one direction. In such a case it may be necessary to set a value which is smaller than the default of 0.001 to avoid subcells being eliminated unnecessarily.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Input block model prototype that defines the extents and parent cell size of the combined model. Records in this file are ignored. This file is optional. If it is not specified models will be combined to fill the volume covered by the range of all input files. |  Input |  Yes |  Model Prototype  
IN1 |  First input model for combining (sorted on IJK). If no prototype is specified the output combined model prototype will have the same parent cell size specification as this file and the limits will be determined from the combined range of all input files. |  Input |  Yes |  Model  
IN2 |  Second input model for combining (sorted on IJK) |  Input |  Yes |  Model  
IN3 - 20 |  Additional, optional input model files for combining (sorted on IJK) |  Input |  No |  Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODELOUT |  Output |  Yes |  Model |  Output combined model  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
TOLERNCE |  Defines the smallest cell that will be included in OUT. Defined as a factor of XINC, YINC, ZINC. Default = (0.001). |  No |  0.001 |  Undefined |  Undefined  
  
## Example
    
    
    !COMBMOD &PROTO(vb_expanded), &IN1(vbpermod1),&IN2(vbmodelz2),          
  
---  
      
    
    &IN3(vbpermod2),&IN4(_vb_mod1),&MODELOUT(comb_mod),          
      
    
    @TOLERNCE=0.001  
      
    
       
      
    
    COMBMOD - Combine multiple models        ... Input validation  
      
    
    ... Combining to limits defined by prototype vb_expanded  
      
    
    ... Adjusting limits of model No. 1 (vbpermod1)  
      
    
    ... Adjusting limits of model No. 2 (vbmodelz2)  
      
    
    ... Adjusting limits of model No. 3 (vbpermod2)  
      
    
    ... Adjusting limits of model No. 4 (_vb_mod1)  
      
    
    ... Combining model No. 1 & 2 (vbpermod1 and vbmodelz2)  
      
    
    ... Warning: Model 1 (vbpermod1) has zero records  
      
    
    ... Combining model No. 3 (vbpermod2)  
      
    
    ... Combining model No. 4 (_vb_mod1)  
      
    
    Output combined model comb_mod contains 392524 records        COMBMOD finished