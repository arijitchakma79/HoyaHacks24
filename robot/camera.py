import cv2
import numpy as np

class Camera:
    def __init__(self):
        self.__cap = cv2.VideoCapture(0)

        if not self.__cap.isOpened():
            print("Cannot open camera")
            exit()

        self.__lastFrame = None

    def readFrame(self):
        ret, frame = self.__cap.read()
        self.__lastFrame = frame

        return frame
    
    def getLastFrameCopy(self):
        if(self.__lastFrame is None):
            return None
        return self.__lastFrame.copy()

    def close(self):
        self.__cap.release()