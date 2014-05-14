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

    # Let's first address the column headers that came in the CSV file
    fields = csv_data.next()
    # We were able to call the `.next()` method on `csv_data` because it is a generator
    # -- Generator functions allow you to declare a function that behaves like an iterator
    #    i.e. it can be used in a `for` loop

    # Let's loop over each row
    # -- With each loop we will add a dictionary that maps a field(column headers) 
    #    to the value in the CSV cell

    # Iterate over each row in csv_data
    for row in csv_data:
        # With each loop append a dictionary using `dict()` to our list (starting empty)
        # We use python's built-in `zip()` to zip together header -> value to make our 
        # dictionary of every row
        # ex: zip('ABCD', 'xy') --> Ax By
        parsed_data.append(dict(zip(fields, row)))


    # Close CSV file

    return parsed_data


#EOF
