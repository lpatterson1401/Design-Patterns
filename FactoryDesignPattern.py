# -*- coding: utf-8 -*-
"""
Practice Design Patterns
LaDonna Patterson

Factory Design pattern 
-Creational Pattern
-create objects without exposing the creation logic to the client and refer to
newly created objects with a common interface

"""

'''Factory Design Pattern'''

class Dog:
    
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Woof!"
    
class Cat:
    
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Meow!"
    
def get_pet(pet="dog"):
    
    '''The factory method'''
    
    pets = dict(dog=Dog("Duke"), cat=Cat("Garfield"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())