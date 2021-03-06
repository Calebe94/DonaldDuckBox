import random, DeviceSerial
from constants import GPIO_BASE_PATH
from constants import PIR_PIN
from serial import Serial

class Presence(object):
    def __init__(self):
        try:
            self.__device = DeviceSerial.DeviceSerial("/dev/ttyACM0", 9600)
        except Exception as identifier:
            print("> Presence: "+str(identifier))
            pass

    def __read(self):
        try:
            self.__device.write('g')
            response = self.__device.read()
            if response.strip() == "1":
                return True
            else:
                return False
            # print(response)
            pass
        except Exception as identifier:
            print("> Presence READ: "+str(identifier))
            return False

    def has_presence(self):
        # true_or_false = random.random()
        
        # if( true_or_false*100 > 70):
        #     print("> Has Presence !")
        #     return True
        # return False
        return self.__read()
