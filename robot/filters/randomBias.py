from filters.filter import Filter, FilterResult

import numpy as np
import random

from perlin_noise import PerlinNoise

class RandomBias(Filter):
    def __init__(self, weight=0.2):
        super().__init__(weight)
        self.__noise = PerlinNoise(octaves=1, seed=random.randint(0,99999999)) 
        
    def getName(self):
        return "randomBias"
    
    def run(self):
        offset = 0
        while True:
            x = [(t * 0.003) for t in range(self.getWidth())]

            hist = np.array([self.__noise([t, offset]) for t in x])
            hist = np.abs(hist)
            hist /= np.max(hist)
            #hist = (hist + 1) / 2

            offset += 0.0001
            self.addResult(FilterResult(hist))