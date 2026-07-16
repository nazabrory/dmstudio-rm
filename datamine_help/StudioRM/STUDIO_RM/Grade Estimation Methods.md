# Grade Estimation Methods

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

It is possible to select different grades to estimate, using different methods and different parameters all in a single run of **ESTIMA** including running **ESTIMA** via the [ESTIMATE](<EstimateDialog.md>) dialog. The different combinations of grades/methods/parameters etc. are each defined by a record in the Estimation Parameter file (&**ESTPARM**).

## Methods available

The estimation method is defined by the field IMETHOD. This can take the following values (links shown launch external topics):

  1. [Nearest Neighbour](<Grade%20Estimation%20Nearest%20Neighbour.md>) (NN)

  2. [Inverse Power of Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) (IPD)

  3. [Ordinary Kriging](<Grade%20Estimation%20Kriging.md>) (OK)

  4. [Simple Kriging](<Grade%20Estimation%20Kriging.md>) (SK)

  5. [Sichel's T Estimator](<Grade%20Estimation%20Sichels%20T%20Estimator.md>) (ST)

  6. [F value](<Grade%20Estimation%20F%20Value.md>) (pseudo estimation method) 

  7. [Lagrange Multiplier](<Grade%20Estimation%20Lagrange%20Multiplier.md>) (pseudo estimation method)

### The Estimation Parameter File

A simple example of an Estimation Parameter file is shown below. In this example AU is estimated using Inverse Power Distance (2) and AG using Ordinary Kriging (3):

Description |  Name of field to be estimated |  Search volume reference number |  Estimation method |  Weighting power for IPD method |  Model variogram reference number  
---|---|---|---|---|---  
Field Name |  VALUE_IN |  SREFNUM |  IMETHOD |  POWER |  VREFNUM  
Field Type |  A-8 Chars |  N |  N |  N |  N  
Record 1 |  AU |  1 |  2 |  2 |  -  
Record 2 |  AG |  2 |  3 |  - |  1  
  
Each estimate is defined as a separate record in the file. In this example different search volumes have been defined for the two grades. The search volume reference numbers (SREFNUM) refer to the equivalent field in the Search Volume Parameter file.

Each estimation method (IMETHOD) has a numeric code, as described previously. The field POWER only applies to Inverse Power Distance (**IMETHOD** =2), and so is set to absent data for other methods. The model variogram reference number refers to a record in the Variogram Model Parameter file, which is described later in a section in [Grade Estimation Variogram Parameters File](<Grade%20Estimation%20Variograms.md>).

### VALUE_IN and VALUE_OU

As can be seen in the example, the VALUE_IN field is an alphanumeric field of 8 characters, and is used to define the grades to be estimated. These grade fields (AU and AG) must exist in the Sample Data file. There is also an optional VALUE_OU field (alphanumeric \- 8 characters) which allows you to specify a name for the field in the Output Model file. If you do not specify a VALUE_OU field, (i.e. it is left blank) then the name of the field in the Output Model file is the same as the name of the VALUE_IN field. In the previous example, there is no VALUE_OU field and so fields AU and AG would be created in the Output Model file.

The VALUE_OU field is particularly useful if you want to estimate the same grade by different methods or by the same method but using different parameters. For example if you want to estimate AU by both Inverse Power Distance and Ordinary Kriging methods, the VALUE_OU field could be AU-IPD and AU-OK. In both cases, the VALUE_IN field would be AU.

Description |  Name of field to be estimated |  Name of field in output file |  Search volume reference number |  Estimation method |  Weighting power for IPD method |  Model variogram reference number  
---|---|---|---|---|---|---  
Field Name |  VALUE_IN |  VALUE_OU |  SREFNUM |  IMETHOD |  POWER |  VREFNUM  
Field Type |  A-8 Chars |  A-8 Chars |  N |  N |  N |  N  
Record 1 |  AU |  AU-IPD |  1 |  2 |  2 |  -  
Record 2 |  AG |  AU-OK |  1 |  3 |  - |  1  
  
### Zonal Control

In some cases it may be necessary to use different parameters for the same grade field in different areas. For example, AU may have a different set of estimation parameters depending on the rock type. It is possible to specify one or two Zone fields using Zonal control and to have different parameters for each Zone.

Zones are defined using the *ZONE1_F and *ZONE2_F fields. For example if different parameters are to be applied depending on Rock Type and Fault Zone then the following fields should be specified:
    
    
    *ZONE1_F(ROCK), *ZONE2_F(FLTZONE)

The fields ROCK and FLTZONE must exist in both the Sample Data file and the Input Prototype Model file. Zonal control cannot be used if the Input Prototype Model file does not contain any cells.

Zone fields may be either alphanumeric or numeric. If they are alphanumeric then they may contain a maximum of 20 characters (5 words). In the following example field ROCK is alphanumeric and field FLTZONE is numeric.

Description |  Name of field to be estimated |  Search volume reference number |  Estimation method |  Rock type field  
{ZONE1_F} |  Rock type field  
{ZONE2_F} |  Weighting power for IPD method |  Model variogram reference number  
---|---|---|---|---|---|---|---  
Field Name |  VALUE_IN |  SREFNUM |  IMETHOD |  ROCK |  FLTZONE |  POWER |  VREFNUM  
Field Type |  A-8 Chars |  N |  N |  A-4 chars |  N |  N |  N  
Record 1 |  AU |  1 |  3 |  A |  1 |  - |  1  
Record 2 |  AU |  1 |  3 |  B |  1 |  - |  2  
Record 3 |  AU |  2 |  2 |  A |  2 |  2 |  -  
Record 4 |  AU |  2 |  2 |  B |  2 |  3 |  -  
Record 5 |  AU |  2 |  2 |  |  |  2 |  -  
  
Record 5 has absent data for both the Zone fields (blank for the alphanumeric field ROCK, and for the numeric field FLTZONE). This set of parameters (the default option) is used for estimating any cells whose ROCK and FLTZONE fields are not explicitly defined in the Estimation Parameter file. In order to use this default option with two Zone fields, it is necessary to specify both values as absent data.

If two Zone fields are defined then it is not possible to specify one field explicitly and have the other field as absent data. For example, you cannot have ROCK as B and FLTZONE as - "".

If there is only one Zone field then the estimation parameters corresponding to an absent Zone value will apply to all values whose Zone field is not otherwise specified in the Estimation Parameter file. Therefore, if all Zones are estimated using a single set of parameters then it is only necessary to have one record in the Estimation Parameter file which has the Zone field as absent data.

### Secondary Fields

The grade being estimated is always written to the Output Model file with its field name determined by the VALUE_IN/VALUE_OU fields. In addition to the grade field, some of the estimation methods also calculate secondary fields. For example, kriging also calculates the number of samples used for kriging and the kriged variance. In order for ESTIMA to write these secondary fields to the Output Model file the field names must be defined using the Estimation Parameter file. For example:

Description| Name of field to be estimated| Search volume reference number| Estimation method| Number of samples used for estimate| Variance of estimate| Dynamic search volume number| Distance to nearest sample  
---|---|---|---|---|---|---|---  
Field Name| VALUE_IN| SREFNUM| IMETHOD| NUMSAM_F| VAR_F| SVOL_F| MINDIS_F  
Field Type| A-8 Chars| N| N| A-8 chars| A-8 chars| A-8 chars| A-8 chars  
Record 1| AU| 1| 3| N-AU| VAR-AU| SVOL-AU| MIDST-AU  
Record 2| AG| 1| 3| N-AG| VAR-AG| SVOL-AG| MIDST-AG  
  
The dynamic search volume was described earlier. It takes values 1, 2 or 3 depending on which search volume is used. In the above example fields SVOL-AU and SVOL-AG are created in the Output Model file to record which dynamic search volume is used for each grade.

The calculation of the transformed distance of a sample from the cell centre was also described earlier in the Search Volume section. The field name in which to record the transformed distance of the nearest sample is defined by the MINDIS_F field. This could be used to assist in categorizing reserves.

The other secondary fields used in this example are NUMSAM_F for recording the number of samples used to make the estimate, and VAR_F to record the variance of the estimate. The latter field is only applicable to some of the estimation methods.

If there were no absent data AU or AG values in the Sample Data file and both variables were estimated using the same search volume parameters, then the NUMSAM_F, SVOL_F and MINDIS_F values would be the same. In this case there would be no need to specify different output field names and so records 1 and 2 could be defined as:

Description| Name of field to be estimated| Search volume reference number| Estimation method| Number of samples used for estimate| Variance of estimate| Dynamic search volume number| Distance to nearest sample  
---|---|---|---|---|---|---|---  
Field Name| VALUE_IN| SREFNUM| IMETHOD| NUMSAM_F| VAR_F| SVOL_F| MINDIS_F  
Field Type| A-8 Chars| N| N| A-8 chars| A-8 chars| A-8 chars| A-8 chars  
Record 1| AU| 1| 3| N| VAR-AU| SVOL| MIDST  
Record 2| AG| 1| 3| N| VAR-AG| SVOL| MIDST  
  
If the variogram parameters are different, then the kriged variances will be different, and therefore different output field names should be used.

If the same output field names are used but different search volume parameters applied, then values will be written to the Output Model file, but it is not possible to distinguish if the values apply to AU or AG. Care must therefore be taken when specifying secondary field names.

Secondary field names must not be the same as the field name in the estimation parameter file. For example, the field name for the variance must not be VAR_F and the field name for the search volume number must not be SVOL_F.

![](../Images/NextExercise.gif)[Go to the next topic](<Grade%20Estimation%20Nearest%20Neighbour.md>) (Nearest Neighbour Method)