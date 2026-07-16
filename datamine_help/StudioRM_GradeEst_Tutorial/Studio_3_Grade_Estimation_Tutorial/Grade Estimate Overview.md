![](../HeaderCell.jpg) |  Grade Estimation User Guide Grade Estimation processes and concepts.  
---|---  
  
#  ![](../Images/GE_MainPic.gif)

# Grade Estimation User Guide

The following topics are available:

## Grade Estimation Help Files

This section of the Help file deals with the processes and concepts involved in Grade Estimation. This is a complex and extensive subject, and for this reason the subject has been broken down into the following categories.

  * Introduction (this topic): introducing ESTIMA

  * [Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>): defining shape and orientation of search.

  * [Dynamic Search Volumes](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>): categorizing reserves based on the number of samples in a volume.

  * [Using Octants](<Grade%20Estimation%20Octants.md>): declustering samples to achieve an even spread.

  * [Key fields](<Grade%20Estimation%20Key%20Fields.md>): restricting the number of samples from any one borehole.

  * [The Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>): a table summarizing all fields required for a SV file.

  * [Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>): representing cells by a three-dimensional array of points.

  * [Estimation Methods](<Grade%20Estimation%20Methods.md>): an overview of the methods available to estimate grade, including:

  *     * [Nearest Neighbour](<Grade%20Estimation%20Nearest%20Neighbour.md>): more details on this grade estimation method.

    * [Inverse Power of Distanc](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>)e: more details on this grade estimation method.

    * [Kriging](<Grade%20Estimation%20Kriging.md>): more details on this grade estimation method.

    * [Sichel's T Estimator](<Grade%20Estimation%20Sichels%20T%20Estimator.md>): more details on this grade estimation method.

  * [The Estimation Parameter file](<Grade%20Estimation%20Parameter%20File.md>): a table summarizing all fields required for the Estimation Parameter file.

  * [Additional Features](<Grade%20Estimation%20Additional%20Features.md>): more functions of the grade estimation processes.

  * [Variograms](<Grade%20Estimation%20Variograms.md>): variogram models available for kriging. Also a table showing the fields required for the Variogram Model Parameter file.

  * [Run Time Optimization](<Grade%20Estimation%20Run%20Time%20Optimization.md>): minimizing the amount of time taken to run grade estimation processes.

  * [Rotated Models and Unfolding](<Grade%20Estimation%20Rotated%20Models.md>): how ESTIMA handles rotated data, and an overview of the unfolding process.

  * [Output and Results](<Grade%20Estimation%20Output%20and%20Results.md>): understanding the output files.

  * [Examples](<Grade%20Estimation%20Examples.md>): some useful examples that highlight how the ESTIMA process works.

  * [Parameters, Files and Fields Reference](<Grade%20Estimation%20Parameter%20Summary.md>): tables containing all required estimation fields and parameters.

  * [System Limits](<Grade%20Estimation%20System%20Limits.md>): information relating to the amount of data ESTIMA can process.

  * [Bibliography](<Grade%20Estimation%20References.md>): published articles relating to grade estimation.

At the end of each section, you can either use Related Topics to see the next topic in sequence, or click the Next Section button.

## Features of ESTIMA

The main features of ESTIMA are:

  * A consistent set of search volume and estimation parameters for all interpolation methods

  * Optimization of sample searching to improve speed

  * Multiple grades can be estimated in a single run

  * The same grade can be estimated by different methods

  * Different search volumes and estimation parameters can be used for the different grades

  * Rectangular or ellipsoidal search volume with anisotropy

  * A dynamic search volume allowing the volume to be increased if there are insufficient

  * samples

  * Restriction of the number of samples by octant and key field

  * Estimation by zone, with separate parameters for each zone

  * Wide selection of variogram model types for both normal and lognormal kriging

  * Automatic transformation of data if the input model is a rotated model

  * Unfolding option available for all estimation types

  * Parent cell estimation

  * Selective update of partial model

## Estimation Methods

The estimation methods provided by ESTIMA include:

  * Nearest Neighbor

  * Inverse Power of Distance

  * Ordinary Kriging

  * Lognormal Kriging

  * Simple Kriging

  * Sichel's t Estimator

## Overview of ESTIMA

ESTIMA requires an Input Prototype Model and a set of Sample Data as input. Usually the Input Prototype Model will already contain cells and sub-cells which represent, for example, a geological structure. In this case, grade values are interpolated into the existing set of cells and sub-cells. If however an empty prototype is specified (i.e. it does not contain any cells or sub-cells), ESTIMA will create cells and sub-cells in the area around the samples as defined by the search volume.

From here on any reference to a model cell will include both cells and sub-cells. A full cell is referred to as a parent cell.

The Sample Data file contains the data which is used to estimate cell grades. At a minimum, the data must include the X, Y and Z coordinates of each sample and at least one grade value. ESTIMA requires a search volume to be defined. This is the volume, centered on the cell being estimated, which contains the samples to be used for grade estimation. More than one search volume can be defined, so that different grades can have different search volumes. The parameters describing the search volume(s) are supplied to ESTIMA from the Search Volume Parameter file.

ESTIMA also requires a set of estimation parameters to be defined for each grade to be estimated. These parameters are also supplied to ESTIMA from a file called the Estimation Parameter file. It will include items such as the estimation method, the search volume reference number the power (for Inverse Power of Distance calculations). Each cell is selected in turn from the Input Prototype Model and the samples lying within the search volume are identified. Each grade specified in the Estimation Parameter file is estimated, and the results are written to the Output Model file.

A summary of the files used by ESTIMA is as follows:

Process |  Description  
---|---  
PROTO |  Input Prototype Model  
IN |  Sample Data  
SRCPARM |  Search Volume Parameters  
ESTPARM |  Estimation Parameters  
VMODPARM |  Variogram Model Parameters  
STRING |  Unfolding Strings  
MODEL |  Output Model  
SAMPOUT |  Sample Output  
  
Other information is supplied to the process as fields and parameters.

![](../Images/NextExercise.gif)[Proceed to the next section](<Concept_Grade%20Estimation%20and%20Interpolation.md>) (ESTIMATE overview)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>)[  
Grade Estimation Dynamic Search V](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>)olumes[  
Grade Estimation Octants](<Grade%20Estimation%20Octants.md>)[  
Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>)[  
Grade Estimation Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)[  
Grade Estimation Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>)[  
Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)[  
Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>)[  
Grade Estimation](<Grade%20Estimation%20Additional%20Features.md>)[Additional Features](<Grade%20Estimation%20Parameter%20File.md>)[  
Grade Estimation Variograms](<Grade%20Estimation%20Variograms.md>)[  
Grade Estimation Run Time Optimization](<../Process_Full_Descriptions/estima-d.md>)[  
Grade Estimation Rotated Models](<Grade%20Estimation%20Rotated%20Models.md>)[  
Grade Estimation Output and Results](<Grade%20Estimation%20Output%20and%20Results.md>)[  
Grade Estimation Examples  
Grade Estimation Parameter Summary](<Grade%20Estimation%20Examples.md>)[  
Grade Estimation System Limits  
Grade Estimation References  
  
ESTIMA command Help ](<Grade%20Estimation%20System%20Limits.md>)[  
ESTIMATE command Help](<../Process_Full_Descriptions/estimate-d.md>)[  
The Estimate dialog  
VARFIT Command Help](<EstimateDialog.md>)