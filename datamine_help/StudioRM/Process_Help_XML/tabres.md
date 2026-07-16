# TABRES Process

To access this process:

  * **Report** ribbon **> > Report >> Calculate Reserves**
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, select **TABRES** and click **Run**.
  * Enter "TABRES" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TABRES>).

## Process Overview

Produces reserve tabulations from a results file produced by other processes (for example, [MODRES](<modres.md>).) or interactive evaluation of a block model or drillholes using perimeters or wireframes.

Several different types of reserve reports may be produced, as chosen interactively. A single execution of **TABRES** produces the chosen table.

The input results file defines the details that may be produced. For example, if there are no grade intervals in the results file, then no grade interval reports are available.

A maximum of five grades may be reported at once, although there may be more than five grades in the results file. The user may choose up to five to be reported at any time. Note that grade intervals (if any) refer to the main grade, which is the one reported first. Even if the main grade should not be among those reported in **TABRES** , grade intervals will still refer to this field.

The process carries out an internal sort so that plane **NUMBER** s are always reported in ascending order, regardless of the order of records on the results file. In general the process works regardless of record order; but in case of problems, sort the file on fields **NUMBER** , **PERIMID** , **SEQUENCE** ,<rocktype>. **PERIMID** s may be the same provided they have a different **SEQUENCE** or **NUMBER**.  
  
>The **SEQUENCE** field is used by **[MODRES](<modres.md>)** to differentiate sets of perimeters on the same bench. Thus, to obtain results for a single pit extension where there are several in the same results file, use retrieval criteria on **SEQUENCE**.

### Classification by Ore, Waste etc.

The results file may contain a rocktype field which classifies the records by rocktype. This classification may be either by given values of the field, or by a set of standard classifications which are ORE, WSTE, AIR, S1, S2, S3, S4, S5, S6 and S7. If this latter was chosen when the results file was established then it is possible to use this classification in the reports and for stripping ratio calculations. In this context, waste is assumed to be everything which is not classified as ORE.

However, if no such classification is available in the results file, it is still possible to classify into the two categories ORE and WSTE by use of a cut-off grade. All material which is above the given cut-off will be classified as ORE; all material which is below or equal to the cut-off will be classified as WSTE.

If ORE, WSTE, etc. classification is available, and a cut-off grade is also specified, then this is used to re-classify ORE material into WSTE if the value of the main grade is below or equal to the cut-off given. No other classifications are affected.

Classification by use of the cut-off will be carried out on the mean main grade within each grade interval; or, if there are no grade intervals, on the overall mean main grade. Note that this could give rise to some inaccuracies if the cut-off specified does not correspond to the grade interval boundaries.

### Planes

The results file may contain records for any number of the four recognized PLANE identifiers **LEVEL** , **COLUMN** , **ROW** or **SECTION**. However, **TABRES** operates on records from a single plane at a time, and ignores all others. The default plane is **LEVEL** ; this may be changed during interaction.

### Reports

The standard reports are as follows:

  1. Summary for each plane. A single line is produced for each plane, showing the total volume and tones mined and the mean of each grade evaluated. Totals over all planes are shown.

  2. Summary for each perimeter. A single line is produced for each perimeter, showing the total volume and tones mined and the mean of each grade evaluated. Totals over all perimeters are shown.

  3. Summary for each perimeter and each plane. A single line is produced for each perimeter in each plane, showing the total volume and tones mined and the mean of each grade evaluated. Totals are also shown for each plane and overall.

  4. Full report. For each rocktype within each perimeter within each plane, a page is produced showing the total volumes and tones mined by grade interval (if any). A cut-off grade table is also produced. Totals are shown for all rocktypes within each perimeter, for all perimeters within each plane, and for all planes.

  5. Ore and waste summary for each plane. For each plane a page is produced showing mean grades for ore, waste and other classifications. These classifications may be either by use of a rocktype field in the results file showing ORE, WSTE, S1-S7 values, or by a cut-off grade which is applied to the main grade value, or by both simultaneously. Stripping ratios (volumetric and tonnage) are calculated, and a cut-off grade table is also shown. Totals over all planes are shown.

  6. Ore and waste summary for each perimeter. This report has the same format as 5 above, but results for each perimeter are reported. Totals over all perimeters are shown.

  7. Ore and waste totals. This is a single page showing the totals over all evaluations, with mean grades for each classification ORE, WSTE etc. It is the total page produced by reports 5 or 6 above.

  8. Full report, as in 4 above, for ore; but summaries for all non-ore rocktypes. This report is similar in form to 6 above, but with the extra detail for ore, where all grade intervals are reported.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
RESULTS |  |  Input |  Yes |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  >=1 : print all tables, even if volumes are zero. Default is omit zero tables (0). | No | 0 | 0,1 | 0,1  
  
## Example
    
    
    !TABRES &RESULTS(PITRESLT)  
  
---  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> NOT A VALID RESULTS FILE <<< >>> FIELD nnnnnnnn MISSING OR WRONG TYPE <<< >>> ERR 103 <<< ( fieldno) IN LEGFIL |  One or more of the fields **MODEL, PERIMIN, TYPE, PLANE, NUMBER, SEQUENCE, PERIMID, DENSITY, VOLUME, TONNES** was missing or wrong type. Fatal; the process is exited. |  Check for the existence and type of fields **MODEL, PERIMIN, TYPE, PLANE, NUMBER, SEQUENCE, PERIMID, DENSITY, VOLUME, TONNES** in the &**RESULTS** file.  
>>> NO RESULT RECORDS FOR PLANE pppppppp <<< |  There were no records matching the requested plane. Fatal; the process is exited. |   
>>> WARNING - ILLEGAL GRADE INTERVAL. RECORD IGNORED <<< |  The grade interval from the **INTERVAL** field was not in the range 1-20. The record is ignored. |   
>>> ERROR - MORE THAN ONE ENTRY FOR GRADE INTERVAL <<< |  More than one grade interval (value of **INTERVAL** field) was found for a particular rocktype, perimid, sequence, number combination. The results file is probably corrupt. Fatal; the process is exited. |