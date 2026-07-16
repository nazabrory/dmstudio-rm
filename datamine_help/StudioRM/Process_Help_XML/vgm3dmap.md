# VGM3DMAP Process

To access this process:

  * Enter "VGM3DMAP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **VGM3DMAP** and click **Run**.

  * This process is accessed using the **[Advanced Estimation](<../STUDIO_RM/Multivariate_Introduction.md>)** wizard.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_V.md#VGM3DMAP>).

## Process Overview

VGM3DMAP is used to interpolate experimental variogram values into a 3D map (represented by a block model).

It is used during the [Investigate Anisotropy](<../STUDIO_RM/Multivariate_Investigate_Anisotropy.md>) phase of Advanced Estimation, although can also be used as a standalone process to output a 3D map block model (3DMAP) and an optional file containing the experimental variograms used to generate the map.

The variogram block model is in standard Datamine block model format. It consists of a 3D matrix of cubic parent cells with the centre of the model assigned the coordinates of 0, 0, 0. The variogram values that are estimated into the model show how the variance increases (correlation decreases) as a function of distance and orientation from the centre point. Viewing planar slices through the centre point allows anisotropy to be identified showing where the correlation between samples differs in different directions. This analysis helps to identify the directions of the axes of the model variogram to be fitted.

### 3D Variogram Block Model

The &3DMAP file will contain the interpolated output variogram block model values It will include a field for the variogram value for each grade as specified by the *Gi fields.

The model file also includes a field showing the weighted average number of sample pairs used to calculate each variogram value. This is calculated by interpolating the number of sample pairs used to create each grade variogram value using the same inverse distance method and parameters as for the grade variogram. The name of this field in the output model is created by combining the grade field name followed by the characters "_N". Applying a legend to this value will show the spatial distribution of the density of information on model sections.

The model can be viewed in the 3D window using all the standard model display options. However it is not currently possible to load it into the Variograms window to view orthogonal sections through the model. 

There is a choice of methods to generate the data used for interpolation to create the 3D variogram model. If GRIDMODE=0 then standard angular experimental variograms are calculated radiating from a centre point at different azimuths and dips. Each lag point along every variogram vector has two data items the variogram value and the number of sample pairs.

If GRIDMODE=1 then the volume around the centre point is divided into a 3D set of cubes. The size of the cubes is defined by the lag distance. Every pair of samples is assigned to one of the cubes based on the azimuth, dip and length of the joining vector. The weighted average variogram value for each cell is assigned to a location within the cell, calculated as a weighted average position of the sample vectors within it. In this way the average variogram value and the number of samples can be calculated for each cell.

The difference between the two GRIDMODE settings is therefore the spatial location of the variogram values and the sample number data. Whichever method is selected these two data items are interpolated into the 3D variogram model using the inverse power of distance method. GRIDMODE=1 is applied when the Investigate Anisotropy option is run from the Advanced Estimation screen.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SAMPLES |  A Datamine file that contains sample positional information and supporting attributes. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
3DMAP |  Output |  Yes |  Undefined |  The output block model file containing the interpolated variogram value for each grade.  
VGRAM |  Output |  No |  Undefined |  Optional output experimental variograms used to create the 3D interpolated variogram. Requires GRIDMODE = 0.  
  
## Fields

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
XPT/YPT/ZPT |  X/Y/Z coordinate of sample data in the SAMPLE file. |  Yes |  XPT/YPT/ZPT |  Undefined |  Undefined  
G1-20 |  Grade fields for variogram calculation. At least G1 must be specified. |  Yes (G1) No (G2-20) |  Undefined |  Undefined |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NBLOCKS |  The number of blocks along each axis for the output variogram block model. A greater number of blocks will result in a finer grid but will require longer calculation times. |  Yes |  40 |  Undefined |  Undefined  
MAXLAG |  The maximum distance between pairs of samples to be considered for variogram calculation. |  Yes |  Undefined |  Undefined |  Undefined  
NLAGS |  The number of lags used to calculate experimental variograms. It is recommended that this value is less than **NBLOCKS**. The incremental lag distance is then calculated as **MAXLAG** / **NLAGS**. |  Yes |  25 |  1,200 |  Undefined  
NANGLES |  The number of angles (directions) for experimental variogram calculation. The increment between directions for both azimuth and dip is then calculated as 180 / **NANGLES** degrees. A greater number may allow more structure to be revealed in the resulting variogram map. This is not used for **GRIDMODE** =1. |  Only if **GRIDMODE** =0 |  9 |  1,180 |  Undefined  
GRIDMODE |  If set to 1 a regular grid is used to calculate experimental variogram values to be interpolated into the output variogram map. If set to 0 standard directional variograms are used. |  Yes |  0 |  0,1 |  0,1  
DISC |  The number of discretization points in X, Y and Z used for inverse distance interpolation of the variogram map. |  No |  3 |  1,10 |  Undefined  
MINSAMP |  The minimum number of experimental variogram points to be found within the search radius when performing inverse distance interpolation of the variogram block model. |  No |  1 |  1,10 |  Undefined  
OPTSAMP |  The optimum number of experimental variogram points to be found within the search radius when performing inverse distance interpolation of the variogram map. |  No |  50 |  1,100 |  Undefined  
SEARCHLF |  The radius of the initial search sphere for each interpolated variogram map point as a factor of the lag distance. |  No |  2 |  0,100 |  Undefined  
SEARCH2F |  The factor of the search sphere relative to the second search sphere. |  No |  1 |  0,100 |  Undefined  
SEARCH3F |  The factor of the search sphere relative to the second search sphere. |  No |  1 |  0,100 |  Undefined  
INVDISTP |  The inverse distance power used when performing inverse distance interpolation of the variogram map. |  No |  1 |  0,100 |  Undefined  
  
Related topics and activities

  * [Advanced Estimation & Variography](<../STUDIO_RM/Multivariate_Introduction.md>)