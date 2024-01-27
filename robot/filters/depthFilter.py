from filters.filter import Filter, FilterResult

import torch
import cv2
import numpy as np

class DepthFilter(Filter):
    def __init__(self, camera):
        self.__camera = camera
        super().__init__(weight=1.0)

        self.__midas = torch.hub.load('intel-isl/MiDaS','MiDaS_small')
        self.__midas.to('cpu')
        self.__midas.eval()

        self.__transforms = torch.hub.load('intel-isl/MiDaS','transforms')
        self.__transform = self.__transforms.small_transform

    def getName(self):
        return "depthFilter"

    def run(self):
        while True:
            frame = self.__camera.getLastFrameCopy()
            if(frame is None):
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            imgbatch = self.__transform(gray).to('cpu')
            with torch.no_grad():
                prediction = self.__midas(imgbatch)
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size=gray.shape[:2],
                    mode='bicubic',
                    align_corners=False
                ).squeeze()

            output = prediction.cpu().numpy()
           
            hist = np.sum(output, axis=0)
            hist /= np.max(hist)
            hist = 1 - hist

            self.addResult(FilterResult(hist))