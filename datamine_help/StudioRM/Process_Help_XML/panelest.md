# PANELEST Process

To access this process:

  * Model ribbon **> > Interpolate >> Panels**.

  * Enter "PANELEST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PANELEST** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PANELEST>).

## Process Overview

Estimate grade and variance of 2D and 3D panels.

Panels are defined either as a set of strings from file PERIM, or as a set of 2D or 3D [discretisation](<../STUDIO_RM/Grade%20Estimation%20Cell%20Discretisation.md>) points from file DISPTIN. The interpolation methods available are nearest neighbour, inverse power of distance or Kriging.

In particular the process allows you to estimate a grade and a Kriged variance for:

  * Any perimeter, without the need to create a block model.

  * A subset of cells from a block model.

See also [PANELK](<panelk.md>) Process.

### Using Strings

The **PERIM** file may contain one or more strings. If the strings are not closed the process will close them to form the panel. You must ensure that a string does not intersect itself as this will lead to incorrect results. String intersections are not checked by the process. There is a limit of 5000 points in any one string.

The strings must be planar and must lie in one of the three orthogonal planes. If a string does not satisfy both these criteria then a warning will be displayed and that string will not be evaluated. Although the strings must be in one of the three orthogonal planes, they do not all have to be in the same plane. 

You can define independent plus and minus projection distances using the parameters DPLUS and DMINUS in order to create a volume. If either of these values are non zero then the panel will be considered as a 3D panel; otherwise it is a 2D panel.

If a panel is 2D then all sample data will be projected onto the plane of the panel even if all three coordinates (X,Y,Z) are specified for the sample data. Hence the evaluation will be in 2D. If you are kriging a 2D panel then you must take care that projecting data onto the plane of the panel does not lead to coincident samples. The process will terminate with an error if there are coincident samples and kriging is used.

Each panel is represented by a set of 2D or 3D discretisation points. You can define the spacing between discretisation points independently in each of the three dimensions using the parameters XDSPACE, YDSPACE and ZDSPACE. Alternatively if you set these parameters to zero the process will calculate a suitable spacing between points. It does this by calculating the maximum extent of the panel in the two dimensions of its plane, and then calculating the corresponding area. This area is equivalent to a rectangle surrounding the panel. Taking the square root of the area gives the side of a square with the same area. The distance between points is then calculated by dividing the length of the side of this square by 10.5. In other words if the original panel were square it would contain 11 x 11 (=121) discretisation points. XDSPACE, YDSPACE and ZDSPACE are originally set to zero then they will all be assigned the same value, as described above, so that the discretisation points are regularly distributed.

A set of discretisation points are generated within the rectangle surrounding the panel, and then the points lying within the panel are selected. If it is a 3D panel then points are also generated in the third dimension, limited by the DPLUS and DMINUS values. The total number of discretisation points lying within the panel is calculated and is compared to the minimum number of points as defined by parameter MINDISC. If the number of points is less than MINDISC then the spacing in each dimension is multiplied by 0.8, a new set of points is generated, and the total is again compared to MINDISC. This procedure is repeated until the total exceeds MINDISC. If insufficient points are found after 10 iterations then a warning message is displayed and the panel is not estimated. If this happens then reduce the spacing, and/or MINDISC, and try again.

If parameter PRINT=2 then the coordinates of the discretisation points will be displayed in the Output window. If PRINT=2 and ECHO=1 then the points will also be written to the print file. If the points are required for further analysis within Datamine, they can be imported directly from the print file.

### Using Points

Instead of generating the discretisation points from strings, as defined above, you can input the discretisation points directly using the DISPTIN file. In this case the parameters XDSPACE, YDSPACE, ZDSPACE, MINDISC, DPLUS and DMINUS are ignored. One method of creating the points could be to use the [TRIFIL](<trifil.md>) process to create a set of cells within an enclosed wireframe or below a DTM. The centre points of the model cells would then be the discretisation points, and so the panel would represent the volume within the wireframe or below the DTM. The output model from **TRIFIL** can be input directly to PANELEST as the DISPTIN file, specifying the **XPT** field as XC, YPT as YC and ZPT as ZC. It is recommended that if you use **TRIFIL** to create the discretisation points then you should not allow any subcelling, so that the points are on a regular grid.

The discretisation points could also be the cell centres of an existing model for which you have already interpolated grade. By selecting a subset of the cells, or the total model, you can estimate a single kriged grade and in particular a single kriged variance for that subset of cells. If the model contains subcells then it would be best to regularise the model first, so that the points are on a regular grid.

### Sample Selection

The MINNUM and MAXNUM parameters allow you to select the minimum and maximum number of samples to be used for making each estimate. For Nearest Neighbour and Inverse Power of Distance there is no limit on MAXNUM. However for kriging MAXNUM must not exceed 1399.

If less than MINNUM samples are found then the panel will not be estimated. If there are more than MAXNUM, then the number is reduced until only MAXNUM remain. This is done by calculating the distance of each sample from the nearest discretisation point. The samples are then sorted according to this distance, and the MAXNUM samples with the smallest distances are selected.

If panels are defined using the PERIM file, then setting parameter INSIDE=1 will ensure that only samples which lie within the panel are used for the grade estimate; if INSIDE=0 then all samples will be considered. If panels are defined using the DISPTIN file, then the parameter **INSIDE** is ignored.

### Grade Estimation Method

The IMETHOD parameter allows you to select the estimation method. 

See [Nearest Neighbour](<../STUDIO_RM/Grade%20Estimation%20Nearest%20Neighbour.md>), [kriging](<../STUDIO_RM/Grade%20Estimation%20Kriging.md>) and [Inverse Power of Distance](<../STUDIO_RM/Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>).

  1. Nearest Neighbour.

For each discretisation point the nearest sample is found. The panel estimate is then the arithmetic mean over all discretisation points. The reported variance is the classical statistical variance of all selected samples.

  2. Inverse Power of Distance.

Each discretisation point is estimated using inverse power of distance, where the power is defined by parameter POWER. The panel estimate is then the arithmetic mean over all discretisation points. The reported variance is the classical statistical variance of all selected samples.

  3. Kriging. 

If parameter **LOG** =0 then normal kriging is used. If **LOG** =1 then log kriging is used, and the following conditions apply:  
\- General Case method  
\- a maximum of 3 iterations  
\- convergence tolerance is set at 0.01  
\- the kriged estimate is used as the mean value for the lognormal variance calculation.

If Kriging is selected then the reported variance is the Kriged variance. Note that this is different from Nearest Neighbour and Inverse Power of Distance which report the classical statistical variance of the selected samples.

### Anisotropy

If Kriging is selected then [anisotropy](<../STUDIO_RM/Dynamic%20Anisotropy%20-%20Introduction.md>) is defined by the parameters of the [variogram model](<../STUDIO_RM/Grade%20Estimation%20Variograms.md>). 

For Nearest Neighbour or Inverse Power of Distance anisotropy is defined using the ANANGLEn, ANAXISn and ANDISTn parameters.

### Totals and Averages

If parameter **TOTAL** =1 and more than one panel has been estimated, then the total area and/or volume and the average grade, weighted by area or volume will be reported in the Output window and saved to the OUT file. The total variance will only be reported if kriging has been used. It is calculated as the weighted average of the individual kriged variances, weighted by the square of the corresponding area or volume. In calculating the total variance it is therefore assumed that the estimates and variances of the individual panels are independent of one another. This will often be a reasonable assumption if the panels are large.

If the panels are defined using the **DISPTIN** file then the volume of each panel must be estimated. This is done by finding the minimum distance between [discretisation](<../STUDIO_RM/Grade%20Estimation%20Cell%20Discretisation.md>) points in each of the X, Y and Z directions and calculating the corresponding volume of influence of a point. The volume of the panel is then the volume of influence of a point multiplied by the number of points. This will give an accurate estimate of volume if the points are on a regular grid, but not otherwise.

### Average Sample-Panel Variogram Value

As described above, if kriging is used then the average variogram value of each selected sample with the panel is written to the sample output file **SAMPOUT**. Sometimes these values are required for further processing and the kriged estimate and variance are not required. The run time is then very much quicker if parameter **VGONLY** is set to 1, so that the kriged estimate and variance are not calculated. Another advantage is that the maximum number of samples per panel in the **SAMPOUT** file is increased from 1,399 to 50,000.

### Timing

The execution speed of the process increases as the number of samples increases and also as the number of discretisation points increases. Also Kriging is significantly slower than Inverse Power of Distance.

### Results

The results for each panel are displayed in the **Output** window. If [kriging](<../STUDIO_RM/Grade%20Estimation%20Kriging.md>) has been selected and PRINT=1 then the panel F value (the variance of a point in the panel) and the Lagrange multiplier are also displayed. There are two output files, both of which are optional, examples of which are also shown below. The OUT file contains a single record for each panel, summarising the results. The SAMPOUT file shows the weight assigned to each sample for each panel. If kriging is used the **SAMPOUT** file also includes the average variogram value of the sample with the panel.

## Input Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
IN| Input sample data file. This must contain the fields **X , Y** , and **VALUE**. Note: A **Z** field is also required for 3D panels.| Input| Yes| Undefined  
VMODPARM| Variogram model parameter file.| Input| No| Variogram - Model  
PERIM| The input string file. This must contain the 5 fields **PANEL , PTN , XP , YP , ZP** . The strings may be open or closed, but must be planar and must lie in one of the three orthogonal planes. Either a PERIM file or a DISPTIN file must be specified.| Input| No| String  
DISPTIN| The input file containing discretisation points. This must include the 3 fields **XPT , YPT , ZPT** A fourth field **PANEL** is optional, and is used to identify different sets of discretisation points representing different panels. Either a **PERIM** file or a **DISPTIN** file must be specified.| Input| No| Point Data  
  
## Output Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
OUT| The output results file, containing a record for each panel estimated. The fields include the panel identifier, the estimated grade, the variance, and other associated information.| Output| No| Undefined  
SAMPOUT| The sample output file. This will contain the samples used to estimate each panel, and the weight assigned to each sample.| Output| No| Undefined  
  
## Fields

Name| Description| Source| Required| Type| Default  
---|---|---|---|---|---  
X| X coordinate of sample data in the IN file.| IN| Yes| Numeric| X  
Y| Y coordinate of sample data in the IN file.| IN| Yes| Numeric| Y  
Z| Z coordinate of sample data in the IN file.| IN| No| Numeric| Z  
VALUE| Field to be estimated in the IN file.| IN| Yes| Numeric| Undefined  
PANEL| Panel identifier. This is a numeric or alpha field (max 40 characters) in the **PERIM** or **DISPTIN** file. If a perimeter file is used then the **PVALUE** field may be used.| PERIM,DISPTIN| No| Numeric| PVALUE  
XPT| X coordinate of discretisation points in the **DISPTIN** file.| DISPTIN| No| Numeric| Undefined  
YPT| Y coordinate of discretisation points in the **DISPTIN** file.| DISPTIN| No| Numeric| Undefined  
ZPT| Z coordinate of discretisation points in the **DISPTIN** file.| DISPTIN| No| Numeric| Undefined  
  
## Parameters

Name| Description| Required| Default| Range| Values  
---|---|---|---|---|---  
MINNUM| Minimum number of samples for panel to be estimated.(1).| No| 1| 1,+| Undefined  
MAXNUM| Maximum number of samples for panel to be estimated. If Kriging is selected then the maximum cannot exceed 1399.| No| 100| 1,+| Undefined  
INSIDE| If set to 1 samples must lie inside panel. This only applies if a **PERIM** file has been specified.| No| 1| 0,1| 0,1  
XDSPACE| The distance between discretisation points in X. If set to zero then a suitable spacing will be generated automatically.| No| 0| Undefined| Undefined  
YDSPACE| The distance between discretisation points in Y. If set to zero then a suitable spacing will be generated automatically.| No| 0| Undefined| Undefined  
ZDSPACE| The distance between discretisation points in Z. If set to zero then a suitable spacing will be generated automatically.| No| 0| Undefined| Undefined  
MINDISC| Minimum number of discretisation points in panel before it can be estimated.| No| 50| 1,+| Undefined  
DPLUS| Perimeter projection distance measured in the increasing direction of the perpendicular axis.| No| 0| 0,+| Undefined  
DMINUS| Perimeter projection distance measured in the decreasing direction of the perpendicular axis.| No| 0| 0,+| Undefined  
IMETHOD| Interpolation method: 1 - nearest neighbour 2 - inverse power of distance 3 - ordinary kriging| No| 3| 1,3| 1,2,3  
VMODNUM| Variogram model reference number as defined by the **VREFNUM** field in the **VMODPARM** file. (1).| No| 1| Undefined| Undefined  
LOG| Flag to indicate whether log kriging is selected. 0 = ordinary kriging 1 = log kriging| No| 0| 0,1| 0,1  
POWER| Power for inverse power of distance method.| No| 2| Undefined| Undefined  
TOTAL| If **TOTAL** is set to 1 then values for the total volume and area over all panels will be reported and saved to the **OUT** file. If kriging is selected then the average variance will be calculated as the weighted average of the individual variances, weighted by the square of the area or volume.| No| 0| 0,1| 0,1  
VGONLY| Flag controlling estimation (0).| **Option**| **Description**  
---|---  
**0**|  \- Calculate estimated grade and variance for each panel.  
**1**|  \- Only create the sample output file. Do not calculate estimated grade and variance.  
No| 0| 0,1| 0,1  
ANANGLE1| First rotation angle for defining anisotropy when nearest neighbour or inverse power of distance methods are selected ie **IMETHOD** = 1 or 2.| No| 0| -360, 360| Undefined  
ANAXIS1| First rotation axis for defining anisotropy when nearest neighbour or inverse power of distance methods are selected ie **IMETHOD** = 1 or 2. This parameter has a value 1 for rotation about the X axis, 2 for rotation about the Y axis, and 3 for rotation about the Z axis. If it is set to 0 then there will be no rotation, irrespective of the value of **ANANGLE1**.| No| 3| 0,3| 0,1,2,3  
ANANGLE2| Second rotation angle for defining anisotropy when nearest neighbour or inverse power of distance methods are selected, that is,**IMETHOD** = 1 or 2.| No| 0| -360, 360| Undefined  
ANAXIS2| Second rotation axis for defining anisotropy when nearest neighbour or inverse power of distance methods are selected ie **IMETHOD** = 1 or 2. This parameter has a value 1 for rotation about the X axis, 2 for rotation about the Y axis, and 3 for rotation about the Z axis. If it is set to 0 then there will be no rotation, irrespective of the value of **ANANGLE2**.| No| 1| 0,3| 0,1,2,3  
ANANGLE3| Third rotation angle for defining anisotropy when nearest neighbour or inverse power of distance methods are selected, that is **IMETHOD** = 1 or 2.| No| 0| -360, 360| Undefined  
ANAXIS3| Third rotation axis for defining anisotropy when nearest neighbour or inverse power of distance methods are selected ie **IMETHOD** = 1 or 2. This parameter has a value 1 for rotation about the X axis, 2 for rotation about the Y axis, and 3 for rotation about the Z axis. If it is set to 0 then there will be no rotation, irrespective of the value of **ANANGLE3**.| No| 3| 0,3| 0,1,2,3  
ANDIST1| Anisotropy distance measured along rotated X axis, when nearest neighbour or inverse power of distance methods are selected ie **IMETHOD** = 1 or 2. This corresponds to the range of influence in that direction.| No| 1| 0.0001,+| Undefined  
ANDIST2| Anisotropy distance measured along rotated Y axis, when nearest neighbour or inverse power of distance methods are selected ie **IMETHOD** = 1 or 2. This corresponds to the range of influence in that direction.| No| 1| 0.0001,+| Undefined  
ANDIST3| Anisotropy distance measured along rotated Z axis, when nearest neighbour or inverse power of distance methods are selected, that is **IMETHOD** = 1 or 2. This corresponds to the range of influence in that direction.| No| 1| 0.0001,+| Undefined  
PRINT| Output control flag (1).| **Option**| **Description**  
---|---  
**0**|  Minimum output. This includes a summary of the input data and the results.  
**1**|  As 0 plus Lagrange multiplier and panel F value  
**2**|  As 1 plus a listing of discretisation points.  
No| 1| 0,2| 0,1,2  
  
## Example
    
    
    !panelest &IN(holes.c),&VMODPARM(VMODEL),&DISPTIN(points),  
  
---  
      
    
    &OUT(RESNEW),&SAMPOUT(sampout),*X(X),*Y(Y),*Z(Z),*VALUE(Fe),  
      
    
    *PANEL(AZONE),@MINNUM=1,@MAXNUM=1399,@INSIDE=0,@XDSPACE=0,  
      
    
    @YDSPACE=0,@ZDSPACE=0,@MINDISC=20,@DPLUS=0,@DMINUS=0,  
      
    
    @IMETHOD=3,@VMODNUM=1,@LOG=0,@POWER=2,@TOTAL=1,@ANANGLE1=0,  
      
    
    @ANAXIS1=3,@ANANGLE2=0,@ANAXIS2=1,@ANANGLE3=0,@ANAXIS3=3,  
      
    
    @ANDIST1=1,@ANDIST2=1,@ANDIST3=1,@PRINT=0,@VGONLY=0  
  
Related topics and activities

  * [Cell Discretisation](<../STUDIO_RM/Grade%20Estimation%20Cell%20Discretisation.md>)

  * [Grade Estimation Methods](<../STUDIO_RM/Grade%20Estimation%20Methods.md>)

  * [Nearest Neighbour](<../STUDIO_RM/Grade%20Estimation%20Nearest%20Neighbour.md>)

  * [Kriging](<../STUDIO_RM/Grade%20Estimation%20Kriging.md>)

  * [Variograms](<../STUDIO_RM/Grade%20Estimation%20Variograms.md>)

  * [Advanced Estimation & Variography](<../STUDIO_RM/Multivariate_Introduction.md>)

  * [Dynamic Anisotropy with ESTIMA](<../STUDIO_RM/Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [PANELK Process](<panelk.md>)