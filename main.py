from modules.MCP_3008 import mcp3008
from modules.SHARP_PM10 import sharpPM10

ADC = mcp3008(0, 0) # CE0
sharpPM10 = sharpPM10(led_pin=21, pm10_pin=1, adc=ADC) 

print(f'MCP read_output          : {ADC.read()}')
print(f'SHARP output read        : {sharpPM10.read()}')
print(f'SHARP output readSequence: {sharpPM10.readSequence()}')
