# Properties

To access this screen:

  * **Home** ribbon **> > Settings >> Properties** (to see information about the project file).

  * Right-click a file in the Project Files control bar and select Properties.

  * Right-click a file in the **Loaded Data** control bar and select **Properties**.

  * Display the **[Properties](<properties%20control%20bar%20overview.md>)** control bar and select a file or object in any control bar.

## General Details:

This tab contains general file information about the current project file, and contains the following read-only fields:

  * File Path: the first field shows the physical location of the project file on your local or network drive.

**Note** : All file paths that are referenced by your application cannot exceed 128 characters in length

  * Size: the size of the file in kilobytes and bytes.

  * Created: the creation date of the current project file.

  * Modified: the date the file was last modified.

  * Accessed: the date the file was last opened.

  * Attributes: this collection of check boxes determines how it is stored on disk, and contains the following options:

    * Read Only: the file is currently protected and can be viewed, but not modified.

    * Archive: the file is an archive file (see [Archiving Data](<archiving.md>)).

    * Compressed: the file is in a compressed format.

    * Hidden: the file is hidden.

    * System: the file is a system file.

  * Extended Precision: if this box is ticked, then the current project is an extended precision project.

## Summary Details:

The **Summary** tab contains optional information that may be associated with the current project file. In most cases, these fields are editable and when present, will be available for viewing by right-clicking the selected file in your file system and selecting Properties, as well as being accessible via your application.

  * Application: this read-only field shows the application that is associated with the project file.

  * Title: the title of the file, normally a brief description of its contents.

  * Subject: a more detailed description of the file contents and/or other useful information.

  * Author: this field is automatically filled on file creation, with the current login name, however, it can be edited.

  * Keywords: if keywords are associated with this file (used during system file searches), they will be shown here. You can add keywords, separated by commas, to allow easier retrieval of files using the Windows search facility.

  * Comments: this freeform text field allows you to view/add any supporting information about the current file that may be useful.

  * Template: if a template has been used to create the current project file, it will be described here.  

## Status Details:

The **Status** tab records version-relevant information about the current project file. All files are read-only:

Revision Number: this field represents the number of times the current project file has been saved, and will be incremented each time the file is saved. Note that this increment will occur each time the project file is saved, and not when individual data files, stored externally to the project, are amended.

Total Editing Time: the time spent developing the current project. This is the based on the amount of time elapsed between a project being opened and closed, for each session. The value shown here will be incremented by this amount to show a compound value.

  * Created: the time and date of file creation.

  * Last Saved: the time and date of the last file save.

  * Last Saved By: the active log in name when the last file save was performed.

  * Last Printed: if the file has been printed, this field shows the data and time this last happened.

  * # Pages: this property is not currently supported by your application

Related topics and activities

  * [System Options](<Options.md>)

  * [Project Settings](<ProjectSettings.md>)