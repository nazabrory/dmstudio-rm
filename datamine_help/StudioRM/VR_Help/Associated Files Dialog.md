# Associated Files

To access this screen:

  * Display any 3D object properties screen and select the Associated Files tab.

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

Associate one or more external files with a loaded (and displayed) 3D object.

For example, you could associate summary information relating to survey station points, or add rimpull analysis data to a haultruck simulation object. 

External files are displayed using the current default application for the associated file type. You display a file by right-clicking the associated object overlay in any 3D window. For example, in the image below, two macro files are associated with a string. Right-clicking the string in a 3D view reveals the following options:

[![](../Images/Associated-Files.png)](<javascript:void\(0\);>)

Clicking either opens the macro in a text editor (as that is the default viewer on the system for .mac files).

**Note** : the **Description** of an associated file is displayed in the menu. See below.

## Using Attributes

You can pass attribute field values as part of either the filename or a parameter.

Typing the field name between square brackets (e.g. '[]') will replace that part of the string with the string value of the attribute related to the part of the visual clicked. For example, a set of drillholes would share a File and Parameters since they are all part of the same strings object.

## Associated Files Example

To access a different file for each drillhole, you could pass the drillhole ID field as part of the parameters list. 

For example, you could enter _Notepad.exe_ in the File field, _BHID_ in the Parameter field, and _Attribute Test_ in the Description field. Right clicking the target overlay in different places and selecting **Attribute Test** from the context menu then allows you to open a text file that relates to the borehole in question (assuming it has been created previously).

## Activities

To associate an external file with a loaded data object overlay:

  1. Open the 3D properties screen for an object overlay.

  2. Select the **Associated Files** tab.

  3. Add a path name to an external File, or browse for the file.

  4. Optionally, specify any command line **Parameters** that should be run when the file is opened. For example, you could open an Excel spreadsheet and force a particular macro to run on opening it.

  5. Enter a menu **Description** to appear when right-clicking the target overlay in a 3D view.

  6. Use the **down arrow** to transfer the associated file item to the list below. All files in the list appear as menu items for the target overlay.

**Note** : select a list item and click the delete button remove it from the associated files list.

  7. If relevant, use the up and down arrows to position menu items.

  8. Click **Test** to make sure that your target file can be opened using the parameter(s) provided. If successful, the target file(s) display using their associated viewing or editing application.

  9. Click **OK** to associate the files with the target overlay.

  10. Test your new menu entries by right-clicking the target overlay in any 3D view.

Related topics and activities

  * [ Information Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)