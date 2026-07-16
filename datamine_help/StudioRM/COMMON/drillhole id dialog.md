# String to Drillhole

To access this screen:

  * Run the [string-to-drillhole](<../command_help/string-to-drillhole.md>) command.

Assign a unique borehole ID (BHID) to a string as part of the **string-to-drillhole** command.

The selected string is used to generate a drillhole trace in memory. Points on the string will determine sample start and end positions.

For single string selections (either selected before or after the command is executed), you can choose which of the attributes within the selected string will act as the borehole identifier Column (for example, **BHID** , but can be any alphanumeric data column). 

Once selected, the current value for the chosen string is displayed in the Value for BHID field. The resulting drillhole file will contain a **BHID** attribute with the displayed value, which can also be edited before you commit to the transformation.

This command works with pre-selection:

  * If a single string is selected before or after the command is run, the Strings to Drillholes screen is displayed automatically, and will contain enabled Column and Value for BHID fields. This allows you to select any attribute from the original string and any value to be used as the unique borehole identification (**BHID**) in the resulting drillhole file.
  * If multiple strings are selected before the command is run (you can only select one afterwards), the assumption is made that there is already an attribute within each string entity that defines the borehole identification value for that entity. As such, only the Column field is accessible: select the attribute that uniquely identifies the resulting borehole from the drop-down list. Click **OK** to convert all selected strings to drillholes.

Related topics and activities

  * [string-to-drillhole ("stdh")](<../command_help/string-to-drillhole.md>)

  * [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>)

  * [Define Drillhole Data Table](<define_drillhole_data.md>)

  * [Define Hole Tables](<Define%20Holes%20Dialog.md>)