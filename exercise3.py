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
        elif answer == "N":
            print("Replace cables and try again.")
        else:
            print("Please input y/n answer only.")
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
                    else:
                        print("Please input y/n answer only.")
                elif answer == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")

# Display error message when entering answers that are neither y or n
                else:
                    print("Please input y/n answer only.")
            else:
                print("Please input y/n answer only.")
        else:
            print("Please input y/n answer only.")
    else:
        print("Please input y/n answer only.")

    return

diagnose_car()

"""

 Test Case 1
    Input: Y
    Output: Are the battery terminals corroded?
    Errors: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: Y
    Output: Clean terminals and try starting again.
    Errors: When input is neither Y or N and it will prompt message "Please input Y/N answer only"

  Test Case 2
    Input: Y
    Output: Are the battery terminals corroded?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Replace cables and try again.
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"

  Test Case 3
    Input: N
    Output : Does the car make a clicking noise?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input : Y
    Output: Replace the battery.
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"

  Test Case 4
    Input: N
    Output: Does the car make a clicking noise?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Does the car crank up but fail to start?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: Y
    Output: Check spark plug connections.
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"


  Test Case 5
    Input: N
    Output: Does the car make a clicking noise?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Does the car crank up but fail to start?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input:N
    Output3: Does the engine start and then die?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Engine is not getting enough fuel. Clean fuel pump.
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"

  Test Case 6
    Input: N
    Output: Does the car make a clicking noise?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Does the car crank up but fail to start?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Does the engine start and then die?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: Y
    Output: Does your car have fuel injection?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Check to ensure the choke is opening and closing.
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"

  Test Case 7
    Input: N
    Output: Does the car make a clicking noise?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Does the car crank up but fail to start?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: N
    Output: Does the engine start and then die?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: Y
    Output: Does your car have fuel injection?
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    Input: Y
    Output: Get it in for service.
    Error: When input is neither Y or N and it will prompt message "Please input Y/N answer only"
    """

