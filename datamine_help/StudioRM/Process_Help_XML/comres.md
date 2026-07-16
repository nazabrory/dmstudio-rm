# COMRES Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COMRES** and click **Run**.
  * Enter "COMRES" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COMRES>).

## Process Overview

Generates a file that contains summary results from a number of different **RESULTS** files, that have been produced by processes such as [MODRES](<modres.md>) or [TRIVAL](<trival.md>).

The output file generated is suitable for subsequent mine planning and scheduling purposes, such as interactive production scheduling (**PRODSH**). The file will contain reserve figures for production units that have been classified by the user into primary and secondary categories, and it will contain all grade fields that are contained in the input **RESULTS** files.

Production scheduling requires some initial definition of the quantities and grades of the mining units to be scheduled. The final product of any evaluation is a comprehensive **RESULTS** file that contains data describing the mining reserves. There are a number of standard fields in a **RESULTS** file, which allow each logical part of an evaluation to be stored as a data record with entries including the tonnage, volume, grade(s), grade intervals, block model position, perimeter numbers and wireframe zone numbers.

The **COMRES** process accepts the input from one or more such **RESULTS** files (maximum 20) and generates a **RESERVE** file, which will be used for subsequent production scheduling. Each record of the **RESERVE** file describes the tonnage and grade of a production unit. The classification of production units stems from user selection of various options during the operation of **COMRES**. This allows production units to be classified into primary and secondary categories, based on criteria available from the **RESULTS** files. This flexibility allows the scheduling extension module to be used for both open pit and underground mining applications.

Two numeric fields in the **RESERVE** file, **PNUM** and **SNUM** , contain the primary and secondary numbers for each production unit. The data entries in these fields come directly from the input **RESULTS** files or are assigned logically according to the selected classification option, e.g. if the secondary classification is based on perimeters, the **SNUM** values will come from the **PERIMID** values in the **RESULTS** file(s). If a number of **RESULTS** files are input, and primary classification by model is required, the **PNUM** entries will increment 1, 2, 3 etc. for each **RESULTS** file.

If secondary classification is by ore/waste, the **SNUM** values will be either 1 for ore or 2 for waste. Another alphanumeric field, **UNIT** , allows a clear primary descriptor to be assigned for each production unit, which will appear on the schedule screen in the **PRODSH** process.

The production rate at which each production unit will be mined may also be defined in the **COMRES** process. The **RESERVE** file is a normal Datamine binary file, and so may be listed, edited or joined with other files using the available relational database facilities.

### Results Files

Enter the name of each **RESULTS** file, followed by <return>. Typing <?> will show a list of the currently selected **RESULTS** files. Typing a back arrow, <, will clear all the filenames entered and reprompt from the beginning. Entries are terminated by just typing <return>. Pressing <!> will terminate the process. When more than one **RESULTS** file is entered, it is expected that each contains the same grade fields.

### Production Rates

Enter required production rate for each **RESULTS** file. Pressing <return> will put absent data into the production rate data record for that **RESULTS** file. These production rate values may be initialized or modified in the **PRODSH** production scheduling process. These values will be stored in the **PRATE** field of the **RESERVE** file.

### Production Unit Classification

For production scheduling purpose, production units are classified from data held in the **RESULTS** files, and this may be done in a number of ways. A primary and optionally a secondary means of classification is available, allowing a number of features during production scheduling. 

If more than one **RESULTS** file has been entered, the user will get the following prompt:
    
    
    > IS THE SAME TYPE OF PRIMARY AND SECONDARY CLASSIFICATION REQUIRED 
     FOR EACH RESULTS FILE [Y]/N  > 

If N or NO is entered, you will get primary and secondary classification options for each **RESULTS** file that has been entered.

If the default option has been taken for the above prompt, then the classification selected below will used for each of the supplied **RESULTS** files.

### Primary Classification

Options are:

  1. Model or Sample File
  2. Plane
  3. Perimeter
  4. Zone

Enter number for required type of primary classification, which will determine the manner of primary tonnage and grade accumulation, in addition to the primary names and numbers in the output **RESERVE** file. Just typing <return> will take the default 'MODEL' or 'SAMPLE FILE' (from a **SECTED** evaluation) primary classification.

### Secondary Classification

Options are:

  1. No secondary classification
  2. Plane
  3. Perimeter
  4. Zone
  5. Ore/Waste
  6. Grade Interval

Enter number for required type of secondary classification. Just typing <return> will take the default, omitting any secondary classification.

These primary and secondary classification prompts will be repeated for each **RESULTS** file entered, if a a separate means of classification for each file was requested above.

Once the primary and secondary classification is complete the **RESERVE** file will be generated.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
RESERVE |  Output |  Yes |  Undefined |  The output file generated, for use in subsequent scheduling processes, such as **PRODSH**. It will contain the following fields, in addition to all of the grade fields in the **RESULTS** file(s). **UNIT** A,8 Field containing the name of each production unit. **PNUM** N Any blocks being scheduled may be categorised according to a primary and secondary classification. The **PNUM** field contains the primary number. The values held in this field will depend on the type of primary classification selected. **SNUM** N Secondary classification number. The values held in this field will depend on the type of secondary classification selected. If ore/waste secondary classification is selected, it will contain values of 1 for all ore units, and values of 2 for all waste units. **NY** N Implicit field, defining the total number of production units in the file, equal to the number of records. **PRATE** N Notional production rate at which each production unit is to be mined. This may contain absent data values, as individual production rates may be defined or changed during operation of **PRODSH**. **TONNES** N Reserve tonnage for each production unit.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ZONE |  Optional numeric zone identifier field that has been used to define individual wireframe zones. This field need only be defined if reserve classification by wireframe zone is required. |  RESERVE |  No |  Numeric |  Undefined  
  
## Example
    
    
    ----------------------------------------------------------------------   
  
---  
      
    
    FILENAME RESERVE1 SHEDXDIR   
      
    
    ----------------------------------------------------------------------   
      
    
    FILE CREATED BY MICL USING COMRES ON 5/ 4/89   
      
    
    ----------------------------------------------------------------------   
      
    
    FILE CONTAINS 19 RECORDS EACH OF LENGTH 10   
      
    
    ----------------------------------------------------------------------   
      
    
    FIELD TYPE WORD.NO STORED START DEFAULT   
      
    
    ----------------------------------------------------------------------   
      
    
    UNIT A 1 Y 1   
      
    
    UNIT A 2 Y 2   
      
    
    PNUM N 1 Y 3 0.0   
      
    
    SNUM N 1 Y 4 0.0   
      
    
    TONNES N 1 Y 5 0.0   
      
    
    PRATE N 1 Y 6 0.0   
      
    
    CU N 1 Y 7 2.0   
      
    
    ZN N 1 Y 8 3.0   
      
    
    PB N 1 Y 9 4.0   
      
    
    NY N 1 N 0 19.0   
      
    
       
      
    
    >>> PRESS <RETURN> TO CONTINUE (OR ! TO TERMINATE) >   
      
    
    UNIT      PNUM SNUM TONNES   PRATE   
      
    
     CU   
      
    
    LEV 15    15.0 15.1 13840.5  300.0 3.497105   
      
    
    LEV 15    15.0 15.2 14341.5  300.0 2.970047   
      
    
    LEV 15    15.0 15.3 8631.188 300.0 2.275357   
      
    
    LEV 14    14.0 14.1 13860.19 300.0 4.34134   
      
    
    LEV 14    14.0 14.2 15619.88 300.0 3.577554   
      
    
    LEV 14    14.0 14.3 15822.19 300.0 3.674741   
      
    
    LEV 13    13.0 13.1 16597.31 300.0 5.150764   
      
    
    LEV 13    13.0 13.2 17079.19 300.0 3.56348   
      
    
    LEV 13    13.0 13.3 10059.56 300.0 4.590841   
      
    
    LEV 12    12.0 12.1 16504.13 300.0 8.868559   
      
    
    LEV 12    12.0 12.2 18105.19 300.0 4.606041   
      
    
    LEV 12    12.0 12.3 16858.31 300.0 4.573792   
      
    
    LEV 11    11.0 11.1 14872.31 300.0 10.59326   
      
    
    LEV 11    11.0 11.2 19954.13 300.0 5.090855   
      
    
    LEV 11    11.0 11.3 17112.0  300.0 3.988503   
      
    
    ASSAYS D   2.0 17.1 26924.92 160.0 8.142336   
      
    
    ASSAYS D   2.0 18.2 27832.03 160.0 1.841848   
      
    
    ASSAYS D   2.0 19.6 24682.9  160.0 3.375697   
      
    
    ASSAYS D   2.0 20.5 35343.56 160.0 2.756991   
      
    
    19 RECORDS LISTED  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> INVALID NAME FOR RESERVES FILE SUPPLIED |  This message indicates that an illegal name has been supplied for the output **RESERVE** file.  
>>> FILE AAAAAAAA CANNOT BE FOUND |  This means that one of the **RESULTS** filenames supplied cannot be found.  
>>> RESULTS CANNOT BE COMBINED FOR THIS PRIMARY/SECONDARY CLASSIFICATION |  Illegal type of primary/secondary classification has been requested, e.g. it is not possible to have the same type of primary and secondary classification.  
>>> NOT A VALID RESULTS FILE :  
FIELD AAAAAAAA MISSING OR WRONG TYPE  
ERR 103 <<< ( 1) IN ULGFIL |  When checking each **RESULTS** file, one of the essential fields is missing or it is numeric when it should be alphanumeric or vice versa.  
>>> ILLEGAL RESULTS FILE : AAAAAAAA |  One of the **RESULTS** files supplied does not have the correct data definition for a **RESULTS** file, one of the essential fields is missing.  
>>> SUPPLIED NAME FOR ZONE FIELD DOES NOT EXIST IN FILE :AAAAAAAA |  If the optional **ZONE** field has been defined, and this wireframe zone classification is required for one of the input **RESULTS** files, the user will get this error if the supplied * **ZONE** field cannot be found.  
>>> NO GRADE INTERVALS IN AAAAAAAA, SO CANNOT SPLIT RESERVES INTO ORE AND WASTE |  If a secondary classification of ore/waste is required, the **RESULTS** file(s) that has been input must contain evaluation data for different grade intervals.  
>>> NO. OF RESULTS FILES EXCEEDS SYSTEM LIMIT OF :N. |  There is a limit to the number of **RESULTS** files that may be entered during one operation of **COMRES**. If the current limit is exceeded this error message will result.  
>>> DIFFERENT NUMBER OF GRADE FIELDS IN THE RESULTS FILES SUPPLIED |  When more than one **RESULTS** file is used as input to **COMRES** , it is expected that each of these files will have the same number of grade fields.  
>>> MIS-MATCH OF DDS IN RESULTS FILES |  When more than one **RESULTS** file is used as input to **COMRES** , it is expected that each of these files will have the same data definition. If this is not the case, this message will result.  
>>> SUPPLIED ZONE FIELD IS NOT NUMERIC |  If categorization is required using wireframe zones, the supplied * **ZONE** field must be numeric.