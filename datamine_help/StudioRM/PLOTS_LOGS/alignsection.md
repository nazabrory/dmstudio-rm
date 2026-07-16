# Aligning Plot Sections  
  
A plot sheet's section definition can be interactively aligned with specific points without changing other section properties. A series of sections is defined by the current center point and the section width, that is, if the current section is vertical at a northing of zero with a width of 50 then other sections will have centre points of ... -100, -50, 0, 50, 100 ....

To adjust a section position in a plot sheet projection:

Note: Adjusting the section can affect multiple other section definitions if you are modifying a [Master Section](<MasterSection.md>).

  1. Display the plot sheet containing the projection whose section you wish to modify.

  2. Left click to select the projection.

The **Projection (Section)** and **Projection (View)** ribbons display.

  3. Display the **Projection (Section)** ribbon.

  4. You can now modify the section definition using any of the following ribbon commands:

     * **Position >> Pick** to move to the section that contains the selected hole collar or intercept. The existing section centre points are not changed. 

Tips: Turn off clipping so that the point for inclusion is visible, and rotate the view perpendicular to the section and then select the new centre point in the rotated view.

     * **Position >> Snap** to move the section to the next selected point. The new section will transect the picked point retaining its azimuth and inclination.

**Tip** : You can also change the section definition for a plot projection by editing the projection's properties. See [Projection Properties](<projection%20properties.md>)

Related topics and activities

  * [Displaying and Editing the Section Definition](<CustomSections.md>)

  * [Projection Properties](<projection%20properties.md>)

  * [Master Sections](<MasterSection.md>)

  * [Section Definition](<CustomSections.md>)

  * [Add a Sheet or Projection](<insertsection.md>)