import sys

# Setting main path to HDC1080
sys.path.append('./drivers/SDL_Pi_HDC1080_Python3')
hdc1080 = SDL_Pi_HDC1080()

# Getting temperature
def HDCtemp(roundto):
	temperature = round(hdc1080.readTemperature(), roundto)
	return temperature

# Getting humidity
def HDChum(roundto):
	humidity = round(hdc1080.readHumidity(), roundto)
	return humidity

print(HDChum(2))
print(HDCtemp(2))
