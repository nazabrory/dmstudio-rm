![](../HeaderCell.jpg) |  Creating and Using Sheet Templates How to create and use sheet templates for plots and logs.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and techniques used to create and use sheet templates for plots and logs.

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

  * Copied and renamed the Plan sheet - see exercises on the [Opening, Copying and Inserting Plot Sheets](<Opening_Copying_and_Inserting_Plot_Sheets.md>) page.

Recommended:

  * Displayed the required Overlays - see the exercise on the [Displaying Plot Sheet Data](<Displaying_Plot_Sheet_Data.md>) page.

  * Formatted the required Overlays in the plan sheet - see the exercise on the [Formatting Overlays](<Formatting_Overlays.md>) page.

  * Modified the View settings in the plan sheet - see the exercise on the [Modifying View Settings](<Modifying_View_Settings.md>) page.

  * Changed the Page Setup options - see the exercise on the [Changing Page Setup options](<changing_page_setup_options.md>) page.

  * Moved and Inserted Plot Items - see the exercises on the [Moving and Inserting Plot Items](<moving_and_inserting_plot_items.md>) page.

## Link to exercises

The following exercises are available on this page:

  * Creating a Plot Sheet Template
  * Creating a New Plot Sheet from a Template

## Exercise: Creating a Plot Sheet Template

In this exercise, you are going to create a sheet template from the formatted Plan plot sheet.

![note.gif \(1017 bytes\)](../images/Tip.gif) | 

  * Use a sheet template files to save a particular sheet's layout and formatting settings and as a starting point for creating new sheets. The advantages include:
  *     * improving work flow and efficiency,
    * enabling the standardization of plot and log sheets for:
    *       * your own use across multiple Studio projects,
      * implementing formatting standards within a department, office or organization.
  * Store shared, standard template files outside the project folder in a suitable general folder which can be accessed by other projects or users.

  
---|---  
  
The exercise procedures are as follows:

Creating a Plot Sheet Template - Configuring the initial data

  1. Unload any data that may be loaded from previous exercises (tip: you can do this by clicking inside the Plots window and type 'ua')
  2. Select the Plots window - you should see a display of the dynamic drillhole data created in a previous exercise.
  3. Drag the following files into the Plots window:  
  
_vb_stopo.dm  
_vb_holes.dm
  4. Select the Plan tab. You should see something similar to the following:  
  
![](../Images/Plot28.jpg)  

  5. Use your knowledge gained in the previous Plots exercises to set up the following plot sheet components:  
  
Insert a Title Box plot item with 3 rows \- use your own formatting for fonts, but try and stick to the contents below:  
  
![](../Images/Plot25.jpg)  
  
Position the North Arrow in the top right corner (page layout mode will need to be ON)  
  
Insert a Scale Bar plot item  

  6. Check that the sheet has the correct objects and plot items displayed and that they are formatted, as shown below:  
  
![](../Images/Plot26.jpg)
  7. The topography lines showing through the title box is kind of annoying? Right-click any part of the control and select Title Box Properties. Use the Drawing Order tab to position the Title Box item at the bottom of the list using the Last button. Click OK.
  8. Activate the  Manage ribbon and select  Save | Template Select  File | Save as Sheet Template .
  9. In the Save Sheet Template dialog, browse to your project folder, define File name: as 'Plan - Portrait', select the Save as type [*.dmtpl], click Save:  
  
![](../Images/dp_Creating%20a%20Plot%20Sheet%20Template%202.jpg)
  10. Depending on your project settings, you may be shown a dialog indicating there have been changes in the current project folder. Click Yes if this appears.
  11. In the Windows Explorer dialog, browse to your project folder and check that the new template file Plan - Portrait.dmtpl has been created - note that it can take several seconds for the template file to be configured and saved, although this will depend on the data that is currently loaded.

![note.gif \(1017 bytes\)](../images/note.gif) |  The above procedure is also used to create a log sheet template.  
---|---  
  
**![](../images/UpArrow.gif)**Top of page

## Exercise: Creating a New Plot Sheet from a Template

![note.gif \(1017 bytes\)](../images/note.gif)| This exercise follows on directly from the previous exercise Creating a Plot Sheet Template.  
---|---  
  
In this exercise, you are going to create a new plot sheet using the template file Plan - Portrait.dmtpl which was created in the previous exercise. The exercise procedures are as follows:

Loading the Template File

  1. Select the Plots window.
  2. Unload any data that has been loaded as a result of the previous exercise.
  3. Drag the following files into the Plots window:  
  
_vb_itblastholes.dm  
_vb_stopo.dm (the same file as shown before)  

  4. Activate the Manage ribbon and select Sheet | From TemplateSelect Insert |Sheet | FromTemplate....

  5. In the Load Sheet Template dialog, browse to your project folder, select the template file Plan - Portrait.dmtpl , click Open.  
  
![](../Images/dp_Using%20a%20Plot%20Sheet%20Template%201.jpg)

Mapping Data to the Template

  1. In the Import Sheet Template(s) dialog,select the Preview check box, clear the Fit To Data check box.  
  
![](../Images/Plot27.jpg)  
  
![note.gif \(1017 bytes\)](../images/note.gif)| Clearing the Fit To Data check box returns the extents of the plot area to those that are stored in the template.  
---|---  
  2. In the Use Data group, left pane, select the first entry [_vb_holes (drillholes) <\- (absent), in the right pane, select [_vb_itblastholes (drillholes)].
  3. In the left pane, check that this entry is now colored black and is mapped i.e. reads '_vb_collars (points) <\- _vb_itblastholes (drillholes)'.
  4. Check that the _vb_stopo object is also mapped (i.e. using the automatic defaults) as shown below, click OK:  
  
![](../Images/Plot29.jpg)
  5. Use the Plot View ribbon to select Scale | FitSelect View | Scale | Fit all Data
  6. Use the Scale by Area commandSelect View | Scale| Area to drag a rectangle around the blasthole data, e,g,:  
  
![](../Images/Plot31.jpg)  
  
Note how the same legend is used to color the blasthole data as in the _vb_holes data set that was used to create the template. The Title box, Scale Bar and North Arrow are all aligned as stipulated by the template.

![note.gif \(1017 bytes\)](../images/note.gif)| 

  * The Use Data data mapping panes are used to map template data format settings to data currently loaded in the project.
  * Additional data can also be imported and mapped at this stage by clicking Import New....
  * When a template is initially imported, Studio attempts to automatically map all loaded data objects and their columns to objects and columns in the template.
  * Mapping can also be done manually by selecting an object on the left and a suitable mapping option from the pane on the right.
  * Objects mapped to absent will not appear as an overlay in the new plot sheet.

  
---|---  
  
![](../Images/NextExercise.gif)[Proceed to the next topic](<Creating_and_Using_Overlay_Templates.md>)