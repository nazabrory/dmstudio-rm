![](../HeaderCell.jpg) |  Grade Estimation Tutorial Introduction to the Grade Estimation Tutorial  
---|---  
  
# Grade Estimation Tutorial

![](../Images/GE_MainPic.gif)

This tutorial introduces you to the key features used for grade estimation. Typically 'grades' are estimated into the cells of a geological block model in order to generate a resource block model, which would then be used as input into the ore reserve optimisation or generation process of a mine planning cycle. Alternatively, 'grades' can estimated using panel (mining block) outlines and results saved to a results table, without creating a block model.

![note.gif \(1017 bytes\)](../Images/note.gif) |  'Grades' are typically concentrations of the minerals or elements of interest. The use of the grade estimation techniques is not restricted to mineral or element concentrations but can also be used to estimate other numerical properties or attributes of interest e.g. layer, rock mass or material properties; geochemical, geomechanical or metallurgical properties.   
---|---  
  
This tutorial covers techniques for both 2- and 3-dimensional estimation exercises. The input for a grade estimation exercise typically uses the results from a geostatistical analysis in order to define mineralization zones and their associated grade estimation parameters.

This tutorial includes introductory sections, procedures and exercises covering the following topics:

  * Defining grade estimation parameters (in both 2D and 3D)

  * Basic estimation tools and techniques

  * Advanced estimation tools and techniques

  * Evaluation and reporting (generation of summary tonnes and grades)

  * Presentation of grade estimation data e.g. as plan plots

## The Main Grade Estimation Processes

Grades are typically estimated for individual block model cells, although grades can also be estimated directly for panels (mining blocks) defined by closed strings or perimeters. The following processes are used to estimate grades:

  * GRADE \- basic grade estimation process, with the following key features:

  *     * estimation into block model cells

    * search, variogram model and estimation parameters input as process parameters

    * single grade estimates

    * a subset of estimation methods

  * ESTIMA \- advanced grade estimation process, with the following features:

  *     * estimation into block model cells

    * search, variogram model and estimation parameters input as process parameters or parameter files

    * can be recorded into a macro or script

    * the full set of estimation methods

  * ESTIMATE \- dialog controlled, advanced grade estimation process, with the following key features:

  *     * estimation into block model cells

    * controlled via interactive dialogs

    * calculation of multiple simultaneous grade estimates

    * search, variogram and estimation parameters stored in tables

    * the full set of estimation methods

    * advanced features

  * PANELEST \- panel grade estimation process, with the following key features:

  *     * estimation of panel outlines (strings) output to a results table

    * can be recorded into a macro or script

    * panels defined by input closed strings or perimeters file

## Grade Estimation Methods

The following grade estimation methods are available in Studio RM:

  * Nearest neighbour

  * Inverse Power Distance

  * Ordinary Kriging

  * Simple Kriging

  * Indicator Estimation

  * Sichel's T.

## Grade Estimation Inputs

The inputs to the above processes typically include a sample file, block model, search volume parameters, variogram model parameters (if a kriging estimation method is used), estimation parameters and panels (if the panel grade estimation process is used). Parameters are stored in parameter files or as parameters within each process. These are summarized below:

### Samples

Sample grades can be point data or drillholes.

### Block Model

All the block model grade estimation methods require a prototype block model to interpolate the sample grades into.

If the specified prototype model already contains cells and subcells, e.g. a geological block model, then grade values will be interpolated into the existing cells. If it is empty, however, then cells and subcells will be created if there are sufficient samples within the search volume.

### Search Volume

A search volume ellipsoid defines the spatial limits and associated parameters used for selecting which samples are to be used when estimating grades into a block model cell; this search volume and its parameters will be the same for each cell in a particular zone and is centered on the cell being estimated.

More than one search volume may be defined e.g. for zonal control or for different grade fields.

### Variogram Models

Variogram model parameters are defined according to a particular standard and are stored either in a parameter file e.g. as output from the VARFIT variogram modeling process, or as parameters within the process. The following variogram models are available.

  * Spherical (single or multiple structures)

  * Power

  * Exponential

  * Gaussian

  * De Wijsian.

### Panels

Panels are stored as closed strings (perimeters) within a strings file and are required for the PANELEST process. Perimeters need to be coplanar and define the limits of each panel whose grade is to be estimated.

### Estimation Parameters

It is necessary to provide a set of estimation parameters for each grade to be estimated. These parameters may be stored as a parameter file, or they can be defined as parameters within the process. The parameters should include items such as the estimation method, the search volume reference number and variogram reference number (if a kriging estimation method is used).

## Grade Estimation Outputs

The output from a block model grade estimation method is a grade block model which contains values for each estimated grade field. Additional output fields may include estimation variance, number of samples and search volume information. These additional fields can be used for the determination of confidence limits for the grade estimates or for controlling detailed evaluations. Detailed or summary evaluations can be performed on these grade block models to generate tonnage-grade reports.

In the case of the panel estimation process, the output is a results file i.e. a summary tonnage-grade report.

Copyright © Datamine Corporate Limited  
JMN_MF_016