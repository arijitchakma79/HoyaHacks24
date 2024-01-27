from serial import Serial

class GPS:
    def __init__(self):
        self.__sp = Serial('/dev/ttyACM0', 4800, timeout=1.0)
        self.__timeoutStep = 100

    def __convert(self, latStr, longStr):
        latDeg = int(latStr[0:2])
        latMin = float(latStr[2:len(latStr) - 1]) / 60
        latitude = latDeg + latMin

        longDeg = int(longStr[0:3])
        longMin = float(longStr[3:len(longStr) - 1]) / 60
        longitude = longDeg + longMin
        longitude = -1 * longitude

        return latitude, longitude

    def getCoords(self):
        latitude = None
        longitude = None

        for t in range(self.__timeoutStep):
            try:
                line = self.__sp.readline().decode('ascii', errors='replace')
                line = line.strip()

                if(line.startswith("$GPGGA")):
                    parts = line.split(",")

                    latStr = parts[2]
                    longStr = parts[4]

                    if(latStr != '' and longStr != ''):
                        latitude, longitude = self.__convert(latStr, longStr)
                    break
            except Exception as e:
                print("GPS Error: " + str(e))
                break


        return latitude, longitude

    def close(self):
        self.__sp.close()


gps = GPS()

"""
while True:
    lat, long = gps.getCoords()
    print("Latitude: " + str(lat) + " Longitude: " + str(long))"""
