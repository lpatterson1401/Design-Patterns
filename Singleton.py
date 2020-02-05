#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:56:58 2020

@author: ladonnapatterson


Singleton Design Pattern
-an information cache shared by multiple objects
-Borg Pattern

"""

class Borg:
    '''makes the class attributes global'''
    _shared_data = {} #dictionary for attributes
    
    def __init__(self):
        self.__dict__ = self._shared_data
        
class Singleton(Borg):
    "inherits from Borg class and shares the attributes"
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) #update attribute dictionary with key-value pair
        
    def __str__(self):
        return str(self._shared_data)

'''created a Singleton object and add the first acronym'''    
q = Singleton(LaDonna="LaDonna")
print(q)

'''create another Singleton object and addd it to the dictionary as a key-value pair'''
x = Singleton(Andrea="Andrea")
print(x)

    
    