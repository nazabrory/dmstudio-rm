# Archive Project Data

Your application maintains links to data in files to ensure data is 'current'. These links are stored in your **[project](<Concept_The_Studio_3_Project_File.md>)**. 

You can also create a snapshot of your application at a specific point in time, optionally storing all loaded data. Such a snapshot is termed an "archive", and is useful for transferring a known data and project configuration from one system to another.

Project archive files are typically larger than their project-only counterparts as they contain the data objects that were loaded at the point of archiving. If a lot of data was loaded, the file could be quite large.

An archive stores loaded data objects in their current state alongside project settings. This differs from a regular project which stores _references_ to files and (optionally) reloads them when the project is loaded.

**Note** : You can also add data to the project file instead of an external file, using the [Data Object Manager](<Data%20Manager%20Dialog.md>).

To archive a document:

  1. Activate the Data ribbon and select Export >> Archive.

  2. Browse to a location to store your archive.

  3. Enter an archive **File name**. A file extension is added automatically.

  4. Click **Save**.

An archive file is stored at the specified location. 

**Note** : Larger archives will take longer to save than those with less content.

Related Information and Activities

  * [Data Object Manager](<Data%20Manager%20Dialog.md>)
  * [Sharing Projects](<../PLOTS_LOGS/SharingDocuments.md>)
  * [Project and File Precision](<Project%20and%20File%20Precision.md>)