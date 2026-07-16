# MDEBUG Macro Command

Provides an interactive source code debugger for the development and testing of macros and menus.

The facility provides features similar to that found in a computer language debugger. **MDEBUG** is implemented as a soft command and can be accessed in the following ways: 

  1. At the **[PROMPT](<prompt.md>)** input command by typing `!MDEBUG`.

  2. As an inline command within a macro or menu 

**MDEBUG** passes control to the macro debugger and displays the current line number. **MDEBUG** will display the current line and the action that caused execution to pause at that line. One of three states will be indicated: 

  1. A BREAKPOINT has been previously set, and control has paused at a breakpoint. 

  2. The STEP command has previously been entered from **MDEBUG** , and control has paused at the next command line. 

  3. An inline **MDEBUG** command has been read from the macro or menu. 

Note: **MDEBUG** can be exited with the `PROCEED` and `STEP` commands. Entering `!` or `RETURN` is accepted as a `PROCEED` command.

**MDEBUG** permits the execution of the following debug commands. Commands can be abbreviated (to one character as each command starts with a unique letter). 

  * `ASSIGN <stack variable> <string>`   

Assigns value of <string> to <stack variable>. <stack variable> need not already exist. 

  * `BREAKPOINT <label>  
BREAKPOINT <line>  
BREAKPOINT`   

Set breakpoint at <label>, <line> or list all breakpoints currently set. 

  * `CLEAR <label>  
CLEAR <line>  
CLEAR +`   

Clear breakpoint set at <label>, <line> or all breakpoints currently set. 

  * `DELETE <stack variable>`   

Delete <stack variable>. 

  * `EXECUTE <full command string (as in a macro)>`   

Execute a command. The full command syntax is required. eg. LIST &IN(myfile). 

  * `FIND <string>`   

List all lines in current macro which contain <string>. 

  * `HELP` Show these comments. 

  * `INFO` Display a summary of the stack file. 

  * `LIST  
LIST n1  
LIST n1 n2  
+  
-`   

List lines near current position, about line n1 or lines n1 to n2 of the current macro. The initial number of lines listed to the screen as a page is 21. If the command 'List n1 n2' is used, the number of lines listed as a page defaults to n2-n1+1. To list to the end of file use the command 'List n1 +'. The command '+' increments the lines listed to the next page, and command '-' decrements the lines listed to the previous page. 

  * `PROCEED  
PROCEED <label>  
PROCEED <line>`   

Continue processing from the current line, the line with <label>, or <line>. 

  * `REVIEW`   

Review commands held on the stack. 

  * `STEP`   

Execute the current command and break at the next at the next command. 

  * `TYPE <stack variable>  
TYPE +  
TYPE`   

Show current value of <stack variable>, or all variables. 

Related topics and activities:

  * [PROMPT](<prompt.md>)