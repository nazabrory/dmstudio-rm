# LINK Process  
  
To access this process:

  * Enter "LINK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **LINK** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LINK>).

## Process Overview

Important: This command is maintained for macro backward compatibility with earlier product versions released before the advent of the Studio range. The **LINK** process is intended to only be run from macros.

LINK may be used to create a new Datamine file inside the project folder, by linking an existing Datamine binary file located outside of the project folder.  
  
LINK with a catalogue file input may be used to restructure a set of Datamine files in the project folder. First files are unlinked (!UNLINK) individually; your application is exited (!**LOGOFF**); the existing database is deleted using system delete commands; your application is then re-entered, re-creating the database; then !**LINK** is entered using the catalogue file copied out previously.

The length of the system file name, including the full path name, is restricted to 56 characters.

The database file name is attached to symbolic file &**OUT**. The name of the external binary file is requested interactively.

**Note** : The external file name cannot be a catalogue file.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Database file name.  
  
## Example
    
    
    !LINK   &OUT(DBFILE)  
  
---  
      
    
    SYSFILE>\#Product Folder#\system\extfile.dm<return>  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> LINK ONLY WORKS WITH NATIVE-FILE DATABASES <<< |  The LINK process only works with Datamine file formats (*.dm, *.dmx). Fatal; the process is exited.  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.  
>>> ERR 120 <<< ( fileno) IN LINK |  Error in format or specifications of the file. This usually means that the external file already exists, but is not in the correct binary format. Fatal; the process is exited.