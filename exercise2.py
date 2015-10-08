#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Defining the function for determining the sides of the shape


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: number of sides must be >= 3 but <= 10

    Expected Outputs: name of the shape

    Errors: if input is anything else, display "Error"

    """
# Prompt the user to enter number of sides as an integer
    sides = int(raw_input("Number of sides in a regular polygon: "))

# The output for each integer ranging from 3 - 10 inclusively
    if sides == 3:
        print("triangle")
    elif sides == 4:
        print("quadrilateral")
    elif sides == 5:
        print("pentagon")
    elif sides == 6:
        print("hexagon")
    elif sides == 7:
        print("heptagon")
    elif sides == 8:
        print("octagon")
    elif sides == 9:
        print("nonagon")
    elif sides == 10:
        print("decagon")

# Display error when inputting integers outside the range
    else:
        print("Error")


name_that_shape()