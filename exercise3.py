#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: Y/N

    Expected Outputs: troubleshooting message

    Errors: when inputting answers other than y/n

    """

    answer = raw_input("Is the car silent when you turn the key? ")

    if answer == "Y":
        answer = raw_input("Are the battery terminals corroded? ")
        if answer == "Y":
            print("Clean terminals and try starting again.")
        if answer == "N":
            print("Replace cables and try again.")
    elif answer == "N":
        answer = raw_input("Does the car make a clicking noise? ")
        if answer == "Y":
            print("Replace the battery.")
        elif answer == "N":
            answer = raw_input("Does the car crank up but fail to start? ")
            if answer == "Y":
                print("Check spark plug connections.")
            elif answer == "N":
                answer = raw_input("Does the engine start and then die? ")
                if answer == "Y":
                    answer = raw_input("Does your car have fuel injection? ")
                    if answer == "Y":
                        print("Get it in for service.")
                    elif answer == "N":
                        print("Check to ensure the choke is opening and closing.")
                elif answer == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")


# diagnose_car()