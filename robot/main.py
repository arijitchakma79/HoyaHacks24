from screen import Screen
from navigator import Navigator
from camera import Camera
from sensorFusion import SensorFusion

from gps import GPS
from client import Client

import cv2
from timer import Timer

#camera = Camera()

#sensorFusion = SensorFusion(camera)
#sensorFusion.startFilters()

client = Client()
gps = GPS()

sendLocationTimer = Timer(5)

while True:
    #frame = camera.readFrame()
    #print("main")

    if(sendLocationTimer.check()):
        lat, long = gps.getCoords()
        print(lat)
        if(lat is not None and long is not None):
            client.sendRobotLocation(lat, long)
            print("Sending Location...")

    #sensorFusion.updateInterestMap()

    if cv2.waitKey(1) == ord('q'):
        break

#camera.close()
cv2.destroyAllWindows()

navigator = Navigator()

"""
screen = Screen()
while True: 
    screen.draw()
"""