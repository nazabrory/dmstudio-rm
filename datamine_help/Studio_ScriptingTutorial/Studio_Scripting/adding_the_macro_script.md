![](../HeaderCell.jpg) |  Adding the Macro Script  
---|---  
  
# Adding the Macro Script

The first step is now complete: we have an HTML user interface, together with all the hooks for the script.

The script language used is not a part of your application - you can use any of a number of standard programming languages: JavaScript, VBScript, PerlScript, PowerBuilder's PowerScript, Python etc. The two languages supported by FrontPage 2003 are VBScript and JavaScript. You should note, however, that not all languages are supported by the latest browsers - for example, VBScript is not supported in Internet Explorer version 10 or higher (although in some cases this can be circumvented with emulation of an earlier version).

Unlike macros and menus, scripts are usually made up of a number of event handlers. These are small sections of script that are executed by the browser when some relevant event occurs.

Only two events are handled in this script:

  * When the window loads (a window onload event occurs). We use this event to make a connection to the Datamine Application Object.

  * When the OK button is pressed (a button onClick event occurs). We use this event to perform the tasks. These include picking a point in the 3D window to locate the shovel, saving the macro 'var' file, calling the macro and finally loading the wireframe file back into the 3D window.

## Prerequisites

  * Ensure a suitable scripting environment is available.

  * We will continue to use the Shovel.htm file created in the previous exercise - [Creating the Macro Interface](<creating_the_macro_interface.md>). This file was stored in C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts

## Links to exercises

The following exercises are available on this page:

  * Adding the windows onload event

  * Adding the Create Shovel button onClick handler

**![](../images/UpArrow.gif)**Top of page

## Exercise: Adding the windows onload event

In this exercise we will add an event that will be fired when the window is loaded.

  1. Above the main window (the one displaying the code), you will notice two drop down list boxes. The left hand one contains the text 'Client Objects & Events' and the right hand one contains the text '(No Events)'.
  2. Using the left hand drop down box and select the item 'window'.
  3. Using the right hand drop down box select the item 'onload'. The following text has been added to the code in the main window. Note: if after selecting the onload item, the words 'Sub window_onload()' appears in the code window, then Script Editor is configured to use VBScript.

function window_onload() {   
}

  4. We now need to enter the JavaScript code to be executed when this event occurs. First, we need to establish a connection between the script and the Studio Application Object. To accomplish this we must define a Datamine application variable, and refer to a routine to instantiate the datamine application object. 
  5. Before the function window_onload() type the following text.  
  
var oDmApp = null;  
var oScript = null;
  6. Within the body of the window_onload() function (between the '{' and '}' characters), type the text 'AutoConnect();'. This instructs the onload event to call a function AutoConnect that we will now write. This routine will use the variable oDmApp defined in step 5.
  7. After the window_onload() function and after the '}' symbol copy and paste (as HTML) the following text:  
  
  
function AutoConnect()  
{  
oScript = new ActiveXObject("DatamineStudio.ScriptHelper");   
oScript.initialize(window);  
oDmApp = oScript.getApplication();  
if (oDmApp== null)  
return false;  
  
else  
  
return true;  
}

  8. The final code should look like the following:

var oDmApp= null;  
var oScript = null;

function window_onload() {  
AutoConnect();  
}

function AutoConnect() {   
oScript = new ActiveXObject("DatamineStudio.ScriptHelper");  
oScript.initialize(window);  
oDmApp = oScript.getApplication();  
if (oDmApp== null)  
return false;  
else  
return true;  
}  

![note.gif \(1017 bytes\)](../images/note.gif) |  The variable oDmApp, oScript and the AutoConnect function are necessary for every scripted solution that connects to the Datamine Application Object. The AutoConnect function initialises the Studio Application Object and presents the script with access to this object via the oDmApp variable. The oScript variable gives access to the Script Helper object.  
---|---  
  
**![](../images/UpArrow.gif)**Top of page

## Exercise: Adding the Create Shovel button onClick handler

In this exercise we will add an onClick event that will be fired when the Create Shovel button is pressed. When the button is pressed, the script executes a series of commands, some of which are interactive.

At the end of the script the data is loaded into the 3D Window. This code is quite straightforward, but reasonably lengthy.

  1. Using the left hand drop down box and select the item 'btnCreateShovel'.
  2. Using the right hand drop down box select the item 'onclick'. The following text has been added to the code in the main window.

function btnCreateShovel_onclick() {

}

  3. Within the body of the btnCreateShovel_onclick() function (between the '{' and '}' characters), copy and paste (as HTML) the following text.

var intAppend = 0;  
if (cbAppend.checked) {  
intAppend = 1 ;  
}  
  
if (tbAzimuth.value == "") {  
alert ("Enter a valid Azimuth for the shovel") ;  
return ;  
}   
  
if (tbElevation.value == "") {  
alert ("Enter a valid Elevation for the shovel") ;  
return ;  
}  
  
// ok lets tell the user what to do next  
tbInfo.value = "Please select a point in the design window" ;  
objVars = new Object() ;  
objVars.APPEND = intAppend ;  
objVars.AZIM = tbAzimuth.value ; 

// Get the point in the design window that will represent E and N we will override Z  
strPoint = oDmApp.ActiveProject.Design.Selection.PickPoint("Select a point");  
var aryTemp = strPoint.substr(7).split(",");  
objVars.E = parseFloat(aryTemp[0]);  
objVars.N = parseFloat(aryTemp[1]);  
// objVars.Z = parseFloat(aryTemp[2]);  
objVars.Z = tbElevation.value ;  
oScript.varsave(varfile, false, objVars); 

// Now run the macro  
oDmApp.ActiveProject.RunMacroFile("Shovel.mac", "T");  
// now load the wireframe file into the design window and refresh the screen  
tbInfo.value = "";  
oDmApp.ExecuteCommand("unload-all-data");  
oDmApp.ActiveProject.Data.LoadFromProject("shovtr");  
oDmApp.ActiveProject.Data.LoadFromProject("shovpt");  
oDmApp.ExecuteCommand("zoom-all-extents");  

  4. We also need to add a variable for the 'var' file and should be the name of the macro that we are running. We will also initialise thetbInfotext box so that no text is shown when the script loads as shown below.

var varfile = "Shovel.var";  
var oDmApp= null;  
var oScript = null;

function window_onload() {  
AutoConnect();  
tbInfo.value = "";  
}

  5. After this code has been added to the HTML document, save it.

**![](../images/UpArrow.gif)**Top of page

![note.gif \(1017 bytes\)](../images/note.gif) | 

## Operation of the Script

The btnCreateShovel_onclick() event handler script creates a wireframe shovel in the design window at the location specified by the user. First the script checks the state of the Append Shovel check box and sets a variable called intAppend so that the value can be passed to the macro. The script then checks that the Shovel Azimuth and Shovel Elevation fields are not empty and only allows the script to proceed if they have values in them. The next step is interactive and we provide a prompt to the user by filling in the tbInfo text box with the words 'Please select a point in the design window'. At this point the user should click somewhere in the design window. The command PickPoint provides a string with these parameters in it. The string is then parsed to obtain the individual X, Y and Z values which are placed into an object called objVars as E and N (notice that the Z field is overwritten with the elevation from the text box). There are many ways to pass variables to a macro. We have decided to create an object and pass the object to the varsave function. The object should contain the names of the variables of the substitution parameters within the macro. Once the varsave command is invoked the shovel.var file will contain the parameters as set by the user. The macro is then executed. This action will either create a new shovel wireframe or append the new shovel to an existing file. Finally we reset the tbInfo text box the system unloads all the data and reloads the 'shovtr' and 'shovpt' Datamine files and then zooms the screen so that all the data fits neatly.  
---|---