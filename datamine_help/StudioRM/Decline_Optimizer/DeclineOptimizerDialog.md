# Decline Optimizer

To access this screen:

  *   *   * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "optimize-decline".

  *   * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **optimize-decline** and click **Run**.

## About Decline Optimizer

Decline Optimizer optimizes the path of a decline so that it passes through a set of defined 3D locations with a specified maximum gradient and controlled radius of curvature for any curved segments. The defined locations will typically be positions for the start of access ramps at each of the major development levels.

Basic constraints on the path include maximum gradient and minimum curvature and there are additional constraints specific to the mining application. These include offsets from ore bodies or other mining activities (termed barriers) and the preferred orientations of drives to minimize problems with ground conditions.

The optimal path must also take into account development and haulage costs over the life of the use of the development.

For mining problems the barrier tests are fundamental, but also create a significant overhead on testing the feasibility of any path. Barriers are provided as either block models or strings and infeasibility is tested from a representative number of points on the path that the user selects.

Unlike mathematical programming techniques like linear programming, the optimizer does not know in advance if there is no feasible solution to the problem, and consequently the user must use some discretion to identify infeasibilities in parts of the supplied data. Consequently it makes sense to lightly constrain the initial problem and then tighten the constraints to improve the solution. What appears intuitive to the engineer is not automatically the choice of the optimizer. The path between two points can be made up of a number of turning combinations, and allowing a subset of the combinations can reduce the overall curvature of the final solution. Careful selection of the elevations of locations, and selection of gradient constraints should be considered.

## The Decline Optimizer Screen

This screen contains two tabs:

The Path Control tab is used to define the calculation parameters and restrictions that will be applied when creating an optimal decline object, and is split into the following sections:

  * [Radius and Gradient](<radius_and_gradient.md>) Define the radius and gradient of incline models generated with theoptimize-declinecommand.

  * [Allowable Offsets](<allowable_offsets.md>) Define tolerance cuboids within which the resulting decline is allowed to deviate from the points on the input control string. 

  * [Direction Control](<>) Define the start and end azimuth values for a generate decline model, along with other parameters to control how path sections are oriented, and whether spirals are permitted. 

  * [Access Point Control](<access_point_control.md>) Determines how access points are positioned with automatically generated optimal decline shapes.

  * [Exclusion Zones](<exclusion_zones.md>) Define zones where decline points are prohibited during optimal decline generation.

The Optimization tab controls how a calculated decline path is further optimized in terms of maximum path lengths, deviation from preferred orientations and also introduces the concept of cost reporting. See [Decline Optimization Method](<optimization_method.md>).

Related topics and activities

  * [Access Point Control](<access_point_control.md>)

  * [Allowable Offsets](<allowable_offsets.md>)

  * [Direction Control](<direction_control.md>)

  * [Exclusion Zones](<exclusion_zones.md>)

  * [Optimization Method](<optimization_method.md>)

  * [Radius and Gradient](<radius_and_gradient.md>)