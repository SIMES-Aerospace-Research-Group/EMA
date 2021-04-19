import sys

# Importing pip libraries
import wiringpi
import spidev
from numpy import median
import wiringpi
import Adafruit_DHT # This device read temperature and humedity. I't reallt necessary? We'll to use the HDC1080 sensor
import Adafruit_BMP.BMP085 as BMP085 # --- BMP085 ---

# Importing Classes and Methods from local files
from mcp3008 import MCP3008
from sharpPM10 import sharpPM10
import lcd_driver

import config

degree_symbol = u"\u00b0"

print('starting...')

sharp_pin = 21
sharp_channel = 1

green_led = 6
yellow_led = 13

try:
    wiringpi.wiringPiSetupGpio() 
    wiringpi.pinMode(green_led, 1)
    wiringpi.pinMode(yellow_led, 1)

    wiringpi.digitalWrite(yellow_led, 1) # power on the yellow LED
    wiringpi.digitalWrite(green_led, 1) # power on the green LED

    Adafruit_BMP085 = BMP085.BMP085() # --- BMP085 ---
    ADC = MCP3008(0, 0) # CE0
    # MQ = MQ(adc=ADC, analog_channel=mq_channel)
    sharpPM10 = sharpPM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)
    lcd = lcd_driver.lcd()
except:
    wiringpi.digitalWrite(green_led, 0) # power off the green LED

while True:
    wiringpi.digitalWrite(yellow_led, 1) # power on the yellow LED
    lcd.lcd_print(['Reading sensors...'])
    

    humidity, temp_dht = Adafruit_DHT.read_retry(dht_model, dht_pin) # (sensor_type, pin_number) # Here is the HDC1080!
    pressure = Adafruit_BMP085.read_pressure() # --- BMP085 --- !
    dust_density = sharpPM10.read()
    
    try:
        print('success')
        wiringpi.digitalWrite(yellow_led, 0) # power off the yellow LED
        
        # Print de HDC-1080
        lcd.lcd_print([
            ('Temp: {0:0.1f}C').format(temp_dht or 0),
            ('Humidity: {0:0.1f}%').format(humidity or 0)
        ])
        
    except:
        lcd.lcd_print(['Proces Unsuccessful'])
        print('Process Unsuccessful')
        wiringpi.digitalWrite(green_led, 0) # power off the green LED


