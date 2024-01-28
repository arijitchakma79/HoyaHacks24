from filters.filter import Filter, FilterResult

from filters.depthFilter import DepthFilter
from filters.forwardBias import ForwardBias
from filters.randomBias import RandomBias

import numpy as np
import matplotlib.pyplot as plt

class SensorFusion:
    def __init__(self, camera, debug=True):
        self.__camera = camera
        self.__debug = debug

        self.__interestMap = np.zeros(640)

        self.__filters = []
        self.__filterResults = {"depthFilter":None,"forwardBias":None,"randomBias":None}
        self.__addFilters()

    def __addFilter(self, filter):
        self.__filters.append(filter)

    def __addFilters(self):
        self.__addFilter(DepthFilter(self.__camera))
        self.__addFilter(ForwardBias())
        self.__addFilter(RandomBias())

    def startFilters(self):
        for filter in self.__filters:
            filter.start()

    def getInterestMap(self):
        return self.__interestMap
    
    def updateInterestMap(self):
        for filter in self.__filters:
            filterResult = filter.popResult()

            if(filterResult is not None):
                self.__filterResults[filter.getName()] = filterResult
                #self.__saveHist(filterResult.getInterestMap(), filter.getName()+"Interest.png")

        self.__interestMap = np.zeros(640)
        for key, value in self.__filterResults.items():
            if self.__filterResults[key] is None:
                continue
            self.__interestMap += self.__filterResults[key].getInterestMap() * self.__filterResults[key].getFilter().getWeight()

        self.__interestMap /= np.max(self.__interestMap)
        
        plt.figure()
        plt.title("Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.plot(self.__interestMap)
        plt.xlim([0, self.__interestMap.shape[0]])
        plt.show(block=True)
        #self.__saveHist(self.__interestMap, "interestMap.png")

    def __saveHist(self, hist, file):
        if(self.__debug == False):
            return

        plt.figure()
        plt.title("Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.plot(hist)
        plt.xlim([0, hist.shape[0]])
        plt.savefig("temp/" + file)

