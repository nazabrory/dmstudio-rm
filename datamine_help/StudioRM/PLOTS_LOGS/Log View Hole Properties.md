# Log View Properties: Hole

To access this screen:

  * On the [**Log View Properties**](<Log-View-Properties.md>) screen, select the **Hole** tab.

The Log View Hole Properties screen is used to configure [log sheets](<../COMMON/Window%20Overview_%20Logs.md>), specifically, the basic formatting properties that apply to the display of the log data.

To configure general log sheet formatting properties:

  1. Display the **Hole** screen.

  2. Select the **Current Hole** **Name**. 

**Note** : For imported files, this description is derived from the field mapped to the default Borehole ID (BHID) field expected by your application. On selection of a hole description from this list, a 'Length' value is added, denoting the FROM-TO length of the selected hole, according to the underlying data.

  3. Define the **Extents** of the selected hole. This is the relevant length of the hole, for the purposes of the log view display. You can display as much, or as little, of the recorded downhole sample data as is required for your data presentation. In this area, you have three choices:

     * Entire Hole Display the entire hole in the log view, encompassing the full range of FROM-TO depth intervals.

     * Automatic The view of the log display will be at the system default scale.

     * Custom Specify your own maximum FROM-TO extents. This has the effect of scaling the view of data in the log view. 

  4. Choose log **Scale** options. 
     * Automatic will display the log view in whichever view is dictated by **Extents** settings (see above).
     * Custom allows you to define your own scale as ratio (1:n). 
     * Check Locked to ensure subsequent log viewing operations do not affect the scale specified here.
  5. Choose how the log view is updated when the underlying data for the hole change using **Initial extents when hole changes** settings. Changes could occur, for example, by the loading or refreshing of data. The following options are available:
     * Entire hole Display the entire hole in the log view, encompassing the full range of FROM-TO depth intervals.
     * Automatic The view of the log display will be at the system default scale.

     * Same as previous hole: When data changes, set the formatting to whatever is relevant to the hole immediately preceding it, according to the index defined by the virtual index based on the BHID description.

     * Invert display for up holes If **checked** , holes that are defined as 'inverted' (that being, where a collar position is of a lower elevation that the corresponding end-of-hole (EOH) position for the same hole entity) cause the log view to be mirrored around the horizontal axis (including the display of images) so that the log split is a true representation of the geometrical alignment of the hole.

     * Always invert display If checked, override the Invert display for up holes (see above) property, and invert the current log view regardless of the relationship between collar and EOH positions.

Related topics and activities:

  * [Changing the downhole scale](<LogPanandScale.md>)

  * [Viewing other holes](<changehole.md>)

  * [Changing sheet and view properties](<Section_View_Data_Area_Properties.md>)

  * [Pan up and down the hole](<LogPanandScale.md>)

  * [Formatting log sheets](<FormatLogColumnSbS.md>)

  * [Logs - Adding Images](<Logs_Adding%20Images.md>)