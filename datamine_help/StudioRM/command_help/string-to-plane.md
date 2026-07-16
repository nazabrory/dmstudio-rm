# string-to-plane ("cstp")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#string-to-plane>)

To access this command:

  * **Digitize** ribbon **> > Tools >> String to Plane**.

  * Right-click a strings data overlay in the **Sheets** or **Project Data** control bar and select **Convert to Planes**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "string-to-plane".

  * Use the quick key combination "cstp".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **string-to-plane** and click **Run**.

## Command Overview

Create [plane](<../COMMON/Studio%203%20Planes%20Overview.md>) data based on the vertices of a selected string object. The original string data is not removed.

A plane object is fitted to the string data according to 'best fit' principles. 

  * If no plane object has yet been defined, a new planes object is created and made current.

  * A plane is represented by a disc or rectangle, depending on the current [Plane Properties](<../VR_Help/Planes%20Properties%20Dialog.md>).

A plane object is similar to a points object, but has a dip (**DIP**) and dip direction (**DIPDIRN**). Planes can be used for a range of reasons, including geotechnical structure orientation for fault domain analysis.

Command steps:

  1. Select the required string.

  2. Run the command.

A plane data object is created.

Related topics and activities

  * [Planes Overview](<../COMMON/Studio%203%20Planes%20Overview.md>)