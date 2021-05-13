import time, sys
import RPi.GPIO as GPIO

redPin = 12
greenPin = 19
bluePin = 13


GPIO.setwarnings(False)
GPIO.cleanup()

def greenOn():
    GPIO.setmode(GPIO.BOARD)
	GPIO.setup(greenPin, GPIO.OUT)

    while True:
        GPIO.output(7, True)
        time.sleep(1)
        GPIO.output(7, False)
        time.sleep(1)

greenOn()