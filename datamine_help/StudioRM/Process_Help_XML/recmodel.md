# RECMODEL Process  
  
To access this command:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **RECMODEL** and click **Run**.
  * Enter "RECMODEL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RECMODEL>).

## Process Overview

RECMODEL is used to compare the tonnes and grades of pairs of groups of cells in a block model with the same value of two ID fields. An example of how it might be used is to compare the optimised pushbacks defined in a block model against designed pushbacks defined by another set of field values.

### Input Files

#### MODEL File

Input model file for reconciliation. It must contain a field identifying the cells to be reconciled with the wireframe volumes.

For example, if the model has been created by NPV Scheduler this field may be the optimally planned pushback identifier PSB_PIT or PIT_NO. The wireframe files could represent the planned pushbacks. The results would provide an indication of how close the designed pushbacks are to the optimised pushbacks.

### Output Files

#### Results

Output results file containing tonnes and grades for categories of each unique value of **IDFIELD2**. The categories, with value of **RECCODE** from 1 to 5, are as follows:
    
    
    CODE=1, SOURCE=IDFIELD1:

The total amount of material in the model with a specified value of **IDFIELD1**.
    
    
    CODE=2, SOURCE=IDFIELD2:

The total amount of material in the model with a specified value of **IDFIELD2**.
    
    
    CODE=3, SOURCE=IDFIELD1 and IDFIELD2:

The total amount of material in the model with the same specified value of **IDFIELD1** AND **IDFIELD2**.
    
    
    CODE=4, SOURCE=IDFIELD1 Only:

The total amount of material in the model with a specified value of **IDFIELD1** and NOT with the specified value of **IDFIELD2**.
    
    
    CODE=5, SOURCE=IDFIELD2 Only:

The total amount of material in the model with a specified value of **IDFIELD2** and NOT with the specified value of **IDFIELD1**.

[![](../Images/RECMODEL_1.png)](<javascript:void\(0\);>)

## Input Files 

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
MODEL |  Input model file for reconciliation. It must contain a field identifying the planned cells to be reconciled with the wireframe volumes.  If the model has been created by Studio NPVS or Studio NPVS+ this field may be the optimally planned pushback identifier **PSB_PIT**. |  Input |  Yes |  Block model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
RESULTS |  Output |  Yes |  Results |  Output results file containing the reserve comparisons. This contains up to 5 records for every separate reconciled volume: Total Planned, Total Mined, Planned and Mined, Planned Only and Mined Only. Volumes are defined by the **PLANNED** and **MINED** fields and can be further broken down by the **KEY1** field and **BENCH** parameter.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
PLANNED |  Field in **MODEL** file used to group the planned blocks. If comparing wireframe designs with pushback reserves in a Studio NPVS or Studio NPVS+ model this field may be **PSB_PIT**. |  MODEL |  Yes |  Any |  Undefined  
MINED |  Field in the **WIRETR** file defining the volumes to be compared to the corresponding **PLANNED** block model cells. |  WIRETR, MODEL |  Yes |  Any |  Undefined  
KEY1 |  Optional Key field in the **MODEL** file used to categorize results (for example, a rock type field). |  MODEL |  No |  Any |  Undefined  
DENSITY |  Density field in the **MODEL** file used to calculate tonnages. |  MODEL |  No |  Any |  DENSITY  
GRADE1-10 |  Grade field in the model file |  MODEL |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VALUE |  Value of **PLANNED** and **MINED** fields to compare. If undefined or zero then all values of **MINED** field will be compared. |  No |  Undefined |  Undefined |  Undefined  
MODLTYPE |  Type of wireframe model to be filled; one of the following options, with default of (1) :- |  1 | Solid 3d, interior to be filled with cells  
---|---  
2 | Solid 3d, exterior to be filled with cells  
3 | Surface, cells to be filled below (for XY), to south (for XZ), or to west (for YZ)  
4 | Surface, cells to be filled above (for XY), to north (for XZ), or to east (for YZ)  
5 | Fill between two surfaces with cells.  
6 | Two surfaces, cells to be filled above upper surface and below lower surface.  
Yes |  1 |  1, 6 |  1,2,3,4,5,6  
FACTOR |  Scaling factor to adjust the units of the Volume and Tonnage in the output files. Volume and Tonnage are divided by this factor. |  No |  1 |  Undefined |  Undefined  
SETABSNT |  Set to 1 to allow **[TONGRAD](<tongrad.md>)** to internally reset absent grade and density values. If this is used, absent grade values are set to their default values. If the default value is absent grade values are set to zero. If density values are absent the default **DENSITY** parameter value is used." |  No |  0 |  0, 1 |  0, 1  
BENCH |  Set to 1 to categorize the reserve comparisons by benches. |  0 |  Do not categorize by benches  
---|---  
1 |  Categorize the results by benches (as defined by the model ZINC default value)  
No |  0 |  0, 1 |  0, 1  
  
## Example
    
    
    !RECMODEL &MODEL(phasemodel),&RESULTS(recmodel_res),*IDFIELD1(PSB_PIT),  
  
---  
      
    
    *IDFIELD2(PHASE),*KEY1(ROCKCODE),*DENSITY(DENSITY),  
      
    
    *GRADE1(AU),@FACTOR=1.0,@SETABSNT=1.0,@BENCH=0.0  
      
    
    ... Input model: phasemodel  
      
    
    ... Default DENSITY value : 1  
      
    
    ... Block Model Field identifier: PSB_PIT  
      
    
    ... Wireframe Field identifier: PHASE  
      
    
    ... Counting number of PSB_PIT values in model phasemodel  
      
    
    ... 8 unique values of PSB_PIT found in model phasemodel  
      
    
    ... Identifying cells for PHASE 1 (Number 1 of 8)  
      
    
    ... Calculating reserves in the Design  
      
    
    ...  
      
    
       
  
Related topics and activities

  * [TONGRAD Process](<tongrad.md>)