import random

def has_presence():
    true_or_false = random.random()
    
    if( true_or_false*100 > 70):
        print("> Has Presence !")
        return True
    return False