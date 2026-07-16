# Master Sections

A section definition in one view can be used to control the display of data in other section and 3D views. In this context, one section is the "master" (the one that controls which changes are rippled out to other sections).

Why use a section master?

Defining a section master allows you to create multiple views in plan, transverse and 3D all using the same section definition. Changing the section definition (width, dip and azimuth) in one view is automatically applied to all views that use the section master. Changing the section position (using the Next and Previous commands) in any one of these views is applied to all views.

To define the section master:

  1. Enable [Page Layout](<PageLayoutMode.md>) mode.

  2. Right-click the projection containing the section definition you wish to set as a master.

  3. Select **Projection >> Section >> Set as Active Section**.

**Note** : If a message is displayed stating there is no current section master, click OK to set the currently selected section as the master.

To apply the section master to another view:

  1. Define a section master (see above).

  2. Display and select the projection you wish to update with master section properties.

  3. Right-click the target projection and select Projection >> Section >> Use Active Section.

  4. At the prompt, click **OK**.

Your section projections are now linked. Changes to the master section (clipping, section position and so on) are now reflected instantly in the associated dependent section.

Note: A master section can control any number of dependent sections.

Related topics and activities

  * [Creating and defining sections](<insertsection.md>)

  * [Changing sheet and view properties](<Section_View_Data_Area_Properties.md>)