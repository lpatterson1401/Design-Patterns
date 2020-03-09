#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:42:11 2020

@author: ladonnapatterson
"""
#types module supports dynamic creations
import types

class Strategy:
    '''Strategy'''
    
    def __init__(self, function=None):
        self.name = "Default Strategy"
        
        if function:
            self.execute = types.MethodType(function, self)
            #dynamically set method to new class
        
    def execute(self): #this is what is being replaced dynamically!!!
        print("{} is used!".format(self.name))
        
        
#Replacement Method 1
def strategy_one(self):
    print"{} is used to execute method 1".format(self.name)
    
    
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


#create default strategy
s0 = Strategy()

s0.execute()

#create first variation of default strategy
s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

#create second variation of default strategy
s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()

