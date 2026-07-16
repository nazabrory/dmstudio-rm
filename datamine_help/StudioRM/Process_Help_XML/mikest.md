# MIKEST Process  
  
To access this process:

  * Estimate ribbon | Estimate >> Indicator

  * Enter "MIKEST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MIKEST** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MIKEST>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

The MIKEST process uses the Indicator Estimation (IE) method to estimate grades into a block model using the cumulative distribution function (CDF) of indicator transformed sample grades. It is similar to the [INDEST](<indest.md>) process except it is based on the Advanced Estimation [COKRIG](<cokrig.md>) process rather than the [ESTIMA](<estima.md>) process. The main advantage of MIKEST over INDEST is processing speed.

To operate, MIKEST needs a series of threshold values between the smallest and largest grade values. These threshold values, referred to as cutoffs, are used to numerically build the CDF of each block in the model. 

For each cutoff, data in the search volume are transformed into zeroes and ones: 1 is assigned if the data are greater than the threshold and 0 if less than or equal to the threshold. MIKEST then estimates the probability that the block grade is greater than the threshold value, using Ordinary Kriging.

Performing this operation for each cutoff across the range of the sample data approximates the CDF for the model cell. After the CDF is built, it is post-processed to calculate the indicator-estimated grade.

MIKEST uses the [COKRIG](<cokrig.md>) process to perform the estimation for each cutoff. 

You must already have calculated a variogram for each cutoff and stored the models in the [Variogram Model file](<../COMMON/filetype.md#VariogramMod>). The [VGRAM](<vgram.md>) process has specific features for calculating indicator variograms.

For each cutoff MIKEST calculates the following data which can optionally be stored in the Output Model file:

  * PRABi: the proportion (fraction) of the model subcell which is above cutoff number i
  * GRABi: the grade of the proportion of the subcell which lies above cutoff.

The main output from MIKEST is the grade above a cutoff of zero, i.e. the indicator-estimated grade of the total subcell.

## Estimation and Fields Parameter Files

In order to use MIKEST, you must specify one record in the [Estimation Parameter File](<../COMMON/filetype.md#Estimation>)EPAR and the Fields File FIELDS for each cutoff. This requires the numeric field *CUTOFF to be included in the file.

The * IN_VAR field in the Fields File is the grade in the input sample &IN file to which the cutoffs are applied. 

The *EST field in the first record of the Fields File contains the name of the field for the MIK estimate in the output &OUTMODEL file. If the *EST field in the Fields File is not specified then the * IN_VAR field will be created in the output model file to hold the indicator estimated grade. If a *EST field is specified in the first record of the Fields File File, then this value will be used for the indicator estimated grade in the output model file

You can only estimate one set of indicators in a single run. In other words all the IN_VAR values must be the same. Also when using MIKEST you cannot estimate a grade using non indicator methods in the same run.

Zone control for indicator estimation can be applied by defining either a single zone field (*ZONE1_F) or two zone fields (*ZONE1_F and *ZONE2_F). The defined zone field(s) must exist in the PROTO, SAMPLES and EPAR files.

If you are using zone control then the EPAR and FIELDS files must include a record for every combination of zone values. If a single zone field has been defined using *ZONE1_F() then EPAR must include a field named ZONE1. The field type (alpha or numeric) must be the same as the field defined by *ZONE1_F(). The values of ZONE1 are the same as the values of *ZONE1_F(). A second zone field ZONE2 can be added to EPAR as for ZONE1. The fields defined by *ZONE1_F() and *ZONE2_F() must be included in the &PROTO and &SAMPLES files.The FIELDS file does not have to include the *ZONEi_F field(s) as the EPAR and FIELDS files are linked automatically by the EREFNUM field.

If you are using zone control then you must define the same number of cutoffs for all zone combination. However the actual cutoff values may differ from one zone combination to another. PRABn and GRABn fields in the output model file must then be handled carefully as they are identified by their cutoff number (n = 1, 2, 3, .) not by their cutoff value. The maximum number of cutoff values is 24 per zone.

Fields for indicator estimation:

  * **BINGRADE** : Used when **GRMETHOD** =4 to set the grade below the cutoff

  * **ABVGRADE** : Sets the grade above the cutoff (only used for the top bin)

## Variogram Model Parameter File

The variogram models are required to enable the PRoportion ABove Cutoff i (PRABi) values to be estimated using the Ordinary Kriging or Simple Kriging methods. There are 15 compulsory fields in the variogram model parameter file. A record (model) is required for each combination of cutoff and zone field and also each zone must have the same number of cutoffs. Therefore if there are 11 cutoffs and 3 values for zone field 1 (*ZONE1_F) then there will be 33 records. 

Fields include:

  * VSETNUM: the variogram model identifier number. This field is used by the Estimation Parameter file to link to the corresponding variogram model.
  * GRADE: the variable for which the variogram model has been fitted. This has been calculated from the PRoportion ABove cutoff (PRABi) field. The field for the first cutoff must be named PRAB1, the second PRAB2 and so on for each zone.
  * GRADE2: this must always be set to the same as GRADE
  * The other 12 compulsory fields are the standard variogram model parameters: VANGLEi, VAXISi, NUGGET, ST1, ST1PARj where i=1,3 and j=1,4

## Grade Above Cutoff

The calculation of the grade above each cutoff requires that the average grade between each successive pair of cutoffs be specified. For example if cutoff grades of 2, 5, 6.5 and 9.5g/t are selected then average grades are required for the ranges:

From | To  
---|---  
0 | 2  
2 | 5  
5 | 6.5  
6.5 | 9.5  
9.5 | > 9.5  
  
Four methods are available to specify the average grade for each range, controlled by parameter @GRMETHOD:

GRMETHOD | Description  
---|---  
1 |  Average of minimum and maximum cutoff values. The grade above the highest cutoff is calculated as the highest cutoff plus half the difference between the highest and second highest cutoffs.  
2 | Calculated by MIKEST from the grades of the samples in the &SAMPLES file.  
3 | Calculated by MIKEST from the grades of the samples in the &SAMPLES file. However for the top bin (above the highest cutoff) the median grade is calculated.  
4 | Values are specified by the user, using the BINGRADE and ABVGRADE fields in the &EPAR file. The BINGRADE field contains the grade below the cutoff and the ABVGRADE field the grade above the cutoff. The ABVGRADE field is therefore only used for the top bin.  
  
GRMETHOD 4 is illustrated in the following table:

CUTOFF | BINGRADE | ABVGRADE  
---|---|---  
2 | 1.3 | -  
5 | 3.6 | -  
6.5 | 5.7 | -  
9.5 | 7.8 | 11.1  
  
The values used by MIKEST can be recorded by specifying an output &AVGRADES file.

## Indicators 

Indicator values are calculated for each sample in the input sample &IN file for each cutoff. An indicator takes the value:

  * 0 the grade is less than or equal to the cutoff.

  * 1 the grade is above the cutoff.

The indicator values can be saved by specifying an output &INDICATE file.

## Output Model 

Fields PRAB1 ... PRABn will be created in the Output Model file to store the proportion of the subcell above each cutoff. These are calculated directly by COKRIG. Then the fields GRAB1 ... GRABn are calculated during the post-processing to store the corresponding grade above each cutoff. The grade above cutoff values (GRABn) are calculated from the proportion and average grade between each pair of cutoffs. For example:

Cutoff Number | Cutoff | PRABn | Calculation  
---|---|---|---  
4 | 9.5 | 0.1 | GRAB4= 11.1 (This figure is taken directly from the ABVGRADE field)  
3 | 6.5 | 0.3 | GRAB3= {0.1x11.1 + (0.3 - 0.1) x7.8} / 0.3 = 8.9  
2 | 5 | 0.6 | GRAB2= {0.1x11.1 + (0.3 - 0.1) x7.8 + (0.6 - 0.3) x 5.7} / 0.6 = 7.3  
1 | 2 | 0.85 | GRAB1= {0.1x11.1 + (0.3 - 0.1) x7.8 + (0.6 - 0.3) x 5.7 + (0.85 \- 0.6)x3.6} / 0.85 = 6.21  
0 | 0 | 1 | Indicator Grade=0.1x11.1 + (0.3 - 0.1) x 7.8 + (0.6 - 0.3) x5.7 + (0.85 - 0.6) x 3.6 + (1.0 - 0.85) x 0.13 = 5.30  
  
The PRABn and GRABn fields will be stored in the output &MODEL file if parameter @PGFIELDS is set to 1.

## Order Relation

One of the main drawbacks of the indicator estimation method is the Order Relation Problem. This will occur if the proportion of the subcell above cutoff n is estimated to be less than the proportion above cutoff n+1. ie PRAB(n) < PRAB(n+1). Three options are available to correct for this, controlled by parameter ORDER:

  * =1: Downwards.

  * =2: Upwards.

  * =3: Average of methods 1 and 2.

The recommended method (and default) is 3. It is also recommended that the same search volume is used for all cutoffs as this reduces the potential for order relation problems.

## Dynamic Anisotropy

The Dynamic Anisotropy option allows the anisotropy rotation angles for defining the search volume and variogram models to be defined individually for each cell in the block model. Thus, the search volume and variogram model can be oriented precisely to follow the trend of the mineralization. 

The three rotation angles of the search volume must be stored in the &PROTO model file and are referenced using the symbolic fields *SANGL1_F, *SANGL2_F and *SANGL3_F. Either two fields (1 and 2) or all three angle fields can be used. Usually only two fields are selected, corresponding to dip direction and dip. The rotation axes corresponding to the three angles are defined using parameters @DA_AXIS1, @DA_AXIS2 and @DA_AXIS3. Their default values are 3 (Z), 1 (X) and 3 (Z). In addition to defining the rotation angles and axes the field SDYNAISO in the &EPAR Estimation parameter file must be set to 1 for all cutoffs in order to activate dynamic anisotropy for search volumes.

The three rotation angles of the variogram model are also stored in the &PROTO model file and are referenced using the symbolic fields *VANGL1_F, *VANGL2_F and *VANGL3_F. The *VANGLi_F fields can be, and often are, the same as the *SANGLi_F fields. The &EPAR file must also include field VDYNAISO set to 1 to use dynamic anisotropy for variograms models. Dynamic anisotropy can be set for search volumes or variogram models or both. It is usual practice that only the first two of the SANGLi_F and VANGLi_F sets of angles are specified. Also it is usual that the same two angle fields are used for both sets. In this case the third angle does not need to be specified and will be assumed to be zero. In all other cases the same field is not permitted in both the SANGLi_F and VANGLi_F sets. 

## Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block_Model_File |  Input model prototype This is a standard block model file containing the 13 compulsory fields. It may also contain the rotated model fields. If it includes cells then it must be sorted on IJK.  
SAMPLES |  Input |  Yes |  Undefined |  Input sample data This must contain X,Y and Z fields and at least one grade field.  
SPAR | Input | Yes |  Undefined |  Search volume parameter file The file contains 13 required fields as described below. For optional fields refer to the COKRIG online Help . Required Fields:

  * SREFNUM: Search volume reference number.
  * SMETHOD: Search volume shape.
    * 1 = 3D rectangle
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

  
EPAR |  Input |  Yes |  Undefined |  Estimation parameter file. Each record in the file describes an estimation method and its associated numeric parameters. There are 9 required fields as described below. 

  * EREFNUM: Estimation reference number
  * CUTOFF: Cutoff grade for indicator calculation.
  * IMETHOD: Estimation method. This must be set to 3 for each record
    * **1** = Nearest neighbour (NN)
    * **2** = Inverse power of distance (ID)
    * 3 = Ordinary kriging (OK).
  * SREFNUM: Search volume reference number
  * VSETNUM: Variogram model set number. This must be different for each cutoff.
  * DISCX: Number of discetisation points in X
  * DISCY: Number of discetisation points in Y
  * DISCZ: Number of discetisation points in Z
  * PARENT: =0 for estimating into subcells. =1 for estimating parent cell

Optional Fields only used if @GRMETHOD=4

  * BINGRADE: This field contains the average grade in the bin below the cutoff.
  * ABVGRADE: This field contains the average grade in the bin above cutoff and is only used for the top bin.

For other optional fields refer to the EPAR section of the online help for COKRIG .  
FIELDS |  Input |  Yes |  Undefined |  Estimation Fields file.  This file is used to define field names associated with each EREFNUM defined in the EPAR file. There are two required fields as described below:

  * EREFNUM: Estimation reference number. The EREFNUM values must match the EREFNUMs in the EPAR file.
  * IN_VAR: The input grade field for which indicators are estimated. The value of this field must be the same in all records.

Optional Fields

  * EST: The name of the output MIK estimate field. This is only required for record 1 of the FIELDS file. If the EST field is not specified the value will be set to the value of the IN_VAR field.

Other optional fields such as NUMSAMP can be defined in the FIELDS file. These fields will then be recorded in the OUTMODEL file. For information on these additional fields refer to the FIELDS section of the COKRIG online help .  
VMODEL |  Input |  Yes |  Variogram - Model |  Variogram model parameter file. Each record in this file defines a variogram model type and its parameters. There are 13 required fields as described below. 

  * VSETNUM: Model variogram set number.
  * VANGLE1: Variogram anisotropy angle 1.
  * VANGLE2: Variogram anisotropy angle 2.
  * VANGLE3: Variogram anisotropy angle 3.
  * VAXIS1: Model variogram rotation axis 1.
  * VAXIS2: Model variogram rotation axis 2.
  * VAXIS3: Model variogram rotation axis 3.
  * NUGGET: Nugget variance.
  * ST1: Variogram model type for structure 1.
    * 1 = Spherical.
    * 2 = Not used.
    * 3 = Exponential.
    * 4 = Gaussian.
  * ST1PAR1: 1st parameter of structure 1 [Range 1 for spherical model].
  * ST1PAR2: 2nd parameter of structure 1 [Range 2 for spherical model].
  * ST1PAR3: 3rd parameter of structure 1 [Range 3 for spherical model].
  * ST1PAR4: 4th parameter of structure 1 [C variance for spherical model].

Optional fields:

  * STn: Variogram model type for structure n. 
  * STnPARp: pth parameter for structure n, where n<=9.

  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUTMODEL |  Output |  No |  Block Model File |  Output model containing estimated MIK grades, etc.  
AVGRADES |  Output |  No |  Undefined |  Output file containing cutoff grade ranges and average grade used for each range. It will include zone field(s), if any, plus the following fields: 

  * BIN: bin or grade range number
  * LO_CUT: lower cutoff grade. 
  * UP_CUT: upper cutoff grade.
  * NSAMPLES: number of samples in SAMPLES file lying within the bin. 
  * BINGRADE: bin grade used for indicator kriging. This is dependent on the GRMETHOD parameter. 
  * SAMPMEAN: mean grade of samples in SAMPLES file lying within the bin. 

  
INDICATE |  Output |  No |  Undefined |  Output indicator file. This is a copy of the sample input SAMPLES file, but also includes the 0/1 indicator values for each cutoff  
SAMPOUT |  Output |  No |  Undefined |  Output sample file containing details of weights for each sample for each cell estimated.  
  
## Fields

**Name** |  **Description** |  **Source** |  **Required** |  **Type** |  **Default**  
---|---|---|---|---|---  
XPT |  X coordinate of sample data in SAMPLES file. If not specified, then XPT is assumed. |  IN |  No |  Numeric |  Undefined  
YPT |  Y coordinate of sample data in SAMPLES file. If not specified, then YPT is assumed. |  IN |  No |  Numeric |  Undefined  
ZPT |  Z coordinate of sample data in SAMPLES file. If not specified, then ZPT is assumed. |  IN |  No |  Numeric |  Undefined  
ZONE1_F |  First field for zonal control. If a field is specified it must be present in both the SAMPLES and PROTO files. |  IN |  No |  Any |  Undefined  
ZONE2_F |  Second field for zonal control. If a field is specified it must be present in both the SAMPLES and PROTO files. |  IN |  No |  Any |  Undefined  
KEY |  Key field used to specify the field limiting the number of samples for estimation using the optional OPTKEY and MAXKEY parameters in the SPAR file. The field must exist in the SAMPLES file. |  SAMPLES |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ORDER |  Order relation correction method:

  1. Downwards.
  2. Upwards.
  3. Average of methods 1 and 2.

|  No |  3 |  1,3 |  1,2,3  
GRMETHOD |  Method for specifying average grade within each cutoff range:

  1. Average of minimum and maximum cutoff values.
  2. Average calculated from samples in SAMPLES file. Mean grade for top bin.
  3. Average calculated from samples in SAMPLES file. Median grade for top bin.
  4. Specify values using BINGRADE and ABVGRADE fields in EPAR file.

|  No |  3 |  1,4 |  1,2,3,4  
PGFIELDS |  Flag to select whether the proportion above cutoff fields (PRABn) and the grade above cutoff fields (GRABn) should be included in the OUTMODEL file:

  0. Do not include the PRABn and GRABn fields.
  1. Include the PRABn and GRABn fields.

|  No |  0 |  0,1 |  0,1  
DA_AXIS1/2/3 |  DA_AXIS1/2/3 Axis of first / second / third rotation angle used for both search volume and variogram model dynamic anisotropy. 1=X, 2=Y, 3=Z |  No |  3-1-3 |  1,3 |  1,2,3  
  
## Notes

The following notes are designed to assist when creating the parameter files:

### EPAR

  * The nine compulsory fields are EREFNUM, CUTOFF, IMETHOD, VSETNUM, SREFNUM, DISC[XYZ], PARENT.
  * Each record must have a different EREFNUM.
  * IMETHOD must be set to 2 for Inverse Power or Distance or 3 for Ordinary Kriging if Dynamic Anisotropy is selected.
  * Additional other fields: BINGRADE and ABVGRADE apply if @GRMETHOD=4. The BINGRADE field contains the grade below the cutoff and the ABVGRADE field the grade above the cutoff. The ABVGRADE field is therefore only used for the top bin.
  * VSETNUM must be different for each cutoff within a zone but can be the same for the same CUTOFF in different ZONEs.
  * There is no restriction on SREFNUMs. They can be shared or individual.
  * If zone control is used then cutoffs must be specified for each zone, if single zone, or for each combination of zones, if two zone control fields. There must be the same number of cutoffs for each zone/zone combination but the CUTOFF values can change between zone/zone combinations.
  * If zone control is used then zone fields (ZONE1, ZONE2 must be included in the EPAR file.
  * Optional fields SDYNAISO and VDYNAISO are used to select Search volume and Variogram model dynamic anisotropy options. 0=do not use option, 1=use option.

### FIELDS

  * The two compulsory fields are EREFNUM and IN_VAR
  * The EREFNUMs in FIELDS must match the EREFNUMs in EPAR.
  * The IN_VAR field is compulsory and specifies the grade field for which indicators are calculated. They must all be the same.
  * If specified the EST field defines the name of the output MIK estimate field. This is only required for the first record. If the EST field is not specified the output MIK estimate field name will be the same as the IN_VAR field.
  * The other secondary fields are optional. Each record defines a different combination of zone and cutoff. Therefore different names should be used for each cutoff within a zone but the same name for the same cutoff in a different zone.
  * If the same search volume is used for all cutoffs then fields NUMSAMP and SINDEX should only be specified once.
  * CUTOFF and ZONE fields can be included in the file to assist naming of secondary fields. They will be ignored by the process.

### SPAR

  * The 13 compulsory fields are SREFNUM, SMETHOD, SDIST[123], SANGLE[123], SAXIS[123], MINNUM1, MAXNUM1.
  * It is recommended that you use the same search volume for all indicators. One of the reasons for this is to reduce the effect of order relation problems. The effect is mitigated to some extent using the order relation parameter but its better to avoid the problem in the first place. Using the same search volume may help to reduce the run time. Nevertheless MIKEST does allow a different search volume for each cutoff in each zone.

### VMODEL

  * The 13 compulsory fields are VSETNUM, VANGLE[123], VAXIS[123], NUGGET, ST1, ST1PAR[1234].
  * There must be a VSETNUM corresponding to every VSETNUM in the EPAR file.
  * A minimum number of variogram models, equal to the number of cutoffs, must be defined. 

## Example

This example is designed to show the files, fields and parameters that are used by the **MIKEST** process. Some of the actual data values are not very realistic. For example only 3 cutoffs have been used whereas in practice around 12 cutoffs would be more usual. 

The example uses 2 zone control fields, Z1 and Z2. Each zone has 2 values, 1 and 2, thus making a total of 4 zone combinations. 

Fields **BINGRADE** and **ABVGRADE** are included in the **EPAR** estimation parameter file even though they are not used as @**GRMETHOD** =3. 
    
    
    !MIKEST   
  
---  
      
    
     &PROTO(M_MOD),&SAMPLES(M_SAMPS),        &SPAR(M_SPAR),&EPAR(M_EPAR),  
      
    
            &VMODEL(M_VPAR),&FIELDS(M_FPAR),   
      
    
       
      
    
            &OUTMODEL(M_OUTMOD),&AVGRADES(M_AVGRADES),  
      
    
            &INDICATE(M_INDICATE),&SAMPOUT(M_SAMPOUT),  
      
    
            *XPT(X),*YPT(Y),*ZPT(Z),  
      
    
            *ZONE1_F(Z1),*ZONE2_F(Z2),  
      
    
            @GRMETHOD=3,@PGFIELDS=1,@ORDER=3  
  
Related topics and activities

  * [COKRIG](<cokrig.md>)

  * [ESTIMA](<estima.md>)

  * [INDEST](<indest.md>)