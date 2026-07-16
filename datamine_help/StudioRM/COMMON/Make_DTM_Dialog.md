# Make DTM

To access this wizard:

  * **Explicit** ribbon **> > DTM >> Make**.

  * Run the [dtm-create](<../command_help/dtm-create.md>) command.

  * Quick key 'md'

The Make DTM wizard is used to create a digital terrain model from loaded string or points data.

A digital terrain model is an open wireframe mesh, normally used to intimate the presence of a topographical surface, although it is also used to denote fault planes or any other planar geological domain. To use this command, at least one string object must exist in memory.

Models can be created with full control over how string attributes are used to define the resulting wireframe attributes. Facilities exist to allow wireframe triangle visual attributes to be derived from both design strings and (if specified) boundary strings.

**Note** : DTM setting defaults are set at the project level, using the [Project Settings](<Project%20Settings_DTM.md>) screen. The screen layout and function is identical to the General Options screen (see below), with the exception of the output object destination, which is absent.

The wizard displays the following screens in sequence.

  1. General Options Define the initial setup for the DTM calculation. 

See [Make DTM: General Options](<Make_DTM_General.md>).

  2. Select DTM Points and Strings Select which point and string object(s) will be used to define the resulting terrain model.

See [Make DTM: Select DTM Points and Strings](<Make_DTM_Points_Strings.md>).

  3. Select Boundary Strings If perimeter strings are to be used to trim the DTM object being created, and providing the object being used to create the base DTM is a string, these are specified here. 

[Make DTM: Select Boundary Strings](<Make_DTM_Boundary.md>).

  4. If the option to use User-defined attributes is selected in the General Options screen, the [Edit Attributes](<edit%20attributes%20pick%20dialog.md>) screen is displayed.

See [Make DTM: Edit Attributes](<Make_DTM_Attributes.md>).

## DTM Considerations

The process of making a digital terrain model from loaded string data hinges on the following criteria:

  * Which string object(s) will be used to create the resulting mesh?

    * If using multiple objects, maybe you could combine them first? This can improve performance, particularly if using the **Make diagonals consistent** option.

  * How will string points be linked during DTM creation?

  * Will data be cleaned/trimmed?

  * How will string attributes be proliferated?

  * Will boundary strings be used to define a periphery?

  * Are you using points or strings to create a DTM?