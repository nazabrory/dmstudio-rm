# ADDMOD Process

To access this process:

  * **Model** ribbon **> > Manipulate >> Combine**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ADDMOD** and click **Run**.
  * Enter "ADDMOD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ADDMOD>).

## Process Overview

Adds two models together by superimposing one onto another.

The resulting output model will contain all fields from both input models. Both input models must have the same origin, the same cell dimensions and the same number of cells in the three directions. However the models may have different numbers of sub-cells in equivalent cells, and the models may also have different cells undefined.

**ADDMOD** would be used for example to superimpose a surface model onto a grade model. This would enable the grade of all cells or sub-cells lying between two surfaces to be identified. If the surface model contains a rock type field showing which cells and sub-cells lie between the two surfaces and the grade model contains an interpolated grade field then the output model will contain both these fields.

If neither model contains any sub cells then the resulting output model will contain all cells which are in the two models. If a cell exists in one model but not in the other then default values will be assigned for those cells in the latter model. The resulting output model will be the same as if the two models had been added together using the **[JOIN](<join.md>)** process on the **IJK** field.

If one of the models, model A, contains sub-cells but the other one, model B, does not, then the output model will contain the same sub-cells as model A and each sub-cell will be assigned the field values from the appropriate cell of model B. If both models contain sub-cells but the sub-cells in a particular cell in one model are not t he same as the sub-cells in the same cell in the other model then the two sets are superimposed thus creating additional sub-cells in the output model.

Both input models must be sorted on the **IJK** field. Note that if the model editor was used to insert or split cells then the file will not be in the required order, and must be sorted first.

The @**TOLERNCE** parameter is used to define the smallest sub cell that will be written to the output model file. It is defined as a factor of the parent cell size in the three dimensions. If a subcell has dimensions xs, ys, zs and the parent cell has dimensions xp, yp, zp, then if xs<@**TOLERNCE** *xp or ys<@**TOLERNCE** *yp or zs<@**TOLERNCE** *zp then the sub cell is considered too small and will not be written to the output model. Care should be taken if the model is a seam type model with just a single cell in one direction. In such a case it may be necessary to set a value which is smaller than the default of 0.001 to avoid sub cells being eliminated unnecessarily.

**Note** : If a particular cell has different sets of sub-cells in the two input models then the superimposition of the sub-cells will create an output model with more sub-cells than either of the two input models. The data for each sub-cell is held as a single record in the model file. Therefore, if there is a significant disparity between sub-cells in the two input models then the output model will be much larger than the input models. Both input models must be sorted on the IJK field, for this process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Model to be updated (sorted on IJK). Must contain at least the fields XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK. |  Input |  Yes |  Block Model  
IN2 |  Update model (sorted on IJK). |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model |  Output model.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
TOLERNCE |  Defines the smallest cell that will be included in OUT. Defined as a factor of XINC, YINC, ZINC. Default = (0.001). |  No |  0.001 |  0,1 |  Undefined  
  
## Example
    
    
    !ADDMOD &IN1(GOLDMOD.1), &IN2(TOPOMOD),   
  
---  
      
    
     &OUT(GOLDMOD.2)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> FATAL ERROR! VIRTUAL ARRAY OVERRUN AT RECORD xxxxx |  Too many sub cells are being operated on. The system is not able to store all of the data during the operation.  
>>> FATAL ERROR. INPUT FILE n NOT SORTED ON IJK FIELD |  Both input files must be sorted on IJK. n is the internal file number of the model file. Fatal; the process is exited.  
>>> ERR 122 <<< (n) IN ADDMOD |  One or more model fields are missing from one of the input models. n is the internal file number of the model file. Fatal; the process is exited.  
>>> INCONSISTENT DATA DEFINITIONS IN TWO MODEL INPUT FILES >>> DEFAULT VALUES FOR FIELDS IN THE TWO MODEL FILES MUST CORRESPOND >>> ERR 123 <<< ( n) IN ADDMOD |  The two input models do not have the same model field default values. Either the model origin, the cell dimensions, or the number of cells are different. Fatal; the process is exited.  
  
Related topics and activities

  * [Block Model Size Limits](<../COMMON/Block_Models_Size_Limits.md>)