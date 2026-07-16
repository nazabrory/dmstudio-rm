# set-tolerance ("sto")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-tolerance>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-tolerance"

  * Use the quick key combination "sto".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **set-tolerance** and click **Run**.

  * **Project Settings** screen >> **Wireframes >> Tolerance**.

## Command Overview

Set matching tolerance for points to be used in the generation of a Digital Terrain Model (DTM). 

Note: For DTM formation no triangles is created with sides of length less than this tolerance.

Note: For the [wireframe-verify](<wireframe-verify.md>) command points within this tolerance are considered duplicate for the purposes of verification. Any triangles that are degenerate after this point merging are discarded.

Related topics and activities:

  * [dtm-create ("md")](<dtm-create.md>)

  * [Project Settings: Wireframing](<../COMMON/Project%20Settings_Wireframing.md>)