![](../HeaderCell.jpg) |  Example - Model Prototype  
---|---  
  
# Model Prototype

This example script _scr_Example Model Prototype.htm (with a standard installation, this file is found under C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts) provides an interface for defining the parameters of a model prototype. It then creates a wireframe model around the outside of the prototype model, and loads the wireframe into the visualizer.

The script interface (with suitable data) looks like the following:

![](../Images/Studio3%20Scripting%20Example%200001.jpg)

The script allows the user to browse for an Outout model name or supply a name in the text box and it allows for the input of X, Y and Z parameters.

## HTML Objects

The HTML objects that are used are.

  * Text boxes for all the XYZ data inputs and model filename.

  * A check box for deciding whether to allow sub-cells or not.

  * A push button.

## Datamine Application Object Methods

The Datamine Application Object Model calls that are being made are.

  * A call to ActiveProject.Browser to display the file browser.

  * Many calls to ParseCommand to carry out the commands for creating and displaying the prototype.

  * Calls to create and initialise the Application model object.

## Creating the Wireframe

The wireframe is created by defining a closed string around each of the six faces of the rectangular model and end-linking them. The corners of the model are numbered as illustrated below.

![](../Images/Studio3%20Scripting%20Example%200002.jpg).

## Points to Note

If you record a database command such as PROTOM that has interactive responses then the responses will be recorded in single quotes. These single quotes are optional and can be removed. However you must include a space between each interactive response as is illustrated in the script. A space is inserted into a character string as " ".

![note.gif \(1017 bytes\)](../images/note.gif) |  The text boxes that represent Maximum X, Maximum Y and Maximum Z have all been write protected and shaded. No manual input will be accepted into these text boxes.  
---|---