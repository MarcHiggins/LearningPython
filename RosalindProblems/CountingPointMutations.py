# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:30:39 2020

@author: marcg


Need to write a function to identify the amount of 
mismatched basepairs in two strings
"""


def mismatches(s,t):
    number = 0
    for i in range(0, len(s)):
        if s[i] == t[i]:
            continue
        else:
            number += 1
    print(number)
    
s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'

mismatches(s,t)
