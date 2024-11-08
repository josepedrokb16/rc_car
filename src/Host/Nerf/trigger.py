from PCA9685_Abstraction.servo_driver import ServoDriver, Channel, Axis
import asyncio
import time

class Trigger():
    OPEN = int((9/100)*ServoDriver.ALWAYS_ON_VALUE)
    CLOSED = int((15/100)*ServoDriver.ALWAYS_ON_VALUE)

    def __init__(self):
        self._servo_driver = ServoDriver()

    async def fire(self):
        self._servo_driver.set_pwm(channel=Channel.TRIGGER.value, value=Trigger.OPEN)
        await asyncio.sleep(1)
        self._servo_driver.set_pwm(channel=Channel.TRIGGER.value, value=Trigger.CLOSED)
