from time import *
import sys
from os import *

confirm = input('''
Los siguientes packetes serán instalados:\n
    update and upgrade system, git-all, python 3, pip 3, EMA Official repository,
    requirement.txt (wiringpi==2.60.1-numpy==1.20.2-config==0.5.0.post0-spidev==3.5
    RPi.GPIO==0.7.0-smbus==1.1.post2-Adafruit_GPIO==1.0.3), lcd-calibration
 ¿Deseas continuar? [S/n] 
 ''')

EMA = 'https://github.com/Rodrigo-Flores/EMA'
install = ['sudo apt update && sudo apt upgrade',
    'sudo apt install software-properties-common -y',
    'sudo apt-get install git-all -y',
    'sudo apt install python3-pip -y',
    f'sudo rm -rf EMA && git clone {EMA}', 
    'pip3 install -r EMA/requirements.txt --force',
    'sudo apt-get update',
    'sudo sh EMA/modules/drivers/lcd/install.sh'
    ]

for package in install:
    system(package)


The following packages will be installed:
  kicad kicad-demos kicad-footprints kicad-libraries kicad-symbols kicad-templates libfreeimage3
  libglew2.1 libjxr0 libngspice0 libocct-data-exchange-7.4 libocct-foundation-7.4
  libocct-modeling-algorithms-7.4 libocct-modeling-data-7.4 libocct-ocaf-7.4
  libocct-visualization-7.4 libtbb2 xsltproc
Do you want to continue? [Y/n] 
