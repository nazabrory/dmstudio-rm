# Generate Cones

To access this screen:

  * In the Command toolbar, run the [cone-from-drillhole](<../command_help/cone-from-drillhole.md>), or [cone-from-string](<../command_help/cone-from-string.md>) command.

  * **Sample Analysis** ribbon **> > Plan >> Cones**.

  * **Sample Analysis** ribbon **> > Plan >> Cones from Strings**.

Generate wireframe cones from selected drillhole or string data. This allows you to visualize potential maximum deviation per unit length to avoid potential drilling pitfalls. 

Note: You can also plan drill and lift deviations using the **[Drillhole Planner](<DrillholePlannerDialog.md>)** , although sometimes it is useful to visualize the full cone to predict outcomes more clearly.

Activity steps:

  1. Load string or drillhole data and display it in any 3D window.

  2. Run the appropriate cone generation command.

The **Generate Cones** screen displays.

  3. Enter the Deviation Per Unit Length This is the maximum expected deviation per unit length of drilling. For example "0.1" could represent 10cm deviation per meter of drilling. If you specify a **Deviation Field** (see below) this becomes the default deviation value in absence of deviation records downhole.

  4. Deviation Field If you data object contains a numeric field with deviation data, use this to determine the deviation downhole in precedence to a fixed **Deviation Per Unit Length** (using that in the absence of record data).

  5. Start Radius By default, deviation is zero at the collar position of the hole, but you can change this by specifying a non-zero positive value. This can be useful if the collar table coordinates aren't 100% reliable.

  6. Enter a Minimum Segment Length The smallest segment length for which new triangles are generated in the wireframe cone (default '0'). If a drillhole file contains small sample lengths, specifying a minimum segment length will prevent the creation of wireframes with a very large numbers of triangles.

  7. Optional, specify a Name Field in the drillhole (existing) that is copied to the output wireframe cone. For example, a borehole identifier to ensure wireframe cones and originating drillholes can be associated.

  8. Click **OK** to generate cone data.

  9. Save your project.

Related topics and activities:

  * [cone-from-drillhole](<../command_help/cone-from-drillhole.md>)

  * [cone-from-string](<../command_help/cone-from-string.md>)