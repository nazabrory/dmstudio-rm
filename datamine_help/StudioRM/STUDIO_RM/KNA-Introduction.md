# Kriging Neighbourhood Analysis

Kriging Neighbourhood Analysis (KNA) is an important step in geostatistics, particularly in grade estimation for geological block models. The primary goal of KNA is to optimize the parameters used in kriging to ensure that the block model's grade estimates are both accurate and reliable.

**Note** : Studio RM supports both Ordinary Kriging (OK) and Simple Kriging (SK) estimation methods, plus others. See [Advanced Estimation & Variography](<Multivariate_Introduction.md>).

These are the main components of a typical KNA study, and an explanation of why this type of analysis can be useful:

Block Model and Kriging

  * **Block Model** A geological block model is a 3D representation of the subsurface, divided into smaller blocks (or cells), each of which has properties like grade (e.g., concentration of a mineral).

  * **Kriging** Kriging is a geostatistical method used to estimate the unknown grade of each block based on known sample points around it.

The Role of "Neighbourhood"

The kriging algorithm uses surrounding sample data (the _neighbourhood_) to estimate the value for each block in the model.

KNA focuses on how to define this neighbourhood to get the most accurate estimation. This involves determining how many samples to include, how far those samples should be from the block being estimated, and how they should be weighted.

Key Parameters Optimized by KNA

KNA helps optimize several important parameters, including:

  * **Search Radius** This defines the maximum distance around the block to search for sample data. If the radius is too large, you might include irrelevant samples. If its too small, you might exclude useful data.

  * **Number of Samples (or Neighbours)** The ideal number of nearby samples to include in the estimation. Too few samples might give unreliable results, while too many can dilute the relevance of closer samples.

  * **Block Discretization** Refers to dividing the block into smaller sub-blocks during estimation. This improves the precision of the kriging algorithm.

  * **Anisotropy and Variogram Model** KNA takes into account the directional continuity of grades (anisotropy) and the variogram, which describes how grade values are correlated with distance.

### Why KNA is Important

KNA is used to facilitate the following:

  * **Accuracy** By optimizing these parameters, KNA ensures that the kriging estimates are as accurate as possible, leading to more reliable grade estimations.

  * **Reducing Bias** Proper neighbourhood definition prevents over-reliance on either too few or too many data points, which could otherwise bias the results.

  * **Efficiency** It helps avoid computational inefficiency by preventing unnecessary calculations using distant or redundant samples.

### KNA Outcome

The result of KNA is a set of optimized kriging parameters that provide the best balance between accuracy and computational efficiency, ensuring that the geological block model gives reliable and realistic grade estimates.

In summary, KNA is a process to fine-tune the kriging estimation method by choosing the best neighbourhood of samples for each block. This ensures that the grades in the block model are estimated with high precision and minimal bias.