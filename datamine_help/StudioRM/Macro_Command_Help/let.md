# LET Macro Command

Sets values of substitution variables. Arithmetic and functions are provided.

The general format for this macro command is:
    
    
    !let <var>=<var1>  
  
---  
      
    
    !let <var>=<var2><op><var3>  
      
    
    !let <var>=<func1>(<var2>)  
      
    
    !let <var>=<func2>(<var2>,<var3>)  
      
    
    !let <var>=ENV(<str1>[,<var2>])  
      
    
    !let <var>=EVAR(<str1>)  
      
    
    !let <var>=INDX(<str1>,<str2>)  
      
    
    !let <var>=LENG(<str1>)  
      
    
    !let <var>=LWC(<str1>)  
      
    
    !let <var>=SUBS(<str1>,<var1>,[<var2>])  
      
    
    !let <var>=UPC(<str1>)  
  
where:

  * `<var>` is a substitution variable.

  * `<var1>` is a substitution variable or a constant.

  * `<op>` is an arithmetic operator + - omitted, `<var1>` and `<var2>` are concatenated as character strings.

  * `<var2>` is a numeric substitution variable or a constant.

  * `<var3>` is a numeric substitution variable or a constant.

  * `<func1>` is a function from the set `SQRT, EXP, LOG, LOGE, LOGN, INT, SIN, COS, TAN, ASIN, ACOS, ATAN, ABS`.

  * `<func2>` is a function from the set `MOD, RAIS, MAX, MIN`.

  * `<str1>` is a string substitution variable or constant.

  * `<str2>` is a string substitution variable or constant.

  * If `<str1>` or `<str2>` contain embedded blanks which must be preserved, the variable or constant should be enclosed in (single) quotes.

  * `ENV` provides access to environment variables. `<str1>` is the name of an environment variable. If `<var2>` is included, it should specify which value (1..N) of the environment variable is required; if omitted, the first value is returned.

  * `EVAR` returns a value of 1 if the argument is a valid substitution string, otherwise 0.

  * `INDX` returns an integer, representing the starting position within `<str1>` of a substring identical to `<str2>`. If `<str2>` occurs more than once, the position of the first match is returned. If `<str2>` does not occur within `<str1>`, `INDX` returns zero (0).

  * `LENG` returns the length of the character string `<str1>`, (the number of characters up to the first trailing blank).

  * `LWC` returns its argument with all upper case letters converted to lower case.

  * `SUBS` returns a substring of `<str1>` that begins at character position `<var1>` and is at most `<var2>` characters long. If `<var2>` is omitted, the remainder of the string is assumed.

  * `UPC` returns its argument with all lower case letters converted to their upper case equivalents.

## Examples
    
    
    !let $3=3!let $1=$2  
  
---  
      
    
    !let $3='$2'  
      
    
    !let $3=$1/$2  
      
    
    !let $5=sin(45)  
      
    
    !let $6=max($1,$3)  
      
    
    !let $d=env(directory)  
      
    
    !let $s=subs($dXXXXX,1,5)  
      
    
    !let $s=$sSUB.DAT  
  
Together, the last three examples will construct the name of the subset file for any directory.

Related topics and activities:

  * [VARINIT](<varinit.md>)

  * [VARLOAD](<varload.md>)

  * [VARSAVE](<varsave.md>)