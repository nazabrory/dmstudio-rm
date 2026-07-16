# GAUSAN Process

To access this process:

  * Enter "GAUSAN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **GAUSAN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_G.md#GAUSAN>).

## Process Overview

Perform a gaussian anamorphose transformation on a set of sample data.

The results can be:

  * displayed on the screen,

  * written to the print file, or;

  * saved in database files.

**Note** : The **POLYNO** output file can subsequently be used as input to the [GRTON](<grton.md>) process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample data file. A maximum of 99998 samples can be processed. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
POLYNO |  Output |  No |  Undefined |  Optional output file containing polynomial coefficients. It includes the following fields: 

  * **POLYINDX** \- polynomial index number [0,1,2,..] 
  * **COEFF** \- the polynomial coefficient. 
  * **ESTVAR** \- estimated variance. 
  * **POLYNUM** \- the number of polynomials used in the transformation. An implicit field.

  
TRANS |  Output |  No |  Undefined |  Optional output file containing transformed values. It includes the following explicit fields: 

  * **VALUE** \- the untransformed value. 
  * **FREQENCY** \- number of occurences of **VALUE**.
  * **ANAMOR** \- the transformed value.
  * **INVERSE** \- inverse of the transformed value.

It also contains the following implicit fields:

  * **POLYNUM** \- the number of polynomials used in the transformation.
  * **NUMSAMP** \- the number of transformed samples. 
  * **MEANORIG** \- mean of the original values. 
  * **VARORIG** \- variance of the original values. 
  * **MEANTRAN** \- mean of the transformed values.
  * **VARTRAN** \- variance of the transformed values. 
  * **MEANINV** \- mean of the inverse values.
  * **VARINV** \- variance of the inverse values.

  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Name of field in the IN file to be transformed. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NUMPOLY |  The number of polynomials to be used. A maxum of 30 is allowed. |  Yes |  Undefined |  1,30 |  Undefined  
PRINT |  Controls the amount of text displayed: |  Option |  Description  
---|---  
0 |  Minimum output to screen  
1 |  As 0 + polynomial coefficients  
2 |  As 1 + reconstitution of variance table  
3 |  As 2 + table of transformed values The default value is (0).  
No |  0 |  Undefined |  Undefined  
  
Related topics and activities

  * [GAUSANAM Process](<gausanam.md>)

  * [GRTON Process](<grton.md>)