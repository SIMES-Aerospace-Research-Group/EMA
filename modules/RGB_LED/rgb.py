import time, sys
import RPi.GPIO as GPIO

redPin = 12
greenPin = 19
bluePin = 13


GPIO.setwarnings(False)
GPIO.cleanup()

def greenOn():
    GPIO.setmode(GPIO.BCM)
	GPIO.setup(greenPin, GPIO.OUT)

    while True:
        GPIO.output(greenPin, True)
        time.sleep(1)
        GPIO.output(greenPin, False)
        time.sleep(1)

greenOn()