from robot import Robot
from gps import GPS

from client import Client
from timer import Timer
import numpy as np
from time import strftime
from datetime import datetime

class Navigator:
    def __init__(self):
        self.__robot = Robot()
        self.__robot.stop()

        self.__wayPoints = []

        self.__client = Client()
        self.__gps = GPS()

        self.__sendLocationTimer = Timer(5)

        self.__oldError=0
        self.__kp=1.7
        self.__kd=0.6

    def __scoutSetup(self):
        pass

    def update(self):   
        if(self.__sendLocationTimer.check()):
            lat, long = self.__gps.getCoords()
            if(lat is not None and long is not None):
                self.__client.sendRobotLocation(lat, long)
                print("Sending Location...")

    def report(self):
            #lat, long = self.__gps.getCoords()
            lat,long = 38.906646, -77.07483766666

            time = datetime.now().strftime("%H:%M")
            dayLong = datetime.now().strftime("%A")
            days = {'Monday':'M',"Tuesday":'T','Wednesday':'T',"Thrusday":'Th',"Friday":'F',"Saturday":'Sat',"Sunday":'Sun'}
            day = days[dayLong]

            if(lat is not None and long is not None):
                self.__client.sendReport(lat, long, time, day)
                print("Sending Location...")

    def move(self, interestMap):
        posX =np.argmax(interestMap)

        error = interestMap.shape[0] - posX
        D = self.__oldError = error

        PD = error * self.__kp + D * self.__kd

        motor1 = 70 - PD
        motor2 = 70 + PD

        if(motor1>100): motor1=100
        if(motor2>100): motor2=100

        if(motor1<40): motor1=40
        if(motor2<40): motor2=40

        self.__robot.setMotor1(motor1)
        self.__robot.setMotor2(motor2)

        self.__oldError = error
        


    def stop(self):
        self.__robot.stop()