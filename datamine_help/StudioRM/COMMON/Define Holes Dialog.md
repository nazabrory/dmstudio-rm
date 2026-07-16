# Define Hole Tables

To access this screen:

  * Sample Analysis ribbon Desurvey >> Dynamic

  * Using the **[command line](<Command_Toolbar.md>)** , enter "define-holes"

  * Display the **[Find Command](<findcommand.md>)** screen, locate **define-holes** and click **Run**.

Map loaded drillhole files to standard drillhole table types and fields. This information is used to create drillhole data objects.

As drillhole data files are imported into the project document, the new tables are automatically added to the hole tables definition, and, when sufficient survey data has been identified, the drillholes are desurveyed. 

So, whether you build the holes using the **[Data Load Wizard](<Data%20Load%20Wizard_Import%20Data%20Tables.md>)** or load and define each table individually using this screen, by the time all the tables have been imported the program will also have completed defining and building the drillholes.

Note: Data must be loaded before selection.

You can view and change the default drillhole definitions and rebuild the holes at any time.

The mapping of data (required fields for defining a drillhole to fields contained in a database table) simply 'links' external and required data. When the process is run, all fields in the selected table will be used to create the drillhole object(s), regardless of whether they are mapped (assigned to drillhole data fields) or not.

To correctly map component data tables to expected drillhole data types and values, complete the following sections:

  * Collars Select the table containing hole collar data.

  * Surveys Select the table containing downhole survey data.

  * Traces Optional; select the table containing hole trace data. If traces are desurveyed by the program, this table is created and assigned by the program.

  * Assays Optional; select the table containing sample assay data.

  * Lithology Select the table containing sample lithology data.

  * Intersections Optional; select the table containing drillhole intersection data. This may be an imported table, or created by the program.

  * Interval Logs Select the table containing hole interval data, e.g. rock mass rating data

  * Depth Logs Select the table containing hole depth data e.g. downhole geophysical survey data

You can also access the following functions:

  * Table Properties: display and edit field assignments for the selected table using the Define Drillhole Data Table screen. Note that this screen is displayed automatically when a new table is selected from any of the lists.

  * Rebuild: desurvey traces using the [Build Holes](<build%20holes%20dialog.md>) screen, after making changes to the hole definition.

  * Desurvey Method: select a desurveying method using the [Desurvey Method](<../PLOTS_LOGS/desurvey%20settings%20dialog.md>) screen.

  * Import Table: import an external data file using the appropriate Data Source Drivers via the [Data Import](<data%20import%20dialog.md>) screen.

  * Create Table: create a new empty table. Displays the [Select Table Type](<Select%20Table%20Type%20Dialog.md>) screen.

Related topics and activities

  * [Defining and Building Drillholes](<LoadingDynamicDrillholeData.md>)

  * [Working with Tables](<../PLOTS_LOGS/abouttables.md>)

  * [Creating an Intersections Table](<../PLOTS_LOGS/CreateIntersections.md>)

  * [ Importing and Exporting Data](<Concept_Importing%20and%20Exporting%20Data.md>)