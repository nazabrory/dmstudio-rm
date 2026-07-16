# Open Standard Project

You can open a Studio project using one of the following methods:

  * Double-click the project file icon in Windows.

  * **Start** Page **> > Open Project**.

  * **[Project](<Ribbon_File_Button.md>)** menu >> **Open**.

Select the project file using the displayed browser and your project opens. 

This is what happens when a project opens:

  * Project settings are reinstated, as previously saved with the target project.

  * If data was set to automatically reload when the project is opened, it is reloaded if it can be found at the expected location (otherwise you are asked to browse for each file that can't be found).

  * If an automation script is set to run on project launch, it is launched (after it is checked for [safe syntax](<Script-updater-tool.md>)).

  * The data windows are reinstated as saved (and any stored plot sheets are redisplayed).

If non-default Datamine file formats are detected within your project folder, Studio needs to convert them to the default file format before opening. Click **OK** to continue. See [Datamine File Formats](<Datamine-File-Format.md>).

You can open a project file of any Studio application. It doesn't have to be your native format, but be aware that projects are handled differently in some cases. For example, you can open a Studio Mapper (.mpproj) file in Studio RM but you won't connect to the mapping database automatically. Similarly, you can open a Studio OP (.opproj) file in Studio EM, but won't be able to change automated pit design settings.

**Note** : Project files that are located outside the project folder are not converted. You can convert files between DM and DMX format in either direction, depending on the current default format. See [Datamine File Formats](<Datamine-File-Format.md>).

Related topics and activities:

  * [Open MineTrust Project](<Activity-Open-MT-Project.md>)

  * [Create a New Project](<Project%20Wizard-Activity-Create.md>)

  * [Create a MineTrust-Enabled Project](<Project%20Wizard-Activity-CreateMT.md>)

  * [Datamine File Formats](<Datamine-File-Format.md>)