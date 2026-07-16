# INDEST Process

To access this process:

  * **Estimate** ribbon **> > Non-linear >> MIK >> INDEST Process**.
  * Enter "INDEST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **INDEST** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INDEST>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

The INDEST process uses the Indicator Estimation (IE) method to estimate grades into a block model using the cumulative distribution function (CDF) of indicator transformed sample grades

To operate, INDEST needs a series of threshold values between the smallest and largest grade values. These threshold values, referred to as cutoffs, are used to numerically build the CDF of each block in the model. For each cutoff, data in the search volume are transformed into 0s and 1s: 1s if the data are greater than the threshold, and 0s if they are less than or equal. It then estimates the probability that the block grade is greater than the threshold value, using one of the standard estimation methods. This is usually kriging, but INDEST allows other methods such as Nearest Neighbour or Inverse Power of Distance to be used. Performing this operation for each cutoff across the range of the sample data approximates the CDF for the model cell. After the CDF is built, it is post processed to calculate the indicator estimated grade.

INDESTuses the ESTIMAprocess to do the estimation for each cutoff. For further details of ESTIMA.

If you are using Indicator Kriging (IK) then you must already have calculated a variogram for each cutoff, and stored the models in the Variogram Model file. The[VGRAM](<vgram.md>)process has specific features for calculating indicator variograms.

For each cutoff INDESTcalculates the following data which can optionally be stored in the **Output Model** file:

  * The proportion (fraction) of the model subcell which is above cutoff.

  * The grade of the proportion of the subcell which lies above cutoff.

The main output from INDESTis the grade above a cutoff of zero, ie the indicator estimated grade of the total subcell.

### Estimation Parameter File

In order to useINDESTyou must specify one record in the Estimation Parameter File &**ESTPARM** for each cutoff. This requires the numeric field **CUTOFF** to be included in the file.

The * **VALUE_IN** field is the grade in the input sample &**IN** file to which the cutoffs are applied. Note that this is different from the use of the * **VALUE_IN** field when using ESTIMATE for Indicator Estimation.

If the * **VALUE_OU** field is not specified then the * **VALUE_IN** field will be created in the output model file to hold the indicator estimated grade. If a * **VALUE_OU** field is specified in the first record of the Estimation Parameter File, then this value will be used for the indicator estimated grade in the output model file

You can only estimate one set of indicators in a single run. In other words all the **VALUE_IN** fields must be the same. Also when using **INDEST** you cannot estimate a grade using non indicator methods in the same run.

If you are using zone control then you must explicitly specify all combinations of zone field(s) in the Estimation Parameter File. You cannot use the option that is available in ESTIMA that allows you to specify an absent data zone field value that then applies to all zones that are not explicitly identified in&ESTPARM.

If you are using zone control then you may use different cutoffs for different zones. However the PRABn and GRABn fields in the output model file must then be handled very carefully! The maximum number of cutoff values is 24.

Fields for indicator estimation:

  * **BINGRADE** : Used when **GRMETHOD** =4 to set the grade below the cutoff

  * **ABVGRADE** : Sets the grade above the cutoff (only used for the top bin)

### Grade Above Cutoff

The calculation of the grade above each cutoff requires that the average grade between each successive pair of cutoffs be specified. For example if cutoff grades of 2, 5, 6.5 and 9.5g/t are selected then average grades are required for the ranges:

From  |  To  
---|---  
0 |  2  
2 |  5  
5 |  6.5  
6.5 |  9.5  
9.5 |  ∞  
  
Four methods are available to specify the average grade for each range, controlled by parameter @**GRMETHOD** :

GRMETHOD  |  Description  
---|---  
1 |  Average of minimum and maximum cutoff values. The grade above the highest cutoff is calculated as the highest cutoff plus half the difference between the highest and second highest cutoffs.  
2 |  Calculated by INDEST from the grades of the samples in the &**IN** file.  
3 |  Calculated by INDEST from the grades of the samples in the &**IN** file. However for the top bin (above the highest cutoff) the median grade is calculated.  
4 |  Values are specified by the user, using the **BINGRADE** and **ABVGRADE** fields in the &**ESTPARM** file. The **BINGRADE** field contains the grade below the cutoff and the **ABVGRADE** field the grade above the cutoff. The ABVGRADE field is therefore only used for the top bin.  
  
**GRMETHOD** of 4 is illustrated in the following table:

CUTOFF  | BINGRADE |  ABVGRADE   
---|---|---  
2 |  1.3 |  -  
5 |  3.6 |  -  
6.5 |  5.7 |   
9.5 |  7.8 |  11.1  
  
The values used by INDEST can be recorded by specifying an output &**AVGRADES** file.

### Indicators

Indicator values are calculated for each sample in the input sample &**IN** file for each cutoff. An indicator takes the value:

0 ‑ the grade is less than or equal to the cutoff.

1 ‑ the grade is above the cutoff.

The indicator values can be saved by specifying an output &**INDICATE** file.

###  Output Model 

Fields **PRAB1 ... PRAB** n will be created in the Output Model file to store the proportion of the subcell above each cutoff. These are calculated directly by ESTIMA. Then the fields **GRAB1 ... GRAB** n are calculated during the post-processing to store the corresponding grade above each cutoff. The grade above cutoff values (**GRABn**) are calculated from the proportion and average grade between each pair of cutoffs. For example:

Cutoff Number  |  Cutoff  |  PRABn  |  Calculation   
---|---|---|---  
4 |  9.5 |  0.1 |  GRAB4= 11.1 (This figure is taken directly from the ABVGRADE field)  
3 |  6.5 |  0.3 |  GRAB3= {0.1x11.1 + (0.3‑0.1)x7.8} / 0.3 = 8.9  
2 |  5 |  0.6 |  GRAB2= {0.1x11.1 + (0.3‑0.1)x7.8 + (0.6‑0.3)x5.7} / 0.6 = 7.3  
1 |  2 |  0.85 |  GRAB1= {0.1x11.1 + (0.3‑0.1)x7.8 + (0.6‑0.3)x5.7 + (0.85‑0.6)x3.6} / 0.85 = 6.21  
0 |  0 |  1 |  Indicator Grade=0.1x11.1 + (0.3‑0.1)x7.8 + (0.6‑0.3)x5.7 \+ (0.85‑0.6)x3.6 + (1.0‑0.85)x1.3 = 5.48  
  
The **PRABn** and **GRABn** fields will be stored in the output &**MODEL** file if parameter @PGFIELDS is set to 1.

### Order Relation

One of the main drawbacks of the indicator estimation method is the Order Relation Problem. This will occur if the proportion of the subcell above cutoff n is estimated to be less than the proportion above cutoff n+1. ie PRAB(n) < PRAB(n+1). Three options are available to correct for this, controlled by parameter ORDER:

=1: Downwards.  
=2: Upwards.  
=3: Average of methods 1 and 2.

The recommended method (and default) is 3.

### Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block_Model_File |  Input model prototype. This is a standard block model file containing the 13 compulsory fields. It may also contain the rotated model fields. If it includes cells then it must be sorted on IJK.  
IN |  Input |  Yes |  Undefined |  Input sample data. This must contain X,Y and Z fields and at least one grade field.  
SRCPARM |  Input |  Yes |  Undefined |  Search volume parameter file.  This contains 24 compulsory fields defining the search volume and the number of samples needed for grade estimation. More than one search volume may be defined. All fields are numeric:

  * SREFNUM: Search volume reference number.
  * SMETHOD: Search volume shape.
  *     * 1 = 3D rectangle
    * 2 = ellipsoid.
  * SDIST1: Max search distance in direction 1.
  * SDIST2: Max search distance in direction 2.
  * SDIST3: Max search distance in direction 3.
  * SANGLE1: First rotation angle for search vol.
  * SANGLE2: Second rotation angle.
  * SANGLE3: Third rotation angle.
  * SAXIS1: Axis for 1st rotation (1=X,2=Y,3=Z).
  * SAXIS2: Axis for 2nd rotation (1=X,2=Y,3=Z).
  * SAXIS3: Axis for 3rd rotation (1=X,2=Y,3=Z).
  * MINNUM1: Min number of samples, 1st search vol.
  * MAXNUM1: Max number of samples, 1st search vol.
  * SVOLFAC2: Axis multiplying factor,2nd search vol.
  * MINNUM2: Min number of samples, 2nd search vol.
  * MAXNUM2: Max number of samples, 2nd search vol.
  * SVOLFAC3: Axis multiplying factor,3rd search vol.
  * MINNUM3: Min number of samples, 3rd search vol.
  * MAXNUM3: Max number of samples, 3rd search vol.
  * OCTMETH: Octant method flag.
    * 0=no octant search
    * 1=use octants
  * MINOCT: Minimum number of octants to be filled.
  * MINPEROC: Minimum number of samples in an octant.
  * MAXPEROC: Maximum number of samples in an octant.
  * MAXKEY: Maximum number of samples with the same key value within an octant.

  
ESTPARM |  Input |  Yes |  Undefined |  Estimation parameter file. Each record in the file describes an estimation method and its associated parameters. The fields are dependent on the estimation methods selected. All fields are optional except for **VALUE_IN** , **SREFNUM** and **CUTOFF**. General fields:

  * VALUE_IN: Grade field to be estimated.
  * SREFNUM: Search volume reference number.
  * CUTOFF: Cutoff grade for indicator calculation.
  * VALUE_OU: Output indicator estimated grade field to be created in **MODEL** (Default is **VALUE_IN**). The required field name must be specified in the first record of the Estimation Parameter file. Values in subsequent records will be ignored.
  * {ZONE1_F}: A/N 1st field for zonal estimation. The actual name of the field is given by the **ZONE1_F** field. e.g. **ZONE1_F**(**ROCK**).
  * {ZONE2_F}: A/N 2nd field for zonal estimation.
  * NUMSAM_F: Field to be created in MODEL for the number of samples.
  * SVOL_F: Field to be created in MODEL for dynamic search volume number.
  * VAR_F: Field to be created in MODEL for variance of estimate.
  * MINDIS_F: Field to be created in MODEL for distance to nearest sample.
  * IMETHOD: Estimation method.
    1. Nearest neighbour (NN)
    2. Inverse power of distance (IPD)
    3. Ordinary Kriging (OK)
    4. Simple Kriging (SK)
    5. Sichel's T Estimator

**Fields for IPD:**

  * ANISO: Anisotropy method:
    1. No anisotropy
    2. Use search volume anisotropy
    3. Use ANANGLEn
  * ANANGLE1: N Anisotropy angle 1.
  * ANANGLE2: N Anisotropy angle 2.
  * ANANGLE3:N Anisotropy angle 3.
  * ANDIST1: N Anisotropy distance 1.
  * ANDIST2: N Anisotropy distance 2.
  * ANDIST3: N Anisotropy distance 3.
  * POWER: N Power of distance for weighting.
  * ADDCON: N Constant added to distance.

Fields for kriging:

  * VREFNUM: Variogram model reference number.
  * LOG: N Lognormal variogram flag. 0 = normal kriging. 1 = lognormal kriging.
  * KRIGNEGW: N Treatment of -ve weights: 0 = -ve weights kept and used. 1 = ignore samples with -ve weights
  * KRIGVARS: N Treatment of variance > sill: 0 = write variance to MODEL. 1 = set variance to sill. Fields for lognormal kriging:
  * GENCASE: N Calculation method: 0 = Rendu's method. 1 = General case.
  * DEPMEAN: N Deposit mean [If 0 then use kriged estimate]. Fields for general case:
  * TOL: N Tolerance for convergence.
  * **MAXITER** : N Maximum number of iterations. Fields for simple kriging:
  * **LOCALMNP** : N Method for calculation of local mean: 1 = use field defined in PROTO 2 = use mean within search vol.
  * LOCALM_F: Name of local mean field in PROTO; used if LOCALMNP=1

Fields for indicator estimation

  * **BINGRADE** : Used when **GRMETHOD** =4 to set the grade below the cutoff

  * **ABVGRADE** : Sets the grade above the cutoff (only used for the top bin)

  
VMODPARM |  Input |  No |  Variogram \- Model |  Variogram model parameter file.  Each record in this file defines a variogram model type and its parameters. Only the VREFNUM field is compulsory.

  * VREFNUM: Model variogram reference number.
  * VANGLE1: Variogram anisotropy angle 1.
  * VANGLE2: Variogram anisotropy angle 2.
  * VANGLE3: Variogram anisotropy angle 3.
  * VAXIS1: Model variogram rotation axis 1.
  * VAXIS2: Model variogram rotation axis 2.
  * VAXIS3: Model variogram rotation axis 3.
  * NUGGET: Nugget variance.
  * ST1: Variogram model type for structure 1.
    1. Spherical
    2. Power
    3. Exponential
    4. Gaussian
    5. De Wijsian
  * ST1PAR1: 1st parameter of structure 1 [Range 1 for spherical model].
  * ST1PAR2: 2nd parameter of structure 1 [Range 2 for spherical model].
  * ST1PAR3: 3rd parameter of structure 1 [Range 3 for spherical model].
  * ST1PAR4: 4th parameter of structure 1 [C variance for spherical model].
  * STn: Variogram model type for structure n. STnPARp pth parameter for structure n, where n<=9.

  
  
### Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  No |  Block Model File |  Output model containing estimated grades, variance etc.  
AVGRADES |  Output |  No |  Undefined |  Output file containing cutoff grade ranges and average grade used for each range. It will include zone field(s), if any, plus the following fields: 

  * **BIN** : bin or grade range number 
  * **LO_CUT** : lower cutoff grade 
  * **UP_CUT** : upper cutoff grade 
  * **NSAMPLES** : number of samples in IN file lying within the bin 
  * **BINGRADE** : bin grade used for indicator kriging. This is dependent on the **GRMETHOD** parameter . 
  * **SAMPMEAN** : mean grade of samples in IN file lying within the bin 

  
INDICATE |  Output |  No |  Undefined |  Output indicator file. This is a copy of the sample input IN file, but also includes the 0/1 indicator values for each cutoff  
SAMPOUT |  Output |  No |  Undefined |  Output sample file containing details of weights for each sample for each cell estimated.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate of sample data in IN file. If not specified, then X is assumed. |  IN |  No |  Numeric |  Undefined  
Y |  Y coordinate of sample data in IN file. If not specified, then Y is assumed. |  IN |  No |  Numeric |  Undefined  
Z |  Z coordinate of sample data in IN file. If not specified, then Z is assumed. |  IN |  No |  Numeric |  Undefined  
ZONE1_F |  First field for zonal control. |  IN |  No |  Any |  Undefined  
ZONE2_F |  Second field for zonal control. |  IN |  No |  Any |  Undefined  
KEY |  Key field used to specify the field limiting the number of samples for estimation. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
LENGTH_F |  Field used for length weighting in IPD. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
DENS_F |  Field used for density weighting in IPD. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description | Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DISCMETH |  Cell discretisation method:

  1. Use **XPOINTS** , **YPOINTS** , **ZPOINTS** to define the number of points in the X,Y,Z directions.
  2. Use **XDSPACE** , **YDSPACE** , **ZDSPACE** to define the distance between points. The default is method (1).

|  No |  1 | 1,2 |  1,2  
XPOINTS |  Number of discretisation points in X. (1) |  No |  1 | Undefined | Undefined  
YPOINTS |  Number of discretisation points in Y. (1) |  No |  1 | Undefined | Undefined  
ZPOINTS |  Number of discretisation points in Z. (1) |  No |  1 | Undefined | Undefined  
XDSPACE |  Distance between discretisation points in X if DISCMETH=2. The default gives just one point. |  No | Undefined | Undefined | Undefined  
YDSPACE |  Distance between discretisation points in Y if DISCMETH=2. The default gives just one point. |  No | Undefined | Undefined | Undefined  
ZDSPACE |  Distance between discretisation points in Z if DISCMETH=2. The default gives just one point. |  No | Undefined | Undefined | Undefined  
PARENT |  Flag to control parent cell estimation:

  * 0=Estimate into individual subcells. Default setting
  * 1= Represent parent cell by a full 3D matrix of points.
  * 2=Represent parent cell by a 3D matrix of points, but select only points lying within subcells. 

|  No |  0 |  0,2 |  0,1,2  
MINDISC |  Minimum number of discretisation points. Only used if PARENT=2. The default is (1). |  No |  1 | Undefined | Undefined  
COPYVAL |  Flag controlling copying of values from PROTO to MODEL if there is insufficient data to estimate them:

  * 0=Assign absent data value[s] in MODEL. Default setting.
  * 1=Copy from PROTO to MODEL. 

|  No |  0 |  0,1 |  0,1  
FVALTYPE |  Flag for cell size approximation for F values:

  1. The exact dimensions of the cell are used. Default setting.
  2. Each cell is approximated by one of a discrete number of cell sizes. 

|  No |  1 |  1,2 |  1,2  
FSTEP |  Step size for cell approximation. This is only used if **FVALTYPE** =2. |  No | Undefined | Undefined | Undefined  
XMIN |  Minimum X value for model updating. The default is the X model origin. |  No | Undefined | Undefined | Undefined  
XMAX |  Maximum X value for model updating. The default is the maximum X value for **PROTO**. |  No | Undefined | Undefined | Undefined  
YMIN |  Minimum Y value for model updating. The default is the Y model origin. |  No | Undefined | Undefined | Undefined  
YMAX |  Maximum Y value for model updating. The default is the maximum Y value for **PROTO**. |  No | Undefined | Undefined | Undefined  
ZMIN |  Minimum Z value for model updating. The default is the Z model origin. |  No | Undefined | Undefined | Undefined  
ZMAX |  Maximum Z value for model updating. The default is the maximum Z value for **PROTO**. |  No | Undefined | Undefined | Undefined  
XSUBCELL |  Number of subcells per parent cell in X if **PROTO** is empty. The default is (1). |  No |  1 |  Undefined |  Undefined  
YSUBCELL |  Number of subcells per parent cell in Y if **PROTO** is empty. The default is (1). |  No |  1 |  Undefined |  Undefined  
ZSUBCELL |  Number of subcells per parent cell in Z if **PROTO** is empty. The default is (1). |  No |  1 |  Undefined |  Undefined  
ORDER |  Order relation correction method:

  1. Downwards.
  2. Upwards.
  3. Average of methods 1 and 2.

|  No |  3 |  1,3 |  1,2,3  
GRMETHOD |  Method for specifying average grade within each cutoff range:

  1. Average of minimum and maximum cutoff values.
  2. Average calculated from samples in **IN** file. Mean grade for top bin.
  3. Average calculated from samples in **IN** file. Median grade for top bin.
  4. Specify values using **BINGRADE** and **ABVGRADE** fields in **ESTPARM** file.

|  No |  3 |  1,4 |  1,2,3,4  
PGFIELDS |  Flag to select whether the proportion above cutoff fields (PRABn) and the grade above cutoff fields (GRABn) should be included in the output MODEL file:

  * 0=Do not include the **PRABn** and **GRABn** fields.
  * 1=Include the **PRABn** and **GRABn** fields.

|  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !INDEST   
  
---  
      
    
     &PROTO(modelb1),&IN(sampleb1),&SRCPARM(spar4),&ESTPARM(eparind),        &VMODPARM(vmodelb),&MODEL(modelind),&AVGRADES(gradeind),  
      
    
            &INDICATE(indind),*X(XPT),*Y(YPT),*Z(ZPT),*ZONE1_F(ROCK),  
      
    
            @DISCMETH=1.0,@XPOINTS=3.0,@YPOINTS=3.0,@ZPOINTS=3.0,  
      
    
            @PARENT=0.0,@COPYVAL=0.0,@FVALTYPE=1.0,@ORDER=3.0,  
      
    
            @GRMETHOD=3.0,@PGFIELDS=0.0