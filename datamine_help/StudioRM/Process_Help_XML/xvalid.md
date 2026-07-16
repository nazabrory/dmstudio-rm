# XVALID Process  
  
To access this process:

  * **Estimate** ribbon **> > Variograms >> Validate**.

  * Enter "XVALID" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **XVALID** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_X.md#XVALID>).

##  Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

XVALID assists in the selection of parameters for grade estimation, using the cross-validation method.

The input data file is the sample data which will later be used for estimating grades into a block model. For kriging it allows different model variograms to be tested and compared. For inverse power of distance it allows different powers to be compared.

The input to **XVALID** is consistent with the input required for the grade estimation process [ESTIMA](<estima.md>). In fact the three input parameter files are identical for the two processes.

The cross-validation method works by removing each point in turn from the data file and estimating its value from the remaining data. In this way a table of actual and estimated values is created. A detailed statistical analysis is then carried out comparing the actuals and estimates. One or more of the estimation parameters can then be changed and the process rerun to see whether the new parameters improve the results of the statistical analysis. The method is therefore iterative, requiring several runs to establish the best set of parameters.

**XVALID** uses the block model grade estimation process [ESTIMA](<estima.md>) to do the actual interpolation. Therefore part of the text on the Output window is the same as for [ESTIMA](<estima.md>), and will refer to a block model rather than points. However the number of discretisation points is set to 1x1x1 so in effect point estimation is being used.

There are three input parameter files all of which can be set up using the [ESTIMATE](<estimate.md>) process or the Table Editor:

  * **SRCPARM** : Search Volume Parameter File

  * **ESTPARM** : Estimation Parameter File

  * **VMODPARM** : Variogram Model Parameter File

and two other input files:

  * **IN** : Sample File

  * **VGRAM** : Experimental Variogram File

The results of the cross-validation are written to three separate output files, all of which are optional:

  * **XVSAMPS** : cross-validated output sample file

  * **XVSTATS** : cross-validation statistics

  * **SAMPOUT** : sample output file containing weights for each estimate

The statistics are also displayed in the **Output** window as illustrated in the example. When the first set of results have been calculated and displayed you are then able to select from a menu which allows you to edit one or more of the parameter files or examine the results, and then rerun the cross-validation:

1 - edit search volume parameter file spar10

2 - edit estimation parameter file epar10

3 - edit variogram model parameter file vpar10

4 - examine variogram model interactively (**[VARFIT](<varfit.md>)**)

5 - examine cross-validation statistics file xxstats

6 - delete cross-validation statistics file xxstats

7 - create plot of actual v estimate

8 - re-run cross-validation

0 - exit cross-validation

Option 4 allows you to use the interactive variogram fitting process [VARFIT](<varfit.md>). In order to use this option you must have specified the experimental variogram file **VGRAM** when selecting **XVALID**.

Options 5 and 6 are only available if the output file **XVSTATS** has been specified.

Option 7 is not available if multiple fields are being cross-validated ie if there is more than one record in the estimation parameter file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample data to be cross validated. This must contain X,Y and Z fields and at least one grade field. |  Input |  Yes |  Undefined  
SRCPARM |  Search volume parameter file. This contains 24 compulsory fields defining the search volume and the number of samples needed for grade estimation. More than one search volume may be defined.  All fields are numeric: 

  * SREFNUM Search volume reference number. 
  * SMETHOD Search volume shape. 
    * 1 = 3D rectangle 
    * 2 = ellipsoid. 
  * SDIST1 Max search distance in direction 1. 
  * SDIST2 Max search distance in direction 2. 
  * SDIST3 Max search distance in direction 3. 
  * SANGLE1 First rotation angle for search vol. 
  * SANGLE2 Second rotation angle. 
  * SANGLE3 Third rotation angle. 
  * SAXIS1 Axis for 1st rotation (1=X,2=Y,3=Z). 
  * SAXIS2 Axis for 2nd rotation (1=X,2=Y,3=Z). 
  * SAXIS3 Axis for 3rd rotation (1=X,2=Y,3=Z). 
  * MINNUM1 Min number of samples, 1st search vol.
  * MAXNUM1 Max number of samples, 1st search vol. 
  * SVOLFAC2 Axis multiplying factor,2nd search vol. 
  * MINNUM2 Min number of samples, 2nd search vol. 
  * MAXNUM2 Max number of samples, 2nd search vol. 
  * SVOLFAC3 Axis multiplying factor,3rd search vol. 
  * MINNUM3 Min number of samples, 3rd search vol. 
  * MAXNUM3 Max number of samples, 3rd search vol. 
  * OCTMETH Octant method flag. 
    * 0 = no octant search, 
    * 1 = use octants. 
  * MINOCT Minimum number of octants to be filled. 
  * MINPEROC Minimum number of samples in an octant. 
  * MAXPEROC Maximum number of samples in an octant. 
  * MAXKEY Maximum number of samples with the same key value within an octant.

|  Input |  Yes |  Undefined  
ESTPARM |  Estimation parameter file. Each record in the file describes an estimation method and its associated parameters. The fields are dependent on the estimation methods selected.  General fields: 

  * VALUE_IN: Field to be estimated.
  * SREFNUM: Search volume reference number. 
  * VALUE_OU: Field to be created in MODEL (Default is VALUE_IN). 
  * {ZONE1_F}: 1st field for zonal estimation. The actual name of the field is given by ZONE1_F on command line e.g. ZONE1_F(ROCK).
  * {ZONE2_F}: 2nd field for zonal estimation.
  * NUMSAM_F: Field to be created in MODEL for the number of samples. 
  * SVOL_F: Field to be created in MODEL for dynamic search volume number. 
  * VAR_F: Field to be created in MODEL for variance of estimate. 
  * MINDIS_F: Field to be created in MODEL for distance to nearest sample. IMETHOD N Estimation method. 
    * 1 = Nearest neighbour (NN). 
    * 2 = Inverse power of dist (IPD). 
    * 3 = Ordinary kriging (OK). 
    * 4 = Simple kriging (SK). 
    * 5 = Sichel's t estimator. Anisotropy fields for NN and IPD: 
  * ANISO: Anisotropy method:
    * 0 = no anisotropy. 
    * 1 = use search vol anisotropy. 
    * 2 = use ANANGLEn. 
  * ANANGLE1: Anisotropy angle 1. 
  * ANANGLE2: Anisotropy angle 2. 
  * ANANGLE3: Anisotropy angle 3. 
  * ANDIST1: Anisotropy distance 1. 
  * ANDIST2: Anisotropy distance 2. 
  * ANDIST3: Anisotropy distance 3.

Fields for IPD: 

  * POWER Power of distance for weighting. 
  * ADDCON Constant added to distance. Fields for kriging: 
  * VREFNUM: Variogram model reference number.
  * LOG: Lognormal variogram flag. 
    * 0 = normal kriging. 
    * 1 = lognormal kriging. 
  * KRIGNEGW: Treatment of -ve weights: 
    * 0 = -ve weights kept and used. 
    * 1 = ignore samples with -ve weights 
  * KRIGVARS Treatment of variance > sill: 
    * 0 = write variance to MODEL. 
    * 1 = set variance to sill. Fields for lognormal kriging: 
  * **GENCASE** Calculation method: 
    * 0 = Rendu's method. 
    * 1 = General case. 
  * DEPMEAN Deposit mean [If 0 then use kriged estimate]. 

Fields for general case: 

  * **TOL** N Tolerance for convergence.
  * **MAXITER** N Maximum number of iterations. 

Fields for simple kriging: 

  * LOCALMNP: Method for calculation of local mean: 
    * 1 = use field defined in PROTO
    * 2 = use mean within search vol.
  * LOCALM_F: Name of local mean field in **PROTO** ; used if **LOCALMNP** =1

|  Input |  Yes |  Undefined  
VMODPARM |  Variogram model parameter file. Each record in this file defines a variogram model type and its parameters. Only the VREFNUM field is compulsory. 

  * VREFNUM Model variogram reference number. 
  * VANGLE1 Variogram anisotropy angle 1. 
  * VANGLE2 Variogram anisotropy angle 2. 
  * VANGLE3 Variogram anisotropy angle 3.
  * VAXIS1 Model variogram rotation axis 1. 
  * VAXIS2 Model variogram rotation axis 2. 
  * VAXIS3 Model variogram rotation axis 3. 
  * NUGGET Nugget variance. 
  * ST1 Variogram model type for structure 1. 
    * 1 = Spherical. 
    * 2 = Power [eg 1 - linear]. 
    * 3 = Exponential. 
    * 4 = Gaussian. 
    * 5 = De Wijsian. 
  * ST1PAR1 1st parameter of structure 1 [Range 1 for spherical model]. 
  * ST1PAR2 2nd parameter of structure 1 [Range 2 for spherical model]. 
  * ST1PAR3 3rd parameter of structure 1 [Range 3 for spherical model]. 
  * ST1PAR4 4th parameter of structure 1 [C variance for spherical model]. 
  * STn Variogram model type for structure n. 
  * STnPARp pth parameter for structure n, where n<=9.

|  Input |  No |  Variogram - Model  
VGRAM |  Experimental variogram file, as created by the variogram calculation process [VGRAM](<vgram.md>).  This experimental variogram file will have been used by the variogram fitting process [VARFIT](<varfit.md>) in order to derive the variogram model defined by **VMODPARM** .  This is only required if you want to use access the variogram display and fitting process **VARFIT** from within **XVALID**. |  Input |  No |  Variogram - Experimental  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
XVSAMPS |  Output |  No |  Undefined |  Cross-validated output sample file. This contains all the fields from the IN sample data file, plus each grade estimate and associated secondary fields such as kriged variance.  
XVSTATS |  Output |  No |  Undefined |  Output file containing a summary of the input parameters and the cross-validation statistics.  It includes a single record for each estimate. The 23 fields in the file are summarised below.  If the file already contains all 23 fields then additional records are appended to the file. If the file does not contain all 23 fields, or if the file does not exist, then a new file is created. 

  * ID \- each estimate is assigned a unique numeric identifier
  * VALUE_IN \- field in sample IN file being estimated
  * VALUE_OU \- field containing estimated value 
  * IMETHOD \- estimation method (1=NN, 2=IPD, 3=OK, 4= SK, 5=ST) 
  * SREFNUM \- search volume reference number 
  * VREFNUM \- variogram reference number 
  * POWER \- power of distance for IPD 
  * NUM_EST \- number of samples for which estimates have been made 
  * NUM_MISS \- number of samples whose values were not estimated 
  * ACT_MEAN \- mean grade of the sample values (the actuals) 
  * EST_MEAN \- mean grade of the estimated values 
  * **DIFF** \- actual mean grade minus estimated mean grade 
  * PC_DIFF \- DIFF as a percentage of the actual mean grade 
  * MAD \- mean absolute difference between actual and estimated grades 
  * ACT_VAR \- variance of the actual grades 
  * EST_VAR \- variance of the estimated grades 
  * COR_COEF \- correlation coefficient between actuals and estimates 
  * KV_VMOD \- mean of the kriged variance of each estimate 
  * KV_DIFF2 \- mean of (Actual - Estimate)**2 
  * KV_RATIO \- ratio of KV_VMOD to KV_DIFF2 
  * REG_CON \- constant of regression line of actual on estimate 
  * REG_SLP \- slope of regression line of actual on estimate 
  * REG_SE \- standard error of regression line of actual on estimate

  
SAMPOUT |  Output |  No |  Undefined |  Output sample file containing details of weights for each sample for each estimate.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate of sample data in **IN** file. If not specified, then X is assumed. |  IN |  Yes |  Numeric |  Undefined  
Y |  Y coordinate of sample data in **IN** file. If not specified, then Y is assumed. |  IN |  Yes |  Numeric |  Undefined  
Z |  Z coordinate of sample data in **IN** file. If not specified, then Z is assumed. |  IN |  Yes |  Numeric |  Undefined  
ZONE1_F |  First field for zonal control. The field must exist in the **IN** file and in the **ESTPARM** file. |  IN, ESTPARM |  No |  Any |  Undefined  
ZONE2_F |  Second field for zonal control. The field must exist in the IN file and in the **ESTPARM** file. |  IN, ESTPARM |  No |  Any |  Undefined  
KEY |  Key field used to specify the field limiting the number of samples for estimation. The field must exist in the **IN** file. |  IN |  No |  Numeric |  Undefined  
LENGTH_F |  Field used for length weighting in **IPD**. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
DENS_F |  Field used for density weighting in **IPD**. The field must exist in the **IN** file. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SMINFAC |  Multiplying factor which is applied to the first search volume, and used to calculate the exclusion volume for estimation. Samples lying within the exclusion volume are not used for the estimation. The factor must be greater than 0 and less than 1. The exclusion volume is concentric with the search volume. |  No |  0.0001 |  0,1 |  Undefined  
PRINT |  Display control: |  Option |  Description  
---|---  
0 |  Minimum output.  
1 |  Maximum output.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !XVALID  &IN(holes.d), &SRCPARM(spar10), &ESTPARM(epar10),   
  
---  
      
    
     &VMODPARM(vpar10), &VGRAM(vgram),&XVSAMPS(xvsamps),  
      
    
     &XVSTATS(xvstats),&SAMPOUT(sampout),@SMINFAC=0.00001,@PRINT=0,@ECHO=0  
  
Related topics and activities

  * [ESTIMA Process](<estima.md>)

  * [ESTIMATE Process](<estimate.md>)

  * [VARFIT Process](<varfit.md>)