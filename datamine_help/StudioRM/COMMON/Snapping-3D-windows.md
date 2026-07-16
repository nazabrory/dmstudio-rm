# Snapping to 3D Data

3D window digitizing comes in two basic forms:

  * Free digitizing, where data points are digitized (either with the mouse or stylus) onto the currently active **[3D section](<../VR_Help/Sections.md>)** , or;

  * Snapping, where data points are added to be coincident with other data points on loaded [3D objects](<../VR_Help/Objects_Introduction.md>).

Snapping is typically performed using the right mouse button during digitizing, or the equivalent action on a smart stylus. In this scenario, snapping can be applied whenever it is appropriate, and you can continue digitizing onto a 3D section (the "free" method) using either the left mouse or a stylus tap.

You can also enable snapping for any type of digitizing, by setting a _passive snapping mode_ using the [auto-snap-switch ("asn")](<../command_help/auto-snap-switch.md>) command.

Also, see [Digitizing in 3D](<../VR_Help/Digitizing_In_VR.md>) and [3D Design](<../VR_Help/Designing_in_VR.md>).

### Snap Settings

If a command doesn't automatically enforce snapping, the data you snap to when right-clicking or using the smart stylus depends on your snap settings. These determine:

  * The data type(s) to which you can snap new data points. 

  * The data object overlay(s) that can be a target for snapping.

  * Special snapping instructions, such as snapping to the mid point of a string edge, or to a grid.

It is important to define your snap settings first and then digitize new data. For example, if you plan to digitize a string that snaps to a wireframe surface during digitizing (as opposed to [projecting](<../VR_Help/Strings_Fitting%20a%20string%20to%20a%20surface.md>) it to the surface after), you will need to ensure wireframe data is enabled as a target for snapping.

**Note** : Snapping can also be used when editing data, such as moving points or extending a string, for example.

Typically, snap settings are defined using your product's **Home** ribbon.

### Snapping to a Grid

You can snap data positions to a grid.

Note: The snapping grid shouldn't be confused with the [3D window visual grid](<Grids-in-3D.md>), which isn't a target for snapping (this system overlay provides 2D and 3D references primarily for measurement purposes. The grid used for snapping is separate, although the two can be made to be the same.

The snapping grid is created using the [Snapping Grid Parameters](<SnappingGrid_Dialog.md>) screen. This determines the spacing of grid lines and, as such, the positions using for snapping when the snapping mode is set to **Snap to Grid**.

Snap setting related topics and activities

  * [Snap Mode](<SnapSettings.md>)

  * [Snapping Grid Parameters](<SnappingGrid_Dialog.md>)

  * [Digitizing in 3D](<../VR_Help/Digitizing_In_VR.md>)

  * [3D Window Grids](<Grids-in-3D.md>)

### Snap Commands

There are several commands that allow snap settings to be defined. Click a link for more information:

**Note** : All _snap-to....switch_ commands are also supported by explicit commands to enable or disable a particular snap mode. For example, **snap-to-point-data-switch** command variations are **snap-to-point-data-on** and **snap-to-point-data-off**. You can find help for these other commands using the search facility, the index or [command tables](<../command_help/commandtable.md>).

### Snapping with Advanced Digitizing

If [Advanced string controls](<advanced_string_design.md>) are enabled, snapping can be affected. Where digitizing constraints (segment length, azimuth, azimuth change or gradient) are enforced, snapping will attempt to honour both these constraints and the objective of snapping. In most cases, the results will be ambiguous, so the following logic applies:

  * If (only) the **Length** of new string segments are constrained, snapping will determine the azimuth and gradient of the next string segment(s) but the length constraint is enforced. For example, in the image below, a string is extended multiple times by 15m intervals by snapping to the white dot (click any image to expand it):

[![](../Images/Advanced-String-Design_Length.png)](<javascript:void\(0\);>)

  * If (only) the **Azimuth** is specified, it is honoured but the distance between the latest string vertex and the snap point determines the segment length. The change in gradient (if any) between the latest string vertex and the snap point is honoured:

[![](../Images/Advanced-String-Design_Azi.png)](<javascript:void\(0\);>)

  * If (only) the **Gradient** is specified, the gradient is enforced. Azimuth and distance are determined by the snap position:

[![](../Images/Advanced-String-Design_Gradient.png)](<javascript:void\(0\);>)

Where constraints are used, including in combination, these take precedence over selected snap positions. In a similar way, if you specify [command line coordinates](<Coordinates_Command%20Line.md>), and constraints are in effect, the coordinates are honoured only so far as they don't violate digitizing constraints.

Related commands and topics

  * [3D Design](<../VR_Help/Designing_in_VR.md>)

  * [Digitizing in 3D](<../VR_Help/Digitizing_In_VR.md>)

  * [Advanced String Design](<advanced_string_design.md>)

  * [auto-snap-switch ("asn")](<../command_help/auto-snap-switch.md>)

  * [snap-always-switch ("sna")](<../command_help/snap-always-switch.md>)

  * [snap-to-drillhole-data-switch](<../command_help/snap-to-drillhole-data-switch.md>)

  * [snap-to-perpendicular-switch ("stpe")](<../command_help/snap-to-perpendicular-switch.md>)

  * [snap-to-plane-data-switch ("stpp")](<../command_help/snap-to-plane-data-switch.md>)

  * [snap-to-point-data-switch ("stpp")](<../command_help/snap-to-point-data-switch.md>)

  * [snap-to-string-data-switch ("stps")](<../command_help/snap-to-string-data-switch.md>)

  * [snap-to-wireframe-data-switch ("stpw")](<../command_help/snap-to-wireframe-data-switch.md>)

  * [set-snap-grid-parameters ("gs")](<../command_help/set-snap-grid-parameters.md>)

  * [set-snap-grid-switch ("stg")](<../command_help/set-snap-grid-switch.md>)

  * [set-snap-lines-switch ("stl")](<../command_help/set-snap-lines-switch.md>)

  * [set-snap-mode ("snm")](<../command_help/set-snap-mode.md>)

  * [set-snap-none-switch ("sn0")](<../command_help/set-snap-none-switch.md>)

  * [set-snap-points-switch ("stpo")](<../command_help/set-snap-points-switch.md>)

  * [set-snap-surface-switch ("sts")](<../command_help/set-snap-surface-switch.md>)