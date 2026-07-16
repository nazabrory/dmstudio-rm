# Interpolating Angles into a Geological Model with ESTIMA

**Note** : **[COKRIG](<../Process_Help_XML/cokrig.md>)** also provides Dynamic Anisotropy support. See [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

Once the dip and dip direction data has been created, the next stage is to interpolate the two sets of angles into the block model. However, it is not possible to use the standard interpolation methods in [ESTIMA](<../Process_Help_XML/estima.md>) as angle data is circular for example the average of 340 and 30 is 5. **IMETHOD** =8 has all the functionality of inverse power of distance (**IMETHOD** =2) but can be used with angular data. 

Therefore interpolating the angular data can be done through the standard **ESTIMA** process using **IMETHOD** =8.

The angular data option has also been added to the [**ESTIMATE**](<EstimateDialog.md>) dialog as a check box adjacent to the Inverse Power of Distance method.

Related topics and activities

  * [Dynamic Anisotropy with ESTIMA](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)