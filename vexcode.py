# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode EXP Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
myVariable = 0

def when_started1():
    global myVariable

    # block 1 #
    drivetrain.drive_for(FORWARD, 600, MM)
    motor_3.spin(FORWARD)
    motor_3.set_stopping(HOLD)
    wait(1, SECONDS)

    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1200, MM)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    # block 2 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 930, MM)
    motor_3.spin(FORWARD)
    wait(1, SECONDS)

    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1230, MM)
    motor_2.spin_for(FORWARD, 100, DEGREES)
    motor_2.set_stopping(HOLD)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_2.spin_for(REVERSE, 100, DEGREES)
    # block 3 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 960, MM)
    motor_3.spin(FORWARD)
    wait(1, SECONDS)

    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1260, MM)
    motor_2.spin_for(FORWARD, 190, DEGREES)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_2.spin_for(REVERSE, 190, DEGREES)
    # block 4 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 990, MM)
    motor_3.spin(FORWARD)
    wait(1, SECONDS)

    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1290, MM)
    motor_2.spin_for(FORWARD, 280, DEGREES)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_2.spin_for(REVERSE, 280, DEGREES)

