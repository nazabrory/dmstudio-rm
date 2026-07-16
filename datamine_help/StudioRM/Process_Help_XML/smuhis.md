# SMUHIS Process

To access this process:

  * Enter "SMUHIS" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SMUHIS** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SMUHIS>).

## Process Overview

Create a histogram using the 'Shortcut' evaluation method.

The process creates a histogram file by evaluating a kriged model using the 'Shortcut' method and estimating the tonnage distribution over the range of cutoffs specified for the histogram intervals. The data in this file can then be used to create grade/tonnage plots.

A Selective Mining Unit (SMU) is the smallest block size that can be mined selectively. The dimensions of an SMU are defined using parameters **SMUXINC** , **SMUYINC** and **SMUZINC**.The output histogram file shows the grade and tonnage for a range of cut-offs for the specified size of SMU.

The process takes account of the distribution of SMUs within each model cell or subcell. This distribution may be either normal (1) or lognormal (2); it is specified by parameter **SMUDIST**.

Care should be taken when using a normal distribution for SMUs (**SMUDIST** =1). Under certain conditions the method can give an overestimation of grade when the block grade is low. This is due to the fact that the theoretical normal distribution can have values below zero, which is not possible in practice. This can lead to the situation where the metal above a cut-off is estimated to be greater than the total metal for the whole block. In such a case a warning message is displayed. If a normal variogram model is fitted (**LOG** =1) but the distribution of the SMUs is lognormal (**SMUDIST** =2) then the mean of the data values (**DATAMEAN**) must be specified.

**INFOEFF** is the information effect variance. It is a constant representing the final production data variance correction and is added to the kriging variance. For further information refer to Journel and Huibrechts.

A similar problem of overestimation can also arise when using a lognormal distribution for SMUs and the grade is low compared to the additive constant (**ADDCON**). In such a case the additive constant should be reduced.

The dispersion variance of an SMU within a model cell or subcell can be defined using one of three methods as controlled by parameter **DVMETHOD**.

  * =1 define a single dispersion variance using parameter **DISVAR**. This variance will then be used as the variance of an SMU within every cell and subcell in the model. This option is therefore most appropriate if all cells in the model are the same size.

  * =2 define the [variogram model](<../COMMON/filetype.md#VariogramMod>) and the dimensions of the **SMU** by parameter. A single dispersion variance is then calculated for the SMU within a parent cell, and this value is used for all cells and subcells. This is similar to 1 above, except that the dispersion variance is calculated by the process rather than being supplied by the user through parameter DISVAR.

  * =3 define the [variogram model](<../COMMON/filetype.md#VariogramMod>) and the dimensions of the **SMU** by parameter. An individual dispersion variance is then calculated for the SMU within each cell and subcell. This is therefore more appropriate than options 1 or 2 if the model contains different cell sizes.

The calculation of the dispersion variance is one of the more time consuming parts of the process if **DVMETHOD** =3. This can be speeded up by making certain approximations as described below. This option is controlled by parameter **VARTYPE**.

  * =1 the exact dimensions of the subcell are used, and so the dispersion variance is calculated for every subcell in the model.

  * =2 each subcell is approximated to one of a discrete number of subcells. As each subcell is processed reference is made to a look up table to see whether the dispersion variance for that size subcell has already been calculated. If it exists then the value is used; if not then it is calculated and stored in the table. This gives a large speed improvement

Whichever option is used the dispersion variance of an SMU in a parent cell is calculated once and stored. Therefore the increase in speed under option 2 will be most apparent when the model includes a large number of subcells.

If **DVMETHOD** =3 and **VARTYPE** =2 then each subcell is approximated by one of a discrete number of sizes. This is controlled by parameters **XSTEP , YSTEP** and **ZSTEP**. Dispersion variances are stored for subcells whose dimensions are an integer multiple of the step sizes. The maximum possible number of increments in each dimension is 20, making a total of 8000 (20**3) discrete sizes.

The user should ensure that the step size in each dimension is greater than or equal to one twentieth of the dimension of the parent cell for the model.
    
    
    XSTEP >= XINC / 20  
    

If this is not the case then the step value will be reset as one twentieth of the parent cell dimension.

An optional bench perimeter can be used to constrain the evaluation. The standard perimeter fields can be supplemented by a **PCODE** field. Perimeters are evaluated assuming mid-bench position and partial cell evaluation.

The evaluation can include recovered fractions. If **RECOVERY** =f (in the range 0-1) then:

  * if **FRACTION** < (1-f), treat f as zero grade
  * if **FRACTION** > f, take the whole block at the average grade.

The output file contains the following fields:

PVALUE  |  perimeter identifier. Only created if PERIM was defined.  
---|---  
PCODE  |  secondary perimeter classification field. Only produced if PERIM and PCODE were defined.  
LOWER, MIDDLE, and UPPER  |  provide histogram bin limits with LOWER being regarded as the cut-off value.  
TONNE, TONNE-% and AVGRADE  |  provide tonnage and grade data for material reporting in the interval with full recovery.  
CTONNE, CTONNE-% and CGRADE  |  provide the cumulative tonnage and grade above the LOWER cut-off grade with full recovery. CMETAL reports the metal content ie CGRADE * TONNE.  
RECOVERY  |  is the mining recovery parameter.  
ARFTONNE and ARFGRADE  |  provide a summary of material below cut-off for those blocks where the recovered fraction is greater than RECOVERY. This material is mined as ore, but is below cut-off.  
BRFTONNE and BRFGRADE  |  provide a summary of material above cut-off for those blocks where the recovered fraction is below (1-RECOVERY). This material cannot be taken as ore, but is still above cut-off.  
TOTONNE and TOGRADE  |  report the total ore tonnes that would be mined for the RECOVERY specified. It is calculated as: TOTONNE = CTONNE + ARFTONNE - BRFTONNE  
  
The first record in the output file has absent data or zero values for most fields. The exceptions are:

CTONNE:  |  the total tonnes in the model  
---|---  
CTONNE-%:  |  100  
CGRADE:  |  the total average grade  
CMETAL:  |  the total metal content  
TOTONNE:  |  same as **CTONNE**  
TOGRADE:  |  same as **CGRADE**  
  
This record provides a summary of the total model without any cut-off. This data is not otherwise provided if the lowest cut-off specified (MINIMUM) is other than zero.

##  Input Files 

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. |  Input |  Yes |  Block Model  
VMODPARM |  Variogram model parameter file. A variogram model is only required if **DVMETHOD** = 2 or 3. |  Input |  No |  Variogram - Model  
PERIM |  Optional bench perimeter file. |  Input |  No |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file. This will contain one record for each histogram bin plus one record for the total model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  A field in the model file which contains the kriged grade estimate. |  IN |  Yes |  Numeric |  Undefined  
VARIANCE |  A field in the model file which contains the kriging variance (as created by **[ESTIMA](<estima.md>)** or [ESTIMATE Process](<estimate.md>)) |  IN |  Yes |  Numeric |  Undefined  
PCODE |  Optional perimeter key field. |  PERIM |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DVMETHOD |  Method for calculating dispersion variance (3) |  Option |  Description  
---|---  
1 |  by parameter **DISVAR**.  
2 |  user defines the variogram model and the dimensions of the SMU by parameter. A single dispersion variance is calculated for the SMU within a parent cell, and this value is used for all cells and subcells.  
3 |  user defines the variogram model and the dimensions of the SMU by parameter. A dispersion variance is calculated for the SMU within each cell and subcell in the model.  
No |  3 |  1,3 |  1,2,3  
VARTYPE |  Method for calculating the variance of a sample in a cell (1). This only applies if **DVMETHOD** = 3. |  Option |  Description  
---|---  
1 |  the exact dimensions of the cell are used  
2 |  the cell is approximated to one of a discrete number of cells. The values for these cells are stored to avoid the need for recalculation for the cell of the same size. This gives a large speed improvement  
No |  1 |  1,2 |  1,2  
SMUDIST |  Distribution of SMUs: (1) |  Option |  Description  
---|---  
1 |  normal  
2 |  lognormal  
3 |  truncated normal  
No |  1 |  1, 3 |  1, 2,3  
DISVAR |  Dispersion variance value. (0) This is only required if **DVMETHOD** =1. |  No |  0 |  Undefined |  Undefined  
DENSITY |  Default density if no density field is defined in the model.  |  No |  1 |  Undefined |  Undefined  
ADDCON |  Additive constant for three parameter lognormal distribution of SMUs. (0). This only applies if **SMUDIST** =2. |  No |  0 |  Undefined |  Undefined  
RECOVERY |  Value for recovered fraction (1). If the recovered fraction is greater than this value then the complete block is considered above cut-off. If the recovered fraction is less than 1- **RECOVERY** then none of the block is considered to be above cut-off. |  No |  1 |  Undefined |  Undefined  
BINSIZE |  Bin width for histogram. (1) |  No |  1 |  Undefined |  Undefined  
MINIMUM |  Lower bound of first bin. If SMUDIST =3, then MINIMUM must be set to zero. (0) |  No |  0 |  Undefined |  Undefined  
NUMBINS |  Number of bins, maximum 200. (50) |  No |  50 |  Undefined |  Undefined  
VMODNUM |  Variogram model reference number as defined by the **VREFNUM** field in the **VMODPARM** file. This only applies if **DVMETHOD** = 2 or 3. |  No |  1 |  Undefined |  Undefined  
LOG |  Log/Normal variogram flag. Default(0). The variogram model, as defined by VGRAM , is Normal if LOG =0 or Lognormal if LOG =1. |  No |  0 |  0,1 |  0,1  
SMUXINC |  X dimension of the Selective Mining Unit. This only applies if **DVMETHOD** = 2 or 3. |  No |  1 |  Undefined |  Undefined  
SMUYINC |  Y dimension of the Selective Mining Unit. This only applies if **DVMETHOD** |  No |  1 |  Undefined |  Undefined  
SMUZINC |  Z dimension of the Selective Mining Unit. This only applies if **DVMETHOD** |  No |  1 |  Undefined |  Undefined  
XSTEP |  X step size for subcell approximation in variance calculations. This is only used if **DVMETHOD** =3 and **VARTYPE** =2. This must be less than the parent cell dimension in X. (1) |  No |  1 |  Undefined |  Undefined  
YSTEP |  Y step size for subcell approximation in variance calculations. This is only used if **DVMETHOD** =3 and **VARTYPE** =2. This must be less than the parent cell dimension in Y. (1) |  No |  1 |  Undefined |  Undefined  
ZSTEP |  Z step size for subcell approximation in variance calculations. This is only used if **DVMETHOD** =3 and **VARTYPE** =2. This must be less than the parent cell dimension in Z. (1) |  No |  1 |  Undefined |  Undefined  
IPOINTS |  Number of discretisation points in X dimension to simulate model cell (6) |  No |  6 |  Undefined |  Undefined  
JPOINTS |  Number of discretisation points in Y dimension to simulate model cell (6) |  No |  6 |  Undefined |  Undefined  
KPOINTS |  Number of discretisation points in Z dimension to simulate model cell (6) |  No |  6 |  Undefined |  Undefined  
DATAMEAN |  Mean grade of the input data (* **VALUE**). This is compulsory if both a normal variogram model is selected (@**LOG** =0) and a lognormal distribution of SMUs is selected (@**SMUDIST** =3). The value is used in the calculation of the variance. |  No |  Undefined |  Undefined |  Undefined  
INFOEFF |  The information effect variance. (0) This is subtracted from the variance. Refer to Journel and Huijbregts, Mining Geostatistics, pp 449-454 for details. |  No |  |  Undefined |  Undefined  
  
## Example
    
    
    !smuhis     &IN(model),&VMODPARM(vmodel),&OUT(t1),*VALUE(Fe1),*VARIANCE(KV1),  
  
---  
      
    
         @DVMETHOD=3,@VARTYPE=1,@SMUDIST=1,@DISVAR=0,@DENSITY=1,@ADDCON=0,  
      
    
          @RECOVERY=1,@BINSIZE=1,@MINIMUM=20,@NUMBINS=50,@VMODNUM=1,@LOG=0,  
      
    
          @SMUXINC=1,@SMUYINC=1,@SMUZINC=1,@XSTEP=1,@YSTEP=1,@ZSTEP=1,  
      
    
          @IPOINTS=6,@JPOINTS=6,@KPOINTS=6  
  
Related topics and activities

  * [SMUMOD Process](<smumod.md>)

  * [ESTIMA Process](<estima.md>)

  * [ESTIMATE Process](<estimate.md>)