# fit-elevation ("fe")

See this command in the [**command table**.](<COMMAND%20TABLE_F.md#fit-elevation>)

To access this command:

  * **Digitize** ribbon **> > Condition >> Condition >> Fit Elevation**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "fit-elevation"

  * Use the quick key combination "fe".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **fit-elevation** and click **Run**.

## Command Overview

Fit string data to a specific elevation.

A typical string of this type is that digitised from an underground level plan where the X and Y data is correct, but the elevations have been set to some arbitrary elevation, for example.

All the other strings currently resident in memory, and displayed according to any filters, are used as reference survey data. Typically, these are strings formed by connecting up points with fully surveyed three-dimensional coordinates. A new string is generated, formed by interpolating the elevation of the survey strings onto the original drive outline string.

Related topics and activities

  * [set-gradient-convention](<set-gradient-convention.md>)

  * [connection-on-grade ("cog")](<connection-on-grade.md>)

  * [adjust-to-gradient ("atg")](<adjust-to-gradient.md>)