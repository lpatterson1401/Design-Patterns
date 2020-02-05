#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:19:29 2020

@author: ladonnapatterson

Prototype

-create many objects efficiently
-cloning

"""

import copy

class Prototype:
    
    def __init__(self):
        self._objects = {}
        
    def register_objects(self, name, obj):
        self._objects[name] = obj
        
    def unregister_objects(self):
        self._objects[name]
        
    def clone(self, name, **attr):
        
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
    
class Car:
    
    def __init__(self):
        self.name = "Tesla"
        self.color = "White"
        self.options = "Model 3"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
    
c = Car()
prototype = Prototype()
prototype.register_objects('Tesla', c)

c1 = prototype.clone('Tesla')
print(c1)