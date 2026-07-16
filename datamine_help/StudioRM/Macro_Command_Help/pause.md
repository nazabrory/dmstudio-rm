# PAUSE Macro Command

Pauses for a time proportional to the @DELAY parameter.

The **PAUSE** macro command is designed for use in a macro, in which it may be required to hold the information on the screen for a while before the next process is executed.

The delay is caused by executing a 'do nothing' arithmetic DO loop the number of times requested by the `@DELAY` parameter * 100. The user should experiment to find the delay caused by any given value of `@DELAY`.

## Example
    
    
    !PAUSE @DELAY=5  
  
---  
  
Related topics and activities:

  * [RETURN](<return.md>)