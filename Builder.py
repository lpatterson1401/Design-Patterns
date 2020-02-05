#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:45:32 2020

@author: ladonnapatterson



Builder Pattern
-director
-abstract builder: interfaces
-concrete builder: implements interfaces
-doesn't rely on polymorphism

"""

class Director():
    
    def __init__(self, builder):
        self._builder = builder
        
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_battery_pack()
        
    def get_car(self):
        return self._builder.car
    
class Builder():
    
    def __init__(self):
        self.car = Car()
        
    def create_new_car(self):
        self.car = Car()
        
class ElectricCar(Builder):
    
    def add_model(self):
        self.car.model = "Tesla"
        
    def add_tires(self):
        self.car.tires = "New Tires"
        
    def add_battery_pack(self):
        self.car.battery_pack = "Battery Pack"
        
        
class Car():
    
    def __init__(self):
        self.model = None
        self.tires = None
        self.battery_pack = None
        
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.battery_pack)
    
builder = ElectricCar()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)