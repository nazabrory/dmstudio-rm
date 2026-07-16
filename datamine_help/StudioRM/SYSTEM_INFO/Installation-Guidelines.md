# Studio RM Installation Guidelines

The following topic describes general information relating to the installation of Datamine Studio software products.

## Installation Prerequisites

See also [System Requirements](<Hardware-Requirements.md>).

The following conditions must be met to successfully install Datamine Software:

  * You are a local administrator of the system being modified. All Datamine desktop products must be installed with full administrative access to the host system.

  * You are using a supported operating system.

  * Your PC meets the minimum supported hardware configuration, including a supported graphics card. See [Graphics Capabilities](<Graphics-Cards.md>) and [System Requirements](<Hardware-Requirements.md>).

  * You have sufficient disk space available.

  * It may be necessary to temporarily disable antivirus or antimalware before installing Studio software.

  * If installing to a non-standard location, that the target folder is not restricted (for example, installing to the Desktop in Windows Protected Mode). Microsoft's Attack Surface Reduction technology can prevent installing from certain locations, for files downloaded from the Internet. 

Also see [Installation Troubleshooter](<Troubleshooter-Installations.md>).

## Application Installation Packages

Datamine Application software products install a combination of items:

  * A core application.

  * Prerequisite components that will be shared by multiple applications. 

Prerequisite components are also available as standalone installation packages from your Datamine Support Portal. 

Note: **Your product will install a version of License Services**. This is the minimum possible version that can be used to activate your product. Don't downgrade License Services after installation as this will prevent your product from running.

## Upgrading Existing Versions

You can upgrade an existing version of the same product or component providing:

The existing product or component has a lower **major.minor.build** version number. For example, Studio RM version 1.3.47.0 can be used to upgrade version 1.2.86.0, 1.3.11.0 and so on.

During installation, an attempt will be made to upgrade the core application and all associated components. For both the application and associated components (also known as prerequisites) you may be asked to confirm that an upgrade of a component is required.

If you choose not to upgrade the core application, installation will stop.

If you choose to install the application but decide not to upgrade a component, installation will continue and attempts will be made to install subsequent components.

## Custom Installations

### Custom Install Options

By default, a core Datamine application and all prerequisite components will be installed/upgraded, if possible. You can change this behaviour by selecting a Custom installation option (see Installation Procedures, below).

A custom installation choice will also allow you to change where the product is installed.

### Installing to Non-standard Locations

The default installation path is recommended, but you can install to a different location if you wish, providing the path to the Studio installation folder does not exceed 170 characters.

Non-standard drive installations are also possible, providing the drive is available permanently to the host PC. Note that installing to removable media may cause performance issues if the transfer speed between the external device and host system is not sufficient.

## Installation Steps

Note: All Studio installations must be performed using an account with local administrative privileges.

To install a version of Studio RM on the current PC with an administrative account, this is the recommended procedure:

  1. Download the installation file from the [Customer Portal](<https://support.dataminesoftware.com/>). 

_Don't have access to the portal? Contact your local Datamine office._

  2. Uninstall the previous version of your product.

  3. Check the previous installation folder location in Windows. If any files remain, delete them.

  4. Restart your PC (this will release a lock applied by Windows on system files where Windows updates are pending).

  5. Run the installation executable (right-click and select **Run as Administrator**).

     1. If a confirmation prompt appears, click **Yes** to proceed.

  6. Click Install. If additional Windows runtimes are required for the software, they are installed first.

  7. On the **Welcome** screen, click **Next**.

  8. Review the **License Agreement** on the following screen and click **Accept** to continue installation.

  9. On the **Customer Information** screen, enter optional **User Name** and Organization details and click **Next**.

  10. On the **Setup Type** screen, decide if you wish to perform a **Complete** installation (recommended) or a **Custom** installation (see above).

  11. The **Ready to Install the Program** panel is the final step of the installation setup procedure. You can choose to add a desktop icon here (selected by default)

  12. The software packages are installed, in the following general order:

     * **Datamine License Services** is installed. If another version is found, you will be asked if you wish to upgrade it.

       * **Microcosm dongle driver** installation you will be prompted to install this driver if it hasnt already been installed. This driver is required if a Datamine dongle is to be used for licensing.

     * **Data Source Drivers** are installed. Again, if an existing driver package is found, you will need to confirm an upgrade. Otherwise, you need to confirm a fresh installation by clicking Install.

     * **Datamine Data Converter** is installed/upgraded.

     * **InTouch GO** (a lightweight visualizer) is installed.

     * **Table Editor is** installed/upgraded.

     * **Core application files** are installed/upgraded. This may take several minutes.

     * **Product registration** is performed. This step adds important information to the Windows registry to allow your product to operate (and is one of the key reasons you need to install software as a local Administrator).

  13. Click **Finish** to complete the installation process.

You can now run your product, although it will need access to a valid license.

### Silent Installations

You can install Datamine Studio applications and prerequisite programs from the command line, without user intervention.

If this is done as part of a group policy or automated rollout process, please ensure the account used to install remotely has full administrative access to the target machine(s), otherwise installation will fail. This document outlines the key basic principles for silent installations of Studio products. You may need to adapt this information to suit your particular bulk/group rollout services.

Note: Datamine can't provide specific support on how to distribute its software via 3rd party remote installation tools.

These unprompted installations can be accessed using command line switches supported by InstallShield packages.

#### Supported Products

All Datamine Studio products released after October 2019 can be installed silently, this includes:

  * Studio Mapper all versions

  * Studio EM 2.5 or higher

  * Studio Geo - all versions

  * Studio NPVS all versions

  * Studio NPVS+ - all versions

  * Studio OP 2.6 or higher

  * Studio RM 1.6 or higher

  * Studio Survey all versions

  * Studio UG 2.3 or higher

#### Command Line Example
    
    
    Datamine Studio RM (64-bit) 1.6.87.0 EN.exe /s /v"/qb ALLUSERS=1 REBOOT=ReallySuppress /norestart /l*v C:\Windows\Temp\Datamine Studio RM (64-bit) 1.6.87.0 EN.log"  
  
---  
  
Related topics and activities

  * [Installation Troubleshooter](<Troubleshooter-Installations.md>)

  * [System Requirements](<Hardware-Requirements.md>)

  * [Graphics Capabilities](<Graphics-Cards.md>)