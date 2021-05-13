from os import system as install
from time import *

def installer():
    EMA = 'https://github.com/Rodrigo-Flores/EMA'
    packages = ['sudo apt update && sudo apt upgrade',
    'sudo apt install software-properties-common -y',
    'sudo apt-get install git-all -y',
    'sudo apt install python3-pip -y',
    f'sudo rm -rf EMA && git clone {EMA}', 
    'pip3 install -r EMA/modules/setups/requirements.txt --force',
    'sudo apt-get update',
    'sudo sh EMA/modules/setups/lcd/install.sh'
    ]

    for package in packages:
        install(package)

def main():
    confirm = input('''
    Los siguientes packetes serán instalados:\n
        update and upgrade system, git-all, python 3, pip 3, EMA Official repository,
        requirement.txt (wiringpi==2.60.1-numpy==1.20.2-config==0.5.0.post0-spidev==3.5
        RPi.GPIO==0.7.0-smbus==1.1.post2-Adafruit_GPIO==1.0.3), lcd-calibration
    ¿Deseas continuar? [S/n] ''')
    if confirm == 'S':
        installer()
    else:
        exit()    
