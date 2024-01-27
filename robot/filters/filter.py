from abc import ABC, abstractmethod 
from threading import Thread

import numpy as np

class FilterResult:
    def __init__(self, interestMap=np.ones(256), uncertanityMap=np.zeros(256)):
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

        Thread.__init__(self)

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight
    
    @abstractmethod
    def run(self):
        pass

