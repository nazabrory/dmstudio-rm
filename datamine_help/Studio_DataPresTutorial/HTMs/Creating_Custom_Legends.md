![](../HeaderCell.jpg) |  Creating Custom Legends Creating custom legends for data formatting and presentation purposes.  
---|---  
  
# Overview

In this portion of the tutorial you are going to create and modify a unique values, rock type legend.

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Links to exercises

The following exercises are available on this page:

  * Creating an Unique Values Legend for Rock Type Codes

  * Modifying a Legend to Use Fill Patterns

## Exercise: Creating a Unique Values Legend for Rock Type Codes

In this exercise you are going to create a unique values legend and define custom colors for the set of rock type codes (field NLITH) found in the static drillholes file _vb_holes.

![](../Images/Tip.gif) | 

  * When starting a new project, define custom legends for data that will be regularly used for modeling, mine design and presentation purposes.
  * Define new color/texture/image standards for you various data columns (or use existing standards if they already exist) e.g. rock types, ore zones, grade categories, mine design elements, mine planning time periods.

  
---|---  
  
**Creating the Unique Values Legend**

  1. Select Format |Legends... or, in the Format toolbar, click Format Legends.
  2. In the Legends Manager dialog, click New Legend....
  3. In the Legend Wizard: Data Table Column dialog, select the Use Object Field option.
  4. Select **the Object** [**_vb_holes (drillholes)],** select the Field [NLITH], click Next>.
  5. In the Legend Wizard: Legend Storage dialog, select the Current Project File option, click Next>.  
![note.gif \(1017 bytes\)](../Images/note.gif) | Legends can be stored in three ways:
     * Current Project File \- these legends are stored in the current project file and are not available for use in other Studio projects.
     * User Legends Storage \- these legends are stored in the external legend file user.elg , in the following locations, and are available to other Studio projects opened by the current user:
Windows XP: C:\Documents and Settings\\[Username]\Application Data\Datamine\Legends  
Windows 7 C:\Users\\[Username]\AppData\Roaming\Datamine\Legends
     * External Legend File \- a single legend is saved to a user defined legend file (.elg), in any location, which can be loaded into any Studio project.  
---|---  
  6. In the Legend Wizard: General dialog, define the legend **Name** as 'vb_holes_NLITH1'.  
![note.gif \(1017 bytes\)](../Images/note.gif)| The Type has been automatically set to [Numeric] as the field NLITH is defined as a numeric field in the _vb_holes(drillholes) table.  
---|---  
  7. Select the Unique Values option, clear the Convert to Filter Expressions check box, click **Next >**.
  8. In the Legend Wizard: Data Range dialog, click Next>.
  9. In the Legend Wizard: Coloring dialog, select the color range [Rainbow blue->red], click Preview Legend....
  10. In the Legend preview dialog, check that your legend is as shown below, click Close:  
  
![](../Images/dp_UniqueValuesLegendNLITH1.jpg)
  11. Back in the Legend Wizard: Coloring dialog, click Finish.
  12. In the Legends Manager dialog, Available Legends group, check that the new legend **vb_holes_NLITH1** is listed (expanded) at the bottom of the project legends folder, as shown below (do not close the dialog):  
  
![](../Images/dp_UniqueValuesLegendNLITH2.jpg)

**Editing the new NLITH Legend colors**

  1. In the Legends Manager dialog, Available Legends group, select vb_holes_NLITH1, if it is not already expanded, click the "+" symbol next to the legend name.
  2. Select the legend item [0], move across to the details (right) side of the dialog.
  3. In the Legend Item Description group, clear the Automatically generate description check box, define the Description as 'Soil'.
  4. In the **Legend Item Format** group, select the Fill Color [Yellow 3], check that Line Color is also [Yellow].  
![note.gif \(1017 bytes\)](../Images/note.gif)| If the Use fill for line colour checkbox is ticked (default), then the Line Color is automatically set when the Fill Color is defined. Clear this checkbox to set line colors independent of fill colors.![](../Images/dp_UniqueValuesLegendNLITH3.jpg)  
  
---|---  
  5. Select the legend item [1].
  6. In the Legend Item Description group, clear the Automatically generate description check box, define the Description as 'Sandstone'.
  7. In the **Legend Item Format** group, select the Fill Color [Red], select the Line Color [Red].
  8. Select the legend item [2].
  9. In the Legend Item Description group, clear the Automatically generate description check box, define the Description as 'Siltstone'.
  10. In the **Legend Item Format** group, select the Fill Color [Bright Green], select the Line Color [Bright Green].
  11. Select the legend item [3].
  12. In the Legend Item Description group, clear the Automatically generate description check box, define the Description as 'Breccia'.
  13. In the **Legend Item Format** group, select the Fill Color [Magenta 1], select the Line Color [Magenta].
  14. Select the legend item [4].
  15. In the Legend Item Description group, clear the Automatically generate description check box, define the Description as 'Basalt'.
  16. In the **Legend Item Format** group, select the Fill Color [Bright Blue], select the Line Color [Bright Blue].
  17. In the **Legends Manager** dialog, click Preview Legend....
  18. In the Legend preview dialog, check that your legend is as shown below, click Close:  
  
![](../Images/dp_UniqueValuesLegendNLITH4.jpg)
  19. Back in the **Legends Manager** dialog, click Close.

## Exercise: Modifying a Legend to Use Fill Patterns

![note.gif \(1017 bytes\)](../Images/note.gif)| This exercise follows on directly from the previous exercise Creating an Unique Values Legend for Rock Type Codes.  
---|---  
  
In this exercise you are going to copy the legend vb_holes_NLITH1, created in the above exercise, then change the fill style from solid color to fill patterns.

![](../Images/Tip.gif)| Use fill patterns for legends when formatting the following:

  * rock types in drillhole logs
  * rock type perimeters in plan or section views
  * ore zones
  * mine planning outlines e.g. ore/waste blocks.

  
---|---  
  
**Copying a Legend**

  1. Select the Plots, Logs or Design window.
  2. Select Format |Legends... or, in the Format toolbar, click Format Legends.
  3. In the Legends Manager dialog, Available Legends group, right-click the project legend vb_holes_NLITH1, select Copy to User Legends.
  4. In the Available Legends group, check that the legend has been copied to the User Legends folder:  
  
![](../Images/dp_UniqueValuesLegendTexturesNLITH1.jpg)
  5. Select vb_holes_NLITH1, in the Legend Properties group on the right, change the Name to 'vb_holes_NLITH2':  
  
![](../Images/dp_UniqueValuesLegendTexturesNLITH2.jpg)

**Changing the vb_holes_NLITH2 User Legend colors to textures**

  1. In the Legends Manager dialog, Available Legends group, User Legends folder, expand the legend vb_holes_NLITH2 .
  2. Select the legend item 'Soil'.
  3. In the **Legend Item Format** group, select the Fill Style [Texture], select the Fill Color [Black], select the Texture File Name [p-Soil B.bmp], select the Line Color [Black], as shown below:  
  
![](../Images/dp_UniqueValuesLegendTexturesNLITH3.jpg)  
![note.gif \(1017 bytes\)](../Images/note.gif)| If the Use fill for line colour checkbox is ticked (default), then the Line Color is automatically set when the Fill Color is defined. Clear this checkbox to set line colors independent of fill colors.![](../Images/dp_UniqueValuesLegendNLITH3.jpg)  
  
---|---  
  4. Select the legend item 'Sandstone'.
  5. In the **Legend Item Format** group, select the Fill Style [Texture], the Fill Color [Black], the Texture File Name [p-Sandstone W.bmp], the Line Color [Black].
  6. Select the legend item 'Siltstone'.
  7. In the **Legend Item Format** group, select the Fill Style [Texture], the Fill Color [Black], the Texture File Name [p-Siltstone N.bmp], the Line Color [Black].
  8. Select the legend item 'Breccia'.
  9. In the **Legend Item Format** group, select the Fill Style [Texture], the Fill Color [Black], the Texture File Name [p-Breccia.bmp], the Line Color [Black].
  10. Select the legend item 'Basalt'.
  11. In the **Legend Item Format** group, select the Fill Style [Texture], the Fill Color [Black], the Texture File Name [p-Basalt.bmp], the Line Color [Black].
  12. In the **Legends Manager** dialog, click Preview Legend....
  13. In the Legend preview dialog, check that your legend is as shown below, click Close:  
  
![](../Images/dp_UniqueValuesLegendTexturesNLITH4.jpg)
  14. Back in the **Legends Manager** dialog, click Close.

**![](../Images/NextExercise.gif)**[Proceed to next topic](<Saving_and_Loading_Legends_Files.md>)

Checklist:

  1. The topic is stored in the relevant tutorial area of the RoboHelp X5 project.

  2. All topics created with this template are set at TOPIC-LEVEL to the relevant TUTORIAL build tag.

  3. Related topics are not normally required - use BROWSE SEQUENCES instead.

  4. Popups

  5. Browse sequences

  6. Index

  7. TOC

  8. Glossary Items

Document History|   
---|---  
Date| Description  
201005| 

  * Updated to reflect MR19 functionality

  
201107| 

  * Updated to reflect MR20 functionality

  
201202| 

  * Updated to:
  *     * reflect MR21 functionality
    * replace 'Datamine' term with 'Studio', 'CAE Mining', etc.
    * apply templates with new 'CAE Datamine Corporate' copyright notice