# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:10:46 2020

@author: marcg
"""
import sys

number = int(input("Please enter a number: "))

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        
    while result == 1:
        print (result)
        break
        
    while result != 1:
        print (result)
        number = result
        return collatz(number)

collatz(number)
