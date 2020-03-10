#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:59:09 2020

@author: ladonnapatterson
"""
#abstract handler
#find handler in case one is not available
class Handler:
    
    def __init__(self, successor):
        #define who is the next handler
        self._successor = successor
        
        
    def handle(self, request):
        handled = self._handle(request)#if handled stop
        
        if not handled:
            self._successor.handle(request)
            
            
    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass")
        
        
class ConcreteHandler1(Handler):
    
    def _handle(self, request):
        if 0 < request <= 10: #condition for handling
            print("Request {} handled in handler 1".format(request)) #condition for handling
            return True #indicates request has been handled
        
class DefaultHandler(Handler):
    
    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True #indicates request was handled
    
class Client:
    
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))
        
        
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)
            
#create a client
c = Client()

#create requests
requests = [2, 5, 30]

#send the request
c.delegate(requests)