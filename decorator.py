#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:18:21 2020

@author: ladonnapatterson
"""

from functools import wraps


#make the decorator transparent
def make_blink(function):
    @wraps(function)
    
    
    #define the inner function
    def decorator():
        #grab the return value 
        ret = function()
        
        #add new functionality
        return "<blink>" + ret + "</blink>"
        
        
    return decorator
    
    
@make_blink #adds tags to original string  
def hello_world():
    
    #this is the original
    return "Hello, World!"

    #check the result of decorating
print(hello_world())

#check if the function name is still the same
print(hello_world.__name__)

#check if the docstring is still the same
print(hello_world.__doc__)