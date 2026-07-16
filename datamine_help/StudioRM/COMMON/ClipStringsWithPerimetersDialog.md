# Clip Strings to Perimeters

To access this screen: 

  * **Digitize** ribbon **> > Tools >> Clip Strings**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "clip-strings-to-perimeters"

  * Use the quick key combination "cltp".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **clip-strings-to-perimeters** and click **Run**.

Clip one or more (open or closed) strings to one or more perimeters (closed strings).

Data can be clipped so that the data that is within the clipping scope is retained, or the data outside is retained.

Data is assigned as either a 'clipper' or is 'clipped' using each of the two Store Current Selection buttons. Selecting either will transfer the selected data to the corresponding group. Once data has been stored, the number of strings for the category is displayed. String data can be part of any displayed object, or even selected from multiple objects.

Once perimeter data has been stored, selecting an X perimeter(s) stored button highlights that data in a 3D window, so you can easily see which data is acting as the 'clipper' and which as the 'clipped'.

Also see [Clip Perimeters to Perimeters](<ClipPerimetersWithPerimetersDialog.md>).

To clip string data to one or more perimeters:

  1. Ensure at least two strings are visible in a 3D window with at least one of them closed (and overlapping other string data).

  2. You can either preselect data (to be clipped, or to form the clipping perimeter) in advance of launching the **clip-strings-to-perimeters** command, or you can select data after the command is run.

  3. Pick the clipping boundary string(s) interactively by clicking in any 3D window and choose to **Store Current Selection** for the **Clipping Perimeters**. The perimeter strings will not be modified.

  4. Do the same to **Store Current Selection** for **Strings to Clip**. These are the strings that are modified and can be either open or closed.

  5. Choose which data you want to keep using **Keep Mode** options:

     * Keep portion within any clipping perimeter.

     * Keep portion outside any clipping perimeter.

You can choose to retain the portion inside the perimeter data, or outside, or both (in which case the current string object is populated with two distinct groups of string traces).

Related topics and activities

  * [clip-perimeters-to-perimeters](<../command_help/clip-perimeters-to-perimeters.md>) (command)

  * [clip-inside-perimeter](<../command_help/clip-inside-perimeter.md>) (command)

  * [clip-outside-perimeter](<../command_help/clip-outside-perimeter.md>) (command)