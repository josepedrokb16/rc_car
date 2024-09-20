import board
from adafruit_pca9685 import PCA9685
import time


class CamGimbal:
    MAX_PITCH = 0.03
    MIN_PITCH = 0.09

    MIN_YAW = 0.15
    MAX_YAW = 0.06
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
        if axis == 2:
            mapped_value = self.map_joystick_to_pca9685_input(value, self.MIN_YAW, self.MAX_YAW)
            self.turn_yaw(mapped_value)
        elif axis == 3:
            mapped_value = self.map_joystick_to_pca9685_input(value, self.MIN_PITCH, self.MAX_PITCH)
            self.turn_pitch(mapped_value)

    def turn_pitch(self, value):
        self.pca.channels[4].duty_cycle = value

    def turn_yaw(self, value):
        self.pca.channels[5].duty_cycle = value

if __name__ == "__main__":
    cg = CamGimbal()
    cg.move_test()

