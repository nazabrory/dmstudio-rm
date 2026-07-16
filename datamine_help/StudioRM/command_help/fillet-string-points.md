# fillet-string-points ("spf")

See this command in the [**command table**.](<COMMAND%20TABLE_F.md#fillet-string-points>)

To access this command:

  * **Edit** ribbon **> > Condition >> Condition >> Fillet String Points**.
  * **Digitize** ribbon **> > Condition >> Condition >> Fillet String Points**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "fillet-string-points"

  * Use the quick key combination "spf".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **fillet-string-points** and click **Run**.

## Command Overview

Soften sharp string direction changes by setting the maximum curvature radius permitted between line segments on a selected string. Points are added to the line to meet the radius setting. 

Data can be selected before running the command, or during the command session.

**Note** : This command fillets all coincident angles according to the values specified. To fillet a single point (or selected points) on a line, use the [fillet-single-string-point](<fillet-single-string-point.md>) command instead.

Command steps:

  1. Load and display string data to be modified.

  2. Run the command.

  3. Choose the **Radius for Filleting**.

  4. Select the line you wish to amend, for example:  
![](../Images/Fillet1.gif)  
  

  5. The line is modified (filleted) to create the necessary points in order to maintain the specified radial curvature. For example, the above line image, filleted to a radius of 30 creates this:  
![](../Images/Fillet2.gif)

Related topics and activities

  * [fillet-single-string-point](<fillet-single-string-point.md>)

  * [fillet-string-points-berm](<fillet-string-points-berm.md>)

  * [smooth-string ("sms")](<smooth-string.md>)

  * [insert-curve ("ics")](<insert-curve.md>)