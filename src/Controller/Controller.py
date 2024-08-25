import board
from adafruit_pca9685 import PCA9685

MAX_SPEED = 0.5
MIN_SPEED = 0
MAX_TURN = 0.14
MIN_TURN = 0.04


class Controller:
    def __init__(self, logger):
        self.i2c = board.I2C()
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 60
        self.logger = logger

    def map_value_to_range(self, variable, min_val, max_val):
        return int((min_val + ((variable + 1) / 2) * (max_val - min_val))*0xFFFF)

    def move(self, event):
        axis = event['axis']
        self.logger.info(f"received event in controller: {event}")
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
        self.pca.channels[1].duty_cycle = value
        self.pca.channels[2].duty_cycle = 0

    def backwards(self, value):
        self.pca.channels[1].duty_cycle = 0
        self.pca.channels[2].duty_cycle = value

    def turn(self, value):
        self.pca.channels[0].duty_cycle = value
