![](../Images/HeaderCell.gif) |  MSO - Global Settings Setting up high-level behavior for MSO  
---|---  
  
# MSO - Global Settings

### To access this dialog:

  * On the [Scenarios](<MSOv3_Scenarios.md>) panel, click Global Options.

This dialog is used to specify system-wide parameters for MSO, including how data files are managed throughout the workflow, and some general settings for the optimization solving engine.

Field Details:

Error Notifications: when generating runs, what should be done with existing data?

\- Prompt before overwriting

\- Silently overwrite without prompting (be careful with this one)

\- Silently backup and overwrite data without prompting

You may find the 2 'silent' options useful if you are planning to set a long list of runs for automatic starting \- these options will prevent the overall run generation process from being interrupted by user prompts related to the presence of existing data.

Solver Parameters

![](../Images/Warning.gif) |  You should be careful when changing MIP solver settings. If you are unsure or unfamiliar with linear programming solvers and their sensitivity to the listed input parameters, it is strongly recommended that you use only default settings.  
---|---  
  
Log File: this is the name of the generated log file. This log file is project-specific, and is stored within the "MSO_Output" sub-folder of your project. From there, it will be located within a folder of the scenario name to which it is relevant.

MIP Solver: this section deals with how the optimization engine performs during MSO usage. It can also be used to select an alternative solver to the LPSolve facility that is enabled by default.

On the basis that a linear programming model consists of an objective (grade or recovered metal), which is a linear equation that must be maximized or minimized (in MSO's case \- maximized). Then there are a number of linear inequalities or constraints that govern how a solution (an ideal stope shape) can be created.

MIP stands for "Mixed Integer (Linear) Programming". Mixed Integer Linear Programming problems are generally solved using a linear-programming based branch-and-bound algorithm..

Select a Solver from the drop-down list and then choose whether you wish to Pre Solve or not. If you choose [Auto] for the Pre Solve setting, this option will dictated by the type of input that is fed to the solver during run calculations.

Pre-solve is a preprocess of the solver model. It looks for ways to simplify it. For example, it can delete unused variables and restrictions, substitute fixed variable values by a constant and so on. The result is a new model that is less complex than the original model and (hopefully) gives rise to more rapid solution calculations.

With regards to Emphasis, you need to decide the ultimate goal of the solver. What does a solution have to be in order to be considered 'possible'?

By default, your solver will attempt to provide a 'balanced' solution, that is, one that respects both the feasibility of the solution and its optimality.

A linear program is infeasible if there exists no solution that satisfies all of the constraints \-- in other words, if no feasible solution can be constructed. Since any real operation that you are modelling must remain within the constraints of reality, infeasibility most often indicates an error of some kind. The source of infeasibility is often difficult to track down. It may stem from an error in specifying some of the constraints in your model, or from some incorrect numbers in your data.

Optimality is best described as 'narrowing the gap': once you have an incumbent (the best integer solution found at any point in the search for a solution), the objective value for this incumbent, assuming the original MIP is a maximization problem ( in MSO, it is), is a valid upper bound on the optimal solution of the given MIP. That is, we know that we will never have to accept an integer solution of value higher than this value. Somewhat less obvious is that, at any time during the branch-and-bound search we also have a valid lower bound, sometimes call the Bestbound. This bound is obtained by taking the minimum of the optimal objective values of all of the current leaf nodes. Finally, the difference between the current upper and lower bounds is known as the gap. When the gap is zero we have demonstrated optimality.

Bearing in mind the above, here are the remaining UI options:

Emphasis: controls trade-offs between speed, feasibility, optimality, and moving bounds in MIP. You have the choice of:

Balanced: balanceoptimalityandfeasibility. This will cause the selected solver to work toward a rapid proof of an optimal solution, but balancing that with effort toward finding high quality feasible solutions early in the optimization.

Feasibility: emphasize feasibility over optimality. This option will cause the solver to frequently generate more feasible solutions as it optimizes the problem, at some sacrifice in the speed to the proof ofoptimality.

Optimality: emphasize optimality over feasibility. When selected,less effort may be applied to finding feasible solutions early.

Bestbound: emphasize moving best bound. With this setting, even greater emphasis is placed on proving optimality through moving the best bound value, so that the detection of feasible solutions along the way becomes almost incidental.

HiddenFeas: emphasize finding hidden feasible solutions. With this setting, the optimizer works hard to find high quality feasible solutions that are otherwise very difficult to find, so consider this setting when theFeasibilityoption has difficulty finding solutions of acceptable quality.

Max Scenario Processing Time (hrs): set a maximum time limit for solution calculation. After the limit has been reached, the best solution will be presented (or no solution, if all outcomes are sub-optimal).

Gap Tolerance: sets an absolute tolerance on the gap between the best integer objective and the objective of the best node remaining. When this difference falls below the value of this parameter, the mixed integer optimization is stopped.

Integrality Tolerance: on some models, the integer solution returned by your solver at default settings may contain solution values for the discrete variables that violate integrality by a small amount. This parameter has a default value of 1e-5, which means that any discrete variable that violates integrality by no more than this amount will not be branched upon for resolution. For most model formulations, this situation is satisfactory and avoids branching that may be essentially meaningless, only consuming additional computing time.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [MSO Introduction](<MSOv3_default.md>)   
[Scenarios](<MSOv3_Scenarios.md>)