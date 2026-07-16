![](../HeaderCell.jpg) |  Further Browse and Copy Extensions  
---|---  
  
# Further Browse and Copy Extensions

The aim of this exercise has been to learn to design the interface and set up the event handlers. However the resulting script has a number of limitations. You might like to try the following improvements by yourself.

## Copy a Single Field

This extension will copy a single field from a file. The script changes the copy command into the selective copy command or SELCOP.

First the interface needs to be extended by inserting an additional row in the table between the Input and Output files. In the left hand cell of the new row the word 'Field' should be typed and then use Insert | Form | Drop-Down Box to define a selection box in the middle column. This box should be given the name 'selFields'. The interface should look like the one below (you may need to set the width of the drop-down box to 115 pixels to give it some initial width).

![](../Images/Studio3%20Scripting%20Browse%200002.jpg)

In order to fill in the list with the names of the fields from the input file, use the following function call in the btnBrowse1_onclick() function.

oScript.makeFieldsPicklist(tbInputFile.value, selFields);

The entire event handler code should now look like this.

function btnBrowse1_onclick() {  
tbInputFile.value = DisplayBrowser();  
oScript.makeFieldsPicklist(tbInputFile.value, selFields);  
}

The makeFieldsPickList has two arguments, the first is the input filename and the second is the name of the select (drop-down box) list where the names are to be added. It is possible to add a third, optional argument to this method, which gives the default value to be displayed. The default value need not necessarily be the name of a field in the file.

Finally, we need to modify the btnOK_onclick() handler for the OK button. The 'copy' command becomes a 'selcop' command, and we need to add the name of the selected field to the command. The new code looks like this:

var theCommand = "selcop &in=" + tbInputFile.value + " &out=" + tbOutputFile.value + " *f1=" + selFields.value + " @keepall=1";

The parameter keepall (set to 1) instructs the command to keep all data and not discard duplicates in the output file. The complete btnOK_onclick() handler should look like the following:

function btnOK_onclick() {  
if (tbInputFile.value == "" || tbOutputFile.value == "") {  
alert("Missing file name");  
return;  
}  
var theCommand = "selcop &in=" + tbInputFile.value +  
" &out=" + tbOutputFile.value +  
" *f1=" + selFields.value + " @keepall=1";  
if (tbRetrieval.value != "")  
theCommand += " {" + tbRetrieval.value + "}";  
oDmApp.ParseCommand(theCommand);  
}

Note that we have also added an alert method to inform the user when input or output files are missing:

![note.gif \(1017 bytes\)](../images/note.gif) |  The reference file for this script is _scr_Browse_and_Copy 0002.htm and can be found in the project directory.  
---|---  
  
## Copying Multiple Fields

For this extension the changes to the user interface are easy; in the Properties dialog for the drop-down box element, set the Height to 4 lines, and check the Allow multiple selections radio button. The User Interface now looks like this.

![](../Images/Studio3%20Scripting%20Browse%200003.jpg)

No changes are needed in the script, apart from adding code to extract the values from the selected items in the drop-down list object. This is done by making further changes to the btnOK_onclick() handler. The code should look like the following:

function btnOK_onclick() {  
if (tbInputFile.value == "" || tbOutputFile.value == "") {  
alert("Missing file name");  
return;  
}  
var theCommand = "selcop &in=" + tbInputFile.value + " &out=" + tbOutputFile.value;  

// Extract selected options from multiple-select menu  
var opts = selFields.options.all;

// "opts" is the collection of all options  
var fieldNum = 0;  
for (var i = 0; i < opts.length; i++) // opts.length is the total number of options  
if (opts(i).selected)  
theCommand += " *f" + (++fieldNum) + "=" + opts(i).value  
if (fieldNum == 0) {  
alert("No fields selected.");  
return;  
}  
if (tbRetrieval.value != "")  
theCommand += " {" + tbRetrieval.value + "}";  
oDmApp.ParseCommand(theCommand);  
}

The field 'opts' is first set to the collection of all options within the selFields drop-down list. This list box has a property called 'selected' which informs us as to which items are actually selected by the user. Those that are selected are appended to the command for retrieval by the SELCOP command. Note, that if no fields are selected the routine returns without doing anything.

![note.gif \(1017 bytes\)](../images/note.gif) |  The reference file for this script is _scr_Browse_and_Copy 0003.htm and can be found in the C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts directory.  
---|---