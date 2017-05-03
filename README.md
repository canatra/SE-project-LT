# SE-project-LT
What is it?
-----------
This project translates simple FORTRAN programs to Python using Antlr4.5 and a FORTRAN grammar, fortran77.g4. The issues faced in this projects were mainly due to the inaccuracies of the fortran77.g4 file. We have updated this file to implement an improved version of the grammar. For more details on the original grammar please visit: https://github.com/antlr/grammars-v4/blob/master/fortran77/fortran77.g4

This project was created for CIS5930 Spring 2017.

This project includes:
----------------------

 the grammar (fortran77.g4)
 
 the driver program (driver.java)

The listener program (f_to_py.java) used to overwrite functions from the fortran77BaseListener.java 

The preprocessor (preprocess.java)

The postprocessor (postprocess.java)

The Bash script that runs the translator 

An example folder with sample programs that can be translated from FORTRAN to Python

The defunct line by line translator

To run the program Antlr4.5 is required. To run the program:

$ ./runme <programname without the .f>

To run the antlr tree see the commands below for details: 

Certain aliases must be set up with these commands

$  Antlr4 fortran77.g4

$  Javac *.java

$  grun fortran77 program name_of_file_to be parsed -gui

The aliases:
------------
$ alias antlr4='java -jar /usr/local/lib/antlr-4.0-complete.jar'

$ alias grun='java org.antlr.v4.runtime.misc.TestRig'

For more details see the Antlr4 Reference.

To install Antlr 4.5 please visit:
 http://www.antlr.org/download.html
