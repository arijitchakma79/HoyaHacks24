import time

class Timer:
    def __init__(self, duration):
        self.__duration = duration
        self.__start = time.time()

    def setDuration(self, duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

    def check(self):
        if((time.time() - self.__start) > self.__duration):
            self.__start = time.time()
            return True
        return False