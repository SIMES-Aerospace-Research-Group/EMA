# Importing libraries
import sys
from colorama import Fore, Back, Style
import SDL_Pi_HDC1080
from datetime import *
import time
import csv
import sys
import os

# Setting main path to HDC1080
sys.path.append('./SDL_Pi_HDC1080_Python3')

# Cleanning console
os.system('clear')

hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

"""
# Opening csv file and writing the headers
with open('HDC-1080.csv', 'w', newline='') as file:
	write = csv.writer(file)
	write.writerow(['Time', 'Temperature(C)', 'Humidity'])
"""

"""
# Setting counter in 0 value
HH = 0
MM = 0
SS = 0
"""

# Main loop
while True:

"""
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	if SS == 60:
		MM += 1
		SS = 0
	elif MM == 60:
		SS = 0
		HH += 1
		MM = 0
"""

	# Getting temperature and humidity from methods
	temperature = round(hdc1080.readTemperature(),1)
	humidity = round(hdc1080.readHumidity(),1)

"""
	with open('HDC-1080.csv', 'a+', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([current_time, hdc1080.readTemperature(), hdc1080.readHumidity()])
"""

"""
	# Printing output and coloring it
	print (Fore.RED + "|-------" + Fore.WHITE + f"{HH}:{MM}:{SS}" + Fore.RED + "-------|")
	print (Fore.WHITE + f'Temperature = {temperature} C°')
	print (Fore.WHITE + f'Humidity = {humidity} %')
	print (Fore.RED + "|----------------------|\n\n" + Style.RESET_ALL)
"""

	# Printing without color
	print (Fore.WHITE + f'Temperature = {temperature} C°')
	print (Fore.WHITE + f'Humidity = {humidity} %')

	# Upping the counter
	# SS += 1
	time.sleep(1)
