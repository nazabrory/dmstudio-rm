![](../HeaderCell.jpg) |  Creating and Using Overlay Templates How to create, use and export overlay templates.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and techniques used to create, apply and export Overlay templates.

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

  * Copied and renamed the Plan sheet - see exercises on the [Opening, Copying and Inserting Plot Sheets](<Opening_Copying_and_Inserting_Plot_Sheets.md>) page.

  * Displayed the required Overlays - see the exercise on the [Displaying Plot Sheet Data](<Displaying_Plot_Sheet_Data.md>) page.

  * Formatted the required Overlays in the copied plan sheet - see the exercise on the [Formatting Overlays](<Formatting_Overlays.md>) page.

## Link to exercises

The following exercises are available on this page:

  * Creating an Overlay Template
  * Applying an Overlay Template
  * Exporting Overlay Templates

## Exercise: Creating an Overlay Template

In this exercise, you are going to create a drillholes overlay template from the drillholes overlay in the Plan 2 plot sheet.

![note.gif \(1017 bytes\)](../images/Tip.gif) |  Use an overlay template to save a particular overlay's formatting settings and as a means of quickly formatting a new overlay with the same set of format settings. The advantages include:

  * improving work flow and efficiency,
  * enabling the standardization of formatting a commonly used overlay within a project.

  
---|---  
  
This includes the following tasks:

  * Creating a new drillholes overlay template

  * Applying formatting to the drillholes template

Creating a new Drillholes Overlay Template

  1. Select the Plots window.
  2. Select the Plan - Portrait tab created in the [previous exercise](<Creating_and_Using_Sheet_Templates.md>), check that the sheet has the drillholes displayed and formatted, as shown below:  
  
![](../Images/Plot31.jpg)
  3. In the Sheets control bar, the Plan -Portrait | Plan Projection | Overlays folder, right-click _vb_itblastholes (drillholes) , select Format....

  4. In the Format Display dialog, Overlays tab, Overlay Objects group, select the Templates option.
  5. Check that the following standard templates are listed, as shown below, click Add...:  
  
![](../Images/dp_Creating%20an%20Overlay%20Template%202.jpg)
  6. In the Add Template dialog, define the Name as 'Drillholes_ZONE_AU', select the Type as Drillholes, click OK:  
  
![](../Images/dp_Creating%20an%20Overlay%20Template%203.jpg)
  7. Back in the Format Display dialog, Overlays tab, Overlay Objects group, check that the new Drillholes_ZONE_AU template has been add to the list:  
  
![](../Images/dp_Creating%20an%20Overlay%20Template%204.jpg)
  8. In the Overlay Format group on the right, select the Drillholes subtab and note that no downhole columns are currently displayed:  
  
![](../Images/dp_Creating%20an%20Overlay%20Template%205.jpg)  
  
![note.gif \(1017 bytes\)](../images/note.gif)| At this stage, a new drillholes template has been generated with minimal default formatting and without any downhole columns displayed along the drillhole traces.  
---|---  

Applying Formatting to the Drillholes Template

  1. In the Overlay Objects group on the left, select the Overlays option, select the _vb_itblastholes (drillholes) object.
  2. Select the Drillholes sub-tab and click Insert...
  3. In the Select Column dialog, select the [AU] option and click OK.
  4. In the Format for AU dialog, select [Filled Histogram], select all other defaults and click OK.  
  
![](../Images/Plot32.jpg)
  5. In the Overlay Format group on the right, Template group (at the bottom of the dialog), template list, select [Drillholes_ZONE_AU], click Update Template:
  6. In the 'Warning. Template will be updated...' confirmation dialog, click Yes.
  7. In the Overlay Objects group, select the Templates option, select the Drillholes_ZONE_AU template.
  8. In the Overlay Format group on the right, select the Drillholes subtab and note that the ZONE and AU downhole columns are displayed:  
  
![](../Images/Plot32.jpg)

![note.gif \(1017 bytes\)](../images/note.gif) |  At this stage the newly created and updated Drillholes_ZONE_AU template is stored within the project file.  
---|---  
  
  9. Click OK in the Format Display dialog.

**![](../images/UpArrow.gif)**Top of page

## Exercise: Applying an Overlay Template

![note.gif \(1017 bytes\)](../images/note.gif)| This exercise follows on directly from the previous exercise Creating an Overlay Template.  
---|---  
  
In this exercise, you are going to first apply the default Drillholes Template and then the Drillholes_ZONE_AU overlay template to the _vb_holes (drillholes) static drillholes overlay. This includes the following tasks:

  * Displaying the overlays

  * Applying a drillhole templates

Displaying the Overlays

  1. Unload any data that may be loaded from the previous exercise.

  2. Drag the following files from the Project Files control bar into the Plots window:  
  
_vb_stopo.dm  
_vb_holes.dm  

  3. Scale the view to fit all the loaded data.

Applying Different Drillholes Templates

  1. In the Sheets control bar, the Plan - Portrait | Plan Projection | Overlays folder, right-click _vb_holes (drillholes) , select Format....

  2. In the Format Display dialog, Overlays tab, Overlay Objects group, check that the _vb_holes (drillholes) overlay is selected.

  3. In the Overlay Format group on the right, select the Drillholes tab.
  4. In the Template group, select the template [Drillholes Template], click Apply Template.
  5. In the Overlay Format group on the right, the Drillholes tab, note that the format settings have changed i.e. no columns are displayed:  
  
![](../Images/dp_Applying%20an%20Overlay%20Template%203.jpg)
  6. In the Format Display dialog, click Apply.
  7. In the Plan - Portrait sheet tab, check that the static drillholes are now formatted as shown below:  
  
![](../Images/Plot33.jpg)  

  8. In the Format Display dialog, the Overlay Format group, Template subgroup, select the template [Drillholes_ZONE_AU], click Apply Template.

  9. In the Format Display dialog, click OK.
  10. In the new Plan - Portrait sheet tab, check that the static drillholes are now formatted as shown below:  
  
![](../Images/Plot34.jpg)

**![](../images/UpArrow.gif)**Top of page

## Exercise: Exporting Overlay Templates

![note.gif \(1017 bytes\)](../images/note.gif)| The Creating an Overlay Template exercise is a prerequisite for this exercise.  
---|---  
  
In this exercise, you are going to export the overlay templates to a new file OverlayTemplates1.tpl .

![note.gif \(1017 bytes\)](../images/Tip.gif)| 

  * Use an overlay templates file to save the formatting settings for a group of overlays and as a means of quickly formatting overlays with a set of templates. The advantages include:
  *     * improving work flow and efficiency,
    * enabling the standardization of formatting a commonly used overlay for:
    *       * your own use across multiple Studio 3 projects,
      * implementing formatting standards within a department, office or organization.
  * Store shared, standard template files outside the project folder in a suitable general folder which can be accessed by other projects or users.

  
---|---  
  
This includes the following tasks:

  * Exporting the overlay templates

Exporting the Overlay Templates

  1. In the Sheets control bar, the Plan - Portrait | Plan Projection | Overlays folder, right-click _vb_holes (drillholes) , select Format....

  2. In the Format Display dialog, the Overlays tab, the Overlay Objects group, select the Templates option.
  3. Click Export...:  
  
![](../Images/dp_Exporting%20Overlay%20Templates%201.jpg)
  4. In the Export Templates dialog, browse to your project folder, define File name: as 'OverlayTemplates1', select the Save as type [Overlay Templates (*.tpl)], click Save:  
  
![](../Images/dp_Exporting%20Overlay%20Templates%202.jpg)

  5. Back in the Format Display dialog, click OK.
  6. In the Windows Explorer dialog, browse to your project folder and check that the new overlay template file OverlayTemplates1.tpl has been created.

![note.gif \(1017 bytes\)](../images/note.gif)| Importing Overlay TemplatesWhen importing an overlay templates file in to a project, note that:

  * existing project templates i.e. those individual templates listed in the Templates pane, are not updated by templates of the same name from the template file
  * templates in the overlay templates file, which are not present in the project, are added to the list in the Templates pane. 

  
---|---  
  
![](../Images/NextExercise.gif)[Proceed to the next section](<Creating_Custom_Legends.md>)