from __future__ import division
from Adafruit_PCA9685 import PCA9685

MAX_SPEED = 2000
MIN_SPEED = 0
MAX_TURN = 600
MIN_TURN = 150


class Controller:
    def __init__(self):
        self.pwm = PCA9685()
        self.pwm.set_pwm_freq(60)

    def map_value_to_range(self, variable, min_val, max_val):
        return int(min_val + ((variable + 1) / 2) * (max_val - min_val))

    def move(self, event):
        axis = event['axis']
        if axis == 0:
            mapped_value = self.map_value_to_range(event["value"], MIN_TURN, MAX_TURN)
            self.turn(mapped_value)
        elif axis == 5:
            mapped_value = self.map_value_to_range(event["value"], MIN_SPEED, MAX_SPEED)
            self.forwards(mapped_value)
        elif axis == 4:
            mapped_value = self.map_value_to_range(event["value"], MIN_SPEED, MAX_SPEED)
            self.backwards(mapped_value)

    def forwards(self, value):
        self.pwm.set_pwm(2, 0, 0)
        self.pwm.set_pwm(1, 0, value)

    def backwards(self, value):
        self.pwm.set_pwm(2, 0, value)
        self.pwm.set_pwm(1, 0, 0)

    def turn(self, value):
        self.pwm.set_pwm(0, 0, value)
