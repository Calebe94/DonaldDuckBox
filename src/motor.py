from constants import GPIO_BASE_PATH
from constants import MOTOR_PIN

def init():
    try:
        # Exporting GPIO 13 used by RELAY
        with file(GPIO_BASE_PATH+"/export", "w") as export:
            export.write(MOTOR_PIN)
            export.close()

        # Setting direction as output
        with file(GPIO_BASE_PATH+"/gpio"+MOTOR_PIN+"/direction", "w") as direction:
            direction.write("out")
            direction.close()
    
        return "OK"
    except Exception as error:
        print(error)
        pass

def on():
    print("> Motor ON!")
    
    with file(GPIO_BASE_PATH+"/gpio"+MOTOR_PIN+"/value", "w") as direction:
        direction.write("1")
        direction.close()
    return "OK"
    
def off():
    print("> Motor OFF!")
    with file(GPIO_BASE_PATH+"/gpio"+MOTOR_PIN+"/value", "w") as direction:
        direction.write("0")
        direction.close()
    return "OK"

def switch():
    return "SWITCH MOTOR"