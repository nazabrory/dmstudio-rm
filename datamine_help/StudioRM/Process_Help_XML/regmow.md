# REGMOW Process  
  
To access this command:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **REGMOW** and click **Run**.
  * Enter "REGMOW" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#REGMOW>).

## Process Overview

Create a regular cell model for pit optimization.

Note: This can be performed on any type of Datamine block model.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input model prototype file, defining the new model origin, number of cells and cell sizes. This is typically set up by process **[PROTOM](<protom.md>)**. The fields required are **XMORIG, YMORIG, ZMORIG, NX, NY, NZ, XINC, YINC, ZINC** (all implicit) and **IJK, XC, YC, and ZC** (all explicit). |  Input |  Yes |  Block Model Prototype  
IN2 |  Input model file for conversion. This must have the fields **XMORIG, YMORIG, ZMORIG, NX, NY, NZ** (implicit) and **IJK, XC, YC and ZC** (explicit).  **XINC, YINC and ZINC** must exist as either explicit (sub-cells permitted) or implicit (no sub-cells). There must also be at least one explicit numeric data field, to be specified as **F1**. The records may be in any order, but speed is greatly increased if they are in **IJK** order. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model File |  Output model file. This will have the model parameters of the input prototype file on IN1 , and may contain up to five averaged fields ( **F1** -**F5**). It will also contain the fields **OREVOL, WASVOL** and **AIRVOL**.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
BLTYPE |  Field in **IN2** which contains a specific value **AIRVAL** when the sub-cell is air. |  IN2 |  No |  Any |  Undefined  
F1-F5 |  Explicit numeric fields to be averaged. F1 is mandatory. |  IN2 |  Yes for F1, no otherwise. |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
AIRVAL |  The value of the **BLTYPE** field that will be used to recognize air blocks and sub-blocks in the input model. |  No |  Undefined |  Undefined |  Undefined  
CUTOFF1 |  If the value in field **F1** is below this, the sub-cell is treated as waste. |  No |  Undefined |  Undefined |  Undefined  
RESTRICT |  Set to 1 if only the blocks on the input model are to be reported in the regularized model. Default is 0. |  No |  0 |  0,1 |  0,1  
PRINT |  >=2 display for each input cell or sub-cell that intersects with an output model cell; **IJK1, IJK, NUMMET, XC, YC, ZC, VOLP, VOLT, F1** [IJK of input and output cell, sub-cell no., input cell centre, volume intersected, total volume to date in output cell, **F1** value] and for each output cell, **IJK, WASVOL, OREVOL** , the **F1** name and the **F1** value. (0). |  No |  0 |  0,2 |  0,1,2  
  
Related topics and activities

  * [PROTOM Process](<protom.md>)