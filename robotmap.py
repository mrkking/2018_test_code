from ctre.talonsrx import TalonSRX
from wpilib import SpeedControllerGroup
from wpilib.drive import DifferentialDrive


class robotmap:



    def __init__(self):
        left_rear_m = TalonSRX(1)
        self.left_front_m = TalonSRX(2)
        self.right_front_m = TalonSRX(0)
        right_rear_m = TalonSRX(2)

        left_drive = SpeedControllerGroup(self.left_front_m, left_rear_m)
        right_drive = SpeedControllerGroup(self.right_front_m, right_rear_m)

        self.robot_drive = DifferentialDrive(left_drive,right_drive)

