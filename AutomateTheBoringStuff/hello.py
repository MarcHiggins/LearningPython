# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:45:34 2020

@author: marcg
"""
### Very easy program to input a name

print ("Hello, world!")
##ask for an input name
print ("What is your name?")
Name = input()

print("Nice to meet you, " + Name)

print("The length of your name is:")
print(len(Name))

print("What is your age?") ##ask for their age
Age = input()
print("You will be " + str(int(Age)+1)+ " in a year.")

