# Project Settings: MineTrust

To access this screen:

  * On the [Project Settings](<ProjectSettings.md>) screen, select the **MineTrust** tab.

Configure project sharing settings for [MineTrust-aware projects](<../MineTrust/MineTrust-Aware-Projects.md>).

Note: MineTrust Connector must be installed locally to display this screen. To share project data using MineTrust, the MineTrust Connector service must be running.

To control how the project updates in the event of project folder changes:

  1. Display the **MineTrust Settings** screen.

  2. Review the MineTrust Connector status message. This with either display that the MineTrust Connector service is configured and running or is not configured. If the latter, review your MineTrust Connector installation and configuration.

  3. Choose how (or if) project data is shared using MineTrust:

     * **Check** Enable project for synchronization from MineTrust to automatically synchronize selected project data changes with other users via MineTrust Online. If **unchecked** , data changes are stored locally (but can be transmitted when the project is enabled.

     * To Share the local project file (and its changes) with MineTrust online, **check** Share project. If **unchecked** , local project file changes are only made locally.

  4. Click **OK** to create or update the current MineTrust package configuration and start synchronizing data. Check your [MineTrust dashboard](<../MineTrust/MineTrust-Dashboard.md>) for status updates.

Note: You can also configure MineTrust settings when creating a new project.

Related topics and activities

  * [Project Settings](<ProjectSettings.md>)

  * [Project Wizard ](<ProjectWizard.md>)

  * [MineTrust-Enabled Projects](<../MineTrust/MineTrust-Aware-Projects.md>)

  * [MineTrust Connector Dashboard](<../MineTrust/MineTrust-Dashboard.md>)