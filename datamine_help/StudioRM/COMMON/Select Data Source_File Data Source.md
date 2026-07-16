# File Data Source

To access this screen:

  * [Select Data Source](<Select%20Data%20Source%20Dialog.md>) screen >> **File Data Source** tab.

This screen is used to connect with a data source that has file data source names (DSNs). 

A DSN is a named configuration that tells an ODBC driver how to connect to a specific database. It typically includes:

  * The ODBC driver to use

  * The server or host name

  * The database name

  * Authentication details (username/password or trusted connection)

  * Optional settings like port, encryption, or timeouts

When you run an ODBC import, the application references the DSN instead of requiring all connection details each time. The **File Data Source** screen, then, asks you to select a .dsn file created from a previous import (or configured elsewhere) or create a new data source connection.

Note: A file-based data source, not necessarily user-dedicated nor local to a computer, can be shared among all users who have the same drivers installed.

This type of data source differs from the [Machine Data Source](<Select%20Data%20Source_Machine%20Data%20Source.md>) which is stored in the Windows registry.

To use an existing file data source:

  1. Display the **File Data Source** screen.

  2. Use Look In to define the directory for which the sub-directories and file DSNs are listed in the window below.
  3. In the browser window, select a data source .dsn file.
  4. Click **OK** to connect to the data source.

To create a new file data source:

  1. Display the **File Data Source** screen.

  2. Click **New**. 

The Create New Data Source screen displays.

  3. Choose the driver for which you are adding a file DSN.

  4. Click Next to specify the name or location of the new file DSN. 

  5. Click Next again to view a summary of the new information. 

  6. Click Finish to display the driver-specific set up screen.

  7. Click **OK** to connect to the new data source.

Related topics and activities:

  * [Select Data Source](<Select%20Data%20Source%20Dialog.md>)

  * [Specify Block Model Parameters](<Specify%20Block%20Model%20Parameters.md>)

  * [Machine Data Source](<Select%20Data%20Source_Machine%20Data%20Source.md>)

  * [Data Import](<data%20import%20dialog.md>)