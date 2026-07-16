# Studio RM 3.0.1 Release Notes

This is a hot fix patch for the previous 3.0 version and includes important fixes and improvements.

## All Improvements

### Commands & Processes

  * STUDIO-7314 A MERGEEST parameter has been added to COKRIG to control whether estimations are merged prior to an estimation run, or calculated separately.

  * STUDIO-7314 COKRIG now completes more quickly when grade capping is applied.

  * STUDIO-7296 A "Use search distance anisotropy" check box, checked by default, is now available for the Nearest Neighbour estimation method.

  * **CORE-9530** You can now choose if files in project subfolders are converted to the default file format on project launch.

  * **CORE-9460** Saving block model data to the project is now much quicker.

### Automation

  * STUDIO-7319 You can now set the name of an output boundary string object with the **Create Vein Surface** command (OutputBoundaryFile=ObjectName).

## Defect Fixes

  * **CORE-9575** An issue causing TRIFIL to corrupt input data if forcibly closed early has been resolved.

  * **CORE-9541** An issue causing SLIMOD to fail with .dmx inputs has been resolved.

  * **STUDIO-7302** An issue causing slow loading of a prototype model via COKRIG (and Advanced Estimation) has been resolved.

  * **STUDIO-7291** When using dynamic anisotropy with COKRIG, the calculated TMINDIST field no longer uses the static ellipse given by the spar file, but instead of the dynamic orientation coded into the model by the DA workflow, as expected.
  * **STUDIO-7261** Average Distance is now properly calculated when using Unfolding in COKRIG.

  * **STUDIO-7260** An issue preventing KNA from displaying expected results in Advanced Estimation has been resolved.

  * **STUDIO-6471** An issue preventing the display of some variograms directions in the Fit tool has been resolved.

  * **CORE-9507** An issue causing INPDDF to incorrectly generate a Datamine wireframe from Leapfrog ASCII data input, has been resolved.

  * **CORE-9462** Loading data objects no longer incorrectly flags them as modified, triggering unnecessary save data prompts on closedown.

  * **CORE-9501** Files created by the DMtoDMX conversion utility can now be loaded into Datamine Supervisor.

  * **CORE-9444** An issue causing clip-strings-to-wireframe to fail on some data has been resolved.

  * **CORE-9357** WIREFILL now correctly interprets default plane information, and a @PLANE parameter is added to allow behaviour override.

  * **CORE-8052** An issue causing SAMPOUT to be created incorrectly when writing alphanumeric fields has been resolved.