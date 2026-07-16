# Clean Wireframe

To access this screen:

  * **Wireframe** ribbon **> > Fix >> Clean**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-clean"

  * Use the quick key combination "wcl".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-clean** and click **Run**.

Fix problems in wireframes found using the **[wireframe-verify](<../command_help/wireframe-verify.md>)** command. 

**Note** : as wireframe cleaning also identifies topologies, it can be used as an alternative to wireframe-verify where wireframes need to have consistent normals (triangle direction) generated.

Different options exist for open (DTM) and closed volumes. 

You can either clean a full, selected wireframe object or preselected wireframe triangles. The latter option can be useful when rectifying crossovers or near-coincident points in imported surface data, and the problematic area is known, for example.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

Command steps:

  1. Choose the data to be cleaned:

     * Clean an entire wireframe Objectselect the wireframe to be cleaned. A list of all loaded wireframes is available. The current wireframe is picked by default. 
     * Clean up a subset of a wireframe with Selected trianglesif you have previously selected wireframe triangles, or intend to select them before running the **wireframe-clean** command, select this option. Selected triangles can be part of any loaded wireframe object(s).

  2. Optionally, select the **Key field** attribute which contains unique values for each region to be cleaned. These distinct zones are processed separately and concatenated in the final result.

**Tip** : where a loaded wireframe contains distinct geological or developmental zones, it is recommended that you use the Key field to identify them as this allows each zone to be cleaned independently.

  3. Choose your **Output Wireframe** options.

**Note** : if you are cleaning an entire wireframe **Object** , you can't overwrite the original data and a new data object must be specified. 

     * If selected triangles are being cleaned, you can choose to output the cleaned data to the **Current Object** , updating it (not duplicating triangles).

     * For any **Input WIreframe** scenario, enter the name of a **New object** to be created, containing cleaned output.

  4. To define General Options:

These settings apply to both DTMs and closed volumes:

     * Remove planar holesif checked, the clean routine detects any area surrounded by a boundary of open edges, and triangulate the boundary to fill the hole. Any triangulations which would cause crossovers within the wireframe are discarded. This option should be used with some caution with DTMs as they have an outer boundary of open edges, the option can be used to close a DTM to make a closed solid, for example:

[![](../Images/wireframe%20clean%201.png)](<javascript:void\(0\);>)   
However, this is not possible if the elevations of the DTM boundary cross over the elevations within the DTM boundary, for example:

[![](../Images/wireframe%20clean%202.png)](<javascript:void\(0\);>)

For these DTMs and for closed solids, the hole removal is intended as a remedial method to fix gaps in the triangulation, possibly caused by digitising errors or other problems:

[![](../Images/Wireframe%20clean%203.png)](<javascript:void\(0\);>)

The new triangles created during the fill process have default attributes applied

     * .**Remove Crossovers** crossovers are formed when triangles intersect at somewhere other than their boundary. The crossover removal will break any intersected triangles along their intersection line, and then attempt to resolve these into new volumes. For example, in the following image, a simple hour glass shape with crossing lines (blue) has been extruded into a volume. The red line shows the triangle crossovers detected from the wireframe verify function. The wireframe is coloured by surface, showing that the verify function has detected a single surface with crossovers.

[![](../Images/Wireframe%20clean%204.png)](<javascript:void\(0\);>)   
The cleaned version of the wireframe shows 2 adjacent surfaces, and no crossovers. 

**Tip** : combine crossover removal with removing small volumes. This can then remove the tiny fragments caused when adjacent surfaces intersect but almost align.

     * **Snap points closer than** \- if checked, this will snap any close wireframe points together before performing any other operations.

**Warning** : use this setting with caution as it snaps points regardless of topology so can cause issue such as shared or open edges, if the tolerance is too high.

     * Remove edges less thansome modelling processes may generate small sliver triangles which can complicate downstream processes or simply increase wireframe file size for no gain. Removing small edges can be thought of as a very simple form of decimation, to remove these trivial triangles. When a triangle edge is encountered which is less than the value specified, the edge is collapsed to one of the existing vertices, resulting in the smaller triangle being deleted and one of the adjacent triangles growing to fill the gap.

[![](../Images/Wireframe%20clean%205.png)](<javascript:void\(0\);>)

     * Remove T Junctions t-junctions are formed when 2 adjacent triangles shared a common edge with a third triangle. Because this stops the triangles from being connected properly, verify detects these as open edges (or sometimes crossovers). When the gap between the point shared by the 2 triangles and the edge of the third falls below the Tolerance value, the third point is snapped to the third triangle, which will then be split using the move point, or the 2 triangles collapsed.

[![](../Images/Wireframe%20clean%206.png)](<javascript:void\(0\);>)

To define Closed Volume Options:

These options are intended for use closed wireframes. 

**Warning** : using these settings with DTMs may result in the entire wireframe being deleted. No checks are performed for this at run time, so make sure you make a back up of your data beforehand if it is not a closed volume.

  * **Remove interior triangles**if **checked** , remove all the triangles within a closed volume, essentially returning the outer shell. Note that if the internal triangles form a valid internal closed volume, then they will not be removed. In the image below, the combined boxes still have some triangles left over from the common edge. The section through the boxes show the triangles are removed after the wireframe cleaning:

[![](../Images/Wireframe%20clean%207.png)](<javascript:void\(0\);>)

  * **Remove hanging sheets** as an alternative to the example above, a cleaner volume could be produced using the hanging sheets removal option. This is not just restricted to internal triangles, but potentially any triangle with an open edge. Triangles are then progressively deleted if they are found to contain open edges. This process continues until all remaining triangles are fully connected.

**Warning** : enabling this setting can cause an entire wireframe to be deleted so should be considered a high-risk option. This could happen, for example, if the option was selected for a closed volume with a hole in the surface.

[![](../Images/Wireframe%20clean%208.png)](<javascript:void\(0\);>)

  * Remove volumes less thanafter a series of complicated wireframe processes, e.g. multiple Booleans, or isoshell generations, its sometimes possible to have a series of small volumes produced which can be attributed to small errors in the original digitising, the result of re-triangulation causing similar surfaces to become slightly different or other reasons. The wireframe cleaning utility allows for all closed volumes below a specified amount to be removed, leaving only the larger, more significant volumes.

[![](../Images/Wireframe%20clean%209.png)](<javascript:void\(0\);>)

  * Remove thicknesses less thanthis option will remove those parts of a volume which have pinched down to a thickness less than the specified amount, leaving a volume concentrated around the areas of non-trivial thickness.

**Tip** : this option can sometimes lead to crossovers, so it is recommended that the Remove crossovers option is used as well (see above).

Related topics and activities

  * **[wireframe-clean](<../command_help/wireframe-clean.md>)** (command)

  * **[Verify Wireframe](<Wireframe%20Verify%20Dialog.md>)**