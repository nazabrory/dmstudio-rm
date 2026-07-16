# Conditioning String Data

String conditioning effectively removes crossovers, duplicate points and other issues that may cause problems in subsequent processing. The string is modified to meet specified criteria for chord lengths and angles.

**Note** : if the precise location of the unmodified string vertices is important, it may be better to smooth the string (see below) as conditioning it can potentially slightly affect the position of any existing string vertex, although the overall string shape is maintained where possible.

The string may be open or closed and adjustment is based on three parameters: minimum chord length, maximum chord length and minimum angle.

Strings are conditioned using the [condition-string](<../command_help/condition-string.md>) (quick keys = "cond").

## Smoothing Strings

String smoothing adds extra points to a string, reducing the length of individual chords to make any curves smoother. The command inserts new points between each existing pair of points. 

The coordinates of the original points on the string remain unaltered. Where the position of unsmoothed string vertices is important, consider smoothing a string to introduce additional vertices without affecting them.

String smoothing is performed using the [smooth-string](<../command_help/smooth-string.md>) command (quick keys = "sms")

**Note** : string smoothing uses a technique called "parabolic blending".

Related topics and activities

  * [The condition-string command](<../command_help/condition-string.md>)

  * [Enter Condition String Parameters](<Condition%20String%20Dialog.md>)

  * [The smooth-string command](<../command_help/smooth-string.md>)