from Adafruit_CharLCD import Adafruit_CharLCD
from time import *

def initLCD(start):
    # Setting the main class
    lcd = Adafruit_CharLCD()

    # Using "clear()" method, to clean the display
    lcd.clear()

    # Setting the message who will be displayed
    lcd.message("[ ! ] Welcome to Air Quality Device!")

    while start:
        try:
            print("Testing LCD\n")

            mssg = "Temp: 25.5° C\nHume: 40 %" # This is just an example

            lcd.clear()
            return lcd.message(mssg)

        except KeyboardInterrupt:
            lcd.clear()
            print("Exiting...")
            GPIO.cleanup()
            start = False
