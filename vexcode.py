#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT7, False)
right_drive_smart = Motor(Ports.PORT9, True)
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 259.34, 320, 40, MM, 1)
motor_4 = Motor(Ports.PORT4, False)
motor_3 = Motor(Ports.PORT3, False)


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

vexcode_initial_drivetrain_calibration_completed = False
def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    global vexcode_initial_drivetrain_calibration_completed
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    vexcode_initial_drivetrain_calibration_completed = True
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


# Calibrate the Drivetrain
calibrate_drivetrain()

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
    # block 1 #
    drivetrain.drive_for(FORWARD, 600, MM)
    motor_3.spin(FORWARD)
    motor_3.set_stopping(HOLD)
    drivetrain.drive_for(FORWARD, 10, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1220, MM)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    # block 2 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 930, MM)
    motor_3.spin(FORWARD)
    drivetrain.drive_for(FORWARD, 10, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1250, MM)
    motor_2.spin_for(FORWARD, 100, DEGREES)
    motor_2.set_stopping(HOLD)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_2.spin_for(REVERSE, 100, DEGREES)
    # block 3 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 980, MM)
    motor_3.spin(FORWARD)
    drivetrain.drive_for(FORWARD, 10, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1280, MM)
    motor_2.spin_for(FORWARD, 190, DEGREES)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_2.spin_for(REVERSE, 190, DEGREES)
      # block 4 #
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1010, MM)
    motor_3.spin(FORWARD)
    drivetrain.drive_for(FORWARD, 10, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1310, MM)
    motor_2.spin_for(FORWARD, 280, DEGREES)
    motor_3.spin(REVERSE)
    drivetrain.drive_for(REVERSE, 300, MM)
    motor_2.spin_for(REVERSE, 280, DEGREES)

