# Holes Control Bar

To hide or show this control bar:

  * **Home** ribbon **> > Window >> Show >> Holes Bar**.

The Holes control bar displays a list of currently loaded dynamic drillholes containing a series of XYZ sample centre points, lengths and directions representing hole traces.

Typically, these holes are desurveyed from drillhole tables using either the **[DESURV](<../Process_Help_XML/desurv.md>)** or **[HOLES3D](<../Process_Help_XML/holes3d.md>)** process.

The list displayed represents the drillhole data that is currently in-memory. For more information on building drillholes, see [Defining and Building Drillholes](<LoadingDynamicDrillholeData.md>).

Context menus are used to access functions. The options available depends on which part of the tree menu is currently highlighted when the menu is displayed:

  * The Top-Level Project Icon Create and update hole sets, and to set which hole set is the default.

  * The Hole Set folder icons Add holes to a specific hole set.

  * The Borehole Identifier icons View borehole properties, and amend desurvey settings.

Further hole management functions are found on the [Format Display](<Format%20Overlays%20Dialog.md>) screen. Right-clicking a drillholes overlay in the 3D window of the Sheets control bar allows you to access a wide range of hole settings, including the [Hole Manager](<Hole%20Manager%20Dialog.md>) screen. This gives you alternative access to some of the functions mentioned here, such as adding holes to a set and other editing options. It also allows you to access the [Hole Set](<Hole%20Set%20Dialog.md>) screen, which allows you to add holes from the full list available. 

Also, you can use the Holes control bar in conjunction with the [Compositor](<Compositor%20Control%20Bar%20Overview.md>) control bar - selecting a hole identifier automatically updates the contents of the Compositor window, showing data relevant to the selected borehole.

## Top Level Menu

Right-clicking the project icon reveals the following options:

  * New Set Create a new hole set in memory, and displays the [New Hole Set](<New%20Hole%20Set.md>) screen.

  * Paste If data has been previously copied from the Hole Set folder, this option is available. Selecting it will transfer the contents of the clipboard to Holes list, creating a new, duplicate hole set.

  * Default Define which hole set is to be the default (the set from which data is copied), using the [Default Hole Set](<default%20hole%20set%20dialog.md>) screen.

## Hole Set Menu

Right-clicking the project icon shows the following options providing the hole set is not the 'All Holes' variety. This folder is reserved to display all holes from all sets. 

The following fields are available (although if the **All Holes** folder is selected, some options are unavailable and you will only be able to copy and view the hole set properties):

  * Add hole(s) Add holes to the current set, via the [New Hole Set](<New%20Hole%20Set.md>) screen.

  * Insert If a drillhole has been copied to the clipboard (using the right-click menu at Borehole Identifier level), insert it into the selected hole set, providing it does not already exist (all borehole identifiers must be unique throughout a set).

  * Delete Remove the hole set. 

Note: This option is not available for the **All Holes** folder.

  * Copy Copy the contents of the hole set folder to the clipboard. You can now insert a copy of the hole set by right-clicking the top-level project icon and selecting Paste.

  * Set Properties Displays an [Object Summary](<Properties%20Dialog.md>) showing properties of the selected object.

  * Default Set Make the selected hole set the default.

## Borehole Identifier Menu

Right-clicking a borehole identifier within a hole set sub-folder displays the following options (although if the identifiers are within the 'All Holes' folder, functionality is restricted to Properties, Exclude, Copy and Synchronize options):

  * Properties Displays the [Drillhole Properties](<hole%20properties.md>) screen, which can be used to view the drillhole settings and edit desurvey settings.

  * Exclude Exclude or include the selected drillhole from the current drillhole set. This is a toggle button.

  * Delete Remove the selected borehole from the set, after confirmation. Please note that you cannot undo this command.

  * Copy Copy the current drillhole to the clipboard. After copying, the item can be inserted using the Paste option accessed by right-clicking a Hole Set Folder, or the Insert Item option (see below).

  * Insert Add holes to the current set, via the [New Hole Set](<New%20Hole%20Set.md>) screen.

  * Insert Item If drillhole data has been copied using the above option, this command will insert it into the currently selected hole set.

  * Synchronize Holes or intervals selected in one view can be displayed in any other using this option. The action of other views when a selection is synchronized is determined by the status of the Linked and Live settings.

Related topics and activities:

  * [Compositor Control Bar](<Compositor%20Control%20Bar%20Overview.md>)

  * [Hole Set](<Hole%20Set%20Dialog.md>)

  * [Hole Set Name](<Hole%20Set%20Name%20Dialog.md>)

  * [New Hole Set](<New%20Hole%20Set.md>)

  * [Defining and Building Drillholes](<LoadingDynamicDrillholeData.md>)