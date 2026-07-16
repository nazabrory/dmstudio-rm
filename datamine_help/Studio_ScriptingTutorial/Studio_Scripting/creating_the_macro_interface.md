![](../HeaderCell.jpg) |  Creating the Macro Interface  
---|---  
  
# Creating the Macro Interface

The interface we are going to create is shown below:

![](../Images/Studio%20Scripting%20MacroShovel%200002.jpg)

This interface contains three of the five substitution parameters that we are going to use in the macro. These are the azimuth and elevation of the shovel. The Append Shovels field will be used to determine whether data overwrites or is appended to the file.

## Prerequisites

  * The macro file Shovel.MAC will be used in this exercise.  
  
This file can be found under C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts. Copy the file _scr_Shovel.MAC to Shovel.MAC now so that you can change the body of the macro when required.

  * The Datamine file shovtr.dm and shovpt.dm will contain the output wireframe data.  
  
These files can be found under C:\Database\DMTutorials\Data\VBOP\Datamine

## Links to exercises

The following exercises are available on this page:

  * Drawing a table to contain the interface objects

  * Adding some text and text boxes

  * Adding a check box

  * Adding a push button

  * Assigning names and values to the controls

## Exercise: Drawing a table to contain the interface objects

You will use a text editor to create the framework script:

  1. Use a text editor (any ASCI editor will be fine) to create a new, empty file.
  2. Save the file as 'Shovel.htm' in the ...Projects\S3ScriptTut\ProjFiles\MyProj1\ directory.
  3. In your empty text file, enter the following:

<html>

<head>

</head>

<body>

</body>

</html>

  4. Create a table using basic HTML syntax containing six rows and two columns. To do this enter the following between the <body> and </body> tags (create new lines):

<table>

<tr><td></td><td></td></tr>

<tr><td></td><td></td></tr>

<tr><td></td><td></td></tr>

<tr><td></td><td></td></tr>

<tr><td></td><td></td></tr>

<tr><td></td><td></td></tr>

</table>

## Exercise: Adding some text and text boxes

Next we will add some text and text boxes to the table. The text describing the contents of the text boxes will be placed into the left hand cells of the table and the text boxes themselves into the right hand cells where appropriate.

  1. Edit the first <tr>...</tr> line in your script by placing the text 'Creating a Wireframe Shovel' between the first <td> and </td> tags, i.e.:

<tr><td>Creating a Wireframe Shovel</td><td></td></tr>

  2. In the next row down, in the same place, type the word 'Shovel Azimuth':

<tr><td>Shovel Azimuth</td><td></td></tr>

  3. In the next row down, type the word 'Shovel Elevation'.

<tr><td>Shovel Elevation</td><td></td></tr>

  4. Next, you need to add a text box form control to the 2nd row of the table, by adding the relevant HTML syntax between the second <td> and </td> tags:

<tr><td>Shovel Azimuth</td><td><input type="text"></td></tr>  

  5. Now repeat step 4 for row three and insert another text box in the cell below:

<tr><td>Shovel Elevation</td><td><input type="text"></td></tr>  

  6. Add a text box to the bottom (6th) table row by modifying this line so that the <td> element spans both columns (the second set of <td></td> tags are removed as they are not needed):

<tr><td colspan = "2"><input type="text" width = "40"></td></tr>

## Exercise: Adding a check box

Next we will add a check box to the table. The text describing these will be associated with the check box itself.

  1. In your script, go to the fourth <tr>...</tr> line and, between the first <td> and </td> tags, enter the HTML syntax for a check box:

<tr><td><input type="checkbox"></td><td></td></tr>

  2. Between the second set of <td> and </td> tags in the same row, type the text 'Append shovels':

<tr><td><input type="checkbox"></td><td>Append Shovels</td></tr>

## Exercise: Adding a push button

Next we will add a push button to the fifth row of the table:

  1. In the fifth row, enter a push button control between the first <td> and </td> tags:

<tr><td><button type="button">Create Shovel</button></td><td></td></tr>

  2. Save your file and double-click it in your browser to launch it as a standalone web page - your interface should now look similar to the one shown at the start of this section, although the formatting may differ depending on your browser's default formatting options.
  3. You can also use your own knowledge of HTML tables and formatting to change the appearance of the table if you wish.

## Exercise: Assigning names and values to the controls

Before we can make anything happen, we need to assign names and initial values to all of the interface controls. Names can be anything that you wish, but remember that upper and lower case letters are distinct (the name 'this' is different from 'This'). A good idea is to prefix the names of controls with two or three letters that identify the type of control, e.g. btnOK for an OK button, or tbSelectedFile for a text box that will contain the name of a selected file.

If you have access to a dedicated HTML editor (such as Dreamweaver, Visual Studio etc.) you can shortcut some of the manual steps below by using an interactive equivalent.

  1. Edit the 2nd table row so that you assign the name 'tbAzimuth' to the text box. You will also need to set a default value of zero:

<tr><td>Shovel Azimuth</td><td><input type="text" name = "tbAzimuth" value = "0"></td></tr>

  2. Similarly, edit the Shovel Elevation text box so that it has a name attribute of 'tbElevation' and a '0' (zero) default value.

<tr><td>Shovel Elevation</td><td><input type="text" name = "tbAzimuth" value = "0"></td></tr>

  3. Next, assign the name 'cbAppend' to the Append Shovels text box:

<tr><td><input type="checkbox" name = "cbAppend"></td><td>Append Shovels</td></tr>

  4. Next, assign the name 'btnCreateShovel' to the Create Shovel button:

<tr><td><button type="button" name = "btnCreateShovel">Create Shovel</button></td><td></td></tr>

  5. Save your file and launch it in a browser to check that the interface still appears as expected (you'll notice that the table is a little wider than before)

![note.gif \(1017 bytes\)](../images/note.gif) |  Be sure to use the exact names for the controls as given in the text above as they are case sensitive.  
---|---