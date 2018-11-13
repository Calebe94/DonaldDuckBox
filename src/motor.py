from constants import GPIO_BASE_PATH
from constants import MOTOR_PIN
import DeviceSerial

class Motor(object):
    def __init__(self):
        try:
            self.__device = DeviceSerial.DeviceSerial("/dev/ttyACM0", 9600)
        except Exception as identifier:
            print("> Motor: "+str(identifier))
            pass
    
    def on(self):
        try:
            self.__device.write('l')
            pass
        except Exception as identifier:
            print("> Motor ON: "+str(identifier))
            pass
    
    def off(self):
        try:
            self.__device.write('d')
            pass
        except Exception as identifier:
            print("> Motor OFF: "+str(identifier))
            pass

    def switch(self):
        return "SWITCH"
