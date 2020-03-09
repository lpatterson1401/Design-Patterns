#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:33:44 2020

@author: ladonnapatterson
"""

def count_to(count):
    
    #create a list
    numbers = ["one", "two", "three", "four", "five"]
    
    #built in iterator returns 5 tuples or pairs
    iterator = zip(range(count), numbers) #range tells up to what number you can count
    
    
    #iterate through the list
    #extract the numbers
    #place them in a generator called number
    for position, number in iterator:
        
        yield number
        
#test the generator returned by the iterator
for num in count_to(3):
    print("{}".format(num))
    
for num in count_to(4):
    print("{}".format(num))
    
    
    