import wiringpi as wipi
from time import *
import wiringpi
import config
import spidev
import sys

from modules.MCP_3008 import mcp3008
from modules.SHARP_PM10 import sharpPM10
from modules.LCD_1602 import Base, Scroll, BacklightOn, BacklightOff, clear, 

#from modules.HDC_1080 import HDCtemp, HDChum

# from modules.RGB_LED import ...

sharp_pin = 21
sharp_channel = 1
ADC = mcp3008(0, 0) # CE0
sharpPM10 = sharpPM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)
dust_density = sharpPM10.read()

print('Testing Base text!')
sleep(1)
Base('Heeyy ...', 1)
Base('k pasa chavales!', 2)
sleep(3)
clear()

print('Testing Scroll text!')
sleep(1)
Scroll('May the force be with you young padawan !!', 1)
sleep(3)

print('Testing Backlight text!')
sleep(1)
for i in range(2):
    BacklightOn()
    sleep(.5)
    BacklightOff()
    sleep(.5)
Base('Hello there', 1)
BacklightOn()
sleep(1)
BacklightOff()
Base('General Kenobi..', 2)
sleep(1)
exit()

# degree_symbol = u"\u00b0"

## Pines GRPIO setup


# Ground = 9

## Setup of modules
# initLCD()



"""
yellowOn() # Pin turned to yellow
for i in (30): # 0.2 seconds * 30 = 6 seconds
    printLCD('[ ? ] Recibiendo datos .  ')
    sleep(.2)
    printLCD('[ ? ] Recibiendo datos .. ')
    sleep(.2)
    printLCD('[ ? ] Recibiendo datos ...')
    sleep(.2)
yellowOff() # Turn off the yellow led

greenOn() # ADDING RGB LED ... CHECK ADAFRUIT RGB DOCUMENTATION
printLCD("[ ok ] Cargando datos ...") # Printing on display
sleep(2)
"""

"""
while True:
    try:
        # Printing out the display
        printLCD(
            (f"Hum: {HDCtemp(2)}"), # Temperature
            (f"Tem: {HDChum(2)}\n"), # Humidity
            (f"Polvo: {sharpPM10.read()}") # Dust density
        )
        sleep(1)

    except: # If something of above fail
        printLCD('[ ! ] PROCESO FALLIDO')
        redOn()
        sleep(3)
        turnOff(redPin)
        turnOff(greenPin)
        turnOff(bluePin)
"""

"""
if dust < supIdealValue: # Ideal case
    greenon()

elif infRegularValue <= dust < supRegularValue: # Regular case
    yellowOn()

else: # Worst case
    redOn()

|| [(0%) ----good---- ](30%)[ ----regular---- ](70%)[ ----bad---- (100%)] ||


"""

greenOn()

print(HDCtemp(2))
print(HDChum(2))
print(sharpPM10.read())
