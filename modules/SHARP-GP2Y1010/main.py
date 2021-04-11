from sharpPM10 import sharpPM10
from mcp3008 import MCP3008

sharp_pin = 21
sharp_channel = 1

ADC = MCP3008()

sharpPM10 = sharpPM10(led_pin=sharp_pin, pm10_pin=sharp_channel, adc=ADC)

dust_density = sharpPM10.read()

print(dust_density)
