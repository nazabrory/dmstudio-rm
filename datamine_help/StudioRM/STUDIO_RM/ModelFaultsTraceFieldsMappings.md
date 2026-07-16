# Map Trace Fields

To access this screen: 

  * Using the **[Model Faults](<ModelFaults.md>)** task, select **Set trace fields mapping**.

The **[Model Faults](<ModelFaults.md>)** tool automatically generates fault wireframes from loaded fault _trace_ data.

A fault trace is a string that represents the profile of a fault at a landmark position. Faults can be constructed using one or more traces. Higher trace numbers tend to produce more convoluted wireframe fault data. Digitize fault traces directly into an active **3D** window, and modify existing traces by extension and/or reversal.

The tool utilizes loaded trace data to form wireframe sheets through extrusion. This extrusion can be controlled either as a general value for all fault traces, or individually per fault trace, or a combination whereby individual fault trace dip and dip direction can set, whilst falling back to the default fault-level orientation if not specified.

Once fault data has been generated, edits to precursor fault traces can either be performed as a batch, then applied to regenerate all affected fault wireframe data, or wireframes will update in real time as traces are edited. 

You use this screen to specify which of your fault trace string attributes will contain dip and dip direction information, used to generate fault wireframe sheets from the trace vertices.

To map trace data attributes ready for fault modelling:

  1. Display the **Map Trace Fields** screen.
  2. Review the current field mappings and make edits as required:
     * _Fault ID_ \- this attribute value is used to distinguish one fault from another. This value is displayed in the **Fault ID** column of the **Faults** table (**Model Faults** screen) and also when setting inter-fault relationships using the **Starts on** and **Stops on** fields (**Model Faults** screen). 

Fault ID values are added to fault trace data and associated wireframe fault data.

Default = _FaultID_.

     * _Dip_ \- the dipping angle of a trace edge. This can be constant or variable throughout each string entity and appears in the **Traces** table of the **Model Faults** screen, where values can also be edited. An average dip value is also recorded in the generated fault wireframe object.

Default = _DIP_.

     * _Dip direction_ \- the dip direction of a trace edge. Can be constant or varied and is also editable using the **Model Faults** screen. An average dip direction value is also recorded in the generated fault wireframe object.

Default = _DIPDIRN_.

  3. Click **OK** to update fault trace field mappings.

Related Topics and Activities

  * [Model Faults](<ModelFaults.md>)
  * [Prepare Fault Data](<ModelFaults-Prepare-Fault-Data.md>)
  * [Edit Fault Traces](<ModelFaults-Edit-Fault-Traces.md>)
  * [Manage Fault Dependencies](<ModelFaults-Manage-Fault-Dependencies.md>)