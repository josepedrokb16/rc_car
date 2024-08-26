import board
from adafruit_pca9685 import PCA9685


class MotorController:
    MAX_SPEED = 0.5
    MIN_SPEED = 0
    MAX_TURN = 0.14
    MIN_TURN = 0.04
    ALWAYS_ON_VALUE = 0xFFFF

    def __init__(self):
        self.i2c = board.I2C()
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 60

    def map_joystick_to_pca9685_input(self, joystick_input, min_duty_cycle, max_duty_cycle):
        """
        Input from the joystick very between [-1, 1]
        """
        duty_cycle = min_duty_cycle + ((joystick_input + 1) / 2) * (max_duty_cycle - min_duty_cycle)
        return int(self.ALWAYS_ON_VALUE*duty_cycle)

    def move(self, event):
        axis = event['axis']
        value = event['value']
        if axis == 0:
            mapped_value = self.map_joystick_to_pca9685_input(value, self.MIN_TURN, self.MAX_TURN)
            self.turn(mapped_value)
        elif axis in [4, 5]:
            mapped_value = self.map_joystick_to_pca9685_input(value, self.MIN_SPEED, self.MAX_SPEED)
            self.set_speed(axis, mapped_value)

    def set_speed(self, axis, value):
        if axis == 4:
            self.pca.channels[1].duty_cycle = 0
            self.pca.channels[2].duty_cycle = value
        elif axis == 5:
            self.pca.channels[1].duty_cycle = value
            self.pca.channels[2].duty_cycle = 0

    def turn(self, value):
        self.pca.channels[0].duty_cycle = value
