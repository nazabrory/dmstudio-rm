# User Interface Profiles

The layout of your application is governed by an external file called a "profile".

A profile is an XML file created and updated automatically by Studio RM each time you modify a part of your [user interface](<User-interface.md>). Profiles should never be edited manually as this can cause application startup to fail.

Your user interface profile is read during [system startup](<Startup-behaviour.md>), and controls the following:

  * Ribbon and toolbar configuration.

  * Control bar position.

  * Toolbar contents and position.

  * Window display, including external or independent 3D windows.

  * The **[Quick Access](<Ribbon_Customize.md>)** menu.

A default profile is used the first time an application is launched, and is updated as interface changes are made. You can also create an independent profile to share with others.

To create a new user interface profile for sharing:

  1. Launch your application and make the necessary interface layout changes to control bars, **Quick Access** menu, windows or toolbars.

  2. Activate the **Format** ribbon.

  3. Select **Customize >> State >> Save**.

  4. Select a storage folder and **File name**.

  5. Click **Save**.

To load a custom user interface profile:

  1. Activate the **Format** ribbon.

  2. **Customize >> State >> Save**.

  3. Locate the .xml file containing profile information.

  4. Click **Load**.

The user interface updates to match the settings in the loaded profile.

To reset the user interface to a default arrangement (application restart method):

  1. Close your application.

  2. Restart your application whilst holding down <CTRL>

  3. If prompted to use a profile that is earlier than expected, click **No**.

Your application launches with a default profile.

To reset the user interface to a default arrangement (no restart methd):

  1. Activate the **Format** ribbon.

  2. **Customize >> State >> Reset**.

The user interface updates to match the settings in the loaded profile.  
  

Related topics and activities:

  * [Studio RM Startup](<Startup-behaviour.md>)

  * [User Interface](<User-interface.md>)

  * [Customizing Control Bars](<Customizing.md>)

  * [Ribbon Customization](<Ribbon_Customization.md>)

  * [Customize](<customize.md>)

  * [Customize Toolbars](<Customize_Toolbars.md>)

  * [Quick Access](<Ribbon_Customize.md>)

    * [Customize Quick Access](<Ribbon_Customize.md>)