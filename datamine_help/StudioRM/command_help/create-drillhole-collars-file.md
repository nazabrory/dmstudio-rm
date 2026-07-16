# create-drillhole-collars-file ("cdhf")

See this command in the [**command table**](<_COMMAND%20TABLE_C.md#create-drillhole-collars-file>).

To access this command: 

  * **Sample Analysis** ribbon **> > Plan >> Create Collars**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "create-drillhole-collars-file"

  * Use the quick key combination "cdhf".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **create-drillhole-collars-file** and click **Run**.

## Command Overview

Creates a drillhole collars table object from the current drillholes object. Drillhole data must be loaded for this command to run.

The collars table will contain the fields: **BHID** , **HLABEL** , **XCOLLAR** , **YCOLLAR** , **ZCOLLAR** , **NSAMPLES** , **LENGTH** , **MINSLENG** , **MAXSLENG** , **XEOH** , **YEOH** , **ZEOH** , **AVGDIP** , **AVGAZI**.

**Note** : This data is created as a table in memory so it must be saved or exported in order to create a file

Command steps:

  1. Load static drillhole data.

  2. Run the command.

  3. On the Create Collars Table screen, define a Collars Table Name (the default is 'collars_DrillholeObjectName').

  4. Click OK.

A collars table is created from the loaded drillhole data object.