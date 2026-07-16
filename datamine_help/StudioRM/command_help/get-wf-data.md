# get-wf-data ("gw")

See this command in the [**command table**.](<COMMAND%20TABLE_G.md#get-wf-data>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "get-wf-data"

  * Use the quick key combination "gw".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **get-wf-data** and click **Run**.

## Command Overview

Get data from supplied wireframe triangle and point files.

When this command is invoked you are prompted for wireframe triangle and point file names. The data in these files will then be added to the current wireframe data. A field called **FILENAME** exists in the current wireframe data, and contains the name of the original triangle file name from which that data originated. This may be used to filter the current wireframe data according to the original source file names. Newly created wireframe data will have a blank **FILENAME** entries.

Note that **FILENAME** is up to 24 characters long and is stored using the DATAMINE file convention ( **UPPERCASE** with an optional dot to delimit any suffix).

Note: The environment variable "WF_NAMING" may be used to specify the default naming convention for wireframe point files. See the information entry on wireframes for more details.

Related topics and activities

  * [get-drillholes](<get-drillholes.md>)

  * [get-points](<get-points.md>)

  * [get-view](<get-view.md>)

  * [get-all-strings ("ga")](<get-all-strings.md>)