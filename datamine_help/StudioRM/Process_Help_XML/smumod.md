# SMUMOD Process

To access this process:

  * Enter "SMUMOD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SMUMOD** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SMUMOD>).

## Process Overview

'Shortcut' method for grade and tonnes above cut-off.

The process uses the 'Shortcut' method to estimate the recovered tonnage and recovered grade above a single user specified cut-off. The input file must be a standard model file containing a kriged grade estimate and a kriged variance. The output model file contains all the fields from the input file plus two additional fields:

  * **FFREC** the proportion of the block above the cut-off.

  * **VALREC** the grade of the proportion above cut-off.

A Selective Mining Unit (SMU) is the smallest block size that can be mined selectively. The dimensions of an SMU can be defined using parameters **SMUXINC , SMUYINC** and **SMUZINC**. The recovered values in the output model file are a function of the specified size of SMU. 

The process takes account of the distribution of SMUs within each model cell or subcell. This distribution may be either normal (1) or lognormal (2); it is specified by parameter **SMUDIST**. If a normal variogram model is fitted (**LOG** =0) but the distribution of the SMUs is lognormal (**SMUDIST** =2) then the mean of the data values (**DATAMEAN**) must be specified.

Care should be taken when using a normal distribution for SMUs (**SMUDIST** =1). Under certain conditions the method can give an overestimation of grade when the block grade is low. This is due to the fact that the theoretical normal distribution can have values below zero, which is not possible in practice. This can lead to the situation where the metal above a cut-off is estimated to be greater than the total metal for the whole block. In such a case a warning message is displayed.

**INFOEFF** is the information effect variance. It is a constant representing the final production data variance correction and is added to the kriging variance. For further information refer to Journel and Huibrechts.

A similar situation of overestimation can also arise using a lognormal distribution for SMUs when the grade is low compared to the additive constant (**ADDCON**). In such a case a reduction in the additive constant should be considered.

The dispersion variance of an SMU within a model cell or subcell can be defined using one of three methods as controlled by parameter **DVMETHOD**.

  1. The user defines a single dispersion variance using parameter **DISVAR**. This variance will then be used as the variance of an SMU within every cell and subcell in the model. This option is therefore most appropriate if all cells in the model are the same size. If this is used there is no need to specify the dimensions of the SMU.

  2. The user defines the variogram model and the dimensions of the SMU by parameter. A single dispersion variance is then calculated for the SMU within a parent cell, and this value is used for all cells and subcells. This is similar to 1 above, except that the dispersion variance is calculated by the process rather than being supplied by the user through parameter **DISVAR**.

  3. The user defines the variogram model and the dimensions of the SMU by parameter. An individual dispersion variance is then calculated for the SMU within each cell and subcell. This is therefore more appropriate than options 1 or 2 if the model contains different cell sizes.

The calculation of the dispersion variance is one of the more time consuming parts of the process if **DVMETHOD** =3. This can be speeded up by making certain approximations as described below. This option is controlled by parameter **VARTYPE**.

  1. The exact dimensions of the subcell are used, and so the dispersion variance is calculated for every subcell in the model.

  2. Each subcell is approximated to one of a discrete number of subcells. As each subcell is processed reference is made to a look up table to see whether the dispersion variance for that size subcell has already been calculated. If it exists then the value is used; if not then it is calculated and stored in the table. This gives a large speed improvement

Whichever option is used the dispersion variance of an SMU in a parent cell is calculated once and stored. Therefore the increase in speed under option 2 will be most apparent when the model includes a large number of subcells.

If **DVMETHOD** =3 and **VARTYPE** =2 then each subcell is approximated by one of a discrete number of sizes. This is controlled by parameters **XSTEP , YSTEP** and **ZSTEP**. Dispersion variances are stored for subcells whose dimensions are an integer multiple of the step sizes. The maximum possible number of increments in each dimension is 20, making a total of 8000 (20**3) discrete sizes.

The user should ensure that the step size in each dimension is greater than or equal to one twentieth of the dimension of the parent cell for the model.
    
    
    XSTEP >= XINC / 20

If this is not the case then the step value will be reset as one twentieth of the parent cell dimension.

## Input Files

  
Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file containing the kriged grade estimate and the kriging variance. |  Input |  Yes |  Block Model  
VMODPARM |  Variogram model parameter file. A variogram model is only required if **DVMETHOD** = 2 or 3. |  Input |  No |  Variogram - Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model |  Output model file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  A field in the model file which contains the kriged grade estimate. |  IN |  Yes |  Numeric |  Undefined  
VARIANCE |  A field in the model file which contains the kriging variance (eg as created by ESTIMA). |  IN |  Yes |  Numeric |  Undefined  
FRREC |  The field to be created in the output model to store the recovered fraction. |  OUT |  Yes |  Numeric |  Undefined  
VALREC |  The field to be created in the output model to store the grade of the recovered fraction. |  OUT |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CUTOFF |  Cut-off grade for calculation of recovered fraction and grade. |  No |  1.0 |  0.000001,+ |  Undefined  
DVMETHOD |  Method for calculating dispersion variance. |  Option |  Description  
---|---  
1 |  by parameter DISVAR  
2 |  user defines variogram model and the dimensions of the SMU by parameter. A single dispersion variance is calculated for the SMU within a parent cell, and this value is used for all cells and subcells.  
3 |  user defines variogram model and the dimensions of the SMU by parameter. A dispersion variance is calculated for the SMU within each cell and subcell in the model.  
No |  3 |  1,3 |  1,2,3  
VARTYPE |  Method for calculating the variance of a sample in a cell (1). This only applies if DVMETHOD = 3. |  Option |  Description  
---|---  
1 |  the exact dimensions of the cell are used  
2 |  the cell is approximated to one of a discrete number of cells. The values for these cells are stored to avoid the need for recalculation for the cell of the same size. This gives a large speed improvement  
No |  1 |  1,2 |  1,2  
SMUDIST |  Distribution of SMUs: =1 normal  =2 lognormal  =3 truncated normal |  No |  1 |  1, 3 |  1, 2,3  
DISVAR |  Dispersion variance value. (0) This is only required if **DVMETHOD** =1. |  No |  0 |  Undefined |  Undefined  
ADDCON |  Additive constant for three parameter lognormal distribution of SMUs. This only applies if **SMUDIST** =2. |  No |  0 |  Undefined |  Undefined  
VMODNUM |  Variogram model reference number as defined by the **VREFNUM** field in the **VMODPARM** file. This only applies if **DVMETHOD** = 2 or 3. |  No |  1 |  Undefined |  Undefined  
LOG |  Log/Normal variogram flag. Default. The variogram model, as defined by **VMODNUM** is, Normal if LOG =0 Lognormal if LOG =1. |  No |  0 |  0,1 |  0,1  
SMUXINC |  X dimension of the Selective Mining Unit. This only applies if **DVMETHOD** = 2 or 3. |  No |  1 |  Undefined |  Undefined  
SMUYINC |  Y dimension of the Selective Mining Unit.This only applies if **DVMETHOD** |  No |  1 |  Undefined |  Undefined  
SMUZINC |  Z dimension of the Selective Mining Unit (1) This only applies if **DVMETHOD** |  No |  1 |  Undefined |  Undefined  
XSTEP |  X step size for subcell approximation in variance calculations. This is only used if **DVMETHOD** =3 and **VARTYPE** =2. This must be less than the parent cell dimension in X.  |  No |  1 |  Undefined |  Undefined  
YSTEP |  Y step size for subcell approximation in variance calculations. This is only used if **DVMETHOD** =3 and **VARTYPE** =2. This must be less than the parent cell dimension in Y.  |  No |  1 |  Undefined |  Undefined  
ZSTEP |  Z step size for subcell approximation in variance calculations. This is only used if **DVMETHOD** =3 and **VARTYPE** =2. This must be less than the parent cell dimension in Z. |  No |  1 |  Undefined |  Undefined  
IPOINTS |  Number of discretisation points in X to simulate model cell. |  No |  6 |  Undefined |  Undefined  
JPOINTS |  Number of discretisation points in Y to simulate model cell. |  No |  6 |  Undefined |  Undefined  
KPOINTS |  Number of discretisation points in Z to simulate model cell. |  No |  |  Undefined |  Undefined  
DATAMEAN |  Mean grade of the input data (* **VALUE**). This is compulsory if both a normal variogram model is selected (@**LOG** =0) and a lognormal distribution of SMUs is selected (@**SMUDIST** =3). The value is used in the calculation of the variance. |  No |  Undefined |  Undefined |  Undefined  
INFOEFF |  The information effect variance. (0) This is subtracted from the variance. Refer to Journel and Huijbregts, Mining Geostatistics, pp 449-454 for details. |  No |  |  Undefined |  Undefined  
  
## Example
    
    
    !smumod     &IN(model),&VMODPARM(vmodel),&OUT(smumod),*VALUE(Fe1),  
  
---  
      
    
         *VARIANCE(KV1),*FRREC(RECFRAC),*VALREC(RECGRADE),@CUTOFF=2.5,  
      
    
         @DVMETHOD=3,@VARTYPE=1,@SMUDIST=2,@DISVAR=0,@ADDCON=0,@VMODNUM=1,  
      
    
         @LOG=0,@SMUXINC=1,@SMUYINC=1,@SMUZINC=1,@XSTEP=1,@YSTEP=1,  
      
    
         @ZSTEP=1,@IPOINTS=3,@JPOINTS=3,@KPOINTS=3  
  
Related topics and activities

  * [SMUHIS Process](<smuhis.md>)

  * [ESTIMA Process](<estima.md>)

  * [ESTIMATE Process](<estimate.md>)