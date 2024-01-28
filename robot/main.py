import cv2

from screen import Screen
from camera import Camera

from sensorFusion import SensorFusion
from navigator import Navigator

from audioDetector import checkAudio
from timer import Timer

camera = Camera()

sensorFusion = SensorFusion(camera)
sensorFusion.startFilters()

navigator = Navigator()
screen = Screen()

audioChecker = Timer(3)

navigator.report()

while True:
    frame = camera.readFrame()
    navigator.update()
    sensorFusion.updateInterestMap()

    navigator.move(sensorFusion.getInterestMap())

    if(audioChecker.check()):
        if(checkAudio()):
            navigator.report()

    #screen.draw()

    if cv2.waitKey(1) == ord('q'):
        break
    
navigator.stop()
camera.close()
cv2.destroyAllWindows()
