# Browsing and Copying

In this lesson we use the Project File Browser to browse for files. The browser is the graphical interface into your project. It is an ActiveX control, which means that it is a software component that can be attached to either your application, or independently to a script that you create.

Note: In this example, you will use Studio's 'safe' method of ActiveX instantiation, as calls to new `ActiveX()` aren't a safe mechanism.

[![](../Images/Studio3%20Scripting%20File%20Browser%200001.jpg)](<javascript:void\(0\);>)

The following exercises can be used to create a script to copy a file with optional retrieval criteria (instructions to refine how the selection takes place).

It uses the Project File Browser which is a part of the Datamine Application Object.

This example can easily be extended to carry out any file processing along the way, or for example to create a script that reads multiple input files and creates one or more output files.