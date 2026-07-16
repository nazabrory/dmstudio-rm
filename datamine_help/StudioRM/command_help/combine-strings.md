# combine-strings ("com")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#combine-strings>)

To access this command:

  * **Digitize** ribbon **> > Tools >> Combine**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "combine-strings".

  * Use the quick key combination "com".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **combine-strings** and click **Run**.

## Command Overview

Generates a single string from two overlapping strings. The attributes of the first string are copied to the second string. To control how attributes of the combined strings are managed in the resulting combined object, use [combine-strings-attrib](<combine-strings-attrib.md>).

This differs from the **[combine-strings-attrib](<combine-strings-attrib.md>)** command as this combines data whilst maintaining the attributes of the original strings.

This command is used in conjunction with the [keep-combined-switch](<keep-combined-switch.md>) mode which dictates whether the original string data is kept when strings are combined. 

**Note** : the overlapping strings do not need to be perimeters i.e. closed strings.

Consider the following example, where **combine-strings** is used to generate inner and outer boundaries:  

Original string arrangements:

![](../Images/CombineStrings1.gif)

There are four possible outcomes:

![](../Images/CombineStrings2.gif)

![](../Images/CombineStrings3.gif)

![](../Images/CombineStrings4.gif)

![](../Images/CombineStrings5.gif)

Command steps:

  1. Run the command.

  2. Select the portion of the first string which is to be included in the combination.

  3. Select the portion of the second string which is to be combined with the first portion.

  4. Click Cancel to close the command.

Related topics and activities

  * [combine-strings-attrib](<combine-strings-attrib.md>)