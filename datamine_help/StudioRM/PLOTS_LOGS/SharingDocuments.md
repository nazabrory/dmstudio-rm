# Sharing Projects  
  
It can be useful to share your project with others. 

Datamine provides several options for project and data sharing both within Studio applications and via external services, such as MineTrust. However, you may just want to share your project data within the same network, or package up a project and associated files to allow someone else to view what you've been up to, or approve your results.

One way to do this is to [Archive Project Data](<../COMMON/archiving.md>) which makes sure that all files referenced by your project (at the point of archiving) are wrapped up in a single project-and-data combination file. This ensures all existing file references and all loaded data can be seen on the destination system.

The following topics discuss _sharing a copy_ of your project with others. For true multi-user capabilities within the same project, you can consider the Datamine MineTrust data management solution - contact your local Datamine office for more details.

**Note** : just like any files on a local network, a project file can only be opened for editing by one person. You can open a project simultaneously on multiple machines, but if the same project file is being accessed, only one (the first) user will be able to modify it.

### How does my application locate data source files?

The location of the external data files referenced by a Studio project can be stored as either an absolute or relative address.

  1. For example, if the full path name of the document is: 

**c:\My Projects\Thunder Gulch\Thunder Gulch.rmproj**

  2. ...and references a data source file stored at:

c:\My Data\Thunder Gulch\tg_collars.txt

  3. ...when the document is opened, the program first looks for the file using the absolute address:

c:\My Data\Thunder Gulch\tg_collars.txt

  4. ...and if the file cannot be located, the program then looks for the file using the relative address: 

..\\..\My Data\Thunder Gulch\tg_collars.txt

In practice, this means that if you are sharing an entire project folder with someone else, and all files within that folder are the only ones referenced by the project file, no additional files or folders need to be shared.

Consider the following scenarios:

##### Copying or moving a project to a different directory on the same disk

If you copy or move the document to a new directory on the same computer, the program will always be able to find the data source files using the absolute address.

##### Copying or moving a project to a different disk on the same computer

If you copy or move the document from the c: drive to say the d: drive, the program will always be able to find the data source files using the absolute address.

#### Copying or moving the document to a different computer on the same network

If the data source files and the document were originally located on different computers on the same network, the absolute address stored in the document will include the network address. So when the document is copied or moved around the network, the program will always be able to locate the data source file using the absolute address.

On the other hand, if the data source file and the document were both originally located on the same computer, the absolute address is local to that computer. Hence if the document is copied or moved across the network, the program will be unable to locate the file using either the absolute or the relative address and will prompt you to locate the file again by displaying the Open dialog. You can however open the document across the network and then save it to the local disk using the Save As command. The copied document will now contain the network locations of all data source files.

#### Copying or moving the document to a different computer off the network

If you copy or move the document to a different computer off the network, the data source files must also be moved to the same relative address.

#### Moving a data source file to another location or name

If you move a data source file to a different directory or a different disk or a different computer on or off the network, or rename the file, the program will be unable to locate the file using either the absolute or the relative addresses and will prompt you to locate the file again by displaying the Open dialog.

## A Note about Custom legends

If you are using custom patterns and textures in your legends, Datamine product installations on other computers will need to be updated with these custom bitmaps.

Related topics and activities

  * [Project Wizard ](<../COMMON/ProjectWizard.md>)

  * [Save Data/Set Auto Reload](<../COMMON/SaveChanges.md>)

  * [Archive Project Data](<../COMMON/archiving.md>)