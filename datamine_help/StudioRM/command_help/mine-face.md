# mine-face ("msp")

See this command in the [**command table**.](<COMMAND%20TABLE_M.md#mine-face>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "mine-face".

  * Use the quick key combination "msp".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **mine-face** and click **Run**.

## Command Overview

Mine face or tonnage zone.

You are asked to select an active face or tonnage zone. If the selected perimeter segment is not a face or tonnage zone, a warning message is displayed.

If you have selected an active face, you are prompted for an advance rate. This supplied rate is used with the number of time units in the current period to determine the total face advance distance. The face is then advanced, creating two new perimeters: one being mined, the other the unmined remnant.

If there is more than one time unit in the current scheduling period, you can step through the period, using different production rates over different elapsed times. The default response is always to progress right through the remainder of the current period at the supplied rate.

### Mining Tonnage Zones

If you selected a tonnage zone, you are prompted for the extraction tonnage. This tonnage is then placed in the current results file with the current TIMENO.

Related topics and activities

  * [mine-tonnes-target](<mine-tonnes-target.md>)