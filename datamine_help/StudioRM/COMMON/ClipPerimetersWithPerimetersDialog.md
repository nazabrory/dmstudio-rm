# Clip Perimeters to Perimeters

To access this screen: 

  * **Digitize** ribbon **> > Tools >> Clip Strings >> Clip Perimeters to Perimeters**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "clip-perimeters-to-perimeters"

  * Use the quick key combination "cptp".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **clip-perimeters-to-perimeters** and click **Run**.

This screen is used to select two distinct groups of perimeter data, and use one set of perimeters (the Clipping Perimeters) to clip the other (the Perimeters to Clip). All data must be closed strings.

Data can be clipped so that the data that is within the clipping scope is retained, or the data outside is retained.

Data is assigned as either a 'clipper' or is 'clipped' using each of the two Store Current Selection buttons. Selecting either will transfer the perimeter data (ignoring open strings and other data types) to the corresponding group. Once data has been stored, the number of perimeters for the category is displayed. Perimeter data can be part of any displayed object, or even selected from multiple objects.

Once perimeter data has been stored, selecting an X perimeter(s) stored button highlights that data in a 3D window.

Also see [Clip Strings to Perimeters](<ClipStringsWithPerimetersDialog.md>).

To clip a perimeter to another perimeter:

  1. Ensure at least two overlapping perimeters (closed strings) are visible in a 3D window.

  2. You can either preselect data (to be clipped, or to form the clipping perimeter) in advance of launching the **clip-perimeters-to-perimeters** command, or you can select data after the command is run.

  3. Pick the clipping boundary string(s) interactively by clicking in any 3D window and choose to **Store Current Selection** for the **Clipping Perimeters**. These strings will not be modified.

  4. Do the same to **Store Current Selection** for **Perimeters to Clip**. These are the strings that are modified.

  5. Choose which data you want to keep using **Keep Mode** options:

     * Keep portion within any clipping perimeter.

     * Keep portion outside of all clipping perimeters.

You can choose to retain both data categories, in which case the current string object is populated with two distinct groups of string traces.

Related topics and activities

  * [clip-strings-to-perimeters ("cltp")](<../command_help/clip-strings-to-perimeters.md>) (command)

  * [clip-perimeters-to-perimeters](<../command_help/clip-perimeters-to-perimeters.md>) (command)

  * [clip-inside-perimeter](<../command_help/clip-inside-perimeter.md>) (command)

  * [clip-outside-perimeter](<../command_help/clip-outside-perimeter.md>) (command)

  * Clip Perimeters to Perimeters (screen)

  * [Clip Strings to Perimeters](<ClipStringsWithPerimetersDialog.md>) (screen)