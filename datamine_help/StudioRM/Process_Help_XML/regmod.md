# REGMOD Process

To access this command:

  * **Model** ribbon **> >Mining >> Reblock >> Regularize**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **REGMOD** and click **Run**.
  * Enter "REGMOD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#REGMOD>).

## Process Overview

Produces a regular cell model from any type of Datamine ore body block model.

The parameters for the output regular cell model are taken from the prototype model &**IN1**. The model to be converted is &**IN2**. The regular model is output to &OUT.

The prototype model may be constructed by using the [PROTOM](<protom.md>) process. Any number of cells and any cell size may be chosen; **REGMOD** computes a weighted average of all input cells and sub-cells falling within the new cell size. However, it is better to choose a multiple or sub-multiple of the input cell size whenever possible, with the new origin chosen so that as many cell boundaries coincide between the old and new models as possible.

The output model will usually have larger cells than the input. However, **REGMOD** will also allow the input model to be divided into smaller cells, if required. Note however that values are always output for whole cells only; sub-cells will not exist in the output model.

The output model will contain two extra fields; **FILLVOL** , which is the total volume in the output cell filled by cells and sub-cells in the input model; and **VOIDVOL** , which is the total cell volume minus **FILLVOL** , or the total volume of the output cell which was not covered by cells and sub-cells.

Up to 25 numeric fields from the input model are averaged and placed in the output model. These fields are specified as field names * **F1** to * **F25**. Averaging is by volume weighting. There must be at least one numeric value field in the input model (* **F1**).

It should be noted that absent grade values are treated as ZERO when regularizing. For example if a cell is divided into two equal subcells of volume 500 each and the AU value in one subcell is 1, and - (absent data) in the other, then the regularised AU value over the parent cell is calculated as 0.5, the **FILLVOL** as 1000 and the **VOIDVOL** as 0. However, if the subcell with absent data is removed, leaving just one subcell, then the regularized **AU** value is 1, the **FILLVOL** is 500 and **VOIDVOL** is 500.

This treatment of absent data values has been designed specifically for calculating the revenue value of a cell in the regularized model, using a process such as [EXTRA](<extra.md>). For example if the revenue for a unit of **AU** is $100 then the dollar value is calculated as:
    
    
    revenue = FILLVOL x grade x $value

  * Case 1: revenue = 1000 x 0.5 x 100 = 50,000

  * Case 2: revenue = 500 x 1.0 x 100 = 50,000 

If **REGMOD** is used for other purposes then the implication of this treatment of absent data grade values should be considered carefully.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input model prototype file, defining the new model origin, number of cells and cell sizes. This is typically set up by process **PROTOM** or create-model-prototype. |  Input |  Yes |  Block Model Prototype  
IN2 |  Input model file for conversion. This must have the fields **XMORIG, YMORIG, ZMORIG, NX, NY, NZ** (implicit) and **IJK, XC, YC and ZC** (explicit). **XINC, YINC** and **ZINC** must exist as either explicit (sub-cells permitted) or implicit (no sub-cells). There must also be at least one explicit numeric data field, to be specified as **F1**. The records may be in any order, but speed is increased if they are in IJK order. |  Input |  Yes |  Block Model  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model |  Output model file. This will have the model parameters of the input prototype file on IN1 , and may contain up to twenty five averaged fields ( F1-F25). It will also contain the fields FILLVOL and VOIDVOL.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1-F25 |  Explicit numeric fields to be averaged. |  IN2 |  No |  Any |  Undefined  
FIELDNAM |  Field in **FIELDLST** to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  >=2 display for each input cell or sub-cell that intersects with an output model cell; **IJK1,IJK,NUMMET,XC,YC,ZC,VOLP,VOLT,F1** [IJK of input and output cell, sub-cell no., input cell centre, volume intersected, total volume to date in output cell, **F1** value] and for each output cell, **IJK, FILLVOL** and **VOIDVOL** values, and the **F1** value. (0). |  No |  0 |  0,2 |  0,1,2  
  
## Example
    
    
    !REGMOD     &IN1(PROTMODL),&IN2(OLDMODEL),  
  
---  
      
    
    &OUT(LGMODEL),*F1(DOLLARS)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> NO NUMERIC FIELDS TO ACCUMULATE. |  One or more of the given field names (*F1-*F25) did not exist, or were implicit, or not numeric. Fatal; the process is exited.  
>>> ERR 122 <<< ( n) IN REGMOD |  One or more of the essential fields in either the prototype or input model file was absent.  
Fatal; the process is exited.