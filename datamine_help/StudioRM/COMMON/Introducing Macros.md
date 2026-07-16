# Introducing Macros

**Note** : this article is one of several covering the macro language in Studio products. Links to related topics and activities are at the end.

Your product incorporates a separate scripting and macro automation interface. This can be used to automate simple or complex tasks.

### What are Macros?

Macros access your product's meta language, a dedicated automation environment to automate [processes](<Studio%203%20Commands%20and%20Processes.md>) to mimic data workflows. 

In a simple sense, a macro can automate the task of running a process and filling in the various files, fields and parameters settings without displaying any user interface. More complex arrangements can include running multiple processes, using the output of one as an input to another and conditionally processing data based on certain conditions. You can even use macros to access operating system commands, read data from files, run macros from scripts and divert process output information to an external file.

**Note** : the macro facility is available in all Studio products.

Generally, macros will access physical files and process data to create information. This could be in the form of an output table or information in an output window, for instance. Macros work on physical file data, not data objects in memory, although you can use a combination of script commands (such as parseCommand, for example) to launch a macro (using the **[XRUN](<../Process_Help_XML/xrun.md>)** process, for example).

Macros are supported by [dedicated macro commands](<Studio%203%20Commands%20and%20Processes.md>). These commands are used to set up conditions, loops, subroutines and let you structure your macro more efficiently and logically, which is important when preparing complex automations that may need maintenance in the future.

### Creating a Macro

Processes and macro commands are written or recorded in text format as a macro file (*.mac). Potentially, macros can also be compiled into menu files, although this is outside the scope of this topic series. Commonly, a macro recording facility is available via your application's Home ribbon, although this will depend on the product you are using. If you are unsure where to find your macro functions, please contact your local Datamine office.

**Note** : The information presented here is a brief introduction to macro writing in Studio products. There is a lot more to learn, including how to validate, debug, set up error trapping and much more. A dedicated eLearning course is available on the Datamine eLearning platform that provides a more in-depth view of the powerful macro language.

Related topics and activities

  * [Macro Writing Rules and Restrictions](<Introducing%20Macros_Restrictions.md>)

  * [Accessing Commands and Processes](<Studio%203%20Commands%20and%20Processes.md>)

  * [Automating Studio Products](<concept_studio%203%20scripting%20overview.md>)