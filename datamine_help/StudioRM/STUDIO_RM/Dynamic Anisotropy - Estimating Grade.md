# Dynamic Anisotropy (ESTIMA): Estimating Grade

**Note** : **[COKRIG](<../Process_Help_XML/cokrig.md>)** also provides Dynamic Anisotropy support. See [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

The dynamic anisotropy option in [ESTIMA](<../Process_Help_XML/estima.md>) allows the orientation of the search volume and/or the orientation of the variogram model to vary from block to block. The only differences between defining a fixed and a variable search volume orientation are:

  * The input prototype model file &**PROTO** must contain one, two or three angle fields.

  * The search volume parameter must contain the names of the corresponding angle fields in fields SANGL1_F, SANGL2_F, SANGL3_F.

The main purpose of the search volume is to select the samples to be used for the estimation. It is independent of the estimation method, and therefore allows it to be used with any estimation method IPD, nearest neighbour, ordinary, simple or indicator kriging, or Sichels T estimator. However, the search volume can also be used to define anisotropic weighting, as described below.

## Defining the Search Volume

The search volume orientation angles are specified as fields in the input prototype model. The names of these fields are defined by you, and are included as fields SANGL1_F, SANGL2_F, SANGL3_F in the search volume parameter file. 

The default values of the three angle fields are defined in the standard fields **SANGLE1, SANGLE2** and SANGLE3 in the search volume parameter file. These defaults are used if one or more of the angle fields are not defined in fields SANGLn_F in the search volume file. Therefore in the common situation where only two angle fields are used it is only necessary to define SANGL1_F and SANGL2_F. The third field SANGL3_F is optional if it exists but is not required then its value should be left blank. The defaults are also used if the value of the angle in the prototype model file is absent data or is outside the range -360 to +360.

The fields used to define the lengths of the search volume axes (**SDIST1, SDIST2, SDIST2**) and the fields used to define the axes about which the volume is rotated (SAXIS1, SAXIS2, SAXIS3) are constant for each search volume.

## Inverse Power of Distance

If IPD is selected then one of the options in the estimation parameter file is to define whether the search volume anisotropy is to be used to transform the distances of each sample from the block centre. The ANISO field can have one of three values, as follows:

  * 0: True distance. The distance is measured in the standard coordinate system no transformation.

  * 1: The distance is measured as a transformed distance, using the search volume shape and orientation.

  * 2: The distance is measured as a transformed distance, using the shape and orientation defined in the estimation parameter file.

The default and most commonly-used value for ANISO is '1' (use the search volume parameters). If this is selected then the orientation of the transformed distances used for IPD calculations vary from block to block.

## Nearest Neighbour

The **ANISO** field in the estimation parameter file also applies to the Nearest Neighbour method, as the transformed distance is used to determine the closest sample. If dynamic anisotropy is selected and **ANISO** =1, then the selection of the nearest sample will be influenced by the orientation of the search volume for each model block.

## Kriging

If one of the kriging methods is chosen then parameter **DYANKR** is used to select whether the variogram model rotation angles should use the dynamic anisotropy option. The possible values of this parameter are:

  * 0: True distance. Do not use dynamic anisotropy. Use fixed angles VANGLE1, VANGLE2, VANGLE3 as defined in the variogram model parameter file.

  * 1: If the search volume uses dynamic anisotropy, then the variogram model uses the same set of angles. If the search volume does not use dynamic anisotropy, then the variogram model uses angles VANGLE1, VANGLE2, VANGLE3.

  * 2: Use dynamic anisotropy but with a different set of angles from the search volume, defined by fields in the input model prototype file. The names of these are specified by fields VANGL1_F, VANGL2_F, VANGL3_F in the estimation parameter file.

  * One or more of the variogram model rotation angles are stored in the block model. It is not necessary for all angles to be stored in the model. If one or two of the VANGL*_F fields are not in the model then their values will be defined by the corresponding VANGLE* values in the variogram model parameter file. The VANGLE* values are also used if the values of the angles in the input block model are absent data.

If the parameter DYANKR is not specified, then the default value of '1' is applied.

Related topics and activities

  * [Dynamic Anisotropy with ESTIMA](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)