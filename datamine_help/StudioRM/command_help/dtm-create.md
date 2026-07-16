# dtm-create ("md")

See this command in the [**command table**.](<COMMAND%20TABLE_D.md#dtm-create>)

To access this command:

  * **Explicit** ribbon **> > DTM >> Make**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "dtm-create"

  * Use the quick key combination "md".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **dtm-create** and click **Run**.

## Command Overview

Generate a digital terrain model (DTM) wireframe from a series of strings. This command has the following capabilities:

  * Choice of full object input and/or individual strings and points

  * Ability to create dtm attributes from input data attributes

  * Optional creation of spur strings to avoid plateaus on ridges and valleys

  * Optional automatic best-fit DTM plane in addition to world and view plane options

  * Automatic nesting of boundary limit strings

#### Boundary Strings

Care should be exercised when creating a DTM using view coordinates rather than world (XY) coordinates. 

For example, if the plan view is in use, but the view direction is set to a significantly different orientation, unexpected results can occur. For this reason, if you have configured a view direction with this type of deviation from the world plane, particular care should be taken in the definition of inner/outer limit strings.

### Make Diagonals Consistent

You can form a DTM from one or more input string or points objects (or a combination). However, where point data is common between multiple objects (meaning there are coincident data points in the set used to form the DTM), it is possible for surface triangulation to be performed in a different way, and often unexpectedly so, compared to the outcome if data were sourced from a single object (without coincident points). 

To mitigate this possibility, the Make Diagonals Consistent option can be checked to ensure the surface generated between disparate data sets is performed identically, ensuring the combined DTM matches the triangulated output from a single data object input.

Note: Selecting this option can introduce a performance hit, so where large coincident data overlaps are known to occur between input objects, it may be more efficient to combine data first into a single object (say, using the [Copy from Object(s)](<../COMMON/CopyDataFromDialog.md>) screen) before generating a DTM.

For more detailed information on this command and its associated wizard, see [Make DTM](<../COMMON/Make_DTM_Dialog.md>).

Command steps:

  1. Run the command.

The [Make DTM](<../COMMON/Make_DTM_Dialog.md>) wizard displays. 

  2. Fill in the required settings and click Next to proceed to next stage of the wizard. For more information on individual settings, see [Make DTM](<../COMMON/Make_DTM_Dialog.md>).

  3. Select the points and strings to be used to create the digital terrain model. 

Click Next.

  4. Select boundary strings (if required) from the displayed list of objects. All loaded string objects are listed.

**Note** : if an open string is selected, it is automatically closed (temporarily) to form a boundary.

Click Next. 

A new DTM (wireframe) object is created and displayed in the primary **3D** window.

  5. Click Finish.

Related topics and activities

  * [Make DTM](<../COMMON/Make_DTM_Dialog.md>)

  * [dtm-new-point-separation ("nps")](<dtm-new-point-separation.md>)

  * [dtm-undo-last-link ("uld")](<dtm-undo-last-link.md>)