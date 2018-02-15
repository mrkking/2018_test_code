import wpilib
from wpilib.command import Command

from commands.drive_by_controller import drive_by_controller
from oi import oi
from robotmap import robotmap
from subsystems.robot_drive_system import robot_drive_system


class robot(wpilib.IterativeRobot):

    robot_map = robotmap()
    robot_drive = robot_drive_system()
    ctrl = oi.ps4_ctrl

    def robotInit(self):
        self.autocommand = Command()

    def autonomousInit(self):
        super().autonomousInit()

    def teleopInit(self):
        if self.autocommand:
            self.autocommand.cancel()
        drive_by_controller()


    def testInit(self):
        super().testInit()

    def autonomousPeriodic(self):
        super().autonomousPeriodic()

    def teleopPeriodic(self):
        super().teleopPeriodic()

    def testPeriodic(self):
        super().testPeriodic()