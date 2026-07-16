# define-new-rosette

See this command in the [**command table**.](<COMMAND%20TABLE_D.md#define-new-rosette>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "define-new-rosette"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **define-new-rosette** and click **Run**.

## Command Overview

Define new rosette (projection angles by azimuth ranges).

Each new rosette is stored in the current rosette file. If a current rosette file is not open when the command is invoked then you are prompted to select one. If you specify a file that does not exist, it is created. 

The rosette values can be used when projecting strings with the project string commands within your application. If a rosette is available it overrides the default face angle. If a cell model file is open and contains a SLOPE field and the use of the SLOPE field is turned on this takes priority over the rosette and default face angle.

Command steps:

  1. You are asked to select with the cursor a location for the new rosette. 

When the location has been selected it is marked on the screen. 

Note: The current view plane orientation must be in plan, (zero dip), to select this location. 

  2. Enter a minimum and maximum Z value to define the range of influence of this rosette. 

  3. Define a series of azimuth ranges together with a value for the face angle and berm width for each of these ranges.