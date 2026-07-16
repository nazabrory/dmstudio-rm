# Blast Displacement Modeler Wizard - IDW Method

### To access this wizard:

  * In the Command toolbar, run the displace-blast-points or displace-blast-strings command.

These commands launch theBlast Displacement Modeler wizard. This allows you to calculate blast displacement using an alternative algorithm to the [Curve Method](<BlastThrowCurveDialog.md>) for calculating blast. This blast displacement process is outlined below:

  1. Output Criteria: specify either the current object or a new object as output for the displaced object, and specify interpolation options.
  2. Blast Outline: optionally select a blast outline perimeter.
  3. Objects to Displace: select the points or strings to displace.
  4. Displacement Vectors: select the vectors that will control the displacement.
  5. Barrier strings: optionally select the barrier strings across which no displacement will occur.

The following settings are available:

Current object: Select the current object as the output by selecting the Current object option.

New object: Select a new object as the output by selecting the New object option, and providing a name in the accompanying box.

Interpolation Options:

IDW Power: the power associated with the Inverse Distance Weighting interpolation method - the default is 2.

Ignore any blast vectors outside of blast outline: a blast vector defines the expected blast movement at a particular point. Selecting this option specifies that blast vectors located outside of an optional blast outline are ignored by the interpolation process.

Select Blast Outline - Objects: displays all loaded strings, and allows you to optionally select a single string as a blast outline. If the Ignore any blast vectors outside of blast outline option is selected, then blast vectors that are located outside of this string are ignored by the interpolation process.

Selection Tool: if toggled on, allows you to select whole objects by clicking them in the 3D window. The corresponding check-box in the Objects box is selected.

All: selects all objects listed in the Objects box.

None: de-selects any selected objects that are listed in the Objects box.

Select Points/Strings to Displace - Objects: displays all loaded points/strings, and allows you to select the relevant object to displace.

Select Vectors \- Objects: displays all loaded strings, and allows you to select strings representing the vectors which control the displacement.

Select Barriers- Objects: displays all loaded strings, and allows you to optionally select the barrier strings across which no displacement will occur.

Back: displays the previous dialog in the Blast Displacement Modeller wizard, and clears any selections that you have made.

Next: displays the next dialog in the Blast Displacement Modeller.

Finish: closes the Blast Displacement Modeller wizard, and runs the blast displacement process. The displaced objects are displayed in the 3D window.

Cancel: closes the Blast Displacement Modeller wizard without running the blast displacement process.

Related topics and activities

  * [Blast Displacement Modeller Wizard - Curve Method](<BlastThrowCurveDialog.md>)