# Print to PDF (Scripting)

If you have a software PDF printer driver installed (if using Windows 10 or later, you will have one installed with your operating system), you can output any plot sheet as a PDF document using the [Project menu](<Ribbon_File_Button.md>)'s Print option.

See [Automating Studio Products](<concept_studio%203%20scripting%20overview.md>).

Once a Studio application object has been instantiated, a method on the **DmProject** interface can be used to specify the name of the plot sheet to print and the output destination of the PDF document.

For example, in the following Javascript snippet, the active project's "From 3D" plot sheet is exported to "C:\Database\MyProject":
    
    
    oDmApp.ActiveProject.PrintPlotSheetToPDF("From 
    	 3D", "C:\\Database\\MyProject\\MyPrintout.pdf", "");

The comma-delimited parameters supporting PrintPlotSheetToPDF() are:

  1. "From 3D" The name of the Plot Sheet of the target project, in quotes
  2. `C:\\Database\\MyProject\\MyPrintout.pdf ` The fully-qualified path to the output PDF document, in quotes
  3. "" (Optional) the name of the PDF printer driver to use when creating the image document. If not specified (as in the example above), the default PDF printer for your system will be used.

Related topics and activities

  * [Automating Studio Products](<concept_studio%203%20scripting%20overview.md>)

  * [The Project Button](<Ribbon_File_Button.md>)