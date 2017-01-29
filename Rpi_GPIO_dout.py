import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



class Rpi_GPIO_dout:
    def __init__(self, BCM_pin, on):
        self.BCM_pin = BCM_pin
        self.on = on
        GPIO.setup(BCM_pin, GPIO.out)



    def toggle():
        self.on = not(self.on)
        GPIO.output(self.BCM_pin, on)

    
    def set_on():
        self.on = True
        GPIO.output(self.BCM_pin, on)

    def set_off():
        self.on = False
        GPIO.output(self.BCM_pin, on)
    
