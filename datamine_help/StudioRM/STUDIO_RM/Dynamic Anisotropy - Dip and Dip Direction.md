# Dip and Dip Direction Data

## Wireframes

If the orebody is narrow and stratified and the orientation of the mineralization follows the hangingwall and footwall, then dip and dip direction data can be calculated for each triangle. This is achieved using the process **[ANISOANG](<../Process_Help_XML/anisoang.md>)** which calculates the true dip angle as well as the dip direction.

The above method is straightforward if the hangingwall and footwall are defined by individual DTMs. However, if the wireframe is enclosed, it will contain triangles joining the hangingwall to the footwall, and it is possible that the orientation of mineralization would not match the end triangles. **ANISOANG** includes an option to define a minimum and maximum acceptable dip and dip direction. Therefore if for example the end triangles are vertical, then they could be removed by setting the maximum dip to 89 degrees, assuming of course that no real dip values of 90 degrees are expected. Otherwise the wireframe would need to be edited and the end triangles removed.

Even if the orebody is not stratified, a wireframe(s) could be used to define the orientation of the mineralization. However, it is probably easier to digitise a set of strings rather than create new wireframes.

## Digitised Strings

An alternative way of defining the dip and dip direction of mineralization is to digitise strings in plan and section that describe the orientation. The strings must be planar, the plans horizontal and the sections vertical. 

## Sections

Strings are digitised in section to define the dip and optionally the dip direction. If the sections are oriented in the true dip direction, then the dip will be the true dip of mineralization and the orientation of the section line will be the true dip direction. Both these angles will be calculated by the **ANISOANG** process, and written to the output Points file, together with the coordinates of the mid-point of each string segment.

If the sections are not oriented in the true dip direction then only the apparent dip can be calculated. In this case the sections must be parallel to each other, so that they all have the same apparent dip direction. The apparent dip angle can then be interpolated into the model and process **[APTOTRUE](<../Process_Help_XML/aptotrue.md>)** used to convert from apparent to true dip.

The azimuth (dip direction) of a section can be calculated from any two points and the dip can be calculated for each string segment and assigned to the mid-point of that segment. The direction in which the strings are digitised is important as the dip is measured for each string segment from point N to point N+1.

## Plans

For plans, the strings can show either the true dip direction or the strike. In both cases the direction of the string is important. In the former case the direction of the string indicates the dip direction and in the latter case the dip direction is defined as either 90 degrees or 270 degrees to the direction of strike. 

## Creating the Angle Data

The process **ANISOANG** takes wireframes and / or strings as input and creates a points file. This includes coordinate fields XPT, YPT and ZPT. It also includes a subset of four fields **TRDIPDIR** , TRDIP, **APDIPDIR** and APDIP as shown in the table below. Which fields are created depends on whether apparent or true angles are calculated.

Field |  True Dip Direction |  True Dip |  Apparent Dip Direction |  Apparent Dip  
---|---|---|---|---  
Field Name |  TRDIPDIR |  TRDIP |  APDIPDIR |  APDIP  
Wireframe |  Y |  Y |  N |  N  
Plan |  Y |  N |  N |  N  
Sections in dip direction |  Y |  Y |  N |  N  
Sections not in dip direction |  N |  N |  Y |  Y  
  
As well as the above fields, five optional fields controlled by parameter **ADDSYMB** may be added. These five fields have the reserved field names for displaying 3D symbols in a 3D window.

  * SYMBOLSymbol code. The symbol is selected by parameter **PLANSYMB** for points created from plan strings, **SECTSYMB** for points created from section strings and **WFSYMB** for points created from wireframe triangles. Codes range from 201 to 267 which are shown in the help file.

  * COLOURColour of SYMBOL. This is defined by parameters **PLANCOL** , **SECTCOL** and **TRICOL**.

  * DIPDIRNField used by 3D windows to define the dip direction of a 3D symbol. This is set equal to **TRDIPDIR** or **APDIPDIR** depending on whether true or apparent dips have been calculated.

  * SDIPUsed in 3D window rendering to define the dip of the 3D symbol. This field is set equal to **TRDIP** or **APDIP** depending on whether true or apparent dips have been calculated. For string data on plans **SDIP** is set equal to 0 (horizontal).

  * SYMSIZESize of the symbol in mm as defined by parameter **SYMSIZE**.

The symbol fields provide a simple and effective way of validating the angle data. The points data file can be loaded and displayed in a 3D window. The symbol fields are recognized and a 3D symbol showing dip and dip direction is displayed.

Related topics and activities

  * [Dynamic Anisotropy with ESTIMA](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)