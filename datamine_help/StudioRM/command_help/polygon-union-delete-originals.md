# polygon-union-delete-originals

See this command in the [**command table**.](<COMMAND%20TABLE_P.md#polygon-union-delete-originals>)

To access this command:

  * **Digitize** ribbon >> **Tools >> Combine >> Polygon Union Unique**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "polygon-union-delete-originals".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **polygon-union-delete-originals** and click **Run**.

## Command Overview

Create a unified perimeter based on other loaded closed strings. How this command operates depends on the relative arrangement of the target strings, erasing the original string data.

  * If overlapping polygons are selected in any 3D window, this command creates a new polygon which contains the area inside all of them.
  * If separate polygons are selected in any 3D window, this command creates an identical polygon for each selected item.

**Note** : A variation of this command - [polygon-union ("plyu")](<polygon-union.md>) \- retains the original polygon string data.

Related topics and activities

  * [polygon-union ("plyu")](<polygon-union.md>)

  * [new-polygon](<new-polygon.md>)

  * [polygon-intersection](<polygon-intersection.md>)