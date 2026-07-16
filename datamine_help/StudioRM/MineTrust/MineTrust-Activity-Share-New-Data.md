# Sharing Data With MineTrust

[MineTrust-enabled projects](<MineTrust-Aware-Projects.md>) are a great way to collaborate on Studio-related tasks. With minimal setup, you can share projects and related data safely and securely. 

You can [Create a MineTrust-Enabled Project](<../COMMON/Project%20Wizard-Activity-CreateMT.md>) or [open one created previously](<../COMMON/Activity-Open-MT-Project.md>). 

### Opening Existing MineTrust Projects

By default, MineTrust projects open in **"view-only" mode** even if MineTrust is locally installed and MineTrust Connector service is running. This is to prevent accidental data changes. You can tell this by looking at the top of the primary 3D window, where a banner appears:

[![](../Images/MineTrust-View-Only.png)](<javascript:void\(0\);>)

You will also see an icon in the top right corner of the application:

![](../Images/MineTrust-View-Only-Icon.png)

When you open the project for editing, the project and contents (known as the "MineTrust package") is 'locked', meaning other MineTrust users can't access it whilst you're busy with it. This lock is released when you close the project, or decide to stop synchronizing data.

### Share Data Using MineTrust

In example activity below, you will digitize a new string in a MineTrust-enabled project and commit the new data file to the MineTrust cloud host, ready for others to access it. The activity assumes you have a MineTrust-enabled project open in editing mode.

  1. In any **3D** window, digitize a new string. See [new-string ("ns")](<../command_help/new-string.md>).

  2. Save the string data as a new Datamine file in the current project directory (or any subfolder). 

  3. Save the project.

  4. Close the project. 

This automatically 'unlocks' the project and starts the process of synchronization.

Note: Data is not committed during a live project session. This minimizes data traffic and ensures you can prepare your data for others completely before sharing it.

Related topics and activities

  * [Open MineTrust Project](<../COMMON/Activity-Open-MT-Project.md>)

  * [Create a MineTrust-Enabled Project](<../COMMON/Project%20Wizard-Activity-CreateMT.md>)

  * [MineTrust View-Only Mode](<View-Only-Mode.md>)

  * [MineTrust Local PC Configuration](<MineTrust-Configure-PC.md>)

  * [MineTrust Connector Dashboard](<MineTrust-Dashboard.md>)

  * [Project Wizard: MineTrust Settings](<../COMMON/Project%20Wizard_MineTrust.md>)

  * [Project Wizard ](<../COMMON/ProjectWizard.md>)