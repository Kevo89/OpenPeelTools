#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################
# FoodCheckPeel XML2CSV Converter
#
#  This script converts the FoodCheckPeel XML
#  file to the Comma Separated Values file type
#  so it's easier to import to common spreadsheet
#  applications.
#  Based on the script posted here:
#   http://www.bearpanther.com/2013/09/14/converting-xml-to-csv-with-python/
#
#  Programmed with Python 2.7 + lxml 3.2.4
#  Kevin Farrugia
############################################

__author__ = "Kevin Farrugia"
__copyright__ = "(c) 2014 Kevin Farrugia"
__license__ = "MIT"
__credits__ = "Derek Swingley (author of Bear Panther)"

import csv
from lxml import etree

print "Welcome to the FoodCheck Peel XML to CSV Conversion utility!\n"
print "============================================================\n"
print "\tPlease make sure that the XML file is the latest\n\t version so that your data isn't out of date.\n"
print "Authored by Kevin Farrugia -  Last updated January 2014\n"
print "------------------------------------------------------------\n"

outFileName = raw_input("What would you like the output file to be named (this defaults to the correct FoodCheckPeel.csv)?  ")
if outFileName.strip() is "":
    outFileName = "FoodCheckPeel.csv"

outputData = []

# File parser
#   Recover set to True to allow it to try to work through broken XML
#   remove_blank_text set to True so that it removes tailing whitespace
fileParse = etree.XMLParser(recover=True, remove_blank_text=True)

#The input XML file name - in our case, it is static and predictable so we don't allow users to change it
fileName = "FoodCheckPeel.XML"

#Parse the XML
root = etree.parse(fileName, fileParse)

#Names of elements that will be carried over (in this case, all of them)
headers = [ "FACILITY_NUMBER", "FACILITY_NAME", "FACILITY_TYPE", "STREET_NUMBER", "STREET_NAME", "STREET_DIR", "CITY", "X", "Y", "LAT", "LON", "INSPECTION_DATE", "STATUS", "INSPECTION_ID", "INSPECTION_TYPE", "INFRACTION_ID", "INFRACTION_TYPE" ]

#Here is where we grab information for each FCP location and parse it out
def getInfo(p):
    rowData = []
    for attribute in headers:
        node = p.find(attribute)
        if node == "LAT" or node == "LON": #Maybe I should change this to X & Y and 2 decimals (still sub-metre accuracy)
            #This is to round off the lat and long so that the filesize isn't as large
            # 5 decimal places comes out to 0.7871m of accuracy error E/W at 45 degrees N/S
            rowData.append(round(float(node.text),5))
        else:
            rowData.append(node.text.encode("utf-8"))
    else:
        rowData.append("")
    return rowData

print "\nReading the Food Check Peel XML..."
print "\n\t...please be patient while it reads and writes the files..."

location = root.findall("ROW")
for p in location:
    locationStatus = getInfo(p)
    if locationStatus:
        outputData.append(locationStatus)

print "\n...finished parsing the XML, starting to write the file..."

outputFile = open(outFileName, "wb")
#This writes the CSV using Python's CSV plugin
# quoting = QUOTE_MINIMAL is used for a couple of reasons:
#   (1) It quotes text only where there are special characters that would interfere with the correct use of the CSV
#   (2) It keeps the file size to a minimum and allows the end user more control over how the field types are interpreted
# As an alternate, QUOTE_NONNUMERIC could be used to quote all fields that contain text. This, however, makes non-quoted fields of type float (for better or worse)
# See http://docs.python.org/2/library/csv.html for more options and info
writeCSV = csv.writer(outputFile, quoting=csv.QUOTE_MINIMAL)
writeCount = 0
for row in outputData:
    writeCSV.writerow(row)
    writeCount += 1

outputFile.close()

print "\n------------------------------------------------------------"
print "\nWrote " + str(writeCount) + " rows out to the " + str(outFileName) + " output file."
print "Great success!  Double check the output, though!"
