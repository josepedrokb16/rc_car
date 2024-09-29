from PCA9685_Abstraction.servo_driver import ServoDriver, Channel, Axis


class DrivingController:
    MAX_SPEED = 0.1
    MIN_SPEED = 0
    MAX_TURN = 0.14
    MIN_TURN = 0.04
    ALWAYS_ON_VALUE = 0xFFFF

    def __init__(self):
        self.servo_driver = ServoDriver()

    def move(self, event):
        axis = event['axis']
        value = event['value']
        if axis == Axis.LEFT_JOYSTICK_HORIZONTAL.value:
            mapped_value = ServoDriver.map_joystick_to_pca9685_input(value,
                                                                    self.MIN_TURN,
                                                                    self.MAX_TURN)
            self.servo_driver.set_pwm(Channel.STEER.value, mapped_value)
        elif axis in [Axis.RIGHT_TRIGGER.value, Axis.LEFT_TRIGGER.value]:
            mapped_value = ServoDriver.map_joystick_to_pca9685_input(value,
                                                                    self.MIN_SPEED,
                                                                    self.MAX_SPEED)
            self.set_speed(axis, mapped_value)

    def set_speed(self, axis, value):
        if axis == Axis.RIGHT_TRIGGER.value:
            self.servo_driver.set_pwm(Channel.DRIVER_PWM_1.value, value)
            self.servo_driver.set_pwm(Channel.DRIVER_PWM_2.value, 0)
        elif axis == Axis.LEFT_TRIGGER.value:
            self.servo_driver.set_pwm(Channel.DRIVER_PWM_1.value, 0)
            self.servo_driver.set_pwm(Channel.DRIVER_PWM_2.value, value)
