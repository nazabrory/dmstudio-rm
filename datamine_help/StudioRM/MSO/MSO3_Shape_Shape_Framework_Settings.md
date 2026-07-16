![](../Images/HeaderCell.gif) |  MSO - Shape Framework Settings Defining MSO Shape Framework details  
---|---  
  
# MSO - Shape Framework Settings

### To access this dialog:

  * Load an MSO [scenario](<MSOv3_Scenarios.md>) with a predefined [Shape Framework Type](<MSO3_Shape_Stope_Generation_Settings.md>) and select Shape on the MSO ribbon.

  * On the [Stope Generation Settings](<MSO3_Shape_Stope_Generation_Settings.md>) view, select OK.

Stope-shape frameworks generally prescribe the orientation and three-dimensional constraints for determining stope-shapes, their allowable dimensions and the manner in which they are optimized. This panel is shown once a high-level framework has been defined, using the [Stope Shape Selection](<MSO3_Shape_Stope_Generation_Settings.md>) wizard, which offers a choice of either Slice, Prism or Boundary Surface framework types.

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

Section and Level Intervals

The selection of start location for levels or sections and spacing for levels and/or sections are key design choices for mine planners.

The initial framework specification defines the extent of the volume to be considered.

The way in which intervals used for stope shape generation are defined will depend on whether you are setting up a [standard](<MSO3_Shape_Framework_Settings_Standard.md>) or [advanced](<MSO3_Shape_Framework_Settings_Advanced.md>) framework.

Slice Method - Framework Settings

Standard and Advanced Frameworks

For the selected framework types, an MSO shape framework can be defined as either a Standard or an Advanced framework. The difference is:

  * For a Standard framework, U and V axis intervals can be either fixed or variable.
  *     * Fixed intervals: this is where both the U and V axis intervals are fixed - like having fixed section spacing and fixed level spacing for vertical orientations or fixed strike sections and fixed wall spacing for horizontal orientations.
    * Variable intervals: where either or both of the U and V-axis intervals is variable. For example like having 4x25m levels and 1x15m sill pillar level for a mine block covering 115m vertical extent which is repeated, or like having 15m primary and 20m secondary stopes along strike (for vertical orientations).  
  
[More about standard slice framework settings...](<MSO3_Shape_Framework_Settings_Standard.md>)
  * An Advanced framework is more flexible and requires you to specify actual coordinates to define long section (U, V) dimensions of the stope-shape geometry. The coordinates can represent either rectangular shapes (orthogonal), or trapezoidal or quadrilateral shapes (non-orthogonal).  
  
[More about advanced slice framework settings...](<MSO3_Shape_Framework_Settings_Advanced.md>)

Prism Method - Framework Settings

The [Prism](<MSO3_Shape_Framework_Settings_Prism.md>) method is a different style of stope optimization to the Slice method. In the Slice method the stope-shape framework is decomposed into individual geometric tubes based on the level and section dimension for the Vertical case, and the stope-shape (or sub-shape) is an optimization over the width of the orebody, with a two stage process to:

  * Firstly, define the seed-shape, and

  * secondly, to anneal the final stope-shape.

The Prism method also requires a stope-shape framework, but uses the decomposition of the framework extents to define sub-problems. The framework extent is subdivided in regular intervals, much like regular quadrilaterals, except that the subdivision is three dimensional rather than two dimensional, and each subdivided volume is referred to as a region, whereas the Slice method subdivision is two dimensional to form a tube.

Prism frameworks are not orientation specific but the XYZ intervals must be regular. A grid increment is defined on this panel for each axis, within regions (i.e. sub-set volumes of the total Prism framework). Shapes from the stope-volume library will normally have dimensions that are an integer multiple of the grid increment and can result in stopes located at any grid increment.

As such, if a Prism framework has been specified, the only definition required is the intervals along the U, V and W axes to form the framework regions. For each of the U, V and W local axes, this panel is used to determine an Increment (size) and Number.

Using Structure Surfaces (Slice and Boundary Surface methods)

A structure surface is a wireframe file that can be used to refine the boundary surface of a stope. In brief, the wireframe acts as a snapping surface providing the resulting shape is economically viable. This data can be specified for both [Slice](<MSO3_Slice_Method.md>) ([Standard](<MSO3_Shape_Framework_Settings_Standard.md>) and [Advanced](<MSO3_Shape_Framework_Settings_Advanced.md>)) method and the [boundary surface](<MSO4_Boundary_Surface_Method.md>) method.

[More about structure surfaces...](<MSO3_Structure_Surfaces.md>)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Stope Shape Selection Wizard](<MSO3_Shape_Stope_Generation_Settings.md>)   
[Shape Frameworks](<MSO3_Frameworks_Concept.md>)   
[Slice Method Overview](<MSO3_Slice_Method.md>)   
[Key Shape Concepts](<MSO3_Shape_Diagram.md>)   
[Slice Method](<MSO3_Slice_Method.md>)   
[Prism Method](<MSO3_Prism_Method.md>)[Boundary Surface Method](<MSO4_Boundary_Surface_Method.md>)[Using Structure Surfaces](<MSO3_Structure_Surfaces.md>)