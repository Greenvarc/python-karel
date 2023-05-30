from stanfordkarel import *

def look_left()->None:
    if(facing_east()): #->
        return
    elif (facing_north()): #-^
        for i in range(3):
            turn_left()
    elif (facing_west()): #-<
        for i in range(2):
            turn_left()