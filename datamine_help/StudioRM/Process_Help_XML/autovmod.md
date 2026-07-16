# AUTOVMOD Process  
  
To access this process:

  * **AUTOVMOD** is automatically accessed via the **[Advanced Estimation wizard](<../STUDIO_RM/Multivariate_Introduction.md>)**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **AUTOVMOD**
  * Enter "AUTOVMOD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#AUTOVMOD>).

## Process Overview

AUTOVMOD is used to automatically fit variogram and cross-variogram models to experimental variogram model data

The only mandatory input to this process is &**VGRAMS** , a file containing experimental variograms, such as that created by the [VGRAM](<vgram.md>) process. The output file is a fitted variogram model.

Retrieval Criteria can be used and applies to all inputs.

## VGRAMS (Input experimental variograms)

The &**VGRAMS** file should contain the experimental variograms (and optionally cross-variograms) from which the variogram model is fitted.

The file must contain the alpha field **GRADE** , where the variable name is specified, and optionally **GRADE2** to specify the second variable for the cross-variograms.

If anisotropic variogram fitting is on (**ANISO** = 1), **WAZI** and WIP, or AZI and DIP fields are required to specify the azimuth and dip values for each experimental variogram. If **ANISO** = 1, records with absent (W)**AZI** and (W**)DIP** values will be ignored. If **ANISO** = 0 and (W)**AZI** and (W**)DIP** are present, only records with absent (W)**AZI** and (W)**DIP** values will be used. **WAZI** and **WDIP** will be used in preference to **AZI** and **DIP** if both are present.

The file must contain the numeric fields; **NO.PAIRS** , **AVE.DIST** and **VGRAM** specifying the number of pairs, average distance and (co-)variogram value per lag. The file must also contain the field **VRGRADE** specifying the (co-)variance per variable this must be consistent across records for each variable combination. If the variance/covariance matrix is not positive definite, a positive definite approximation will be used.

Each variogram / cross-variogram for a specific variable combination and direction must be ordered by lag (i.e. by **AVE.DIST**). If multiple sets of the same variable combination / direction are found, only the first is used.

Example file:

GRADE |  GRADE2 |  AZI |  DIP |  LAG |  AVE.DIST |  NO.PAIRS |  VGRAM |  VRGRADE  
---|---|---|---|---|---|---|---|---  
V |  V | 0 | 0 |  3 |  9.23655251 |  89 |  43501.357 |  90104.1285  
V | V | 0 | 0 |  4 |  11.907085 |  76 |  59934.939 |  90104.1285  
V | V | 0 | 0 | 6 |  18.5201788 |  144 |  50488.215 |  90104.1285  
V | V | 0 | 0 | 7 |  20.8608547 |  221 |  52338.884 |  90104.1285  
V | V | 0 | 0 | 8 |  23.1065762 |  29 |  73978.557 |  90104.1285  
V | V | 0 | 0 | 9 |  27.7653056 |  48 |  66461.985 |  90104.1285  
V | V | 0 | 0 | 10 |  30.1252673 |  228 |  74705.725 |  90104.1285  
V | V | 0 | 0 | 11 |  32.590156 |  56 |  83772.173 |  90104.1285  
V | V |  10 | 0 | 3 |  9.35453375 |  93 |  42219.125 |  90104.1285  
V | V | 10 | 0 | 4 |  11.8346962 |  84 |  49039.75 |  90104.1285  
V | V | 10 | 0 | 5 |  13.6014705 |  3 |  18326.248 |  90104.1285  
V | V | 10 | 0 | 6 |  18.5037464 |  120 |  59821.477 |  90104.1285  
V | V | 10 | 0 | 7 |  20.9222617 |  215 |  62070.362 |  90104.1285  
V | V | 10 | 0 | 8 |  23.2539724 |  40 |  82015.079 |  90104.1285  
V | V | 10 | 0 | 9 |  27.8759329 |  41 |  76356.469 |  90104.1285  
V | V | 10 | 0 | 10 |  30.204982 |  202 |  74504.89 |  90104.1285  
V | V | 10 | 0 | 11 |  32.6099785 |  118 |  88274.922 |  90104.1285  
|  |  |  |  |  |  |  |   
V |  U | 0 | 0 | 3 |  9.2641395 |  56 |  76101.262 |  115674.356  
V | U | 0 | 0 | 4 |  11.822023 |  53 |  108904.34 |  115674.356  
V | U | 0 | 0 | 6 |  18.6037187 |  69 |  113042.52 |  90104.1285  
V | U | 0 | 0 | 7 |  20.8373739 |  93 |  117518.29 |  90104.1285  
V | U | 0 | 0 | 8 |  23.1060254 |  21 |  176858.68 |  90104.1285  
V | U | 0 | 0 | 9 |  27.7634941 |  28 |  141543.48 |  90104.1285  
V | U | 0 | 0 | 10 |  30.1473913 |  133 |  126577.57 |  115674.356  
V | U | 0 | 0 | 11 |  32.5943458 |  29 |  146002.9 |  115674.356  
  
## NUGGET(Known nugget file)

&NUGGET is used to specify known nugget value(s) for all variogram and cross-variogram models. The file must contain the alpha field GRADE, where the variable name is specified, and optionally GRADE2 to specify the second variable for the cross-variogram nugget. The file must also contain the numeric field NUGGET to specify the nugget value.

If a variable combination is missing or if the NUGGET value is absent data (-), the nugget will be set to 0.

If the same variable combination is found in the GRADE and GRADE2 column multiple times, only the first is used. N.B. GRADE = X GRADE2 = Y and GRADE = Y, GRADE2 = X are equivalent.

If the nugget matrix is not positive definite, a positive definite approximation will be used.

If this file is not specified the nugget values will be fitted to the model.

Example file:

GRADE |  GRADE2 |  NUGGET  
---|---|---  
U |  U |  580000  
V |  V |  27000  
U |  V |  100000  
  
## STRUCTS (Allowed structures file)

&STRUCTS is used to specify how many and which structure types can be used in the fitted model and any constraints on the ranges for those structures. It must contain the numeric field MODEL which is used to specify the type of structure allowed. It can optionally contain the numeric fields RANGEMIN and RANGEMAX to specific the minimum and maximum range values to be fitted for the associated structure type. To allow more than one structure of a particular model, specify the same MODEL on multiple records.

Allowed **MODEL** values:

1 = Spherical

3 = Exponential

4 = Gaussian

Both RANGEMIN and RANGEMAX must be non-absent for range constraints to be valid. If either or both are absent data then range constraints will not be applied. This does not affect the validity of the corresponding MODEL value.

If the file is not specified, up to 3 spherical structures will be allowed.

Example file allowing two constrained spherical models, and one constrained exponential model with a range between 100 and 500:

MODEL |  RANGEMIN |  RANGEMAX  
---|---|---  
1 |  0 |  20  
1 |  20 |  100  
3 |  100 |  500  
  
## SILLS (Cumulative sill file)

This file is used to specify constraints on the cumulative sill value for each variable. It must contain the alpha field GRADE and the numeric field SILL which are used to specify the variable name and cumulative sill value for that variable respectively.

The cumulative SILL value is calculated as the sum of the sills for each structure. It does not include the NUGGET. In terms of the fields in the variogram model parameter file:

SILL = ST1PAR4 + ST2PAR4 \+ ST3PAR4 + ...

If the same variable is found in the GRADE column multiple times, only the first is used.

If this file is not specified there will be no constraints set on the sill values.

Example file:

GRADE |  SILL  
---|---  
U |  10000  
V |  20000  
  
## Process Parameters Summary

### **VREFNUM**

The variogram reference number to be used for the output variogram model.

### MINNUGPC

The minimum percentage of the total sill that the fitted nugget value must reach to be included in the model.

The allowed range is [0%, 30%].

### MINSILPC

The minimum percentage of the total sill that the sill value of a fitted structure must reach for that sill to be included in the model.

The allowed range is [1%, 30%].

### MAXSTRCT

Maximum number of structures to be fitted in the model. The allowed range is [1, 9].

### MAXIT

The maximum number of iterations to run during the fitting process. This number will only be reached if the algorithm does not converge.

### MULTIVAR

Set to 1 load cross-variograms if present and fit a multivariate variogram model suitable for use in cokriging.

### ANISO

Set to 1 to read and fit anisotropic variograms. Set to 0 to read and fit isotropic variograms.

## Command Window Output

The command window will display:

  * The (cross-)variograms and directions read from the **VMODEL** file.

  * The variances and co-variances (and the positive definite approximation, if not already positive definite)

  * The list of allowed structures in the model.

  * The maximum structures and iterations.

  * The minimum nugget and sill percentages.

  * The nugget values set, if the **NUGGET** file is used (and the positive definite approximation, if not already positive definite)

  * The number of fitted structures.

  * The fitted rotation.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
VGRAMS |  A Datamine file that contains experimental variograms. It must contain the columns GRADE (and GRADE2 for crossvariograms), AVE.DIST, NO.PAIRS, VGRAM and VRGRADE. If fitting anisotropic variograms (ANISO=1), it must have the fields WAZI and WDIP or AZI and DIP. Each experimental variogram (defined by a GRADE, GRADE2, (W)AZI and (W)DIP) must be ordered by AVE.DIST. VRGRADE must be consistent for each record of each GRADE/GRADE2 combination. |  Input |  Yes |  Undefined  
NUGGET |  File to define fixed nugget values for the variogram model. The file must contain GRADE, GRADE2 and NUGGET to define the variable, covariable and fixed nugget values respectively. Missing variable/covariable combinations will have their nugget value set to 0. If the file is not defined, nugget values will be fitted. |  Input |  No |  Undefined  
SILLS |  File to define the cumulative sill value for each variable. It must contain the fields GRADE and SILL to define the variable and the cumulative sill for that variable. If the file is not defined there will be no constraints set on the cumulative sill. |  Input |  No |  Undefined  
STRUCTS |  File to define the allowed structures in the fitted model. The file must contain the MODEL field which should be set to 1 (Spherical), 3(Exponential) or 4(Gaussian). It can optionally contain the numeric fields RANGEMIN and RANGEMAX to define the minimum and maximum range value for that structure \- these values can be set to absent if no range is to be defined for that structure. If the file does not exist up to 3 spherical structures will be allowed. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
VMODEL |  Output |  Yes |  Undefined |  Output file for the fitted variogram model(s). If the file already exists the model will be appended to the file, otherwise a new file will be created.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VSETNUM |  The output model set VSETNUM value. |  Yes |  1 |  Undefined |  Undefined  
MINNUGPC |  Minimum nugget percent |  Yes |  1 |  0,30 |  Undefined  
MINSILPC |  Minimum sill percent per structure. |  Yes |  5 |  1,9 |  Undefined  
MAXSTRCT |  Maximum number of structures. |  Yes |  3 |  Undefined |  Undefined  
MAXIT |  Maximum number of iterations. |  Yes |  1000 |  Undefined |  Undefined  
MULTIVAR |  Set to 1 load cross-variograms if present and fit a multivariate variogram model suitable for use in cokriging. |  Yes |  1 |  0,1 |  0,1  
ANISO |  Set to 1 to fit anisotropic variograms, 0 to fit isotropic variograms. |  Yes |  1 |  0,1 |  0,1  
MAJORAZI |  Azimuth of the major direction for the fitting. |  No |  Undefined |  Undefined |  Undefined  
MAJORDIP |  Set to 1 to fit anisotropic variograms, 0 to fit isotropic variograms. |  No |  Undefined |  Undefined |  Undefined  
SEMIMAZI |  Set to 1 to fit anisotropic variograms, 0 to fit isotropic variograms. |  No |  Undefined |  Undefined |  Undefined  
SEMIMDIP |  Set to 1 to fit anisotropic variograms, 0 to fit isotropic variograms. |  No |  Undefined |  Undefined |  Undefined  
  
Related topics and activities

  * [Advanced Estimation wizard](<../STUDIO_RM/Multivariate_Introduction.md>)

  * [VGRAM Process](<vgram.md>)