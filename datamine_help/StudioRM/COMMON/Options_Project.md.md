# Project Options

To access these screens:

  * [Options](<Options.md>) screen **> > Project**.

Configure settings that apply to your project:

## General Options

Confirm wireframe point filename in browser If **checked** , you must confirm the name of the wireframe points file associated with the selected triangles file before it is loaded. If **unchecked** , and a points file with the same name plus a "pt" suffix is found in the same location, the wireframe triangle pair are loaded together (if no points file is found, you are asked to select one).

Hide empty folders If checked, empty project folders are hidden from view in control bars.

Project File Double Click Choose the double-click action for items in the **[Project Files](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)** control bar; either load the file or open the file in the default browser (for example, **Table Editor** for .dm or .dmx files).

Project Switching If **checked** , you must confirm to close one project and open another.

Unload All Data If Confirm before "Unload all data" is checked, a confirmation prompt displays when running the unload-all command by any method, if data changes have been made since the last save.

**Interactive Editing** If **Double click to finish** is checked, double-clicking terminates the current modal command. If unchecked, two digitized points are added, most likely very close to or coincident with each other.

## Automatic Updating

The following options allow you to determine if, and how, your project is updated automatically:

  * Detect new files in the project... If **checked** , new files recently added to the project are announced when the project file is opened, and the project document is updated.

  * Detect files added to or removed... If **checked** , files added or removed from the current project are detected during the project session and the project is updated.

  * Automatically update project (no prompts) Only available if one or both of the two options above are checked, **checking** this ensures the project is updated without prompts. If unchecked, you are prompted to confirm changes to the project file.

**Note** : These options can affect system performance if enabled.

  * File Exclusions Exclude certain files from triggering the 'project update' process. The list shown contains all currently excluded file types. You can use the wildcard symbols '?' and '*' to add variable data. File exclusions will be applied in the order shown in the resulting list. The following actions are possible:

Choose this...| ...to do this  
---|---  
New File Exclusion| Create a new file exclusion, using wildcards if necessary.  
Delete File Exclusion| Remove the highlighted exclusion from the list.  
Move Exclusion Up| Move the selected exclusion up the list.  
Move Exclusion Down| Move the selected exclusion down the list.  

## Printing

Project-data-related printing options. Select one of these:

  * Screen/actual size Show all project data at 100% scale when outputting to the printer.

  * Fit to printer page size Scale project data printed output to match the media associated with your printer.  

## Files, Fields, Parameters

The following options determine how process screens behave:

  * Save always Running a command always saves over the top of identically-named files if an output file is created.

  * Restore always Running a command always restores original files if an output file is created and the resulting filename matches an existing file.

  * Give a warning when overwriting files **Check** to always prompt when overwriting existing files.

Related topics and activities

  * [System Options](<Options.md>)