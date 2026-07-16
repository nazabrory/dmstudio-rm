# Section Properties

Note: This topics relies on concepts outlined here: [3D Sections](<Sections.md>).

To access this screen:

  * In the Sheets control bar, active 3D window folder, Sections folder, right-click a section object, select Properties.

  * In the Sheets control bar (Sheet, Projection, 3D Overlay Group sub-menu), double click the Section Line option.

  * In the **Sheets** or **Project Data** control bar, double click a parent section object.

  * In the active **3D** window, double-click a parent section object.

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The Section Properties screen properties of a parent 3D section. 

The behaviour of this screen (particularly, the fields that are available for editing) depends on how it was opened:

  * If you have imported a section definition file, or one exists in memory, you can see the definitions held within the imported table, but you will not be able to edit them individually \- this must be achieved by the parent application. 

You can view all associated section definitions using this screen.

Section table-based objects display read-only Section Orientation, Section Mid-Point, Plane Dimensions and Section Width options , as these are controlled by the table.

  * If you are using a [default section](<Sections.md>) or section created in the 3D window you can access and edit that definition in full, using this screen.

  * If you are updating the section used to represent a 3D overlay (within a **3D Overlay Group** folder) in the Plots window, you can edit the section used within that projection using this screen. [More about 3D Overlay Groups...](<../PLOTS_LOGS/3D%20Overlay%20Concept.md>)

To define a parent or standalone 3D section:

  1. Display the **Section Properties** screen.

  2. Enter the Name of the section. This appears in the **Sheets** and **Project Data** control bars.

  3. If editing a parent section (the section has child entities), review the name of the **Section Table** data object associated with the section. For standalone sections, this field is blank (a section definition object isn't needed for this type of section).

  4. Define the **Section Orientation**. That is, how it is oriented in the 3D world. You can use one or more of these options:

     * Use a present orientation with Horizontal, North-South or East-West. 

     * Edit the Azimuth and Inclination of each section individually by manually entering the numeric values for each in the fields to the right of the buttons.

  5. Set the **Section Ref Point** (the mid point of the selected section in 3D space) by defining coordinate values. 

Note: This is the point around which section rotations occur and also determines the mid-point of the visible section when **Plane Dimensions** are used (see below).

  6. Define **Plane Dimensions**. By default, each plane is displayed as infinite in both key axes, however, you can override this setting and define your own section limits by checking Use Dimensions and entering the required values for Width and Height.

Note: This is a display setting - you can still digitize 'outside' of the displayed section and the section will still be treated as infinite.

  7. If there are multiple child sections of a parent section, use the Position arrows to cycle through the definitions available, updating the screen fields automatically.

  8. Define **Clipping** settings:

     * None No clipping is performed.
     * Front All items in front of the main section plane is clipped.

     * Back All item behind the main section plane is clipped.

     * Outside All items, except those falling within the defined Section Widths (see above) from the current section plane is clipped out.

Note: If you are defining a section to support the display of 3D overlays in a [**3D Overlay Group of a plot sheet**](<../PLOTS_LOGS/3D%20Overlay%20Concept.md>), only None and Outside options are supported.

     * Disable on hide If checked, clipping is only performed when the section is displayed, and disabled when hidden.

     * Primary Clipping Set Front and Back settings to set the amount of data clipped in front of and behind the section.

Note: Select Infinite for either **Front** or **Back** to effectively disable primary clipping regardless of other view clipping controls.

     * Optionally, apply Secondary Clipping to the section. See [Clipping 3D Data](<Clipping-Data.md>).

Note: You can also apply global data clipping values to the entire 3D scene (in relation to the 3D 'camera') using the [Environmental Settings](<EnvironmentalSettings_Dialog.md>) screen.

  9. Choose **Section Plane** visualization settings. These properties only control how the section appears in the 3D view:

     1. Fill Flood the section plane with a (by default, semi-transparent) colour.

     2. Lines Show the boundary lines of the section as hatched lines.

     3. Arrow Show an arrow indicating the front facing aspect of a section. This is important when differentiating the front and rear of a section plane when clipping is applied according to the Front and Back values set.

     4. Color Set a colour for the section plane by double-clicking the colour-preview pane. A colour picker will then be shown, allowing you to select another colour.

     5. Opacity Set the transparency of the section plane here, from 0% to 100% (opaque).

  10. Define Section Extents formatting. These offer the same settings as **Section Plane** (see above) minus the Arrow setting (which isn't relevant).

  11. Click **OK** to update the current section display.

  12. Save your project.

Related topics and activities:

  * [Using the Sections Folder](<workspace_sections.md>)

  * [Section Row Properties](<../COMMON/SectionRowProperties.md>)
  * [Create or Modify a 3D Section](<../COMMON/3D%20Section%20Manager.md>)
  * [Create Multiple Sections](<../COMMON/Create-multiple-sections.md>)

  * [Create or Modify a 3D Section](<../COMMON/3D%20Section%20Manager.md>)