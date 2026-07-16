![](../HeaderCell.jpg) |  Grade Estimation - Optimization Speeding up the grade estimation process.  
---|---  
  
# Run-time Optimization

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

Several features included in ESTIMA have been designed to minimize run time. Some of these are activated automatically whereas others are user controlled.

It is strongly recommended that estimation parameters are tested on a small model first. This may be either a representative subset of the full model or a model with a larger cell size and less cell splitting than the final model. Also for those features where there is a choice, always select a suitable approximation for the first test run.

## Sample Search

One of the most time consuming parts is the selection of samples within the search volume. A 'super-block' search algorithm has been implemented in order to minimize this part of the process.

There is no need to sort the Sample Data file on any particular field, because ESTIMA sets up its own indexes. However, it is necessary to ensure that the Input Prototype Model is sorted on IJK, or the process will terminate with an error message.

## Multiple Variables

The ability to estimate multiple variables in a single run of ESTIMA leads to a significant reduction in run times. If two or more grades are estimated using the same search volume and the same estimation parameters, then the incremental time for the second and subsequent grades is very small. Even if different estimation parameters are used there is still a time saving when estimating multiple grades.

## Discretisation Points

Cell discretisation points are used for the Inverse Power Distance, [Ordinary Kriging and Simple Kriging](<Grade%20Estimation%20Kriging.md>) estimation methods. The more points the longer the processing time but the better the cell representation. It is recommended that a small number of [discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>) points are used for test runs.

## Number of Samples

Processing time is also a function of the number of samples used for making each estimate. For methods such as [Inverse Power Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) and [Sichel’s t estimator](<Grade%20Estimation%20Sichels%20T%20Estimator.md>), the actual calculation involved is fairly small and so using a large maximum number of samples will only slow the process down in so far as the search time is increased. However, for kriging, each estimate involves solving a set of n simultaneous linear equations, where n is the number of samples used for the estimate.

The time taken to solve each set of n equations is approximately proportional to n2.

## Kriging Variance

Calculating the kriging variance involves calculating the geostatistical F value - the average value of the variogram in a cell. In order to do this the variogram function is called approximately n2/2 times, where n is the total number of discretisation points in the cell.

Obviously, this can be a time consuming operation if the number of points is large. Therefore, if the kriged variance is not going to be used in the presentation of reserves there is no point in calculating it. If a value for the VAR_F field in the Estimation Parameter file is not specified then the variance will not get calculated.

If the kriging variance is calculated, then ESTIMA stores the F value for a parent cell. Therefore, calculating the variance for a model which contains nearly all parent cells is not nearly as time-consuming as a model containing mainly sub-cells.

## Parameter @FVALTYPE

A time saving option has been included which allows the dimensions of a cell to be approximated by a discrete number of cell sizes. This is controlled by parameters @FVALTYPE and @FSTEP. Parameter @FVALTYPE takes one of the following values:

  * =1 \- the exact dimensions of the cell are used, and so the F value is calculated for every cell in the model, except the parent cell which is calculated just once.

  * =2 \- each cell is approximated to one of a discrete number of cells. As each cell is processed reference is made to a look up table to see whether the F value for that size cell has already been calculated. If it exists then the value is used; if not then it is calculated and stored in the table for future use. This gives a large speed improvement.

It is not possible to have @FVALTYPE=2 if the parent cell estimation with discretisation points within cells (@PARENT=2) has been specified. If this combination is specified, then @FVALTYPE will be reset to 1.

## Parameter @FSTEP

Parameter @FSTEP defines the step size which is used for approximating the dimensions of the cell. F values are stored for subcells whose dimensions are an integer multiple of the step size.

For example if @FSTEP=2, then any cell with dimensions in the range:

5 < XINC <_ 7, 1 < YINC <_ 3, 7 < ZINC <_ 9

would be approximated by a cell of dimensions 6 x 2 x 8.

If the dimension of a cell in one direction is less than half the step size, then it will be approximated by a dimension equal to the step size. Therefore in the previous example the criteria should really be stated as:

5 < XINC <_ 7, 0 < YINC <_ 3, 7 < ZINC <_ 9

As with discretisation points a test on a small part of the model should be carried out to find the effect of differing the step size. A step size of 1 will generally significantly improve processing speed without making any significant difference to the kriging variance.

![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Rotated%20Models.md>) (Grade Estimation of Rotated Models)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Introducing the Grade Estimation User Guide](<Grade%20Estimate%20Overview.md>)[  
Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>)[  
Grade Estimation Dynamic Search Volumes](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>)[  
Grade Estimation Octants](<Grade%20Estimation%20Octants.md>)[  
Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>)[  
Grade Estimation Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)[  
Grade Estimation Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>)[  
Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)[  
Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>)[  
Grade Estimation Additional Features  
Grade Estimation Variograms  
Grade Estimation Rotated Models  
Grade Estimation Output and Results  
Grade Estimation Parameter Summary  
Grade Estimation System Limits](<Grade%20Estimation%20Additional%20Features.md>)[  
Grade Estimation References  
  
ESTIMA command Help   
ESTIMATE command Help  
The Estimate dialog  
VARFIT Command Help](<Grade%20Estimation%20References.md>)