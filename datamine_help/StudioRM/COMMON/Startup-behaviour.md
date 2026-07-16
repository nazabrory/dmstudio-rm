# Studio RM Startup

Studio RM is launched from the Windows desktop or **Start** menu.

During the startup phase, the following things happen:

  1. A license check is performed. Your application will only launch if:

     1. A valid license can be found either on your local system or a remote license server.

**Note** : If retrieving a remote license, you may need to provide user credentials.

     2. Your client system has been able to access the Internet at least once in the last 30 days. This is to ensure you have the latest security information from Datamine on your system (data is not transmitted to Datamine during this check).

  2. An interface [profile](<Startup-behaviour-profiles.md>) is detected. This will either be a default profile or, if one has been stored, a custom profile. Profiles store user interface layout information.

  3. Studio RM initializes and the detected profile is used to arrange screen components.

  4. [Custom ribbon items](<Ribbon_Customization.md>) display, if detected.

  5. The **[Start](<Start_Page.md>)** page displays.

     1. If no connection to the Internet is available, or you have chosen to disable online content, an installed, generic **Start** page displays.

     2. If a connection to the Internet is available and you have chosen to display online content, a live, online **Start** page displays

**Tip** : You can swap between online and offline systems in **[Options](<Options.md>)**.

  6. After creating or opening a project, further set up is performed:

     1. If required, a 3D window displays using [default options](<Options_InTouch.md>).

     2. Custom cursors display in the 3D window, or a default cursor if none are available.

Related topics and activities:

  * [The Start Page](<Start_Page.md>)

  * [Studio RM Installation Guidelines](<../SYSTEM_INFO/Installation-Guidelines.md>)

    * [Installation Troubleshooter](<../SYSTEM_INFO/Troubleshooter-Installations.md>)

  * [System Requirements](<../SYSTEM_INFO/Hardware-Requirements.md>)

  * [Graphics Capabilities](<../SYSTEM_INFO/Graphics-Cards.md>)

  * [User Interface Profiles](<Startup-behaviour-profiles.md>)