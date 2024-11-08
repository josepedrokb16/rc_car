import board
from adafruit_pca9685 import PCA9685
from enum import Enum


class Axis(Enum):
    LEFT_JOYSTICK_HORIZONTAL = 0
    LEFT_JOYSTICK_VERTICAL = 1
    RIGHT_JOYSTICK_HORIZONTAL = 2
    RIGHT_JOYSTICK_VERTICAL = 3
    LEFT_TRIGGER = 4
    RIGHT_TRIGGER = 5


class Channel(Enum):
    STEER = 0
    DRIVER_PWM_1 = 1
    DRIVER_PWM_2 = 2
    PITCH = 4
    YAW = 5
    TRIGGER = 12


class ServoDriver:
    ALWAYS_ON_VALUE = 0xFFFF

    def __init__(self):
        self.i2c = board.I2C()
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 60

    @staticmethod
    def map_joystick_to_pca9685_input(joystick_input, min_duty_cycle, max_duty_cycle):
        """
        Input from the joystick very between [-1, 1]
        """
        duty_cycle = min_duty_cycle + ((joystick_input + 1) / 2) * (max_duty_cycle - min_duty_cycle)
        return int(ServoDriver.ALWAYS_ON_VALUE*duty_cycle)

    def set_pwm(self, channel: int, value: int):
        self.pca.channels[channel].duty_cycle = value
