# Data Export

To access this screen:

  * **Data** ribbon **> > Export >> External**.

  * In the [Data Object Manager](<Data%20Manager%20Dialog.md>), select an item from the Loaded Objects list and click Export Object.

  * Right-click an object in the Loaded Data control bar and select Data >> Export.

Convert loaded data into external files of a specific format. 

Files are written according to the specified category of data they belong to, and the type of data within that category. This combination of properties determines which routines are used to create the resulting files. The technology behind all this is called "Data Source Drivers" and each driver is responsible for creating file(s) of a specific type. 

Note: Some drivers are created by Datamine - these are the ones we can fully support, whilst others are provided in collaboration with other mining software vendors. In the latter case, we will always attempt to support your data transfer scenarios, but may not be able to do so if the 3rd party driver doesn't do so by default.

Activity steps

  1. Select a **Driver Category**. This is the general format you want to create. For example, to create a .dxf file, select _CAD_.

  2. Select a Data Type. 

Note: Each category supports its own data types. For example, you can export anything via the Text driver, but the Surpac driver only supports block models and strings.

  3. Click **OK** to either export data or continue with driver-specific screens to configure your output for a particular format.

Tip: Click **Driver Help** for more information on the currently selected driver.

Related topics and activities

  * [Data Types](<Data.md>)

  * [Export to Google Earth](<ExportDataGoogleEarth_Concept.md>)

  * [Data Object Manager](<Data%20Manager%20Dialog.md>)

  * [Data Import](<data%20import%20dialog.md>)

  * [Data Unload](<Data%20Unload%20Dialog.md>)