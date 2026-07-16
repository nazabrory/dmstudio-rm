# fillet-single-string-point ("ssp")

See this command in the [**command table**.](<COMMAND%20TABLE_F.md#fillet-single-string-point>)

To access this command:

  * **Digitize** ribbon **> > Condition >> Condition >> Fillet Single String Point**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "fillet-single-string-point"

  * Use the quick key combination "ssp".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **fillet-single-string-point** and click **Run**.

## Command Overview

Specify the maximum curvature radius permitted between line segments on points of a string. Points are added to the line where appropriate to maintain the maximum radial curvature. 

This command reports the following string conditions when encountered:

  * Attempting to create a string such that there is an angle of 0 degrees between the points.

Resulting Error "The selected point has an angle of 0 degrees so cannot be filleted. Please select a different point."

  * Attempting to create a string such that there is an angle of 180 degrees between the points.

Resulting Error The selected point has an angle of 180 degrees so cannot be filleted. Please select a different point."

  * Attempting to create a string with a large angle and make the radius extremely small.

Resulting Error "The selected point cannot be filleted with a radius X because this radius is too small compared to the point angle and no points would be added. Please select a different point."

**Note** : This command is used to modify selected points on a line - to fillet all points on a selected line, use the [fillet-string-points](<fillet-string-points.md>) command.

**Note** : Your string data can be on any plane. Filleting is performed using the mean plane of the selected string.

Command steps

  1. Ensure at least one string is loaded and in view in a **3D** window.

  2. Run the command.

  3. Specify a **Radius for Filleting**.

  4. Select a point on a line to modify.

The 'corner' created by the convergence of the line segments at that point is modified according to the radial curvature specified.

Related topics and activities

  * [fillet-string-points ("spf")](<fillet-string-points.md>)

  * [fillet-string-points-berm](<fillet-string-points-berm.md>)

  * [smooth-string ("sms")](<smooth-string.md>)

  * [insert-curve ("ics")](<insert-curve.md>)