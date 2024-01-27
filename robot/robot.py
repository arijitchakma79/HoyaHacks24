import RPi.GPIO as GPIO
from enum import Enum

class Switch(Enum):
    ForwardRight = 0
    ForwardLeft = 1
    BackRight = 2
    BackLeft = 3

class Robot:
    def __pinNumbers(self):
        self.__switchFR = 0
        self.__switchFL = 1
        self.__switchBR = 2
        self.__switchBL = 3

        self.__motor1Dir = 4
        self.__motor2Dir = 5

        self.__motor1PWMPin = 12
        self.__motor2PWMPin = 13

    def __setInputModes(self):
        GPIO.setup(self.__switchFR, GPIO.IN)
        GPIO.setup(self.__switchFL, GPIO.IN)
        GPIO.setup(self.__switchBR, GPIO.IN)
        GPIO.setup(self.__switchBL, GPIO.IN)

        GPIO.setup(self.__motor1Dir, GPIO.OUT)
        GPIO.setup(self.__motor2Dir, GPIO.OUT)
        GPIO.setup(self.__motor1PWM, GPIO.OUT)
        GPIO.setup(self.__motor2PWM, GPIO.OUT)

    def __pwmSetup(self):
        self.__motor1PWM = GPIO.PWM(self.__motor1PWMPin, 1000)	
        self.__motor2PWM = GPIO.PWM(self.__motor2PWMPin, 1000)	

        self.__motor1PWM.start(0)
        self.__motor1PWM.start(1)

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        self.__pinNumbers()
        self.__setInputModes()
        self.__pwmSetup()

    def __setMotorSpeed(self, speed, index):
        dirPin = [self.__motor1Dir, self.__motor2Dir][index]
        if(speed>0):
            GPIO.output(dirPin, GPIO.HIGH)
        else:
            GPIO.output(dirPin, GPIO.LOW)

        pwm = [self.__motor1PWM, self.__motor2PWM][index]
        pwm.ChangeDutyCycle(abs(speed))

    def setMotor1Speed(self, speed):
        self.__setMotorSpeed(speed, 0)

    def setMotor2Speed(self, speed):
        self.__setMotorSpeed(speed, 1)

    def getSwitchData(self):
        #ForwardRight, ForwardLeft, BackRight, BackLeft
        data = [0, 0, 0, 0]

        if(GPIO.input(self.__switchFR) == GPIO.HIGH): 
            data[Switch.ForwardRight] = 1

        if(GPIO.input(self.__switchFL) == GPIO.HIGH): 
            data[Switch.ForwardLeft] = 1

        if(GPIO.input(self.__switchBR) == GPIO.HIGH): 
            data[Switch.BackRight] = 1

        if(GPIO.input(self.__switchBL) == GPIO.HIGH): 
            data[Switch.BackLeft] = 1

        return data
