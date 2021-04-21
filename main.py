## Importing system libraries
import sys
import wiringpi
import spidev
from numpy import median
import wiringpi as wipi
import config
from time import *

## Importing Classes and Methods from local files
from modules import MCP3008
from modules import HDC1080
from modules import LCD1602
from modules import RGB_LED
from modules import SHARPPM10

# degree_symbol = u"\u00b0"

## Pines setup
sharp_pin = 21
sharp_channel = 1

redPin = 11
greenPin = 13
bluePin = 15

## Setup of modules
initLCD()

# ADD LED ... CHECK ADAFRUIT RGB DOCUMENTATION
blink(redPin)
blink(greenPin)
blink(bluePin)

ADC = MCP3008(0, 0) # CE0

sharpPM10 = sharpPM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)

yellowOn() # Pin turned to yellow
for i in (30): # 0.2 seconds * 30 = 6 seconds
    printLCD('[ ok ] Tomando datos .  ')
    sleep(.2)
    printLCD('[ ok ] Tomando datos .. ')
    sleep(.2)
    printLCD('[ ok ] Tomando datos ...')
    sleep(.2)
yellowOff() # Turn off the yellow led

try:
    # Printing on display
    lcd.lcd_print("Success")

    # ADDING RGB LED ... CHECK ADAFRUIT RGB DOCUMENTATION
    greenOn()

    dust_density = sharpPM10.read() # Reading dust density with sharpPM10

    # Printing out the data
    printLCD(f'{HDCtemp(2)}  {HDChum(2)}')

    # Printing on display
    printLCD([
        (f"Hum: {humidity}"),
        (f"Tem: {temperature}"),
        (f"Polvo: {dust_density}")
    ])

except:
    lcd.lcd_print(['Process Unsuccessful'])
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)
