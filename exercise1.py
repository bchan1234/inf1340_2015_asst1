#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

money = 2000
share_value = 900.00
money_paid = money * share_value
buy_commission = 0.03 * money_paid

share_sold_total = money * 942.75
sold_commission = share_sold_total * 0.03
money_left = share_sold_total - money_paid - sold_commission - buy_commission


