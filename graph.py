#!/usr/bin/env python2
#// File: graph.py
#// Description: [ Take parsed data and represent it graphically ]
#// Current Version: 0.1-0 as of 2014-05-17 written by Alex Loranger
#// This comment has ceased to be!
#//

# import in alphabetical order
# -- 1. Standard Library modules
# -- 2. External/third party packages/modules
# -- 3. Internal/self-written modules 
from collections import Counter 
# import the library and reference it using plt instead of full name
import matplotlib.pyplot as plt # <type: 'module'>
import numpy.numarray as na
import parse

"""
Review of `parse()` function ::
    1. Initialize the raw file.
    2. Read the CSV file with the appropriate delimiter, then close the file.
    3. Initialize an empty list which will be returned by the function.
    4. Grab the first row of the CSV file, the headers/column names, and assign them
    to the `fields` variable, which will be a list.
    5. Iterate over each remaining row in the CSV file, mapping column headers -> row
    values, and add to our list we initialized in step 3.
    6. Return the `parsed_data` variable

"""

# file to be parsed
MY_FILE = "../data/sample_sfpd_incident_all.csv"

# visualize days
def  visualize_days():
    """Visualize data by day of week."""

    # Grab our parsed data that we parsed earlier
    data_file = parse.parse(MY_FILE, "||")

    # Make a new variable, `counter`, from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen each day of the week.
    # -- `Counter` from module `collections` behaves very similarly to Python's
    #    dictionary structure. 
    # -- What we do with `Counter` is iterate through each line item in `data_file`
    #    (which is a list of dictionaries) grabbing each key labeled "DayOfWeek"
    # -- What the `Counter` does is every time is sees the "DayOfWeek" key set to
    #    a value of "Monday", it will give a tally, etc.
    counter = Counter(item["DayOfWeek"] for item in data_file # list comprehension
                                                              # "iterate every dictionary
                                                              # value of every dictionary 
                                                              # key set to "DayOfWeek" for
                                                              # every line item in `data_file`"
    """
    for item in data_file:
        item += item["DayOfWeek"]
        item += "\n"

    """

    # Seperate the x-axis data (days of the week) from the 
    # `counter` variable from te y-axis data (number of incidents for each day)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]

    # `plt.xticks()` only accepts tuples for labeling the x-axis
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # With that y-axis data, assign it to a `matplotlib` plot instance
    plt.plot(data_list)Monday

    # Create the amount of ticks needed for our x-axis, and assign it the labels

    # Save the plot!

    # Close plot file.

# visualize type

# main

#EOF
