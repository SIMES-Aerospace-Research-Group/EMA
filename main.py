## Importing system libraries
# from numpy import median
import wiringpi as wipi
from time import *
import wiringpi
import config
import spidev
import sys

## Importing Classes and Methods from local files
#from modules.MCP_3008 import MCP3008.open, MCP3008.read, MCP3008.close
from modules.MCP_3008 import mcp3008
from modules.SHARP_PM10 import sharpPM10

#from modules.LCD_1602 import Base, Scroll, Backlight
#from modules.HDC_1080 import HDCtemp, HDChum
# sys.path.append('./MCP_3008_Python3')
# sys.path.append('./SHARP_PM10_Python3')

ADC = MCP_3008.MCP_3008(0, 0) # CE0
sharp_pin = 21
sharp_channel = 1
sharpPM10 = sharpPM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)

print(sharpPM10.read())
# sharpm10 = SHARP_PM10.SHARP_PM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)
# print(sharpm10.read())

exit()



# from modules.RGB_LED import ...

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
