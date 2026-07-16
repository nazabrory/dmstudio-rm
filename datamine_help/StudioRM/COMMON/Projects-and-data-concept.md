# Projects and Data

Your application keeps data organized using a project.

A **project** contains the following information:

  * References to data files, or actual data.

  * Project settings, including visualization and system behaviour settings.

  * Properties such as creation date, author, and so on.

**Data** exists both within or outside of a project. A data file can be saved and sent separately, or it can be deployed as part of project file. Data files are the 'truth' of your working scenario and come in a wide range of data formats, including Datamine's proprietary formats. Data can 'belong' to a project either as a link to a data file (also known as a "reference") or as the actual binary data itself (where the file is saved to the project, or the data was loaded at the time the project was **[archived](<archiving.md>)**).

Once data is loaded, it becomes an _object_. Loaded data objects can be manipulated using your product's commands and functions.

Data contains **attributes**. Data is, in essence, a table where the table columns are attributes. Attributes are also referred to as "fields" and "columns". 

An attribute can be numeric, or contain text and numbers as an alphanumeric type. If alphanumeric, an attribute has a width (the number of characters that can fit into the attribute). Regardless of the attribute type, there are restrictions on the length of attribute names. See [Attribute Naming Convention](<Attribute_Naming_Convention.md>) and [Short and Long Field Modes](<Long_Field_Mode.md>).