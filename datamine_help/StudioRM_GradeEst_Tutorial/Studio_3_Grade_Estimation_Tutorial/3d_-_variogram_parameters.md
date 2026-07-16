# 3D - Variogram Parameters

![](../HeaderCell.jpg) |  Defining 3D Variogram Parameters Defining 3-dimensional variogram parameters for use in a grade estimation run.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process ESTIMATE to import and check a set of 3D variogram parameters.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the introductory page Variogram Models, in the Grade Estimation User Guide.

  * [Files](<tutorial_files.md>)required for the exercises on this page:

  *     * _uepv

##  Exercise: Importing Variogram Model Parameters Using ESTIMATE

In this exercise you are going to import a set of variogram model parameters that have been output from the variogram modeling process VARFIT. The set of variogram model parameters have the following general characteristics:

  * the set contains 12 sets of parameters i.e. one for each of the grade fields Cu, Ag, Au and Co for each of three grade zones (ZONE = 1, 2, 3)

  * the variograms have been modelled with 1 or 2 structure spherical models

  * the variogram models are omni-directional i.e. the same in all directions

  * record 5 i.e. for Cu zone 2 contains a set of dummy parameters.

![note.gif \(1017 bytes\)](../images/note.gif) |  When modeling experimental variograms using the process VARFIT, the resultant models are saved to a variogram model file using the standard Studio variogram model conventions. If you have modeled experimental variograms using a different programme, make sure that you use the correct transformations when converting the external modeling programme's model results into Studio's variogram model parameter format. As an example, check the conversions to the following Studio variogram parameters:

  * Variogram axes and angles of rotation
  * Nugget, Spatial Variance (i.e. Sill - Nugget) and Sill.

  
---|---  
  
## Importing An Existing Set of Variogram Model Parameters Using ESTIMATE

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Estimate | Interpolate Select  Models | Interpolation Processes | Interpolate Grades from Menu .

  3. In the Grade Estimation (ESTIMATE) dialog, Files tab, click Next.

  4. .In the Grade Estimation (ESTIMATE) dialog, Unfolding tab, click Next

  5. In the Search Volumes tab, click Next.

  6. In the Variogram Models tab, Index group, click Import.

  7. In the Project Browser dialog, Database Tables pane, All Tables folder, select the table _uepv , click OK.

  8. In the Index group, check that 12 variogram models are listed, as shown below:  
  
![](../Images/get_NewVariogramModelParamFileUsingESTIMATE%201.gif)

## Checking the Imported Variogram Model Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Variogram Models tab, Index group, select the 1:CU ZONE 1 item from the list.

  2. In the Rotation sub-tab, Variogram Rotation group, check that the rotation parameters are as shown below:  
  
![](../Images/get_NewVariogramModelParamFileUsingESTIMATE%202.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The SecondRotation Angle value is set to 0. This indicates that there is no rotation about the second variogram axis.  
---|---  
  3. In the Structures sub-tab, Structures group, check that the variogram structure parameters are as shown below:  
  
  
![](../Images/get_NewVariogramModelParamFileUsingESTIMATE%203.gif)  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  This variogram model has the following characteristics:
     * has a Nugget Variance of 0.01
     * consists of two spherical structures, indicated by the two records shown in the summary pane
     * the structures are anisotropic, indicated by the same values listed in the X Range, Y Range and Z Range columns
     * has a first and second spatial variance of 0.265 and 0.263 respectively.  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif)| 
     * The Rotation and Structures sub-tabs can be used to edit the variogram parameters.
     * These parameters would then need to be saved to the projects variogram model file by using the Export button in the Index group.  
---|---  

## Checking The Variogram Model Parameters Summary

  1. In the Grade Estimation (ESTIMATE) dialog, Variogram Models tab, Summary sub-tab, check that the variogram parameters for the first four models are as shown below:  
  
![](../Images/get_NewVariogramModelParamFileUsingESTIMATE%204.gif)  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  This Summary sub-tab is used to view and not edit parameter values.  
---|---  
  2. In the Grade Estimation (ESTIMATE) dialog, click Cancel. 

**![](../images/UpArrow.gif)**Top of page