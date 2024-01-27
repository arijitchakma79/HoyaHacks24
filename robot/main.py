from screen import Screen
from navigator import Navigator
from camera import Camera
import cv2

from sensorFusion import SensorFusion

camera = Camera()

sensorFusion = SensorFusion(camera)
sensorFusion.startFilters()

while True:
    frame = camera.readFrame()
    print("main")
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