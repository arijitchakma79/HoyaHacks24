from filters.filter import Filter, FilterResult

import numpy as np
import scipy.stats as stats

import math
import time

class ForwardBias(Filter):
    def __init__(self, weight=0.15):
        super().__init__(weight)
        
    def getName(self):
        return "forwardBias"
    
    def run(self):
        mu = 0
        variance = 1

        sigma = math.sqrt(variance)

        x = np.linspace(mu - 3*sigma, mu + 3*sigma, self.getWidth())
        hist = stats.norm.pdf(x, mu, sigma)
        hist /= np.max(hist)

        while True:
            #print("forward")
            self.addResult(FilterResult(self, hist))
            time.sleep(0.5)