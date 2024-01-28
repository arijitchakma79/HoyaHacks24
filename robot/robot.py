from gpiozero import LED, PWMOutputDevice
from time import sleep
from gpiozero.pins.lgpio import LGPIOFactory

factory = LGPIOFactory(chip=4)

class Robot:
   def __init__(self):
      self.__motorA1 = LED(16, pin_factory=factory, active_high =True)
      self.__motorA2 = LED(18, pin_factory=factory, active_high =True)

      self.__motorB1 = LED(22, pin_factory=factory, active_high =True)
      self.__motorB2 = LED(8, pin_factory=factory, active_high =True)

      self.__pwm1 = PWMOutputDevice(12, pin_factory=factory,frequency=1000)
      self.__pwm2 = PWMOutputDevice(13, pin_factory=factory,frequency=1000)

      self.__motorA1.off()
      self.__motorA2.on()

      self.__motorB1.off()
      self.__motorB2.on()

      self.stop()

   def setMotor1(self, speed):
      if(speed==0):
         self.__motorA2.off()
      else:
         self.__motorA2.on()
      self.__pwm1.value = (speed / 100)
   
   def setMotor2(self, speed):
      if(speed==0):
         self.__motorB2.off()
      else:
         self.__motorB2.on()
      self.__pwm2.value = (speed / 100)

   def stop(self):
      self.setMotor1(0)
      self.setMotor2(0)
