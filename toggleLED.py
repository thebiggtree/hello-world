import RPi.GPIO as GPIO
import time
#configure Pi to use BCM pin names instead of pin positions
GPIO.setmode(GPIO.BCM)

led_pin = 18
switch_pin = 26
on = False;

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

def toggle_led():
    global on
    on = not(on)
    GPIO.output(led_pin, on)

try:
        while True:
            if GPIO.input(switch_pin) == False:
                print("Button Pressed")
                toggle_led()
                time.sleep(1)

finally:
    print("Cleaning up")
    GPIO.cleanup()


    
