#!/usr/bin/python
import abc

class base_fun(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self):
        return
