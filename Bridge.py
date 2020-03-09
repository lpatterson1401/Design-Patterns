#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:23:34 2020

@author: ladonnapatterson
"""

class DrawingAPIOne(object):
    #Implement concrete class one
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!".format(x, y, radius))
        
        
class DrawingAPITwo(object):
    #Implement concrete class two
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!".format(x, y, radius))
    

class  Circle(object):
    #Implement independent abstraction
    
    #initialize attributes
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
        
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
        
        
        
    def scale(self, percent):
        self._radius *= percent
        
        
#Create first circle
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#draw the circle
circle1.draw()

#Create 2nd circle
circle2 = Circle(1, 2, 3, DrawingAPITwo())
circle2.draw()

