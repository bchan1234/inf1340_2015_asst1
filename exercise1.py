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
total_money_paid = money_paid + buy_commission


share_sold_total = money * 942.75
sold_commission = share_sold_total * 0.03
#money_left = share_sold_total - money_paid - sold_commission - buy_commission
total_money_recieved = share_sold_total - sold_commission

money_left = total_money_recieved - total_money_paid

if money_left > 0:
    print('Lakshmi made a profit of ' + money_left)
elif money_left < 0:
    # inverting negative value to positive value
    loss = money_left * -1
    print('Lakshmi made a loss of ' + str(loss))
else:
    print('Lakshmi neither made a profit nor a loss')



