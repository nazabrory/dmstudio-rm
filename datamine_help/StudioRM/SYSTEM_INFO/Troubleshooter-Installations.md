# Installation Troubleshooter

Sometimes, installations of software don't go according to plan.

There are many possible causes for a failed installation, including insufficient hardware, active blocking by antivirus or antimalware services, unsupported hardware or software configurations, operating system security settings and so on. This topic is based on the incidents that have been reported to us in the past, and how they were resolved.

Important: Only install Datamine products downloaded from the Datamine Customer Portal. These installation packages are fully tested and free of viruses and malware. Installers or other supporting files from other sources should always be avoided as they may have been modified since we released them or may even install software that permits malicious actors to access your PC, putting you and your organization at risk.

If you can't find the answer you need below, please contact your local Datamine office for guidance.

Before you install Datamine Studio products, see [System Requirements](<Hardware-Requirements.md>), [System Guidance](<System-Guidance.md>) and [Graphics Capabilities](<Graphics-Cards.md>).

## Common Installation Problems & Solutions

Symptom | Cause | Recommendation  
---|---|---  
Double-clicking an installation file does nothing. | File is blocked.  |  Right-click the file and select Properties, then click **Unblock** .  
There is a problem with this Windows Installer package. A program run as part of the setup did not finish as expected  | Commonly caused by a partial/incomplete or corrupt download.  | Delete the local copy of the installer and download again. If the issue recurs, ensure your Network/Internet connection is not intermittent. If the problem persists, contact Datamine.   
At any point during installation, the message The installer was interrupted before Application could be installed is displayed and installation stops.  | Commonly caused by a partial/incomplete or corrupt download.  | Delete the local copy of the installer and download again. If the issue recurs, ensure your Network/Internet connection is not intermittent. If the problem persists, contact Datamine.   
A program required for this install to complete could not be run  | This Error indicates a problem with the Windows Installer's registration status inside the Operating System.  | 

  1. Click Start, click Run, type **MSIEXEC /UNREGISTER** , and then click OK. Even if you do this correctly, it may look like nothing occurs.
  2. Try the installation again. 

  
During installation, the message WARNING: could not delete temporary file followed by a file location.  | The location on the Windows system that is being used to store temporary installation files is restricted.  |  Ensure you are installing software as a local Administrator, or an account with the same privileges.  Check that the folder is not protected by other Windows setttings.  Disable User Account Control (UAC) If running from the Windows desktop, ensure Protected Desktop Mode is disabled.  Reboot the system to clear any pending Windows updates. Temporarily disable all running antivirus/antimalware/antispyware services (including group policies).   
Windows will not permit the installation to continue due to insufficient privileges | You are attempting to install Datamine software without administrative account privileges.  | Change the current account to one with local administrative rights and restart the installation. Right-click the installer file and select Run as Administrator. Enter new credentials if prompted.   
The Windows Installer Service could not be accessed.  Windows Installer Service couldn't be started. Could not start the Windows Installer service on Local Computer.  Error 5: Access is denied. |  You are attempting to install Datamine software without administrative account privileges.  The Windows Installer engine is corrupted and requires repair.  These errors can occur with general computer usage. Uninstalling applications, applying updates, and sometimes manual changes to some Windows components can cause these problems to surface.  |  Follow Microsofts guidance, here:  [http://support.microsoft.com/kb/324516 ](<http://support.microsoft.com/kb/324516>)  
Antivirus or antimalware services report an installation option as a potential threat.  | Installation behaviour has been deemed malicious by the installed/running security software.  |  Temporarily disable antivirus/antimalware services and reinstall.  Configure 3rd party security software to permit the unrestricted installation of Datamine products, prerequisites and runtimes.   
.could not be completed, do you wish to continue the installation?  A newer version of [item] is already installed.  | Attempted downgrade of insitu components.  |  Normally, you can proceed without any adverse behavior as the component(s) already on the machine are newer than the one(s) you are attempting to install. If a downgrade is required, you will need to manually uninstall the relevant components before re-running the installation package. Note: You cannot downgrade License Services below the minimum expected version for your product (it is installed with your product).  
"Windows cannot access the specified device, path or file. You may not have the appropriate permissions to access the item." | Microsoft's Attack Surface Reduction service is preventing installation. | See "Microsoft Attack Surface Reduction", below, for guidance.  
"There is a file or folder on your computer called "C:\Program" which could cause certain applications to not function correctly..." on PC startup. (In Studio Products) functions that involve filtering (including Quick Filter, extract object data and specifying filter expressions in the Data Object Manager) do not isolate data as expected. |  This is usually caused by installation of 3rd party software. For example, a product attempts to install something to C:\Program Files and the space after program is interpreted as the end of the string, generating a file of unknown contents (possibly empty) at the root of C: Known examples of these products are:

  * Webroot SecureAnywhere
  * Carbon Black (a VMWare product)

| Rename the file to "Program1" and then delete it.  
  
## Microsoft Attack Surface Reduction

Microsoft's Attack Surface Reduction technology is an additional layer of security provided by the Windows operating system.

It analyses multiple simultaneous conditions to determine if something should (or shouldn't) be installed on your PC. These criteria can include the original source of the file(s), where it is being installed from (which network or local folder location) and whether the file or file type is one that has been installed on your PC previously, amongst other things.

Sometimes, where a new version of Studio is downloaded from the Internet, despite our own in-house validation and certification processes for installation executable files, an installation package can be perceived as a threat. In this situation, an error occurs during installation that states:

Windows cannot access the specified device, path or file. You may not have the appropriate permissions to access the item

It's not particularly helpful, but you can get more information from the Windows Event Viewer, and other log files. 

#### What's Causing it?

Some versions of Windows Defender (Microsofts built-in antivirus) include something called _ASR rules_. These rules can block installers from running if theyre stored in certain folders or if they were recently downloaded from the internet.

So, if youre seeing a permissions error during installation, your PC might be blocking it based on:

  * Where the installer is stored (e.g. your Desktop or Downloads folder)

  * Whether the file was recently downloaded and hasnt been trusted yet

ASR is a highly configurable protection layer and one that can adapt itself over time based on your local PC activities. As such, on occasion, Windows will block the installation of software it deems a threat. There can be false positives.

#### Quick Fix: Move the Installer Somewhere 'Safe'

Heres what to do:

  1. Right-click the installer file you downloaded.

  2. Select **Properties**.

  3. If you see a checkbox near the bottom that says **Unblock** , check it, then **click OK**.

  4. Move the installer to a trusted folder, like **C:\MyFiles** (create a new folder if it doesnt exist).

  5. Right-click the installer again and choose **Run as administrator**.

This usually resolves the issue immediately.

#### Why This Works

Some folders (like Desktop, Downloads, or Temp) are watched closely by security tools because theyre common targets for malware. By moving the installer to a neutral folder like C:\MyFiles, you're telling Windows this file is okay.

Also, checking the Unblock box removes a safety tag that Windows adds to downloaded files, which can sometimes prevent them from running. You can access this option by right-clicking the installer file - it is at the bottom of the default tab displayed.

#### Is This Actually Safe?

Yes! Weve carefully tested our installers and they are digitally signed, and completely safe. Installation checks, both automated and hands-on are performed on every released installation package, across a wide range of environments. Our development environments are highly secure and constantly monitored for potential threats.

Datamine products are safe to install if they have been downloaded from the Datamine Customer Portal.

**Not sure where your installer came from?** Delete it and download a version from the portal. If you don't have access, contact Datamine.

If your IT team needs more details (for example, about our digital signatures or further technical explanation), feel free to reach out to us directly were happy to help.

#### Still Stuck?

It may be that something else is preventing you installing our software. If you're still having trouble:

  * Take a screenshot or video of the error.

  * Let us know your Windows version.

  * Tell us what folder the installer is currently in.

  * contact our support team and well get you sorted quickly.

Related topics and activities

  * [Studio RM Installation Guidelines](<Installation-Guidelines.md>)

  * [System Guidance](<System-Guidance.md>)

  * [System Requirements](<Hardware-Requirements.md>)

  * [Graphics Capabilities](<Graphics-Cards.md>)