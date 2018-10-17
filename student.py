import pigo
import time  # import just in case students need
import random
from math import cos, sin

# setup logs
import logging
LOG_LEVEL = logging.INFO
LOG_FILE = "/home/pi/PnR-Final/log_robot.log"  # don't forget to make this file!
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)


class Piggy(pigo.Pigo):
    """Student project, inherits teacher Pigo class which wraps all RPi specific functions"""

    def __init__(self):
        """The robot's constructor: sets variables and runs menu loop"""
        print("I have been instantiated!")
        # Our servo turns the sensor. What angle of the servo( ) method sets it straight?
        self.MIDPOINT = 86
        # YOU DECIDE: How close can an object get (cm) before we have to stop?
        self.SAFE_STOP_DIST = 30
        self.HARD_STOP_DIST = 15
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.LEFT_SPEED = 150
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.RIGHT_SPEED = 155
        # This one isn't capitalized because it changes during runtime, the others don't
        self.turn_track = 0
        # Our scan list! The index will be the degree and it will store distance
        self.scan = [None] * 180
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        if __name__ == "__main__":
            while True:
                self.stop()
                self.menu()

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {"n": ("Navigate forward", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "c": ("Calibrate", self.calibrate),
                "s": ("Check status", self.status),
                "h": ("Open House", self.open_houe),
                "q": ("Quit", quit_now),
                "f": ("Forward", self.move_ahead),
                "l": ("Turn left", self.left_turn),
                "r": ("Turn right", self.right_turn)}
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = raw_input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    # YOU DECIDE: How does your GoPiggy dance?
    def move_ahead(self):
        self.encF(int(input("\nhow many revolutions \n")))
        pass
    def left_turn(self):
        self.encL(int(input("\nhow many revolutions \n")))
        pass
    def right_turn(self):
        self.encR(int(input("\nhow many revolutions \n ")))
        pass
        """executes a series of methods that add up to a compound dance"""

    def dance(self):
        if not self.safe_to_dance():
            print("\nnot safe to dance \n")
            return
        print("\ndancing \n")
        self.s_curve_dance()
        for x in range(5):
            self.wheelie_back()
        self.figure_eight()
        self.surprise()
        """
       
        self.      
        """

    #dances


    def s_curve_dance(self):
        """moves in a s pattern forward"""
        self.fwd()
        self.set_speed(200,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(175,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(150,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(175,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(200,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(200,175)
        time.sleep(.5)
        self.fwd()
        self.set_speed(200,150)
        time.sleep(.5)
        self.fwd()
        self.set_speed(200,175)
        time.sleep(.5)
        self.fwd()
        self.set_speed(200,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(175,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(150,200)
        time.sleep(.5)
        self.fwd()
        self.set_speed(175,200)
        time.sleep(.5)


    def wheelie_back(self):
        """pitiful attempt to pick the back wheels up"""
        self.set_speed(250,250)
        self.encF(5)
        self.encB(18)


    def figure_eight(self):
        """makes a figure eight"""
        self.set_speed(200,200)
        self.encR(8)
        self.fwd()
        self.set_speed(100,200)
        time.sleep(2)
        self.fwd()
        self.set_speed(200,100)
        time.sleep(4)
        self.fwd()
        self.set_speed(100,200)
        time.sleep(2)
        self.set_speed(200,200)

    #gart
    def surprise(self):
        """creates the coolest move you have ever seen"""
        for x in range(2):
            self.encF(30)
            self.encL(5)
            self.encB(5)
            self.encR(10)
            self.encB(5)
            self.encL(5)
            self.encB(5)
            self.encR(10)
            self.encB(5)
            self.encL(5)
            self.encB(5)
            self.encR(10)
            self.encB(5)
            self.encL(5)
            self.encB(5)
            self.encR(10)
            self.encB(5)

    #yuke
    def dancing_forward(self):
        """head rotate with its body"""
        for x in range(3):
            self.servo(self.MIDPOINT - 30)
            self.encR(2)
            self.servo(self.MIDPOINT)
            self.encF(5)
            self.servo(self.MIDPOINT + 30)
            self.encL(2)
            self.servo(self.MIDPOINT)
            self.encF(5)


    def safe_to_dance(self):
        """completes circle while checking for obstructions"""
        # check for obstructions
        for x in range(4):
            if not self.is_clear():
                return False
            self.encR(7)
        #no problems
        return True

        print("\n---- LET'S DANCE ----\n")
        ##### WRITE YOUR FIRST PROJECT HERE

        self.encF(18)
        self.encL(50)
        for x in range(1):
            self.servo(30)
        for x in range(1):
            self.servo(150)
        self.encB(18)
        self.encR(18)
        pass

    def obstacle_count(self):
        """scans and estimates the number of obstacles within sight"""
        self.wide_scan()
        found_something = False
        counter = 0
        for ang, distance in enumerate(self.scan):
            if distance and distance < 200 and not found_something:
                found_something = True
                counter += 1
                print("Object # %d found, I think" % counter)
            if distance and distance > 200 and found_something:
                found_something = False
        print("\n----I SEE %d OBJECTS----\n" % counter)

    def safety_check(self):
        """subroutine of the dance method"""
        self.servo(self.MIDPOINT)  # look straight ahead
        for loop in range(4):
            if not self.is_clear():
                print("NOT GOING TO DANCE")
                return False
            print("Check #%d" % (loop + 1))
            self.encR(8)  # figure out 90 deg
        print("Safe to dance!")
        return True

    def nav(self):
        """auto pilots and attempts to maintain original heading"""
        logging.debug("Starting the nav method")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        while True:
            if self.is_clear():
                self.cruise()
            else:
                self.encR(10)

    def cruise(self):
        """ drive straight while path is clear """
        self.fwd()
        while self.dist() > self.SAFE_STOP_DIST:
            time.sleep(.5)
        self.stop()
####################################################
############### STATIC FUNCTIONS

def error():
    """records general, less specific error"""
    logging.error("ERROR")
    print('ERROR')


def quit_now():
    """shuts down app"""
    raise SystemExit

##################################################################
######## The app starts right here when we instantiate our GoPiggy


try:
    g = Piggy()
except (KeyboardInterrupt, SystemExit):
    pigo.stop_now()
except Exception as ee:
    logging.error(ee.__str__())
