from filters.filter import Filter, FilterResult

import numpy as np
import scipy.stats as stats

import math

class ForwardBias(Filter):
    def __init__(self, weight=0.4):
        super().__init__(weight)
        
    def getName(self):
        return "forwardBias"
    
    def run(self):
        while True:
            mu = 0
            variance = 1

            sigma = math.sqrt(variance)

            x = np.linspace(mu - 3*sigma, mu + 3*sigma, self.getWidth())
            hist = stats.norm.pdf(x, mu, sigma)
            hist /= np.max(hist)

            self.addResult(FilterResult(hist))