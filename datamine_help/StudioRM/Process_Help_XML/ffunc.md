# FFUNC Process  
  
To access this process:

  * Enter "FFUNC" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FFUNC** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FFUNC>).

## Process Overview

The F function estimates the variance of a point in a block, based on a variogram model which is selected from the input variogram model file **VMODPARM**.

The block whose F value is to be calculated is simulated by a 3 dimensional matrix of discretisation points. The F value is calculated as the average value of the variogram between each possible pair of discretisation points.

The number of discretisation points in each of the X, Y and Z directions is specified by parameters **IPOINTS** , **JPOINTS** and **KPOINTS**. It is recommended that a minimum of 4 x 4 x 4 points is used. The processing speed is proportional to the number of points used.

You will be prompted interactively to enter the X, Y and Z dimensions of the block. The F value will be displayed in the Output window, and you may then enter the dimensions of another block, or ! to terminate the process.

By estimating the F-function for two block sizes, the theoretical Dispersion Variance for selective mining units within a kriged block can be calculated. This can then be used as input to processes [SMUHIS](<smuhis.md>) and [SMUMOD](<smumod.md>).

**Note** : You will be prompted interactively to enter the dimensions of the block whose F value is required.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
VMODPARM |  Input variogram model file. |  Input |  Yes |  Variogram - Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  Optional output file. This will contain the block dimensions and F value in fields **XINC** , **YINC** , **ZINC** and **FVALUE**.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VMODNUM |  Variogram model number, as defined by **VREFNUM** field in **VMODPARM** file. Default (1). |  No |  1 |  Undefined |  Undefined  
LOG |  Log/Normal variogram flag. Default(0). The variogram model, as defined by **VGRAM** , is Normal if LOG =0 or Lognormal if LOG =1. |  No |  0 |  0,1 |  0,1  
IPOINTS |  Number of discretisation points in X dimension to simulate block (6) |  No |  6 |  Undefined |  Undefined  
JPOINTS |  Number of discretisation points in Y dimension to simulate block (6) |  No |  6 |  Undefined |  Undefined  
KPOINTS |  Number of discretisation points in Z dimension to simulate block (6) |  No |  6 |  Undefined |  Undefined  
  
## Example
    
    
    !FFUNC  &VMODPARM(vmodel), &OUT(fvalues), @VMODNUM=1, @LOG=0,  
  
---  
      
    
    @IPOINTS=6, @JPOINTS=6, @KPOINTS=6  
      
    
    Calculation of Average Value of Variogram within 3D Block  
      
    
    ---------------------------------------------------------  
      
    
    Variogram model file VMODEL includes fields for up to 9 structures.  
      
    
    The file contains 10 records.  
      
    
    Model 1.00 has been retrieved from file.  
      
    
    Number of fully defined structures = 2  
      
    
    N Nugget Variance = 1.6000  
      
    
    G1 Rotation Angle 1 = 22.5  X1 Rotation Axis 1 = 3 (Z)  
      
    
    G2 Rotation Angle 2 = 0.0   X2 Rotation Axis 2 = 2 (Y)  
      
    
    G3 Rotation Angle 3 = 180.0 X3 Rotation Axis 3 = 1 (X)  
      
    
    Structure Model Type Range X Range Y Range Z Spatial Var  
      
    
    T          AX      AY      AZ        C  
      
    
    1          1        19.0    23.0    43.0   2.9000  
      
    
    2          1        38.0    64.0    90.0   2.3000  
      
    
    3          1           -       -       -        -  
      
    
    Number of discretisation points in X,Y,Z =   6   6   6  
      
    
    You will now be prompted to enter the X,Y and Z dimensions of the 3D block.  
      
    
    Enter the next block size (or ! to terminate):  
      
    
    ----------------------------------------------  
      
    
    X Block Size >10  
      
    
    Y Block Size >12  
      
    
    Z Block Size >5  
      
    
    F-function estimate for block of size 10.000 x 12.000 x 5.000  
      
    
    Average value of variogram in block = 3.1309  
      
    
    Enter the next block size (or ! to terminate):  
      
    
    ----------------------------------------------  
      
    
    X Block Size >!  
  
Related topics and activities

  * [SMUHIS Process](<smuhis.md>)

  * [SMUMOD Process](<smumod.md>)