# MIKSCELL Process

To access this process:

  * Estimate ribbon | Estimate >> MIK Subcell

  * Enter "MIKEST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MIKEST** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MIKSCELL>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**MIKSCELL** is designed to take a model created by Multiple Indicator Kriging (MIK) and convert it into a model that is suitable for input to Studio NPVS or Studio NPVS+

In the MIK model each record includes a pair of fields, **PRABi** and **GRABi** , i=1,n, containing the PRoprtion ABove cut off and the GRade ABove cutoff for a set of n cutoff grades. In the output model the interval between successive cutoff grades is represented by an individual subcell.

The volume of each subcell represents the volume of material between the cutoffs. The dimensions of the subcell are set equal to the dimensions of the parent cell in two directions and in the third direction the size is calculated so that the volume is correct. Parameter AXIS defines the method used for determining the subcell size.

Parameter **MINVOL** allows the user to specify the minimum volume of an individual subcell. If a subcell volume is less than the minimum it will be combined with the subcell in the grade interval below. However note that if the total volume of all subcells is less than **MINVOL** the combined subcell will still be included in the output model.

The output model includes field **INTERVAL**. This is set to 1 for the subcell that represents the material lower than the first cutoff, 2 for material between the first and second cutoffs, and so on. If **MINVOL** has been selected and two or more subcells have been combined then the **INTERVAL** values will also be averaged so non integer values of **INTERVAL** will be created.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
MODELIN |  Convert Multiple Indicator Kriging (MIK) output created by **[ESTIMA](<estima.md>)** or **[INDEST](<indest.md>)** to individual subcells for each grade range. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODELOUT |  Output model file containing individual subcell for each grade range. |  Yes |  Input |  Block Model  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
Grade |  Grade field in input model containing the MIK grade - that is the grade above a cutoff of zero. |  Undefined |  Yes |  Undefined |  Undefined  
F1 to F10 |  Grade fields in input model. Will be copied to the output model. |  Undefined |  No |  Undefined |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
Axis |  Axis along which the dimension of the subcell will be proportioned. Along the other two axes the dimensions of the subcell will be the size of the parent cell (3): =1 : subcell will have variable length along the X axis. Along axes Y and Z it will be the size of the parent cell. =2 : subcell will have variable length along the Y axis. Along axes X and Z it will be the size of the parent cell. =3 : subcell will have variable length along the Z axis. Along axes X and Y it will be the size of the parent cell. |  Yes |  3 |  1,3 |  1,2,3  
MINVOL |  The minimum volume of a subcell. If the subcell is less than the minimum it will be combined with the subcell with the next lowest grade. If the lowest grade subcell is less than **MINVOL** it will be combined with the subcell in thegrade range above |  No |  0 |  |   
TOLERNCE |  This defines the smallest subcell that will be included in **MODELOUT** as a proportion of the parent cell size.  The default of 0.0001 means that the subcell size along each axis cannot be less than 0.01% of the parent cell size. | No | 0.0001 |  |   
  
## Example
    
    
    !MIKSCELL   
  
---  
      
    
     &MODELIN(MODELIK4),&OUT(MODELIK4A),*GRADEIN(AU),  
      
    
    @AXIS=3,@TOLERNCE=0.0001  
      
    
    MIKSCELL  
      
    
    6 cutoffs in modelik4  
      
    
    ... creating subcells  
      
    
    cutoff 1  
      
    
    cutoff 2  
      
    
    cutoff 3  
      
    
    cutoff 4  
      
    
    cutoff 5  
      
    
    cutoff 6  
      
    
    Calculation of subcells complete  
      
    
    - input file modelik4 contains 3970 records  
      
    
    - output file modelik4a contains 1915 records  
  
Related topics and activities

  * [INDEST Process](<indest.md>)

  * [ESTIMA Process](<estima.md>)

  * [ESTIMATE Process](<estimate.md>)