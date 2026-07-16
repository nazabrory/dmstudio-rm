# Creating the Browse and Copy Interface

The interface you are going to create is shown below:

[![](../Images/Studio3%20Scripting%20Browse%200001.jpg)](<javascript:void\(0\);>)

Similar to the previous exercise group, this set of exercises guides you through creating an HTML table and hooking up some Javascript functions to each of its components. The table itself consists of some buttons, text and text boxes.

## Prerequisites

  * The file `_vb_scr_points.dm`_vb will be used to test the script.  
  
This file can be found at `C:\Database\DMTutorials\Data\VBOP\Datamine` for standard installations.

## Exercise: Drawing a table to contain the interface objects

  1. In Notepad, create a new, empty text file called "Browse.htm".
  2. Create an empty <HTML> tags and within it place <HEAD> and <BODY> section opening and closing tags.
  3. Construct a 5 x 5 table using HTML within the <BODY> section using <TABLE>, <TR> and <TD> elements.
  4. At this stage, you just need to construct an empty table - no cell contents.
  5. Once you have created the table, Save your file. It should contain similar syntax to this:
         
         <!DOCTYPE html PUBLIC   
  
---  
           
              "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">  
           
         <html xmlns="http://www.w3.org/1999/xhtml">  
           
         <head>  
           
         <meta http-equiv="Content-Type"   
           
              content="text/html; charset=iso-8859-1" />  
           
         <title>Untitled   
           
              Document</title>  
           
         </head>  
           
         <BODY>  
           
         <table>  
           
           <tr>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
           </tr>  
           
           <tr>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
           </tr>  
           
           <tr>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
           </tr>  
           
           <tr>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
           </tr>  
           
           <tr>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
             <td>&nbsp;</td>  
           
           </tr>  
           
         </table>  
           
         </BODY>  
           
         </html>  
           
            
  

## Exercise: Adding text and text boxes

Next you will need to add text and text boxes to the table.

The text describing the contents of the text boxes will be placed into the left hand cells of the table and the text boxes themselves into the central column cells.

You can either do this using source code edits, or using an interactive WYSIWYG editor.

  1. Add the words 'Copy a File' to the central column in row 1. Use additional formatting if you wish to embolden the text.
  2. Next, you need to merge all of the cells in the top row. This is done using the <ROWSPAN> attribute if you are editing source code manually.
  3. Horizontally align the text in the top row centrally.
  4. In the left hand cell in the second row, type 'Input File'.
  5. In the left hand cell in the third row, type 'Output File'.
  6. In the left hand cell in the fourth row, type 'Retrieval Criteria'.
  7. Insert a Text Field form element into the central column of the second row (name = "txtInput"). This will place a text box within the cell. This will be used to display the name of the input file.
  8. Repeat step 6 for the middle column, third row (name = "txtOutput"). This will be used to display the name of the output file.
  9. Repeat step 6 for the middle column, fourth row (name = "txtRet"). This is where you will enter retrieval criteria.

The <BODY> section of your file should now look like this:
    
    
    <BODY>  
  
---  
      
    
    <table>  
      
    
      <tr>  
      
    
        <td colspan="3"><div   
      
    
         align="center">Copy a File </div></td>  
      
    
      </tr>  
      
    
      <tr>  
      
    
        <td>Input File </td>  
      
    
        <td><label>  
      
    
          <input   
      
    
         type="text" name="txtInput" />  
      
    
        </label></td>  
      
    
        <td>&nbsp;</td>  
      
    
      </tr>  
      
    
      <tr>  
      
    
        <td>Output File   
      
    
         </td>  
      
    
        <td><input type="text"   
      
    
         name="txtOutput" /></td>  
      
    
        <td>&nbsp;</td>  
      
    
      </tr>  
      
    
      <tr>  
      
    
        <td>Retrieval Criteria   
      
    
         </td>  
      
    
        <td>&nbsp;</td>  
      
    
        <td>&nbsp;</td>  
      
    
      </tr>  
      
    
      <tr>  
      
    
        <td>&nbsp;</td>  
      
    
        <td>&nbsp;</td>  
      
    
        <td>&nbsp;</td>  
      
    
      </tr>  
      
    
    </table>  
      
    
    </BODY>  
      
    
       
  
## Exercise: Adding browse buttons

Next we will add some buttons for activating the form.

  1. In row 2, right-hand cell, add a Push Button HTML form element (name = "btnInput")
  2. Repeat step 1 by selecting the right hand cell, third row (name = "btnOutput").
  3. Repeat step 1 by selecting the middle column and fifth (last) row (name = "btnOK").
  4. Save your Browse.htm text file.

![](../Images/UpArrow.gif)Top of page