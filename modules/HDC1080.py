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
hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

def HDCtemp(roundto):
	temperature = round(hdc1080.readTemperature(), roundto)
	return temperature

def HDChum(roundto):
	humidity = round(hdc1080.readHumidity(), roundto)
	return humidity
