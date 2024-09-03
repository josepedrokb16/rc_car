import board
from adafruit_pca9685 import PCA9685
import time

ALWAYS_ON_VALUE = 0xFFFF

i2c = board.I2C()
pca = PCA9685(i2c)
pca.frequency = 60

for i in range(100):
    current_duty_cycle = (i/100)
    print(f"Duty Cycle: {current_duty_cycle}")
    pca.channels[1].duty_cycle = int(current_duty_cycle*ALWAYS_ON_VALUE)
    time.sleep(1)
