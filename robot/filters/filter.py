from abc import ABC, abstractmethod 
from threading import Thread

import numpy as np

class FilterResult:
    def __init__(self, interestMap=np.ones(640), uncertanityMap=np.zeros(640)):
        self.__interestMap = interestMap
        self.__uncertanityMap = uncertanityMap

    def setInterestMap(self, interestMap):
        self.__interestMap = interestMap

    def getInterestMap(self):
        return self.__interestMap
    
    def setUncertanityMap(self, uncertanityMap):
        self.__uncertanityMap = uncertanityMap

    def getUncertanityMap(self):
        return self.__uncertanityMap

class Filter(ABC, Thread):
    def __init__(self, weight = 1.0):
        self.__weight = weight
        self.__stack = []

        self.__width = 640

        Thread.__init__(self)

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight
    
    def getWidth(self):
        return self.__width

    def addResult(self, filterResult):
        self.__stack.append(filterResult)

    def popResult(self):
        if(len(self.__stack) == 0):
            return None

        filterResult = self.__stack.pop(len(self.__stack) - 1)
        return filterResult
    
    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def run(self):
        pass

