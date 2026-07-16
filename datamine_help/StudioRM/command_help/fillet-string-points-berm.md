# fillet-string-points-berm

See this command in the [**command table**.](<COMMAND%20TABLE_F.md#fillet-string-points-berm>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "fillet-string-points-berm"

  * Use the quick key combination "spbf".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **fillet-string-points-berm** and click **Run**.

## Command Overview

Specify the maximum curvature radius permitted between line segments on a selected berm string. Points are added to the line.

This command will fillet all coincident angles according to the values specified. If you wish to fillet a single point (or selected points) on a line, use the [fillet-single-string-point](<fillet-single-string-point.md>) command instead.

Command steps:

  1. Run the command.

  2. Specify a maximum radial curvature (using the Fillet String Points screen).

  3. Select the line you wish to amend, for example:  
  
[![](../Images/Fillet1.gif)](<javascript:void\(0\);>)  
  

  4. The new line will then be modified (filleted) to create the necessary points in order to maintain the specified radial curvature, for example, the above line image, filleted to a radius of 30 shows:  
  
[![](../Images/Fillet2.gif)](<javascript:void\(0\);>)

Related topics and activities

  * [fillet-single-string-point](<fillet-single-string-point.md>)