# KNA Process

To access this process:

  * Enter "KNA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **KNA** and click **Run**.

  * Used by [Advanced Estimation](<../STUDIO_RM/Multivariate_Introduction.md>) wizard

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_K.md#KNA>).

## Process Overview

KNA (Kriging Neighbourhood Analysis) is used to optimize the parameters for grade estimation. Typically multiple estimations are performed on a small number of blocks and the results are averaged for each estimation and compared to find an optimal set of parameters. The parameters are then used by the COKRIG process to estimate grades into a block model by a range of methods including Kriging.

The input to KNA is similar to COKRIG:

  * SAMPLES: Samples file
  * TESTBLKS: Up to three sets of model blocks to be tested are identified by their XC, YC and ZC coordinates. Each set can represent a different area and is identified by the _BLKGROUP_ field

  * EPAR: Specifies estimation parameters such as search volume identifier, kriging method, block size and discretization points

  * FIELDS: Input (grade) and output (estimation/**KNA** stats) field names for each estimation

  * VMODEL: Contains the variogram model parameters

  * SPAR: Contains the search volume parameters referenced in the **EPAR** file

The output file **OUT** lists block size, block group, discretization, search parameters and **KNA** statistics.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SAMPLES |  A file containing sample positional information and supporting attributes. |  Input |  Yes |  Undefined  
TESTBLKS |  A file containing centre positions of test blocks to perform grade estimation on. It can optionally contain a numeric field to specify groups of blocks to calculate statistics per group which must be specified as the _BLKGROUP_ field. |  Input |  Yes |  Undefined  
EPAR |  The input estimation parameter file used to specify parameters and for each estimation. This must contain the following fields:

  * SREFNUM
  * IMETHOD
  * DISCX
  * DISCY
  * DISCZ
  * BLKSZX
  * BLKSZY
  * BLKSZZ

_SREFNUM_ defines the reference of the search parameters found in the SPAR file. _IMETHOD_ is used to specify the Interpolation method

  * 3=Ordinary Kriging (default)
  * 4=Simple Kriging using sample means
  * 10=Simple Kriging using means defined in FIELDS
  * 11=Simple Kriging using local means defined in the prototype).

_DISCX, DISCY, DISCZ_ specify the number of discretization points.  _BLKSZX, BLKSZY, BLKSZZ_ specify the dimensions of the cells to be interpolated into. |  Input |  Yes |  Undefined  
FIELDS |  A file that contains field names of variables to be used in estimation. Input variables must be included under the mandatory column IN_VAR and each of these fields must be present in the **SAMPLES** and **VGRAM** file. If more than 1 variable is supplied Multivariate (Co)Kriging will be performed. If _IMETHOD_ =10 is used, the column _SKMEAN_ must be used to specify the mean per variable. If _IMETHOD_ =11 is used the column _LOC_MEAN_ must be used to specify the local mean fields in the prototype model. |  Input |  Yes |  Undefined  
VMODEL |  The input (cross-)variogram model parameter file. If more than 1 variable is suppled in the **FIELDS** file (i.e. multivariate estimation), this file must contain the columns _GRADE_ and _GRADE2_. |  Input |  Yes |  Undefined  
SPAR |  The input search parameter file. This must contain the following 12 mandatory fields:

  * _SREFNUM_ which is used to store a reference number for each record which is then specified by the SREFNUM parameter in COKRIG.
  * _SDIST1, SDIST2, SDIST3_ specifying the search distances in the X, Y and Z directions respectively.
  * _SAXIS1, SAXIS2, SAXIS3_ specifying the first, second and third axes which the search volume is to be rotated around (1 = x, 2 = Y, 3 = Z).
  * _SANGLE1, SANGLE2, SANGLE3_ which specify the clockwise angles which search volume is rotated around the axes specified by _SAXIS1, SAXIS2, SAXIS3_.
  * _MINNUM1_ which is the minimum number of samples required per estimate
  * _MAXNUM1_ which is the optimum number of samples to be used per estimate.

|  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  The output file which will contain statistics for each estimation which has been performed.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
XPT/YPT/ZPT |  X/Y/Z coordinate of sample data in the **SAMPLE** file. |  IN |  Yes |  Undefined |  XPT/YPT/ZPT  
KEY |  Key field used to specify the field limiting the number of samples for estimation using the optional **OPTKEY** and **MAXKEY** parameters in the **SPAR** file. The field must exist in the **SAMPLES** file. |  IN |  No |  Undefined |  Undefined  
BLKGROUP |  Numeric field in the **PROTO** file used to split test blocks into groups to calculate statistics from. |  IN |  No |  Undefined |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VSETNUM |  The reference number of the variogram model set to be used from the **VMODEL** file |  Yes |  1 |  Undefined |  Undefined  
NOKSTATS |  Set this parameter to 1 to prevent output of Kriging statistics. Typically used with BLKCOV=1 when testing the number of discretization points to be used. |  No |  0 |  0,1 |  0,1  
BLKCOV |  Set this parameter to 1 to calculate and output block covariance. Typically used for testing discretization. |  No |  0 |  0,1 |  0,1  
NBLKCOV |  The number of random samples to use for calculating block covariance per **KNA** run. A value of at least 20 is recommended to ensure reasonable precision. |  No |  20 |  Undefined |  Undefined  
PRNT |  The level of detail for text printed to the command window. A value of 0 only prints errors, a value of 1 additionally prints warnings and progress, a value of 2 additionally prints further information. |  Yes |  0 |  0,1 |  0,1  
NTHREADS |  Number of threads to be used for the main calculation. Any value less than 1 will automatically select the values based on the number of virtual cores on the computer. |  No |  -1 |  Undefined |  Undefined  
  
Related topics and activities

  * [Advanced Estimation & Variography](<../STUDIO_RM/Multivariate_Introduction.md>)