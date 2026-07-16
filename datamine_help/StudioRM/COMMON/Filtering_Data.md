# Filtering Data

A _filter_ is a mechanism for separating a subset of information from the whole data set, such that only the data you wish to load, display or process, is available; the rest is ignored. Being object-based, your Datamine application is not as dependent on filters as earlier versions, but there are still many occasions where filtering is desirable.

When an object 'passes' a filter, it is available for further processing, evaluation or display.

A filter is a mechanism for separating a subset of information from the whole set of data, such that only the data you need to load, display or process, is available; the rest is ignored. 

Filters can operate at several different levels in your application:

  * Data can be filtered as it is loaded or reloaded in to memory. This actively prevents data from being loaded into memory, so the application never 'receives' it.

This is referred to as **load filtering**.

  * An object (data in memory) can be filtered such that only a part of the object is used in certain commands. The filtered information isn't lost; it is just temporarily excused from further processing, unless you instruct otherwise.

This is often called **in-memory filtering** or **object filtering**.

  * An object type, individual object or all loaded objects can be filtered such that only part of the data is displayed e.g. in the 3D (any), Plots, Tables or Reports windows.

This is commonly called **view filtering**.

### Load Filtering

Datamine binary format files (,dm, .dmx) can be filtered as they are loaded from the Project Files control bar, by holding CTRL when dragging file references into a 3D window. This screen lets you pick the field(s) to be loaded and to constrain loading using a filter expression. See [Expression Builder](<Expression%20Builder%20Dialog.md>).

### In-memory Filtering

Once data is loaded, objects can be filtered using other filtering commands. In-memory filtering is also referred to as _object filtering_. Filters are applied temporarily, 

For example, you could use the Filter All Objects commands to filter multiple objects of the same object type, which contain a shared custom attribute, say, an underground mine design consisting of separate string models for development and stoping, with a work area attribute (e.g. LEVEL=127)

These are typically found on the Format ribbon but can also be accessed using commands, including:

  * [filter-all-drillholes](<../command_help/filter-all-drillholes.md>)

  * [filter-all-model-files](<../command_help/filter-all-model-files.md>)

  * [filter-all-objects](<../command_help/filter-all-objects.md>)

  * [filter-all-planes](<../command_help/filter-all-planes.md>)

  * [filter-all-points](<../command_help/filter-all-points.md>)

  * [filter-all-strings](<../command_help/filter-all-strings.md>)

  * [filter-all-wireframe-triangles](<../command_help/filter-all-wireframe-triangles.md>)

  * [filter-drillhole-off](<../command_help/filter-drillhole-off.md>)

  * [filter-drillholes ("fdh")](<../command_help/filter-drillholes.md>)

  * [filter-model-file ("fm")](<../command_help/filter-model-file.md>)

  * [filter-objects ("fob")](<../command_help/filter-objects.md>)

  * [filter-planes ("fln")](<../command_help/filter-planes.md>)

  * [filter-point-off ("nfp")](<../command_help/filter-point-off.md>)

  * [filter-points ("fp")](<../command_help/filter-points.md>)

  * [filter-string-off ("nfs")](<../command_help/filter-string-off.md>)

  * [filter-strings ("fs")](<../command_help/filter-strings.md>)

  * [filter-wireframes ("fww")](<../command_help/filter-wireframes.md>)

  * [filter-wireframe-triangles](<../command_help/filter-wireframe-triangles.md>)

You can also filter in-memory data using the **Data Object Manager** , which permits a filter expression to be specified and applied to all loaded data.

### Filter Expressions

Filter expressions can be applied in various places of your application, including when loading data and managing in-memory data. The [Expression Builder](<Expression%20Builder%20Dialog.md>) can be used to construct these filters, using [logical expression syntax](<logical%20expressions.md>). 

These expressions can be saved, using the **Quick Filter** control bar and applied to other loaded data objects of the same type. See [Quick Filter Control Bar](<Quick%20Filter%20Dialog.md>).

Related topics and activities

  * [Logical Expressions](<logical%20expressions.md>)

  * [Expression Builder](<Expression%20Builder%20Dialog.md>)

  * [Logical Expressions](<logical%20expressions.md>)

  * [Data Object Manager](<Data%20Manager%20Dialog.md>)

  * [Quick Filter Control Bar](<Quick%20Filter%20Dialog.md>)