#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:47:09 2020

@author: ladonnapatterson
"""

class Korean:
    def __init__(self):
        self.name = "Korean"
        
    def speak_korean(self):
        return "An-neyong?"
    
class British:
    def __init__(self):
        self.name = "British"
        
    def speak_english(self):
        return "Hello"
    
    
class Adapter:
    #change the generic method name into individualized methods
        def __init__(self, object, **adapted_method):
        #change the name of the object
            self._object = object
        
        #add a new dict item to establish the mapping betweent the 
        #generic method, for example: speak(), and the concrete method
        
            self.__dict__.update(adapted_method)
        
        
        def __getattr__(self, attr):
            return getattr(self._object, attr)
        
#list to store speaker objects
objects = []
    
#create Korean object
korean = Korean()
    
#create British object
british = British()
    
#add the objects to the list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))
    
    
for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
        

            
            
            