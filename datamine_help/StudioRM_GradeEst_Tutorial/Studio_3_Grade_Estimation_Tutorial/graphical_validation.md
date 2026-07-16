![](../HeaderCell.jpg) |  Visual Validation Validating the estimated block model cell grades using graphical methods.  
---|---  
  
# Overview

In this portion of the tutorial you are going to validate the estimated block model cell grades by generating and inspecting a Q-Q plot of the block model and the drillhole grades. This will be done using the process PPQQPLOT.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the full process description for PPQQPLOT.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _udhz5c

    * _ubm5g

![note.gif \(1017 bytes\)](../images/note.gif) |  What is a Q-Q Plot? In the grade estimation context, the QQ plot is a plot of the quantiles of two grade distributions against each other i.e. of quantiles of a particular grade field from one data set (e.g. block model cells - the estimates) against the quantiles (for the same grade field) from another data set (e.g. composited drillholes - the ). A quantile is defined as the fraction (or percent) of the number of data points below the given value. For example, the 0.2 (or 20%) quantile is the point at which 20% percent of the data fall below and 80% fall above that value.  If the two sets come from populations with the same probability distributions, then the plotted points should fall along the 45 degree reference line.  
---|---  
  
##  Exercise: Graphical Validation of Block Model Grade Estimates using Q-Q Plots

In this exercise you are going to graphically validate the AU grade block model cell estimates for the cyan ore zone (ZONE=1). This will be done by generating and inspecting a Q-Q plot of the AU grade field in the 5m composited drillhole samples vs the 5x5x5m block model cells:

  * First Input file: 5m regular celled block model

  * Second Input file: 5m composited drillhole samples

  * Grade field: AU (g/t)

  * Zone field: ZONE (values 1, 2 and 3).

The grades were estimated using the Search, Variogram and Estimation parameter files _ueps,_uepv and _uepe respectively.

The 3D grade block model and drillhole samples are shown in the image below.  

![](../Images/get_StatsValidation%201.GIF)   

![note.gif \(1017 bytes\)](../images/note.gif) |  In the above image, the block model cells are colored according to three separate mineralization zones (cyan: ZONE=1, green: ZONE=2, red: ZONE=3). The fold axis of the ore body plunges at 35 degrees towards the East, the tabular to massive shaped limbs have a dip of 40 degrees, a maximum down dip length of 240m and a thichkness (perpendicular to the bottom contact) of 5m -45m . The drillholes are set in fans which are parallel with the dip direction of each limb and are spaced 50m apart .tom contact) of between 5 and 45m . The drillholes are set in fans which are parallel with the dip direction of each limb and are spaced approximately 50m apart.  
---|---  
  
![](../Images/Tip.gif) |  Use Q-Q Plots to check for:

  * bias in the estimates.

  
---|---  
  
## Generating the QQ Plot

  1. Activate theSample Analysisribbon and selectCharts | PP and QQ Plots

  2. In the PPQQPLOT dialog, Files tab, Input files group, set IN1* by browsing for and selecting the drillholes file _udhz5c.

  3. Set IN2* by browsing for and selecting the block model file _ubm5g.

  4. In the Output files group, define a new QQOUT output file 'qqouAU' and a new QQPLOT file 'qqplAU'.

![](../Images/get_GraphValidationQQPlot%202.gif)   

  5. In the Fields tab, select the VALUE1* field [AU], the VALUE2* field [AU].

  6. Select the KEY* field [ZONE].  
  
![](../Images/get_GraphValidationQQPlot%203.gif)  

  7. In the Paramaters tab, define the settings shown below, click OK.  
  
![](../Images/get_GraphValidationQQPlot%204.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The minimum (MINIMUM1, MINIMUM2) and maximum (MAXIMUM1, MAXIMUM2) values displayed on the plot axes are automatically generated if not defined by the user.  
---|---  
  8. In the Command control bar, check that the PPQQPLOT process has run to completion:  
  
![](../Images/get_GraphValidationQQPlot%205.gif)

## Viewing the Q-Q Plot

  1. Select the Graphics window and check that your plot is as shown below (your background and symbol colors will probably be different to those shown below):  
  
![](../Images/get_GraphValidationQQPlot%206.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * The block model quantiles are plotted on the Y-axis and the drillhole quantiles on the X-axis.
     * The symbols represent the three mineralization zones as follows:
     *        * + ZONE = 1
       * x ZONE = 2
       * ^ ZONE = 3 (triangles).  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  Using the Q-Q Plot for validating grade estimates:
     1.         * the plotted points (i.e. model cells vs drillhole composites) should deviate as little as possible from the 1:1 line shown on the graph
        * deviation away from the 1:1 line indicates bias in the estimates.  
---|---  

## Viewing a Q-Q Plot File

  1. In the Project Files control bar, expand the Plot Files folder.

  2. Right-click on the plot file qqplau and select Display .

  3. Select the Graphics window and check that your plot is as shown below (your background and symbol colors will probably be different to those shown below):  
  
![](../Images/get_GraphValidationQQPlot%206.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The 'BEEP' sound within the Graphics window can be temporarily disabled as follows:

  * Right-click the Volume icon in the windows Taskbar.
  * Select Open Volume Control.
  * In the Volume Control dialog, Volume Control group, check the Mute All tick box.
  * Click Close.

  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  As an alternative to generating (and then viewing) plots from PPQQPLOT, the output data file qqouAU can be used to create a scatter plot in the Plots window (Insert | Chart | Scatter Plot). The VALUE1 field is selected for the X Axis and the VALUE2 field for the Y Axis, with ZONE being used as the Key Field:  
  
![](../Images/get_GraphValidationQQPlot%207.gif)  
---|---  
  
**![](../images/UpArrow.gif)**Top of page