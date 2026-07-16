# VR Data to an Animated 3D PDF File

![](../HeaderCell.jpg) |  Exporting Animated VR Data to a 3D PDF File How to set up and export Animated VR window data to a 3D PDF File.  
---|---  
  
# Overview

In this portion of the tutorial you are going to set up a sequence animation in the 3DVR window and export it to a 3D PDF file.

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Links to exercises

The following exercises are available on this page:

  * Exporting Animated 3DVR Data to a 3D PDF File

## Exercise: Exporting Animated 3DVR Data to a 3D PDF File

![note.gif \(1017 bytes\)](../images/Tip.gif) |  The main uses for and characteristics of these interactive 3D formats include:

  * distribution, collaboration and sharing of interactive spatial data in a standard, high quality, compressible format, by both engineering and non-engineering staff
  * no need to have specialized 3D visualization software i.e. commonly available, simple to operate PDF viewers can be used to view these files
  * embedding in PowerPoint presentations without the need for plug-ins
  * inclusion in technical reports.

  
---|---  
  
In this exercise, you are going to set up a sequence animation for data loaded in the VR window and then export it to a 3D *.pdf format file, using the PDF3D export function; this file will then be viewed using Adobe Acrobat. This includes the following tasks:

  * Displaying and Formatting Loaded Data
  * Defining a Sequence Animation for the Block Model
  * Creating the 3D PDF File
  * Viewing the animated 3D PDF File.

**Displaying and Formatting the Loaded Data**

  1. Unload any data that may be loaded from a previous exercise.
  2. Select the 3DVR window.
  3. In the Project Files control bar, Block Models folder, drag-and-drop the following files into the 3DVR window:  
  
_vb_npvmod1 (block model)  
_vb_faulttr/_vb_faultpt (wireframe)  
_vb_stopotr/stopopt (wireframe)  

  4. In the Sheets control bar, fully expand the VR folder.

  5. Turn ON the display of only the following Overlays (i.e. check the boxes to the left of each item):   
  

     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)
     * _vb_npvmod1 (block model)   

  6. Using the Format Display dialog, format each of the following Overlays, setting the Style tab, Display As options to Faces:   

     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)
  7. Using the Format Display dialog, format _vb_npvmod1 (block model) as follows:

     * in the Display Type group, select the option Blocks
     * in the Options group, select Show Fill and clear all other check boxes
     * in the Color group, select the Column [PUSHBACK] and click Use Default Legend.
  8. In the Section toolbar, check that the No Clipping option is selected.  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  Unlike the Design window, which has a single clipping associated with the View Plane, clipping in the VR window is associated with each defined Section. The overall displayed clipping is thus a result of the accumulative effect of all enabled clipping limits. The clipping parameters are set and enabled/disabled for each section in the Section Properties dialog's Clipping group. The No Clipping option button can only be used to turn clipping OFF; use the Clip Back and Clip Front option buttons to turn clipping ON.  
---|---  
  9. Using the  View ribbon, select  Zoom Fit | Zoom West In the  VR View Navigation toolbar, click  West .
  10. Double-click the _vb_npvmod1 item found in the Sheets | 3D | Block Models section.
  11. Set the Display type to Blocks.
  12. Ensure the Legend option is select and the [PUSHBACK] column is selected. Use the default legend for this column.
  13. Compare your view with that shown below:  
  
![](../Images/dp_Export%20To%20Animated%203D%20PDF%201.jpg)

Defining and Testing a Sequence Animation for the Block Model

  1. In the Sheets control bar, 3DVR \- Block Models folder, double-click _vb_npvmod1 (block model).
  2. In the Block Model Properties dialog, Sequence Column group, select [PUSHBACK].
  3. In the Sequence Options group, define the following parameters, click OK:  

     * select the Single Frame option
     * set Anim. Rate to '1'
     * set Anim. Step to '1'
     * select the Loop option.  
  
![note.gif \(1017 bytes\)](../images/note.gif)| Determining Animation Rate and Step ParametersThe following method can be used to determine a set of starting parameters:
       1. Determine the range of the values for the selected sequence column
       2. Determine the Animation Step size
       3. Set the Animation Rate equal to the Animation Step size.
       4. When working with block models, test and adjust the above settings so that block model slices are visible for each step. In this example, a value of 80 was used.
For example, using the block model file _vb_npvmod1 (block model) the and the field XC (block model X-coordinates)
       1. Range = Maximum - Minimum = 6480 - 5660 = 820
       2. Animation Step size = Range / 10 = 820 / 10 = 82
       3. Let Animation Rate = Animation Step size = 82
       4. Adjusted value after testing: 80  
---|---  
  4. In the Sheets control bar, 3DVR \- Block Models folder, right-click _vb_npvmod1 (block model), select Sequence Controls.
  5. In the Sequence Control dialog, click Play.
  6. In the 3DVR view, check that the block model is colored on PUSHBACK and sequenced using the same field (the block model cell pushback number.
  7. In the Sequence Control dialog, click Stop and then close the dialog.

Creating the 3D PDF File

  1. With the 3DVR window displayed, select File | Export to PDF3D.

  2. In the Export to PDF3D dialog, Filename field, click Browse.

  3. In the Save As dialog, select your tutorial folder, define the file name as 'Animated VR Data 1', select the Save as type [.pdf], click Save:  
  
![](../Images/dp_Export%20To%20Animated%203D%20PDF%202.jpg)

  4. Back in the Export to PDF3D dialog, Options group, select Animation, click OK:  
  
![](../Images/Plot39.jpg)  

![note.gif \(1017 bytes\)](../images/note.gif) |  Selecting the Animation option automatically also only exports the displayed (visible) objects.  
---|---  

Viewing the Animated 3D PDF File

![note.gif \(1017 bytes\)](../images/note.gif)| GeneralThe following steps show the use of Adobe Acrobat™ for viewing the 3D PDF file. Other PDF viewers work in a similar manner.Please note that Adobe Acrobat or any other PDF 3D content viewer is not provided nor supported by Datamine.Depending on what PDF viewer you have installed and what program is by default associated with the 3D PDF file types (.pdf, .u3d, .prc), the exported file is automatically opened with the default viewer. If this does not happen, then using Windows Explorer, browse to your project folder and open the exported file.Double-sided RenderingIn the VR window, wireframes are by default displayed as double-sided surfaces (see the Wireframe Properties dialog, General tab, Face Direction group).InAdobe Acrobat, the double-sided rendering option is by default turned OFF. If your exported file is displayed as shown below (i.e. the green topography surface and part of the orange fault surface appear to be 'missing'), then the double-sided rendering is currently disabled:![](../Images/dp_Export%20To%20Animated%203D%20PDF%204.jpg) To turn it on (for the current and future sessions), use the following procedure:

  * In Adobe Acrobat , select Edit | Preferences,
  * In the Preferences dialog, 3D & Multimedia tab, Renderer Options group, select the Enable double-sided rendering option, click OK.

  
---|---  
  
  1. In the Adobe Acrobat dialog, compare your view of the 3D model to that shown below:   
  
![](../Images/dp_Export%20To%20Animated%203D%20PDF%205.jpg)

  2. In the Animation toolbar, click Play.

  3. Note how the block model is animated in south-north orientated slices, moving in steps from back (west) towards you (east):  
  
![](../Images/dp_Export%20To%20Animated%203D%20PDF%206.jpg)

  4. In the Animation toolbar, click Stop.

  5. Explore some of the other Animation toolbar options.

  6. Close the Adobe Acrobat dialog when you have finished viewing the animated 3D model.