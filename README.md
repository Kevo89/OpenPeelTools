OpenPeelTools
=============

Tools for use with the Region of Peel's open data

##fcp_xml2csv

This tool simply converts the Food Check Peel (FCP) data from its original XML source to a Comma Separated Value file type for easier use and portability.

###Requirements

* Python 2.7
* lxml - Python Library

This will probably work on other Python 2.x or 3.x versions, but it has not been tested.

###Using

This script assumes the FCP XML file is in the same directory as the Python script and also assumes the file retains the original name ("FoodCheckPeel.XML").

* Place the XML file and Python script in the same directory
* Run the command on Linux in the Terminal using: `python fcp_xml2csv.py`
* Run the command on Windows by double clicking the Python script or running this command in Command Prompt: `fcp_xml2csv.py`
* The program will ask you want you want to call the file - by default it uses FoodCheckPeel.csv if you leave the field blank
* It does its work
* Bam! Donezo.

#License
The MIT License (MIT)

Copyright (c) 2014 Kevin Farrugia

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
