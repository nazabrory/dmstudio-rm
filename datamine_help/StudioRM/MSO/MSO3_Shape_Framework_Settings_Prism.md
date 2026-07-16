![](../Images/HeaderCell.gif) |  MSO - Prism Framework Settings Defining MSO Shape Framework details  
---|---  
  
# MSO - Prism Framework Settings

### To access this dialog:

  * Load an MSO [scenario](<MSOv3_Scenarios.md>) with a predefined [Shape Framework Type](<MSO3_Shape_Stope_Generation_Settings.md>) and select Shape on the MSO ribbon.

  * On the [Stope Generation Settings](<MSO3_Shape_Stope_Generation_Settings.md>) view, select OK.

Stope-shape frameworks generally prescribe the orientation and three-dimensional constraints for determining stope-shapes, their allowable dimensions and the manner in which they are optimized. This panel is shown once a high-level framework has been defined, using the [Stope Shape Selection](<MSO3_Shape_Stope_Generation_Settings.md>) wizard, which offers a choice of either Slice, Prism or Boundary Surface framework types.

The Prism method optimally combines the stope-volumes within each framework "region" with no overlapping of either regular or various irregular stope-volumes (i.e. it selects the optimum non-overlapping combination of rectangular stope-volumes). The goal of the optimisation is to select the set of non-overlapping stope-shapes that maximises value for the material to be extracted by the selected stope-shapes. All possible combinations of shapes and positions are considered in the optimisation. [More...](<MSO3_Prism_Method.md>)

This panel is used to define details for the selected [Framework Type](<MSO3_Shape_Stope_Generation_Settings.md>) and its contents will depend on which of the two framework types has been selected.

Select a link for more information:

  * [Slice Method Panel Details (Standard framework)](<MSO3_Shape_Framework_Settings_Standard.md>)
  * [Slice Method Panel Details (Advanced framework)](<MSO3_Shape_Framework_Settings_Advanced.md>)
  * Prism Method Panel Details
  * [Boundary Surface Method Panel Details](<MSO4_Boundary_Surface_Method.md>)

Section and Level Intervals

The selection of start location for levels or sections and spacing for levels and/or sections are key design choices for mine planners.

The initial framework specification defines the extent of the volume to be considered.

The way in which intervals used for stope shape generation are defined will depend on whether you are setting up a standard or advanced framework.

Slice Method - Framework Settings

Standard and Advanced Frameworks

For the selected framework types, an MSO shape framework can be defined as either a Standard or an Advanced framework. The difference is:

  * For a Standard framework, U and V axis intervals can be either fixed or variable.
  *     * Fixed intervals: this is where both the U and V axis intervals are fixed - like having fixed section spacing and fixed level spacing for vertical orientations or fixed strike sections and fixed wall spacing for horizontal orientations.
    * Variable intervals: where either or both of the U and V-axis intervals is variable. For example like having 4x25m levels and 1x15m sill pillar level for a mine block covering 115m vertical extent which is repeated, or like having 15m primary and 20m secondary stopes along strike (for vertical orientations).  
  
More about standard framework settings...
  * An Advanced framework is more flexible and requires you to specify actual coordinates to define long section (U, V) dimensions of the stope-shape geometry. The coordinates can represent either rectangular shapes (orthogonal), or trapezoidal or quadrilateral shapes (non-orthogonal).  
  
More about advanced framework settings...

Standard Frameworks

Defining a standard framework is a case of defining the sections and levels properties, and whether you wish to use additional string data to control gradients and/or ore development.

To minimise the number of combinations to be considered, the stope-shape size Increment should be a sub-multiple of the stope dimension. The origin shift should be a sub-multiple of the stope sizes. For example, the stope sizes might be 20-35 in increments of 5 and the origin step size is set to 5. As the run-time for a large set of increment combinations might be prohibitive, a single test scenario should be run to estimate the likely runtime for all combinations, e.g. nominate a single stope size and no origin step to ascertain the run-time for a single iteration.

The stope sections (U-axis) may be regularly spaced or irregularly spaced. At the same time, the stope levels (V-axis) may be regularly spaced, irregularly spaced or irregularly spaced with variable Gradient.

Selecting the Standard Frameworks option reveals the following options:

Sections (U): select whether you will defining:

Fixed intervals (see "Standard and Advanced Frameworks", above): specify the interval distance to automatically calculate the Number of intervals along the U axis.

Note that the section interval multiplied by the number of intervals will equal the U model prototype distance as seen on the Orientation panel (e.g. UAxis Distance = 160 and sections Increment = 5 will mean the Number of intervals is 32).

Variable intervals: select this option and you can define the U coordinate at which an interval Increment (Size) can be defined. There is no limit to the number of section intervals you can define - just add and remove table columns as required. In the following example, a 160m U-Axis Distance has been broken up into irregular intervals, starting at the model U origin (55340m coordinate):

![](../Images_STUDIORM_ONLY/MSO3_Sections1.jpg)

Levels (V): levels are defined in a similar manner to sections, with the added option to specify a string file containing variable gradient values (this is known as the Gradient Control String).

For non-transverse frameworks, the following level options are available:

Fixed intervals (see "Standard and Advanced Frameworks", above): specify the interval distance to automatically calculate the number of intervals along the V axis.

Variable: similar to the definition of variable U-axis sections, use the table to define a 'map' of intervals and sizes to define a variable framework. For example, like having 4 x 25m levels and 1 x 15m sill pillar level for a mine block covering 115m vertical extent which is repeated, or like having 15m primary and 20m secondary stopes along strike (for vertical orientations).

Gradient Strings: a gradient control-string can be used to define the gradients of levels along the orebody strike axis (variable V-axis). The strings would typically be used for orebodies with an extensive strike length, such that the difference in elevation from the level access point to the level strike extremity is significant. The gradient control-string will change the framework geometry, as shown in the image below:  
  
![](../Images/MSO3_GradControl2.jpg)  

A stope face is created where a pair of gradient strings intersects adjacent sections. Ideally the control-strings should have the same orientation as the stope-framework U-axis. Care is required to ensure that adjacent strings extend to intersect all sections. This will avoid unintended trapezoidal shapes, or unintended gaps, as shown below:  
  
![](../Images/MSO3_GradControl1.jpg)  

Polytube Strings: in cases where the orebody is wide it may also be appropriate to have a gradient in the transverse (W direction). A fixed gradient change from the horizontal (in degrees) can be specified for the far and near side for vertical frameworks.  

![note.gif \(1017 bytes\)](../Images/note.gif) |  Polytube Strings can only be specified if a control surface has been set up in the Dynamic Dip and Strike Controls section of the [Scenarios](<MSOv3_Scenarios.md>) panel.  
---|---  
  
A polytube control string is used to model a tube as a 3d shape. The strings are used to locate the corners of the tube. Annealing works by sliding the stope corners along the corner strings, at each increment changing the (x,y,z) coordinate rather than a simple adjustment of the W coordinate for a fixed quadrilateral (U,V). Annealing overheads are increased for this flexibility.  

![note.gif \(1017 bytes\)](../Images/note.gif) |  Polytube Strings cannot be used in conjunction with shape [refinement](<MSOv3_Refinement.md>).  
---|---  
  
  
[More about MSO Control Strings...](<MSO3_Control%20Strings.md>)

![](../Images/Warning.gif) |  Increasing the number of MSO framework sections and levels, either through decreasing the Increment or setting up a variable increment configuration (on the [Shape](<MSO3_Shape_Shape_Framework_Settings.md>) panel) can have a dramatic effect on the resulting stope-shapes, including the processing time that is required to perform a run. It is good practice to start with a coarse framework (levels and sections) and gradually increase the "resolution" of the calculation until an optimal result is acquired. The image below shows 4 separate runs for the same basic scenario (and equally basic input model). Example timings for each run are as follows - all following a Standard Framework approach and no [post-processing](<MSOv3_Options.md>) options::

  1. Sections: Fixed increment = 20 = 8 intervals (framework = 160m XDistanceas defined on[Orientation](<MSOv3_Orientation.md>)panel).   
Levels: Fixed increment = 40 = 4 intervals (framework = 160m Z Distance)  
Processing time: 1m 2s
  2. Sections: Fixed increment = 5 = 32 intervals  
Levels: Fixed increment = 10 = 16 intervals  
Processing time = 11m 14 s
  3. Sections: Fixed increment = 5 = 32 intervals  
Levels: Fixed increment = 40 = 4 intervals  
Processing time = 2m 47s
  4. Sections: Fixed increment = 20 = 8 intervals  
Levels: Fixed increment = 16 = 10 intervals  
Processing time = 1m 38s

![](../Images_STUDIORM_ONLY/MSO_Timings.jpg) (Timings from an 8mhz Dell Precision M6800 8Ghz, Intel Core i7 3.00 GHz quad core with NVidia Quadro K4100M)  
---|---  
  
For transverse frameworks, the following level options are available:

Transverse shape frameworks are a special case of XZ or YZ orebody orientations that optimize shapes in both the transverse and vertical directions. This method is suited to gentle/shallow dipping, thicker orebodies. You can define your section spacing either manually, or using imported string data:

Use Sub-Level Section Spacing: selecting this option allows you to define your test for optimal sublevel spacing. Define the extents of the search using the Minimum and Maximum spacing values within which to find the best solution and the Increment to use within that range. Put another way, for framework optimization, the stope-shape minimum and maximum size and increment are supplied for the axes specified by the stope orientation plane, and the Axis step size for the origin shift along the same axes.

For example, the following image represents a test for sublevels of 60, 70 and 80m in increments of 10m and an origin shift of 20m:  
  
![](../Images/MSO_Sublevels.jpg)

Use Sub-Level Section Strings: an alternative to explicitly defining sub-level test parameters, this option allows you to define your level positions (with gradient) using imported string data (which must be in Datamine binary format). Stopes are not optimized in this scenario but are rather controlled by the lateral extent of the section control strings, e.g.:  
  
![](../Images/MSO_ControlStrings.jpg)

For all standard frameworks, the following options are available:

Use Ore Development Strings: an Ore Development String is used to define level layouts on fixed elevations (horizontal gradient) using development centrelines. A stope cannot be created unless its floor is located on a control-string, and a stope floor cannot be located on more than one control-string.

Ore development strings do not change the framework, and should be added as an option to a second-pass run. The strings are typically used to control the location of stopes and pillars from section to section. They define practical level layouts by constraining the transverse lateral extents of stope-shapes for parallel lodes (i.e. W-axis direction). The strings can also be used to constrain the strike extents (U-axis) to say remove strike outliers.

Select this option to select a Datamine string file.

[More about MSO Control Strings...](<MSO3_Control%20Strings.md>)   
  
![](../Images_STUDIORM_ONLY/MSO3_ControlStrings2.jpg)

Advanced Frameworks

  
Section and Level Intervals Field Details

In MSO, an Advanced Framework is used to specify coordinates that will represent long section (U, V) dimensions of the stope-shape geometry. The coordinates can represent either rectangular shapes (orthogonal), or trapezoidal shapes (non-orthogonal).

  * Stope Rectangles and Stope Trapezoids: for rectangular definitions (Stope Rectangles option), you can define your own U and V minimum and maximum values. The Stope Trapezoids option allows you to determine the additional point settings required to define the non-orthogonal shape. A trapezoid stope-shape has two opposite parallel sides and is defined by the coordinates (umin, umax, v1min, v1max, v2min, v2max).  
  
![](../Images_STUDIORM_ONLY/MSO3_Rect_Trap.jpg)  
  
Both rectangular and trapezoidal methods define the stope-shape in long section, and the projection of this shape in the W-axis direction (i.e. transverse direction) forms the face of the stope-shape "tube".  
  
Specification of the stope-shape dimensions can be individually specified within the extents of the framework. This may be of particular use for orebodies that require irregularly located/shaped pillars or require an irregular exclusion zone around say a shaft, workshop, and development access or require irregular stopes with say variable section end-walls so that they are at right-angles to the contour.  
  
Use the supplied grid to define each rectangle (4 properties) or trapezoid (6 properties)

  * Stope Face Polygons: polygonal shapes for the stope profile have been possible using sub-stope polygons, but the polygonal shape was constrained to the boundary of the tube dimensions in U and V. A typical application might have been room and pillar mining where the pillar and the non-pillar mining shape could be supplied.   
  
For sublevel caving an interlocking set of shapes (with more points to define the profile) is required. These are referred to as stope polygons. One or more shapes are defined as points to create a closed polygon and stope polygons are replicated within the framework volume by specifying a UV offset from the framework origin for the first shape, and a UV increment for replicating the shape across the framework, e.g.:  
  
![](../Images/VPR.jpg)  
  
One or more stope polygons can be defined in the table with the assumption that replicated stope polygons do not overlap. The Stope Polygons are processed in the order generated by the replication.   
  
Exact evaluation and reporting is automatically enabled if this option is selected (but can be overridden if required) to ensure that the stope shapes are accurately evaluated. 

    1. Select the Stope Face Polygons option

    2. For each shape to be replicated, create a new table row.

    3. Enter the U Origin Offset and V Origin Offset from the framework origin.

    4. Define the U Step and V Step to be used for replication.

    5. If required, enter a scaling value to be applied.

    6. Click in the Point List field and select Edit to define a closed polygon shape in local coordinates, using the Point List Configuration dialog.

    7. Repeat steps 3-6 for each row/shape you wish to add.

  * Optimized Regular: the stope-shape framework can be floated in the stope orientation plane (using defined step increments) to optimise the start location for both the level and section without changing the dimensions of the level interval (V-axis dimension) or section spacing (U axis dimension). The stope-shape framework can then be further refined by also changing the level and/or section spacing dimensions.   
  
[More about regular framework optimization options...](<MSO3_Framework_Optimization.md>)

  * Quad Strings: quad strings are used to pre-define 4 corners of the MSO quad. The optimization is done in W direction. Each string must be closed containing 5 points.

  * Stope Seed Strings / Wireframes: typically used for reprocessing existing stopes, The string file or wireframe file output from a previous run can be supplied as a seed shape input file. The stope shapes are used as the seed shape rather than generate new seed shapes from the default slice/seed method. No new shapes are formed but there is the possibility that some supplied seed shapes may become sub economic, or not satisfy the new geometry parameters.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Both wireframe and string files have a limitation of 1000 records upon attempting to run the scenario, generating an error if the file has more records.   
---|---  
  
    * Selecting the Stope Seed Strings option prompts you to browse for a string file and define the attribute that represents the stope identifier using the Stope Number Field drop-down list.

    * Selecting the Stope Seed Wireframes option prompts you to browse for the triangle and point partner files that represent your previously-generated stopes. As above, a Stope Number Field selection is also required. 

  * Complex Stope Shape: in operational mine designs the sections may not be parallel e.g. radial sections, and the gradient may vary across strike as well as along strike for wide orebodies. To accommodate these requirements a more flexible geometry is achieved by using strings to define the tube corner lines. Annealing overheads are increased for this flexibility.  
  
With this option, you provide the strings that define the tube corner strings. The Stope Shape Framework is then defined by the volume extent and then a set of strings that, when matched, define the level and section position for every tube. In this way, frameworks can be a mix of parallel and radial sections, for example.   
  
Additional housekeeping is required in the string preparation to provide attributes for each supplied string to identify the level and section for each string. Input is restricted to 2 point strings and output 4 point stope shapes with no support for post-processing.   
  
In the figure below, the strings have two additional attributes to identify the sections and levels, labelled as U1, U2, U3 and U4 for the sections, and V1, V2, V3 for the levels. A tube is generated where a volume is defined by adjacent sections and levels. If there is a missing section or level for one of the corner strings of a tube then no tube is generated:  
![](../Images/MSO_Polytube_Complex.jpg)

    1. Select the Complex Stope Shape framework option

    2. Select the string file representing the tube corner strings.

    3. Select the attribute within the string file representing the U Identifier and V Identifier.

    4. Choose the default value for the attribute.

    5. For both U and V directions, use the corresponding table to define a numeric value of the selected identification attribute.

Structure Surfaces

The following controls are available to both Standard and Advanced Slice frameworks, and the Boundary Surface framework:

  
Use Structure Surface Wireframe: select this option to select a Datamine wireframe triangle file. This option is available for both Standard and Advanced Frameworks.

This option results in the stope-shape either snapping-to the structure surface (e.g. include waste that would normally fall into the stope-void due to the presence of the structure) or standing-off (expanding) from the structure surface (e.g. leaving a skin of ore against the structure for dilution control i.e. ore loss).

MSO assesses both options in generating the seed-shape, and applies the same rules to the annealed shape. If the snapping-to shape is sub-economic, then MSO will still consider the standing-off option. This will depend upon the relative position of mineralized material and the structure surface.

Expand option:

You will need to define the range within which expanded stope points are created at the loaded surface. The default option is to set the maximum 'snap distance' from the floor and roof (Max Floor Distance and Max Roof Distance).

You can choose whether to specify a minimum distance from the structure wireframe, within which the stope expands the stope-shape to that structure surface. If one or more corners are within the minimum distance, the remaining corners are tested against the maximum distance. This is the Use Minimum Distances option, which if selected, will require you to set a Min Floor Distance and a Min Roof Distance.

The stope wall is snapped-to the structure position if it falls within the set criteria (minimum - target, maximum - range). This can result in a dip angle that is flatter or steeper than set in the stope geometry parameters.

Snap To option:

With this option, you set the distance range from either the [floor] or [roof] - you just select the wireframe file, and a Min Distance and Max Distance. Stope points that fall within this distance range from the loaded control surface will be 'snapped' to the surface.

Optimize: horizontal deposits, for example mineral sands where the mineralization is found under overlying waste, add additional complexities for generation of the optimal mining surface. 

You can run the Stope Optimizer to find the optimal mineralized profile but not been possible to take into account the cost of removing the overlying waste where it can be mined separately, or the penalty applied when the whole profile is mined and processed as a single unit. Using the topography surface as a Structure surface, and snapping/expanding the optimized mineralized zone to the surface is a valid approach, but this option does not resolve the cost or penalty. 

Instead, you can choose to optimize the horizontal mining unit that has been developed. 

If Optimize is selected, you can choose a wireframe triangle/point file pair to specify a surface that will not be mined past. Typically, this surface is topography, but it doesn't need to be. You can also choose what surface represents using the Position drop-down list.

The following example shows how a Structure Surface Wireframe is used,

![](../Images_STUDIORM_ONLY/MSO_StructureControlSurface.jpg)

Prism Method - Framework Settings

The [Prism](<MSO3_Prism_Method.md>) method is a different style of stope optimization to the Slice method. In the Slice method the stope-shape framework is decomposed into individual geometric tubes based on the level and section dimension for the Vertical case, and the stope-shape (or sub-shape) is an optimization over the width of the orebody, with a two stage process to:

  * Firstly, define the seed-shape, and

  * secondly, to anneal the final stope-shape.

The Prism method also requires a stope-shape framework, but uses the decomposition of the framework extents to define sub-problems. The framework extent is subdivided in regular intervals, much like regular quadrilaterals, except that the subdivision is three dimensional rather than two dimensional, and each subdivided volume is referred to as a region, whereas the Slice method subdivision is two dimensional to form a tube.

Prism frameworks are not orientation specific but the XYZ intervals must be regular. A grid increment is defined on this panel for each axis, within regions (i.e. sub-set volumes of the total Prism framework). Shapes from the stope-volume library will normally have dimensions that are an integer multiple of the grid increment and can result in stopes located at any grid increment.

As such, if a Prism framework has been specified, the only definition required is the intervals along the U, V and W axes to form the framework regions. For each of the U, V and W local axes, this panel is used to determine an Increment (size) and Number.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Stope Shape Selection Wizard](<MSO3_Shape_Stope_Generation_Settings.md>)   
[MSO Shape Frameworks](<MSO3_Frameworks_Concept.md>)   
[Slice Method Overview](<MSO3_Slice_Method.md>)   
[MSO Key Shape Concepts](<MSO3_Shape_Diagram.md>)   
[MSO Slice Method](<MSO3_Slice_Method.md>)   
[MSO Prism Method](<MSO3_Prism_Method.md>)