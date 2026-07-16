# dtm-new-point-separation ("nps")

See this command in the [**command table**.](<COMMAND%20TABLE_D.md#dtm-new-point-separation>)

To access this command:

  * **Explicit** ribbon **> > Create >> Point Separation**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "dtm-new-point-separation"

  * Use the quick key combination "nps".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **dtm-new-point-separation** and click **Run**.

## Command Overview

Ensure that a maximum string edge length is not exceeded before triangulation takes place when linking strings, such as with the [link-strings](<link-strings.md>) command.

  * If set to zero, default triangulation occurs without constraint, permitting triangle edges of any potential size during triangulation. The target is to generate a wireframe with the minimum number of triangles.

  * If set to a value above zero, triangles within the generated wireframe will not have an edge greater thant the maximum length.

Higher values will permit the generation triangles with longer edges.

Regardless of the specified separation distance, the current **Linking Method** and **String Linking Control** settings (as specified in [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)) are honoured.

**Note** : Adjusting the point separation via the **dtm-new-point-separation** command also updates the **Maximum Segment Length** value on the **Project Settings** screen (**Wireframe Linking** tab). See [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>).

Command Steps:

  1. Run the command.

The **Maximum Point Separation** screen displays.

  2. Enter the **Maximum distance between additional points**. This is the maximum distance between wireframe vertices in surface or volume data generated from string linking commands, including end-linking and DTM creation.

Related topics and activities

  * [Maximum Point Separation](<../COMMON/wireframe%20maximum%20separation%20dialog.md>) (screen)

  * [link-strings](<link-strings.md>)

  * [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)