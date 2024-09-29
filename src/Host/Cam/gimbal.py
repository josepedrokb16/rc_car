from PCA9685_Abstraction.servo_driver import ServoDriver, Channel, Axis


class CamGimbal():
    MAX_PITCH = 0.03
    MIN_PITCH = 0.09
    MIN_YAW = 0.15
    MAX_YAW = 0.06

    def __init__(self):
        self._servo_driver = ServoDriver()

    def move(self, event):
        axis = event['axis']
        value = event['value']
        if axis == Axis.RIGHT_JOYSTICK_HORIZONTAL.value:
            mapped_value = ServoDriver.map_joystick_to_pca9685_input(value, self.MIN_YAW, self.MAX_YAW)
            self._servo_driver.set_pwm(channel=Channel.YAW.value, value=mapped_value)
        elif axis == Axis.RIGHT_JOYSTICK_VERTICAL.value:
            mapped_value = ServoDriver.map_joystick_to_pca9685_input(value, self.MIN_PITCH, self.MAX_PITCH)
            self._servo_driver.set_pwm(channel=Channel.PITCH.value, value=mapped_value)
