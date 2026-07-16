# Running the Browse and Copy Script

Make sure that you have saved the completed script. If you want to use the reference version then take a copy of '_scr_Browse_and_Copy 0001.htm' into your Tutorial database.

## Prerequisites

  * The file _vb_scr_points.dm will be used to test the script. This file can be found at `C:\Database\DMTutorials\Data\VBOP\Datamine`

  * The Browse.htm file created during the exercise [Creating the Browse and Copy Interface](<creating_the_browse_and_copy_interface.md>).

## Exercise: Running and testing the script

You will run three tests on the script to ensure it is working as expected.

  1. Run your application and create a new, empty project.
  2. Activate the Home ribbon and select **Scripts >> Run Script**.
  3. You may, at this stage, see a dialog asking if you wish to convert your script to the Studio standard specification. In this instance, select No.
  4. Select the `Browse.htm` file created in [Creating the Browse and Copy Interface](<creating_the_browse_and_copy_interface.md>) and click Open. 
  5. You will now use the top **Browse**... button to select the file `_vb_scr_points`. Click Browse..., from the Browser dialog select the file `_vb_scr_points` from `C:\Database\DMTutorials\Data\VBOP\Datamine` and click OK.
  6. You can either specify the name of an Output File or use the second Browse... button. For this example we will type the name of the file as 'OutFile'.
  7. Leave the Retrieval Criteria text box blank.
  8. Before executing the script ensure that the Command window is visible and right clicking in the window select Clear from the popup menu.
  9. Click the OK button in the script window. The Command window should now display the information that 80 records were copied to the file `outfile.dm`.
  10. Leaving the Input and Output file details as they are, type '=19' into the Retrieval Criteria text box.
  11. Click the OK button in the script window. The Command window should now display the information that 38 records were copied to the file `outfile.dm` and the currently established retrieval criteria was 19.
  12. Repeat step 8 and 9 defining '=11' as the retrieval criteria. The Command window should now display the information that 17 records were copied to the file outfile.dm and the currently established retrieval criteria was 11.

![](../Images/UpArrow.gif)Top of page

![note.gif \(1017 bytes\)](../Images/note.gif) |  If the script needs to be debugged then use the methods in the previous exercise.  
---|---