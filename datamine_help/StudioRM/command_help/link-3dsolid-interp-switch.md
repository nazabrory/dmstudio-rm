# link-3dsolid-interp-switch

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-3dsolid-interp-switch>)

To access this command:

  * On the [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>) screen, toggle the **Uniform Interpolation** setting.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-3dsolid-interp-switch"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-3dsolid-interp-switch** and click **Run**.

## Description

Toggle the Uniform Interpolation option applied when using the 3D Solid wireframe linking method.

Uniform Interpolation applies a unit length parameterisation to the string segments between tag strings. That is, the vertices from one string are imprinted onto the other (vice versa) as if one cut each string, stretched both out to the same length, imprinted temporary vertices and formed connections; finally restoring the original string shapes. 

The wireframe is generated using both the temporary and original string vertices.

**Note** : the [link-3dsolid-method-switch](<link-3dsolid-method-switch.md>) for this command to be effective.

Related topics and activities

  * [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)
  * [link-multiple-strings ("lms")](<link-multiple-strings.md>)
  * [Link Multiple Strings](<../COMMON/3D%20Solid%20Dialog.md>)
  * [link-3dsolid-align-switch](<link-3dsolid-align-switch.md>)

  * [ link-3dsolid-collate-switch](<link-3dsolid-collate-switch.md>)

  * [ link-3dsolid-method-switch](<link-3dsolid-method-switch.md>)

  * [ link-3dsolid-view-plane-switch](<link-3dsolid-view-plane-switch.md>)