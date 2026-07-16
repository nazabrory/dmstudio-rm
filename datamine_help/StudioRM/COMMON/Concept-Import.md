# Importing Data

Your project stores references to _files_. These are typically linked to a particular processing scenario or campaign. 

Files can be 'imported to your project' as one of a wide range of [Datamine file types](<Datamine-File-Format.md>) and 3rd party data sources (using the powerful **Data Source Drivers** facility), and from any accessible network location. 

Note: If using MineTrust, these files can exist on the cloud and shared between multiple users.

When you import a file to your project, you are forging a connection between the physical file on disk (or the data on the cloud) and your project. In the Project Files control bar, dedicated icons highlight the origin of each file (that is, whether the file is located in your project folder or somewhere remote), and the file's format (DM or DMX). See [Project Control Bar Icons](<Project%20Icon%20Reference.md>)

Once a file has been imported to the project, the driver used to import it (either Datamine or a 3rd party vendor) is stored, meaning future project sessions already have all the import information needed to load the file(s) and start working with them.

Project files can also be loaded as part of running a command or process in Studio where, commonly, the file is selected using the [Project Browser](<ProjectBrowser.md>).

Using your **Project Files** or **Project data** control bar, you can quickly load data into memory (whereupon a file becomes an _object_) using context menu options or drag-and-drop. 

You can also automatically load project files when you open your project. Once loaded, these data objects are available for processing and analysis. You can also load data that isn't yet associated with your project, using a wide range of methods. See [Loading Data](<Concept_Loading%20Data.md>) and [Import and Load Data](<Concept_Importing%20and%20Exporting%20Data.md>).

There are a few ways to import files to your project:

  * [Import Project Files by Driver](<importfiles-Driver.md>)

Import a file (or file collection - some 3rd party formats require multiple files to describe a data object) and add its reference to the project. You select the data driver and import settings (fields to import, field mapping, Datamine files to create) as part of the import process.

  * [Import Multiple Files to Project](<ImportMultipleFileOptions.md>)

Select one or more files to import using the **Select Source Files** screen and Studio will attempt to deduce the correct driver based on the file's (or files') extension. 

Not all files can be loaded this way. Some file formats require information from you during import (for example, by using the [Text Wizard](<Text%20Wizard.md>) or - probably more easily - the [Text Importer](<text-importer.md>)).

Note: File extensions are not always unique to a particular driver. For example, DAT is used by multiple 3rd party vendors. In these cases, you must import files using the "by driver" approach,

  * [Text Importer](<text-importer.md>)

The **Text Importer** is a batch import mechanism for text files. You select your files and then configure the importation settings for each (including attribute mapping, if you are expecting to end up with a particular Datamine File type.

  * [Drillhole Importer](<DrillholeImporter-screen.md>)

Import, validate and desurvey dynamic drillhole data using a smart, automated tool that supports multiple files and data sources. You can also load drillhole component tables manually (see [Dynamic Drillhole Data](<LoadingDynamicDrillholeData.md>)).

  * [Map Data](<ImportMaps.md>)

Import map data from Studio Mapper using a dedicated import tool.