# Insert Points from Grid

To access this screen:

  * **Digitize** ribbon **> > Edit >> Insert Points >> Insert Using Grid**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "insert-point-segment-center"

  * Use the quick key combination "ipsc".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **insert-point-segment-center** and click **Run**.

Make new string vertices on selected string data, based on XYZ grid intersections. 

When this command is invoked you are prompted for grid intervals along the X, Y and Z axes, followed by the corresponding origin points, which will be used as the basis for the insertion of new vertices. 

If there is a current string, the new vertices will be inserted along it, otherwise the command is modal and the user may select any number of strings, each of which will have new 'gridded' vertices added.

Note: Points are added using a custom grid, unrelated to any previously loaded or displayed grid data.

Activity steps:

  1. Load or digitize a string in a 3D view. 

  2. Select the string data to be modified.

  3. Display the **Insert Points from Grid** screen.

  4. Enter an X/Y/Z Axis interval. This is the distance between points on a grid to be used as a template for the points on a line.

  5. Enter an X/Y/Z Origin to define the origin of the grid used to interpret line points.

  6. Click **OK**.

Selected string data is modified.

Related topics and activities

  * [grid-interval-on-string ("ipg")](<../command_help/grid-interval-on-string.md>)

  * [clip-strings-to-perimeters ("cltp")](<../command_help/clip-strings-to-perimeters.md>)

  * [clip-to-perimeter ("ctp")](<../command_help/clip-to-perimeter.md>)

  * [clip-inside-perimeter ("cip")](<../command_help/clip-inside-perimeter.md>)

  * [clip-outside-perimeter ("cop")](<../command_help/clip-outside-perimeter.md>)