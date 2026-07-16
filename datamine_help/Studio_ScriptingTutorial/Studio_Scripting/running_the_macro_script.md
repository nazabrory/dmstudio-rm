![](../HeaderCell.jpg) |  Running the Macro Script  
---|---  
  
# Running the Macro Script

## Removing Macro Prompts

Before the script can be run we need to remove the macro Prompt commands. The following lines should be removed from the Shovel.MAC macro (found under C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts). This can be performed by editing the file inNotepad.

!PROMPT

0

1 Append Shovels (0=no, 1=yes) [$APPEND#] ? '$APPEND#',N

1 position of shovel in Easting [$E#] ? '$E#',N

1 position of shovel in Northing [$N#] ? '$N#',N

1 position of shovel in Elevation [$Z#] ? '$Z#',N

1 Azimuth that shovel is facing [$AZIM#] ? '$AZIM#',N

## Running the Script

The script should be run by selecting Tools | Scripting | Run Script... from the menu. To test the script follow the steps below.

  1. Ensure the Append Shovel check box is cleared.
  2. Enter a Shovel Azimuth of '45' degrees.
  3. Click the Create Shovel button, and then click in the centre of the Design window.
  4. Ensure the Append Shovel check box is checked.
  5. Enter a Shovel Elevation of '20'.
  6. Click the Create Shovel button, and then click in the top left hand corner of the Design window.
  7. Notice that the Design window zooms to display both images appropriately.
  8. Enter a Shovel Elevation of '-30'.
  9. Enter a Shovel Azimuth of '120' degrees.
  10. Click the Create Shovel button, and then click in the top right hand corner of the Design window. 

Update the view by typing 'uv' while focused on the 3D window. Adjust the view to see that shovels lie above and below the central plane as shown below.

[![](../Images/Studio%20Scripting%20MacroShovel%200004.jpg)](<../Images/Studio%20Scripting%20MacroShovel%200004.jpg>)  
---  
[Expand this image...](<../Images/Studio%20Scripting%20MacroShovel%200004.jpg>)  
  
## Validation

We have not included any validation on the values that are entered into the script interface. Null or inappropriate values may cause problems when the macro is running. Validation can be done using JavaScript, but is not part of this exercise.