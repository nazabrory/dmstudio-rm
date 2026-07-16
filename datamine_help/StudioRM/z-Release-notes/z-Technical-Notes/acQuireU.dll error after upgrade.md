# acQuire Data Connection - Failure after Upgrade

Technical Note: TN00441

## Background

In October 2023, Studio products supported by the acQuire Data Provider (for example, Studio RM) benefited from an upgrade to allow access to the latest capabilities. This driver update included an important 'wireframe constraint' feature and several other improvements. This driver update was deployed through our standard mechanism - Data Source Drivers, starting with Studio RM 2.0.

Unfortunately, this update to the acQuire Data Provider cannot be fully compatible with legacy acQuire-supported products and a compatibility break is unavoidable. This can lead to a failed acQuire data connection in a legacy product following the installation of a newer (but different) product on the same system. 

An example of this could be installing Studio RM 2.0 onto a system where Studio RM Pro 1.13 is already installed, and those products exist side-by-side.

## What's the Problem?

This issue only affects you if you need to connect to an acQuire data source through both a legacy (pre-October 2023) and new (October 2023 or later) application that is running on the same system.

If a new acQuire Data Provider is installed on a system that already hosts an older (pre-October 2023) application that makes use of the same data connection, the older application attempts to use the newer driver, and encounters a situation where files needed by the newer driver are not available.

As such, when the newer application is installed, the older application is no longer be able to access data through the acQuire Data Provider. The newer product will continue to have access.

## What's the Solution?

**Note** : This procedure will only be needed if you are running a combination of pre-October 2023 products and newer products side-by-side on the same system. As newer versions are installed over time, this procedure will become unnecessary.

It depends on whether you need access to an acQuire data source for your projects or not.

If not, there's nothing to do. This issue won't affect you.

If you need both legacy and new applications to connect to an acQuire database, you'll need to add some files to your system. It will only take a few minutes, using the following procedure:

  1. Ensure you are accessing Windows using an account with administrative privileges.

  2. If a failing legacy product is running, close it.

  3. Download the "AcquireFix.zip" archive from the following URL:

<https://dataminesoftware-my.sharepoint.com/:u:/p/productstore/EWxsrZ0K5c5Prmpv9YXJpUIBFcuC0d3XaevjD1FR-tk9YA?e=8OAxfx>

  4. Open the archive. The archive contains four files:

     * oc1101as.dll

     * oe1101as.dll

     * og1301as.dll

     * RWUXThemeS10.dll

  5. Copy these files to a temporary location, outside of the archive.

  6. In a folder browser, open the "Bin" folder of the legacy product that cannot connect to an acQuire data source following the installation of the newer product. For standard installations, this is at a location similar to **C:\Program Files\Datamine\\[Product Name]\Bin** , for example, **C:\Program Files\Datamine\StudioRM Pro\Bin**.

  7. Copy the files from the temporary location to the folder path above. Depending on your operating system access settings, you may need to confirm this action, possibly several times.

  8. Once all new files are in place, restart your legacy application. Both it and the newly installed product will be able to access acQuire data.