# Format Landmark Symbols

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

There are two types of drillhole overlay symbols; landmark symbols and [structural](<DHProp-format-structural-symbols.md>) symbols. 

The following activity describes how to display landmark symbols. These have a fixed location and represent key positions that identify the direction of the drillhole and how it is positioned with respect to a **[3D display section](<Sections.md>)**. Collar and end-of-hole positions, for example, are drillhole _landmark_ positions.

![](../Images/Drillhole_Symbols.gif)

Drillhole landmark points

This activity references controls in the **Symbols** command group of the [Drillholes Properties: Symbols](<Drillholes%20Properties%20Dialog%20\(Symbol%20Visual\).md>) screen.

Activity steps

  1. Display drillhole data in any 3D view and display the [Drillholes Properties: Symbols](<Drillholes%20Properties%20Dialog%20\(Symbol%20Visual\).md>) screen.
  2. To display a symbol at the **Collar** , **Section plane pierce point** , **Section plane entry and exit** or **End of hole** :

     1. Check the landmark position to display (you can display none or any).

     2. For each checked landmark symbol, specify the **Size**. 

     3. Choose how the size value will be interpreted using the menu to choose either _World_ (**Size** = world measurement units) or _Screen_ (**Size** = pixels).

**Note** : World-scaled symbols will scale with the view but Screen-scaled symbols will be shown at the same size regardless of the view magnification.

     4. Pick a **Symbol** to display:

        1. Choose a symbol collection using the menu provided. Symbol collections can vary between products. See **[Symbols](<../COMMON/Symbol%20List.md>)**.

        2. Pick a monochrome symbol.

     5. If required, choose a custom colour. If unchecked, the system default colour will be used.

        1. Check the **Color** box.

        2. Expand the colour menu to pick a colour.

  3. To display **Sample ticks** (the point at which a new core sample begins) or **Depth intervals** (markers at fixed distances down the hole):
     1. Check the appropriate item.
     2. Choose if the ticks or markers will appear to the _Left_ , _Centre_ or _Right_ of the drillhole. This represents the initial display; ticks or markers will rotate with the data if view changes are made.
     3. Choose how the size value will be interpreted using the menu to choose either _World_ (**Size** = world measurement units) or _Screen_ (**Size** = pixels).

     4. If defining **Depth intervals** , specify the distance between intervals using the **Every** field.

     5. Pick a **Symbol** to display:

        1. Choose a symbol collection using the menu provided. Symbol collections can vary between products. See **[Symbols](<../COMMON/Symbol%20List.md>)**.

        2. Pick a monochrome symbol.

     6. If required, choose a custom colour. If unchecked, the system default colour will be used.

        1. Check the **Color** box.

        2. Expand the colour menu to pick a colour.

Related Information and Activities

  * Format Landmark Symbols
  * [Drillhole Properties - General](<DH_PropDialog_General.md>)
  * [Drillhole Properties - Lines](<DHPropDialog_Segments.md>)
  * [Drillhole Properties - Labels](<DH_PropDialog_Labels.md>)
  * [Drillhole Properties - Columns](<DH_PropDialog_Columns.md>)
  * [Drillhole Properties - Associated Files](<Associated%20Files%20Dialog.md>)
  * [Drillhole Properties - Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)
  * [Drillhole Properties - Templates](<3D_Templates.md>)