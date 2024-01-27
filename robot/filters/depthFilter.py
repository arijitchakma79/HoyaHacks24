from filters.filter import Filter

import torch
import cv2

class DepthFilter(Filter):
    def __init__(self, camera):
        self.__camera = camera
        super().__init__(weight=1.0)

        self.__midas = torch.hub.load('intel-isl/MiDaS','MiDaS_small')
        self.__midas.to('cpu')
        self.__midas.eval()

        self.__transforms = torch.hub.load('intel-isl/MiDaS','transforms')
        self.__transform = self.__transforms.small_transform

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
            #output_norm = cv2.normalize(output, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

            cv2.imwrite("depthMap.png", output)
            