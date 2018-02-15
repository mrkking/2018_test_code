from wpilib.command import Command

from robot import robot


class drive_by_controller(Command):

    def __init__(self):
        self.requires(robot.robot_drive)
        self.robot_drive = robot.robot_drive
        self.ctrl = robot.ctrl

    def initialize(self):
        super().initialize()

    def execute(self):
        self.robot_drive.drive(self.ctrl.getRawAxis(1), self.ctrl.getRawAxis(2))

    def isFinished(self):
        return super().isFinished()

    def end(self):
        super().end()

    def interrupted(self):
        super().interrupted()

