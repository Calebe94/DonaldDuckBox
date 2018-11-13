from serial import Serial
import serial.tools.list_ports, os

class DeviceSerial(object):
    def __init__(self, port, baudrate):
    	self.baudrate = baudrate
    	self.port 	  = port
        self.__connection = False
        try:
            self.__device = Serial(port, baudrate=baudrate, timeout=1)
            self.__connection = True
        except Exception as e:
            self.__connection = False
            print("Erro: %s"%e)

    def read(self):
        try:
            resposta = self.__device.read(500)
            if resposta == '':
                return('TIMEOUT')
            else:
                return resposta
        except Exception as e:
            self.__connection = False
            self.close()

    def write(self, data):
        try:
            for char in data:
                self.__device.write(char)
            self.__device.write("\n")
        except Exception as e:
            print("Erro: %s"%e)
            self.__connection = False
            self.close()

    def close(self):
        try:
            self.__device.close()
        except Exception as e:
            print("Erro: %s"%e)

    def is_connected(self):
        return os.path.exists(self.port)
    
    def ports(self):
        ports = list(serial.tools.list_ports.comports())  
        for port_no, description, address in ports:
            if 'USB' in description:
                # print(port_no)
                return port_no
# def main():
#     tiva = Tiva(TIVA_ADDRESS, 9600)
#     tiva.start()