# -*- coding: utf-8 -*-
"""
List chapter for automate the boring stuff
"""

# Converting a list to a string with commas 
#and then inserting and before the last occurance

spam = ['apples', 'bananas', 'tofu', 'cats']


def list_converter (lst):
    str=", "
    lst.insert(-1, 'and')
    return(str.join(lst))
    
print(list_converter(spam))
