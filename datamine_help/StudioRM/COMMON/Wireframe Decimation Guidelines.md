# Wireframe Decimation

Wireframe decimation reduces data by simplifying edge and wireframe faces based on criteria. However, its crucial to balance data size and accuracy to avoid losing meaningful wireframe information.

### Decimation Guidelines

  * The verification process should always be run before a wireframe is decimated, using the [Wireframe Decimate](<Wireframe%20Decimate%20Dialog.md>) screen.

  * You can only verify entire wireframe data objects \- it is not possible to verify a subset of a wireframe object.

  * When running a pre-decimation verification, the Remove Duplicate Vertices option should be selected.

  * The Maximum Error and Percentage Reduction options are key to a successful decimation; in most cases, it is advised to use a Maximum Error instead of a Percentage Reduction. A sensible value for the former will normally preserve important features, whereas the latter will use a less elegant (although quicker) algorithm in order to achieve the expected data reduction.

  * The best Maximum Error value will vary greatly depending on the context of the wireframe (e.g. topologies may be able to cope with large errors, but an engineering design may not). It is for this reason that **Maximum Error** is not specified by default, even though it it preferred.

Regardless of how the command is initiated, the parameters controlling verification are entered using the [Wireframe Verify](<Wireframe%20Verify%20Dialog.md>) screen. Verification can include, with or without tolerance values, a check for open edges, shared edges and/or crossover areas. You also have the option to remove duplicate vertices and/or faces when these entities are intercepted.

Related topics and activities

  * [Decimate Wireframe](<Wireframe%20Decimate%20Dialog.md>)

  * [Clean Wireframe](<Wireframe%20Clean%20Dialog.md>)

  * [Verify Wireframe](<Wireframe%20Verify%20Dialog.md>)