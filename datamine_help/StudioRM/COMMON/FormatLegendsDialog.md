# Legends Manager

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The Legends Manager screen provides various tools for creating, editing and managing legends.

The screen is split into two halves:

  * The left side shows the **Available Legends** in one of three categories (System, User and project). Expand a category and pick a legend to update the list below. 

  * The **Selected legend** list displays the intervals of the legend selected above. Selecting a legend displays (or updates) the Legend Properties panel on the right. Below this list, you'll find the following functions:

    * **New Legend...** opens the Create New Legend wizard which provides a simple method to create a new legend, and set its data type and file location.

    * Load Legend... opens a file browser allowing you to select a Datamine legend file (.elg). When loaded, it will be available for editing in the Available Legends list.

    * Show Details and **Hide Details** allows the properties panel on the right to be expanded or collapsed.

    * Apply applies the current settings and selections to the selected legend or legend item, and redraws any displayed sheets. The screen remains open for further editing.

    * Close applies the current settings and selections to the selected legend or legend item, and closes the screen.

Once a legend has been selected, the **Legend Properties** panel displays the following functions:

  * **Legend Properties** enter a **Name** , **Interval Type** (_Value_ , _Range_ or _Filter Expression_) and a **Data Type** (_Numeric_ or _Alphanumeric_).

  * **Legend Item Description** choose to **Automatically generate description** (or enter your own interval description) and define the **Value** of the interval.

  * **Legend Item Format** define the visual appearance of object data assigned to the legend interval. 

  * **Preview Legend** show a popup window displaying all intervals of the current legend and their respective visual formatting.

**Note** : these options are explained in more detail in your **Legends Manager** context help. Display the **Legends Manager** and press F1 to see it.

There are several ways of generating legends in Studio products:

  * You can define any type of legend using the Legends Manager.
  * You can create date-based legends using the [Create Date Legend](<Create_Date_Legend.md>) dialog.
  * You can quickly create a visualization legend using the [Quick Legend](<Quick_Legend_Dialog.md>) tool.
  * You can generate a filter legend based on one or more attributes values, using the [Multiple Attribute](<MultipleAttributeLegend.md>) Legend tool.
  * Several commands and functions within Studio will automatically create (and possibly assign) legends.