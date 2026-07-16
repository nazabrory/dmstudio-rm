# Data Refresh

To access this screen:

  * Right-click the top-level project icon in the Loaded Data control bar and select Refresh.

  * Activate the Data ribbon and select Load >> Refresh (top level icon).

  * In the **Sheets** or **Project Data** control bar, right-click an overlay and select **Data >> Refresh**.

## Refreshing vs. Reloading Data

How refreshing and reloading affects your loaded data depends on how the original data was loaded.

If data was loaded using one of Datamine's Data Source Drivers, including Datamine files:

  * **Refreshing** data renews the selected data object using whatever load settings were used to originally load it. For example, if you had loaded a Datamine points file whilst holding the <CTRL> key and filtered one or more columns, the **Refresh** command repeats the same action when bringing the data back into your application.

If no load options were set originally, the file is refreshed in its entirety.

  * **Reloading** data also renews the current in-memory object based on the current state of the physical file on disk, but in this case any previous load options such as filtering or formula application are reset and you are given the chance to set new load options using the appropriate screen for the selected driver.

In summary: refreshing reuses previous data load instructions (without prompts) and reloading asks you to define them again.

In the case of drag-and-drop loading, where default load options are set (no screens are displayed), **Refresh** and **Reload** result in the same outcome (data in memory is renewed without further prompts or load options).

To refresh loaded data:

  1. Display the **Data Refresh** screen.

  2. Select one or more objects from the **Select objects to refresh** list. You can use keyboard modifiers **SHIFT** and **CTRL** to select multiple items.

**Tip** : click **Select All** or **Select None** to perform a global selection or deselection of items.

  3. Click **OK**.

The selected data items are refreshed. Data is renewed based on your previous data loading instructions.

Related topics and activities

  * [Data Reload](<Data%20Reload%20Dialog.md>)

  * [Data Unload](<Data%20Unload%20Dialog.md>)