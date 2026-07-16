# MODTRA Process  
  
To access this process:

  * **Model** ribbon **> > Data From Model >> Drillholes**.

  * Enter "MODTRA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MODTRA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MODTRA>).

## Process Overview

This process creates a regular grid of trace lines through a model.

These trace lines describe the continuity of a field value or set of field values in the model. Average values of all other model fields are calculated and associated with each trace segment.

The process simulates either a rectangular grid of drillholes, drilled through the model parallel to one of model axes, or a set of drillholes whose collars are defined in the optional &**GRID** file. The user specifies between one and five fields (* **F1** to * **F5**) which are used to terminate the simulated drillhole samples. If the value of any of the specified fields change, then the sample is terminated and a new sample started. The sample is written to a standard borehole format file, together with the average value of all numeric fields for that sample. If the model contains alpha fields then the dominant value of each field is also written to the output sample file. The dominant value is defined as the value which has the longest length. If the model contains a **DENSITY** field then the calculations of the average values and of the longest length are tonnage weighted.

The output drillhole file contains the standard drillhole fields - **BHID, FROM, TO, LENGTH, A0, B0** plus all the non-model fields from the model file. **BHID** is a numeric field, starting at 1 and increasing in steps of 1.

The purpose of creating the simulated drillholes is to plot a section through them. This will show the continuity of the * **FN** variable(s) in the section plane. A similar display could also be achieved using colour fill of subcells. A model section plot without colour fill will include subcell boundaries, which will display the continuity over a field or set of fields, but not as clearly as a drillhole section.

The specified fields * **F1** \- * **Fn** should have discrete values rather than being continuous; if a numeric field is specified such as an interpolated grade, then it is highly probable that the field value will change at every subcell boundary. If it is required to show continuity over a range of numeric values, then a 'flag' field should be created in the model with **EXTRA** prior to using **MODTRA**. For example if continuity is required within grade ranges 0-2, 2-5, 5-10, 10-20, 20+ then a flag value can be created in **EXTRA** for each of the 5 ranges. This flag field can then be specified as * **F1**.

  * Having defined a plane, only two of the parameters @**XORIG** , @**YORIG** , @**ZORIG** apply. For example, if @**PLANE** = 3, (YZ) then @**XORIG** is ignored. Similarly for @**XSPACE** and @**NUMX**. 

  * The dominant value of an alpha field is calculated for each drillhole sample as that value with the greatest length (tonnage weighted if there is a **DENSITY** field in the model). In order to preallocate accumulators it is assumed that there will be a maximum of 40 discrete values for any alpha field. If during the course of calculating the dominant value within a sample, a 41st value is found, then the value with the smallest current length will be dropped from the accumulators.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
MODEL |  Input model. Must contain the 13 standard model fields - **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK** \- plus at least one other field. |  Input |  Yes |  Block Model  
GRID |  Optional input grid file defining the location of the simulated drillholes. It must contain ALL fields **XG** , **YG** , **ZG** , regardless of the **PLANE** parameter setting. This file must NOT include an alpha **BHID** field, as this would clash with the numeric **BHID** field created in **OUT**. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Drillhole File |  Output holes file. Will contain the fields **BHID, FROM, TO, X, Y, Z, LENGTH, A0, B0** plus all fields from input model file except the 13 standard model fields.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1-F5 |  Fields over which continuity is required within a sample. |  MODEL |  Yes |  Any |  Undefined  
XG |  Optional **GRID** field name holding X co-ordinate. Default is **XG**. Ignored if **PLANE** =3. |  GRID |  No |  Numeric |  XG  
YG |  Optional **GRID** field name holding Y co-ordinate. Default is **YG**. Ignored if **PLANE** =2. |  GRID |  No |  Numeric |  YG  
ZG |  Optional **GRID** field name holding Z co-ordinate. Default is **ZG**. Ignored if **PLANE** =1. |  GRID |  No |  Numeric |  ZG  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLANE |  Drillhole orientation. Default (1). |  Option |  Description  
---|---  
1 |  \- XY. A grid of vertical holes is created.  
2 |  \- XZ. A grid of horizontal holes is created, running from North to South.  
3 |  \- YZ. A grid of horizontal holes is created, running from East to West.  
No |  1 |  1,3 |  1,2,3  
XORIG |  X co-ordinate of collar of first drillhole. Default is model X origin plus half a parent cell X dimension. Ignored if **PLANE** =3 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
YORIG |  Y co-ordinate of collar of first drillhole. Default is model Y origin plus half a parent cell Y dimension. Ignored if **PLANE** =2 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
ZORIG |  Z co-ordinate of collar of first drillhole. Default is model Z origin plus half a parent cell Z dimension. Ignored if **PLANE** =1 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
XSPACE |  Spacing in X between drillholes. Default is the parent cell X dimension. Ignored if **PLANE** =3 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
YSPACE |  Spacing in Y between drillholes. Default is the parent cell Y dimension. Ignored if **PLANE** =2 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
ZSPACE |  Spacing in Z between drillholes. Default is the parent cell Z dimension. Ignored if **PLANE** =1 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
NUMX |  Number of drillholes in X direction. Default is the number up to the model X limit. Ignored if **PLANE** =3 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
NUMY |  Number of drillholes in Y direction. Default is the number up to the model Y limit. Ignored if **PLANE** =2 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
NUMZ |  Number of drillholes in Z direction. Default is the number up to the model Z limit. Ignored if **PLANE** =1 or **GRID** specified. |  No |  Undefined |  Undefined |  Undefined  
MISS |  Missing cells treatment. Default is (0) |  Option |  Description  
---|---  
0 |  Where no model cell or subcell exists, no drillhole sample will be created.  
1 |  Where no model cell or subcell exists, drillhole sample will be created with missing values.  
No |  Undefined |  Undefined |  Undefined  
PRINT |  Print flag. Default (0). 0 - minimum output. 1 - summary of percentage complete and number of holes written. |  No |  Undefined |  Undefined |  Undefined  
  
## Example

This example creates a rectangular grid of drillholes drilled horizontally through the model from east to west. The spacing in the vertical Z direction between holes is 15 m (possibly representing the bench height) and 20 m spacing in the Y (north-south) direction.
    
    
    !MODTRA &MODEL(MODEL1), &OUT(HOLES), *F1(ROCKTYPE), F2(STRAT),   
  
---  
      
    
    @PLANE=3, @YORIG= 100, @ZORIG=200, @YSPACE=20, @ZSPACE= 15  
  
## Error and Warning Messages

Message | Description | Solution  
---|---|---  
>>> Fatal Error: in ffffffff file <<< |  Where ffffffff is either **MODEL** or OUT. The program found an error on trying to access the file you specified as the ffffffff file. |  Check that the file name is correct and that it exists.  
>>> Fatal Error: in a field in ffffffff file <<< |  where ffffffff is either **MODEL** or **OUT**. The program found an error on trying to access one of the fields in the file you specified as the ffffffff file. |  Check that the file contains the compulsory fields ( the 13 standard model fields if it is the **MODEL** model file). Also check that they are of the correct type (Alpha/Numeric, Explicit/Implicit).  
>>> Fatal Error: F1 field not in MODEL file <<< |  A field reference has been set but it doesn't exist in **MODEL**. |  Check that the specified * **F1** field exists in the input **MODEL** file.