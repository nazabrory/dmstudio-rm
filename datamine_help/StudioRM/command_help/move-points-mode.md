# move-points-mode ("mpo")

See this command in the [**command table**.](<COMMAND%20TABLE_M.md#move-points-mode>)

To access this command:

  * **Home** ribbon **> > Edit >> Move Points**.

  * **Explicit** ribbon **> > Design >> Move Points**.

  * **Digitize** ribbon **> > Edit >> Move Points**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "move-points-mode"

  * Use the quick key combination "mpo".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **move-points-mode** and click **Run**.

## Command Overview

Interactively move points and string points in any 3D window.

A point or string can be selected before this command is run. In this case, only selected data be moved.

There are 3 possible ways that this type of editing can be performed:

  * Data can be edited relative to the screen (that is, around a plane that is orthogonal to the current camera view). This behaviour is performed if the project setting Move relative to screen is checked. See [Project Settings: Points and Strings](<../COMMON/Project%20Settings_Points%20and%20Strings.md>).

  * Data can be edited relative to the current data plane. This type of editing allows the planar alignment of data to be maintained regardless of the position and direction of the 3D 'camera'. The bounding box aligns with the plane of rotation/point movement. This behaviour is performed if the project setting Move relative to plane is enabled. See [Project Settings: Points and Strings](<../COMMON/Project%20Settings_Points%20and%20Strings.md>).

  * Data can be edited using a locked view. In this case, the camera is always orthogonal to the view. See [Section Locking](<../COMMON/Section_Locking.md>).

### Movement Options

There are two ways to move points:

#### Click-Click

With this method, left click (or tap) once to select a point and click again to reposition it. 

#### Click-Drag

Click (or tap) and drag a point to a new position.

In either mode, snapping is supported.

## How to Use

  1. Run the command.

  2. Select a point to be moved.

  3. Place the point(s) at the new location(s).

  4. Click Done.

Related topics and activities

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [new-points](<new-points.md>)[  
new-string](<new-string.md>)