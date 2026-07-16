![](../Images/HeaderCell.gif) |  Compositor/Digitizer Output Customizing Compositor and Digitizer Output  
---|---  
  
# Customizing Compositor and Digitizer Output

Assays in the compositor and digitizer windows are displayed to six decimal places by default.

## Changing assay format

  1. In the Loaded Data control bar, expand the assays table, select the field that you wish to format (Au, in the example below).

![](../Images/Format%20assay.gif)

  2. Open the Properties window, if not already open (right-click in toolbar area and select Properties).

  3. Select the Default Format field from the Properties window and choose a more suitable format from the pull-down. Au displayed to two decimal places in example below.

![](../Images/Format%20assay2.gif)

## Creating custom formats

If none of the formats in the Default Format pull down are suitable, it is easy to create your own, custom format. For instance, you may wish to display units as well as the value. The method is the same as above except, instead of selecting on the options from the Default Format property, type in your own format using the following simple rules.

  1. Start a custom format with "%".

  2. Define decimal places by a decimal point followed by a digit (defining the number of places); the number definition ends with the letter "f".

  3. Anything after the "f" is free typing and this can be the units such as % or g/t.

Example: To show a gold assay to three decimal places and with the units "g/t", you should type: "%.3f g/t".

![](../Images/Format%20assay3.gif)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Compositor tool](<Composite_Tool.md>)