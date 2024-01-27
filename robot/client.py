import requests

class Client:
    def __init__(self, ipAddress = "161.35.251.92"):
        self.__address = "http://" + str(ipAddress)

    def __gps2str(self, lat, long):
        return "lat="+str(lat)+"&"+"long="+str(long)

    def sendRobotLocation(self, latitude, longitude):
        response = requests.get(self.__address + "/robot-set-location?"+self.__gps2str(latitude, longitude))