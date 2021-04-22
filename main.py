## Importing system libraries
from numpy import median
import wiringpi as wipi
from time import *
import wiringpi
import config
import spidev
import sys

## Importing Classes and Methods from local files
from modules import SHARPPM10
from modules import MCP3008
from modules import HDC1080
from modules import LCD1602
from modules import RGB_LED

# degree_symbol = u"\u00b0"

## Pines GRPIO setup
sharp_pin = 21
sharp_channel = 1

redPin = 11
greenPin = 13
bluePin = 15
# Ground = 9

## Setup of modules
initLCD()

# ADD LED ... CHECK ADAFRUIT RGB DOCUMENTATION
blink(redPin)
blink(greenPin)
blink(bluePin)

ADC = MCP3008(0, 0) # CE0

sharpPM10 = sharpPM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)


yellowOn()
limit = 30
print('\t[ ? ] Tomando datos ...')

"""
yellowOn() # Pin turned to yellow
for i in (30): # 0.2 seconds * 30 = 6 seconds
    printLCD('[ ? ] Tomando datos .  ')
    sleep(.2)
    printLCD('[ ? ] Tomando datos .. ')
    sleep(.2)
    printLCD('[ ? ] Tomando datos ...')
    sleep(.2)
yellowOff() # Turn off the yellow led

printLCD("[ ok ]") # Printing on display

greenOn() # ADDING RGB LED ... CHECK ADAFRUIT RGB DOCUMENTATION

"""

while True:
    try:
        # Printing out the display
        printLCD(
            (f"Hum: {HDCtemp(2)}"), # Temperature
            (f"Tem: {HDChum(2)}\n"), # Humidity
            (f"Polvo: {sharpPM10.read()}) # Dust density
        )
        sleep(3)
    except:
        printLCD('Process Unsuccessful')
        sleep(3)
        turnOff(redPin)
        turnOff(greenPin)
        turnOff(bluePin)
