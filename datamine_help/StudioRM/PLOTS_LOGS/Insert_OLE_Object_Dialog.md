![](../Images/HeaderCell.gif) |  Insert Document Dialog Using Microsoft's OLE insertion routines  
---|---  
  
# Insert Document Dialog

### To access this dialog use one of the following:

  * In the Plots or Logs window, select a sheet and toggle on Page Layout Mode; using theManageribbon, selectInsert | Plot Item(top level icon); in the Plot Item Library dialog select [Document], click OK.

  * In the Sheets control bar, right-click a plot or log sheet, select Insert; in the Plot Item Library dialog select [Document], click OK.

This dialog is used to either create an OLE object type within the current project (unlinked to external data) or to specify an OLE-friendly file format that can be embedded within your plot or log sheet (linked or unlinked).

Field Details:

There are two main options on this dialog:

  * Create New: this option will always result in an unlinked file - meaning there will be no connection between any external document and your project. The data can be edited by the default application (e.g. Excel, Word etc.) but this application is used to edit the embedded content. The procedure for creating a new, empty embedded document object in your current section is:

  *     1. With the Insert Document dialog open, ensure the Create New option is selected.

    2. Select an Object Type from the list displayed. The choice made is important as it will define the application that will be used to create/edit the content of the embedded object. The list of object types is specific to your system - all registered OLE-friendly formats will be displayed. Remember, you can only embed static content in a plot sheet, so your choice of object type should reflect this criterion.

    3. If you wish to embed the content as initially viewable data, ensure the Display As Icon check box is cleared. If you wish to show your embedded content as an icon (to be double-clicked), you can select this check box (not recommended for hardcopy printouts).

  * Create from File: with this option, you have the choice of linking to an external file, or taking a "snapshot" of the file in its last saved state, to be embedded within your plot view.  
  
If you only wish to record a particular object at a particular moment in time, creating a "snapshot", and that the underlying data changing in future will not be relevant to your presentation, it is likely that dynamic linking between the embedded object and the external file will not be necessary. Note that you cannot associate a non-linked object with a data source after it has been embedded - once it becomes embedded, even though it is still associated with the external application and can be edited as such, it is native to the project.  
  
To create a snapshot (unlinked) item, ensure theLinkcheck box is cleared when adding the new object.  
  
However, if the external file is constantly updated, or is likely to be in the future, for example, in the case of an output file from another process, you can embed a dynamically linked document that will allow you to refresh your object with the click of a button, loading in the latest underlying data whether that is a database table, picture, graph or other format. Dynamically linked documents are also updated automatically when a project is loaded if such items are contained within it. Linked objects can be updated as required during a session, and can even be linked to an alternative data source after initial embedding. You can also break a link at any time, resulting in a snapshot document as explained above.  
  
To create a live (linked) item, ensure theLinkcheck box is selected when adding the new object.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Inserting documents into plot sheets involves the use of an industry-standard framework commonly referred to as 'OLE'. OLE stands for "Object Linking and Embedding". This standard (known as a "compound document standard" as it allows for the creation of documents built up using disparate underlying technologies), developed by Microsoft Corporation, enables you to create objects with one application (such as Microsoft Excel or Word) and then link or embed them in a second application (such as Studio 3). Embedded objects retain their original format and, optionally, maintain the link to the application that created them. Note that although many formats are supported for OLE import, only static content (non-animated) will be shown. For more information on embedding OLE objects, refer to [Inserting OLE Objects](<Inserting%20OLE%20Objects.md>).  
---|---  
  
![](../Images/StepByStep2.gif)

To insert an external document into a particular section:

  1. Open the Plots window, and display the sheet that you wish to add an OLE object to.

  2. Open the Sheets control bar.

  3. Expand the Plots folder to show all available sections, e.g.:  
  
![](../Images/OLE1.gif)

  4. Right-click the sheet description corresponding to the sheet that is currently displayed.

  5. Select Insert...

  6. Select [Document] from the Plot Item Library.

  7. In the Insert Document dialog, select either an object type and follow the remaining Microsoft dialogs to import your object, or select a file in an OLE-friendly format to insert.

Inserting Animated Content in a Plot Section View

Although many formats are supported for this type of import, only static content (non-animated) can be shown directly in the Plot section view - although animated content such as movie clips and Flash files can be displayed as icons, to be opened manually in the default application.

To insert, say, a media clip in .avi format:

  1. Insert the item as a link to a physical file (ensure the Create from File option is used).

  2. Ensure the Link check box is selected.

  3. It is also necessary to ensure the Show as Icon check box is selected.

  4. Click OK

To show the animated content it is necessary to:

  1. Enter Page Layout Mode (theManageribbon andLayout | Layout Mode) if not in this mode already.

  2. Right-click the embedded icon representing the animated content.

  3. Select Document | Open...

  4. Your content will then be displayed in the associated application.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Inserting Documents](<Inserting%20OLE%20Objects.md>)[  
Configuring Documents](<ConfigureOLEObject.md>)[  
Plot Item Library Dialog](<plotitemlibrary.md>)