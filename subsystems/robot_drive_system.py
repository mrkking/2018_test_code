from wpilib.command import Subsystem, PIDSubsystem

from commands.drive_by_controller import drive_by_controller
from robot import robot


class robot_drive_system(PIDSubsystem):

    robot_drive = robot.robot_map.robot_drive
    pidoutput = 0.0

    def initDefaultCommand(self):
        drive_by_controller()


    def drive(self, lspeed, rspeed):
        self.robot_drive.tankDrive(lspeed, rspeed)

    def __init__(self):
        super().__init__(3.0,0.0,0.0)
        self.getPIDController().setAbsoluteTolerance(2.0)
        self.getPIDController().setOutputRange(-1.0, 1.0)

    def returnPIDInput(self):
        pass

    def drivedistance(self, dist):
        self.getPIDController().setP(3.0)
        self.getPIDController().setContinuous(False)
        self.getPIDController().setSetpoint(dist)
        self.getPIDController().enable()

    def rotateToAngle(self, angle):
        self.getPIDController().setInputRange(-180, 180)
        self.getPIDController().setContinuous(True)
        self.getPIDController().setSetpoint(angle)
        self.getPIDController().enable()

    def enddDrive(self):
        self.getPIDController().disable()
        self.robot_drive.tankDrive(0.0, 0.0)

    def usePIDOutput(self, output):
        self.pidoutput = output

