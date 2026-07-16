# DECLUST Process

To access this process:

  * Sample Analysis ribbon **> > Decluster >> Simple**.

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DECLUST** and click **Run**.
  * Enter "DECLUST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DECLUST>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

The **DECLUST** process declusters a set of sample data to reduce areas of high-density points. This can be useful where a more uniform distribution of points is required, such as when reconstructing a point cloud or adjusting sample density prior to estimation.

It is common practice to take more samples in high grade areas in order to improve the level of confidence in the estimation. However, when data are not on a regular grid then using the full data set will give a biased estimate of the mean, variance and histogram. In addition, clustered data can affect an indicator variogram.

**Note** : This process supports **[retrieval criteria](<../COMMON/Retrieval_Criteria_Overview.md>)**.

Declustering is the process of adjusting the full data set i.e. by removing or weighting data points in densely sampled areas, to give a more representative and evenly spaced set of samples. The **DECLUST** process provides two methods of doing this, with both methods requiring a regular 3D grid to be placed over the sample data. The two methods are:

  1. Sample Selection - select a single sample from each grid cell. 
  2. Declustered Weight - assign every sample a weight based on the number of samples in the grid cell

If the Sample Selection method is chosen then **DECLUST** provides a choice of four ways of assigning the value to the grid cell:

  1. Select a sample at random within each grid cell. A new random sample is generated for each run.
  2. Select a sample at random within each grid cell. The same 'random' sample is generated for each run.
  3. Select the sample nearest to the grid cell centre.
  4. Calculate the average value of all samples within the grid cell.

If the Declustered Weight method is chosen then the weight, **DCWEIGHT** , for a sample is calculated as:

`DCWEIGHT = NDATA / NCELLS / NPERCELL`

where:

  * **NDATA** is the total number of samples

  * **NCELLS** is the number of grid cells containing one or more samples

  * **NPERCELL** is the number of samples in the grid cell

The sum of the weights over all samples equals the total number of samples (**NDATA**). Therefore if a sample lies in a high density area it will have a weight of less than 1, and if it is in a low density area it will have a weight of more than 1. The output file from the Declustered Weight method can be used to transform data into a normal distribution, for input to the NSCORE or SGSIM processes.

One of the problems with the declustering method is that different grid sizes will generate different statistics. However, in general a regular grid about the size of the average sample spacing is suggested.

The process writes a summary table for each method to the [Output](<../COMMON/Output%20Control%20Bar%20Overview.md>) control bar.

  1. **Sample Selection** : shows statistical parameters for each numeric field in the output file. These statistics can be saved to a file if the **STAT_TBL** output file is specified.

  2. **Declustered Weigh** t: shows the declustered weight as a function of the number of samples per grid cell. These statistics can be saved to a file if the **WGTS_TBL** output file is specified.

**Note** : The process **DECLUST** has a limit of only being able to use input sample files with a maximum of 53 fields. If the process is run with an input sample file of greater than 53 fields, a warning message is displayed which prompts you to reduce the number of fields.  

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample data file. This must contain a set of 3D coordinates (eg X,Y,Z) and at least one other field. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Undefined |  Output file containing declustered samples. At least one of the two output files OUT or WTOUT must be selected.  
WTOUT |  Output |  No |  Undefined |  Output file containing declustered weights. This will be a copy of the IN file, but will also include the field DCWEIGHT. At least one of the two output files OUT or WTOUT must be selected.  
WGTS_TBL |  Output |  No |  Undefined |  Output file containing summary statistics for declustered weights.  
STAT_TBL |  Output |  No |  Undefined |  Output file containing summary statistics for declustered and clustered WTFIELD samples.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate of sample data |  IN |  Yes |  Numeric |  X  
Y |  Y coordinate of sample data |  IN |  Yes |  Numeric |  Y  
Z |  Z coordinate of sample data |  IN |  Yes |  Numeric |  Z  
WTFIELD |  Field to be used for calculating declustered weights. This is only relevant if a WTOUT file has been specified and one or more of the grade fields in the IN file contain absent data values. Specifying a WTFIELD field ensures that records containing absent data values for that field will be ignored. If a WTFIELD field is not specified but a WTOUT file has been selected then the Z field is used. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
METHOD |  Declustering method if OUT file specified: 1 = random selection within grid (different selection each run) 2 = pseudo random selection within grid (repeatable) 3 = nearest to grid centre 4 = average of samples within grid |  No |  1 |  1,4 |  1,2,3,4  
XGRID |  Grid size in X |  Yes |  Undefined |  0.00001,+ |  Undefined  
YGRID |  Grid size in Y |  Yes |  Undefined |  0.00001,+ |  Undefined  
ZGRID |  Grid size in Z |  Yes |  Undefined |  0.00001,+ |  Undefined  
XORIG |  X coordinate of grid origin |  No |  0 |  Undefined |  Undefined  
YORIG |  Y coordinate of grid origin |  No |  0 |  Undefined |  Undefined  
ZORIG |  Z coordinate of grid origin |  No |  0 |  Undefined |  Undefined  
CENTRE |  Flag to show whether the X, Y and Z coordinates of the grid centre should be included in the OUT file. If selected the names of the fields in the file will be XCENTRE, YCENTRE and ZCENTRE: |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !DECLUST &IN(sampleb),&OUT(dsampleb),&OUT(dcwts),  
  
---  
      
    
    *X(X),*Y(Y),*Z(Z),@METHOD=2,  
      
    
    @XGRID=10,@YGRID=10,@ZGRID=10,@XORIG=0,@YORIG=0,@ZORIG=0,@CENTRE=0  
      
    
       
  
## Error and Warning Messages

Message |  Solution  
---|---  
The input sample file has greater than 53 fields. |  Reduce the number of fields in the input sample file e.g. by using **[SELCOP](<selcop.md>)** or **[SELDEL](<seldel.md>)** to generate a new file.