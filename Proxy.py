#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:29:43 2020

@author: ladonnapatterson
"""

import time

class Producer:
    #define the resource intensive object to instantiate
    
    def produce(self):
        print("Producer is working hard!")
        
    def meet(self):
        print("Producer has time to meet you!")
        
        
class proxy:
    #define the proxy as the middleman
    def __init__(self):
        self.occupied = "Yes"
        self.producer = None
        
        
    def produce(self):
        print("Checking to see if the the producer is ready")
        
        if self.occupied == "No":
            #if producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            
            #producer meets the guest
            self.producer.meet()
        
        else:
            time.sleep(2)
            print("Producer is busy")

#instantiate a proxy
p = proxy()

#make the proxy
p.produce()
