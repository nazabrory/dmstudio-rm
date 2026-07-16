# The Start Page

The **Start** page is the first screen you see when your application starts. It appears as soon as the application has made its license checks and [installed the expected profile](<Startup-behaviour-profiles.md>).

The Start page is a web page embedded within your application. It provides information about the latest released version (if running in online mode) and access to basic project functions.

This topic describes the default **Start** Page. You can, if you wish, create your own Start page and configure your system to load that one instead. See **[Environment Options](<Options_Environment.md>)**.

## Offline vs. Online 

There are two versions of the Studio Start page:

  * The **offline** version contains static content, plus access to project loading and opening commands.

  * The **online** version displays information about the latest available release, project loading and opening commands plus links to other Datamine online resources such as eLearning.

Note: The online **Start** page is updated when a new version of Studio RM comes out. This also appears for users of older versions.

Your **Start** page will attempt to detect if a web connection is available before opening an online version of the Start page. This check is performed at system startup. You can swap between online and offline mode at any time (see below).

## Start Page Functions

Use the **Start** page to:

  * Create a new project.

  * Open an existing project, including a MineTrust-shared project.

  * Swap from an offline to an online page version (Internet access required).

  * Access the **[Customer Support Portal](<https://support.dataminesoftware.com/>)** to access latest releases and release notes.

  * View the latest released version's highlights.

  * Access other resources including the **[Datamine Documentation Website](<http://docs.dataminesoftware.com/> "Datamine Documentation Website")** , training information and Support.

To create a new Studio RM project:

  1. Display the **Start** page (online or offline version).

  2. Select **New Project**.

The [**[New Project Wizard](<project%20wizard_create.md>)**](<ProjectWizard.md>) displays.

To open an unshared project (method 1):

  1. Display the **Start** page (online or offline version).

  2. Select **Open Project.**

  3. Locate a project file to open.

  4. Click **Open**.

The selected project is loaded.

**Note** : You can also selected a recently opened project using the **Recent Projects** list.

To open an MineTrust-shared project (method 2):

  1. Display the **Start** page (online or offline version).

  2. Select **Open Project from MineTrust**.

  3. Locate a project file to open using the browser.

  4. Click **Open**.

The selected project is loaded and synchronization begins.

See [MineTrust-Enabled Projects](<../MineTrust/MineTrust-Aware-Projects.md>).

To swap from offline to online mode:

There are two ways to swap from offline to online Start page mode:

  1. Enable **Use online systems** on the **Start** page. This only appears on the offline page, then restart the application.

  2. Display **[Options](<Options.md>)** and enable the **Environment tab.** Select** Use online systems**.

**Note** : The **Use online systems** setting persists between different sessions of your application.

Related topics and activities

  * [Project Wizard ](<ProjectWizard.md>)

  * [Project Settings: MineTrust](<Project%20Settings_MineTrust.md>)

    * [MineTrust-Enabled Projects](<../MineTrust/MineTrust-Aware-Projects.md>)