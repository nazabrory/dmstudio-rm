# CSOWOPT Process

To access this process:

  * **Simulate** ribbon **> > Conditional Simulation >> Ore Waste**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CSOWOPT** and click **Run**.
  * Enter "CSOWOPT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CSOWOPT>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

This process identifies ore and waste blocks in a conditionally simulated model by minimizing the cost of incorrectly classifying ore as waste or waste as ore. 

Reserves are calculated for a range of costs and prices for each cutoff, allowing the sensitivity of the reserves to changes in these parameters to be quantified.

The **CSOWOPT** process carries out the following functions:

  * Inputs a conditionally simulated block model statistics file as created by [CSMODEL](<csmodel.md>).
  * Inputs a range of processing costs and metal prices as defined by a minimum value, maximum value and increment. A single cost or price is selected by setting the minimum equal to the maximum.
  * Calculates whether each block is ore or waste by minimizing the cost of misclassifying ore as waste or waste as ore for each combination of cost, price and cutoff.
  * Creates a reserves table of tonnes and grade classified by cost, price and cutoff.
  * Creates an output model identifying ore and waste blocks for each cutoff. This model is only created for the minimum cost and minimum price values

## Input STATMOD Mode

This model must have been created as the output **STATMOD** model by the [CSMODEL](<csmodel.md>) process. Details of the fields in this model are given in the description for [CSMODEL](<csmodel.md>). The fields used by the **CSOWOPT** process are;

  * the 13 standard model fields **(IJK** , **XC** , **XINC** , **NX** , **XMORIG** , etc)
  * **MEAN** : the mean grade for all realizations.
  * **PAx** : the probability that the grade of the cell exceeds cutoff x.
  * **GAx** : the grade of the cell above cutoff x.
  * **GBx** : the grade of the cell below cutoff x.

## Method

The decision as to whether a block is ore or waste is usually made by comparing the estimated grade of the block with a cutoff grade. There are four possible consequences of this decision:

  1. The true grade of the block is above cutoff and the block is sent to the mill
  2. The true grade of the block is above cutoff and the block is sent to the waste dump
  3. The true grade of the block is below cutoff and the block is sent to the waste dump
  4. The true grade of the block is below cutoff and the block is sent to the mill

The method used by **CSOWOPT** minimizes the cost of misclassifying ore and waste, cases 2 and 4 above. If the costs of mining ore and waste are equal, then the value of a block can be defined as:
    
    
    Value = Revenue - Cost

where:

  * Revenue = Mill Recovery (R) * Price (P) * Grade (G)

  * Cost = Cost of Mining and Milling (C)

So:
    
    
    Value = R*P*G - C

There are two types of value, potential and actual:

  * The potential value of a block is the value of the block if the correct decision is made. 
  * The actual value of a block is the value of the block given the decision that was made.

The loss in value due to the decision is then the actual value minus the potential value. For cases 1 and 3 the actual and potential values are the same, so there is no loss due to the decision. However cases 2 and 4 give the following loses:

  * Ore sent to waste dump: loss of potential value i.e. `-(R*P*G - C)`
  * Waste sent to mill: actual difference between revenue and cost i.e. `R*P*G - C`

Since the grade G is actually a random variable, not a constant, there is a probability p that the grade is above cutoff. Therefore:
    
    
    Total loss = (1-p) * (R*P*G - C) - p * (R*P*G - C)

This can be expressed as:
    
    
    Expected loss = (1-p) * (R*P*GB - C) - p * (R*P*GA - C)

where GA is the grade above cutoff and GB the grade below cutoff.

A block is sent to the mill if the expected loss as a result of this decision is less than the expected loss from sending the block to the waste dump. The breakeven point occurs when the two loses are equal, which is when:
    
    
    (1-p) * (R*P*GB - C)= -p * (R*P*GA - C)

Solving this for p gives:
    
    
     p  =  (GB - C/(R*P)) /  (GB - GA) 

The probability that the block exceeds the cutoff grade is stored in field **PAx** in the input **STATMOD** model for cutoff x. The GA and **GB** values are also stored in the model as fields **GAx** and **GBx** respectively. Therefore by comparing the value of probability p with the value of **PAx** , the decision can be made as to whether the block should be classified as ore or waste:

  * if **PAx** > p, then the block is classified as ore
  * if **PAx** < p, then the block is classified as waste

## Prices and Costs

Parameters **COSTMIN** , **COSTMAX** and **COSTINC** allow a range of processing costs to be specified. Cost includes both the mining and milling cost; it is assumed that mining cost is the same for ore and waste. Reserves are calculated for each cost **COSTMIN** , **COSTMIN** +1* **COSTINC** , **COSTMIN** +2* **COSTINC** , etc while the value is less than or equal to **COSTMAX**. If only a single cost is required then **COSTMAX** should be set equal to **COSTMIN** , or just left blank. Prices are specified in a similar way using parameters **PRICEMIN** , **PRICEMAX** and **PRICEINC**.

Care should be taken with the units in which costs and prices are specified. If the original grade units were in g/t then the fields GAx and GBx will also be in g/t. Then the cost should be in currency/t ( and the price should be in currency/g. If the grade units are % then prices should be multiplied by 0.01. 

Grade| Cost| Price| Price Multiplying Factor| Comment  
---|---|---|---|---  
g/t| $/t| $/g| 1|   
%| $/t| $/kg| 1/100 = 0.01| Adjust for %  
%| $/t| $/lb| 2204/100 = 22.04| Adjust for % and  
2204 lbs / tonne  
  
For example, if the metal price is 0.80 $/lb then the price value entered should by 0.80 * 22.04 = 17.632

## Output OREMOD File

The output **OREMOD** file is a block model containing the 0/1 flags for each cutoff showing whether the cell is waste/ore for that cutoff. **MEAN** is the mean grade of the cell averaged over all realizations, and **VARIANCE** is the grade variance over all the realizations. Note that the model is only calculated for the minimum cost (**COSTMIN**) and minimum metal price (**PRICEMIN**). These two values are saved as implicit fields (not stored explicitly) in the model data definition. If you want to create the model for a cost and price value that are not the minimum, then you will need to rerun the process for just a single value of cost and price.

Field| Stored| Description  
---|---|---  
IJK| Yes| IJK index  
XC| Yes| X coordinate of centre of parent cell  
YC| Yes| Y coordinate of centre of parent cell  
ZC| Yes| Z coordinate of centre of parent cell  
XINC| Yes| Parent cell size in the X direction  
YINC| Yes| Parent cell size in the Y direction  
ZINC| Yes| Parent cell size in the Z direction  
MEAN| Yes| Arithmetic mean grade  
VARIANCE| Yes| Variance  
OR0| Yes| 0/1 flag showing waste/ore for cutoff 0  
OR0.5| Yes| 0/1 flag showing waste/ore for cutoff 0.5  
....| ....|  ....  
OR9| Yes| 0/1 flag showing waste/ore for cutoff 9  
XINC| Yes| Parent cell size in the X direction  
YINC| Yes| Parent cell size in the Y direction  
ZINC| Yes| Parent cell size in the Z direction  
XMORIG| No| X origin of model  
YMORIG| No| Y origin of model  
ZMORIG| No| Z origin of model  
NX| No| Number of parent cells in the X direction  
NY| No| Number of parent cells in the Y direction  
NZ| No| Number of parent cells in the Z direction  
COST| No| Mining/milling cost (COSTMIN)  
PRICE| No| Metal price (PRICEMIN)  
  
## Program Limits

Maximum number of costs = 30  
Maximum number of prices = 30  

## System Files

  * **_csolog.txt** \- Log file. Only useful if there is a problem.

  * **_cso_*.txt** \- Temporary system files. These will be deleted if the process terminates cleanly. 

  * **_sp*.dm** \- Temporary Datamine files. These will be deleted if the process terminates cleanly.

All files matching the template _cso_*.txt and _sp*.dm are deleted as the process terminates. Therefore you should not use any of these file names for your own work.

## Input Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
STATMOD| Conditionally simulated block model statistics file. This file will have been created as the output STATMOD file by CSMODEL, and must include the fields PAx, GAx and GBx for at least one value of cutoff grade x.| Input| Yes| Block Model  
  
## Output Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
RESERVES| Output| Yes| Table| Output reserves file containing total tonnes and grade for blocks calculated as ore, classified by processing cost, metal price and cutoff.  
OREMOD| Output| No| Block Model| Output block model. This file includes flag field OWx which equals 1 if the block is ore and 0 if it is waste, for each cutoff x, for processing cost COSTMIN and metal price PRICEMIN .  
PLOT| Output| No| Plot| Template name for output plot file(s) showing tonnes, grade and/or metal above cutoff (Y axis) against cutoff (X axis). The PLOT file template name should be a maximum of 23 characters. A single character is added to this name to create the actual file name, as follows: G - Grade T - Tonnes M - Metal The parameters GPLOT , TPLOT and MPLOT define which plots to create. A minimum of 2 cutoffs must have been defined in order for the PLOT file(s) to be created.  
  
## Example
    
    
    !CSOWOPT    
  
---  
      
    
    &STATMOD(statmod1),&RESERVES(reserve2),&OREMOD(oremod1),  
      
    
    @COSTMIN=30,@COSTMAX=40,@COSTINC=10,  
      
    
    @PRICEMIN=10,@PRICEMAX=12,@PRICEINC=2,  
      
    
     @RECOVERY=90,@DENSITY=2.5  
  
Related topics and activities

  * **[CSMODEL Process](<csmodel.md>)**