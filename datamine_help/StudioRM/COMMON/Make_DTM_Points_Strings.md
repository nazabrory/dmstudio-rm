# Make DTM: Select DTM Points and Strings

To access this wizard:

  * Click **Next** on the [General Options](<Make_DTM_General.md>) screen of the [Make DTM](<Make_DTM_Dialog.md>) wizard.

The Make DTM wizard is used to create a digital terrain model from loaded string or points data.

After [General Options](<Make_DTM_General.md>) have been defined, all the points and strings which will be used to produce the DTM can be selected. 

Where all the strings or points within an object should be used, the object can be selected within the Objects list. 

The pick button may also be used to select an entire object, by selecting the pick button, then selecting the object in a 3D view. 

With the Pick button deselected, individual strings or points can be selected using standard 3D view selection methods.

The Pick button should only be used for selected _complete_ objects and will toggle the corresponding check box in the the **Objects** list for any object clicked. To select individual items or aspects of an object, you will need to make sure that this button is disabled, and use the standard mouse-driven data selection in the **3D** window to ensure the relevant items are highlighted before continuing.

Note: If a separate limit string object is used, and it is required to contribute to the wireframe produced, it must be selected in the Select DTM Points and Strings dialog as well as in the Select Boundary Strings screen.

#### What happens next?

Click **Next** to display either:

  * The **Select Boundary** strings screen (if the **Use boundary strings** general option was previously checked), or;

  * The **Edit Attributes** screen (if the **Use boundary strings** general option was previously unchecked but **Attributes >> User defined** was checked, or;

  * The generated DTM (if both **Use boundary strings** and **Attributes >> User defined** were previously unchecked.

Related topics and activities

  * [Make DTM](<Make_DTM_Dialog.md>)

  * [Make DTM: General Options](<Make_DTM_General.md>)

  * [Make DTM: Select Boundary Strings](<Make_DTM_Boundary.md>)

  * [Make DTM: Edit Attributes](<Make_DTM_Attributes.md>)