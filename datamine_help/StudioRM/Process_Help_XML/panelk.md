# PANELK Process

To access this process:

  * Enter "PANELK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PANELK** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PANELK>).

## Process Overview

See also [PANELEST Process](<panelest.md>).

This process estimates the average value and the estimation variance of irregular shaped 2-D panels using kriging.

Panels are defined as a series of 2-D points in a standard string file. The value of **ZP** is ignored. Several panels may be held in the same file, all of which will be evaluated in a single run of the process. It does not matter whether the panel strings are open or closed. **VMETHOD** controls the method by which the variogram model is defined:

VMETHOD=1

A single structure spherical model is used, defined by parameters **NUGGET** and so on. This method is consistent with earlier versions of the process, and is the default.

VMETHOD=2

The standard range of variogram models is available, defined by interactive prompting. This is consistent with processes **KRG3DB** , **PTK3DA** and so on. **VMETHOD** =1 then the two variogram ranges are defined by **RANGE1** and **RANGE2** , and the anisotropy angle by **VGANGLE1**. 

Note: The angle is measured clockwise from the North to direction 1. Direction 2 is perpendicular to direction 1 in the same plane as the panels. It does not matter whether direction 1 represents the major or minor axis.

The following definitions are equivalent:

  * RANGE1 100 300 100 

  * RANGE2 300 100 300 

  * VGANGLE1 50 140 230

If **VMETHOD** =2 then the user is prompted interactively to enter the variogram parameters for all 3 directions. The data for the 3rd direction, perpendicular to the plane of the panels, is not used, but values must still be entered for that direction. It is suggested that values in the third direction are set equal to the values in direction 1 or direction 2. Whatever values are entered for the third direction,the range must not be set to zero. - only samples within a distance **SEARCH** of the centre of gravity (CG) ofthe panel are selected. - if more than **NMAX** lie within the search area, then the nearest **NMAX** to the CG are selected. 

**NSIM**

The origin of the grid is at a point defined by the minimum X and Y of the panel points. **MINSIM** then the value of **NSIM** is increased by 1, and the process is repeated until the number of internal points exceeds **MINSIM**. The maximum number of simulated points allowed is 1000. Processing speed is approximately proportional to the square of the number of samples in the kriging matrix. It is also influenced to a lesser extent by the number of simulated points in the panel.

Warning: If two or more samples have the same X and Y coordinate then an error will be reported as _ERR 131 in SOLVED_ and _ERR 122 in PKM3DA_.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input sample data file. This must contain the three fields **X , Y** and **VALUE**. |  Input |  Yes |  Undefined  
IN2 |  The input panel data file. This must contain the 4 fields **PANEL , PTN , XP** field must be defined explicitly, and will often be called **PVALUE**. The strings may be open or closed. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  The output results file. This will contain the following fields: 

  * **FIELD** The grade being kriged. 
  * **PANEL** Panel identifier copied from the IN2 file. 
  * **KRIGEST** The kriged estimate. 
  * **KRIGVAR** The kriging variance. 
  * **NUMSAM** The number of samples used to make the kriged estimate. 
  * **AREA** The area inside the panel. 
  * **SIMPTS** The number of simulated points inside the panel. 
  * **FVALUE** The average value of the variogram in the panel.

  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate of sample data in the IN file. |  IN |  Yes |  Numeric |  X  
Y |  Y coordinate of sample data in the IN file. |  IN |  Yes |  Numeric |  Y  
VALUE |  Field to be kriged in the **IN** file. |  IN |  Yes |  Numeric |  Undefined  
PANEL |  Panel identifier. This is a numeric field in the **IN2** file. Its name will often be **PVALUE**. |  IN2 |  Yes |  Numeric |  PVALUE  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NUGGET |  Nugget variance (0). |  No |  0 |  Undefined |  Undefined  
VAR1 |  Spatial variance (1). The difference between the nugget variance |  No |  1 |  Undefined |  Undefined  
RANGE1 |  The range of the variogram in direction 1.  Direction 1 is used for defining the anisotropy angle, [ **VGANGLE1**] , which is measured clockwise from the North.  Note: It does not matter whether direction 1 is the major or minor axis. |  No |  1 |  Undefined |  Undefined  
RANGE2 |  The range of the variogram in direction 2, perpendicular to direction 1. (1) |  No |  1 |  Undefined |  Undefined  
VGANGLE1 |  The angle between the N axis and direction 1, measured clockwise from N in degrees (0). |  No |  0 |  Undefined |  Undefined  
SEARCH |  Maximum search distance from centre of gravity of panel (9999). |  No |  9999 |  Undefined |  Undefined  
NMAX |  The maximum number of samples to be used.  |  No |  50 |  1,1900 |  Undefined  
NSIM |  The starting value for the number of simulated points in the X and Y directions for panel simulation. The default value of (20) means that the initial square grid has 20x20=400 points.  |  No |  20 |  Undefined |  Undefined  
MINSIM |  Minimum number of simulated points in panel. The default is (400). |  No |  400 |  Undefined |  Undefined  
VMETHOD |  Method for defining variogram parameters (1) |  Option |  Description  
---|---  
1 |  Use parameters **NUGGET , VAR1 , RANGE1 , RANGE2 ,** and **VGANGLE1**. This is consistent with earlier versions of **PANELK** and can be used for a single structure spherical model.  
2 |  Define parameters using interactive prompts. This method allows a selection of variogram models, defined using VGRAM.  
No |  1 |  1,2 |  1,2  
VGRAM |  Variogram model type (1). Possible values are: |  **Option** |  **Description**  
---|---  
**1** |  Single structure spherical model.  
**2** |  Two structure spherical model.  
**3** |  Linear model.  
**4** |  De Wijsian model.  
**5** |  Exponential model.  
**6** |  Gaussian model.  
**7** |  Experimental model.  
**8** |  NOT USED.  
**9** |  NOT USED.  
**10** |  Multi structure spherical model with anisotropy.  
No |  1 |  1,10 |  1,2,3,4,5,6,7,10  
PRINT |  Output control flag (1). |  **Option** |  **Description**  
---|---  
**0** |  Minimum output. Just a summary of the sample data and a table of results is output.  
**1** |  As 0 plus a summary of all input files, fields and parameters.  
**2** |  As 1 plus a listing of all simulated points, plus all samples and kriged weights.  
**3** |  As 2 plus a listing of panel points.  
No |  1 |  0.3 |  0,1,2,3  
  
Related topics and activities

  * [PANELEST Process](<panelest.md>)