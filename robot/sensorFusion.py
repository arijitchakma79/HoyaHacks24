from filters.filter import Filter, FilterResult
from filters.depthFilter import DepthFilter

import numpy as np
import matplotlib.pyplot as plt

class SensorFusion:
    def __init__(self, camera):
        self.__camera = camera

        self.__interestMap = np.ones(256)

        self.__filters = []
        self.__addFilters()

    def __addFilter(self, filter):
        self.__filters.append(filter)

    def __addFilters(self):
        self.__addFilter(DepthFilter(self.__camera))

    def startFilters(self):
        for filter in self.__filters:
            filter.start()

    def getInterestMap(self):
        return self.__interestMap
    
    def updateInterestMap(self):
        for filter in self.__filters:
            filterResult = filter.popResult()

            if(filterResult is not None):
                self.__saveHist(filterResult.getInterestMap(), filter.getName()+"Interest.png")

    def __saveHist(self, hist, file):
        plt.figure()
        plt.title("Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.plot(hist)
        plt.xlim([0, hist.shape[0]])
        plt.savefig(file)
