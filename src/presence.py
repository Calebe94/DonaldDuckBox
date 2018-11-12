import random

from constants import GPIO_BASE_PATH
from constants import PIR_PIN
def init():
    try:
        # Exporting GPIO 13 used by RELAY
        with file(GPIO_BASE_PATH+"/export", "w") as export:
            export.write(PIR_PIN)
            export.close()

        # Setting direction as output
        with file(GPIO_BASE_PATH+"/gpio"+PIR_PIN+"/direction", "w") as direction:
            direction.write("out")
            direction.close()
    
        return "OK"
    except Exception as error:
        print(error)
        pass
    
    return "OK"

def read():
    try:
        with file(GPIO_BASE_PATH+"/gpio"+PIR_PIN+"/value", "r") as value:
            if( value.read() == "1"):
                return True
            else: 
                return False
    except Exception as error:
        print(error)
        pass
    return False

def has_presence():
    # true_or_false = random.random()
    
    # if( true_or_false*100 > 70):
    #     print("> Has Presence !")
    #     return True
    # return False
    return read()