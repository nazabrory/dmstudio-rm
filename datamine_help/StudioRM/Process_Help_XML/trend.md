# TREND Process

To access this process:

  * Enter "TREND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **TREND** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TREND>).

## Process Overview

Fit a polynomial trend surface to a set of data.

A polynomial of order 1, 2 or 3 may be fitted. The coefficients are calculated, displayed in the Command window, and stored in the output file. A summary of the goodness of fit parameters are also displayed in the Command window.

Note: If any record has any of *X, *Y or *Z values absent, the record is ignored and is not included in the record count.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. Must contain the fields X , Y , and VALUE. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file containing the surface coefficients. The fields are C0, CX, CY, CXY, CX2, CY2, CX2Y, CXY2, CX3, CY3.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X Co-ordinate fieldname. |  IN |  Yes |  Numeric |  Undefined  
Y |  Y Co-ordinate fieldname. |  IN |  Yes |  Numeric |  Undefined  
VALUE |  Field to be fitted. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ORDER |  Order of surface (1,2, or 3). |  Yes |  1 |  1,3 |  1,2,3  
PRINT |  >0, displays original samples, fitted points and differences (0). |  No |  0 |  0,1 |  0,1  
SELECT |  Allows the user to select every nth record, where n=SELECT (1). |  No |  1 |  Undefined |  Undefined  
  
## Example
    
    
    !TREND    &IN(SAMPLES),&OUT(COEFFS),*X(XCOORD),          
  
---  
      
    
    *Y(YCOORD),*VALUE(COPPER),@CINT=2.0,          
      
    
    MINIMUM=0,@ORDER=2,@PRINT=1  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> TOO MUCH DATA. COMPUTING TREND SURFACE ON FIRST 1000 RECORDS. <<< |  The maximum number of points which may be processed is 1000. All other points are ignored, and processing continued with the first 1000. |  Reduce the number of data points in the file.  
>>> TOO LITTLE DATA. CANNOT COMPUTE TREND SURFACE OF REQUIRED ORDER. >>> ERR 120 <<< ( fileno) IN TREND |  The minimum number of points needed for computation of a surface is 3 for order 1, 6 for order 2 and 10 for order 3. Fatal; the process is exited. |  Specify an input file with sufficient data points.  
>>> FIELD aaaaaaaa NOT NUMERIC <<< >>> ERR 120 <<< ( fileno) IN TREND |  One of the * **X** , * **Y** or * **Z** fields were not numeric. Fatal; the process is exited. |  Using the Datamine Table Editor, check the field types in the input data file.  
>>>ORDER CANNOT BE LESS THAN ONE, ORDER = ONE HAS BEEN ASSUMED |  A value of @**ORDER** below the minimum permitted value has been entered. The value is reset to the minimum and processing continues. |  Specify a valid value for @**ORDER**.  
>>>ORDER CANNOT BE GREATER THAN THREE. ORDER = THREE HAS BEEN ASSUMED |  A value of @**ORDER** above the maximum permitted value has been entered. The value is reset to the maximum and processing continues. |   
>>>ABSOLUTE VALUE OF DIV. IS LESS THAN OR EQUAL TO ZERO >>> ERR 501 <<< ( 0) IN DSLE |  The matrix of data presented for solution was singular. The data is inappropriate. Warning; the process continues, but the results may be meaningless. |