![](../Images/HeaderCell.gif) |  Stereonet - Data Selection Dialog An overview of features  
---|---  
  
# Stereonet - Data Selection Dialog

### To access this dialog:

  * In the [Stereonet](<Stereonet_Dialog.md>) dialog, select the Data Selection tab.

The Stereonet - Data Selection dialog is used to select the required structure points data, either from a loaded object or a from file; then select the dip direction, dip and optional key field, as the first step in generating a stereonet plot.

Field Details:

Files and Fields:

Loaded Data: select this option to use a loaded points object.

Object Name: use this drop-down to select the loaded points object.

Data File: select this option to use an external points data file i.e. a file not already not loaded into the Design/VR windows.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Selecting this option will not enable you to select data points in the stereonet and view their corresponding points in the Design or VR windows \- the Loaded Data option needs to be selected for this.  
---|---  
  
File Name: check the name of the selected file.  
  
![](../Icon_Popups/icScatterPlot_BrowseFile.gif) : browse and select a data file (*.dm) that has been added to the project. Opens the [Project Browser](<../COMMON/ProjectBrowser.md>) dialog.

![](../Icon_Popups/icRefreshScatterPlotFile.gif) : refresh/reload the data file.

Dip: select the structure points 'dip' field; the standard field name SDIP, if present in the data file/object, is automatically detected and selected as the default.

Dip Direction: select the structure points 'dip direction' field; the standard field name DIPDIRN, if present in the data file/object, is automatically detected and selected as the default.

Key Field: optionally select a key field which will be used to generate multiple stereonet plots, one for each key field value e.g. per rock type, joint set.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Use <Ctrl> \+ click to deselect any selected items in this list.  
---|---  
  
Summary: use this pane to view the chart summary information.

Apply: click this button to generate and display a stereonet in the Preview Pane; this needs to be done before moving onto the next tab.

![note.gif \(1017 bytes\)](../Images/note.gif)| When a project file is opened which contains charts that make used of linked files (and not loaded data) and the linked file(s) cannot be located (perhaps because it is unavailable, has been renamed or moved), the following error message is displayed:![](../Images/Chart_Var_FileError1.gif)Clicking OK will then display the Open dialog which is used to browse and select the required file(s):  
---|---  
  
![openbook.gif \(910 bytes\)](../Images/openbook.gif)|  Related Topics  
---|---  
| [The Stereonet Dialog](<Stereonet_Dialog.md>)  
[Stereonet - Charts](<Stereonet_Charts_Dialog.md>)  
[Stereonet - Sets](<Stereonet_Sets_Dialog.md>)  
[Stereonet - Planes](<Stereonet_Planes_Dialog.md>)  
[Stereonet - Cones](<Stereonet_Cones_Dialog.md>)  
[Stereonet - Information](<Stereonet_Information_Dialog.md>)  
[Stereonet - Settings](<Stereonet_Settings_Dialog.md>)