# MineTrust-Enabled Projects

A Studio project that shares data via the MineTrust cloud service is said to be "MineTrust-aware". 

Shared files are automatically synchronised with **MineTrust** so that other people accessing that data always have access to the latest version available, ensuring data is consistent across your organization for all projects where synchronization is enabled.

Before you can start to share data via the MineTrust cloud, you need to set a few things up, as described below.

Data synchronization activity information and other MineTrust Connector functions can be accessed using the [MineTrust Connector Dashboard](<MineTrust-Dashboard.md>).

### No MineTrust?

A MineTrust-enabled project will always 'look' for a connection to its cloud host when you open it. As such the "MineTrust awareness" of a project is an intrinsic property. This doesn't mean you can't open it though, as if you haven't got access to MineTrust you are offered a choice on project startup (click the image to expand it):

[![](../Images/MineTrust-View-Only2.png)](<javascript:void\(0\);>)

  * Clicking **No** opens the project in **view-only mode**. In this mode you can still:

    * Load and unload data within the project.

    * Modify visual properties, including:

      * Formatting styles (Line, Symbols, Opacity, and so on)

      * Legends

      * Filtering and selection tools

    * Navigate and explore the 3D workspace, including selecting and querying objects.

Note: Filters and legends are created temporarily and are not saved in View Only mode.

  * Clicking **Yes** opens the project as a standalone, unshared clone of the project. In this case, your changes aren't shared with others and are only performed in isolation. 

This is, essentially, creating an offline copy of the shared project.

By default, MineTrust projects open in **"view-only" mode** even if MineTrust is locally installed and MineTrust Connector service is running. This is to prevent accidental data changes. You can tell this by looking at the top of the primary 3D window, where a banner appears:

[![](../Images/MineTrust-View-Only.png)](<javascript:void\(0\);>)

You will also see an icon in the top right corner of the application:

![](../Images/MineTrust-View-Only-Icon.png)

When you open the project for editing, the project and contents (known as the "MineTrust package") is 'locked', meaning other MineTrust users can't access it whilst you're busy with it. This lock is released when you close the project, or decide to stop synchronizing data.

Click **Enable Editing Mode** to start modifying the project.

See [MineTrust View-Only Mode](<View-Only-Mode.md>).

See [Sharing Data With MineTrust](<MineTrust-Activity-Share-New-Data.md>)

## Configuring MineTrust

MineTrust relies on a background service that continually checks for project changes and (depending on your settings) synchronizes data with a secure cloud platform for access by an approved audience.

MineTrust depends on **MineTrust Connector** , which must be installed on any local device or server that will be synchronising data with the central instance. The connector facilitates automated, encrypted transfer of project files and supports scheduled synchronisation intervals.

MineTrust also depends on an available **license** , managed centrally via the Datamine Customer Portal. Customers are able to nominate accounts for access. Datamine will facilitate enabling access for those accounts.

## Data Synchronization

How and when is data synchronized between the MineTrust cloud store and the local machine?

MineTrust project changes are made during a project session, whilst the project is 'locked' from access by other users (other than in [MineTrust View-Only Mode](<View-Only-Mode.md>)). This makes sure your changes are batched up and committed in a single operation for others to benefit from.

For example, consider the following timeline showing two Studio users make changes to the same project in a MineTrust enabled organization:

[![](../Images/MineTrust-Lock2.png)](<javascript:void\(0\);>)

In summary, opening a MineTrust-enabled project for editing locks it, and closing the project (or stopping synchronization) unlocks it, automatically synchronizing changes.

Related topics and activities

  * [Open MineTrust Project](<../COMMON/Activity-Open-MT-Project.md>)

  * [Create a MineTrust-Enabled Project](<../COMMON/Project%20Wizard-Activity-CreateMT.md>)

  * [MineTrust View-Only Mode](<View-Only-Mode.md>)

  * [MineTrust Local PC Configuration](<MineTrust-Configure-PC.md>)

  * [MineTrust Connector Dashboard](<MineTrust-Dashboard.md>)

  * [Project Wizard: MineTrust Settings](<../COMMON/Project%20Wizard_MineTrust.md>)

  * [Project Wizard ](<../COMMON/ProjectWizard.md>)