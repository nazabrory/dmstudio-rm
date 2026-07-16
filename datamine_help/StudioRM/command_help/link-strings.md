# link-strings ("ls")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-strings>)

To access this command:

  * **Explicit** ribbon **> > Create >> Link**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-strings"

  * Use the quick key combination "ls".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-strings** and click **Run**.

## Description

Creates a wireframe link between two perimeters (closed strings) or two strings. If using **tag strings** , they cannot be linked.

  * Use the [link-to-line](<link-to-line.md>) command to link a string to a perimeter.
  * The links take their color from the first string of each string-pair used for the linking.
  * Various settings can be used to control linking, see [Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>).
  * Tag strings can be used to control linking, see [use-tag-switch](<use-tag-switch.md>).

Note: This command uses the **Maximum Segment Length** value (if greater than zero), as specified in **[Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)** to limit the generated segment length of generated wireframe triangles.

Command steps:

  1. Load or digitize any tag strings you wish to use to control the linking of strings. See **[Wireframe Tag Strings](<../COMMON/Wireframe_Tag_Strings.md>)**.

  2. To restrict string linking to a subset of loaded and visible string data, select it in any 3D window so that it is highlighted.

  3. In the [Current Objects](<../COMMON/Current_Objects_Toolbar.md>) toolbar, select or create a new current wireframe object. Alternatively, if no current wireframe object exists, a new one is created automatically.

  4. Run the command.

  5. Following the prompts in the Status Bar, select a point on the first string perimeter.

**Note** : If string data was preselected, you will only be able to choose a string that is selected.

  6. Select a point on the second string or perimeter. A wireframe surface is generated between the two strings.

**Note** : If string data was preselected, you will only be able to choose a string that is selected.

  7. Repeat step 3 until all required strings and perimeters have been linked in sequence.

  8. Click Cancel.

Related topics and activities

  * [use-tag-switch](<use-tag-switch.md>)

  * [Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)

  * [Wireframe Tag Strings](<../COMMON/Wireframe_Tag_Strings.md>)

  * [end-link ("eli")](<end-link.md>)

  * [end-link-boundary ("elb")](<end-link-boundary.md>)

  * [Current Objects Toolbar](<../COMMON/Current_Objects_Toolbar.md>)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|    
[open-string](<open-string.md>)[  
open-all-strings](<open-all-strings.md>)