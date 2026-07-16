# edit-coincident-points-switch ("ecp")

See this command in the [command table.](<COMMAND%20TABLE_E.md#edit-coincident-points-switch>)

To access this command:

  * Home ribbon >> Edit >> Move Points >> Coincident Points.
  * **Digitize** ribbon **> > Edit Modes >> Coincident Points**.
  * Using the Project Settings screen >> [Points and Strings](<../COMMON/Project%20Settings_Points%20and%20Strings.md>) tab, select **Edit coincident points**.

  * Enter "edit-point-coordinate" into the Command toolbar and press <ENTER>.
  * Use the quick key combination "epc".

## Command Overview

This command assists with editing of strings / wireframes when particular string / wireframe points need to remain connected or when strings / wireframes are required to remain adjacent, e.g., a set of dig outlines on a mining bench or adjacent wireframe triangles of a DTM surface.

Toggles the switch which enables coincident points on strings or wireframes to be moved at the same time when using [**move-points-mode**](<move-points-mode.md>) or [move-wireframe-point](<move-wireframe-point.md>) respectively; enables points to be inserted simultaneously on multiple segments of different strings if they are coincident, when using the [insert-points-mode](<insert-points-mode.md>) command.

**Tip** : Verifying a wireframe will ensure that any duplicate points are removed).

Command Steps:

  1. Launch the edit-coincident-points-switch command.

The command state alternates between ON and OFF. 

     * If **ON** \- selecting and moving string/wireframe points also moves any coincident string/wireframe points.
     * If **OFF** \- selecting and moving string/wireframe points will not move any coincident string/wireframe points.

  
Related Topics and Activities

  * [move-points-mode](<move-points-mode.md>)
  * [ insert-points-mode](<insert-points-mode.md>)
  * [ move-wireframe-point](<move-wireframe-point.md>)