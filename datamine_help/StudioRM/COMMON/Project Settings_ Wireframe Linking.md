# Project Settings: Wireframe Linking

To access this screen:

  * Display the [Project Settings](<ProjectSettings.md>) screen and select the Wireframe Linking tab.

This screen is used to configure string-linking settings, including end linking and DTM creation commands.

## Linking Methods

These settings define the general method used to link string data. The following options are available:

  * 3D Solid: Enforce a proprietary linking algorithm, and the results may be the same or different from the other linking methods, depending on different string layouts. The 3D Solid approach is particularly adept at overcoming the problems associated with bifurcated wireframe generation (see [Trouser Leg Problem](<../command_help/link-boundary.md>)). 

See [[3D Solid Linking](<3D%20Solid%20Linking%20Method.md>).](<3D%20Solid%20Linking%20Method.md>)

  * Minimum surface area: If selected, the triangulation between selected strings has the minimum overall wireframe surface area.

  * Equi-angular shape: This is the default string linking approach, meaning the resulting triangulation between selected strings generates triangles where the preferred shape is equi-angular.

What does this mean? One measure of the shape of the triangle is the radius of the circumcircle fitted through the three vertices of the triangle. If the three points on the two strings selected to form a triangle minimise the circumcircle radius, this will generate a well shaped triangle. If the three edges were of equal length, the triangle would be an equilateral, and if two edges are of equal length then an isosceles triangle is formed with equal angles at the base of the triangle. If the optimal triangulation minimises the sum of the circumcircle radii of the triangles formed, then the preferred shape will be equi-angular.

  * Proportional length: If selected, triangulation generates triangles where the triangle edges are similar proportional distances along the two strings.  This criteria works best where the shapes of the two strings are similar.

If the shape of the strings is dissimilar, then to get best results tag strings should be used to link together those string sections that are similar. The starting edge for the triangulation is determined either by a user defined tag string, or selected by the system using the closest pair of points on the two strings to be linked. The triangles are formed to best maintain their proportional position along the two strings.

If multiple tag strings are supplied, then the proportional position is defined between adjacent pairs of tag strings. For any pair of strings this method can only generate one link. If this criteria is selected and the toggle linking-method-switch is set on for optimal linking, then the equiangular shape method (link-radii-method switch) will be used.

**Note** : Although not set as the default string linking criteria, **Proportional length** will always be the fastest because no Optimization is involved. Where the shapes are similar this method can often produce the best link, particularly if tag strings are used judiciously. If string shapes are not similar then the other criteria (equi-angular shape, minimum surface area) work more effectively.

## String Linking Control

These settings determine the way in which the linking method (see above) is applied. The following options are available:

  * Optimal linkingtoggle between optimal and sub-optimal (fast) linking methods. If turned on, when linking strings the wireframe will be created optimally with the best surface being selected from those that satisfy the linking criterion. If turned off the linking will be done with tag strings - either user supplied, or if none exist then the closest pair of points on the two strings after translation to a common centre of gravity will form an implicit tag string. Each pair of tag strings is linked independently. The speed advantage of the sup-optimal increases with an increasing number of string points. If the sub-optimal method fails then linking will default to the optimal method.

**Note** : The Optimal linking option does not apply to the 3D Solid Linking method, and is unavailable if that method is chosen.

  * Link crossover checkingtoggle crossover checking on or off for string linking. If the crossover toggle is on then any link that would contain crossovers is automatically rejected. Crossover checking will _increase the processing time_ , especially where the strings have a large number of points. For regular string shapes the user may elect to set crossover checking off, but a wireframe intersection check is still recommended.

    * If sub-optimal linking has been selected and fails then optimal linking will be tried. If optimal linking also fails and you have checked that there are no crossovers in the strings, the best strategy is to:

    * Switch crossover linking off.

    * Complete the link.

    * Use the wireframe intersections command ([wf-intersections](<../command_help/wf-intersections.md>)) to locate the crossover.

  * End link multiple stringsif **checked** , the ends of volumes generated by a string linking operation are automatically closed.

  * Use tag stringstoggle the use of tag strings on or off for string linking. Tag strings can provide additional control when string linking. This toggle controls whether the tag strings are considered or ignored when creating a link between strings. The tag strings that may be required for sub-optimal linking to achieve the required shape and avoid crossovers may be unnecessary for optimal linking.

  * Wireframe attributes from stringstoggle the source of wireframe attributes between taking attributes from the original strings (checked) or using default wireframe attribute values.

  * **Maximum Segment Length** this setting limits the maximum distance between wireframe points (the maximum length of a wireframe mesh segment) when linking strings, including end linking and DTM creation. If zero, triangulation will attempt to complete using the minimum number of triangles but if greater than zero, wireframe data will be generated with triangle edge lengths limited to the value specified. 

**Note** : This value can also be set via the [dtm-new-point-separation ("nps")](<../command_help/dtm-new-point-separation.md>) command.

## 3D Solid Options

Specify default settings for the [link-multiple-strings](<../command_help/link-multiple-strings.md>) command, and the initial values shown on the [Link Multiple Strings](<3D%20Solid%20Dialog.md>)screen. The following options are available:

  * Collate by distanceif **checked** , the Collate by distance value specifies the maximum distance between strings for them to be considered on the same level. 

**Note** : this state can also be toggled using the [link-3dsolid-collate-switch](<../command_help/link-3dsolid-collate-switch.md>) command.

  * Use current view planeif **checked** , an attempt is made to sort the selected strings into groups according to their depth in current view coordinates. It is normally sufficient to leave this check box cleared, in which case, the 3D Solid algorithm will sort strings using its own criteria. 

**Note** : this state can also be toggled using the [link-3dsolid-view-plane-switch](<../command_help/link-3dsolid-view-plane-switch.md>) command.

  * Align strings **check** to create automatic virtual tag lines, which control how the strings are linked together. 

**Note** : this state can also be toggled using the [link-3dsolid-align-switch](<../command_help/link-3dsolid-align-switch.md>) command.

  * Uniform Interpolationapply a unit length parameterisation to the string segments between tag strings. That is, the vertices from one string are imprinted onto the other (vice versa) as if one cut each string, stretched both out to the same length, imprinted temporary vertices and formed connections; finally restoring the original string shapes. The wireframe is generated using both the temporary and original string vertices. 

**Note** : this state can also be toggled using the [link-3dsolid-interp-switch](<../command_help/link-3dsolid-interp-switch.md>) command.

Related topics and activities

  * [Project Settings:Wireframing](<Project%20Settings_Wireframing.md>)

  * [Link Multiple Strings](<3D%20Solid%20Dialog.md>) (screen)

  * [3D Solid Linking Method](<3D%20Solid%20Linking%20Method.md>)

  * [ link-multiple-strings](<../command_help/link-multiple-strings.md>)

  * [link-3dsolid-align-switch](<../command_help/link-3dsolid-align-switch.md>)

  * [link-3dsolid-collate-switch](<../command_help/link-3dsolid-collate-switch.md>)

  * [link-3dsolid-method-switch](<../command_help/link-3dsolid-method-switch.md>)

  * [link-3dsolid-view-plane-switch](<../command_help/link-3dsolid-view-plane-switch.md>)

  * [link-radii-method-switch ("tea")](<../command_help/link-radii-method-switch.md>)

  * [dtm-new-point-separation ("nps")](<../command_help/dtm-new-point-separation.md>)