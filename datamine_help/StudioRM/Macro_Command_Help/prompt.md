# PROMPT

Displays lines on screen and prompts for input.

**PROMPT** enables menu screens to be constructed and substitution variables to be defined or redefined as often as required. In-built validation procedures are available on the responses to prompts.

The `!PROMPT` command is followed by as many data lines as required. The first character of the line may be any one of the following:

  * The line will be displayed on the screen.

  * A prompt string is being defined. 

A line beginning with any other character than those listed will be ignored and treated as a comment.

Each data line may be up to 80 characters long, including the first 0 or 1

### Numeric Responses

The substitution variable, may optionally be followed by a number of parameters. The most simple form of this type of prompt string is:
    
    
    1 Enter number > '$1'

The response to `$1` must be numeric, that is an integer or decimal number of form 12 or 12.56. A number such as `2.4E-6` or - (absent) or + (highest possible system number), or `TR` (trace), or `DL` (Detection Limit) are not allowed.

Range limits can be placed on the response. For example:
    
    
    1 Enter number > '$1'.n.1.3

The numeric response (indicated by n or N) must now lie in the range 1 - 3 inclusive. Note that both upper and lower limits must be specified. The order is lower, upper.

It is also possible to enter a string of permitted values for the response, for example:
    
    
    1 Enter number > '$1',n,1,3,1,2,3

In this case, only values 1, 2 or 3 are permitted any other number that falls within the specified range e.g. 1.1 is not permitted.

### Alphanumeric Responses

The format for alphanumeric strings is very similar. For example:
    
    
    1 Enter file name > '$1',a

This allows a character string (indicated by a or A) up to a maximum of 72 characters as a response.

We can defined the maximum length of the string as follows:
    
    
    1 Enter file name > '$1',a,24

Here the string may be no more than 24 characters long.

Just as for numbers it is also possible to specify a set of responses which can be accepted. For example:
    
    
    1 Enter file name > '$1',a,5,file1, file2, file3

This would permit only the responses file1, file2 or file3.

If the last character on a prompt line (starting with 1) is a comma, then the line can be continued. a maximum length of 240 characters is permitted, counting from the character following the initial 1 to the end of the last non-blank character. For example:
    
    
    Enter file name >
    
    
    '$1',n,1,20,1,2,3,4,5,6,7,8,9,10,
    
    
    11,12,13,14,15,16,17,18,19,20

**Note** : Any characters over 240 will be ignored.

Upon matching responses, an exact response is required for alphanumeric variable. If a comma is to be part of the required response, then the response must be contained within quotes. For example:
    
    
    1 Enter file name > '$1',a,10,'a,b','b,c'

would permit the responses to be a,b or b,c.

### Default Values

A default may be defined to any response. This default is contained within square brackets, and must appear before the substitution variable. For example:
    
    
    1 Enter choice (1, 2 or 3) [1] > '$1',an,1,3,1,2,3

If <return> is pressed, then the default taken will be 1. The default does not have to be part of the permitted responses but it must be of the same type (numeric or alphanumeric).

### Substitution in Prompt Lines

Existing substitution variables may be incorporated into prompt lines. Suppose that a variable $1 was already set up with value collars. We could then include a prompt:
    
    
    !PROMPT
    
    
    0 Your input file is $1
    
    
    1 Enter required file name [$1] > '$1',a,8
    
    
    This would appear on the screen as:
    
    
    Your input file is collars
    
    
    Enter required file name [collars] >

The response would default to collars if <return> was pressed. if another name were given, this would replace $1 with its new value.

Substitution can also take place within the permitted responses. For example, the following is permitted:
    
    
    1 Enter choice [$2] > '$1',n,1,$3,$1,$2,$3

Note that in this example $1, $2 and $3 must be numeric variables. If they are not an error will occur.

### Stack File Display

If to any prompt the response is !!, then the current stack file will be displayed. The format is:
    
    
    STACK NUMBER 4
    
    
    ============
    
    
    STACK FILE REVISION NO : STACK v3.2
    
    
    FILE TYPE (0=DATABASE, 1=MENU, >=2=EXTERNAL) : 3
    
    
    FILE NAME : mymacro.mac
    
    
    MACRO NAME IN FILE : m
    
    
    RECORD NUMBER OF !START : 36
    
    
    MACRO POINTER WITHIN MACRO : 12
    
    
    NUMBER OF SUBSTITUTION VARIABLES : 2
    
    
     
    
    
    SUBSTITUTION VARIABLES AND VALUES
    
    
    ==========================
    
    
    $1    =    3
    
    
    $2    =    12.0000
    
    
    END OF STACK LISTING  
    ================

### Termination of Macros or Menus

The response '!' will cause a menu or macro to be terminated, unless this response has been trapped by entering it as a permitted response.

### Bypassing Macros or Menus

If `!<string>` has been entered which is not one of the permitted responses, then this will be assumed to be a process (for example, **HOLES3D** , **ADDMOD** and so on) for execution. The command will be executed immediately, and then the macro will resume running from the `!PROMPT` command from which the command was issued. This facility allows a menu to be temporarily bypassed.

## Notes

2  |  Clears screen.  
---|---  
0  |  Lines to be displayed.  
1 '$1',n,bot,top,<list of responses> |  Prompt line for numeric response.  
---|---  
|  Bot is lower limit,  
|  top is upper limit.  
|  <list of responses> with each separated by commas:  
|  eg. 3,4.2,5. All items following '$1' are optional.  
1 '$1',a,len,<list of responses> |  Prompt line for alpha response.  
|  Len is maximum length of response in characters.  
|  <List of responses> with each separated by commas:  
|  eg. a,ab,c. All items following '$1' are optional.  
  
Response is placed in variable '$1' (any string up to 8 chars) and substitutes in all command and data lines (except labels).

Defaults are placed in square brackets. Substitution in the line is permitted, like this:
    
    
    1 Enter choice ($1,$2,$3) [$3]>'$1',n'$1,$3,$1,$2,$3

## Examples

The user's response, supplied after the character prompt > is placed in substitution variable $1, so that all subsequent references to $1 in the macro will be substituted by the given response:
    
    
    !PROMPT  
  
---  
      
    
    0  
      
    
    0 File listing macro.  
      
    
    0 ================  
      
    
    1 Enter the file name to be listed (up to 8 chars) > '$1',a,8  
      
    
    !LIST &in($1)  
      
    
       
      
    
    !XXO:PROMPT  
      
    
    0  
      
    
    0 EXAMPLE MENU  
      
    
    0 --------------------------------  
      
    
    0  
      
    
    0 Select from the following choices:-  
      
    
    0  
      
    
    0 List the file directory    
      
    
    0 List a named file    
      
    
    0 End session    
      
    
    0  
      
    
    1 Enter your choice (1,2,3) > '$1',n,1,2,1,2,!  
      
    
    !GOTO XX$1  
      
    
    !XX1:LISTDR  
      
    
    !GOTO XXO  
      
    
    !XX2:PROMPT  
      
    
    1 Enter name of file to be listed > '$2',a,8  
      
    
    !LIST &in($2)  
      
    
    !GOTO XXO  
      
    
    !XX!:LOGOFF  
      
    
    !END  
  
## Error and Warning Messages

The possible error messages that are displayed for an incorrect numeric response are:

>>> |  OUTSIDE RANGE OF 99999 OT 99999 <<<  
---|---  
>>> |  ILLEGAL CHARACTER IN POSITION 9 <<<  
>>> |  NON-NUMERIC PERMITTED RESPONSE <<<  
  
The possible error messages that are displayed for an incorrect alphanumeric response are:

>>> |  ALPHA STRING LONGER THAN 9999 CHARS <<<  
---|---  
  
Other message are:

>>> |  NO MATCH TO PERMITTED VALUES <<< The response entered does not match the set of permitted values. <listing of all permitted values>  
---|---  
>>> |  NUMBER REQUIRED IN RANGE 99999 to 99999 <<<  
>>> |  RESPONSE MUST BE ONE OF THE FOLLOWING <<< <listing of all permitted values> This message appears when ? is entered at a prompt.  
>>> |  MALFORMED PROMPT STRING <<<  
|  The prompt string is unrecognizable.