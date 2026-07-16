# VARFIT Process  
  
**Note** : **VARFIT** is now superseded by more comprehensive model fitting functions available in the [Advanced Estimation](<../STUDIO_RM/Multivariate_Introduction.md>) wizard.

To access this process:

  * Enter "VARFIT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **VARFIT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_V.md#VARFIT>).

## Process Overview

The process allows you to display experimental variograms, as produced by the [VGRAM](<vgram.md>) process, and fit a model to them using interactive graphics.

Note: If you are planning to use a [Variogram Chart](<../PLOTS_LOGS/VARMOD_Model_Fitting.md>) to either load existing **VARFIT** variogram models or create new variogram models from VGRAM generated experimental variograms, please see [this page](<../PLOTS_LOGS/Rotation_Parameters_in_VARFIT_and_Variogram_Charts.md>) for more information on rotation parameters.

Either an isotropic or an anisotropic model can be defined, comprising a nugget variance and up to 9 individual structures. Each structure may be either spherical, power, exponential, Gaussian or De Wijsian. Parameters for models comprising one, two or three structures can be moved on the screen with the mouse. Models with four or more structures are edited by entering the parameters directly.

The model parameters can be saved in the output file. They can then retrieved and edited in subsequent use of VARFIT, and can be used as input to the grade estimation process [ESTIMA](<estima.md>).

As well as displaying the variograms on the graphics screen the process also allows the variograms to be listed. Therefore all details pertaining to each variogram can be accessed interactively. This includes the lag distance, number of sample pairs, covariance and the three different types of variogram. The mean and variance of the samples is also given.

The available commands are divided into three menus:

  1. Variogram Fitting - this is the main menu for selecting variograms and fitting a model.
  2. Display Control - use this menu for customizing the graphics area.
  3. Plotting - this menu just includes creating and superimposing plot files.

Details of the commands in each menu are given below.

### Experimental Variograms

Use "Variogram - Summary" to get a complete list of all variograms in the input file. Then select the ones you want to display using "Variogram \- Add/Remove". The variograms are then added to the display list, with a legend entry for each one. You can temporarily remove a variogram using the "Variogram - Show/Hide command". Select the variogram to be removed by clicking its legend entry. Click it again to restore it.

### Fitting a Model

Use the "Define New Model" command to create an initial model. You can select up to three structures which will all be spherical (type=1). If you want different variogram types then edit the model via the keyboard ("Edit Model - Keyboard"). If you want more than 3 structures then you will have to use the keyboard method for defining the model parameters. If you have 3 or less structures then you can edit the model parameters using the mouse ("Edit Model - Mouse").

### Model Rotation

If you select an isotropic model then it will have the same range in all three directions, and so you do not need to define the model rotation. If you select an anisotropic model, then by default the axes of the model will lie along the coordinate axes. If you want the model axes to be rotated with respect to the coordinate system then you must use either "Model Rotation - Mouse" or "Model Rotation \- Keyboard". If you use the mouse method for model rotation then one of the experimental variograms being displayed must lie along the X axis of the model. A second experimental variogram must also be displayed which lies in the XY plane of the model. Usually this is along the Y axis of the model, but it is not compulsory for it to be so. The process will calculate the model Y axis, as lying in the XY plane, perpendicular to the X axis. The model Z axis will then be calculated perpendicular to the XY plane. The process will also calculate the angles that are needed to rotate from the coordinate system to the model system. If you use the keyboard method for model rotation then you are prompted to enter the angles that are needed to rotate from the coordinate system to the model system.

### Editing The Model

You can edit the model parameters using the keyboard or the mouse, or a combination of both. If you use the mouse method then select the parameter to be moved by clicking it with the right mouse button, and move it with the left mouse button. If you want to set one of the parameters to an exact value, then use the "Edit Model - Keyboard" command. You can do this while you are editing the model with the mouse.

### Range:Sill Link

A symbol is displayed to identify the three ranges and the sill for each structure. Initially, when you select a range symbol and move it with the mouse, then the sill remains constant. However if you select "Toggle - Range:Sill Link", then moving the range symbol will also move the sill. You can toggle between the two methods while editing the model with the mouse.

### Angle Definition

If you calculated your variograms using [VGRAM](<vgram.md>), and you used the rotated plane option, then the variogram file will contain the azimuth and dip of each variogram in both the world coordinate system (fields **WAZI** and **WDIP**) and in the local (rotated) coordinate system (fields **AZI** and **DIP**). When the variograms are initially displayed in **VARFIT** the legend is in terms of the local coordinate system. You can toggle between the two systems using the "Toggle - Angle Definition" command.

### Help

Help information is available for every command. First select the Help button from the menu, and then select the command for which you require help. Selecting help on help will cancel the command.

### Macros

**VARFIT** can be run from a macro. If you simply want to load **VARFIT** from the macro and then use **VARFIT** interactively you should put the command !**KBON** immediately before !**VARFIT** and !**KBOFF** immediately afterwards. If you want to include **VARFIT** commands in the macro then the best way is to set macro recording and run **VARFIT** interactively first. The resulting macro will show you the 2 character code for each command. You can then edit the macro if required. In fact you must replace any single ! by [ or ]. A single ! will always occur when you terminate the selection of variograms for the initial display. If you insert ** as a command then control will pass from macro mode to interactive use. When you exit **VARFIT** , control will return to the macro. The two character codes are also given in the file varfit.aim in the helpfile directory.  

## VARIOGRAM FITTING Menu

### Help

When you select the "Help" command you are immediately prompted to select the command for which you require help. Select the **Help** command again to cancel.

### Redraw

Redraw the **Graphics** window.

### Variogram - Summary

Display a summary list of all variograms in the input file to the **Output** window.

### Variogram - List

List an experimental variogram to the **Output** window.

### Variogram - Add/Remove

Use this command to add or remove variograms from the display list. Specify the variogram number to add it, or specify it as a negative number to remove it. Specify **+** to add all variograms, or **-** to remove all. Terminate adding or removing variograms with a **!**

### Variogram - Show/Hide

When you add a variogram to the display list, using **Add/Remove Variograms** , it will automatically be displayed. If you want to hide it temporarily, but you do not want to remove it from the display list, then use the **Show/Hide Variograms** command. The variogram to be hidden is selected by clicking on the legend at the required variogram entry. The display for that variogram will then be hidden. Click again to restore the display.

### Variogram \- Remove Hidden

Variograms which are in the display list, but which are currently hidden, are annotated in white. This command removes the hidden variograms from the display list. In order to display them again at a later stage you will have to use the **Variogram \- Add/Remove** command.

### Variogram \- Perpendicular

This command selects all variograms which are perpendicular to the reference variogram. You choose the reference variogram by clicking the appropriate legend entry with the mouse. The reference variogram and all perpendicular variograms are then displayed on the graphics screen, and are summarized in the **Output** window. Any variograms which were previously displayed are now hidden. You can continue to choose different reference variograms with the mouse without having to reselect the command. Choose any other command to terminate the selection of perpendicular variograms.

### Define New Model

This command will define ranges and sills for a model variogram. You can define whether you want a 1,2 or 3 structure spherical model, and whether or not you want the model to be isotropic (same range in all 3 directions). The maximum sill is set equal to the variance of the samples, but the values of all other parameters are based on the extent of the graphics display, and not on any statistical fitting method. It is simply intended to give a starting point for you to fit the model.

You can also use this command to delete a model, so that no model is currently defined.

### Model Rotation - Mouse

When a new model is defined using the **Define New Model** command, the axes of the model are set parallel to the axes of the coordinate system. If your model is not parallel to the coordinate system then you must define the orientation of the model using either:

  * **Model Rotation - Mouse** , or;

  * **Model Rotation - Keyboard** (see below)

The **Model Rotation - Mouse** command allows you to define the axes of the model variogram by selecting the experimental variograms which lie along the axes of the model. Therefore at least two experimental variograms must be displayed, which are in directions that are perpendicular to each other. The third axis will then be calculated, as it must be perpendicular to the other two.  
  
You must first select the experimental variogram which corresponds to the X axis of the model. Then select either the variogram corresponding to the Y axis, or any variogram which lies in the XY plane of the model. If you do not select the Y axis, then it is calculated automatically as being 90 degrees from the X axis in the XY plane you have defined. You select the two variograms by clicking the mouse on the legend entry of the required variogram.

### Model Rotation - Keyboard

When you use the **Define New Model** command, the initial model you specify is parallel to the axes of the coordinate system. If you want the model to be rotated with respect to the coordinate system then you must specify the rotations. This can be done either through the keyboard, using the **Model Rotation \- Keyboard** command, or with the mouse, using the **Model Rotation - Mouse** command.

When using the **Model Rotation - Mouse** command you are prompted to enter the rotation angles and the axes about which the rotations take place.

### Edit Model - Mouse

This command allows you to change the model variogram parameters with the mouse. Select the parameter to be changed by clicking close to the required parameter with the right mouse button, and then select the new position with the left mouse button. You can continue repositioning the parameter by further clicks of the left mouse button.

If no model is defined when you select this command, then the **Define New Model** command is activated automatically. You must then reselect the **Edit Model - Mouse** command to start editing the model.

You can select certain commands without leaving the **Edit Model - Mouse** command. These include:

  * Redraw

  * Toggle - Previous Model

  * Toggle - (An)isotropy

  * Toggle - Range:Sill Link

  * Variogram - Show/Hide

  * Edit Model - Keyboard

Use the **Edit Model - Keyboard** command to round parameters to suitable values, if required.

### Edit Model - Keyboard

Define a new model or edit an existing model by entering the parameters through the keyboard.

### Cancel

Use this command if you wish to terminate a command which uses mouse selection from the Graphics window. For example **Edit Model - Mouse** , or **Model Rotation - Mouse**.

### Model \- Get From File

Get a model which has previously been saved in the variogram model file.

### Model \- Write To File

Write the current variogram model to the output model file.

### Model \- List Parameters

List the parameters of the current variogram model to the Output window.

### Toggle \- Previous Model

If the toggle is ON then when a model parameter is changed then both the new and the previous models are displayed. All previous models are displayed until the **Redraw** command is selected.

### Toggle \- Parameter Symbols

When you define a model, symbols are displayed corresponding to the ranges and sills of the model. Use this command to switch the display of the symbols off and on.

### Toggle \- Number Of Pairs

The number of pairs of samples used for calculating the variogram value can be annotated on the graphics screen. This command switches the annotation on and off. Note that the number of sample pairs can also be found by using the **Variogram - List** command. Also the **Minimum Number Of Pair** s command can be used to remove from the display any variogram point which has less than the minimum number of sample.

### Toggle - (An)isotropy

When you created the model, you created it as either isotropic (same range in all 3 directions), or anisotropic different ranges in different directions. This command allows you to switch between isotropic and anisotropic. If the model was originally isotropic, then this command will create individual ranges, although they will initially be the same. If the model was originally anisotropic then an isotropic range is created as the average of the 3 individual ranges for each structure.

### Toggle \- Range;Sill Link

This toggle applies when you are editing the variogram model parameters using the mouse. Initially if you select a range as the parameter to move, then only the range moves and the sill remains fixed. The sill can be moved by selecting it and then moving it. If you toggle the range:sill link, then when you move the range, the sill will also move. Select the toggle again if you want to disconnect them.

### Toggle \- Angle Definition

If the variograms have been calculated using [VGRAM](<vgram.md>) and if a rotated plane was specified when VGRAM was run, then the input variogram file will contain the azimuth and dip of the variograms in both the world and local (rotated) coordinate systems. The "Toggle \- Angle Definition" command allows you to switch between the two definitions. The azimuth and dip shown in the legend will change accordingly.

## DISPLAY CONTROL Menu

### Help

When you select the "Help" command you are immediately prompted to select the command for which you require help. Select the "Help" command again to cancel.

### Redraw

Redraw the **Graphics** window.

### Edit \- X/Y Minimum Values

This command allows you to define the minimum values on the X and Y axes.

### Edit \- X/Y Maximum Values

This command allows you to define the maximum values on the X and Y axes.

### Edit \- X Grid Interval

This command allows you to define the spacing between grid lines on the X axis. It also lets you define the number of decimal places to be used for the annotation of the grid lines.

### Edit - Y Grid Interval

This command allows you to define the spacing between grid lines on the Y axis. It also lets you define the number of decimal places to be used for the annotation of the grid lines.

### Annotate \- Axes

Change the annotation on the X and Y axes.

### Annotate \- Plot

Define a line of text and display it at any location in the data area. You may define up to 20 independent lines of text each with a maximum of 72 characters. For each line you are prompted to define the starting point of the text using the mouse. To remove a line of text select the required line number and just press ENTER at the _ANNOTATION_ prompt.

### Change Character Size

Change the character size and aspect ratio for all text displayed on the graphics screen.

### Edit Variogram Attributes

Each variogram which is displayed is assigned a color, a linetype and a symbol. This option allows you to change these settings.

### Select Normal/Log/Relative

The input variogram file includes the normal variogram, the lognormal variogram, the pairwise relative variogram, and the covariance. You can select the variogram to display from a menu in the **Output** window.

### Minimum Number Of Pairs

You can select the minimum number of sample pairs to be displayed. If any variogram point has less than the minimum number, then it will not be displayed.

### Default Settings

The default settings you can change are:

  1. Lines Between Prompts

Some of the commands which write text to the **Output** window divide the text into sections, with a prompt between each section. This option allows you to define the number of lines between prompts. Enter 0 for no prompting.

  2. Pairs Annotation Angle

The "Toggle - Number of Pairs" command annotates the number of pairs of samples at each variogram point. You can change the angle of the annotation; 0 is horizontal, 90 is vertically downwards, etc.

  3. Dividing Factor

You can scale the variogram values plotted on the Y axis by specifying a dividing factor. All variogram values are divided by this factor prior to being displayed. If the factor is greater than 1, then the values are decreased; if less than 1 then the values are increased. A model is fitted to the adjusted values. However if it is saved to the output file then the true values are written. If a model is read from file then it is adjusted by the factor, before being displayed.

### Toggle \- Autoscaling

Autoscaling is initially set ON. This means that the initial minimum values on the X & Y axes are set to zero and the initial maximum values are set automatically depending on the maximum X & Y values of the first variogram selected. The interval between grid lines is also set automatically.

If autoscaling is ON and you add or remove variograms, then the maximum Y value and the Y grid interval are adjusted automatically to fit the variograms. The maximum X value and the X grid interval will not be changed. If autoscaling is ON then the minimum X and Y values will always be set to zero.

If you toggle autoscaling OFF then the current X & Y minimum and maximum values and grid intervals are maintained irrespective of variograms which may be added to or removed from the display. To change the values you must either reset them using the individual Edit commands or toggle autoscaling back ON.

Note that the maximum value on the X axis is set according to the maximum value of the first variogram displayed. Toggling autoscaling ON or OFF will not affect the maximum X value or the X grid interval. The only way to change these two values is to use the individual Edit commands to reset them.

### Toggle \- Background Colour

The initial display has a black data area, with a grey background. You can toggle between a grey and a black background using the **Toggle - Background Colour** command.

### Toggle \- Bell

Some commands include a bell to draw your attention to information displayed on the **Output** screen. The "Toggle - Bell" command allows you switch the bell on or off.

### Toggle \- Grid Type

A full grid is displayed on the initial screen. You can toggle between the full grid and tick marks using the **Toggle - Grid Type** command.

### Toggle \- Legend Display

Switch the legend display on or off.

### Toggle \- Legend Header

The legend header is a single line of text located immediately above the legend. This commands allows you to switch the display of the legend header on and off.

### Toggle \- Normalise

The **Normalize** toggle allows you to normalize the displayed variogram(s). This means that all variogram values are divided by the variance, so that the sill is set to 1. This is particularly useful when comparing variograms from different rock types or different cutoffs for indicator variograms.

### Toggle \- Symbol Display

A symbol is plotted at each point on the experimental variogram. This command allows you to switch the display of symbols on or off.

### Toggle \- Text Display

The initial **Graphics** window includes a text area in which the variogram model parameters are displayed, if defined. The position of the origin of the data area is controlled by the environment variable **DATA_AREA** which is usually defined in the aim file **VARFIT.AIM.** The aim file should also include an environment variable **DATA_AREA_NOTEXT** which defines an alternative layout which does not include the text area. You can swap between the two layouts using the **Toggle - Text Display** command.

### Toggle \- Variance

If you toggle the variance ON, then a horizontal line is displayed showing the variance of the samples. The default is OFF, so the line will not be plotted.

### Run Macro

This option allows you to run a sequence of commands which had previously been saved in a text file.

The best way of writing a macro is to switch macro recording on before you enter **VARFIT**. Then use the commands which you want to store in the macro, so that the command names and responses are saved to the file. Exit from **VARFIT** , and switch macro recording off. Edit the text file in your system editor. Remove the !**START** , the call to !**VARFIT** , the **EX** (exit) command, !**END** , and any of the **VARFIT** commands which you do not want included. Then reenter **VARFIT** and use the **Run Macro** command.

## PLOT FILES MENU

### Help

When you select the **Help** command you are immediately prompted to select the command for which you require help. Select the command again to cancel.

### Redraw

Redraw the **Graphics** window.

### Create Plot File

The current display is saved in a database file. A grey border, if displayed on the screen, will not be included in the plot file.

### Superimpose Plot File

Superimpose an existing plot file on the **Graphics** window.

## Exit

Exit the variogram fitting process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File containing experimental variogram[s]. This will usually be created by VGRAM. The file can contain up to 500 variograms. |  Input |  Yes |  Variogram  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Input and output file for parameters of fitted models. The file contains one record per model. If the file already exists and contains all the required fields [53 fields in total] then any existing models are maintained, otherwise the file is deleted and a new one created. The new file will contain the following fields: **VREFNUM** \- variogram reference number  **VANGLE1** \- first rotation angle **VAXIS1** \- first rotation axis  **VANGLE2** \- second rotation angle  **VAXIS2** \- second rotation axis  **VANGLE3** \- third rotation angle  **VAXIS3** \- third rotation axis  **NUGGET** \- nugget variance  **ST1** \- model type for structure 1 

  * 1=spherical
  * 2=power
  * 3=exponential
  * 4=gaussian
  * 5= De Wijsian

**ST1PAR1** \- parameter 1 for structure 1  **ST1PAR2** \- parameter 2 for structure 1  **ST1PAR3** \- parameter 3 for structure 1  **ST1PAR4** \- parameter 4 for structure 1  **ST9** \- model type for structure 9  **ST9PAR1** \- parameter 1 for structure 9  **ST9PAR2** \- parameter 2 for structure 9  **ST9PAR3** \- parameter 3 for structure 9  **ST9PAR4** \- parameter 4 for structure 9  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
AVE.DIST |  The field to be plotted along the X axis. Usually either **LAG** or **AVE.DIST**. The default is **AVE.DIST**. |  IN |  No |  Numeric |  AVE.DIST  
VGRAM |  The field to be plotted along the Y axis.  |  IN |  No |  Numeric |  VGRAM  
KEY |  If the **IN** file was created using **VGRAM** and a **KEY** field was used, then the name of the **KEY** field should be specified here. |  IN |  No |  Any |  Undefined  
AZI |  Field containing azimuth of experimental variogram.  |  IN |  No |  Undefined |  AZI  
DIP |  Field containing dip of experimental variogram. Usually **DIP** , the default. |  IN |  No |  Numeric |  DIP