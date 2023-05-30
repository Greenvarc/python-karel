from stanfordkarel import *
def main():
    turn_left()
    pick_beeper()
    while (front_is_clear()):
        move()
        pick_beeper() if beepers_present() else ''
    turn_left()
    for i in range(4):
        move()
    pick_beeper()
    turn_left()
    while (front_is_clear()):
        move()
        pick_beeper() if beepers_present() else ''
    for y in range(3):
        turn_left()
    for i in range(4):
        move()
    pick_beeper()
    for y in range(3):
        turn_left()
    while (front_is_clear()):
        move()
        pick_beeper() if beepers_present() else ''
    turn_left()
    for i in range(4):
        move()
    pick_beeper()
    turn_left()
    while (front_is_clear()):
        move()
        pick_beeper() if beepers_present() else ''






if __name__=="__main__":
    run_karel_program()