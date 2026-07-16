# POLREG Process  
  
To access this process:

  * **Sample Analysis** ribbon >> Statistics Processes >> Polynomial Regression.

  * Enter "POLREG" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **POLREG** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#POLREG>).

## Process Overview

Polynomial regression. The polynomial fitted is up to the 5th order, and thus includes a regression line.

The polynomial is of the form:-
    
    
    Y = C0 + C1*X + C2*X2 + C3*X3 + C4*X4 + C5*X5

where the coefficients C0, C1, C2, C3, C4 and C5 are written to the output file.

The input file must contain two explicit numeric fields *X and *Y. The polynomial is calculated as Y estimates for X values. There must be at least (order+1) points. If either the *X or *Y value is absent data in a particular record, the record is ignored. This allows regression polynomials to be computed on incomplete sets of data; for example original assays and a partial set of check assays.

  * **DATAFILE** : Name of the input data file.

  * **XDATA** : The X field in the input file that was used.

  * **YDATA** : The Y field in the input data file that was used.

  * **GOODNFIT** : The goodness of fit.

  * **CORRCOEF** : The coefficient of variance.

  * **STDERR** : The standard error.  

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  Output file containing the coefficients.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X co-ordinate of the sample data. |  IN |  Yes |  Numeric |  X  
Y |  Y co-ordinate of the sample data. |  IN |  Yes |  Numeric |  Y  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ORDER |  Order of the polynomial required (1,2,3,4 or 5). |  Yes |  1 |  1,5 |  1,2,3,4,5  
PRINT |  If set to 1 then a table of estimated values, based on the regression equation, will be written to the Command window. The default is (0), do not create the table. |  No |  0 |  0,1 |  0,1  
  
* * *

## Example

In the following example, a regression line is calculated for estimating P2O5 field values from FE field values in file assays.
    
    
    !POLREG     &IN(ASSAYS),&OUT(COEFFS),*X(FE),*Y(P2O5),@ORDER=1  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ORDER CANNOT BE LESS THAN 1, ORDER=1 HAS BEEN ASSUMED <<< |  A value of @**ORDER** below the minimum permitted value has been entered. The value is reset to the minimum and processing continues.  
>>> ORDER CANNOT BE GREATER THAN 5, ORDER=5 HAS BEEN ASSUMED <<< |  A value of @**ORDER** above the maximum permitted value has been entered. The value is reset to the maximum and processing continues.  
>>> FIELD nnnnnnnn IS NOT NUMERIC <<< >>> ERR 120 <<< ( fileno) IN POLREG |  Either the *X or *Y fields were not numeric. Fatal; the process is exited.  
>>> TOO LITTLE DATA, CANNOT COMPUTE POLYNOMIAL OF REQUIRED ORDER <<< >>> ERR 120 <<< ( fileno) IN POLREG |  The minimum number of points required is @**ORDER** \+ 1. Fatal; the process is exited.  
>>> ABSOLUTE VALUE OF DIV. IS LESS THAN OR EQUAL TO ZERO >>> ERR 501 <<< ( 0) IN DSLE |  The matrix of data presented for solution was singular. The data is inappropriate. Warning; the process continues, but the results may be meaningless.