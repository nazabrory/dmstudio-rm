# Dynamic Anisotropy with ESTIMA

**Note** : **[COKRIG](<../Process_Help_XML/cokrig.md>)** also provides Dynamic Anisotropy support. See [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

The [ESTIMA](<../Process_Help_XML/estima.md>) command is a comprehensive process for interpolating grades into a block model. It uses a search volume, centred on each block in turn, in order to select samples to be used for estimation by one of several methods. The search volume is usually a 3D ellipsoid, which is defined by the length and orientation of its three axes. The continuity of mineralization often varies with direction and so the search ellipsoid should be oriented to follow the direction of the mineralization. In addition the anisotropy weighting for the estimation methods should also follow the direction of mineralization. 

In earlier releases of Studio, several techniques were available to allow the search volume to be oriented appropriately, but in general they were approximations which required complex data manipulation. It can be shown that a misalignment of only a few degrees can cause the extrapolation of ore into waste and waste into ore, so it is very important to get the orientation of the search volume and estimation parameters correctly aligned.

The exception to the approximation methods is the UNFOLD option, which provides an exact solution to the problem of estimating grade in folded and deformed orebodies, and has proved to be a very useful tool in complex situations. However the Unfold solution often requires the user to create a detailed set of strings to define the folding, which can be a time consuming task. 

The dynamic anisotropy (DA) option in **ESTIMA** allows the anisotropy rotation angles for defining the search volume and variogram models to be defined individually for each cell in the block model. Thus, the search volume is oriented precisely and follows the trend of the mineralization. However this is only part of the solution as the rotation angles need to be assigned to each cell in the model in the first place. 

Your application offers two processes that facilitate the preparation of data for dynamic anisotropy modelling, providing an easy to use and precise method of calculating the anisotropy angles:

  * ANISOANG: provided to calculate dip and dip direction angles from string and wireframe data. These angles can be interpolated into the block model using [ESTIMA](<../Process_Help_XML/estima.md>).

  * APTOTRUE: if the dip angle is the apparent dip, then this process is available to convert from apparent dip angle to true dip angle.

Note: COKRIG also offers DA support. See 

This following topics assume that you are familiar with [grade estimation](<Grade%20Estimate%20Overview.md>) methods in general and in particular with the [ESTIMA](<../Process_Help_XML/estima.md>) process in Studio.

Related topics and activities

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

  * [Dynamic Anisotropy (ESTIMA) - Ellipsoid and Orientation](<Dynamic%20Anisotropy%20-%20Ellipsoid%20and%20Orientation.md>)

  * [Dynamic Anisotropy (ESTIMA) - Creating a Study](<Dynamic%20Anisotropy%20-%20Creating%20a%20Study.md>)

  * [Dynamic Anisotropy - Dip and Dip Direction](<Dynamic%20Anisotropy%20-%20Dip%20and%20Dip%20Direction.md>)

  * [Dynamic Anisotropy (ESTIMA) - Interpolating Angles](<Dynamic%20Anisotropy%20-%20Interpolating%20Angles.md>)

  * [Dynamic Anisotropy - True Dip Angles](<Dynamic%20Anisotropy%20-%20True%20Dip%20Angles.md>)

  * [Dynamic Anisotropy (ESTIMA) - Estimating Grade](<Dynamic%20Anisotropy%20-%20Estimating%20Grade.md>)

  * [Dynamic Anisotropy (ESTIMA) - Example 1](<Dynamic%20Anisotropy%20-%20Example%201.md>)

  * [Dynamic Anisotropy (ESTIMA) - Example 2](<Dynamic%20Anisotropy%20-%20Example%202.md>)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [ESTIMA](<../Process_Help_XML/estima.md>)   
[Grade Estimation Introduction](<Grade%20Estimate%20Overview.md>)