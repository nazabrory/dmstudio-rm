# Saving DirectX Models

You can create DirectX (.x) models from loaded wireframe models. These can then be used in simulations as "VR objects".

See [VR Objects and Types](<VR-Objects-and-Types.md>).

To save loaded wireframe data in .x format:

  1. Create or load wireframe data.

Note: The loaded wireframe can comprise one or more surfaces, but data to be exported must be a part of the same data object.

  2. Display the [Wireframe Properties: General](<Wireframe_Properties_Dialog.md>) screen.

  3. Check the Double Sided option. This is important for .x file exports.

  4. In the **Sheets** or **Project Data** control bar, right-click the wireframe overlay (any overlay of that object) and select **Data >> Export**.

The [Data Export](<../COMMON/ExportTable.md>) screen displays.

  5. Select the Driver Category _DirectX_ and the Data Type _Wireframe_.

  6. Click OK.

  7. Enter the file name to be created.

  8. Select the field that will represent the colour field in the output file.

  9. Click OK.

The DirectX file is saved.

Related topics and activities:

  * [Wireframe Properties: General](<Wireframe_Properties_Dialog.md>)

  * [VR Objects and Types](<VR-Objects-and-Types.md>)

  * [VR Objects and Simulations](<Objects_Simulation%20objects.md>)

  * [Mobile Simulation Objects](<Objects_Mobile%20objects.md>)