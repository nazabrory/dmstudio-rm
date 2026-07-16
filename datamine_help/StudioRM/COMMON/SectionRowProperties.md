# Section Row Properties

Note: This topics relies on concepts outlined here: [3D Sections](<../VR_Help/Sections.md>).

To access this screen:

  * Double-click a child section definition in the **Sheets** or **Project Data** control bar.

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

Define a [3D section](<../VR_Help/Sections.md>), as part of multiple definitions belonging to the same 3D section 'parent'. Similar to the [Section Properties](<../VR_Help/Section%20Properties%20Dialog.md>) screen, the **Section Row Properties** screen is used to support the 'child' section of a full section definition. As such, it shares some commands with the parent section equivalent screen.

Activity steps:

  1. Display the **Section Row Properties** screen.

  2. Enter the Text to be displayed in the **Sheets** and **Project Data** control bars.

  3. Define the **Section Orientation**. That is, how it is oriented in the 3D world. You can use one or more of these options:

     * Use a present orientation with Horizontal, North-South or East-West. 

     * Edit the Azimuth and Inclination of each section individually by manually entering the numeric values for each in the fields to the right of the buttons.

  4. Set the **Section Ref Point** (the mid point of the selected section in 3D space) by defining coordinate values. 

Note: This is the point around which section rotations occur and also determines the mid-point of the visible section when **Plane Dimensions** are used (see below).

  5. Define **Plane Dimensions**. By default, each plane is displayed as infinite in both key axes, however, you can override this setting and define your own section limits by checking Use Dimensions and entering the required values for Width and Height.

Note: This is a display setting - you can still digitize 'outside' of the displayed section and the section will still be treated as infinite.

  6. If there are multiple child sections of a parent section, use the Position arrows to cycle through the definitions available, updating the screen fields automatically.

  7. Define **Clipping** settings:

     * None No clipping is performed.
     * Front All items in front of the main section plane is clipped.

     * Back All item behind the main section plane is clipped.

     * Outside All items, except those falling within the defined Section Widths (see above) from the current section plane is clipped out.

Note: If you are defining a section to support the display of 3D overlays in a [**3D Overlay Group of a plot sheet**](<../PLOTS_LOGS/3D%20Overlay%20Concept.md>), only None and Outside options are supported.

     * Disable on hide If checked, clipping is only performed when the section is displayed, and disabled when hidden.

     * Primary Clipping Set Front and Back settings to set the amount of data clipped in front of and behind the section.

Note: Select Infinite for either **Front** or **Back** to effectively disable primary clipping regardless of other view clipping controls.

     * Optionally, apply Secondary Clipping to the section. See [Clipping 3D Data](<../VR_Help/Clipping-Data.md>).

Note: You can also apply global data clipping values to the entire 3D scene (in relation to the 3D 'camera') using the [Environmental Settings](<../VR_Help/EnvironmentalSettings_Dialog.md>) screen.

  8. Click **OK** to update the current section display.

  9. Save your project.

Related topics and activities:

  * [Using the Sections Folder](<../VR_Help/workspace_sections.md>)

  * [Section Properties](<../VR_Help/Section%20Properties%20Dialog.md>)

  * [Create or Modify a 3D Section](<3D%20Section%20Manager.md>)
  * [Create Multiple Sections](<Create-multiple-sections.md>)

  * [Create or Modify a 3D Section](<3D%20Section%20Manager.md>)