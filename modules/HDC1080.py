# Importing libraries
import SDL_Pi_HDC1080
import sys

# Setting main path to HDC1080
sys.path.append('./SDL_Pi_HDC1080_Python3')
hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

def HDCtemp(roundto):
	temperature = round(hdc1080.readTemperature(), roundto)
	return temperature

def HDChum(roundto):
	humidity = round(hdc1080.readHumidity(), roundto)
	return humidity
