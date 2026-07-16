# Format Display: Advanced

To access this screen:

  1. Display the [Format Display](<Format%20Overlays%20Dialog.md>) screen.

  2. Select a string object overlay.

  3. Select the **Advanced** tab.

Specify how string overlay data that falls within the secondary clipping zones is formatted; to specify first string points and selected strings point scaling options.

The following options are available:

Secondary Clipping  
---  
Front |  Configure the format of data that falls within the [secondary clipping region](<../PLOTS_LOGS/ClipView.md>) of a projection, and specifically, in front of the active 3D section. You can either:

  * Choose a **fixed** line format, line width and colour, or;
  * Choose a **legend** and **attribute** (containing linestyle codes) for variable formatting throughout the overlay. If you choose this option, you can also elect to Hide values not in legend, meaning data that can't be matched to a legend interval is not displayed.

  
Back | As above, but configure formatting for data that falls behind the active section, in the secondary clipping region.  
Filled | If checked, string data within the secondary clipping region is filled if the string is closed.  
Symbol Size Adjustments  
First symbol |  Select the size of the first line symbol. Your options are:

  * No adjustment
  * _Set_ Choose a symbol size in screen dimensions.
  * _Scale_ Define a factor by which the current symbol size is multiplied.  Tip: This can be useful to exaggerate the difference between symbols applied using a legend lookup.

  
Selected strings |  As above, but change all symbols of selected line data.  Tip: This can help to distinguish selected data from the rest of the pack in a busy projection requiring manual editing of point positions.  
  
Related topics and activities:

  * [Format Display](<Format%20Overlays%20Dialog.md>)

  * [Clipping Plots Data](<../PLOTS_LOGS/ClipView.md>)

  * [Format Display: Symbols](<format%20display%20dialog_overlays_symbols.md>)