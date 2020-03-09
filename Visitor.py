#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:11:13 2020

@author: ladonnapatterson
"""

class House(object): #class that is visited
    def accept(self, visitor):
    #Interface to accept the visitor
        visitor.visit(self)
        
    def  work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) #reference to hvac specialist in the house object
        
    def work_on_electricity(self, electrician):
        #reference to the electrician inside the house object
        print(self, "worked on by", electrician)
        
    def __str__(self):
        #return the class name when the house obj is printed
        return self.__class__.__name__
    
    
class Visitor(object):
    #abstract visitor
    def __str__(self):
        return self.__class__.__name__
    
class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)
        
class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)
        

#create specialists
hv = HvacSpecialist()
e = Electrician()

#create house object
home = House()

#let the house accept the specialist and work by involeing the visit() method
home.accept(hv)

home.accept(e)