![](../Images/HeaderCell.gif) |  MSO - Shape Defining your MSO Shape Framework  
---|---  
  
# MSO - Shape

### To access this dialog:

  * Select Shape on the MSO ribbon - the view that is displayed will depend on the status of your project (see below).

Stope-shape frameworks generally prescribe the orientation and three-dimensional constraints for determining stope-shapes, their allowable dimensions and the manner in which they are optimized.

The Shape Framework Settings Panel

This panel is used to define the Framework Type and define the sections/levels and other structural controls that will define your overall shape framework.

There are two possible presentations for this panel;

  * New framework: If a shape framework has not yet been defined, you will be shown a simple view containing a button to Select a Stoping Method. This button displays the [Stope Shape Selection Wizard](<MSO3_Shape_Stope_Generation_Settings.md>).
  * Existing framework: If you have already defined a framework type/geometry and orientation, you will be shown the existing settings for the framework (using the [Shape Framework Settings](<MSO3_Shape_Shape_Framework_Settings.md>) panel. You can edit these settings, or change the framework type using the Change button, which redisplays the Stope Shape Selection Wizard.

Stope Optimization Methods

The Mineable Shape Optimizer tool supports the following shape frameworks:

  * "Slice Method" which generates and evaluates thin slices across the mineralized zones that are aggregated into seed-shapes (looking at all possible permutations) that satisfy stope and pillar width constraints. The seed-shapes are then annealed to the final optimized stope-shape satisfying the stope and pillar width, stope geometry constraints (e.g. wall dips angles, strike twist, etc.), and other miscellaneous constraints (e.g. zone mixing, exclusion zones, etc.). The result is a set of stope-shapes constrained to the basic limitations of the envisaged mining method.  
  
Slice method frameworks are available in either Standard or Advanced types.  
  
[Standard Slice Framework Settings](<MSO3_Shape_Framework_Settings_Standard.md>)  
[Advanced Slice Framework Settings](<MSO3_Shape_Framework_Settings_Advanced.md>)  

  * "Prism Method" which optimally combines a set of shapes from a library of stope-volumes within regions without allowing overlapping of the generated stopes. It is typically applicable to massive orebodies or wide/thick deposits whose stopes tend to be designed by blocking out the orebody in a grid-like pattern.  
  
[Prism Framework Settings](<MSO3_Shape_Framework_Settings_Prism.md>)  

  * "Boundary Surface Method" for narrow high grade reefs or lenses, where subcell modelling has some spatial accuracy limitations, it can prove more effective to model stope shapes off the geological wireframes directly. The stope walls are modelled as a mesh of points from [3x3] to [6x6] points. Dilution, orebody positioning in the stope, and an option to split the stope into waste and ore components, are provided.   
  
[Boundary Surface Framework Settings](<MSO4_Boundary_Surface_Method.md>)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Stope Shape Selection Wizard](<MSO3_Shape_Stope_Generation_Settings.md>)[Shape Framework Settings](<MSO3_Shape_Shape_Framework_Settings.md>)[Standard Slice Framework Settings](<MSO3_Shape_Framework_Settings_Standard.md>)[Advanced Slice Framework Settings](<MSO3_Shape_Framework_Settings_Advanced.md>)[Prism Framework Settings](<MSO3_Shape_Framework_Settings_Prism.md>)[Boundary Surface Framework Settings](<MSO4_Boundary_Surface_Method.md>)