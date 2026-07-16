# pick-inner-limit

See this command in the [**command table**](<COMMAND%20TABLE_P.md#pick-inner-limit>).

To access this command:

  *   * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "pick-inner-limit"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **pick-inner-limit** and click **Run**.

## Command Overview

Select a string that is to define an inner limit (hole) of the DTM.  

The string must be closed. When the string is selected it is displayed in the colour green to indicate it is an inner limit string. The string can represent a two dimensional outline of the required DTM or it can contain points that are required to make up part of the DTM. If the string represents a two dimensional outline then only the X and Y coordinates of its points are considered.

The toggle command dtm-limit-include-switch controls whether the limit strings should themselves be included in the DTM when the command [dtm-create](<dtm-create.md>) is invoked. More than one inner limit string may be selected. If inner limit string(s) are being used an [outer limit string](<pick-outer-limit.md>) must also be selected.

Note: Limit strings must be based on at least one object being selected for inclusion in DTM creation. If a limit string exists for an object that is not selected in the **Objects** list for this screen, it is ignored.

Related topics and activities

  * [pick-outer-limit](<pick-outer-limit.md>)

  * [make-dtm-from-objects](<make-dtm-from-objects.md>)