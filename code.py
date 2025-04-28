#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()


# Wait for sensor(s) to fully initialize
wait(100, MSEC)

# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 

# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration
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
    drivetrain.set_drive_velocity(70, PERCENT)
    motor_4.set_stopping(HOLD)
    motor_3.set_stopping(HOLD)
    # block 1 #
    drivetrain.drive_for(FORWARD, 600, MM)
    motor_4.spin(FORWARD)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1200, MM)
    motor_4.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    # block 2 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 930, MM)
    motor_4.spin(FORWARD)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1230, MM)
    motor_3.spin_for(FORWARD, 100, DEGREES)
    motor_4.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_3.spin_for(REVERSE, 100, DEGREES)
    # block 4 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 960, MM)
        motor_4.spin(FORWARD)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1260, MM)
    motor_3.spin_for(FORWARD, 190, DEGREES)
    motor_4.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_3.spin_for(REVERSE, 190, DEGREES)
      # block 5 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 990, MM)
        motor_4.spin(FORWARD)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1290, MM)
    motor_3.spin_for(FORWARD, 280, DEGREES)
    motor_4.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_3.spin_for(REVERSE, 280, DEGREES)


when_started1()
