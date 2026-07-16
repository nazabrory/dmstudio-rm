![](../Images/HeaderCell.gif) |  MSO - Controls MSO shape framework controls  
---|---  
  
# MSO - Controls

### To access this dialog:

  * Using the MSO ribbon, define a scenario and select Controls.

The Controls panel, part of the MSO workflow, is used to define the base geometries for stope shapes to be created. The contents will depend on the type of framework type selected on the [Shape](<MSOv3_Shape.md>) panel.

![](../Images/Splitter.png)

Slice Method Controls

![](../Images/MSO3_SLICE.jpg)

For a [Slice](<MSO3_Slice_Method.md>) method, this panel is used to define the slice interval and stope width, plus dilution and dip and strike angle settings. Ultimately, these settings define the 'rules' by which optimal stope shapes will be generated in order to match the [economic](<MSOv3_Economics.md>), [orientation](<MSOv3_Orientation.md>) and [shape framework](<MSOv3_Shape.md>) settings you have already defined.

[More about Slice method controls...](<MSO3_Controls_Slice.md>)

![](../Images/Splitter.png)

Prism Method Controls

![](../Images/MSO3_PRISM.jpg)

For a [Prism](<MSO3_Prism_Method.md>) method, this panel is used to define the axis increments and either to specify the stope shape dimensions for each of the U, V and W axes, or to define a list of stope shape dimensions in tabular form.

More about Prism Method Controls...

![](../Images/Splitter.png)

Surface Boundary Method controls

![](../Images/BoundarySurface1.png)

For narrow high grade reefs or lenses, where subcell modelling has some spatial accuracy limitations, it can prove more effective to model stope shapes off the geological wireframes directly. The stope walls are modelled as a mesh of points from [3x3] to [6x6] points. Dilution, orebody positioning in the stope, and an option to split the stope into waste and ore components, are provided.

[More about Boundary Surface method controls...](<MSO3_Controls_BoundarySurface.md>)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Slice Method Overview](<MSO3_Slice_Method.md>)   
[MSO Shape Frameworks](<MSO3_Frameworks_Concept.md>)   
[MSO Angle Conventions](<MSO3_Framework_Angles.md>)   
[MSO Key Shape Concepts](<MSO3_Shape_Diagram.md>)