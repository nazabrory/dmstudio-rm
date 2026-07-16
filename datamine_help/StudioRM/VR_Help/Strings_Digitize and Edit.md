# Create Alignment Strings

Alignment strings (strings used to align mobile [VR objects](<sheets_vrobjects.md>) in a simulation) can be digitized directly onto wireframe surfaces in the 3D window.

[![](../Images/Mobile-VR-Object.png)](<javascript:void\(0\);>)

A mobile VR object with an alignment string

This involves a specific mode of digitizing, not to be confused with other string digitizing commands, such as new-string, extend-string and so on. The method described here allows strings to be digitized directly onto a wireframe surface, regardless of 3D section orientation. Points are automatically projected to the nearest wireframe along the line of sight.

To digitize an alignment string in a 3D view:

  1. Load and display one or more wireframe surfaces or volumes in the 3D window.

  2. Elevate your viewpoint and pitch the view direction down so that you can see the surface clearly If there is a shallow angle between your view direction and the surface, small movements of the cursor may produce very large movements over the surface.

  3. In the Sheets control bar, active 3D window folder, right-click the Strings subfolder and select New.

The **Strings Properties** screen displays. 

  4. Type a name for the string into the Name box and click OK.

  5. In the 3D window, digitize (left-click only permitted) the required sequence of points onto a loaded and displayed wireframe surface.

  6. Press ESC to stop digitizing string points and cancel digitizing mode.

The point (or vertex) and edge of the string are displayed using the default rendering settings. You can change the rendering options later, after the trace has been defined, including hiding the string.

  7. Double-click the string to change its formatting if required. See [String Properties: General](<String_Properties_Dialog_General.md>).

  8. Consider [smoothing](<../command_help/smooth-string.md>) your string to introduce more vertices and ensure a smooth change of object direction during simulation playback.

Note: Alignment strings can also be digitized using any other digitizing command, and you can edit alignment strings created with the above method using any string editing command. Once created, alignment strings are indistinguishable to any string data in Studio products.

Related topics and activities

  * [Attaching Objects to Strings](<Strings_Attaching%20objects%20to%20strings.md>)

  * [Create a Flythrough](<Simulation_Creating%20a%20Flythrough.md>)

  * [3D Strings Menus](<Sheets_strings.md>)

  * [smooth-string ("sms")](<../command_help/smooth-string.md>)

  * [String Properties: General](<String_Properties_Dialog_General.md>)

  * [Strings Properties: Symbols](<String_Properties_Dialog_VertexVisualTab.md>)

  * [Strings Properties: Lines](<Traces%20Properties%20Dialog%20\(Edge%20Visual\).md>)

  * [Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)

  * [Fitting Strings onto a 3D Surface](<Strings_Fitting%20a%20string%20to%20a%20surface.md>)