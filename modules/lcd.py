from Adafruit_CharLCD import Adafruit_CharLCD
from time import *
import os

os.system("clear")

# Setting the main class
lcd = Adafruit_CharLCD()

# Using "clear()" method, to clean the display
lcd.clear()

# Setting the message who will be displayed
lcd.message("Welcome to Air Quality Device")

# The condition to while loop
x = 0

while x != 1:
    try:
        print("Testing LCD\n")

        string = "Temp: 25.5° C\nHume: 40 %" # This is just an example

        lcd.clear()
        lcd.message(string)

    except KeyboardInterrupt:
        lcd.clear()
        print("Exiting...")
        GPIO.cleanup()
        x = 1
