![](../HeaderCell.jpg) |  Example - Accessing Records and Fields  
---|---  
  
# Accessing Records and Fields

This example script _scr_Example Record and Field.htm (found with a standard installation at C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts) provides an interface for accessing the value of a field in a selected record from a Datamine file.

The script interface looks like the following.

![](../Images/Studio3%20Scripting%20Example%200003.jpg)

## HTML Objects

The HTML objects that are used are.

  * Text boxes for the filename, record, field and value information.

  * A browse button for selecting a file name.

  * Navigation buttons to browse through the record and field information of the Datamine file.

## Datamine Application Object Methods

The Datamine Application Object Model calls that are being made are.

  * A call to ActiveProject.Browser to display the file browser.

  * A link to the DmFile.DmTableADO Object which is an interface for an ActiveX Data Objct (ADO) record set on the open file. This object will provide all the information on the data within the file and for navigation through the file. These properties and functions include MoveFirst, MoveLast, MoveNext, EOF, BOF, FieldCount, GetCurrentRow, GetRowCount, GetFieldName and GetColumn.

  * Calls to create and initialise the Application model object.

![note.gif \(1017 bytes\)](../images/note.gif) |  For further information on ADO refer to <http://msdn.microsoft.com/data/default.aspx>. The Datamine OLEDB provider currently allows reading and updating existing records. It does not allow creating new records or new files.  
---|---