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
