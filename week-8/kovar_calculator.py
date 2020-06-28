# ============================================
# Title:  kovar_calculator.py
# Author: Sarah Kovar
# Date:   19 June 2020
# Modified by: Sarah Kovar
# Description: Python add, subtract, divide functions.
# ===========================================

#name displayed on screen
first_name = 'Sarah'
last_name = 'Kovar'
print(first_name + ' ' + last_name)

#add function
def add(number01, number02):
    return number01 + number02

#subtract function
def subtract(number01, number02):
    return number01 - number02

#divide function
def divide(number01, number02):
    return number01 / number02

#print output
print(add(1, 2))
print(subtract(4, 1))
print(divide(8, 2))