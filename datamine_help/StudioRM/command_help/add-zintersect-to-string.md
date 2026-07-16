# add-zintersect-to-string ("azs")

See this command in the [**command table**.](<_COMMAND%20TABLE_A.md#add-zintersect-to-string>)

To access this command:

  * **Digitize** ribbon **> > Edit >> Insert Points >> Insert at Z Intersect**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter `add-zintersect-to-string`.

  * Use the quick key combination "azs".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate _add-zintersect-to-string_ and click **Run**.

## Command Overview

Add one or more vertices to string data at the specified elevation

String shape is unaffected by this command. An additional vertex (or vertices where a string passes through the same elevation more than once) is added to the target string.

  * If you **select data first** , only that selection is updated. If no intersection can be found between the string and the target elevation in this scenario, the command ends.

  * If **no data is selected** , once an elevation is picked, successive strings can be picked. If no intersection can be found for any data, a message is shown.

Command Steps:

  1. Optionally, select string data in a **3D** window. If data is preselected, only that data is modified, if possble.

  2. Run the command.

  3. Enter a Z Intersect Value. This is the elevation (the Z value) that is used to create a new point on the target string data. 

  4. Click **OK**.

If data **was preselected** , a new data point is added to any occurrence of the string passing through the target elevation.

If data **was not preselected** , pick a string to update. 

  5. If data wasn't preselected beforehand, click **Done** to complete the command. If data was preselected, the command ends automatically.

Related commands and activities

  * [insert-points-mode](<insert-points-mode.md>)

  * [insert-point-segment-center](<insert-point-segment-center.md>)

  * [insert-at-intersections](<insert-at-intersections.md>)

  * [insert-by-segment-length](<insert-segment-by-length.md>)