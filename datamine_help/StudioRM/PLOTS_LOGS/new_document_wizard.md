![](../Images/HeaderCell.gif) |  New Document Wizard New Document Wizard  
---|---  
  
# New Document Wizard

## General

All pages of the document wizard have the following buttons which enable the user to move easily from step to step (and back if necessary).

Choose |  To Do this  
---|---  
Back |  Return to the previous page of the wizard to undo or change any of action taken there  
Next |  Move to the next page and continue through the document creation procedure  
Cancel |  Close the wizard without any data being imported. Creates an empty document  
  
## Import Data Types Page

  1. Select all the data types needed to create the Studio 3 ProjectDownhole Explorer document by checking the boxes.

![note.gif \(1017 bytes\)](../Images/note.gif) | "Drillhole Tables" is effectively a heading. To import tables, expand the heading and check the individual tables required.  
---|---  
  
  2. Click Next. Provided data types have been selected, an Import Database or Import Table page will open.

## Import Database or Table Page

These pages have a window which shows files, of the specific type, which have been loaded. This will be empty to begin with. This page has two additional buttons.

Choose |  To Do this  
---|---  
Add |  Start the appropriate data import process for the data type specified  
Remove |  Remove a loaded table or database. Highlight table in window and click button  
  
  1. Click Add...

Depending on whether you are connecting to a database or a table, the wizard will open either the Data Source dialog or Data Import dialog. Each has its own specific help.

  2. When data has been loaded, either add another table of the same type by clicking Add... or click Next to import the next data type or move to the Import Complete page.

## Import Complete Page

The wizard will automatically create 3D drillhole traces from collar and survey data, if the option is checked. Likewise, if appropriate data is loaded, the wizard will give the option to create an intersections table.

The imported data may be reviewed by stepping back through the wizard using the Back buttons. Click the Finish button to complete the creation of the new document.

![](../Images/Tip.gif) |  With regards to the Plots window (and to a lesser extent, the Logs window), much of the hierarchical structure of a particular sheet can be stored in template form. This minimizes the effort required to generate a consistent look and feel across a range of presentation projects by automatically generating a standard arrangement of sheets, projections and, if required, data object overlays. [Find out more about Plot Templates...](<PLOTS_Plot%20Templates.md>)  
---|---  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Validating data](<validatedata.md>)[  
Defining and building drillholes](<../COMMON/LoadingDynamicDrillholeData.md>)[  
Creating and defining section plots](<insertsection.md>)[  
Formatting drillholes](<FormatHoles.md>)[  
Creating log plots](<CreateLog.md>)[  
Formatting log sheets](<FormatLogColumnSbS.md>)