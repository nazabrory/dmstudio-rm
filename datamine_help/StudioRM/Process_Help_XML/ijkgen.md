# IJKGEN Process

To access this process:

  * **Model** ribbon **> > Create >> From XYZ Data**.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **IJKGEN** and click **Run**.

  * Enter "IJKGEN " into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#IJKGEN>).

## Process Overview

Recalculates or calculates the IJK field for a model.

To recalculate IJK values for an existing model, this model is entered on the &**IN** file, and a prototype model (as produced by [PROTOM](<protom.md>)) entered as the &**PROTO** file. The output file &**OUT** may be the same as the input, if required. Parameter @**PSMODEL** is set to zero in this case, meaning additional attributes other than IJK will not be transferred to the output file.

@**PSMODEL** =1 can be used to append the output file with the model fields of the input file, overwriting existing fields as required.

Recalculation of IJK values is often carried out to expand a model (for example, when the original model defined did not cover sufficient volume to include all the waste rock required for an open pit). For this, it is only necessary to define the new origin, number of cells etc. using [PROTOM](<protom.md>) before using **IJKGEN**.

#### Building a model from cell centre values

To create a valid model file from a file containing just cell centre co-ordinates, the output file must be a different name from the input. Parameter @**PSMODEL** is set to 1 to ensure that all model fields are written across from the prototype to the output file. The input file does not have to be sorted.

#### Building a model from a regular set of values

Block models coming into your application from other systems often comprise a set of values on a regular grid, with no positional data. Such data can be turned into a Datamine cell model with the aid of [EXTRA](<extra.md>) and IJKGEN. The stages are:-

1\. Enter the data as a Datamine file, with one record per block.

2\. Use [EXTRA](<extra.md>) to compute cell centre co-ordinates for each block.

3\. Use IJKGEN as described above to generate a model.

4\. Sort the model on IJK for speed of access.

### The Prototype Model

The input prototype model defines the cell sizes, origin, model dimensions etc. that will appear in the output model. Thus the process [PROTOM](<protom.md>) should be used prior to **IJKGEN** to set up this prototype model. It is very important to ensure that the model origin, cell sizes etc. are chosen so that the bottom left hand corner of a cell is at the model origin. Cell sizes should be defined to be the same as in the input model on &IN, or you run the risk of creating a model with overlapping cells or gaps between cells.

The **IJKGEN** process does not check for this, as there are circumstances where this is useful (for example, creating a pseudo model from blast hole data, where each hole is assigned to a cell with unit volume).

Note that **IJKGEN** will include rotated model fields, if found in the model prototype, to the resulting output (sorted) file).

### Data lying outside the model

If the data on &IN lies outside the model limits as defined in the prototype, then the IJK field will be set to absent data with a warning message. You must remove or change such IJK values before entering processes.

### Maximum IJK Value

The maximum IJK value is 2,147,483,647. This means you can have a model with, for example, 1400x1400x1000 parent cells.

See [Block Model Size Limits](<../COMMON/Block_Models_Size_Limits.md>).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Input prototype model describing the model parameters. Normally set up by PROTOM. Must contain the numeric fields XC, YC, ZC, IJK (explicit) and XMORIG, YMORIG, ZMORIG, NX, NY, NZ (implicit) and XINC, YINC, ZINC (either, as required). For recalculation of IJK in an existing model, may be the same file as IN. |  Input |  Yes |  Block Model Prototype  
IN |  Overwritten |  Yes |  Undefined |  Input file to be converted into a model. Must contain the fields X , Y and Z representing (sub-)cell centre locations. This can be an existing model for recalculation of IJK.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  BlockModel |  Output model file. May be the same as IN where IN already contains model fields; in this case, recalculation is in-place. IJK will be set to absent (-) if the record lies outside the model limits.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Explicit numeric field in IN containing the X co-ordinate of the (sub-)cell centre. |  IN |  Yes |  Numeric |  X  
Y |  Explicit numeric field in IN containing the Y co-ordinate of the (sub-)cell centre. |  IN |  Yes |  Numeric |  Y  
Z |  Explicit numeric field in IN containing the Z co-ordinate of the (sub-)cell centre. |  IN |  Yes |  Numeric |  Z  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PSMODEL |  |  Option |  Description  
---|---  
0 |  Just generate IJK field without copying additional attributes to the output model. This is the recommended option if your output file already contains the expected attributes.  
1 |  Place all other model fields as well as IJK into the output model. This will copy standard fields from the prototype to the output file, overwriting any fields of the same name copied from the input points file.  
Yes |  0 |  0,1 |  0,1  
  
## Example

Recalculation of IJK for oldmodel, using required model parameters from newproto. The new model is written to newmodel.
    
    
    !IJKGEN   &PROTO(newproto),&IN(oldmodel),&OUT(newmodel),   
  
---  
      
    
     @PSMODEL=0  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> WARNING - CELL AT nnnnnnn.nn LIES OUTSIDE MODEL <<< |  The IJK field will be set to absent data. If @PSMODEL=1, then XC, YC, ZC, XINC, YINC, ZINC values will also be set to absent data.  
>>> MISSING ESSENTIAL FIELD IN MODEL PROTOTYPE <<< >>> ERR 103 <<< ( fieldno) IN IJKGEN |  The prototype was missing an essential field from the set XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK. fieldno gives the index to which field was missing. Fatal; the process is exited.  
>>> BAD MODEL FILE: FIELD IMPLICIT OR WRONG TYPE <<< >>> ERR 122 <<< ( fileno) IN IJKGEN |  The prototype file was incorrect. Fatal; the process is exited.  
>>> CANNOT ADD FIELDS WHEN UPDATING IN-PLACE <<< >>> ERR 132 <<< ( 0) IN IJKGEN |  An attempt was made to use in-place updating without their being an existing IJK field, or with @PSMODEL=1 without other model fields being present. Fatal; the process is exited.  
>>> ERROR \- FIELD nnnnnnnn IS ALPHA, NOT NUMERIC <<< >>> ERR 134 <<< ( fieldno) IN IJKGEN |  One of the fields *X, *Y or *Z was alphanumeric instead of numeric in the &IN file. This message may also be produced if one of the fields is missing from the file. Fatal; the process is exited.