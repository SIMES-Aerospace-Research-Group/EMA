from Adafruit_CharLCD import Adafruit_CharLCD
# import Adafruit_CharLCD
from time import *

def initLCD():
    # Setting the main class
    lcd = Adafruit_CharLCD()

    # Using "clear()" method, to clean the display
    lcd.clear()

    # Setting the message who will be displayed
    lcd.message("[ ! ] Inicializando dispositivo...")
    sleep(3)

def printLCD(msg):
    lcd.message(msg)
    lcd.clear()
    GPIO.cleanup()
