# Calculating True Dip Angles with APTOTRUE  
  
As described in [Dynamic Anisotropy - Dip and Dip Direction](<Dynamic%20Anisotropy%20-%20Dip%20and%20Dip%20Direction.md>), the dip values interpolated into the model can be either apparent or true. If they are apparent values then they will need to be converted to true values before they can be used for grade estimation. The process **[APTOTRUE](<../Process_Help_XML/aptotrue.md>)** is designed to perform this function.

## Converting Apparent Dip to True Dip

The process **APTOTRUE** takes as input the model file into which the apparent dip and true dip direction angles have been interpolated using ESTIMA, and creates an output model file that includes the true dip angle. The parameter **APDIPDIR** defines the apparent dip direction which enables the true dip to be calculated.

Related topics and activities

  * [Dynamic Anisotropy with ESTIMA](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)