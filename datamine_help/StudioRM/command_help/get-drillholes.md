# get-drillholes ("gd")

See this command in the [**command table**.](<COMMAND%20TABLE_G.md#get-drillholes>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "get-drillholes"

  * Use the quick key combination "gd".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **get-drillholes** and click **Run**.

## Command Overview

Read data from a drillhole file with optional Input filter.

Data from a nominated file is read into memory under the control of an optional Input filter. Multiple files may be read into memory by selecting this option for each file in turn. (Provided no fields conflict in type or length with current data in memory.)

The field 'FILENAME' is created automatically by the system, all records read for a given file will have the filename set appropriately. This is particularly useful when using filters. Note that FILENAME is up to 24 characters long and is stored using the DATAMINE file convention (UPPERCASE with an optional dot to delimit any suffix).

In addition, any non-standard attribute fields specified at startup time will also be added to the system data.

Related topics and activities

  * [get-all-strings ("ga")](<get-all-strings.md>)

  * [get-points](<get-points.md>)

  * [get-view](<get-view.md>)

  * [get-wf-data](<get-wf-data.md>)