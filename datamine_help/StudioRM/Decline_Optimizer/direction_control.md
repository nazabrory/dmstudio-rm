# Direction Control

To access these controls:

  * Display the [Decline Optimizer](<DeclineOptimizerDialog.md>) screen and select the **Path Control** tab.

Define the start and end azimuth values for a decline model, along with other parameters to control how path sections are oriented, and whether spirals are permitted.

Activity steps

  1. **Decline Optimizer >> Path Control** tab.

  2. Choose if the End of decline path is a straight line.

     * If **checked** , the path to the end point will be a straight line. 

     * If **unchecked** the azimuth of the end of the decline is modelled according to design string azimuth data at the end location.

  3. Decide if you want to Use Extended Path Types. 

If a partial turn to the left is designated _L_ and a partial turn to the right _R_ , and a straight segment _is S_ , then the 4 basic path types between two locations are (_LSL_ , _LSR_ , _RSL_ , _RSR_) and the remaining two path types are (_RLR_ , _LRL_).

If **checked** all 6 path types may be used. If **unchecked** only the four basic types are used (one turn cannot feed directly into another turn).

  4. The Min straight proportion option provides a method to control the proportion of the path that is straight segments. If Straight/(Straight+Curved, not spiral) < proportion then the proportion of straight segment is increased for a feasible path.

  5. Set the Initial Azimuth and the Final Azimuth of the decline in degrees. 

If an Azimuth Field Name is selected to specify the azimuth and there is a valid value at the start or end points this takes precedence over the Initial Azimuth and Final Azimuth options. If no attribute name is selected the azimuths of the decline are unconstrained.

  6. Decide if you want to Allow Spirals.

  7. Decide what type of search is performed when attempting to honour all decline constraints, including entry and exit points.

     * If Exhaustive Search is **checked** , a regularized search to sample azimuths on a fixed increment within the full 360 degree range is performed. In effect, this method will attempt to sample all possible azimuth combinations down the decline.

     * If Exhaustive Search is **unchecked** , a randomized search of entry and exit points is performed for each vertex of the decline string.

Note: An exhaustive search will take longer.

Related topics and activities

  * [Decline Optimizer Introduction](<DeclineOptimizerDialog.md>)