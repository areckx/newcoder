# -*- coding: utf-8 -*-
#!/usr/bin/python2
#// File: parse.py
#// Description: [ parses a csv file and represents its data in a graph ]
"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""
#// Current Version: 0.1-0 as of 2014-mm-dd written by Alex Loranger
#// This comment has ceased to be!
#//
import csv

MY_FILE = "data/sample_sfpd_incident_all.csv"

# In defining the function, we know that we want it to give a CSV file, as well as
# the delimiter in which the CSV file uses to delimit each element/column
def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

# We also know that we want to return a JSON-like object. A JSON file/object is just 
# a collection of dictionaries, much like Python's dictionary

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    # second `delimiter` refers to parse() argument
    # `csv_data` is now an iterator, we can get each element one at a time
    csv_data = csv.reader(opened_file, delimiter = delimiter)

    # Build a data structure to return parsed data

    # set up an empty list 
    parsed_data = []


    # Close CSV file

    return parsed_data


#EOF
