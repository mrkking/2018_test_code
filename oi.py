from wpilib import Joystick
from wpilib.buttons import JoystickButton


class oi:

    ps4_ctrl = Joystick(0)

    def __init__(self):
        pass
        #example button press action
        #triangle = JoystickButton(ps4_ctrl, 3)
        #triangle.whenPressed("place command here")