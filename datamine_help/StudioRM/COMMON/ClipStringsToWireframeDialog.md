# Clip Strings to Wireframe

To access this screen:

  * **Digitize** ribbon **> > Tools >> Clip to Perimeter >> Clip to Surface**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "clip-strings-to-wireframe".

  * Use the quick key combination "cltw".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **clip-strings-to-wireframe** and click **Run**.

Clip selected string data to loaded wireframe surface or volume data.

Select the clipping wireframe and (if an open surface is selected) the planar direction used for clipping.

To clip string data to wireframe data:

  1. Load the string data to clip and the wireframe data to act as the clipping boundary.

Note: Data from multiple wireframe objects can be used for clipping, but all clipping wireframes must be either closed volumes or open surfaces. You can't pick a combination.

  2. Select the string data to be clipped (data from any string object can be selected.

**Note** : Only selected string data is clipped.

  3. Display the **Clip Strings to Wireframe** screen.

  4. Review the Strings to Clip. This displays the number of currently stored strings (and the number selected when the screen displayed initially. 

Note: Select string data whilst the **Clip Strings to Wireframe** screen is displayed and click **Store current selection** to update the string collection that is clipped when the command is run.

  5. Choose if Closed volume(s) or **Open surface(s)** are being used for clipping.

     * If you are clipping using an **open surface** (say, a topography), choose the **Plane Orientation** that will determine which aspect of string data is clipped and which is retained:

       * _Horizontal_ Clip using a horizontal plane. This is useful for topographies or hangingwall surfaces without significant dip.

       * _North-South_ Clip using a vertical plane where the surface is clipped in relation to the N-S plane.

       * _East-West_ As above, but using the E-W plane to determine the clipped region.

**Note** : The planar selection, in combination with **Keep Mode** settings (see below) determines which data is clipped and which data remains.

  6. Choose which data is clipped using **Keep Mode** settings. The options here depend on whether you have chosen **Closed volume(s)** or **Open surface(s)** above.

     * If you are using **Closed volume(s)** to clip string data, the following inclusive options are available:

       * _Keep portion within wireframe_ Check to retain the data within a closed volume or uncheck to clip it.

       * _Keep portion on wireframe_ Check to retain the data at the intersection of the wireframe data or uncheck to clip it.

       * _Keep portion outside wireframe_ Check to retain the data outside a volume or uncheck to clip 

     * If you are using **Open surface(s)** to clip string data, choose one or more

       * _Keep portion behind wireframe surface_

       * _Keep portion on wireframe surface_

       * _Keep portion in front of wireframe surface_

       * _Keep portion out of bounds_ If checked, data that doesn't lie directly above, on or below the wireframe surface (according to the planar direction) is retained. If unchecked, it is clipped.

Note: At least one **Keep Mode** must be selected.

  7. Choose a numeric Tolerance. Data that lies within this distance of the wireframe boundary is clipped, regardless of the 'side' it lies.

  8. Click **Clip**.

Selected string data is clipped.

  9. Save your project.

Related topics and activities

  * [clip-strings-to-wireframe ("cltw")](<../command_help/clip-strings-to-wireframe.md>) (command)

  * [Clip Perimeters to Perimeters](<ClipPerimetersWithPerimetersDialog.md>)
  * [Clip Strings to Perimeters](<ClipStringsWithPerimetersDialog.md>)