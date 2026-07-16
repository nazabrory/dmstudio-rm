# Accessing Commands and Processes

Commands in your application can be categorized in numerous ways: by window, by data type, by object, by work function etc.. This section will look at commands and processes.

  * Commandsare interactive instructions which create or influence objects in memory. A command can either be launched using a script, a command-line entry or interactively using one of the many functions in your application.

  * Processes are file-based. They require one or more files in Datamine binary format, and depending upon the process, convert the data to create one or more new Datamine format files.

Note: There is a subset of these processes that are used to construct more complex logic within macros - these commands (unrelated to any others that represent or support mining domain processes) are referred to throughout this help file as "Macro Processes" (you can find an A-Z list of them [here](<../command_help/commandtable.md>)).

Commonly-used commands have ribbon buttons for easy access. Your system is also supported by control bars and a handful of toolbars. 

The contents of control bars, ribbons and tool bars is dynamic; they respond to their context such that only those relevant to the window in focus, the command being run or the data that has been loaded are available. Windows and control bars also have context menus which open with a mouse right-click.

In addition to the above access methods, a 3D window can interpret quick key combinations and command names to access commands and options.

Note: This functionality can also be accessed using [scripts](<concept_studio%203%20scripting%20overview.md>) in conjunction with the Studio Application Object Model.

## The Find Command Screen

All processes and commands for your application are listed in alphabetical order in the Find Command screen. You can access this dialog by clicking the magnifying glass on the [Command](<Command_Toolbar.md>) toolbar. 

This screen shows the command name, a quick key (if one exists) and a description of the command. Select any command and click Run to execute it.

See [Find Command](<findcommand.md>)

## Quick Keys

Many design commands can be run using a quick key combination (such as "rd" for redraw-display, for example). This is a unique sequence of 2 to 4 keys. 

To run a command from a quick key, ensure that the focus is in a 3D window, then type out the keys (or do the same using a digital keyboard). All quick key assignments are listed in the command table and in the command's help page. 

Note: Pressing <ESC> while typing in a quick key will cancel a partially entered short cut key and remove it from the Status bar.

## Using the Command Toolbar

[![](../Images/tbCommand1.gif)](<javascript:void\(0\);>)

All processes and commands can be run by typing the command name or process into the Run Command field of the Command toolbar and clicking the Run Command ![](../Icon_Popups/icRunCommand.gif) button. All processes are listed on the Find Command screen (see above).

Previously run commands or processes can also be selected from the Run Command menu displayed by right-clicking the 3D window. 

All available commands and processes are listed in the [Command Tables](<../command_help/commandtable.md>).

Related topics and activities:

  * [Command Tables](<../command_help/commandtable.md>)