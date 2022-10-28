#!/bin/bash

sudo python3 /home/administrator/arm/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --port /dev/ttyACM0  --appfpga top.bin --m4app blink.bin --mode m4-fpga --reset


pdflatex arm.tex

zathura arm.pdf

#termux-open arm.tex
