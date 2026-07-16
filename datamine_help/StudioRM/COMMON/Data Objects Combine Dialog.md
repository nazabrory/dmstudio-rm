# Combine Data Objects

To access this screen:

  * In the [Data Object Manager](<Data%20Manager%20Dialog.md>), select Combine Objects

  * Run the command 'combine-data-objects' (quick key 'cdo')

  * **Data** ribbon **> > Objects >> Combine**.

Combine multiple objects into a single new object. All objects to be combined must be the same type (for example, they must all be block models, wireframes or strings and so on).

You can either merge data into a new object, or you can append one of the existing objects selected for combination. This is a useful way to extend an existing data object. For example, you could add a new closed string to a series of sectional zone interpretations as a result of new sample data.

To combine an object:

  1. Select the data Type . 

Select _< All>_ to later choose from any loaded data object, although clicking on any object in the displayed list will automatically filter it to show both the item selected and only other objects of the same data type.

  2. A list of all valid data objects displays in the left-hand list. Use -> to transfer data objects into the Combine List.

  3. The Combine List represents the data objects that will be merged. 

If you displayed the  Combine Data Objects dialog via the  Data Object Manager , the previously-selected object will already appear in the  Combine List automatically.

You can remove data objects from the Combine List using <-, if you need to.

  4. If you wish to specify a field that will be used to denote where the original data came from in the combined object, specify the field name in the Object Group Field area (or select an existing attribute). This field will be created in the new combined object.

If a group field isn't specified, data will be merged without additional attribution.

  5. When you have set up the Combine List as required, click OK to create the new object.

     * When combining objects, you will need to combine objects of the same data type. It is not possible, for example, to combine a drillhole and block model object, or a wireframe and string object. For this reason, when a new Type is selected, the Combine List is cleared, only allowing selection from a list of a particular data type, and only showing currently loaded data objects.
     * Objects are combined in a top-bottom order.

Remember that the new object is not saved as a physical file at this stage, nor data added to the project file. To do this, you will need to save the data file using the [Loaded Data](<Loaded%20Data%20Control%20Bar.md>) control bar or save the project file.

Related topics and activities

  * [Object Manager](<Data%20Manager%20Dialog.md>)

  * [Copy Data From](<CopyDataFromDialog.md>)