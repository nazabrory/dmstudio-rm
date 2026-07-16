![](../HeaderCell.jpg) |  Exporting VR Data to a 3D PDF File How to set up and export VR window data to a 3D PDF File.  
---|---  
  
# Overview

In this portion of the tutorial you are going to set up data in the VR window and export it to a 3D PDF file.

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Links to exercises

The following exercises are available on this page:

  * Exporting 3DVR Data to a 3D PDF File

## Exercise: Exporting 3DVR Data to a 3D PDF File

![note.gif \(1017 bytes\)](../images/Tip.gif) |  The main uses for and characteristics of these interactive 3D formats include:

  * distribution, collaboration and sharing of interactive spatial data in a standard, high quality, compressible format, by both engineering and non-engineering staff
  * no need to have specialized 3D visualization software i.e. commonly available, simple to operate PDF viewers can be used to view these files
  * embedding in PowerPoint presentations without the need for plug-ins
  * inclusion in technical reports.

  
---|---  
  
In this exercise, you are going to create a 3D *.pdf format file from the data loaded in the VR window, using the PDF3D export function; this file will then be viewed using Adobe Acrobat. This includes the following tasks:

  * Displaying and Formatting Loaded Data
  * Deleting and Creating New Viewpoints
  * Creating the 3D PDF File
  * Viewing the 3D PDF File.

**Displaying and Formatting Loaded Data**

  1. Select the 3DVR window.
  2. Unload any data that may be loaded from previous exercises.
  3. Using the Project Files control bar and drag the following files into the 3DVR window:

  1.      * _vb_holes(drillholes)
     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_mintr/minpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)

  4. In the Sheets control bar, fully expand the 3DVR folder.
  5. Turn ON the display of only the following Overlays (i.e. check the boxes to the left of each item):  
  

     * _vb_holes(drillholes)
     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_mintr/minpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)  
  
![note.gif \(1017 bytes\)](../images/note.gif)| Make sure that all other overlays, including 3DVR Objects are not displayed.  
---|---  
  6. Using the Format Display dialog, format each of the following Overlays, setting the Style tab, Display As options to Faces:  

     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_mintr/minpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)
  7. Using the Format Display dialog, format _vb_holes(drillholes) by setting the String Name Column to [BHID] and selecting Show Name.

  8. In the Section toolbar, check that the No Clipping option is selected.   
  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  Unlike the Design window, which has a single clipping associated with the View Plane, clipping in the VR window is associated with each defined Section. The overall displayed clipping is thus a result of the cumulative effect of all enabled clipping limits. The clipping parameters are set and enabled/disabled for each section in the Section Properties dialog's Clipping group. The No Clipping option button can only be used to turn clipping OFF; use the Clip Back and Clip Front option buttons to turn clipping ON.  
---|---  
  9. Use the  View ribbon to select  Zoom Fit | Zoom Plan In the  VR View Navigation toolbar, click  Plan .
  10. Compare your 3DVR view with that shown below:  
  
![](../Images/Plot35.jpg)  

**Deleting and Creating New Viewpoints**

  1. Using the  View ribbon select  Viewpoints | Store In the  VR Viewpoints toolbar, click  Store Viewpoint .
  2. Select  Zoom Fit | Zoom West In the  VR View Navigation toolbar, click  West .
  3. Compare your 3DVR view with that shown below:  
  
![](../Images/dp_Export%20To%203D%20PDF%202.jpg)
  4. Using the  View ribbon select  Viewpoints | Store In the  VR Viewpoints toolbar, click  Store Viewpoint .
  5. In the Sheets control bar, 3DVR Objects folder, check that the two new viewpoints, i.e. Viewpoint 1 and Viewpoint 2, are listed.

  6. Select Split Horizontally.

  7. Select the lower window and choose [Viewpoint 2] from the drop-down list.

  8. Select the upper window and choose [Viewpoint 1] from the drop-down list.

  9. Check your results against the data shown below:  
  
![](../Images/Plot36.jpg)

  10. Note how the view alignment corresponds to the original view settings, but the data is not automatically scaled to fit the confines of the split window. This is expected behaviour for a view definition - the zoom factor will be applied as per the original data scale (when the viewpoint was created). If you wish to create a view that is zoomed to show all data in a horizontal split window, you will need to zoom the data in each window (either re-run the Zoom Fit commands or manually zoom) then save 2 new viewpoints; one for each 'half window', e.g.:  
  
![](../Images/Plot37.jpg)

  11. Go back to a single view, ready for a PDF3D export (click the Split Horizontal button again).

Creating the 3D PDF File

  1. With the 3DVR window displayed, activate the Data ribbon and select Data | Export PDF3Dselect File | Export to PDF3D.

  2. In the Export to PDF3D dialog, Filename field, click Browse.

  3. In the Save As dialog, select your tutorial folder, define the file name as 'VR Data 1', select the Save as type [.pdf], click Save:  
  
![](../Images/dp_Export%20To%203D%20PDF%203.jpg)

  4. Back in the Export to PDF3D dialog, Options group, select Only export visible objects(theExport labelscheck box is enabled by default, but there are no labels to display so this setting is not relevant), click OK:  
  
![](../Images/Plot38.jpg)

Viewing the 3D PDF File

![note.gif \(1017 bytes\)](../images/note.gif)| GeneralThe following steps show the use of Adobe Acrobat™ for viewing the 3D PDF file. Other PDF viewers work in a similar manner.Please note that Adobe Acrobat or any other PDF 3D content viewer is not provided nor supported by Datamine.Depending on what PDF viewer you have installed and what program is by default associated with the 3D PDF file types (.pdf, .u3d, .prc), the exported file is automatically opened with the default viewer. If this does not happen, then using Windows Explorer, browse to your project folder and open the exported file.Double-sided RenderingIn the 3DVR window, wireframes are by default displayed as double-sided surfaces (see the Wireframe Properties dialog, General tab, Face Direction group).InAdobe Acrobat, the double-sided rendering option is by default turned OFF. If your exported file is displayed as shown below (i.e. the green topography surface and part of the orange fault surface appear to be 'missing'), then the double-sided rendering is currently disabled:![](../Images/dp_Export%20To%203D%20PDF%205.jpg) To turn it on (for the current and future sessions), use the following procedure:

  * In Adobe Acrobat , select Edit | Preferences,
  * In the Preferences dialog, 3D & Multimedia tab, Renderer Options group, select the Enable double-sided rendering option, click OK.

  
---|---  
  
  1. In the Adobe Acrobat dialog, compare your view of the data to that shown below:   
  
![](../Images/dp_Export%20To%203D%20PDF%206.jpg)

  2. In the main window, use click-and-drag to rotate the view, <Shift> \+ click-and-drag to zoom and <Ctrl> \+ click-and-drag to pan the view.

  3. In the 3D toolbar, Views drop-down, select the saved viewpoint [Viewpoint 1]:  
  
![](../Images/dp_Export%20To%203D%20PDF%207.jpg)

  4. Compare your view to that shown below:  
  
![](../Images/dp_Export%20To%203D%20PDF%208.jpg)

  5. Open the Model Tree control bar and expand the Wireframes and Strings folders and confirm that the displayed overlays have been exported:  
  
![](../Images/dp_Export%20To%203D%20PDF%209.jpg)

  6. Right-click on different model objects and explore the various context menu options.

  7. Close the Adobe Acrobat dialog when you have finished viewing the 3D model.

![](../Images/NextExercise.gif)[Proceed to the next topic](<Exporting_VR_Data_to_Animated_3DPDF_File.md>)