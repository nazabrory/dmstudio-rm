# Data Types

Your application uses and recognizes several types of data and it is important to understand the nature of each and how it is accessed.

## Summary of Data Types

Data Type |  Description |  Classification  
---|---|---  
A |  Datamine file (.dm, .dmx) |  Datamine Binary format files which exist in the default project folder. |  Internal  
B |  Distributed Datamine file (.dm, .dmx) |  Datamine files which exist in windows folders other than the default project folder. |  External  
C |  Imported DSD cached as Datamine file (.dm, .dmx) |  Datamine files created from an external data source, and can be refreshed from this source using the data source driver; these exist in the default project folder.  |  Internal  
D |  External Data, automatically imported |  Data from an external data source which is always loaded into memory when the project is opened. This uses the Data Source Drivers. |  External  
E |  Archived Data |  Data which is stored within the Project file. This data is loaded into memory when the document is opened.  |  N/A  
F |  Other files |  All other file based data which is relevant to the project such as .htm, .mac, office documents (Word, Excel) , .gvp replay files, .bmp , emf, etc.  |  Internal  
G |  In Memory Data |  Data created in memory that has not yet been saved either within the project or to a file, local or remote.  |  Internal  
  
## Data type A: Datamine file in the project folder

In general, these are working files such as strings and wireframes, which do not need to be stored in a central database. Your application can run using only this type of data.

To improve performance, temporary files created during batch processing, or data manipulation, may also fall into this category.

### Data Type A Usage Table

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
Y |  Y |  Y |  Y |  N  
  
## Data type B: Distributed Datamine file

These are external Datamine files containing data which can be shared between two or more users. Having a single reference point avoids the need to manage multiple copies of a key file and ensures all users are always working with the same data.

#### Example of use

  * A resource model has been created, and is being updated, by geologists also it also needs to be accessed by the mine engineers for planning purposes.

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
Y |  Y |  Y |  Y |  N  
  
## Data type C: Imported Data cached as a Datamine file

Cached files are used to access data from a third party source and store it in the project folder, as a Datamine file, for further processing. The key characteristic of this data type is that a link is maintained to the external source so that the Datamine file can be refreshed easily whenever a latest version of the source data is required. This data type is used for mine data stored in a third party format but which needs to be processed using a Datamine application.

#### Examples of use

  * A large geological block model (many megabytes) is stored in a corporate geological modeling system. Your application will recognize that the data are stored externally, in the corporate database, but it will optimize its performance by accessing the data using its own formats.

  * Drilling data (Collars, Surveys, and Samples files) are usually stored in an external database such as SQL Server or Microsoft ACCESS. The data are often imported into Studio for further validation, processing and modeling. As with geological block models it is not always desirable to get the very latest data if it is changing frequently and represents work in progress.

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
Y |  Y |  Y |  Y |  N  
  
## Data type D: Automatically Imported Data

This memory-based data type is used to access data from a third party source and load it into the data Window. In other words, the data are loaded into memory but are not stored as a Datamine file. A link to the external source is maintained so that the data can be reloaded easily into the data Window when needed. This is for data that are not processed directly but are needed for display or reference purposes when working with other data.

#### Example of use

  * When surveyed underground development wireframes (drives and cross-cuts) are imported for use in a ring design, they are only needed as a reference. The wireframes themselves will not be changed.

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
Y |  N |  N |  Y |  Y  
  
## Data type E: Archived Data

These data are actually stored within the Project file rather than in a linked external source. The archived data type is useful for saving a snapshot of the data (and any settings) used at a particular time.

#### Example of use

  * A set of plots can be be saved as archived data to be printed-out at a later date.

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
Y |  N |  N |  Y |  Y  
  
## Data type F: Other

Other data includes file-based data which are not stored in the Datamine format such as fields and records. The most common examples would be macros and scripts which are used to record and run user-defined sequences of commands. Both macros and scripts are stored as lists of commands with associated settings in text files.

#### Examples of use

  * Bitmap files, representing Company logos, to be added to title boxes on plotted plans and sections would also fall into this category.

  * A bitmap file representing seismic survey data could be loaded as geo-referenced data into the Design Window, or it could be loaded as a texture, mapped onto a 3D surface in a **3D** window.

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
N |  N |  N |  |  N  
  
## Data Type G: In Memory data

3D View |  Batch Processing |  Macros |  Scripts |  Automatic Memory Load  
---|---|---|---|---  
Y |  N |  N |  Y |  Y  
  
Related topics and activities

  * [Datamine File Descriptions](<filetype.md>)