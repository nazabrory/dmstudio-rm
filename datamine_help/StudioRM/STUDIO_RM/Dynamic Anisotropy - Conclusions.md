# Dynamic Anisotropy (ESTIMA): Conclusions

**Note** : **[COKRIG](<../Process_Help_XML/cokrig.md>)** also provides Dynamic Anisotropy support. See [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

  * The **Dynamic Anisotropy** option in [ESTIMA](<../Process_Help_XML/estima.md>) allows the rotation angles for the search volume and variogram to be defined individually for each model cell.

  * The search volume can be oriented to follow the trend of the mineralization precisely.

  * Previously this could only be achieved using the UNFOLD option, which often required detailed digitising of tag strings to define the folding.

  * The misalignment of the search volume by just a few degrees can cause the extrapolation of ore into waste and waste into ore.

  * Dynamic Anisotropy provides an easy-to-use and fast way of improving the accuracy of grade estimation; for example, for gently folded and rolling orebodies, and ore bodies with mineralization orientation aligned with mappable geological parameters such as sedimentary bedding orientation.

## Practical Considerations

The macros found in this section give a detailed description of the commands used in a dynamic anisotropy study. However, some of the parameters for **ESTIMA** have been chosen for the purpose of expediency and may not always be the most appropriate for an auditable resource project. In particular, the number of discretisation points used in runs of **ESTIMA** is 2x2x2. If a sensitivity study has not been undertaken then 3x3x3 would probably be better.

When interpolating angles from strings, the maximum number of samples in the search volume should be kept small. The string data already represents an average angle, so further averaging is unnecessary. There is an argument for using the nearest neighbour method (IMETHOD=1) for interpolating angles.

If the model contains subcells then parent cell estimation (PARENT=1) should be considered when estimating angles. This will speed up the processing and in general will not have any effect on the resulting angles.

The spacing of digitised strings and the number of segments is dependent on the variability and geometry of the orebody. However it is quick and easy to digitise strings so it is better to err on the side of too much data.

Unless the orebody is narrow and has a regular outline it is usually better to interpolate angles from digitised strings, rather than use wireframe triangles.

**Tip** : it is important to validate both the angle data created from the strings using **[ANISOANG](<../Process_Help_XML/anisoang.md>)** , and the angle data after it has been converted to true angles using **[APTOTRUE](<../Process_Help_XML/aptotrue.md>)**. This can be done by displaying rotated 3D symbols in a 3D window.

The search volume is oriented individually for each cell. However, the lengths of the axes of the search volume are fixed for each search volume, as defined by fields SDIST1, SDIST2 and SDIST3. Usually these lengths will be derived from the ranges of the variogram model which will be calculated relative to a fixed coordinate system, which does not take into account the folded nature of the orebody. Therefore the lengths of the axes will be averaged over the folding. If a more exact calculation of the variogram model is required, then the [UNFOLD](<../Process_Help_XML/unfold.md>) process or command should be used.

## Dynamic Anisotropy & Kriging

Both examples have used the [Inverse Power of Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) (IPD) estimation method for estimating grades using ESTIMA. Field ANISO was not specified in the [Estimation Parameter files](<Grade%20Estimation%20Parameter%20File.md>), so the default of 1 was applied, which means that the distances for IPD weighting are transformed using the axes and angles of the search volume.

If [Kriging](<Grade%20Estimation%20Kriging.md>) (IMETHOD=3) is selected instead of IPD (IMETHOD=2) and parameter DYANKR is set to 1, the default, then the variogram model rotation angles are set equal to the search volume rotation angles. The full range of values for DYANKR is:

  * 0. Do not use dynamic anisotropy. Use angles **VANGLEn** as defined in the variogram model parameter file **VMODPARM**.

  * 1. If the search volume uses dynamic anisotropy, then the variogram model uses the same set of axes and angles.

  * 2. Use dynamic anisotropy, but with a different set of angles from the search volume. The names of the corresponding fields are specified by fields VANGLn_F in the [estimation parameter file](<Grade%20Estimation%20Parameter%20File.md>)ESTPARM.

**Note** : if option 2 is used then one or more of the fields VANGL1_F, VANGL2_F, VANGL3_F must be added to the estimation parameter file. The angles are specific to the estimation, not to the variogram model. The actual names of the fields must then be included in the input prototype model.

Related topics and activities

  * [Dynamic Anisotropy (ESTIMA) - Introduction](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy (ESTIMA) - Example 1](<Dynamic%20Anisotropy%20-%20Example%201.md>)

    * [Dynamic Anisotropy (ESTIMA) - Example 1 Macro 1](<Dynamic%20Anisotropy%20-%20Example%201%20Macro%201.md>)

  * [Dynamic Anisotropy (ESTIMA) - Example 2](<Dynamic%20Anisotropy%20-%20Example%202.md>)

    * [Dynamic Anisotropy (ESTIMA) - Example 2 Macro 1](<Dynamic%20Anisotropy%20-%20Example%202%20Macro%201.md>)

    * [Dynamic Anisotropy - Example 2 Macro 2](<Dynamic%20Anisotropy%20-%20Example%202%20Macro%202.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)