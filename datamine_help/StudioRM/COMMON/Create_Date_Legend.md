# Create Date Legend

### To access this dialog: 

  * Format ribbon >> Overlays >> Date Legend.

  * Use the quick-key combination 'cdl'.

  * Enter create-date-legend into the command line.

Generate legends based on date values, such as those created by Datamine's [Datamine Task Scheduler](<V14_CONCEPT_EPS_Overview.md>) (DTS) application. Build up a series of date ranges, which can either be the same or different in terms of duration and frequency. 

One application could be to generate a date legend based on the periods of the currently loaded DTS schedule, or you can generate one manually using simple time and duration increments. You have full control over colour cycling and recurrence of the category within the legend (if required).

A date legend applied to a series of mining blocks in the 3D view

You can create either a project or user legend, which is then selectable in any legend selection drop-down control in your application (e.g. to colour according to the chronology of an operational scheduling sequence. 

There are several ways of generating legends in Studio products:

  * You can define any type of legend using the [Legends Manager](<FormatLegendsDialog.md>).
  * You can create date-based legends using the Create Date Legend dialog.
  * You can quickly create a visualization legend using the [Quick Legend](<Quick_Legend_Dialog.md>) tool.
  * You can generate a filter legend based on one or more attributes values, using the [Multiple Attribute](<MultipleAttributeLegend.md>) Legend tool.
  * Several commands and functions within Studio will automatically create (and possibly assign) legends.

To generate a custom date legend:

  1. Display the Create Date Legend screen.
  2. Enter the **Legend Name** you wish to assign to your date legend, or select an existing date legend to update.

  3. Choose your **Storage** option: either a _Project_ or as a _User_ legend.

**Note** : a user legend is transferable between projects.

  4. Select the Custom radio button and use the date picker to select the date of the earliest legend bin.

  5. The desired bin labelling format is the one used by the current operating system (the locale). This is chosen using the _%x_ option.

  6. In the intervals table below, click "+" to add a new row to the table.

  7. Define the **Duration** , time unit and **Increment** for the legend bin. For example, if the first set of bins represents 3 months of weekly intervals: Duration = 3, the time unit is _Months_ and the Increment is _Weeks_ :  
  

  8. Click "+" again for the next legend generation instruction. Continuing the example above, add monthly intervals for 9 months with the following settings:  
  

  9. Continue to add rows, where a new row is required wherever the time unit or Increment changes. For example, you could add a third row representing the 2nd year in quarters:  
  

  10. Define the **From** and **To** colours for each of the instructions and the type of transition for each instruction. For example, you could change the From and To values for the second row of the example above to cycle from blue to white, and the third row could be set as random colours:  
  

  11. Choose how the legend bin colours **Transition** **From** one colour **To** the other. 

The _Clockwise_ and _Anticlockwise_ options determine if colours progress in a From-To direction or To-From. Alternatively, pick _Random_ colouring for each interval of the range.

  12. By default, a colour cycle is applied across all values in the date legend, but you can set up a **Recurring** pattern if you wish (say, to highlight days of the week). 

For example, in the image below, the left image shows the start of default non-recurring colouring across all date periods (the cycle is actually from red to green but the later bins are obscured). On the right, the same **Transition** , **From** and **To** settings are selected, but **Recurring** is **checked** with an **Every** value of 4, meaning the colour cycle repeats every four periods:

  13. Click OK to generate the legend.

  14. Open the Legends Manager and expand either the **User Legends** or **Project Legends** category (**Available Legends** list).

  15. Locate the new legend and expand it to review the new legend date intervals. Following the example above, you would see 12 weekly intervals transitioning from red to green, followed by 9 monthly intervals cycling from blue to white, followed by four intervals representing quarters, randomly coloured:  
  

Related topics and activities

  * [Legends Manager](<FormatLegendsDialog.md>)