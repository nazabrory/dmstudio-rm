# GRTON Process

To access this process:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **GRTON** and click **Run**.

  * Enter "GRTON" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_G.md#GRTON>).

## Process Overview

Calculate grades and tonnages using results from a Gaussian anamorphosis.

**Note** : The process [GAUSAN](<gausan.md>) must have been run previously to create a file of the polynomial coefficients.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
POLYNO |  Input file containing polynomial coefficients. This file is created as output by process **GAUSAN**. The following fields are required: 

  * **POLYINDX** \- polynomial index number [0,1,2,..] 
  * **COEFF** \- the polynomial coefficient. 
  * **POLYNUM** \- the number of polynomials used in the transformation.

|  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
QTN |  Output |  Yes |  Undefined |  Compulsory output file containing grade and tonnage values for different cut-offs. Change of support calculations are NOT used. It includes the following explicit fields: 

  * **CUTOFF** \- actual cut-off grade 
  * **ANAMOR** \- gaussian anamorphose 
  * **TONABOVE** \- ratio of tons mined above cut-off 
  * **METABOVE** \- ratio of metal recovered above cut-off 
  * **GRDABOVE** \- average grade above cut-off 
  * **TONBELOW** \- ratio of tons mined below cut-off 

It also includes the following implicit field: 

  * **CHSUPP** \- change of support variable. This is always set to 1.

  
QTR |  Output |  No |  Undefined |  Optional output file containing grade and tonnage values for different cut-offs. Change of support calculations are used. It includes the following explicit fields: 

  * **CUTOFF** \- actual cut-off grade 
  * **ANAMOR** \- gaussian anamorphose 
  * **TONABOVE** \- ratio of tons mined above cut-off 
  * **METABOVE** \- ratio of metal recovered above cut-off 
  * **GRDABOVE** \- average grade above cut-off 
  * **TONBELOW** \- ratio of tons mined below cut-off It also includes the following implicit fields. 
  * **CHSUPP** \- change of support variable. 
  * **BLOCKVAR** \- block variance, as defined by parameter **BLOCKVAR**.

  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SUPPORT |  Change of support flag: |  Option |  Description  
---|---  
0 |  Support change calculations not used  
1 |  Support change calculations used The default value is (0).  
No |  0 |  0,1 |  0,1  
BLOCKVAR |  The block variance. This parameter is compulsory if a change of support is required; ie if SUPPORT=1. |  No |  Undefined |  Undefined |  Undefined  
MAXITER |  Maximum number of iterations. The default value is (100). |  No |  100 |  Undefined |  Undefined  
PRINT |  Controls the amount of text displayed: The default value is (0). |  Option |  Description  
---|---  
0 |  Minimum output to screen  
1 |  As 0 + grade/tonnage results  
2 |  As 1 + display for each iteration  
No |  0 |  0,2 |  0,1,2  
  
Related topics and activities

  * [GAUSAN Process](<gausan.md>)