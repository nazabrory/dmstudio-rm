# Build Holes

To access this screen:

  * Display the [Define Hole Tables](<Define%20Holes%20Dialog.md>) screen and click Rebuild....

  * **Sample Analysis** ribbon **> > Desurvey >> Dynamic >> Build Dynamic**. 

Define hole trace settings during the creation (or recreation) of dynamic or static drillholes. 

A collars and survey table (as a minimum) must be defined to build holes. See **[Define Holes](<Define%20Holes%20Dialog.md>)**.

When creating static drillholes via the Build Holes screen, a static holes overlay is added to all views (including Plots window views). For more information on how your application uses overlays to represent views of objects, see [View Hierarchy](<View%20Hierarchy.md>).

To build drillholes from specified component tables:

  1. Choose if a new trace is created for every drillhole defined within the supporting tables used to build the drillholes (as specified with the [Define Hole Tables](<Define%20Holes%20Dialog.md>) dialog): 

     * If **Create new traces for all holes** is **checked** , a new trace is created for every hole.

     * If Use existing traces and only desurvey new holes is **unchecked** , data is created for holes that are not currently represented as static (desurveyed) holes, preserving existing desurveyed data. You should select this option if you have:

       * Changed the table definitions and field assignments of assays, lithology and other log tables.

       * Imported new log tables.

  2. Decide if you want to generate static drillholes when building holes (see [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>)).

     * If **Create Static Drillholes** is **checked** , you will create static drillholes from the dynamic drillhole tables during the hole building process.

     * If **Create Static Drillholes** is **unchecked** , dynamic drillholes are created, based on component tables.

If you choose to create static data, the following options become available:

     1. Add samples for each survey point: if checked, add additional sample intervals at survey points

     2. Remove Dynamic Holes: remove the dynamic drillholes object from memory after the static drillholes object has been created.

Related topics and activities

  * [Define Hole Tables](<Define%20Holes%20Dialog.md>)

  * [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>)