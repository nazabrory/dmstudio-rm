# Creating a Polygon

This section introduces many of the ideas behind scripting, and develops a useful example, step by step. You will be developing a new interface with text boxes and buttons, and adding the script.

Note: In this example, you will use Studio's 'safe' method of ActiveX instantiation, as calls to new `ActiveX()` aren't a safe mechanism.

Your application contains a handy process called CONPOL, for finding the convex hull around a set of points. The script developed in this tutorial integrates the CONPOL process with the 3D Window, so that any selection of the point and string data currently in the 3D Window can be passed to CONPOL, and the resulting polygon loaded back into the 3D Window. The script processes X and Y coordinates, i.e. it works in a plan view.

You may either create some point data in the 3D window or use the specially created file for the example.