from modules.MCP_3008 import mcp3008
from modules.SHARP_PM10 import sharpPM10
from modules.LCD_1602 import Base, Scroll, BacklightOn, BacklightOff, clear
from modules.HDC_1080 import HDCtemp, HDChum
# from modules.RGB_LED import ...

from time import *

def init():
    clear()
    for i in range(4):
        BacklightOff()
        sleep(.4)
        BacklightOn()
        sleep(.4)
    
    Scroll('Estación de Monitoreo Ambiental', 2)
    sleep(.5)
    clear()
    Base('      EMA       ', 1)
    sleep(2)
    clear()

    for i in range(4):
        BacklightOff()
        sleep(.3)
        BacklightOn()
        sleep(.3)

    Scroll('Leyendo datos de sensores ... ')

def data():
    #  Preparando configuraciones de sensores
    ADC = mcp3008(0, 0) # CE0
    sharpPM10 = sharpPM10(led_pin=21, pm10_pin=1, adc=ADC)

    #  Enviando datos al display LCD
    # Base('----------------', 1)
    clear()
    Base(f'PM2.5: {sharpPM10.read()}', 1)
    Base(f'PM10: {sharpPM10.read()}, 2')

    BacklightOff()
    sleep(.5)
    clear()
    BacklightOn()

    Base(f'Temp: {HDCtemp(1)} C°', 1)
    Base(f'Hume: {HDChum}%', 2)

def main():
    init()
    clear()
    while True:
        data()

if __name__ == '__main__':
    main()












# print('Testing Base text!')
# sleep(1)
# Base('Heeyy ...', 1)
# Base('k pasa chavales!', 2)
# sleep(3)
# clear()

# print('Testing Scroll text!')
# sleep(1)
# Scroll('May the force be with you young padawan !!', 1)
# sleep(3)
# clear()

# print('Testing Backlight text!')
# sleep(1)
# for i in range(2):
#     BacklightOn()
#     sleep(.5)
#     BacklightOff()
#     sleep(.5)
# Base('Hello there', 1)
# BacklightOn()
# sleep(1)
# BacklightOff()
# Base('General Kenobi..', 2)
# sleep(1)

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