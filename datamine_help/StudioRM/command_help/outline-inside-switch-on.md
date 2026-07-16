# outline-inside-switch-on

See this command in the [**command table**.](<COMMAND%20TABLE_O.md#outline-inside-switch-on>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "outline-batch-switch".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **outline-batch-switch** and click **Run**.

## Command Overview

Used by the [generate-outlines](<generate-outlines.md>) command to determine which boundary strings are to be considered 'internal'. This is particularly relevant where you need to control which outlines are nested within others.

Running this command will will add an **INSIDE** column when outlines are generated from the generate-outlines routine. Note that with this switch activated, and [outline-batch-switch](<outline-batch-switch.md>) set, a nested outline will produce 2 outlines: one is described in the resulting outlines file as **INSIDE** =1 to terminate the outer region, and **INSIDE** =0 to start the next region.

The **INSIDE** column is also supported by the [Divide Wireframe by Strings](<wf-divide-by-strings.md>) command to allow you to create voids in blocks, or to speed up the processing of outlines with only a small number of nested outlines.

Related topics and activities

  * [generate-outlines](<generate-outlines.md>)

  * outline-inside-switch-on

  * [outline-selection-switch ("tsin")](<outline-selection-switch.md>)

  * [outline-batch-switch](<outline-batch-switch.md>)
  * [wf-divide-by-strings](<wf-divide-by-strings.md>)

  * [outl-batch-switch ("trs")](<outl-batch-switch.md>)

  * [outl-deselect-outer ("dol")](<outl-deselect-outer.md>)

  * [outline-batch-switch ("trs")](<outline-batch-switch.md>)

  * [outline-storage-switch ("tsif")](<outline-storage-switch.md>)

  * [outl-limit-switch ("uo")](<outl-limit-switch.md>)

  * [outl-plane-switch ("ftp")](<outl-plane-switch.md>)

  * [outl-select-outer ("ool")](<outl-select-outer.md>)