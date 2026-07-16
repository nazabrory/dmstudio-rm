# generate-distance-contours 

See this command in the [**command table**.](<COMMAND%20TABLE_G.md#generate-distance-contours>)

To access this command:

  * **Implicit** ribbon >> **Contour** >> **Distance**.

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **generate-distance-contours** and click **Run**.

  * Enter "generate-distance-contours" into the [**Command Line.**](<../COMMON/Command_Toolbar.md>)

## Command Overview

This command is used to model contours representing the distance from sample positions.

A points file must be loaded to access this command. Attributes are not considered with this command.

The outputs from this command are (optionally) contours strings and an output grid model. You cannot generate an output surface with this command, as the resulting strings and grid model are assigned a fixed elevation.

By default, the grid model will lie just below the output strings, to allow them both to be visualized easily, for example:

You can change these settings using the [Generate Contours - Output Data](<../COMMON/GenerateContourOutputPage.md>) page.

This command uses the Generate Contours screen:

  1. Define the scope of contouring; select input objects.
  2. Define the extents of your contouring by setting a minimum and maximum X and Y of the data hull (with an optional margin) and the resolution of the output grid.
  3. Choose if you want to output contour strings and/or a grid object (a block model)
  4. Configure how contour strings are created; define the lowest and highest values (and interval) and at which elevation you wish your output data to be positioned.

For more information on this command, please refer to [Distance Contours.](<../COMMON/Contours_Distance_Introduction.md>)

Related topics and activities

  * [Distance Contours](<../COMMON/Contours_Distance_Introduction.md>)

  * [generate-contours-from-holes-intercepts](<generate-contours-from-holes-intercepts.md>)

  * [generate-contours-from-points](<generate-contours-from-points.md>)

  * [Contours from Points - Introduction](<../COMMON/Contours_From_Points_Intro.md>)