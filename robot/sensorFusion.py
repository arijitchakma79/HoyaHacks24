import numpy as np
from filters.filter import Filter, FilterResult

from filters.depthFilter import DepthFilter

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
        pass
