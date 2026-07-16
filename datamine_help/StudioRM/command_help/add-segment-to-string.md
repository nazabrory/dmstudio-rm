# add-segment-to-string ("ass")

See this command in the [**command table**.](<_COMMAND%20TABLE_A.md#add-segment-to-string>)

To access this command:

  * Digitize ribbon >> Design >> Tools >> Extend.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter `add-segment-to-string`.

  * Use the quick key combination "ass".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate _add-segment-to-string_ and click **Run**.

## Command Overview

Select a string and add a segment to it.

If strings are preselected, data picking is restricted to selected string data only. You can apply one or multiple edits to a string within the same command session.

**Tip** : This command can be completed by double-clicking (or tapping) anywhere in a 3D window.

Command Steps:

  1. Run the command. 

  2. Select the string and the end to be extended.

  3. The Add Segment to String screen appears.   
  
The current world azimuth of the string segment closest to the pick position is calculated automatically and displayed as Segment Azimuth. You can either continue to extend the string at this azimuth or choose your own value (0-360 degrees).  
  
You can also specify a _relative_ azimuth change, say + 10 degrees, using the "+" field, which accepts both positive and negative values.  
  
You can also define a Segment Gradient.

  4. Define the distance and method by which you want to extend the selected string:

    * Horizontal Distance   
Input the distance, from the current terminal string vertex for the string to be extended on a flat / horizontal plane and at the given azimuth / gradient values. This must be a positive value. 

    * Vertical Distance   
Set a vertical distance change from the current terminal string vertex, for the string to be extended in a vertical direction at the given azimuth / gradient values. This must be a positive value.

    * Slope Distance   
Specify an inclined length. Enter the length of the new segment here, to be created at the defined azimuth and gradient. This must be a positive value.

    * To Elevation   
Extend to a target elevation. The new string segment is created at the given gradient and azimuth, extending until the target elevation is reached. This can be a negative or positive number.  
  
Once a distance method has been selected and edited, press <ENTER> to automatically calculate other field values.

  6. Click OK to apply the extension edit to the selected string.   
  
If required, restart from step 4 for multiple edits.

**Tip** : Whilst azimuth values of the terminal string edge are automatically calculated and displayed when **Add Segment to String** is opened, the extension settings are whatever values were used for the previous extension in the current project session.  
  
This means you can quickly adjust the string repeatedly , or make minor adjustments, to alter the **Horizontal Distance** change whilst maintaining the same **Vertical Distance** , **Slope Distance** , and **Target Elevation** values as the previous edit.