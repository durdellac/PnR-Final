import pigo
import time  # import just in case students need
import random
from math import cos, sin
from gopigo import *
import logging



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
        self.SAFE_STOP_DIST = 35
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
                "h": ("Open House", self.open_house),
                "q": ("Quit", quit_now),
                "f": ("Forward", self.move_ahead),
                "l": ("Turn left", self.left_turn),
                "r": ("Turn right", self.right_turn),
                "t": ("Test left or right", self.skill_test)}
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = raw_input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    # YOU DECIDE: How does your GoPiggy dance?
    def move_ahead(self):
        i= int(input("\nhow many revolutions \n"))
        enc_tgt(1, 1, i)
        fwd()
        time.sleep(1+(i//18))

    def left_turn(self):
        i= int(input("\nhow many revolutions \n"))
        enc_tgt(1, 1, i)
        left_rot()
        self.turn_track += i
        time.sleep(1 + (i // 18))

    def right_turn(self):
        i= int(input("\nhow many revolutions \n "))
        enc_tgt(1, 1, i)
        right_rot()
        self.turn_track += i
        time.sleep(1 + (i // 18))



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
        count= 0
        """auto pilots and attempts to maintain original heading"""
        logging.debug("Starting the nav method")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        while True:
            if self.pre_distance() > 30:
                self.cruise()
                count= 0
            else:
            #if robot gets stuck
                if count ==10:
                    self.troubleshoot()
                else:
                    self.direction_choice()
                    count += 1

    def troubleshoot(self):
        """stops the robot if there """
        print("It appears that the robot is stuck in a loop")
        print("Would you like to pause the app")
        choice = input ("Y/N")
        if "Y" in choice:
            self.stop()
        elif "N" in choice:
            self.nav()
        else:
            print ("That isn't a valid option")
            self.troubleshoot()

    def pre_distance(self):
        """checks close to robot before cruising"""
        total_dist = 0
        self.servo(self.MIDPOINT - 3)
        total_dist += self.distance()
        time.sleep(.01)
        self.servo(self.MIDPOINT)
        total_dist += self.distance()
        time.sleep(.01)
        self.servo(self.MIDPOINT + 3)
        total_dist += self.distance()
        return (total_dist/3)

    def direction_choice(self):
        """decides which direction to turn for cruise"""
        #current issue: when scanning too close stop command interferes
        m ={}
        m['left_dist'] = 0
        m['mid_left_dist'] = 0
        m['mid_dist'] = 0
        m['mid_right_dist'] = 0
        m['right_dist'] = 0

        self.encL(7)
        for ang in range(self.MIDPOINT + 15, self.MIDPOINT - 15, -3):
            self.servo(ang)
            mes_1 = self.distance()
            mes_2 = self.distance()
            m['left_dist'] += ((mes_1+mes_2)/2)
        self.encR(4)
        for ang in range(self.MIDPOINT + 15, self.MIDPOINT - 15, -3):
            self.servo(ang)
            mes_1 = self.distance()
            mes_2 = self.distance()
            m['mid_left_dist'] += ((mes_1+mes_2)/2)
        self.encR(3)
        for ang in range(self.MIDPOINT + 15, self.MIDPOINT - 15, -3):
            self.servo(ang)
            mes_1 = self.distance()
            mes_2 = self.distance()
            m['mid_dist'] += ((mes_1+mes_2)/2)
        self.encR(3)
        for ang in range(self.MIDPOINT + 15, self.MIDPOINT - 15, -3):
            self.servo(ang)
            mes_1 = self.distance()
            mes_2 = self.distance()
            m['mid_right_dist'] += ((mes_1+mes_2)/2)
        self.encR(4)
        for ang in range(self.MIDPOINT+15, self.MIDPOINT-15, -3):
            self.servo(ang)
            mes_1 = self.distance()
            mes_2 = self.distance()
            m['right_dist'] += ((mes_1+mes_2)/2)
        self.encL(7)
        time.sleep(1)

        if max(m, key=m.get) == 'left_dist':
            self.encL(7)
        elif max(m, key=m.get) == 'mid_left_dist':
            self.encL(3)
        elif max(m, key=m.get) == 'mid_dist':
            pass
        elif max(m, key=m.get) == 'mid_right_dist':
            self.encR(3)
        elif max(m, key=m.get) == 'right_dist':
            self.encR(7)
        else:
            print("rip the display code")
        time.sleep(1)

    def cruise_check(self):
        """proprietary check for obstacles used while driving"""
        total_dist = 0
        self.servo(self.MIDPOINT -7)
        total_dist += self.distance()
        if total_dist > 40:
            total_dist =0
            self.servo(self.MIDPOINT)
            total_dist += self.distance()
            if total_dist > 40:
                total_dist = 0
                self.servo(self.MIDPOINT +7)
                total_dist += self.distance()
                return total_dist
            else:
                return total_dist
        else:
            return total_dist


        return total_dist

    def distance(self):
        """custom distance to subvert self.dist"""
        d= us_dist(15)
        time.sleep(.01)
        print ("DISTANCE MEASURED: " + str(d) + " CM")
        return d



    def cruise(self):
        """ drive straight while path is clear """
        print("cruising")
        self.fwd()
        if self.cruise_check() > 30:
        #scan to check for obstacles while driving
            print("clear while cruising")
            time.sleep(.01)
        else:
            self.stop()
            time.sleep(.1)
            print("stopped cruising")
            self.encB(5)
        #returns robot to nav method

    def open_house(self):
        """Cute demo used for open house"""
        while True:

            self.dist()
            if self.dist() < 10:
            #gets scared and needs space like a true introvert
                self.encB(10)
                print("\n\n\n Woah! I need some space (-.-) \n\n\n")
                time.sleep(2.5)
                self.encF(10)
                time.sleep(.2)

            elif self.dist() < 30:
                #half turn, flip midway then rest of the turn
                self.encF(1)
                print ("\n\n\n Watch this! \n\n\n")
                time.sleep(.2)
                self.encL(8)
                self.set_speed(100,200)
                self.encB(42)
                self.set_speed(200,200)
                self.encR(15)
                self.set_speed(200,100)
                self.encF(42)
                self.encL(8)
                self.set_speed(150,150)
                time.sleep(.2)
            else:
                #looks for people to run from
                for x in range (160,0,-20):
                    self.servo(x)
                    time.sleep(.2)
                self.servo(self.MIDPOINT)
                time.sleep(1)

    def skill_test(self):
        """demonstrates that I actually know what I'm doing in class"""
        choice= raw_input("Left/Right or Turn Until Clear?")

        if "l" in choice:

            self.wide_scan(count=2)
            left_dist= 0
            right_dist= 0
            for ang in range (146,86,-1):
                if self.scan[ang]:
                    left_dist += self.scan[ang]
            for ang in range (84,24,-1):
                if self.scan[ang]:
                    right_dist += self.scan[ang]

            if abs(left_dist - right_dist) <= 600:
                print ("\n I can't tell which direction \n")
            elif left_dist > right_dist:
                print ("\n Object on right side \n")
                self.encL(8)
            elif right_dist > left_dist:
                print ("\n Object on left side \n")
                self.encR(8)
        else:
            #turns until no object directly ahead
            while not self.is_clear():
                self.encL(3)



def stop(self):
        """spams stop command and moves servo to midpoint"""
        print('All stop.')
        for x in range(3):
            stop()
        self.servo(self.MIDPOINT)
        logging.info("STOP COMMAND RECEIVED")

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
