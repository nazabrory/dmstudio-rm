# link-shape-method-switch ("tpr")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-shape-method-switch>)

To access this command:

  * On the [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>) screen, select the **Proportional length** setting.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-shape-method-switch"

  * Use the quick key combination "tpr".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-shape-method-switch** and click **Run**.

## Command Overview

Select proportional length as the string linking criteria.

If toggled on, the resulting triangulation between selected strings generates triangles where the triangle edges are similar proportional distances along the two strings.

This criteria works best where the shape of the two strings is similar. If the shape of the strings is dissimilar, then to get best results tag strings should be used to link together those string sections that are similar.

The starting edge for the triangulation is determined either by a user defined tag string, or selected by the system using the closest pair of points on the two strings to be linked. The triangles are formed to best maintain their proportional position along the two strings.

If multiple tag strings are supplied, then the proportional position is defined between adjacent pairs of tag strings.

For any pair of strings this method can only generate one link. If this criteria is selected and the toggle [linking-method-switch](<linking-method-switch.md>) is set on for optimal linking, then the equiangular shape method (link-radii-method switch) is used.

Although not set as the default string linking criteria, it will always be the fastest because no Optimization is involved. Where the shapes are similar this method can often produce the best link, particularly if tag strings are used judiciously. If string shapes are not similar, the other criteria (equi-angular shape, minimum surface area) can work more effectively.

### Using the 3D Solid linking method

If you have strings on adjacent sections that are to be linked together, and those strings cross each other when viewed in the direction of wireframing, then temporary vertices are inserted into the string and these temporary vertices are used when the wireframe is created. Since pairs of strings are wireframed at a time it is possible for these temporary vertices to be created for one pair of strings and not the other. In this situation a wireframe may be built which contains inconsistencies. 

Therefore, the 3D-Solid method is not suitable for use with the older linking commands if adjacent sections contain strings that cross each other in the direction of wireframing.

See [**3D Solid linking method**.](<../COMMON/3D%20Solid%20Linking%20Method.md>)

Related topics and activities

  * [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)

  * [link-3dsolid-interp-switch](<link-3dsolid-interp-switch.md>)

  * [link-3dsolid-align-switch](<link-3dsolid-align-switch.md>)

  * [link-3dsolid-view-plane-switch](<link-3dsolid-view-plane-switch.md>)

  * [link-3dsolid-collate-switch](<link-3dsolid-collate-switch.md>)

  * [link-selected-string-el-switch](<link-selected-string-el-switch.md>)

  * [link-area-method-switch ("tma")](<link-area-method-switch.md>)

  * [linking-method-switch ("tlm")](<linking-method-switch.md>)