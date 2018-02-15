from wpilib.command import Command

from robot import robot


class drive_by_distance(Command):

    def __init__(self, name=None, timeout=None):
        super().__init__(name, timeout)
        self.requires(robot.robot_drive)
        self.robot_drive = robot.robot_drive

    def initialize(self):
        pass

    def execute(self):
        self.robot_drive.drivedistance(25)

    def isFinished(self):
        return self.robot_drive.onTarget()

    def end(self):
        self.robot_drive.enddDrive()

    def interrupted(self):
        self.robot_drive.enddDrive()
