# connect-strings ("conn")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#connect-strings>)

To access this command:

  * **Digitize** ribbon **> > Tools >> Connect**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "connect-strings"

  * Use the quick key combination "conn".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **connect-strings** and click **Run**.

## Command Overview

Connects two strings, from the selected end-point of the first to the selected end-point of the second. With this command, attributes from the first selected string are copied to the merged entity. 

If the two strings started as separate string objects, the second string is incorporated into the first string object and removed from the second.

**Note** : the "connected" string adopts the attributes of the first selected string. To preserve the original string attributes, use [connect-strings-attrib](<connect-strings-attrib.md>). 

Command steps:

  1. Run the command. If a string is already selected, you are prompted to "Select selected string at the required end", otherwise the prompt "Select first string at the required end" is displayed.

  2. You are asked to "Select other string at the required end". The two strings are joined between the selected end points.

  3. Complete the command by clicking **Done** , or double-clicking (or tapping) in a **3D** window.

Related topics and activities

  * [connect-strings-attrib](<connect-strings-attrib.md>)

  * [merge-string-segments](<merge-string-segments.md>)

  * [merge-string-segments-attrib](<merge-string-segments-attrib.md>)
  * [merge-strings-to-object](<merge-strings-to-object.md>)