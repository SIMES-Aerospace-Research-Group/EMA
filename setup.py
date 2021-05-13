from time import *
import sys
from os import *

confirm = input('''
The following packages will be installed:
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
After this operation, 324 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
