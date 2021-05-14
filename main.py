from modules.MCP_3008 import mcp3008
from modules.SHARP_PM10 import sharpPM10
from modules.LCD_1602 import Base, Scroll, BacklightOn, BacklightOff, clear
from modules.HDC_1080 import HDCtemp, HDChum
# from modules.RGB_LED import ...

from time import *
import random

ADC = mcp3008(0, 0) # CE0
sharpPM10 = sharpPM10(led_pin=21, pm10_pin=1, adc=ADC)

def data():
    BacklightOn()

    clear()
    Base(f'PM2.5: {sharpPM10.read()}', 1)
    Base(f'PM10: {sharpPM10.read()}', 2)

    sleep(2)
    BacklightOff()
    clear()
    BacklightOn()
    Base(f'Temp: {HDCtemp(3)} {chr(223)}C', 1)
    Base(f'Hume: {HDChum(3)} %', 2)
    sleep(2)

def init():
    clear()
    BacklightOn()
    for i in range(4):
        BacklightOff()
        sleep(.05)
        BacklightOn()
        sleep(.05)
    
    Scroll('Estacion de Monitoreo', 1)
    Scroll("            Ambiental", 2)
    clear()
    sleep(2)
    Base('      EMA       ', 1)
    sleep(2)
    clear()

    for i in range(4):
        BacklightOff()
        sleep(.05)
        BacklightOn()
        sleep(.05)

    Scroll('Leyendo datos de sensores ...', 1)

def main():
    init()
    clear()
    try:
        while True:
            data()
    except KeyboardInterrupt:
        clear()
        print('\n')
        exit()
if __name__ == '__main__':
    main()



'''

3000 +     = VERY POOR
1050-3000  = POOR
300-1050   = FAIR
150-300    = GOOD
75-150     = VERY GOOD
0-75       = EXCELLENT

'''

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