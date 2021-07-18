# Fake-Data-Generator

<h2><i>string_format_generator.py</i></h2>

  &emsp;&emsp;<b><i>Take Parameters:</i></b></br>
  &emsp;&emsp;&emsp;&emsp;<b><i>1. Number of rows:</i></b> Number of strings want to generate</br>
  &emsp;&emsp;&emsp;&emsp;<b><i>2. Format:</i></b> Format of strings want to generate</br>
  &emsp;&emsp;&emsp;&emsp;<b><i>3. Elements:</i></b> list of all elements of string format except special characters</br>
  &emsp;&emsp;&emsp;&emsp;<b><i>4. Constraints:</i></b> JSON Object contain constraint on each element that it should be random or choosen from a specific data set</br>
  &emsp;&emsp;&emsp;&emsp;<b><i>5. Data sets:</i></b> JSON Object contain all data lists from which format element should be choosen</br>
  &emsp;&emsp;<b><i>Working:</i></b></br>
  &emsp;&emsp;&emsp;&emsp;Create copy of the string format</br>
  &emsp;&emsp;&emsp;&emsp;Then for each string element check constarints</br>
  &emsp;&emsp;&emsp;&emsp;Then on basis of constraints generate value for that element</br>
  &emsp;&emsp;&emsp;&emsp;And then replace that element with generated value</br>
  &emsp;&emsp;&emsp;&emsp;Append that new generated string in output list</br>
  &emsp;&emsp;&emsp;&emsp;At the end return that list</br>
  
  

<h2><i>choose_random.py</i></h2>

  &emsp;&emsp;Take list of elements and randomly select one element from them and return that.
 
 
<h2><i>random_string_generator.py</i></h2>
  
  &emsp;&emsp;Take length and generate string of that length by combining random alphabets
  
 <h2><i>test1.py</i></h2>
 
  &emsp;&emsp;Test function which have specific parameters for email format. Call string_format_generator() by passing those parameters and print &emsp;&emsp;list of generated email id's returned by function.
  
  <h2><i>test2.py</i></h2>
 
  &emsp;&emsp;Test function which have specific parameters for name format. Call string_format_generator() by passing those parameters and print &emsp;&emsp;list of generated full names returned by function.
