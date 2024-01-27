from screen import Screen
from navigator import Navigator
from camera import Camera
from sensorFusion import SensorFusion

import cv2


camera = Camera()

sensorFusion = SensorFusion(camera)
sensorFusion.startFilters()



while True:
    frame = camera.readFrame()
   
    sensorFusion.updateInterestMap()

    if cv2.waitKey(1) == ord('q'):
        break

camera.close()
cv2.destroyAllWindows()

navigator = Navigator()

"""
screen = Screen()
while True: 
    screen.draw()
"""