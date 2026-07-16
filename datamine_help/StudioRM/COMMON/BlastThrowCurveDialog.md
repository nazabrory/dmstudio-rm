# Blast Displacement Modeler - Curve Method

To access this dialog:

  * In the Command toolbar, run the displace-blast-points-curve or displace-blast-strings-curve command.

These commands launch theBlast Displacement Modeler wizard, which allows you to calculate blast displacement using an alternative algorithm to the [IDW method](<BlastThrowIDWDialog.md>) for calculating blast. This blast displacement process is outlined below:

  1. Output Criteria: specify either the current object or a new object as output for the displaced object, and specify the powder factor.
  2. Blast Outline: select a closed blast outline perimeter string.
  3. Select Free Face: select segments at the start, end and within the free face segments on the Blast Outline string, and specify the Free Face Influence, in metres.
  4. Objects to Displace: select the points or strings to displace.
  5. Displacement Vectors: select the vectors that will control the displacement.
  6. Barrier strings: optionally select the barrier strings across which no displacement will occur.

The following settings are available:

Current object: Select the current object as the output by selecting the Current object option.

New object: Select a new object as the output by selecting the New object option, and providing a name in the accompanying box.

Powder Factor: Specify the powder factor in kg/m.

Select Blast Outline - Objects: Displays all loaded strings, and allows you to select a single, closed blast outline perimeter string.

Selection Tool: If toggled on, allows you to select whole objects by clicking them in the 3D window. The corresponding check-box in the Objects box is selected.

All: Selects all objects listed in the Objects box.

None: De-selects any selected objects that are listed in the Objects box.

Select Free Face:

\- Select the segment at the start of the free face segments on the Blast Outline string by clicking it in the 3D window.

\- Select the segment at the end of the free face segments on the Blast Outline string by clicking it in the 3D window.

\- Select a segment within the free face segments on the Blast Outline string by clicking it in the 3D window.

\- Enter a value in the Free Face Influence box

Select Points/Strings to Displace - Objects: displays all loaded points/strings, and allows you to select the relevant object to displace.

Select Vectors \- Objects: displays all loaded strings, and allows you to select strings representing the vectors which control the displacement.

Select Barriers- Objects: displays all loaded strings, and allows you to optionally select the barrier strings across which no displacement will occur.

Back: displays the previous dialog in the Blast Displacement Modeller wizard, and clears any selections that you have made.

Next: displays the next dialog in the Blast Displacement Modeller.

Finish: closes the Blast Displacement Modeller wizard, and runs the blast displacement process. The displaced objects are displayed in the 3D window.

Cancel: closes the Blast Displacement Modeller wizard without running the blast displacement process.

Related topics and activites

  * [Blast Displacement Modeller Wizard - IDW Method](<BlastThrowIDWDialog.md>)