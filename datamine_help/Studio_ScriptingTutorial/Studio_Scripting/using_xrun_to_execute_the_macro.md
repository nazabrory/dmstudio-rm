![](../HeaderCell.jpg) |  Using XRUN to Execute the Macro  
---|---  
  
# Using XRUN to Execute the Macro

We will first examine the Macro that we are going to use. This is located in your project directory and called _scr_Shovel.MAC. This file in turn uses a wireframe definition, and can be found under C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts

The macro uses the standard techniques for setting default values and prompting. The main steps are.

  * Define default values for substitution variables.

  * Test whether the 'var' file exists, and if it does replace the initial defaults with the saved values.

  * Use prompt to define current values, with defaults as defined in the previous steps.

  * Create and display the wireframe model at the required location.

  * Save the substitution variables.

You will see that the five substitution variables that are prompted for using the prompt command are.

  * $APPEND# - decision whether to append shovels into a single file or overwrite the file. A zero overwrites the file.

  * $E# - position of the shovel in Easting.

  * $N# - position of the shovel in Northing.

  * $Z# - position of the shovel in Elevation.

  * $AZIM# - the orientation of the shovel in degrees. Zero degrees represents North.

In the following exercise we will remove these prompts from the macro and create a script with an HTML interface that will run the macro.

To see how the macro works, save a copy of the macro file _scr_Shovel.MAC as Shovel.mac in your Tutorial project directory. Then run the macro by typing 'XRUN' into the Run Command window and taking all the default values to the prompts. The macro will create a wireframe file called shovtr.dm and shovpt.dm. At the end of the macro this file will not be displayed automatically.

The text in the Output window shows the progress of the macro. The figure above represents a shovel located at -50 Easting, 20 Northing and 0 Elevation with an Azimuth of 45 degrees.