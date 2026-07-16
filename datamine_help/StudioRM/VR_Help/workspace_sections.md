# 3D Sections Menu

To access this menu:

  * **Sheets** control bar **> > Sections >> Right-click a parent section**.

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The active 3D window folder of the Sheets control bar is used to set view properties for all loaded 3D window data, access object-specific properties, and load/unload data from memory. 

The Sections folder contains a list of all loaded section objects (this includes the Default Section and any additional user defined sections) and any loaded or imported section definition files.

The following menu hierarchy is used:

  * Top level menu (Sheets control bar only) - contains commands relating to all sections in memory. 
  * Sections parent menu \- contains commands relating to a section, or group of sections if multiple definitions exist. 
  * Section Definition menu \- contains commands relating to a single definition within a parent section. 

Find out more about the relationship between parent sections and section definitions [here](<../COMMON/3D%20Section%20Manager.md>).

### Sections Top Level Menu

  * **Double-clicking** the **Sections** top level folder in the **Sheets** control bar displays a Data Import screen, allowing you to select a Section Definition File for import.

  * Right-clicking the top level Sections folder shows the following menu options:
    * **Load** Displays a Data Import dialog, allowing you to select a Section Definition File for import (this emulates the double-click behaviour for this folder icon).
    * **New** Select this option and click in the active 3D window to show the [Orientation](<Section%20Orientation%201%20Point.md>) screen. Note that this is the same command as [Section Orientation 1 Point](<Section%20Orientation%201%20Point.md>).
    * **Create from Loaded Data** Select a section definition file in memory in order to create another instance of a 3D section object. Note that you can only import objects that are currently part of the active project - if all available items of this data type are already loaded and viewable, or if no items of the specified type exist in the project file, you will be alerted to this fact and the import operation will cease.
    * **Show All** Enable the display of all items held within the selected folder.
    * **Hide All** Disable the display of all items held within the selected folder.
    * **Redraw All** Redraw (refresh) the view of all items in the selected folder.
    * **Delete All** Remove all loaded project items from your scene. This will not delete physical files.

### Sections Parent Item Menu

Right-clicking an item in the first sub-level of the Sections folder shows the following menu options:

  * **Save** Save the current overlay's data object without further prompts. For this option to be available, you will need to have already saved the associated object in memory to a file.

Note: This option only appears if multiple section definitions exist for the section.

  * Data This option cascades the following sub-menu:

    * Reload...: reload the selected object into memory using new load and import settings.

    * Refresh...: refresh the selected object into memory using its associated data load and import settings.

    * Save As...: save the selected new 3D object to the project file or a new Datamine file. This option opens the Save New 3D Object dialog.

    * Export...: export the selected object to a Datamine or non-Datamine file, using the [Data Export](<../COMMON/ExportTable.md>) screen.

    * To Excel...: export the selected object's table and open it in MS Excel. This provides an quick means of exporting data to *.xls format.

    * Unload...: unload the selected object data from memory.

Note: This option only appears if multiple section definitions exist for the section.

  * **Make Active Section** Make the current section 'active', meaning subsequent interactive design commands will

  * **Data Object Manager** Displays the [Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>), with the associated data object selected for further analysis.

Note: This option only appears if multiple section definitions exist for the section.

  * **Edit Interactively** Use the View ribbon's section widgets facility to edit the position and orientation of the selected section. Find out more about Section Widgets [here](<../COMMON/Section_Widgets.md>).

  * **Rename** Rename the parent section item using this command.

  * **[Section Name] Properties** Access context-sensitive properties for the selected section, using the [Section Properties](<Section%20Properties%20Dialog.md>) screen.

  * **Copy** Creates an identical, automatically named copy of the selected object (note that there is no requirement to paste the item - the list of objects will be updated automatically). Copied objects have no link to their origins; changes to the original object will not affect the duplicated item, and vice versa.

Note: Only the currently active section is copied to a new object \- if a section definition table is loaded, the other sections will not be contained within the new section object.

  * **Look At** Automatically positions the 'camera' to show the selected section.

  * **Align View** Automatically rotate the view of the current data so that the specified section is viewed 'face on', i.e. perpendicular to the viewpoint. Note that if [LookAt](<vr_navigation_look_at.md>) mode is active, the view will be rotated around the specified point, but if inactive, the view will rotate around the current camera position to so that the final viewing direction is perpendicular to the section.

    * In LookAt mode, this command will always try to ensure that the viewpoint remains on the 'same side' of the LookAt point, using the reverse normal of the section if necessary.

    * If not in LookAt mode, this command will always try to force a view directly towards the section, using the reverse normal of the section if necessary.

  * **Redraw** Redraw the currently selected section in the active 3D window.

  * **Set Plane** This sub-menu allows you to redefine the orientation of the current section interactively, using one of the following options:

  * **By 1 Point** Select this option and click a point on a surface to display a second orientation menu from which you must select either toAlign to Surface(following the normals of the selected location),Horizontal, North-Southor East-West options, using the[Section Orientation by 1 Point](<Section%20Orientation%201%20Point.md>) screen.

  * **By 2 Points** Similar to the above option, but two points are required. After the second point has been digitized, you are offered options of either a Horizontal, Vertical or Perpendicular alignment before the section is updated.

  * **By 3 Points** This option allows you to define all of the information that is required to set up a view direction; the first point references the bottom left of the view 'plane', followed by the top-left and bottom-right points. The resulting plane formed from the 3 points will be used to set the new view direction.

  * **Set Clipping** Control how data is clipped in relation to the defined section:

    * **None** Do not clip data.

    * **Front** Clip data that lies in front (according to the world coordinates) of the section plane.

    * **Back** Clip data that lies behind (according to the world coordinates) the section plane.

    * **Outside** Clip all data that does not fall with the 'volume' of the section. For example, if a section is defined to be 5 meters wide, the resulting data slice will also be 5 meters wide.

  * **Next Section** If a section definition table has been loaded, containing multiple instances of view sections, selecting this option will display the next section in sequence (in the top-down order specified by the underlying data table).

  * Previous Section As above, but shows the previous section in the loaded table.

  * Add Section Add a new definition to the current section in memory \- this definition will contain position, orientation and section width properties. You can add as many section definitions to a parent section as you like. Each will be shown as a new entry in the list and can be independently configured using the [Section Row Properties](<../COMMON/SectionRowProperties.md>) screen.

  * **Rename** Rename the selected 3D overlay.

  * **Delete [Section Name]** Remove the current section from memory (and the display area) using this option. You will be asked to confirm your deletion.

Note: If a parent section, containing multiple entries, is deleted, it is the database table (i.e. all defined section orientations) that will be removed from memory, and not just the section currently displayed. 

### Section Definition Menu:

Right-clicking a section definition in the second sub-level of the Sections folder shows the following menu options:

**Select** Make the section definition active by selecting it - this will push the properties held in the section definition up to the parent item, which can then be edited further, if required.

**Overwrite** Update the selected section definition with the active section's properties.

**Delete** Delete the current section definition from the loaded section definition table.

Related topics and activities

  * [Sheets Control Bar Overview](<../COMMON/Sheets%20Control%20Bar%20Overview.md>)

  * [Section Properties](<Section%20Properties%20Dialog.md>)

  * [Section Row Properties](<../COMMON/SectionRowProperties.md>)

  * [[Section Locking](<../COMMON/Section_Locking.md>)](<../COMMON/SectionRowProperties.md>)

  * [Section Widgets](<../COMMON/Section_Widgets.md>)

  * [ Section Orientation](<Section%20Orientation%201%20Point.md>)

  * [Wireframe Split](<../COMMON/Wireframe%20Split%20Dialog.md>)

  * [Section Orientation 1 Point](<Section%20Orientation%201%20Point.md>)

  * [Section Orientation 2 Point](<Section%20Orientation%202%20Point.md>)