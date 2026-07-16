# INCLUDE Macro Command

The "!INCLUDE" soft command enables records from a DATABASE file to be incorporated as normal data or statement lines within a Macro or Menu.

When encountered at runtime, the `!INCLUDE` command is replaced with one or more records from the nominated file.

General Format :
    
    
    !INCLUDE &FILE(file), *TEXT(textfld), *KEY(keyfld), @VALUE='keyval'  
  
---  
  
Where:

  * `&FILE(file)` specifies the database file to read, and must be supplied.

  * `*TEST(textfld)` is optional, and specifies the name of the field within `FILE` to use. The default is 'TEXT'.

  * `*KEY(keyfld), @VALUE='keyval'` are optional. Taken together they permit selection of a subset of records from FILE. `Keyval `is specified as a quoted ('') string. 

The statement may be extended onto as many lines as necessary; continuation is implied by ending the previous line with a comma. `!INCLUDE` commands can be nested. These are expanded as encountered, and placed in a buffer for inclusion in the macro.

The `!INCLUDE` command is discarded if no (matching) lines are found in FILE. It is illegal to supply additional data/text on the `!INCLUDE` statement line.

The line(s) returned from `FILE` must be valid data or command lines for the macro or menu being executed. Blank lines in `FILE` are honoured, and passed on for macro processing. Substitution variables are permitted, both in the statement itself and within the lines returned from the file.

## Restrictions

The following restrictions should be noted:

  * Records from `FILE` are stored in a buffer. Each line in the buffer is processed in turn. When all lines have been processed, normal macro execution resumes on the next line after the `!INCLUDE` call.

  * If control soft-commands (**[GOTO](<goto.md>)** , **[GOSUB](<gosub.md>)** and so on) are part of the included text, all remaining commands in the buffer WILL STILL BE EXECUTED. Control will be transferred to the target label ONLY when the buffer is empty and normal processing resumes. Macro Labels in `!INCLUDE`d text are ignored. For these reasons, it is recommended that control commands are not supplied in include files.

  * Multi-line soft commands cannot be used in `!INCLUDE` files for the current implementation (**[FIELD](<field.md>)** , **[VARLOAD](<varload.md>)** , **[VARSAVE](<varsave.md>)**) are restricted to single line commands

Note: **[PROMPT](<prompt.md>)** cannot be used either

## Examples

Create and use a standard set of test criteria to list all plotfiles with the PICDIR process. All records in the file 'PLOTSPEC', field 'TEXT' will be supplied as TEST> criteria to [PICDIR](<../Process_Help_XML/picdir.md>):
    
    
    !INPFIL &OUT(PLOTSPEC) # create the file  
  
---  
      
    
    Database file containing test for plotfiles  
      
    
    TEXT A 72 Y ' '          
      
    
    ]  
      
    
    ok  
      
    
    # no system file  
      
    
    ( FILE *.P OR FILE ???????P ) END  
      
    
    !PICDIR &OUT(PLOTLIST)  
      
    
    !INCLUDE &FILE(PLOTSPEC)  
  
Incorporate one of a standard library of equations in a **[GENTRA](<../Process_Help_XML/gentra.md>)** routine. The file `FORMULAE` contains various assay cut formulae, which are keyed on the field `ASSAYCUT`. The required equation has the key value `AU10CUT`:
    
    
     !LET $value#='AU10CUT'          
  
---  
      
    
     !GENTRA &IN(SAMPLES),&OUT(CUTASSAY)  
      
    
     !INCLUDE &FILE(FORMULAE),*TEXT(TEXT), *KEY(ASSAYCUT),  
      
    
     @VALUE='$value#'  
      
    
     END  
      
    
     OK  
      
    
     !LIST &IN(CUTASSAY)  
  
Related topics and activities:

  * [GOTO Macro Command](<goto.md>)

  * [GOSUB Macro Command](<gosub.md>)